"""Tests for scripts/send_digest.py — daily digest email.

These tests mock subprocess, OpenAI, requests, and env vars so no
API keys or network access are needed.
"""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Ensure scripts/ is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from send_digest import (  # noqa: E402
    _load_logo_b64,
    _make_excerpt,
    build_deep_link,
    build_email,
    generate_digest_narrative,
    get_new_summary_paths,
    main,
    parse_summary_info,
    send_email,
)

FAKE_LOGO_B64 = "data:image/svg+xml;base64,PHN2Zz48L3N2Zz4="

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

FAKE_NARRATIVE = "Today the OTel community discussed collector improvements and SDK updates."

SAMPLE_SUMMARY = textwrap.dedent("""\
    ## Key Topics
    - Discussed collector stability
    ## Action Items
    - Follow up on PR #123
    ## Participants
    Tyler, Damien
""")

GIT_DIFF_OUTPUT = (
    "docs/content/Go-SIG/2026-03-05/summary.md\n"
    "docs/content/Go-SIG/2026-03-05/transcript.md\n"
    "docs/content/Collector-SIG/2026-03-05/summary.md\n"
    "docs/content/Collector-SIG/2026-03-05/meeting-notes.md\n"
)


def _mock_openai_client(response_text: str = FAKE_NARRATIVE) -> MagicMock:
    mock_message = MagicMock()
    mock_message.content = response_text
    mock_choice = MagicMock()
    mock_choice.message = mock_message
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = mock_response
    return mock_client


def _env(**overrides: str) -> dict[str, str]:
    """Return a base env dict with all required keys, updated with overrides."""
    base = {
        "OPENAI_API_KEY": "test-openai-key",
        "RESEND_API_KEY": "test-resend-key",
        "DIGEST_TO": "user@example.com",
    }
    base.update(overrides)
    return base


def _mock_subprocess_result(stdout: str = "") -> MagicMock:
    result = MagicMock()
    result.stdout = stdout
    return result


# SHA of the commit that summarize pushed (passed via artifact as SUMMARIZE_COMMIT_SHA)
FAKE_COMMIT_SHA = "1111111122222222333333334444444455555555ff"


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestGetNewSummaryPaths:
    """Tests for git diff filtering and commit SHA routing."""

    def test_git_diff_filtering(self) -> None:
        """Only paths ending with /summary.md should be returned."""
        env = {"SUMMARIZE_COMMIT_SHA": FAKE_COMMIT_SHA, "SUMMARIZE_COMMIT_FOUND": "true"}
        with (
            patch(
                "send_digest.subprocess.run",
                return_value=_mock_subprocess_result(GIT_DIFF_OUTPUT),
            ),
            patch.dict("os.environ", env),
        ):
            paths = get_new_summary_paths()
        assert len(paths) == 2
        assert all(p.endswith("/summary.md") for p in paths)
        assert "docs/content/Go-SIG/2026-03-05/transcript.md" not in paths
        assert "docs/content/Collector-SIG/2026-03-05/meeting-notes.md" not in paths

    def test_no_summarize_commit_skips(self) -> None:
        """SUMMARIZE_COMMIT_FOUND=true, SHA empty → summarize pushed nothing → return []."""
        env = {"SUMMARIZE_COMMIT_SHA": "", "SUMMARIZE_COMMIT_FOUND": "true"}
        with (
            patch("send_digest.subprocess.run") as mock_run,
            patch.dict("os.environ", env),
        ):
            paths = get_new_summary_paths()
        assert paths == []
        mock_run.assert_not_called()  # no git calls needed

    def test_workflow_dispatch_uses_head_diff(self) -> None:
        """SUMMARIZE_COMMIT_FOUND=false (workflow_dispatch) → fall back to HEAD~1 diff."""
        import os as _os

        _os.environ.pop("SUMMARIZE_COMMIT_SHA", None)
        _os.environ.pop("SUMMARIZE_COMMIT_FOUND", None)
        with (
            patch(
                "send_digest.subprocess.run",
                return_value=_mock_subprocess_result("docs/content/Go-SIG/2026-03-05/summary.md\n"),
            ),
        ):
            paths = get_new_summary_paths()
        assert len(paths) == 1

    def test_git_diff_failure_exits(self) -> None:
        """git diff failure should exit non-zero instead of silently returning an empty set."""
        env = {"SUMMARIZE_COMMIT_SHA": FAKE_COMMIT_SHA, "SUMMARIZE_COMMIT_FOUND": "true"}
        with (
            patch(
                "send_digest.subprocess.run",
                side_effect=subprocess.CalledProcessError(
                    128, ["git", "diff"], stderr="bad revision"
                ),
            ),
            patch.dict("os.environ", env),
            pytest.raises(SystemExit) as exc_info,
        ):
            get_new_summary_paths()
        assert exc_info.value.code == 1


