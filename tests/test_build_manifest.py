"""Tests for build_site.py manifest builder."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from build_site import build_manifest, build_speakers_index, iter_meetings_jsonl, parse_summary
from build_site import main as build_main
from scraper.transcript_io import parse_header

SAMPLE_TRANSCRIPT = """\
SIG: Go SIG
Date: 2026-02-05
Duration: 33 minutes
Source URL: https://zoom.us/rec/share/abc123
============================================================

Tyler 02:14 Hey, Damien.
Damien Mathieu 02:19 Hey!
"""

SAMPLE_TRANSCRIPT_2 = """\
SIG: Go SIG
Date: 2026-02-12
Duration: 45 minutes
Source URL: https://zoom.us/rec/share/def456
============================================================

Tyler 02:00 Welcome everyone.
"""

SAMPLE_TRANSCRIPT_JAVA = """\
SIG: Java SIG
Date: 2026-02-05
Duration: 60 minutes
Source URL: https://zoom.us/rec/share/java123
============================================================

Jack 00:01 Hello!
"""

SAMPLE_TRANSCRIPT_RENAMED = """\
SIG: Go Instrumentation SIG
Date: 2026-02-19
Duration: 50 minutes
Source URL: https://zoom.us/rec/share/ghi789
============================================================

Tyler 02:00 We renamed the SIG.
"""

SAMPLE_TRANSCRIPT_TRIVIAL = """\
SIG: Go SIG
Date: 2026-02-20
Duration: 2 minutes
Source URL: https://zoom.us/rec/share/trivial123
============================================================

## Zoom Recording Transcript

**Tyler** 00:01 Hello?
"""

SAMPLE_METADATA = """\
SIG: Go SIG
Meeting Notes: https://docs.google.com/document/d/go-doc/edit
Repository: https://github.com/open-telemetry/opentelemetry-go
"""

SAMPLE_SUMMARY = """\
## Key Topics
- Discussion on merging PRs related to instrumentation release.
- Debate on the necessity and content of `agents.md`.

## Action Items
- Jack Berg to refine the `agents.md`.

