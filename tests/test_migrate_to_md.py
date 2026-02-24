"""Tests for scripts/migrate_to_md.py."""
from __future__ import annotations

import textwrap
from pathlib import Path
from unittest.mock import patch

import pytest

from scripts.migrate_to_md import (
    _build_md_content,
    _format_body_line,
    ensure_metadata,
    migrate,
    migrate_file,
)
from scraper.transcript_io import SEPARATOR, parse_header, parse_reference

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_OLD_TRANSCRIPT = textwrap.dedent("""\
    SIG: Go SIG
    Date: 2026-02-05
    Duration: 33 minutes
    Source URL: https://zoom.us/rec/share/example
    ============================================================

    Tyler 02:14 Hey, Damien.
    Damien Mathieu 02:19 Hey!
    How's it going?
""")

_EXPECTED_HEADER_LINES = [
    "SIG: Go SIG",
    "Date: 2026-02-05",
    "Duration: 33 minutes",
    "Zoom Recording URL: https://zoom.us/rec/share/example",
    SEPARATOR,
]


# ---------------------------------------------------------------------------
# _format_body_line
# ---------------------------------------------------------------------------

class TestFormatBodyLine:
    def test_speaker_line_gets_bold(self) -> None:
        assert _format_body_line("Tyler 02:14 Hey.") == "**Tyler** 02:14 Hey."

    def test_multi_word_speaker(self) -> None:
        result = _format_body_line("Damien Mathieu 02:19 Hey!")
        assert result == "**Damien Mathieu** 02:19 Hey."[:-1] + "!"

    def test_continuation_line_unchanged(self) -> None:
        assert _format_body_line("How's it going?") == "How's it going?"

    def test_empty_line_unchanged(self) -> None:
        assert _format_body_line("") == ""

    def test_utterance_can_be_empty(self) -> None:
        assert _format_body_line("Tyler 02:14 ") == "**Tyler** 02:14 "


# ---------------------------------------------------------------------------
# _build_md_content
# ---------------------------------------------------------------------------

class TestBuildMdContent:
    def _header(self) -> dict:
        return {
            "sig_name": "Go SIG",
            "date": "2026-02-05",
            "duration_minutes": 33,
            "source_url": "https://zoom.us/rec/share/example",
        }

    def test_header_fields_present(self) -> None:
        content = _build_md_content(self._header(), [])
        for line in _EXPECTED_HEADER_LINES:
            assert line in content

    def test_old_source_url_key_not_present(self) -> None:
        content = _build_md_content(self._header(), [])
        assert "Source URL:" not in content

    def test_meeting_notes_section_present(self) -> None:
        content = _build_md_content(self._header(), [])
        assert "## Meeting Notes" in content

    def test_transcript_section_present(self) -> None:
        content = _build_md_content(self._header(), [])
        assert "## Zoom Recording Transcript" in content

    def test_body_lines_converted(self) -> None:
        content = _build_md_content(self._header(), ["Tyler 02:14 Hey."])
        assert "**Tyler** 02:14 Hey." in content

    def test_continuation_lines_preserved(self) -> None:
        content = _build_md_content(self._header(), ["How's it going?"])
        assert "How's it going?" in content

    def test_ends_with_newline(self) -> None:
        content = _build_md_content(self._header(), [])
        assert content.endswith("\n")

    def test_result_parseable_by_parse_header(self, tmp_path: Path) -> None:
        content = _build_md_content(self._header(), [])
        p = tmp_path / "2026-02-05.md"
        p.write_text(content)
        parsed = parse_header(p)
        assert parsed is not None
        assert parsed["sig_name"] == "Go SIG"
        assert parsed["date"] == "2026-02-05"
        assert parsed["duration_minutes"] == 33
        assert parsed["source_url"] == "https://zoom.us/rec/share/example"


# ---------------------------------------------------------------------------
# migrate_file
# ---------------------------------------------------------------------------

class TestMigrateFile:
    def test_dry_run_does_not_write_files(self, tmp_path: Path) -> None:
        txt = tmp_path / "2026-02-05.txt"
        txt.write_text(_OLD_TRANSCRIPT)
        result = migrate_file(txt, dry_run=True)
        assert result is True
        assert txt.exists()
        assert not (tmp_path / "2026-02-05.md").exists()

    def test_execute_creates_md_and_removes_txt(self, tmp_path: Path) -> None:
        txt = tmp_path / "2026-02-05.txt"
        txt.write_text(_OLD_TRANSCRIPT)
        result = migrate_file(txt, dry_run=False)
        assert result is True
        assert not txt.exists()
        assert (tmp_path / "2026-02-05.md").exists()

    def test_md_content_is_correct(self, tmp_path: Path) -> None:
        txt = tmp_path / "2026-02-05.txt"
        txt.write_text(_OLD_TRANSCRIPT)
        migrate_file(txt, dry_run=False)
        content = (tmp_path / "2026-02-05.md").read_text()
        assert "Zoom Recording URL:" in content
        assert "Source URL:" not in content
        assert "**Tyler** 02:14 Hey, Damien." in content
        assert "**Damien Mathieu** 02:19 Hey!" in content
        assert "How's it going?" in content
        assert "## Zoom Recording Transcript" in content

    def test_malformed_header_is_skipped(self, tmp_path: Path) -> None:
        txt = tmp_path / "bad.txt"
        txt.write_text("NOT A VALID HEADER\n")
        result = migrate_file(txt, dry_run=False)
        assert result is False
        assert txt.exists()  # not deleted

    def test_missing_separator_is_skipped(self, tmp_path: Path) -> None:
        txt = tmp_path / "nosep.txt"
        txt.write_text("SIG: Go SIG\nDate: 2026-02-05\nDuration: 1 minutes\nSource URL: x\n")
        result = migrate_file(txt, dry_run=False)
        assert result is False


