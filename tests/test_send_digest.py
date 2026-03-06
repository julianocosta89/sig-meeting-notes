"""Tests for scripts/send_digest.py — daily digest email.

These tests mock subprocess, OpenAI, requests, and env vars so no
API keys or network access are needed.
"""
from __future__ import annotations

import sys
import textwrap
from datetime import date as _date
from pathlib import Path
from unittest.mock import MagicMock, call, patch

import pytest

# Ensure scripts/ is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from send_digest import (  # noqa: E402
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


# SHA that the workflow passes as SUMMARIZE_HEAD_SHA (the pre-run HEAD)
FAKE_PRE_RUN_SHA = "aaaaaaaabbbbbbbbccccccccddddddddeeeeeeee00"
# SHA after summarize pushes its commit (different → guard passes, diff proceeds)
FAKE_NEW_SHA = "1111111122222222333333334444444455555555ff"


def _subprocess_side_effects(diff_stdout: str) -> list[MagicMock]:
    """Return [git_rev_parse_result, git_diff_result] for subprocess.run side_effect.

    rev-parse returns FAKE_NEW_SHA (≠ FAKE_PRE_RUN_SHA) so the guard recognises
    that summarize pushed a new commit and proceeds to the git diff.
    """
    return [_mock_subprocess_result(FAKE_NEW_SHA), _mock_subprocess_result(diff_stdout)]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestGetNewSummaryPaths:
    """Tests for git diff filtering and SHA guard."""

    def test_git_diff_filtering(self) -> None:
        """Only paths ending with /summary.md should be returned."""
        with (
            patch("send_digest.subprocess.run", side_effect=_subprocess_side_effects(GIT_DIFF_OUTPUT)),
            patch.dict("os.environ", {"SUMMARIZE_HEAD_SHA": FAKE_PRE_RUN_SHA}),
        ):
            paths = get_new_summary_paths()
        assert len(paths) == 2
        assert all(p.endswith("/summary.md") for p in paths)
        assert "docs/content/Go-SIG/2026-03-05/transcript.md" not in paths
        assert "docs/content/Collector-SIG/2026-03-05/meeting-notes.md" not in paths

    def test_no_new_commit_guard(self) -> None:
        """If HEAD equals SUMMARIZE_HEAD_SHA, summarize committed nothing → return []."""
        with (
            # rev-parse returns the same SHA as SUMMARIZE_HEAD_SHA → no new commit
            patch("send_digest.subprocess.run", return_value=_mock_subprocess_result(FAKE_PRE_RUN_SHA)) as mock_run,
            patch.dict("os.environ", {"SUMMARIZE_HEAD_SHA": FAKE_PRE_RUN_SHA}),
        ):
            paths = get_new_summary_paths()
        assert paths == []
        mock_run.assert_called_once()  # git diff never called

    def test_no_sha_env_skips_guard(self) -> None:
        """Without SUMMARIZE_HEAD_SHA (workflow_dispatch), guard is skipped."""
        import os as _os
        _os.environ.pop("SUMMARIZE_HEAD_SHA", None)
        with (
            patch("send_digest.subprocess.run", return_value=_mock_subprocess_result(
                "docs/content/Go-SIG/2026-03-05/summary.md\n"
            )),
        ):
            paths = get_new_summary_paths()
        assert len(paths) == 1


