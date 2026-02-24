#!/usr/bin/env python3
"""Backfill meeting-notes.md files for existing transcripts.

For each transcript that has no meeting-notes.md sibling, fetches the SIG's
Google Doc and writes the Attendees and Agenda content to a separate file.

Usage:
    # Dry run (default — shows what would change, writes nothing)
    python scripts/backfill_meeting_notes.py

    # Apply changes
    python scripts/backfill_meeting_notes.py --execute

    # Limit to one SIG (substring match on slug)
    python scripts/backfill_meeting_notes.py --execute --sig agent-management
"""
from __future__ import annotations

import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scraper import gdoc  # noqa: E402

TRANSCRIPTS_DIR = ROOT / "docs" / "content"


def _needs_notes(transcript_path: pathlib.Path) -> bool:
    """Return True if no meeting-notes.md exists alongside this transcript."""
    return not (transcript_path.parent / "meeting-notes.md").exists()


def _format_notes(attendees: list[str], agenda: list[str]) -> str:
    parts: list[str] = []
    if attendees:
        parts.append("### Attendees")
        parts.extend(attendees)
        parts.append("")
    if agenda:
        parts.append("### Agenda")
        parts.extend(agenda)
        parts.append("")
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true",
                        help="Write changes to disk (default: dry run)")
    parser.add_argument("--force", action="store_true",
                        help="Re-fetch and overwrite existing meeting-notes.md files")
    parser.add_argument("--sig", default=None,
                        help="Limit to SIGs whose slug contains this substring")
    args = parser.parse_args()
    dry_run = not args.execute

    if dry_run:
        print("DRY RUN — pass --execute to apply changes\n")

    stats = {"checked": 0, "no_url": 0, "no_content": 0, "updated": 0}

    for md_path in sorted(TRANSCRIPTS_DIR.glob("*/*/transcript.md")):
        slug = md_path.parent.parent.name
        if args.sig and args.sig.lower() not in slug.lower():
            continue

        if not args.force and not _needs_notes(md_path):
            continue

        stats["checked"] += 1
        date = md_path.parent.name  # directory name is the date

        meta_path = md_path.parent.parent / "metadata.md"
        notes_url = ""
        if meta_path.exists():
            for line in meta_path.read_text().splitlines():
                if line.startswith("Meeting Notes:"):
                    notes_url = line.split(":", 1)[1].strip()
                    break

        if not notes_url:
            print(f"  SKIP (no Meeting Notes URL): {slug}/{date}")
            stats["no_url"] += 1
            continue

        print(f"  Fetching {slug} / {date} ...", end=" ", flush=True)
        result = gdoc.fetch_meeting_notes(notes_url, date)
        attendees = result.get("attendees", [])
        agenda = result.get("agenda", [])

        if not attendees and not agenda:
            print("no content found")
            stats["no_content"] += 1
            continue

        notes_text = _format_notes(attendees, agenda)
        notes_content = "## Meeting Notes\n\n" + notes_text
        notes_path = md_path.parent / "meeting-notes.md"

        if dry_run:
            print(f"{len(attendees)} attendees, {len(agenda)} agenda items [DRY RUN]")
        else:
            notes_path.write_text(notes_content, encoding="utf-8")
            print(f"{len(attendees)} attendees, {len(agenda)} agenda items")

        stats["updated"] += 1

    print(f"\nDone. checked={stats['checked']} updated={stats['updated']} "
          f"no_url={stats['no_url']} no_content={stats['no_content']}")


if __name__ == "__main__":
    main()