# ---------------------------------------------------------------------------
# ensure_metadata
# ---------------------------------------------------------------------------

class TestEnsureMetadata:
    def test_creates_metadata_when_absent(self, tmp_path: Path) -> None:
        with patch("scripts.migrate_to_md.community.get_meeting_notes_url", return_value=""):
            ensure_metadata(tmp_path, "Go SIG", dry_run=False)
        assert (tmp_path / "metadata.md").exists()

    def test_metadata_content(self, tmp_path: Path) -> None:
        with patch(
            "scripts.migrate_to_md.community.get_meeting_notes_url",
            return_value="https://docs.google.com/document/d/go-doc/edit",
        ):
            ensure_metadata(tmp_path, "Go SIG", dry_run=False)
        ref = parse_reference(tmp_path / "metadata.md")
        assert ref is not None
        assert ref["sig_name"] == "Go SIG"
        assert ref["meeting_notes_url"] == "https://docs.google.com/document/d/go-doc/edit"

    def test_does_not_overwrite_existing_metadata(self, tmp_path: Path) -> None:
        existing = tmp_path / "metadata.md"
        existing.write_text("SIG: Go SIG\nMeeting Notes: https://original\nRepository: \n")
        with patch("scripts.migrate_to_md.community.get_meeting_notes_url", return_value="https://new"):
            ensure_metadata(tmp_path, "Go SIG", dry_run=False)
        ref = parse_reference(existing)
        assert ref is not None
        assert ref["meeting_notes_url"] == "https://original"

    def test_dry_run_does_not_write(self, tmp_path: Path) -> None:
        with patch("scripts.migrate_to_md.community.get_meeting_notes_url", return_value=""):
            ensure_metadata(tmp_path, "Go SIG", dry_run=True)
        assert not (tmp_path / "metadata.md").exists()


# ---------------------------------------------------------------------------
# migrate (full run)
# ---------------------------------------------------------------------------

class TestMigrate:
    def _make_tree(self, tmp_path: Path) -> Path:
        transcripts = tmp_path / "transcripts"
        sig = transcripts / "Go-SIG"
        sig.mkdir(parents=True)
        (sig / "2026-02-05.txt").write_text(_OLD_TRANSCRIPT)
        (sig / "2026-02-12.txt").write_text(_OLD_TRANSCRIPT.replace("02-05", "02-12"))
        return transcripts

    def test_dry_run_migrates_nothing(self, tmp_path: Path) -> None:
        transcripts = self._make_tree(tmp_path)
        with patch("scripts.migrate_to_md.community.get_meeting_notes_url", return_value=""):
            migrate(transcripts, dry_run=True)
        assert len(list(transcripts.glob("**/*.txt"))) == 2
        assert len(list(transcripts.glob("**/*.md"))) == 0

    def test_execute_migrates_all_files(self, tmp_path: Path) -> None:
        transcripts = self._make_tree(tmp_path)
        with patch("scripts.migrate_to_md.community.get_meeting_notes_url", return_value=""):
            migrate(transcripts, dry_run=False)
        assert len(list(transcripts.glob("**/*.txt"))) == 0
        assert sorted(f.name for f in transcripts.glob("**/*.md")) == [
            "2026-02-05.md",
            "2026-02-12.md",
            "metadata.md",
        ]

    def test_returns_zero_on_full_success(self, tmp_path: Path) -> None:
        transcripts = self._make_tree(tmp_path)
        with patch("scripts.migrate_to_md.community.get_meeting_notes_url", return_value=""):
            failures = migrate(transcripts, dry_run=False)
        assert failures == 0

    def test_returns_nonzero_on_skipped_files(self, tmp_path: Path) -> None:
        transcripts = tmp_path / "transcripts"
        sig = transcripts / "Go-SIG"
        sig.mkdir(parents=True)
        (sig / "bad.txt").write_text("NOT VALID\n")
        with patch("scripts.migrate_to_md.community.get_meeting_notes_url", return_value=""):
            failures = migrate(transcripts, dry_run=False)
        assert failures == 1

    def test_empty_transcripts_dir(self, tmp_path: Path) -> None:
        transcripts = tmp_path / "transcripts"
        transcripts.mkdir()
        failures = migrate(transcripts, dry_run=False)
        assert failures == 0
