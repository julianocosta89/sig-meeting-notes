"""Tests for scraper/community.py — README parsing and slug lookup."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import scraper.community as community
from scraper.community import _cell_to_key, _parse_readme, get_meeting_notes_url

# ---------------------------------------------------------------------------
# Minimal README fixture with two SIG rows
# ---------------------------------------------------------------------------

_SAMPLE_README = """\
## Specification SIGs

| Name | Meeting Time | Meeting Notes | Slack Channel |
|------|-------------|---------------|---------------|
| Java: SDK + Instrumentation&nbsp;<a id="sig-java" href="#sig-java"><sup>🔗</sup></a> | Thursday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/java-doc-id/edit) | #otel-java |
| Go: SDK + Automatic Instrumentation&nbsp;<a id="sig-go" href="#sig-go"><sup>🔗</sup></a> | Tuesday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/go-doc-id/edit) | #otel-go |
| Semantic Conventions: Telemetry Schema&nbsp;<a id="sig-semconv" href="#sig-semconv"><sup>🔗</sup></a> | Monday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/semconv-doc-id/edit) | #otel-semconv |
| Collector: Collector, OpAMP&nbsp;<a id="sig-collector" href="#sig-collector"><sup>🔗</sup></a> | Wednesday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/collector-doc-id/edit) | #otel-collector |

## Other SIGs

| Name | Meeting Time | Meeting Notes |
|------|-------------|---------------|
| Row without a Google Doc | Monday | Some text without a link |
"""


class TestCellToKey:
    def test_simple_name(self) -> None:
        assert _cell_to_key("Go") == "go"

    def test_colon_prefix(self) -> None:
        assert _cell_to_key("Java: SDK + Instrumentation") == "java"

    def test_multi_word_prefix(self) -> None:
        assert _cell_to_key("Semantic Conventions: Telemetry Schema") == "semantic-conventions"

    def test_strips_html_tags(self) -> None:
        cell = 'Go: SDK<a id="sig-go" href="#sig-go"><sup>🔗</sup></a>'
        assert _cell_to_key(cell) == "go"

    def test_strips_nbsp_entity(self) -> None:
        assert _cell_to_key("Go&nbsp;SIG") == "go-sig"

    def test_header_row(self) -> None:
        assert _cell_to_key("Name") == "name"


class TestParseReadme:
    def test_extracts_all_rows(self) -> None:
        result = _parse_readme(_SAMPLE_README)
        assert len(result) == 4

    def test_java_url(self) -> None:
        result = _parse_readme(_SAMPLE_README)
        assert result["java"] == "https://docs.google.com/document/d/java-doc-id/edit"

    def test_go_url(self) -> None:
        result = _parse_readme(_SAMPLE_README)
        assert result["go"] == "https://docs.google.com/document/d/go-doc-id/edit"

    def test_semantic_conventions_url(self) -> None:
        result = _parse_readme(_SAMPLE_README)
        assert (
            result["semantic-conventions"]
            == "https://docs.google.com/document/d/semconv-doc-id/edit"
        )

    def test_collector_url(self) -> None:
        result = _parse_readme(_SAMPLE_README)
        assert result["collector"] == "https://docs.google.com/document/d/collector-doc-id/edit"

    def test_skips_row_without_gdoc(self) -> None:
        result = _parse_readme(_SAMPLE_README)
        # "Row without a Google Doc" has no [Google Doc](...) link
        assert not any("row" in k for k in result)

    def test_empty_readme(self) -> None:
        assert _parse_readme("") == {}

    def test_no_table_rows(self) -> None:
        assert _parse_readme("# Just a heading\n\nSome prose.") == {}


class TestGetMeetingNotesUrl:
    def setup_method(self) -> None:
        # Reset module-level cache before each test
        community._cache = None

    def _mock_load(self, readme_text: str = _SAMPLE_README) -> MagicMock:
        mock_resp = MagicMock()
        mock_resp.text = readme_text
        mock_resp.raise_for_status = MagicMock()
        return mock_resp

    def test_exact_slug_match(self) -> None:
        with patch("scraper.community.requests.get", return_value=self._mock_load()):
            url = get_meeting_notes_url("go")
        assert url == "https://docs.google.com/document/d/go-doc-id/edit"

    def test_slug_with_sig_suffix(self) -> None:
        with patch("scraper.community.requests.get", return_value=self._mock_load()):
            url = get_meeting_notes_url("Go-SIG")
        assert url == "https://docs.google.com/document/d/go-doc-id/edit"

    def test_slug_with_wg_suffix(self) -> None:
        # Collector-SIG should match 'collector' key
        with patch("scraper.community.requests.get", return_value=self._mock_load()):
            url = get_meeting_notes_url("Collector-SIG")
        assert url == "https://docs.google.com/document/d/collector-doc-id/edit"

    def test_multi_word_slug(self) -> None:
        with patch("scraper.community.requests.get", return_value=self._mock_load()):
            url = get_meeting_notes_url("Semantic-Conventions-SIG")
        assert url == "https://docs.google.com/document/d/semconv-doc-id/edit"

    def test_unknown_slug_returns_empty(self) -> None:
        with patch("scraper.community.requests.get", return_value=self._mock_load()):
            url = get_meeting_notes_url("Unknown-SIG-XYZ")
        assert url == ""

    def test_cache_is_used_on_second_call(self) -> None:
        with patch("scraper.community.requests.get", return_value=self._mock_load()) as mock_get:
            get_meeting_notes_url("go")
            get_meeting_notes_url("go")
        # requests.get should only be called once despite two lookups
        mock_get.assert_called_once()

    def test_network_error_returns_empty(self) -> None:
        with patch(
            "scraper.community.requests.get",
            side_effect=community.requests.RequestException("timeout"),
        ):
            url = get_meeting_notes_url("go")
        assert url == ""

    def test_http_error_returns_empty(self) -> None:
        mock_resp = MagicMock()
        mock_resp.raise_for_status.side_effect = community.requests.HTTPError("404")
        with patch("scraper.community.requests.get", return_value=mock_resp):
            url = get_meeting_notes_url("go")
        assert url == ""

    def test_reverse_prefix_match(self) -> None:
        """key = 'collector-sig', target = 'collector' → key.startswith(target + '-') match."""
        readme = (
            "| Name | Meeting Time | Meeting Notes |\n"
            "|------|-------------|---------------|\n"
            "| Collector SIG: Core&nbsp; | Monday | "
            "[Google Doc](https://docs.google.com/document/d/reverse-id/edit) |\n"
        )
        mock_resp = MagicMock()
        mock_resp.text = readme
        mock_resp.raise_for_status = MagicMock()
        with patch("scraper.community.requests.get", return_value=mock_resp):
            url = get_meeting_notes_url("collector")
        assert url == "https://docs.google.com/document/d/reverse-id/edit"
