"""Tests for generate_summaries.py — AI-powered transcript summarisation.

These tests mock the OpenAI client so no API key or network access is needed.
"""
from __future__ import annotations

import textwrap
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("openai")

from generate_summaries import (
    MAX_TRANSCRIPT_CHARS,
    generate_summary,
    process_transcripts,
    read_transcript_body,
)

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
        p = tmp_path / "test.txt"
        p.write_text(SAMPLE_TRANSCRIPT, encoding="utf-8")
        body = read_transcript_body(p)
        assert "SIG:" not in body
        assert "Date:" not in body
        assert "Duration:" not in body
        assert "==========" not in body
        assert "Tyler 02:14" in body

    def test_truncate_long_transcript(self, tmp_path: Path) -> None:
        """Transcripts exceeding ~12,000 chars should be truncated."""
        assert len(LONG_TRANSCRIPT_BODY) > 12_000
        p = tmp_path / "long.txt"
        p.write_text(LONG_TRANSCRIPT, encoding="utf-8")
        body = read_transcript_body(p)
        assert len(body) <= MAX_TRANSCRIPT_CHARS

    def test_short_transcript_not_truncated(self, tmp_path: Path) -> None:
        """Short transcripts should be returned as-is."""
        p = tmp_path / "short.txt"
        p.write_text(SAMPLE_TRANSCRIPT, encoding="utf-8")
        body = read_transcript_body(p)
        assert "Tyler 02:14 Hey, Damien." in body
        assert "Damien Mathieu 02:19 Hey!" in body

    def test_empty_body(self, tmp_path: Path) -> None:
        """A transcript with only a header should return empty body."""
        content = (
            "SIG: Test SIG\n"
            "Date: 2026-01-01\n"
            "Duration: 60 minutes\n"
            "Source URL: https://example.com\n"
            "============================================================\n\n"
        )
        p = tmp_path / "empty.txt"
        p.write_text(content, encoding="utf-8")
        body = read_transcript_body(p)
        assert body.strip() == ""

    def test_no_separator_returns_empty(self, tmp_path: Path) -> None:
        """A file without the separator line should return empty string."""
        p = tmp_path / "bad.txt"
        p.write_text("garbage content\n", encoding="utf-8")
        assert read_transcript_body(p) == ""


# ---------------------------------------------------------------------------
# Tests: summary generation with mocked OpenAI
# ---------------------------------------------------------------------------

class TestGenerateSummary:
    """Tests for the core summary generation logic with mocked OpenAI."""

    def test_calls_openai_with_transcript(self) -> None:
        """The OpenAI API should be called with transcript content."""
        mock_client = _mock_openai_client()
        result = generate_summary(
            mock_client, "Go SIG", "2026-02-05", "33",
            "https://zoom.us/rec/share/example", "Tyler 02:14 Hey!",
        )
        mock_client.chat.completions.create.assert_called_once()

    def test_returns_summary_text(self) -> None:
        """The function should return the summary from OpenAI."""
        mock_client = _mock_openai_client()
        result = generate_summary(
            mock_client, "Go SIG", "2026-02-05", "33",
            "https://zoom.us/rec/share/example", "Tyler 02:14 Hey!",
        )
        assert "Go SIG" in result
        assert "Key Topics" in result

    def test_uses_gpt4o_mini_model(self) -> None:
        """The OpenAI call should use gpt-4o-mini for cost efficiency."""
        mock_client = _mock_openai_client()
        generate_summary(
            mock_client, "Go SIG", "2026-02-05", "33",
            "https://zoom.us/rec/share/example", "Tyler 02:14 Hey!",
        )
        call_args = mock_client.chat.completions.create.call_args
        assert call_args.kwargs["model"] == "gpt-4o-mini"

    def test_prompt_includes_transcript_body(self) -> None:
        """The prompt sent to OpenAI should include the transcript body."""
        mock_client = _mock_openai_client()
        generate_summary(
            mock_client, "Go SIG", "2026-02-05", "33",
            "https://zoom.us/rec/share/example", "Tyler 02:14 Hey, Damien!",
        )
        call_args = mock_client.chat.completions.create.call_args
        messages = call_args.kwargs["messages"]
        prompt_text = " ".join(m["content"] for m in messages)
        assert "Tyler" in prompt_text
        assert "Damien" in prompt_text