## Participants
Trask Stalnaker, John Watson, Jack Berg
"""


def _write_transcript(base: Path, slug: str, filename: str, content: str) -> None:
    date = Path(filename).stem  # e.g. "2026-02-05"
    d = base / slug / date
    d.mkdir(parents=True, exist_ok=True)
    (d / "transcript.md").write_text(content, encoding="utf-8")


def _write_metadata(base: Path, slug: str, content: str = SAMPLE_METADATA) -> None:
    d = base / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "metadata.md").write_text(content, encoding="utf-8")


class TestParseHeader:
    def test_valid_header(self, tmp_path: Path) -> None:
        p = tmp_path / "test.txt"
        p.write_text(SAMPLE_TRANSCRIPT, encoding="utf-8")
        result = parse_header(p)
        assert result is not None
        assert result["sig_name"] == "Go SIG"
        assert result["date"] == "2026-02-05"
        assert result["duration_minutes"] == 33
        assert result["source_url"] == "https://zoom.us/rec/share/abc123"

    def test_new_format_zoom_recording_url(self, tmp_path: Path) -> None:
        p = tmp_path / "test.md"
        p.write_text(
            "SIG: Go SIG\nDate: 2026-02-05\nDuration: 33 minutes\n"
            "Zoom Recording URL: https://zoom.us/rec/share/abc123\n"
            "============================================================\n"
        )
        result = parse_header(p)
        assert result is not None
        assert result["source_url"] == "https://zoom.us/rec/share/abc123"

    def test_missing_sig_prefix(self, tmp_path: Path) -> None:
        p = tmp_path / "bad.txt"
        p.write_text("Name: Go SIG\nDate: 2026-02-05\nDuration: 33 minutes\nSource URL: x\n===\n")
        assert parse_header(p) is None

    def test_missing_date_prefix(self, tmp_path: Path) -> None:
        p = tmp_path / "bad.txt"
        p.write_text("SIG: Go SIG\nWhen: 2026-02-05\nDuration: 33 minutes\nSource URL: x\n===\n")
        assert parse_header(p) is None

    def test_missing_duration_prefix(self, tmp_path: Path) -> None:
        p = tmp_path / "bad.txt"
        p.write_text("SIG: Go SIG\nDate: 2026-02-05\nLength: 33 minutes\nSource URL: x\n===\n")
        assert parse_header(p) is None

    def test_missing_url_prefix(self, tmp_path: Path) -> None:
        p = tmp_path / "bad.txt"
        p.write_text("SIG: Go SIG\nDate: 2026-02-05\nDuration: 33 minutes\nURL: x\n===\n")
        assert parse_header(p) is None

    def test_nonexistent_file(self, tmp_path: Path) -> None:
        assert parse_header(tmp_path / "nope.txt") is None

    def test_single_minute(self, tmp_path: Path) -> None:
        p = tmp_path / "test.txt"
        content = SAMPLE_TRANSCRIPT.replace("33 minutes", "1 minute")
        p.write_text(content, encoding="utf-8")
        result = parse_header(p)
        assert result is not None
        assert result["duration_minutes"] == 1


class TestBuildManifest:
    def test_basic_manifest(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert len(manifest["sigs"]) == 1
        sig = manifest["sigs"][0]
        assert sig["slug"] == "Go-SIG"
        assert sig["name"] == "Go SIG"
        assert len(sig["meetings"]) == 1
        assert sig["meetings"][0]["date"] == "2026-02-05"
        assert sig["meetings"][0]["duration_minutes"] == 33
        assert sig["meetings"][0]["has_summary"] is False

    def test_sig_metadata_from_metadata_md(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_metadata(src, "Go-SIG")

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        sig = manifest["sigs"][0]
        assert sig["meeting_notes_url"] == "https://docs.google.com/document/d/go-doc/edit"
        assert sig["repository_url"] == "https://github.com/open-telemetry/opentelemetry-go"

    def test_sig_metadata_empty_when_no_metadata_md(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        sig = manifest["sigs"][0]
        assert sig["meeting_notes_url"] == ""
        assert sig["repository_url"] == ""

    def test_metadata_md_not_included_as_meeting(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_metadata(src, "Go-SIG")

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert len(manifest["sigs"][0]["meetings"]) == 1

    def test_meetings_sorted_descending(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        meetings = manifest["sigs"][0]["meetings"]
        assert len(meetings) == 2
        assert meetings[0]["date"] == "2026-02-12"
        assert meetings[1]["date"] == "2026-02-05"

    def test_sigs_sorted_alphabetically(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Java-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT_JAVA)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        slugs = [s["slug"] for s in manifest["sigs"]]
        assert slugs == ["Go-SIG", "Java-SIG"]

    def test_has_summary_true(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        # Summary lives as a sibling of transcript.md
        (src / "Go-SIG" / "2026-02-05" / "summary.md").write_text("# Summary\n")

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"][0]["meetings"][0]["has_summary"] is True

    def test_generated_at_present(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert "generated_at" in manifest
        assert manifest["generated_at"].endswith("Z")

    def test_empty_transcripts_dir(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        src.mkdir(parents=True)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"] == []

    def test_duration_values(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        meetings = manifest["sigs"][0]["meetings"]
        durations = {m["date"]: m["duration_minutes"] for m in meetings}
        assert durations["2026-02-05"] == 33
        assert durations["2026-02-12"] == 45

    def test_display_name_from_latest_transcript(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-19.md", SAMPLE_TRANSCRIPT_RENAMED)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        sig = manifest["sigs"][0]
        assert sig["name"] == "Go Instrumentation SIG"

    def test_display_name_stable_with_older_file_added(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-19.md", SAMPLE_TRANSCRIPT_RENAMED)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()
        assert manifest["sigs"][0]["name"] == "Go Instrumentation SIG"

        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()
        assert manifest["sigs"][0]["name"] == "Go Instrumentation SIG"

    def test_trivial_transcript_flagged(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-20.md", SAMPLE_TRANSCRIPT_TRIVIAL)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        meeting = manifest["sigs"][0]["meetings"][0]
        assert meeting["trivial"] is True

    def test_real_transcript_not_trivial(self, tmp_path: Path) -> None:
        real_transcript = """\
SIG: Go SIG
Date: 2026-02-05
Duration: 33 minutes
Source URL: https://zoom.us/rec/share/abc123
============================================================

## Zoom Recording Transcript

