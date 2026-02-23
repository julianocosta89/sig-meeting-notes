#!/usr/bin/env python3
"""
Build the docs/ tree for GitHub Pages from the transcripts/ directory.

Reads every transcripts/{slug}/{date}.txt, parses the 4-line header,
copies the file into docs/transcripts/{slug}/{date}.txt, and writes
docs/manifest.json with metadata about every SIG and meeting.
"""
from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from scraper.transcript_io import parse_header

ROOT = Path(__file__).parent
TRANSCRIPTS_SRC = ROOT / "transcripts"
DOCS_DIR = ROOT / "docs"
SUMMARIES_DIR = DOCS_DIR / "summaries"
MANIFEST_PATH = DOCS_DIR / "manifest.json"


def build_manifest() -> dict:
    """Walk transcripts/ and build the manifest dict + copy files to docs/."""
    sigs: dict[str, dict] = {}

    for txt_path in sorted(TRANSCRIPTS_SRC.glob("*/*.txt")):
        slug = txt_path.parent.name
        header = parse_header(txt_path)
        if header is None:
            print(f"  WARNING: skipping {txt_path} (unparseable header)")
            continue

        date_str = header["date"]

        # Copy transcript to docs/transcripts/{slug}/
        dest_dir = DOCS_DIR / "transcripts" / slug
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(txt_path, dest_dir / txt_path.name)

        # Check for summary
        summary_path = SUMMARIES_DIR / slug / f"{date_str}.md"
        has_summary = summary_path.exists()

        meeting_entry = {
            "date": date_str,
            "duration_minutes": header["duration_minutes"],
            "has_summary": has_summary,
        }

        if slug not in sigs:
            sigs[slug] = {
                "slug": slug,
                "name": header["sig_name"],
                "meetings": [],
            }
        sigs[slug]["meetings"].append(meeting_entry)

    # Sort meetings within each SIG by date descending
    for sig_data in sigs.values():
        sig_data["meetings"].sort(key=lambda m: m["date"], reverse=True)

    # Sort SIGs alphabetically by slug
    sorted_sigs = sorted(sigs.values(), key=lambda s: s["slug"])

    manifest = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sigs": sorted_sigs,
    }
    return manifest


def main() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    manifest = build_manifest()

    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    total_sigs = len(manifest["sigs"])
    total_meetings = sum(len(s["meetings"]) for s in manifest["sigs"])
    print(f"Built manifest: {total_sigs} SIGs, {total_meetings} meetings")


if __name__ == "__main__":
    main()
