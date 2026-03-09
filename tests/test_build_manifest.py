"""Tests for build_site.py manifest builder."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from build_site import build_manifest, main as build_main
from scraper.transcript_io import parse_header

SAMPLE_TRANSCRIPT = """\
SIG: Go SIG
Date: 2026-02-05
Duration: 33 minutes
============================================================

Tyler 02:14 Hey, Damien.
Damien Mathieu 02:19 Hey!
"""

SAMPLE_TRANSCRIPT_2 = """\
SIG: Go SIG
Date: 2026-02-12
Duration: 45 minutes
============================================================

Tyler 02:00 Welcome everyone.
"""

SAMPLE_TRANSCRIPT_JAVA = """\
SIG: Java SIG
Date: 2026-02-05
Duration: 60 minutes
============================================================

Jack 00:01 Hello!
"""

SAMPLE_TRANSCRIPT_RENAMED = """\
SIG: Go Instrumentation SIG
Date: 2026-02-19
Duration: 50 minutes
============================================================

Tyler 02:00 We renamed the SIG.
"""

SAMPLE_METADATA = """\
SIG: Go SIG
Meeting Notes: https://docs.google.com/document/d/go-doc/edit
Repository: https://github.com/open-telemetry/opentelemetry-go
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

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
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

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        sig = manifest["sigs"][0]
        assert sig["meeting_notes_url"] == "https://docs.google.com/document/d/go-doc/edit"
        assert sig["repository_url"] == "https://github.com/open-telemetry/opentelemetry-go"

    def test_sig_metadata_empty_when_no_metadata_md(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        sig = manifest["sigs"][0]
        assert sig["meeting_notes_url"] == ""
        assert sig["repository_url"] == ""

    def test_metadata_md_not_included_as_meeting(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_metadata(src, "Go-SIG")

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert len(manifest["sigs"][0]["meetings"]) == 1

    def test_meetings_sorted_descending(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
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

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        slugs = [s["slug"] for s in manifest["sigs"]]
        assert slugs == ["Go-SIG", "Java-SIG"]

    def test_has_summary_true(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        # Summary lives as a sibling of transcript.md
        (src / "Go-SIG" / "2026-02-05" / "summary.md").write_text("# Summary\n")

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"][0]["meetings"][0]["has_summary"] is True

    def test_generated_at_present(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert "generated_at" in manifest
        assert manifest["generated_at"].endswith("Z")

    def test_empty_transcripts_dir(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        src.mkdir(parents=True)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"] == []

    def test_duration_values(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
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

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        sig = manifest["sigs"][0]
        assert sig["name"] == "Go Instrumentation SIG"

    def test_display_name_stable_with_older_file_added(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-19.md", SAMPLE_TRANSCRIPT_RENAMED)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()
        assert manifest["sigs"][0]["name"] == "Go Instrumentation SIG"

        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()
        assert manifest["sigs"][0]["name"] == "Go Instrumentation SIG"

    def test_manifest_json_serializable(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Java-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT_JAVA)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
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

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert not stale_dir.exists()

    def test_no_stale_files_is_noop(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert (src / "Go-SIG" / "2026-02-05" / "transcript.md").exists()

    def test_transcripts_dir_missing_is_safe(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert len(manifest["sigs"]) == 1

    def test_malformed_header_does_not_delete_transcript(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"

        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-10.md", "garbage header\n")

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert (src / "Go-SIG" / "2026-02-05" / "transcript.md").exists()
        assert (src / "Go-SIG" / "2026-02-10" / "transcript.md").exists()

    def test_all_malformed_headers_does_not_delete_sig_dir(self, tmp_path: Path) -> None:
        """SIG directory must survive even when every transcript has an unparseable header."""
        docs = tmp_path / "docs"
        src = docs / "content"

        _write_transcript(src, "Go-SIG", "2026-02-05.md", "garbage header\n")
        _write_transcript(src, "Go-SIG", "2026-02-10.md", "garbage header\n")

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
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

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"][0]["meetings"][0]["has_meeting_notes"] is True

    def test_has_meeting_notes_false(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["sigs"][0]["meetings"][0]["has_meeting_notes"] is False

    def test_min_max_dates(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["min_date"] == "2026-02-05"
        assert manifest["max_date"] == "2026-02-12"

    def test_min_max_dates_none_when_empty(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        src.mkdir(parents=True)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            manifest = build_manifest()

        assert manifest["min_date"] is None
        assert manifest["max_date"] is None

    def test_meeting_count(self, tmp_path: Path) -> None:
        docs = tmp_path / "docs"
        src = docs / "content"
        _write_transcript(src, "Go-SIG", "2026-02-05.md", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.md", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
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

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs):
            build_manifest()

        assert metadata_only.exists()
        assert (metadata_only / "metadata.md").exists()


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
        ):
            build_main()

        assert manifest_path.exists()
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert len(data["sigs"]) == 1
        assert data["sigs"][0]["slug"] == "Go-SIG"

    def test_main_creates_docs_dir(self, tmp_path: Path) -> None:
        """main() should create DOCS_DIR if it doesn't exist."""
        docs = tmp_path / "new_docs"
        src = docs / "content"

        manifest_path = docs / "manifest.json"
        with (
            patch("build_site.TRANSCRIPTS_SRC", src),
            patch("build_site.DOCS_DIR", docs),
            patch("build_site.MANIFEST_PATH", manifest_path),
        ):
            build_main()

        assert docs.exists()
