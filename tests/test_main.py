"""Tests for main.py — transcript processing logic."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import main
from main import _write_meeting_notes

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
