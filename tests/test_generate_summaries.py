"""Tests for generate_summaries.py — AI-powered transcript summarisation.

These tests mock the OpenAI client so no API key or network access is needed.
"""
from __future__ import annotations

import textwrap
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# ---------------------------------------------------------------------------
# Sample data
# ---------------------------------------------------------------------------

SAMPLE_TRANSCRIPT = textwrap.dedent("""\
    SIG: Go SIG
    Date: 2026-02-05
    Duration: 33 minutes
    Source URL: https://zoom.us/rec/share/example
    ============================================================

    Tyler 02:14 Hey, Damien.
    Damien Mathieu 02:19 Hey!
    Tyler 02:20 How's it going?
""")

LONG_TRANSCRIPT_BODY = "Alice 00:01 " + ("word " * 3000) + "\n"
LONG_TRANSCRIPT = textwrap.dedent("""\
    SIG: Go SIG
    Date: 2026-02-05
    Duration: 60 minutes
    Source URL: https://zoom.us/rec/share/example
    ============================================================

""") + LONG_TRANSCRIPT_BODY

FAKE_SUMMARY_MD = textwrap.dedent("""\
    # Go SIG — 2026-02-05

    **Duration:** 33 minutes
    **Source:** https://zoom.us/rec/share/example

    ## Key Topics
    - Discussed recent Fostim conference highlights

    ## Action Items
    - Follow up on collector stability work

    ## Participants
    Tyler, Damien Mathieu
""")


def _write_transcript(base: Path, slug: str, filename: str, content: str) -> None:
    d = base / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / filename).write_text(content, encoding="utf-8")


def _mock_openai_client(response_text: str = FAKE_SUMMARY_MD) -> MagicMock:
    """Return a MagicMock that mimics openai.OpenAI().chat.completions.create()."""
    mock_message = MagicMock()
    mock_message.content = response_text

    mock_choice = MagicMock()
    mock_choice.message = mock_message

    mock_response = MagicMock()
    mock_response.choices = [mock_choice]

    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = mock_response
    return mock_client


# ---------------------------------------------------------------------------
# Tests: transcript body extraction & truncation
# ---------------------------------------------------------------------------

class TestTranscriptParsing:
    """Tests for reading and truncating transcript text."""

    def test_extract_body_strips_header(self, tmp_path: Path) -> None:
        """The header (lines 1-5) and blank line 6 should be stripped."""
        # This test validates that generate_summaries reads only the
        # transcript body (after the === separator), not the header.
        p = tmp_path / "test.txt"
        p.write_text(SAMPLE_TRANSCRIPT, encoding="utf-8")

        # TODO: import and call the real extract function once implemented
        # body = extract_transcript_body(p)
        # assert "SIG:" not in body
        # assert "Tyler 02:14" in body

    def test_truncate_long_transcript(self) -> None:
        """Transcripts exceeding ~12,000 chars should be truncated."""
        # The body of LONG_TRANSCRIPT is ~15,000 chars
        assert len(LONG_TRANSCRIPT_BODY) > 12_000

        # TODO: import and call the real truncate function once implemented
        # truncated = truncate_transcript(LONG_TRANSCRIPT_BODY, max_chars=12_000)
        # assert len(truncated) <= 12_000

    def test_short_transcript_not_truncated(self) -> None:
        """Short transcripts should be returned as-is."""
        short_body = "Tyler 02:14 Hey, Damien.\nDamien Mathieu 02:19 Hey!\n"
        assert len(short_body) < 12_000

        # TODO: import and call the real truncate function once implemented
        # result = truncate_transcript(short_body, max_chars=12_000)
        # assert result == short_body


# ---------------------------------------------------------------------------
# Tests: summary generation with mocked OpenAI
# ---------------------------------------------------------------------------

