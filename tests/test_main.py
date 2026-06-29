"""Tests for main.py — transcript processing logic."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import main
from main import (
    _ensure_metadata,
    _format_body_line,
    _parse_date,
    _resolve_sig,
    _write_meeting_notes,
    write_transcript,
)

# ---------------------------------------------------------------------------
# _write_meeting_notes
# ---------------------------------------------------------------------------


class TestWriteMeetingNotes:
    def test_writes_both_sections(self, tmp_path):
        notes_path = tmp_path / "meeting-notes.md"
        notes = {"attendees": ["- Alice", "- Bob"], "agenda": ["- Item 1"]}
        result = _write_meeting_notes(notes_path, notes)

        assert result is True
        assert notes_path.exists()
        content = notes_path.read_text()
        assert "## Meeting Notes" in content
        assert "### Attendees" in content
        assert "- Alice" in content
        assert "### Agenda" in content
        assert "- Item 1" in content

    def test_writes_attendees_only(self, tmp_path):
        notes_path = tmp_path / "meeting-notes.md"
        notes = {"attendees": ["- Alice"], "agenda": []}
        result = _write_meeting_notes(notes_path, notes)

        assert result is True
        content = notes_path.read_text()
        assert "### Attendees" in content
        assert "### Agenda" not in content

    def test_writes_agenda_only(self, tmp_path):
        notes_path = tmp_path / "meeting-notes.md"
        notes = {"attendees": [], "agenda": ["- Item 1"]}
        result = _write_meeting_notes(notes_path, notes)

        assert result is True
        content = notes_path.read_text()
        assert "### Agenda" in content
        assert "### Attendees" not in content

    def test_returns_false_when_empty(self, tmp_path):
        notes_path = tmp_path / "meeting-notes.md"
        notes = {"attendees": [], "agenda": []}
        result = _write_meeting_notes(notes_path, notes)

        assert result is False
        assert not notes_path.exists()


# ---------------------------------------------------------------------------
# _format_body_line
# ---------------------------------------------------------------------------


class TestFormatBodyLine:
    def test_formats_speaker_line(self):
        assert _format_body_line("Alice 0:01 Hello") == "**Alice** 0:01 Hello"

    def test_returns_plain_line_unchanged(self):
        # Lines that don't match the speaker-timestamp pattern pass through as-is.
        assert _format_body_line("plain text") == "plain text"
        assert _format_body_line("") == ""


# ---------------------------------------------------------------------------
# _parse_date
# ---------------------------------------------------------------------------


class TestParseDate:
    def test_valid_date(self):
        from datetime import datetime

        result = _parse_date("2026-06-16", "--since")
        assert result == datetime(2026, 6, 16)

    def test_invalid_date_returns_none(self):
        assert _parse_date("not-a-date", "--since") is None

    def test_invalid_format_returns_none(self):
        assert _parse_date("16/06/2026", "--between") is None


# ---------------------------------------------------------------------------
# _ensure_metadata — cold-start (no metadata.md yet)
# ---------------------------------------------------------------------------


class TestEnsureMetadata:
    def test_cold_start_creates_metadata_with_url(self, tmp_path):
        sig_dir = tmp_path / "Test-SIG"
        sig_dir.mkdir()
        transcript_path = sig_dir / "2026-06-16" / "transcript.md"
        transcript_path.parent.mkdir()

        meeting = MagicMock()
        meeting.sig_name = "Test SIG"
        meeting.sig_slug = "Test-SIG"

        with patch("scraper.community.get_meeting_notes_url", return_value="https://doc.url"):
            result = _ensure_metadata(meeting, transcript_path)

        assert result == "https://doc.url"
        metadata = (sig_dir / "metadata.md").read_text()
        assert "Meeting Notes: https://doc.url" in metadata

    def test_cold_start_creates_metadata_without_url(self, tmp_path):
        sig_dir = tmp_path / "Test-SIG"
        sig_dir.mkdir()
        transcript_path = sig_dir / "2026-06-16" / "transcript.md"
        transcript_path.parent.mkdir()

        meeting = MagicMock()
        meeting.sig_name = "Test SIG"
        meeting.sig_slug = "Test-SIG"

        with patch("scraper.community.get_meeting_notes_url", return_value=""):
            result = _ensure_metadata(meeting, transcript_path)

        assert result == ""
        assert (sig_dir / "metadata.md").exists()


# ---------------------------------------------------------------------------
# _resolve_sig
# ---------------------------------------------------------------------------


class TestResolveSig:
    def _make_meetings(self, slugs):
        meetings = []
        for slug in slugs:
            m = MagicMock()
            m.sig_slug = slug
            meetings.append(m)
        return meetings

    def test_no_match_returns_none(self):
        meetings = self._make_meetings(["Go-SIG", "Java-SIG"])
        assert _resolve_sig(meetings, "python") is None

    def test_single_match_returns_slug(self):
        meetings = self._make_meetings(["Go-SIG", "Python-SIG", "Java-SIG"])
        assert _resolve_sig(meetings, "python") == "Python-SIG"

    def test_alias_expansion(self):
        meetings = self._make_meetings(["Semantic-Convention-SIG", "Java-SIG"])
        assert _resolve_sig(meetings, "semconv") == "Semantic-Convention-SIG"

    def test_multi_match_valid_selection(self):
        meetings = self._make_meetings(["Go-SIG", "Go-Compile-Time-SIG"])
        with patch("builtins.input", return_value="1"):
            result = _resolve_sig(meetings, "go")
        assert result in ("Go-Compile-Time-SIG", "Go-SIG")

    def test_multi_match_eof_returns_none(self):
        meetings = self._make_meetings(["Go-SIG", "Go-Compile-Time-SIG"])
        with patch("builtins.input", side_effect=EOFError):
            result = _resolve_sig(meetings, "go")
        assert result is None

    def test_multi_match_invalid_then_valid(self):
        meetings = self._make_meetings(["Go-SIG", "Go-Compile-Time-SIG"])
        # First call: non-numeric (ValueError), second: out-of-range, third: valid
        with patch("builtins.input", side_effect=["not-a-number", "99", "1"]):
            result = _resolve_sig(meetings, "go")
        assert result is not None


# ---------------------------------------------------------------------------
# process_meetings — happy path (new transcript scraped from Zoom)
# ---------------------------------------------------------------------------


class TestProcessMeetingsExceptions:
    """Exception paths inside the Playwright scrape loop."""

    def _setup(self, tmp_path):
        meeting = _make_meeting(tmp_path)
        transcript_path = tmp_path / "content" / meeting.sig_slug / "2026-06-16" / "transcript.md"
        transcript_path.parent.mkdir(parents=True)
        metadata_path = transcript_path.parent.parent / "metadata.md"
        metadata_path.write_text(
            "SIG: Test SIG\nMeeting Notes: https://docs.google.com/document/d/abc\n"
        )
        return meeting, transcript_path

    def _patched_pw(self):
        mock_page = MagicMock()
        mock_context = MagicMock()
        mock_context.new_page.return_value = mock_page
        mock_browser = MagicMock()
        mock_browser.new_context.return_value = mock_context
        mock_pw = MagicMock()
        mock_pw.__enter__ = MagicMock(return_value=mock_pw)
        mock_pw.__exit__ = MagicMock(return_value=False)
        mock_pw.chromium.launch.return_value = mock_browser
        return mock_pw

    def test_zoom_scrape_error_counts_as_skipped(self, tmp_path):
        from scraper.zoom import ZoomScrapeError

        meeting, _ = self._setup(tmp_path)
        mock_pw = self._patched_pw()

        with (
            patch.object(main, "TRANSCRIPTS_DIR", tmp_path / "content"),
            patch("main.sync_playwright", return_value=mock_pw),
            patch("scraper.gdoc.fetch_meeting_notes", return_value={"attendees": [], "agenda": []}),
            patch("main.scrape_transcript", side_effect=ZoomScrapeError("expired")),
        ):
            tracer = MagicMock()
            tracer.start_as_current_span.return_value.__enter__ = MagicMock(
                return_value=MagicMock()
            )
            tracer.start_as_current_span.return_value.__exit__ = MagicMock(return_value=False)
            errors, skipped, urls = main.process_meetings([meeting], tracer)

        assert errors == 0
        assert skipped == 1
        assert meeting.url in urls

    def test_unexpected_exception_counts_as_error(self, tmp_path):
        meeting, _ = self._setup(tmp_path)
        mock_pw = self._patched_pw()

        with (
            patch.object(main, "TRANSCRIPTS_DIR", tmp_path / "content"),
            patch("main.sync_playwright", return_value=mock_pw),
            patch("scraper.gdoc.fetch_meeting_notes", return_value={"attendees": [], "agenda": []}),
            patch("main.scrape_transcript", side_effect=RuntimeError("boom")),
        ):
            tracer = MagicMock()
            tracer.start_as_current_span.return_value.__enter__ = MagicMock(
                return_value=MagicMock()
            )
            tracer.start_as_current_span.return_value.__exit__ = MagicMock(return_value=False)
            errors, skipped, urls = main.process_meetings([meeting], tracer)

        assert errors == 1
        assert skipped == 0
        assert meeting.url in urls


class TestProcessMeetingsHappyPath:
    def test_scrapes_and_writes_transcript(self, tmp_path):
        meeting = _make_meeting(tmp_path)

        # No pre-existing transcript
        transcript_path = tmp_path / "content" / meeting.sig_slug / "2026-06-16" / "transcript.md"
        transcript_path.parent.mkdir(parents=True)
        # metadata.md with a notes URL
        metadata_path = transcript_path.parent.parent / "metadata.md"
        metadata_path.write_text(
            "SIG: Test SIG\nMeeting Notes: https://docs.google.com/document/d/abc\n"
        )

        fake_lines = ["Speaker 0:01 Hello"]
        fake_notes = {"attendees": ["- Alice"], "agenda": ["- Item 1"]}

        mock_page = MagicMock()
        mock_context = MagicMock()
        mock_context.new_page.return_value = mock_page
        mock_browser = MagicMock()
        mock_browser.new_context.return_value = mock_context

        mock_pw = MagicMock()
        mock_pw.__enter__ = MagicMock(return_value=mock_pw)
        mock_pw.__exit__ = MagicMock(return_value=False)
        mock_pw.chromium.launch.return_value = mock_browser

        with (
            patch.object(main, "TRANSCRIPTS_DIR", tmp_path / "content"),
            patch("main.sync_playwright", return_value=mock_pw),
            patch("scraper.gdoc.fetch_meeting_notes", return_value=fake_notes),
            patch("main.scrape_transcript", return_value=fake_lines),
        ):
            tracer = MagicMock()
            tracer.start_as_current_span.return_value.__enter__ = MagicMock(
                return_value=MagicMock()
            )
            tracer.start_as_current_span.return_value.__exit__ = MagicMock(return_value=False)

            errors, skipped, _ = main.process_meetings([meeting], tracer)

        assert errors == 0
        assert skipped == 0
        assert transcript_path.exists()
        assert "Speaker" in transcript_path.read_text()
        notes_path = transcript_path.parent / "meeting-notes.md"
        assert notes_path.exists()
        assert "- Alice" in notes_path.read_text()


# ---------------------------------------------------------------------------
# write_transcript
# ---------------------------------------------------------------------------


class TestWriteTranscript:
    def _make_meeting(self):
        from datetime import datetime

        m = MagicMock()
        m.sig_name = "Test SIG"
        m.sig_slug = "Test-SIG"
        m.start_date = datetime(2026, 6, 16)
        m.duration_minutes = 30
        return m

    def test_writes_transcript_file(self, tmp_path):
        meeting = self._make_meeting()
        path = tmp_path / "transcript.md"
        write_transcript(path, meeting, ["Speaker 0:01 Hello"])
        assert path.exists()
        content = path.read_text()
        assert "SIG: Test SIG" in content
        assert "**Speaker** 0:01 Hello" in content

    def test_writes_meeting_notes_when_notes_provided(self, tmp_path):
        meeting = self._make_meeting()
        path = tmp_path / "transcript.md"
        notes = {"attendees": ["- Alice"], "agenda": ["- Item 1"]}
        write_transcript(path, meeting, [], notes=notes)
        notes_path = tmp_path / "meeting-notes.md"
        assert notes_path.exists()
        assert "- Alice" in notes_path.read_text()

    def test_no_meeting_notes_when_notes_is_none(self, tmp_path):
        meeting = self._make_meeting()
        path = tmp_path / "transcript.md"
        write_transcript(path, meeting, [], notes=None)
        assert not (tmp_path / "meeting-notes.md").exists()

    def test_no_meeting_notes_when_notes_is_empty(self, tmp_path):
        meeting = self._make_meeting()
        path = tmp_path / "transcript.md"
        write_transcript(path, meeting, [], notes={"attendees": [], "agenda": []})
        assert not (tmp_path / "meeting-notes.md").exists()


# ---------------------------------------------------------------------------
# Backfill path in process_meetings: transcript exists, meeting-notes missing
# ---------------------------------------------------------------------------


def _make_meeting(tmp_path: Path, slug: str = "Test-SIG", date: str = "2026-06-16"):
    """Return a minimal Meeting-like object for testing."""
    from datetime import datetime

    m = MagicMock()
    m.sig_name = "Test SIG"
    m.sig_slug = slug
    m.start_date = datetime.strptime(date, "%Y-%m-%d")
    m.duration_minutes = 30
    m.url = "https://zoom.us/rec/share/test"
    return m


class TestProcessMeetingsBackfill:
    """When transcript.md exists but meeting-notes.md doesn't, notes are backfilled."""

    def test_backfills_missing_notes(self, tmp_path):
        meeting = _make_meeting(tmp_path)

        # Pre-create transcript.md so the skip path is taken
        transcript_path = tmp_path / "content" / meeting.sig_slug / "2026-06-16" / "transcript.md"
        transcript_path.parent.mkdir(parents=True)
        transcript_path.write_text("SIG: Test SIG\nDate: 2026-06-16\n")

        # Also create metadata.md with a notes URL
        metadata_path = transcript_path.parent.parent / "metadata.md"
        metadata_path.write_text(
            "SIG: Test SIG\nMeeting Notes: https://docs.google.com/document/d/abc\n"
        )

        fake_notes = {"attendees": ["- Alice"], "agenda": ["- Topic 1"]}

        with (
            patch.object(main, "TRANSCRIPTS_DIR", tmp_path / "content"),
            patch("scraper.gdoc.fetch_meeting_notes", return_value=fake_notes),
            patch("main.sync_playwright"),
        ):
            tracer = MagicMock()
            tracer.start_as_current_span.return_value.__enter__ = MagicMock(
                return_value=MagicMock()
            )
            tracer.start_as_current_span.return_value.__exit__ = MagicMock(return_value=False)

            main.process_meetings([meeting], tracer)

        notes_path = transcript_path.parent / "meeting-notes.md"
        assert notes_path.exists(), "meeting-notes.md should be written during backfill"
        content = notes_path.read_text()
        assert "- Alice" in content
        assert "- Topic 1" in content

    def test_skips_backfill_when_notes_already_exist(self, tmp_path):
        meeting = _make_meeting(tmp_path)

        transcript_path = tmp_path / "content" / meeting.sig_slug / "2026-06-16" / "transcript.md"
        transcript_path.parent.mkdir(parents=True)
        transcript_path.write_text("SIG: Test SIG\n")

        notes_path = transcript_path.parent / "meeting-notes.md"
        notes_path.write_text("## Meeting Notes\n\n### Attendees\n- Existing\n")

        with (
            patch.object(main, "TRANSCRIPTS_DIR", tmp_path / "content"),
            patch("scraper.gdoc.fetch_meeting_notes") as mock_fetch,
            patch("main.sync_playwright"),
        ):
            tracer = MagicMock()
            tracer.start_as_current_span.return_value.__enter__ = MagicMock(
                return_value=MagicMock()
            )
            tracer.start_as_current_span.return_value.__exit__ = MagicMock(return_value=False)

            main.process_meetings([meeting], tracer)

        mock_fetch.assert_not_called()

    def test_no_backfill_when_no_notes_url(self, tmp_path):
        meeting = _make_meeting(tmp_path)

        transcript_path = tmp_path / "content" / meeting.sig_slug / "2026-06-16" / "transcript.md"
        transcript_path.parent.mkdir(parents=True)
        transcript_path.write_text("SIG: Test SIG\n")

        # metadata.md exists but has no Meeting Notes URL
        metadata_path = transcript_path.parent.parent / "metadata.md"
        metadata_path.write_text("SIG: Test SIG\nMeeting Notes: \n")

        with (
            patch.object(main, "TRANSCRIPTS_DIR", tmp_path / "content"),
            patch("scraper.gdoc.fetch_meeting_notes") as mock_fetch,
            patch("main.sync_playwright"),
        ):
            tracer = MagicMock()
            tracer.start_as_current_span.return_value.__enter__ = MagicMock(
                return_value=MagicMock()
            )
            tracer.start_as_current_span.return_value.__exit__ = MagicMock(return_value=False)

            main.process_meetings([meeting], tracer)

        mock_fetch.assert_not_called()
        assert not (transcript_path.parent / "meeting-notes.md").exists()

    def test_no_backfill_when_notes_empty(self, tmp_path):
        meeting = _make_meeting(tmp_path)

        transcript_path = tmp_path / "content" / meeting.sig_slug / "2026-06-16" / "transcript.md"
        transcript_path.parent.mkdir(parents=True)
        transcript_path.write_text("SIG: Test SIG\n")

        metadata_path = transcript_path.parent.parent / "metadata.md"
        metadata_path.write_text(
            "SIG: Test SIG\nMeeting Notes: https://docs.google.com/document/d/abc\n"
        )

        with (
            patch.object(main, "TRANSCRIPTS_DIR", tmp_path / "content"),
            patch(
                "scraper.gdoc.fetch_meeting_notes",
                return_value={"attendees": [], "agenda": []},
            ),
            patch("main.sync_playwright"),
        ):
            tracer = MagicMock()
            tracer.start_as_current_span.return_value.__enter__ = MagicMock(
                return_value=MagicMock()
            )
            tracer.start_as_current_span.return_value.__exit__ = MagicMock(return_value=False)

            main.process_meetings([meeting], tracer)

        assert not (transcript_path.parent / "meeting-notes.md").exists()
