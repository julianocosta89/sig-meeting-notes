"""Tests for build_site.py manifest builder."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from build_site import build_manifest, parse_header

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


def _write_transcript(base: Path, slug: str, filename: str, content: str) -> None:
    d = base / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / filename).write_text(content, encoding="utf-8")


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
        src = tmp_path / "transcripts"
        docs = tmp_path / "docs"
        _write_transcript(src, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            manifest = build_manifest()

        assert len(manifest["sigs"]) == 1
        sig = manifest["sigs"][0]
        assert sig["slug"] == "Go-SIG"
        assert sig["name"] == "Go SIG"
        assert len(sig["meetings"]) == 1
        assert sig["meetings"][0]["date"] == "2026-02-05"
        assert sig["meetings"][0]["duration_minutes"] == 33
        assert sig["meetings"][0]["has_summary"] is False

    def test_meetings_sorted_descending(self, tmp_path: Path) -> None:
        src = tmp_path / "transcripts"
        docs = tmp_path / "docs"
        _write_transcript(src, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.txt", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            manifest = build_manifest()

        meetings = manifest["sigs"][0]["meetings"]
        assert len(meetings) == 2
        assert meetings[0]["date"] == "2026-02-12"
        assert meetings[1]["date"] == "2026-02-05"

    def test_sigs_sorted_alphabetically(self, tmp_path: Path) -> None:
        src = tmp_path / "transcripts"
        docs = tmp_path / "docs"
        _write_transcript(src, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Java-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT_JAVA)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            manifest = build_manifest()

        slugs = [s["slug"] for s in manifest["sigs"]]
        assert slugs == ["Go-SIG", "Java-SIG"]

    def test_transcript_copied_to_docs(self, tmp_path: Path) -> None:
        src = tmp_path / "transcripts"
        docs = tmp_path / "docs"
        _write_transcript(src, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            build_manifest()

        copied = docs / "transcripts" / "Go-SIG" / "2026-02-05.txt"
        assert copied.exists()
        assert copied.read_text(encoding="utf-8") == SAMPLE_TRANSCRIPT

    def test_has_summary_true(self, tmp_path: Path) -> None:
        src = tmp_path / "transcripts"
        docs = tmp_path / "docs"
        _write_transcript(src, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        # Create a summary file
        summary_dir = docs / "summaries" / "Go-SIG"
        summary_dir.mkdir(parents=True)
        (summary_dir / "2026-02-05.md").write_text("# Summary\n")

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            manifest = build_manifest()

        assert manifest["sigs"][0]["meetings"][0]["has_summary"] is True

    def test_generated_at_present(self, tmp_path: Path) -> None:
        src = tmp_path / "transcripts"
        docs = tmp_path / "docs"
        _write_transcript(src, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            manifest = build_manifest()

        assert "generated_at" in manifest
        assert manifest["generated_at"].endswith("Z")

    def test_empty_transcripts_dir(self, tmp_path: Path) -> None:
        src = tmp_path / "transcripts"
        src.mkdir()
        docs = tmp_path / "docs"

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            manifest = build_manifest()

        assert manifest["sigs"] == []

    def test_duration_values(self, tmp_path: Path) -> None:
        src = tmp_path / "transcripts"
        docs = tmp_path / "docs"
        _write_transcript(src, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Go-SIG", "2026-02-12.txt", SAMPLE_TRANSCRIPT_2)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            manifest = build_manifest()

        meetings = manifest["sigs"][0]["meetings"]
        durations = {m["date"]: m["duration_minutes"] for m in meetings}
        assert durations["2026-02-05"] == 33
        assert durations["2026-02-12"] == 45

    def test_manifest_json_serializable(self, tmp_path: Path) -> None:
        src = tmp_path / "transcripts"
        docs = tmp_path / "docs"
        _write_transcript(src, "Go-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT)
        _write_transcript(src, "Java-SIG", "2026-02-05.txt", SAMPLE_TRANSCRIPT_JAVA)

        with patch("build_site.TRANSCRIPTS_SRC", src), \
             patch("build_site.DOCS_DIR", docs), \
             patch("build_site.SUMMARIES_DIR", docs / "summaries"):
            manifest = build_manifest()

        # Should not raise
        serialized = json.dumps(manifest, indent=2)
        roundtripped = json.loads(serialized)
        assert roundtripped["sigs"][0]["slug"] == "Go-SIG"