**Tyler** 02:14 Hey, Damien.
**Damien Mathieu** 02:19 Hey!
**Tyler** 02:22 Let's get started with the agenda.
**Damien Mathieu** 02:30 Sounds good to me.
"""
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", real_transcript)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        meeting = manifest["sigs"][0]["meetings"][0]
        assert meeting["trivial"] is False

    def test_manifest_json_serializable(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Java-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT_JAVA)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        serialized = json.dumps(manifest, indent=2)
        roundtripped = json.loads(serialized)
        assert roundtripped["sigs"][0]["slug"] == "Go-SIG"


class TestStaleFileRemoval:
    def test_stale_sig_dir_removed(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        # A truly stale dir has no transcript.md files (e.g. leftover empty dir)
        stale_dir = src / "Old-SIG"
        stale_dir.mkdir(parents=True)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert not stale_dir.exists()

    def test_no_stale_files_is_noop(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert (src / "Go-SIG" / "2026-02-05" / "transcript.md").exists()

    def test_transcripts_dir_missing_is_safe(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert len(manifest["sigs"]) == 1

    def test_malformed_header_does_not_delete_transcript(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"

        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-10.md", "garbage header\n")

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert (src / "Go-SIG" / "2026-02-05" / "transcript.md").exists()
        assert (src / "Go-SIG" / "2026-02-10" / "transcript.md").exists()

    def test_all_malformed_headers_does_not_delete_sig_dir(self, tmp_path: Path) -> None:
        """SIG directory must survive even when every transcript has an unparseable header."""
        docs = tmp_path / "docs"
        src = docs / "content"

        _write_transcript(src, "Go-SIG", "2026-02-05.md", "garbage header\n")
        _write_transcript(src, "Go-SIG", "2026-02-10.md", "garbage header\n")

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert (src / "Go-SIG").exists()
        assert (src / "Go-SIG" / "2026-02-05" / "transcript.md").exists()
        assert (src / "Go-SIG" / "2026-02-10" / "transcript.md").exists()

    def test_has_meeting_notes_true(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        (src / "Go-SIG" / "2026-02-05" / "meeting-notes.md").write_text(
            "## Meeting Notes\n\n### Attendees\n- Tyler\n", encoding="utf-8"
        )

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"][0]["meetings"][0]["has_meeting_notes"] is True

    def test_has_meeting_notes_false(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"][0]["meetings"][0]["has_meeting_notes"] is False

    def test_min_max_dates(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["min_date"] == "2026-02-05"
        assert manifest["max_date"] == "2026-02-12"

    def test_min_max_dates_none_when_empty(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        src.mkdir(parents=True)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["min_date"] is None
        assert manifest["max_date"] is None

    def test_meeting_count(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"][0]["meeting_count"] == 2

    def test_metadata_only_sig_dir_not_deleted(self, tmp_path: Path) -> None:
        """SIG directory with only metadata.md (no transcripts) must not be deleted."""
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        metadata_only = src / "New-SIG"
        metadata_only.mkdir(parents=True)
        (metadata_only / "metadata.md").write_text(
            "Meeting Notes URL: https://example.com/notes\nRepository URL: https://example.com/repo\n"
        )

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert metadata_only.exists()
        assert (metadata_only / "metadata.md").exists()

    def test_non_dir_entry_in_transcripts_src_is_skipped(self, tmp_path: Path) -> None:
        """A file at the slug level (not a directory) should be silently skipped."""
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        (src / "some-file.txt").write_text("unexpected file", encoding="utf-8")

        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert len(manifest["sigs"]) == 1


# ---------------------------------------------------------------------------
# TestBuildSiteMain — the main() entry point
# ---------------------------------------------------------------------------


class TestBuildSiteMain:
    def test_main_writes_manifest_json(self, tmp_path: Path) -> None:
        """main() should create docs/ and write manifest.json."""
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        manifest_path = docs / "manifest.json"
        with (
            patch("build_site.TRANSCRIPTS_SRC", src),
            patch("build_site.DOCS_DIR", docs),
            patch("build_site.MANIFEST_PATH", manifest_path),
            patch("build_site.SPEAKERS_PATH", docs / "speakers.json"),
            patch("build_site.MEETINGS_JSONL_PATH", docs / "meetings.jsonl"),
        ):
            build_main()

        assert manifest_path.exists()
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert len(data["sigs"]) == 1
        assert data["sigs"][0]["slug"] == "Go-SIG"

    def test_main_writes_speakers_json(self, tmp_path: Path) -> None:
        """main() should write speakers.json."""
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        (src / "Go-SIG" / "2026-02-05" / "summary.md").write_text(SAMPLE_SUMMARY, encoding="utf-8")
        speakers_path = docs / "speakers.json"
        with (
            patch("build_site.TRANSCRIPTS_SRC", src),
            patch("build_site.DOCS_DIR", docs),
            patch("build_site.MANIFEST_PATH", docs / "manifest.json"),
            patch("build_site.SPEAKERS_PATH", speakers_path),
            patch("build_site.MEETINGS_JSONL_PATH", docs / "meetings.jsonl"),
        ):
            build_main()

        assert speakers_path.exists()
        data = json.loads(speakers_path.read_text(encoding="utf-8"))
        assert "speakers" in data
        names = [s["name"] for s in data["speakers"]]
        assert "Trask Stalnaker" in names

    def test_main_writes_meetings_jsonl(self, tmp_path: Path) -> None:
        """main() should write meetings.jsonl with one line per meeting."""
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        meetings_jsonl_path = docs / "meetings.jsonl"
        with (
            patch("build_site.TRANSCRIPTS_SRC", src),
            patch("build_site.DOCS_DIR", docs),
            patch("build_site.MANIFEST_PATH", docs / "manifest.json"),
            patch("build_site.SPEAKERS_PATH", docs / "speakers.json"),
            patch("build_site.MEETINGS_JSONL_PATH", meetings_jsonl_path),
        ):
            build_main()

        assert meetings_jsonl_path.exists()
        lines = meetings_jsonl_path.read_text(encoding="utf-8").strip().splitlines()
        assert len(lines) == 1
        record = json.loads(lines[0])
        assert record["slug"] == "Go-SIG"
        assert record["date"] == "2026-02-05"

    def test_main_creates_docs_dir(self, tmp_path: Path) -> None:
        """main() should create DOCS_DIR if it doesn't exist."""
        docs = tmp_path / "new_docs"
        src = docs / "content"

        manifest_path = docs / "manifest.json"
        with (
            patch("build_site.TRANSCRIPTS_SRC", src),
            patch("build_site.DOCS_DIR", docs),
            patch("build_site.MANIFEST_PATH", manifest_path),
            patch("build_site.SPEAKERS_PATH", docs / "speakers.json"),
            patch("build_site.MEETINGS_JSONL_PATH", docs / "meetings.jsonl"),
        ):
            build_main()

        assert docs.exists()

    def test_main_records_span_on_exception(self, tmp_path: Path) -> None:
        """main() should record the exception on the span and re-raise it."""
        docs = tmp_path / "docs"
        manifest_path = docs / "manifest.json"

        with (
            patch("build_site.DOCS_DIR", docs),
            patch("build_site.MANIFEST_PATH", manifest_path),
            patch("build_site.build_manifest", side_effect=RuntimeError("build failed")),
            pytest.raises(RuntimeError, match="build failed"),
        ):
            build_main()


