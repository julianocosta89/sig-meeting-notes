#!/usr/bin/env python3
"""
Build the docs/ tree for GitHub Pages.

docs/content/ is the single source of truth for all meeting content.
Each meeting lives in docs/content/{slug}/{date}/ with:
  - transcript.md   — transcript header + speaker lines
  - meeting-notes.md — attendees and agenda (optional)
  - summary.md       — AI summary (optional)

SIG-level metadata is in docs/content/{slug}/metadata.md.

Reads every docs/content/{slug}/{date}/transcript.md, parses the header,
and writes docs/manifest.json with metadata about every SIG and meeting.
"""

from __future__ import annotations

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

from scraper.otel_setup import StatusCode, configure_tracer
from scraper.transcript_io import (
    MIN_TRANSCRIPT_LINES,
    count_transcript_lines,
    parse_header,
    parse_reference,
    read_transcript_body,
)

ROOT = Path(__file__).parent
TRANSCRIPTS_SRC = ROOT / "docs" / "content"
DOCS_DIR = ROOT / "docs"
MANIFEST_PATH = DOCS_DIR / "manifest.json"


def _remove_stale_docs(source_slugs: set[str]) -> None:
    """Remove slug dirs under docs/content/ for SIGs no longer present in source."""
    if not TRANSCRIPTS_SRC.is_dir():
        return
    for slug_dir in sorted(TRANSCRIPTS_SRC.iterdir()):
        if not slug_dir.is_dir():
            continue
        if slug_dir.name not in source_slugs:
            shutil.rmtree(slug_dir)
            print(f"  Removed stale docs/content/{slug_dir.name}/")


def build_manifest() -> dict:
    """Walk docs/content/ and build the manifest dict."""
    sigs: dict[str, dict] = {}
    source_slugs: set[str] = set()

    for md_path in sorted(TRANSCRIPTS_SRC.glob("*/*/transcript.md")):
        slug = md_path.parent.parent.name

        source_slugs.add(slug)

        header = parse_header(md_path)
        if header is None:
            print(f"  WARNING: skipping {md_path} (unparseable header)")
            continue

        date_str = header["date"]
        has_summary = (md_path.parent / "summary.md").exists()

        has_meeting_notes = (md_path.parent / "meeting-notes.md").exists()

        body = read_transcript_body(md_path)
        is_trivial = count_transcript_lines(body) < MIN_TRANSCRIPT_LINES

        meeting_entry = {
            "date": date_str,
            "duration_minutes": header["duration_minutes"],
            "has_summary": has_summary,
            "has_meeting_notes": has_meeting_notes,
            "trivial": is_trivial,
            "_sig_name": header["sig_name"],
        }

        if slug not in sigs:
            ref = parse_reference(md_path.parent.parent / "metadata.md")
            sigs[slug] = {
                "slug": slug,
                "name": header["sig_name"],
                "meeting_notes_url": ref["meeting_notes_url"] if ref else "",
                "repository_url": ref["repository_url"] if ref else "",
                "meetings": [],
            }
        sigs[slug]["meetings"].append(meeting_entry)

    # Also preserve dirs that have metadata.md but no transcripts yet
    # (e.g. pre-provisioned SIG metadata or temporarily empty SIG dirs).
    for metadata_path in TRANSCRIPTS_SRC.glob("*/metadata.md"):
        source_slugs.add(metadata_path.parent.name)

    _remove_stale_docs(source_slugs)

    all_dates: list[str] = []
    for sig_data in sigs.values():
        sig_data["meetings"].sort(key=lambda m: m["date"], reverse=True)
        sig_data["name"] = sig_data["meetings"][0]["_sig_name"]
        sig_data["meeting_count"] = len(sig_data["meetings"])
        for m in sig_data["meetings"]:
            all_dates.append(m["date"])
            del m["_sig_name"]

    sorted_sigs = sorted(sigs.values(), key=lambda s: s["slug"])

    manifest = {
        "generated_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "min_date": min(all_dates) if all_dates else None,
        "max_date": max(all_dates) if all_dates else None,
        "sigs": sorted_sigs,
    }
    return manifest


def main() -> None:
    tracer = configure_tracer("otel-recordings-build-site")

    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    with tracer.start_as_current_span("build site") as span:
        try:
            manifest = build_manifest()

            MANIFEST_PATH.write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            total_sigs = len(manifest["sigs"])
            total_meetings = sum(len(s["meetings"]) for s in manifest["sigs"])
            span.set_attribute("manifest.sigs", total_sigs)
            span.set_attribute("manifest.meetings", total_meetings)
        except Exception as exc:
            span.record_exception(exc)
            span.set_status(StatusCode.ERROR, str(exc))
            raise

    print(f"Built manifest: {total_sigs} SIGs, {total_meetings} meetings")


if __name__ == "__main__":
    main()