class TestMain:
    """Tests for the main() orchestration."""

    def test_empty_recipients_after_filter(self) -> None:
        """DIGEST_TO with only commas -> no valid addresses -> exits cleanly."""
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"
        env = _env(DIGEST_TO=",,,", SUMMARIZE_HEAD_SHA=FAKE_PRE_RUN_SHA)
        with (
            patch("send_digest.subprocess.run", side_effect=_subprocess_side_effects(diff_output)),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest.requests.post") as mock_post,
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 0
        mock_post.assert_not_called()

    def test_no_new_summaries(self) -> None:
        """HEAD == SUMMARIZE_HEAD_SHA (no new commit) -> exits cleanly, no API calls."""
        with (
            # rev-parse returns same SHA as SUMMARIZE_HEAD_SHA → guard fires → []
            patch("send_digest.subprocess.run", return_value=_mock_subprocess_result(FAKE_PRE_RUN_SHA)),
            patch.dict("os.environ", {"SUMMARIZE_HEAD_SHA": FAKE_PRE_RUN_SHA}),
            patch("send_digest.requests.post") as mock_post,
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 0
        mock_post.assert_not_called()

    def test_missing_digest_to(self) -> None:
        """DIGEST_TO not set -> exits cleanly."""
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"
        with (
            patch("send_digest.subprocess.run", side_effect=_subprocess_side_effects(diff_output)),
            patch.dict("os.environ", {"SUMMARIZE_HEAD_SHA": FAKE_PRE_RUN_SHA, "DIGEST_TO": ""}),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 0

    def test_missing_resend_api_key(self) -> None:
        """RESEND_API_KEY not set -> exits with error."""
        env = _env(RESEND_API_KEY="", SUMMARIZE_HEAD_SHA=FAKE_PRE_RUN_SHA)
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"
        with (
            patch("send_digest.subprocess.run", side_effect=_subprocess_side_effects(diff_output)),
            patch.dict("os.environ", env, clear=False),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            pytest.raises(SystemExit) as exc_info,
        ):
            main()
        assert exc_info.value.code == 1

    def test_happy_path(self, tmp_path: Path) -> None:
        """New summaries found -> OpenAI called -> Resend POST made."""
        # Write a summary file to disk
        summary_dir = tmp_path / "docs" / "content" / "Go-SIG" / "2026-03-05"
        summary_dir.mkdir(parents=True)
        (summary_dir / "summary.md").write_text(SAMPLE_SUMMARY)

        mock_client = _mock_openai_client()
        mock_resp = MagicMock()
        mock_resp.status_code = 200

        env = _env(SUMMARIZE_HEAD_SHA=FAKE_PRE_RUN_SHA)
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"

        with (
            patch("send_digest.subprocess.run", side_effect=_subprocess_side_effects(diff_output)),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest.ROOT", tmp_path),
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
        summary_dir = tmp_path / "docs" / "content" / "Go-SIG" / "2026-03-05"
        summary_dir.mkdir(parents=True)
        (summary_dir / "summary.md").write_text(SAMPLE_SUMMARY)

        mock_client = _mock_openai_client()
        mock_resp = MagicMock()
        mock_resp.status_code = 200

        env = _env(DIGEST_TO="a@test.com, b@test.com, c@test.com", SUMMARIZE_HEAD_SHA=FAKE_PRE_RUN_SHA)
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"

        with (
            patch("send_digest.subprocess.run", side_effect=_subprocess_side_effects(diff_output)),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest.ROOT", tmp_path),
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
        summary_dir = tmp_path / "docs" / "content" / "Go-SIG" / "2026-03-05"
        summary_dir.mkdir(parents=True)
        (summary_dir / "summary.md").write_text(SAMPLE_SUMMARY)

        mock_client = _mock_openai_client()
        mock_resp = MagicMock()
        mock_resp.status_code = 200

        env = _env(DIGEST_TO="a@test.com,,b@test.com,", SUMMARIZE_HEAD_SHA=FAKE_PRE_RUN_SHA)
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"

        with (
            patch("send_digest.subprocess.run", side_effect=_subprocess_side_effects(diff_output)),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest.ROOT", tmp_path),
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
        summary_dir = tmp_path / "docs" / "content" / "Go-SIG" / "2026-03-05"
        summary_dir.mkdir(parents=True)
        (summary_dir / "summary.md").write_text(SAMPLE_SUMMARY)

        mock_client = _mock_openai_client()
        mock_resp = MagicMock()
        mock_resp.status_code = 400
        mock_resp.text = "Bad Request"

        env = _env(SUMMARIZE_HEAD_SHA=FAKE_PRE_RUN_SHA)
        diff_output = "docs/content/Go-SIG/2026-03-05/summary.md\n"

        with (
            patch("send_digest.subprocess.run", side_effect=_subprocess_side_effects(diff_output)),
            patch("send_digest.os.environ.get", side_effect=lambda k, d="": env.get(k, d)),
            patch("send_digest.ROOT", tmp_path),
            patch("send_digest._create_openai_client", return_value=mock_client),
            patch("send_digest._render_html", return_value="<html>mock</html>"),
            patch("send_digest._load_logo_b64", return_value=FAKE_LOGO_B64),
            patch("send_digest.requests.post", return_value=mock_resp),
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