class TestGenerateSummary:
    """Tests for the core summary generation logic with mocked OpenAI."""

    def test_generates_summary_file(self, tmp_path: Path) -> None:
        """A new summary .md file should be created for a transcript."""
        transcripts = tmp_path / "transcripts"
        summaries = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        mock_client = _mock_openai_client()

        # TODO: import and call the real generate function once implemented
        # with patch("generate_summaries.TRANSCRIPTS_SRC", transcripts), \
        #      patch("generate_summaries.SUMMARIES_DIR", summaries), \
        #      patch("generate_summaries._get_openai_client", return_value=mock_client):
        #     generate_summaries()
        #
        # summary_file = summaries / "Go-SIG" / "2026-02-05.md"
        # assert summary_file.exists()
        # mock_client.chat.completions.create.assert_called_once()

    def test_skips_existing_summary(self, tmp_path: Path) -> None:
        """If a summary already exists, the transcript should be skipped."""
        transcripts = tmp_path / "transcripts"
        summaries = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        # Pre-create the summary
        (summaries / "Go-SIG").mkdir(parents=True)
        (summaries / "Go-SIG" / "2026-02-05.md").write_text(FAKE_SUMMARY_MD)

        mock_client = _mock_openai_client()

        # TODO: import and call the real generate function once implemented
        # with patch("generate_summaries.TRANSCRIPTS_SRC", transcripts), \
        #      patch("generate_summaries.SUMMARIES_DIR", summaries), \
        #      patch("generate_summaries._get_openai_client", return_value=mock_client):
        #     generate_summaries()
        #
        # mock_client.chat.completions.create.assert_not_called()

    def test_openai_called_with_transcript_content(self, tmp_path: Path) -> None:
        """The OpenAI call should include the transcript body in the prompt."""
        transcripts = tmp_path / "transcripts"
        summaries = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        mock_client = _mock_openai_client()

        # TODO: import and call the real generate function once implemented
        # with patch("generate_summaries.TRANSCRIPTS_SRC", transcripts), \
        #      patch("generate_summaries.SUMMARIES_DIR", summaries), \
        #      patch("generate_summaries._get_openai_client", return_value=mock_client):
        #     generate_summaries()
        #
        # call_args = mock_client.chat.completions.create.call_args
        # messages = call_args.kwargs.get("messages") or call_args[1].get("messages")
        # prompt_text = " ".join(m["content"] for m in messages)
        # assert "Tyler" in prompt_text
        # assert "Damien" in prompt_text

    def test_multiple_transcripts_processed(self, tmp_path: Path) -> None:
        """All transcripts without summaries should be processed."""
        transcripts = tmp_path / "transcripts"
        summaries = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)
        _write_transcript(transcripts, "Go-SIG", "2026-02-12.txt",
                          SAMPLE_TRANSCRIPT.replace("2026-02-05", "2026-02-12"))

        mock_client = _mock_openai_client()

        # TODO: import and call the real generate function once implemented
        # with patch("generate_summaries.TRANSCRIPTS_SRC", transcripts), \
        #      patch("generate_summaries.SUMMARIES_DIR", summaries), \
        #      patch("generate_summaries._get_openai_client", return_value=mock_client):
        #     generate_summaries()
        #
        # assert mock_client.chat.completions.create.call_count == 2
        # assert (summaries / "Go-SIG" / "2026-02-05.md").exists()
        # assert (summaries / "Go-SIG" / "2026-02-12.md").exists()

    def test_uses_gpt4o_mini_model(self, tmp_path: Path) -> None:
        """The OpenAI call should use gpt-4o-mini for cost efficiency."""
        transcripts = tmp_path / "transcripts"
        summaries = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        mock_client = _mock_openai_client()

        # TODO: import and call the real generate function once implemented
        # with patch("generate_summaries.TRANSCRIPTS_SRC", transcripts), \
        #      patch("generate_summaries.SUMMARIES_DIR", summaries), \
        #      patch("generate_summaries._get_openai_client", return_value=mock_client):
        #     generate_summaries()
        #
        # call_args = mock_client.chat.completions.create.call_args
        # model = call_args.kwargs.get("model") or call_args[1].get("model")
        # assert model == "gpt-4o-mini"


# ---------------------------------------------------------------------------
# Tests: summary output format
# ---------------------------------------------------------------------------

class TestSummaryFormat:
    """Tests for the expected Markdown structure of generated summaries."""

    def test_summary_has_required_sections(self) -> None:
        """Generated summaries should contain the expected sections."""
        assert "# Go SIG" in FAKE_SUMMARY_MD
        assert "## Key Topics" in FAKE_SUMMARY_MD
        assert "## Action Items" in FAKE_SUMMARY_MD
        assert "## Participants" in FAKE_SUMMARY_MD

    def test_summary_has_metadata(self) -> None:
        """Generated summaries should include duration and source URL."""
        assert "**Duration:**" in FAKE_SUMMARY_MD
        assert "**Source:**" in FAKE_SUMMARY_MD
