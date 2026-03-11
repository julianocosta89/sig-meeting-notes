"""Tests for scripts/cleanup_trivial_meetings.py."""

from __future__ import annotations

from pathlib import Path

from scraper.transcript_io import MIN_TRANSCRIPT_LINES, SEPARATOR
from scripts.cleanup_trivial_meetings import find_trivial_summaries


def _write_transcript(base: Path, slug: str, date: str, line_count: int) -> Path:
    """Create a fake transcript.md with the given number of content lines."""
    meeting_dir = base / slug / date
    meeting_dir.mkdir(parents=True, exist_ok=True)
    lines = [f"SIG: {slug}", f"Date: {date}", "Duration: 30 minutes", SEPARATOR, ""]
    lines.extend(f"Speaker: utterance {i}" for i in range(line_count))
    (meeting_dir / "transcript.md").write_text("\n".join(lines), encoding="utf-8")
    return meeting_dir


class TestFindTrivialSummaries:
    def test_trivial_with_summary_detected(self, tmp_path: Path) -> None:
        """Trivial meeting with summary.md should be found."""
        meeting_dir = _write_transcript(tmp_path, "Go-SIG", "2026-03-01", 1)
        summary = meeting_dir / "summary.md"
        summary.write_text("## Key Topics\n- Nothing\n", encoding="utf-8")

        affected = find_trivial_summaries(tmp_path)
        assert len(affected) == 1
        assert affected[0] == summary

    def test_real_meeting_not_affected(self, tmp_path: Path) -> None:
        """Meeting with enough lines should not be affected."""
        meeting_dir = _write_transcript(tmp_path, "Go-SIG", "2026-03-01", MIN_TRANSCRIPT_LINES)
        summary = meeting_dir / "summary.md"
        summary.write_text("## Key Topics\n- Real topic\n", encoding="utf-8")

        affected = find_trivial_summaries(tmp_path)
        assert affected == []

    def test_trivial_without_summary_no_error(self, tmp_path: Path) -> None:
        """Trivial meeting without summary.md should not cause errors."""
        _write_transcript(tmp_path, "Go-SIG", "2026-03-01", 1)

        affected = find_trivial_summaries(tmp_path)
        assert affected == []

    def test_trivial_transcript_with_appended_section_detected(self, tmp_path: Path) -> None:
        """Trivial transcript followed by a Meeting Notes section should still be detected."""
        meeting_dir = tmp_path / "Go-SIG" / "2026-03-01"
        meeting_dir.mkdir(parents=True)
        # 1 transcript line + appended ## Meeting Notes with several lines
        text = (
            f"SIG: Go SIG\nDate: 2026-03-01\nDuration: 5 minutes\n{SEPARATOR}\n\n"
            "## Zoom Recording Transcript\n\n"
            "**Alice** 00:01 Okay\n"
            "## Meeting Notes\n\n"
            "- Attendee 1\n- Attendee 2\n- Attendee 3\n"
        )
        (meeting_dir / "transcript.md").write_text(text, encoding="utf-8")
        summary = meeting_dir / "summary.md"
        summary.write_text("## Key Topics\n- Hallucinated\n", encoding="utf-8")

        affected = find_trivial_summaries(tmp_path)
        assert len(affected) == 1
        assert affected[0] == summary


class TestDryRunVsExecute:
    def test_dry_run_does_not_delete(self, tmp_path: Path) -> None:
        """Dry-run should find but not delete."""
        meeting_dir = _write_transcript(tmp_path, "Go-SIG", "2026-03-01", 1)
        summary = meeting_dir / "summary.md"
        summary.write_text("## Key Topics\n- Nothing\n", encoding="utf-8")

        affected = find_trivial_summaries(tmp_path)
        assert len(affected) == 1
        # Dry-run: don't call unlink — file still exists
        assert summary.exists()

    def test_execute_deletes_summary_only(self, tmp_path: Path) -> None:
        """Execute mode should delete summary.md but leave transcript.md."""
        meeting_dir = _write_transcript(tmp_path, "Go-SIG", "2026-03-01", 1)
        summary = meeting_dir / "summary.md"
        summary.write_text("## Key Topics\n- Nothing\n", encoding="utf-8")
        transcript = meeting_dir / "transcript.md"

        affected = find_trivial_summaries(tmp_path)
        for path in affected:
            path.unlink()

        assert not summary.exists()
        assert transcript.exists()
