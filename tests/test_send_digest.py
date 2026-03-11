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
    _is_trivial_transcript,
    _load_logo_b64,
    build_deep_link,
    build_email,
    generate_digest_narrative,
    get_new_summary_paths,
    main,
    parse_summary_info,
    parse_summary_sections,
    send_email,
)

FAKE_LOGO_B64 = "data:image/png;base64,iVBORw0KGgo="

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
            patch("send_digest._is_trivial_transcript", return_value=False),
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
            patch("send_digest._is_trivial_transcript", return_value=False),
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
            patch("send_digest._is_trivial_transcript", return_value=False),
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
            patch("send_digest._is_trivial_transcript", return_value=False),
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
            patch("send_digest._is_trivial_transcript", return_value=False),
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
            patch("send_digest._is_trivial_transcript", return_value=False),
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
            patch("send_digest._is_trivial_transcript", return_value=False),
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
            patch("send_digest._is_trivial_transcript", return_value=False),
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

    def test_highlights_present_in_meetings(self) -> None:
        """Each meeting dict from build_email should have a populated highlights list."""
        summaries = [{"slug": "Go-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY}]
        captured: list[dict] = []

        def _capture_render(template_vars: dict) -> str:
            captured.append(template_vars)
            return "<html>mock</html>"

        with (
            patch("send_digest._render_html", side_effect=_capture_render),
            patch("send_digest._load_logo_b64", return_value=FAKE_LOGO_B64),
        ):
            build_email(FAKE_NARRATIVE, summaries, "2026-03-05", 1)

        meetings = captured[0]["meetings"]  # type: ignore[index]
        assert len(meetings) == 1
        assert "highlights" in meetings[0]
        assert meetings[0]["highlights"] == ["Discussed collector stability"]


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

    def test_single_meeting_uses_summary_prompt(self) -> None:
        """One-meeting input should not ask for cross-SIG correlations."""
        mock_client = _mock_openai_client()
        summaries = [{"slug": "Go-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY}]
        generate_digest_narrative(mock_client, summaries)
        call_kwargs = mock_client.chat.completions.create.call_args[1]
        user_msg = next(m["content"] for m in call_kwargs["messages"] if m["role"] == "user")
        assert "cross-cutting" not in user_msg
        assert "correlations" not in user_msg

    def test_multi_meeting_uses_cross_sig_prompt(self) -> None:
        """Multiple meetings should get the cross-SIG correlation prompt."""
        mock_client = _mock_openai_client()
        summaries = [
            {"slug": "Go-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY},
            {"slug": "Collector-SIG", "date": "2026-03-05", "content": SAMPLE_SUMMARY},
        ]
        generate_digest_narrative(mock_client, summaries)
        call_kwargs = mock_client.chat.completions.create.call_args[1]
        user_msg = next(m["content"] for m in call_kwargs["messages"] if m["role"] == "user")
        assert "cross-cutting" in user_msg


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
# TestParseSummarySections
# ---------------------------------------------------------------------------


class TestParseSummarySections:
    def test_parses_key_topics_as_highlights(self) -> None:
        content = "## Key Topics\n- Discussed collector stability\n- Reviewed PR #42\n"
        result = parse_summary_sections(content)
        assert result["highlights"] == ["Discussed collector stability", "Reviewed PR #42"]

    def test_strips_leading_dash_from_bullets(self) -> None:
        content = "## Key Topics\n- Item with dash\n"
        result = parse_summary_sections(content)
        assert result["highlights"] == ["Item with dash"]

    def test_parses_action_items(self) -> None:
        content = "## Action Items\n- Follow up on PR #123\n- Update docs\n"
        result = parse_summary_sections(content)
        assert result["action_items"] == ["Follow up on PR #123", "Update docs"]

    def test_parses_participants(self) -> None:
        content = "## Participants\nTyler, Damien\n"
        result = parse_summary_sections(content)
        assert result["participants"] == "Tyler, Damien"

    def test_empty_content_returns_empty(self) -> None:
        result = parse_summary_sections("")
        assert result["highlights"] == []
        assert result["action_items"] == []
        assert result["participants"] == ""

    def test_missing_section_returns_empty(self) -> None:
        content = "## Key Topics\n- Only topics here\n"
        result = parse_summary_sections(content)
        assert result["action_items"] == []
        assert result["participants"] == ""

    def test_unknown_section_ignored(self) -> None:
        content = "## Unknown Section\n- Should be ignored\n## Key Topics\n- Kept\n"
        result = parse_summary_sections(content)
        assert result["highlights"] == ["Kept"]

    def test_full_summary(self) -> None:
        result = parse_summary_sections(SAMPLE_SUMMARY)
        assert result["highlights"] == ["Discussed collector stability"]
        assert result["action_items"] == ["Follow up on PR #123"]
        assert result["participants"] == "Tyler, Damien"


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

        png = b"\x89PNG\r\n\x1a\n"
        (tmp_path / "docs").mkdir()
        (tmp_path / "docs" / "OTelMinutes-logo.png").write_bytes(png)
        with patch("send_digest.ROOT", tmp_path):
            result = _load_logo_b64()
        assert result.startswith("data:image/png;base64,")
        assert _b64.b64encode(png).decode("ascii") in result


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
            patch("send_digest._is_trivial_transcript", return_value=False),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 1

    def test_all_trivial_summaries_skips(self) -> None:
        """All summaries trivial → exits cleanly with no email sent."""
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"
        env = _env(SUMMARIZE_COMMIT_SHA=FAKE_COMMIT_SHA, SUMMARIZE_COMMIT_FOUND="true")
        with (
            patch("send_digest.subprocess.run", return_value=_mock_subprocess_result(diff_output)),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest._is_trivial_transcript", return_value=True),
            patch("send_digest.requests.post") as mock_post,
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 0
        mock_post.assert_not_called()


# ---------------------------------------------------------------------------
# TestIsTrivialTranscript
# ---------------------------------------------------------------------------


class TestIsTrivialTranscript:
    def test_trivial_transcript_detected(self, tmp_path: Path) -> None:
        """Transcript with fewer than MIN_TRANSCRIPT_LINES should be trivial."""
        from scraper.transcript_io import SEPARATOR

        meeting_dir = tmp_path / "docs" / "content" / "Go-SIG" / "2026-03-05"
        meeting_dir.mkdir(parents=True)
        transcript = meeting_dir / "transcript.md"
        transcript.write_text(
            f"SIG: Go SIG\nDate: 2026-03-05\nDuration: 5 minutes\n{SEPARATOR}\n\nSpeaker: hi\n",
            encoding="utf-8",
        )
        with patch("send_digest.ROOT", tmp_path):
            assert _is_trivial_transcript("docs/content/Go-SIG/2026-03-05/summary.md") is True

    def test_real_transcript_not_trivial(self, tmp_path: Path) -> None:
        """Transcript with enough lines should not be trivial."""
        from scraper.transcript_io import SEPARATOR

        meeting_dir = tmp_path / "docs" / "content" / "Go-SIG" / "2026-03-05"
        meeting_dir.mkdir(parents=True)
        lines = "\n".join(f"Speaker: line {i}" for i in range(10))
        transcript = meeting_dir / "transcript.md"
        transcript.write_text(
            f"SIG: Go SIG\nDate: 2026-03-05\nDuration: 30 minutes\n{SEPARATOR}\n\n{lines}\n",
            encoding="utf-8",
        )
        with patch("send_digest.ROOT", tmp_path):
            assert _is_trivial_transcript("docs/content/Go-SIG/2026-03-05/summary.md") is False

    def test_missing_transcript_not_trivial(self, tmp_path: Path) -> None:
        """Missing transcript file should not be considered trivial."""
        with patch("send_digest.ROOT", tmp_path):
            assert _is_trivial_transcript("docs/content/Go-SIG/2026-03-05/summary.md") is False

    def test_trivial_transcript_with_commit_sha(self) -> None:
        """With commit_sha, reads transcript via git show at that commit snapshot."""
        from scraper.transcript_io import SEPARATOR

        trivial_text = (
            f"SIG: Go SIG\nDate: 2026-03-05\nDuration: 5 minutes\n{SEPARATOR}\n\nSpeaker: hi\n"
        )
        with patch("send_digest._run_git") as mock_git:
            mock_git.return_value = MagicMock(stdout=trivial_text)
            result = _is_trivial_transcript(
                "docs/content/Go-SIG/2026-03-05/summary.md", commit_sha="abc123"
            )
        assert result is True
        mock_git.assert_called_once_with(
            ["show", "abc123:docs/content/Go-SIG/2026-03-05/transcript.md"]
        )

    def test_real_transcript_with_commit_sha(self) -> None:
        """With commit_sha and enough lines, is not trivial."""
        from scraper.transcript_io import SEPARATOR

        lines = "\n".join(f"Speaker: line {i}" for i in range(10))
        real_text = f"SIG: Go SIG\nDate: 2026-03-05\nDuration: 30 minutes\n{SEPARATOR}\n\n{lines}\n"
        with patch("send_digest._run_git") as mock_git:
            mock_git.return_value = MagicMock(stdout=real_text)
            result = _is_trivial_transcript(
                "docs/content/Go-SIG/2026-03-05/summary.md", commit_sha="abc123"
            )
        assert result is False

    def test_git_show_failure_not_trivial(self) -> None:
        """If git show fails (e.g. file not in that commit), treat as not trivial."""
        with patch("send_digest._run_git", side_effect=SystemExit(1)):
            result = _is_trivial_transcript(
                "docs/content/Go-SIG/2026-03-05/summary.md", commit_sha="abc123"
            )
        assert result is False