class TestMain:
    """Tests for the main() orchestration."""

    def test_empty_recipients_after_filter(self) -> None:
        """DIGEST_TO with only commas -> no valid addresses -> exits cleanly."""
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"
        env = _env(
            DIGEST_TO=",,,", SUMMARIZE_COMMIT_SHA=FAKE_COMMIT_SHA, SUMMARIZE_COMMIT_FOUND="true"
        )
        with (
            patch("send_digest.subprocess.run", return_value=_mock_subprocess_result(diff_output)),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest.requests.post") as mock_post,
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 0
        mock_post.assert_not_called()

    def test_no_new_summaries(self) -> None:
        """SUMMARIZE_COMMIT_FOUND=true, SHA empty → summarize pushed nothing → exits cleanly."""
        with (
            patch("send_digest.subprocess.run") as mock_run,
            patch.dict(
                "os.environ", {"SUMMARIZE_COMMIT_SHA": "", "SUMMARIZE_COMMIT_FOUND": "true"}
            ),
            patch("send_digest.requests.post") as mock_post,
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 0
        mock_run.assert_not_called()
        mock_post.assert_not_called()

    def test_missing_digest_to(self) -> None:
        """DIGEST_TO not set -> exits cleanly."""
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"
        with (
            patch("send_digest.subprocess.run", return_value=_mock_subprocess_result(diff_output)),
            patch.dict(
                "os.environ",
                {
                    "SUMMARIZE_COMMIT_SHA": FAKE_COMMIT_SHA,
                    "SUMMARIZE_COMMIT_FOUND": "true",
                    "DIGEST_TO": "",
                },
            ),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 0

    def test_missing_resend_api_key(self) -> None:
        """RESEND_API_KEY not set -> exits with error."""
        env = _env(
            RESEND_API_KEY="", SUMMARIZE_COMMIT_SHA=FAKE_COMMIT_SHA, SUMMARIZE_COMMIT_FOUND="true"
        )
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"
        with (
            patch("send_digest.subprocess.run", return_value=_mock_subprocess_result(diff_output)),
            patch.dict("os.environ", env, clear=False),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 1

    def test_happy_path(self, tmp_path: Path) -> None:
        """New summaries found -> OpenAI called -> Resend POST made."""
        mock_client = _mock_openai_client()
        mock_resp = MagicMock()
        mock_resp.status_code = 200

        env = _env(SUMMARIZE_COMMIT_SHA=FAKE_COMMIT_SHA, SUMMARIZE_COMMIT_FOUND="true")
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"

        with (
            patch(
                "send_digest.subprocess.run",
                side_effect=[
                    _mock_subprocess_result(diff_output),  # git diff in get_new_summary_paths
                    _mock_subprocess_result(SAMPLE_SUMMARY),  # git show in parse_summary_info
                ],
            ),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest._create_openai_client", return_value=mock_client),
            patch("send_digest._render_html", return_value="<html>mock</html>"),
            patch("send_digest._load_logo_b64", return_value=FAKE_LOGO_B64),
            patch("send_digest.requests.post", return_value=mock_resp) as mock_post,
        ):
            main()

        mock_client.chat.completions.create.assert_called_once()
        mock_post.assert_called_once()
        call_json = mock_post.call_args.kwargs.get("json") or mock_post.call_args[1].get("json")
        assert call_json["from"] == "digest@otelminutes.jcosta.dev"
        assert call_json["to"] == ["user@example.com"]
        assert "Go-SIG" in call_json["subject"] or "1 meetings" in call_json["subject"]

    def test_multiple_recipients(self, tmp_path: Path) -> None:
        """DIGEST_TO with comma-separated list -> to field is a list."""
        mock_client = _mock_openai_client()
        mock_resp = MagicMock()
        mock_resp.status_code = 200

        env = _env(
            DIGEST_TO="a@test.com, b@test.com, c@test.com",
            SUMMARIZE_COMMIT_SHA=FAKE_COMMIT_SHA,
            SUMMARIZE_COMMIT_FOUND="true",
        )
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"

        with (
            patch(
                "send_digest.subprocess.run",
                side_effect=[
                    _mock_subprocess_result(diff_output),
                    _mock_subprocess_result(SAMPLE_SUMMARY),
                ],
            ),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest._create_openai_client", return_value=mock_client),
            patch("send_digest._render_html", return_value="<html>mock</html>"),
            patch("send_digest._load_logo_b64", return_value=FAKE_LOGO_B64),
            patch("send_digest.requests.post", return_value=mock_resp) as mock_post,
        ):
            main()

        call_json = mock_post.call_args.kwargs.get("json") or mock_post.call_args[1].get("json")
        assert call_json["to"] == ["a@test.com", "b@test.com", "c@test.com"]

    def test_blank_recipients_filtered(self, tmp_path: Path) -> None:
        """Trailing comma or double-comma in DIGEST_TO -> blank entries dropped."""
        mock_client = _mock_openai_client()
        mock_resp = MagicMock()
        mock_resp.status_code = 200

        env = _env(
            DIGEST_TO="a@test.com,,b@test.com,",
            SUMMARIZE_COMMIT_SHA=FAKE_COMMIT_SHA,
            SUMMARIZE_COMMIT_FOUND="true",
        )
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"

        with (
            patch(
                "send_digest.subprocess.run",
                side_effect=[
                    _mock_subprocess_result(diff_output),
                    _mock_subprocess_result(SAMPLE_SUMMARY),
                ],
            ),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest._create_openai_client", return_value=mock_client),
            patch("send_digest._render_html", return_value="<html>mock</html>"),
            patch("send_digest._load_logo_b64", return_value=FAKE_LOGO_B64),
            patch("send_digest.requests.post", return_value=mock_resp) as mock_post,
        ):
            main()

        call_json = mock_post.call_args.kwargs.get("json") or mock_post.call_args[1].get("json")
        assert call_json["to"] == ["a@test.com", "b@test.com"]

    def test_resend_error_handling(self, tmp_path: Path) -> None:
        """Resend returns 400 -> error printed, exits non-zero."""
        mock_client = _mock_openai_client()
        mock_resp = MagicMock()
        mock_resp.status_code = 400
        mock_resp.text = "Bad Request"

        env = _env(SUMMARIZE_COMMIT_SHA=FAKE_COMMIT_SHA, SUMMARIZE_COMMIT_FOUND="true")
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"

        with (
            patch(
                "send_digest.subprocess.run",
                side_effect=[
                    _mock_subprocess_result(diff_output),
                    _mock_subprocess_result(SAMPLE_SUMMARY),
                ],
            ),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest._create_openai_client", return_value=mock_client),
            patch("send_digest._render_html", return_value="<html>mock</html>"),
            patch("send_digest._load_logo_b64", return_value=FAKE_LOGO_B64),
            patch("send_digest.requests.post", return_value=mock_resp),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()

        assert exc_info.value.code == 1

    def test_git_show_failure_exits(self) -> None:
        """git show failure while reading a summary snapshot should fail fast."""
        paths = ["docs/content/Go-SIG/2026-03-05/summary.md"]
        with (
            patch("send_digest.get_new_summary_paths", return_value=paths),
            patch(
                "send_digest.subprocess.run",
                side_effect=subprocess.CalledProcessError(
                    128, ["git", "show"], stderr="missing object"
                ),
            ),
            patch.dict("os.environ", _env(SUMMARIZE_COMMIT_SHA=FAKE_COMMIT_SHA)),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 1


class TestBuildEmail:
    """Tests for email construction."""

    def test_subject_format(self) -> None:
        """Subject contains date and meeting count."""
        summaries = [
            {"slug": "Go-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY},
            {"slug": "Collector-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY},
        ]
        with (
            patch("send_digest._render_html", return_value="<html>mock</html>"),
            patch("send_digest._load_logo_b64", return_value=FAKE_LOGO_B64),
        ):
            email = build_email(FAKE_NARRATIVE, summaries, "2026-03-05", 2)
        assert "2026-03-05" in email["subject"]
        assert "2 meetings" in email["subject"]

    def test_deep_link_urls(self) -> None:
        """Plain-text body contains correct deep-link URLs."""
        summaries = [
            {"slug": "Go-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY},
            {"slug": "Collector-SIG", "date": "2026-03-06", "content": SAMPLE_SUMMARY},
        ]
        with (
            patch("send_digest._render_html", return_value="<html>mock</html>"),
            patch("send_digest._load_logo_b64", return_value=FAKE_LOGO_B64),
        ):
            email = build_email(FAKE_NARRATIVE, summaries, "2026-03-05", 2)
        assert "?sig=Go-SIG&date=2026-03-05" in email["text"]
        assert "?sig=Collector-SIG&date=2026-03-06" in email["text"]


class TestGenerateDigestNarrative:
    """Tests for OpenAI narrative generation."""

    def test_calls_openai(self) -> None:
        """OpenAI should be called with the combined summaries."""
        mock_client = _mock_openai_client()
        summaries = [{"slug": "Go-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY}]
        result = generate_digest_narrative(mock_client, summaries)
        mock_client.chat.completions.create.assert_called_once()
        assert result == FAKE_NARRATIVE

    def test_no_choices_raises_value_error(self) -> None:
        """Empty choices list from OpenAI should raise ValueError."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = []
        mock_client.chat.completions.create.return_value = mock_response
        summaries = [{"slug": "Go-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY}]
        with pytest.raises(ValueError):
            generate_digest_narrative(mock_client, summaries)


# ---------------------------------------------------------------------------
# TestParseSummaryInfo — filesystem path (no commit SHA)
# ---------------------------------------------------------------------------


class TestParseSummaryInfo:
    def test_reads_from_filesystem(self, tmp_path: Path) -> None:
        path = "docs/content/Go-SIG/2026-03-05/summary.md"
        summary_file = tmp_path / path
        summary_file.parent.mkdir(parents=True, exist_ok=True)
        summary_file.write_text("Summary content", encoding="utf-8")

        with patch("send_digest.ROOT", tmp_path):
            result = parse_summary_info(path)

        assert result["slug"] == "Go-SIG"
        assert result["date"] == "2026-03-05"
        assert result["content"] == "Summary content"

    def test_returns_empty_content_when_file_missing(self, tmp_path: Path) -> None:
        path = "docs/content/Go-SIG/2026-03-05/summary.md"
        with patch("send_digest.ROOT", tmp_path):
            result = parse_summary_info(path)

        assert result["slug"] == "Go-SIG"
        assert result["date"] == "2026-03-05"
        assert result["content"] == ""


# ---------------------------------------------------------------------------
# TestMakeExcerpt
# ---------------------------------------------------------------------------


class TestMakeExcerpt:
    def test_returns_first_non_heading_line(self) -> None:
        content = "## Key Topics\n- Item 1\n## Action Items\n- Item 2\n"
        assert _make_excerpt(content) == "- Item 1"

    def test_skips_heading_lines(self) -> None:
        content = "## Heading\n\nSome text here.\n"
        assert _make_excerpt(content) == "Some text here."

    def test_all_headings_falls_back_to_raw(self) -> None:
        content = "## Only Headings\n## More Headings\n"
        result = _make_excerpt(content)
        assert "Heading" in result

    def test_truncates_long_line(self) -> None:
        content = "Regular text: " + "x" * 400 + "\n"
        assert len(_make_excerpt(content)) <= 300

    def test_empty_content(self) -> None:
        assert _make_excerpt("") == ""


# ---------------------------------------------------------------------------
# TestBuildDeepLink
# ---------------------------------------------------------------------------


class TestBuildDeepLink:
    def test_format(self) -> None:
        url = build_deep_link("Go-SIG", "2026-03-05")
        assert "sig=Go-SIG" in url
        assert "date=2026-03-05" in url

    def test_starts_with_site_base(self) -> None:
        from send_digest import SITE_BASE_URL

        url = build_deep_link("Java-SIG", "2026-02-10")
        assert url.startswith(SITE_BASE_URL)


# ---------------------------------------------------------------------------
# TestLoadLogob64
# ---------------------------------------------------------------------------


class TestLoadLogob64:
    def test_returns_data_uri(self, tmp_path: Path) -> None:
        import base64 as _b64

        svg = b"<svg></svg>"
        (tmp_path / "docs").mkdir()
        (tmp_path / "docs" / "OTelMinutes-logo.svg").write_bytes(svg)
        with patch("send_digest.ROOT", tmp_path):
            result = _load_logo_b64()
        assert result.startswith("data:image/svg+xml;base64,")
        assert _b64.b64encode(svg).decode("ascii") in result


# ---------------------------------------------------------------------------
# TestSendEmail
# ---------------------------------------------------------------------------


class TestSendEmail:
    def test_200_status_succeeds(self) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        with patch("send_digest.requests.post", return_value=mock_resp):
            send_email(
                "key", ["u@example.com"], {"subject": "S", "html": "<p>test</p>", "text": "test"}
            )

    def test_201_status_succeeds(self) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 201
        with patch("send_digest.requests.post", return_value=mock_resp):
            send_email(
                "key", ["u@example.com"], {"subject": "S", "html": "<p>test</p>", "text": "test"}
            )

    def test_error_status_exits(self) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 400
        mock_resp.text = "Bad Request"
        with patch("send_digest.requests.post", return_value=mock_resp):
            with pytest.raises(SystemExit):
                send_email(
                    "key",
                    ["u@example.com"],
                    {"subject": "S", "html": "<p>test</p>", "text": "test"},
                )


# ---------------------------------------------------------------------------
# TestMain — additional cases
# ---------------------------------------------------------------------------


class TestMainExtra:
    def test_missing_openai_api_key(self) -> None:
        """OPENAI_API_KEY not set → exits with error."""
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"
        env = {
            "SUMMARIZE_COMMIT_SHA": FAKE_COMMIT_SHA,
            "SUMMARIZE_COMMIT_FOUND": "true",
            "DIGEST_TO": "user@example.com",
            "OPENAI_API_KEY": "",
            "RESEND_API_KEY": "key",
        }
        with (
            patch("send_digest.subprocess.run", return_value=_mock_subprocess_result(diff_output)),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 1