# ---------------------------------------------------------------------------
# TestParseSummary
# ---------------------------------------------------------------------------


class TestParseSummary:
    def test_parses_participants(self, tmp_path: Path) -> None:
        p = tmp_path / "summary.md"
        p.write_text(SAMPLE_SUMMARY, encoding="utf-8")
        result = parse_summary(p)
        assert result == ["Trask Stalnaker", "John Watson", "Jack Berg"]

    def test_missing_file_returns_empty(self, tmp_path: Path) -> None:
        assert parse_summary(tmp_path / "missing.md") == []

    def test_no_participants_section_returns_empty(self, tmp_path: Path) -> None:
        p = tmp_path / "summary.md"
        p.write_text("## Key Topics\n- Topic A\n", encoding="utf-8")
        assert parse_summary(p) == []

    def test_participants_extracted_correctly(self, tmp_path: Path) -> None:
        p = tmp_path / "summary.md"
        p.write_text("## Participants\nAlice, Bob\n", encoding="utf-8")
        assert parse_summary(p) == ["Alice", "Bob"]

    def test_strips_trailing_dot_from_names(self, tmp_path: Path) -> None:
        p = tmp_path / "summary.md"
        p.write_text("## Participants\nAlice., Bob.\n", encoding="utf-8")
        assert parse_summary(p) == ["Alice", "Bob"]

    def test_filters_ellipsis_placeholder(self, tmp_path: Path) -> None:
        p = tmp_path / "summary.md"
        p.write_text("## Participants\nAlice, Bob, ...\n", encoding="utf-8")
        assert parse_summary(p) == ["Alice", "Bob"]

    def test_filters_others_variants(self, tmp_path: Path) -> None:
        p = tmp_path / "summary.md"
        p.write_text(
            "## Participants\nAlice, others, and others., and other unnamed members.\n",
            encoding="utf-8",
        )
        assert parse_summary(p) == ["Alice"]

    def test_filters_others_with_parenthetical(self, tmp_path: Path) -> None:
        p = tmp_path / "summary.md"
        p.write_text("## Participants\nAlice, others (not specified).\n", encoding="utf-8")
        assert parse_summary(p) == ["Alice"]

    def test_deduplicates_repeated_names(self, tmp_path: Path) -> None:
        p = tmp_path / "summary.md"
        p.write_text("## Participants\nAlice, Bob, Alice\n", encoding="utf-8")
        assert parse_summary(p) == ["Alice", "Bob"]


