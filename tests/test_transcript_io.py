"""Tests for scraper.transcript_io helpers."""

from scraper.transcript_io import SEPARATOR, count_transcript_lines, extract_transcript_body


class TestCountTranscriptLines:
    def test_empty_body(self):
        assert count_transcript_lines("") == 0

    def test_only_headings_and_blanks(self):
        body = "## Zoom Recording Transcript\n\n### Section\n\n"
        assert count_transcript_lines(body) == 0

    def test_mixed_headings_and_real_lines(self):
        body = (
            "## Zoom Recording Transcript\n"
            "\n"
            "**Alice** 00:01 Hello everyone\n"
            "### Break\n"
            "**Bob** 00:05 Thanks for joining\n"
        )
        assert count_transcript_lines(body) == 2

    def test_real_transcript_content(self):
        body = (
            "**Alice** 00:01 Hello everyone\n"
            "**Bob** 00:05 Thanks for joining\n"
            "**Alice** 00:10 Let's get started\n"
            "**Bob** 00:15 Sounds good\n"
        )
        assert count_transcript_lines(body) == 4

    def test_localized_transcript_line(self):
        body = "**Fernando Grimaldo** 13:47 Okay…"
        assert count_transcript_lines(body) == 1


class TestExtractTranscriptBody:
    def test_extracts_transcript_section(self):
        text = (
            f"SIG: Go SIG\nDate: 2026-01-01\nDuration: 30 minutes\n{SEPARATOR}\n\n"
            "## Zoom Recording Transcript\n\n"
            "**Alice** 00:01 Hello\n"
            "**Bob** 00:05 Thanks\n"
        )
        body = extract_transcript_body(text)
        assert "**Alice** 00:01 Hello" in body
        assert "SIG: Go SIG" not in body

    def test_falls_back_to_all_content_after_separator(self):
        text = f"SIG: Go SIG\n{SEPARATOR}\n\n**Alice** 00:01 Hello\n"
        body = extract_transcript_body(text)
        assert "**Alice** 00:01 Hello" in body

    def test_no_separator_returns_empty(self):
        assert extract_transcript_body("no separator here") == ""