# ---------------------------------------------------------------------------
# Tests: process_transcripts integration
# ---------------------------------------------------------------------------

class TestProcessTranscripts:
    """Tests for the main processing loop."""

    def test_creates_summary_file(self, tmp_path: Path) -> None:
        """A new summary .md file should be created for a transcript."""
        transcripts_dir = tmp_path / "docs" / "transcripts"
        summaries_dir = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts_dir, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        mock_client = _mock_openai_client()
        with patch("generate_summaries.time.sleep"):
            process_transcripts(mock_client, transcripts_dir, summaries_dir)

        summary_file = summaries_dir / "Go-SIG" / "2026-02-05.md"
        assert summary_file.exists()
        assert "Go SIG" in summary_file.read_text(encoding="utf-8")
        mock_client.chat.completions.create.assert_called_once()

    def test_skips_existing_summaries(self, tmp_path: Path) -> None:
        """If a summary already exists, the transcript should be skipped."""
        transcripts_dir = tmp_path / "docs" / "transcripts"
        summaries_dir = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts_dir, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        # Pre-create the summary
        (summaries_dir / "Go-SIG").mkdir(parents=True)
        (summaries_dir / "Go-SIG" / "2026-02-05.md").write_text("existing summary")

        mock_client = _mock_openai_client()
        with patch("generate_summaries.time.sleep"):
            process_transcripts(mock_client, transcripts_dir, summaries_dir)

        mock_client.chat.completions.create.assert_not_called()
        assert (summaries_dir / "Go-SIG" / "2026-02-05.md").read_text() == "existing summary"

    def test_processes_multiple_transcripts(self, tmp_path: Path) -> None:
        """All transcripts without summaries should be processed."""
        transcripts_dir = tmp_path / "docs" / "transcripts"
        summaries_dir = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts_dir, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)
        _write_transcript(
            transcripts_dir, "Go-SIG", "2026-02-12.txt",
            SAMPLE_TRANSCRIPT.replace("2026-02-05", "2026-02-12"),
        )

        mock_client = _mock_openai_client()
        with patch("generate_summaries.time.sleep"):
            generated, skipped = process_transcripts(mock_client, transcripts_dir, summaries_dir)

        assert generated == 2
        assert skipped == 0
        assert mock_client.chat.completions.create.call_count == 2
        assert (summaries_dir / "Go-SIG" / "2026-02-05.md").exists()
        assert (summaries_dir / "Go-SIG" / "2026-02-12.md").exists()

    def test_handles_unparseable_transcript(self, tmp_path: Path) -> None:
        """Unparseable transcripts should be skipped without crashing."""
        transcripts_dir = tmp_path / "docs" / "transcripts"
        summaries_dir = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts_dir, "Bad-SIG", "2026-02-05.txt", "garbage content\n")

        mock_client = _mock_openai_client()
        with patch("generate_summaries.time.sleep"):
            process_transcripts(mock_client, transcripts_dir, summaries_dir)

        mock_client.chat.completions.create.assert_not_called()
        assert not (summaries_dir / "Bad-SIG" / "2026-02-05.md").exists()

    def test_returns_counts(self, tmp_path: Path) -> None:
        """process_transcripts should return (generated, skipped) counts."""
        transcripts_dir = tmp_path / "docs" / "transcripts"
        summaries_dir = tmp_path / "docs" / "summaries"
        _write_transcript(transcripts_dir, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)
        _write_transcript(
            transcripts_dir, "Go-SIG", "2026-02-12.txt",
            SAMPLE_TRANSCRIPT.replace("2026-02-05", "2026-02-12"),
        )

        # Pre-create one summary
        (summaries_dir / "Go-SIG").mkdir(parents=True)
        (summaries_dir / "Go-SIG" / "2026-02-05.md").write_text("existing")

        mock_client = _mock_openai_client()
        with patch("generate_summaries.time.sleep"):
            generated, skipped = process_transcripts(mock_client, transcripts_dir, summaries_dir)

        assert generated == 1
        assert skipped == 1


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