# ---------------------------------------------------------------------------
# TestManifestSummaryFields
# ---------------------------------------------------------------------------


class TestManifestSummaryFields:
    def test_manifest_includes_participants_from_summary(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        (src / "Go-SIG" / "2026-02-05" / "summary.md").write_text(SAMPLE_SUMMARY, encoding="utf-8")
        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()
        meeting = manifest["sigs"][0]["meetings"][0]
        assert "key_topics" not in meeting
        assert meeting["participants"] == ["Trask Stalnaker", "John Watson", "Jack Berg"]

    def test_manifest_empty_participants_when_no_summary(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        with patch("build_site.TRANSCRIPTS_SRC", src), patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()
        meeting = manifest["sigs"][0]["meetings"][0]
        assert "key_topics" not in meeting
        assert meeting["participants"] == []


# ---------------------------------------------------------------------------
# TestBuildSpeakersIndex
# ---------------------------------------------------------------------------


class TestBuildSpeakersIndex:
    def _make_manifest(self, meetings_by_sig: dict) -> dict:
        sigs = []
        for slug, meetings in meetings_by_sig.items():
            sigs.append({"slug": slug, "name": slug.replace("-", " "), "meetings": meetings})
        return {"generated_at": "2026-04-30T08:00:00Z", "sigs": sigs}

    def test_single_speaker_single_sig(self) -> None:
        manifest = self._make_manifest(
            {"Go-SIG": [{"date": "2026-02-05", "participants": ["Alice"]}]}
        )
        result = build_speakers_index(manifest)
        assert len(result["speakers"]) == 1
        speaker = result["speakers"][0]
        assert speaker["name"] == "Alice"
        assert speaker["meeting_count"] == 1
        assert speaker["sigs"] == ["Go-SIG"]
        assert speaker["meetings"] == [{"sig": "Go-SIG", "date": "2026-02-05"}]

    def test_speaker_across_multiple_sigs(self) -> None:
        manifest = self._make_manifest(
            {
                "Go-SIG": [{"date": "2026-02-05", "participants": ["Alice", "Bob"]}],
                "Java-SIG": [{"date": "2026-02-06", "participants": ["Alice"]}],
            }
        )
        result = build_speakers_index(manifest)
        alice = next(s for s in result["speakers"] if s["name"] == "Alice")
        assert alice["meeting_count"] == 2
        assert alice["sigs"] == ["Go-SIG", "Java-SIG"]
        assert len(alice["meetings"]) == 2

    def test_speakers_sorted_alphabetically(self) -> None:
        manifest = self._make_manifest(
            {"Go-SIG": [{"date": "2026-02-05", "participants": ["Zara", "Alice", "Bob"]}]}
        )
        result = build_speakers_index(manifest)
        names = [s["name"] for s in result["speakers"]]
        assert names == ["Alice", "Bob", "Zara"]

    def test_meetings_sorted_newest_first(self) -> None:
        manifest = self._make_manifest(
            {
                "Go-SIG": [
                    {"date": "2026-01-01", "participants": ["Alice"]},
                    {"date": "2026-03-01", "participants": ["Alice"]},
                ]
            }
        )
        result = build_speakers_index(manifest)
        alice = result["speakers"][0]
        assert alice["meetings"][0]["date"] == "2026-03-01"
        assert alice["meetings"][1]["date"] == "2026-01-01"

    def test_no_participants_produces_empty_speakers(self) -> None:
        manifest = self._make_manifest({"Go-SIG": [{"date": "2026-02-05", "participants": []}]})
        result = build_speakers_index(manifest)
        assert result["speakers"] == []

    def test_generated_at_copied_from_manifest(self) -> None:
        manifest = self._make_manifest({})
        result = build_speakers_index(manifest)
        assert result["generated_at"] == "2026-04-30T08:00:00Z"

    def test_duplicate_participant_in_meeting_counted_once(self) -> None:
        manifest = self._make_manifest(
            {"Go-SIG": [{"date": "2026-02-05", "participants": ["Alice", "Alice"]}]}
        )
        result = build_speakers_index(manifest)
        assert len(result["speakers"]) == 1
        alice = result["speakers"][0]
        assert alice["meeting_count"] == 1
        assert len(alice["meetings"]) == 1


# ---------------------------------------------------------------------------
# TestIterMeetingsJsonl
# ---------------------------------------------------------------------------


class TestIterMeetingsJsonl:
    def _make_manifest_entry(self, slug: str, date: str, **kwargs) -> dict:
        defaults = {
            "has_summary": False,
            "has_meeting_notes": False,
            "trivial": False,
            "duration_minutes": 33,
            "participants": [],
        }
        defaults.update(kwargs)
        return {
            "sigs": [
                {
                    "slug": slug,
                    "name": slug.replace("-", " "),
                    "meetings": [{"date": date, **defaults}],
                }
            ]
        }

    def test_produces_valid_json_line(self, tmp_path: Path) -> None:
        src = tmp_path / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        manifest = self._make_manifest_entry("Go-SIG", "2026-02-05")
        lines = list(iter_meetings_jsonl(manifest, src))
        assert len(lines) == 1
        record = json.loads(lines[0])
        assert record["slug"] == "Go-SIG"
        assert record["sig_name"] == "Go SIG"
        assert record["date"] == "2026-02-05"
        assert record["summary"] == ""
        assert record["meeting_notes"] == ""

    def test_includes_summary_text_when_present(self, tmp_path: Path) -> None:
        src = tmp_path / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        (src / "Go-SIG" / "2026-02-05" / "summary.md").write_text(SAMPLE_SUMMARY, encoding="utf-8")
        manifest = self._make_manifest_entry("Go-SIG", "2026-02-05", has_summary=True)
        lines = list(iter_meetings_jsonl(manifest, src))
        record = json.loads(lines[0])
        assert "Key Topics" in record["summary"]
        assert record["meeting_notes"] == ""

    def test_includes_meeting_notes_when_present(self, tmp_path: Path) -> None:
        src = tmp_path / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        (src / "Go-SIG" / "2026-02-05" / "meeting-notes.md").write_text(
            "## Meeting Notes\n\n### Attendees\n- Tyler\n", encoding="utf-8"
        )
        manifest = self._make_manifest_entry("Go-SIG", "2026-02-05", has_meeting_notes=True)
        lines = list(iter_meetings_jsonl(manifest, src))
        record = json.loads(lines[0])
        assert "Meeting Notes" in record["meeting_notes"]

    def test_missing_summary_file_falls_back_to_empty(self, tmp_path: Path) -> None:
        src = tmp_path / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        manifest = self._make_manifest_entry("Go-SIG", "2026-02-05", has_summary=True)
        lines = list(iter_meetings_jsonl(manifest, src))
        record = json.loads(lines[0])
        assert record["summary"] == ""

    def test_missing_notes_file_falls_back_to_empty(self, tmp_path: Path) -> None:
        src = tmp_path / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        manifest = self._make_manifest_entry("Go-SIG", "2026-02-05", has_meeting_notes=True)
        lines = list(iter_meetings_jsonl(manifest, src))
        record = json.loads(lines[0])
        assert record["meeting_notes"] == ""

    def test_empty_manifest_produces_no_lines(self, tmp_path: Path) -> None:
        manifest = {"sigs": []}
        lines = list(iter_meetings_jsonl(manifest, tmp_path))
        assert lines == []

    def test_multiple_meetings_produce_multiple_lines(self, tmp_path: Path) -> None:
        src = tmp_path / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)
        manifest = {
            "sigs": [
                {
                    "slug": "Go-SIG",
                    "name": "Go SIG",
                    "meetings": [
                        {
                            "date": "2026-02-12",
                            "duration_minutes": 45,
                            "has_summary": False,
                            "has_meeting_notes": False,
                            "trivial": False,
                            "participants": [],
                        },
                        {
                            "date": "2026-02-05",
                            "duration_minutes": 33,
                            "has_summary": False,
                            "has_meeting_notes": False,
                            "trivial": False,
                            "participants": [],
                        },
                    ],
                }
            ]
        }
        lines = list(iter_meetings_jsonl(manifest, src))
        assert len(lines) == 2
        dates = [json.loads(line)["date"] for line in lines]
        assert set(dates) == {"2026-02-05", "2026-02-12"}
