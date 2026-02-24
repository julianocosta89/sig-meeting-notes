#!/usr/bin/env python3
"""One-time migration: restructure flat transcript files into per-meeting folders.

Usage
-----
    # Preview what would change (no files written):
    uv run python scripts/migrate_to_content.py

    # Apply the migration:
    uv run python scripts/migrate_to_content.py --execute

What it does
------------
For each docs/transcripts/{slug}/{date}.md:
  - Splits into docs/content/{slug}/{date}/transcript.md
    (header + separator + ## Zoom Recording Transcript section)
  - Writes docs/content/{slug}/{date}/meeting-notes.md
    (## Meeting Notes content — only if non-empty)

For each docs/transcripts/{slug}/metadata.md:
  - Copies to docs/content/{slug}/metadata.md

For each docs/summaries/{slug}/{date}.md:
  - Moves to docs/content/{slug}/{date}/summary.md

Finally removes docs/transcripts/ and docs/summaries/ after migration.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scraper.transcript_io import SEPARATOR  # noqa: E402

TRANSCRIPTS_DIR = ROOT / "docs" / "transcripts"
SUMMARIES_DIR = ROOT / "docs" / "summaries"
CONTENT_DIR = ROOT / "docs" / "content"

MN_HEADER = "## Meeting Notes"
ZR_HEADER = "## Zoom Recording Transcript"


def _split_transcript(text: str) -> tuple[str, str]:
    """Split a flat transcript into (transcript_content, meeting_notes_content).

    Returns:
        transcript_content: header + SEPARATOR + ## Zoom Recording Transcript section
        meeting_notes_content: ## Meeting Notes content (empty string if absent/empty)
    """
    sep_idx = text.find(SEPARATOR)
    if sep_idx == -1:
        return text, ""

    header = text[: sep_idx + len(SEPARATOR)]
    after_sep = text[sep_idx + len(SEPARATOR) :].lstrip("\n")

    zr_idx = after_sep.find(ZR_HEADER)
    mn_idx = after_sep.find(MN_HEADER)

    if zr_idx == -1:
        # No ZR section — wrap everything as transcript body
        transcript_content = (
            header + "\n\n" + ZR_HEADER + "\n\n" + after_sep.rstrip() + "\n"
        )
        return transcript_content, ""

    zr_body = after_sep[zr_idx + len(ZR_HEADER) :].lstrip("\n").rstrip() + "\n"
    transcript_content = header + "\n\n" + ZR_HEADER + "\n\n" + zr_body

    if mn_idx == -1 or mn_idx >= zr_idx:
        return transcript_content, ""

    mn_raw = after_sep[mn_idx + len(MN_HEADER) : zr_idx].strip()
    if not mn_raw:
        return transcript_content, ""

    meeting_notes_content = MN_HEADER + "\n\n" + mn_raw + "\n"
    return transcript_content, meeting_notes_content


def migrate(dry_run: bool = True) -> int:
    """Run the migration. Returns 0 on success."""
    prefix = "[DRY RUN] " if dry_run else ""

    # --- Step 1: Migrate transcript files ---
    all_md = sorted(TRANSCRIPTS_DIR.glob("*/*.md")) if TRANSCRIPTS_DIR.is_dir() else []
    transcript_files = [f for f in all_md if f.name != "metadata.md"]
    meta_files = [f for f in all_md if f.name == "metadata.md"]

    print(
        f"{prefix}Migrating {len(transcript_files)} transcript(s) "
        f"from {TRANSCRIPTS_DIR}"
    )
    notes_count = 0

    for md_path in transcript_files:
        slug = md_path.parent.name
        date_str = md_path.stem
        dest_dir = CONTENT_DIR / slug / date_str

        text = md_path.read_text(encoding="utf-8")
        transcript_content, meeting_notes_content = _split_transcript(text)

        has_notes = bool(meeting_notes_content)
        if has_notes:
            notes_count += 1

        if dry_run:
            label = (
                f"  [DRY RUN] {slug}/{date_str}.md → {slug}/{date_str}/transcript.md"
            )
            if has_notes:
                label += " + meeting-notes.md"
            print(label)
        else:
            dest_dir.mkdir(parents=True, exist_ok=True)
            (dest_dir / "transcript.md").write_text(
                transcript_content, encoding="utf-8"
            )
            if has_notes:
                (dest_dir / "meeting-notes.md").write_text(
                    meeting_notes_content, encoding="utf-8"
                )
            md_path.unlink()
            label = f"  {slug}/{date_str}.md → {slug}/{date_str}/transcript.md"
            if has_notes:
                label += " + meeting-notes.md"
            print(label)

    # --- Step 2: Migrate metadata.md files ---
    print(f"\n{prefix}Migrating {len(meta_files)} metadata.md file(s)")
    for meta_path in meta_files:
        slug = meta_path.parent.name
        dest = CONTENT_DIR / slug / "metadata.md"
        if dry_run:
            print(f"  [DRY RUN] {slug}/metadata.md → content/{slug}/metadata.md")
        else:
            (CONTENT_DIR / slug).mkdir(parents=True, exist_ok=True)
            shutil.copy2(meta_path, dest)
            meta_path.unlink()
            print(f"  {slug}/metadata.md → content/{slug}/metadata.md")

    # --- Step 3: Migrate summaries ---
    if SUMMARIES_DIR.is_dir():
        summary_files = sorted(SUMMARIES_DIR.glob("*/*.md"))
        print(
            f"\n{prefix}Migrating {len(summary_files)} summary file(s) "
            f"from {SUMMARIES_DIR}"
        )
        for sum_path in summary_files:
            slug = sum_path.parent.name
            date_str = sum_path.stem
            dest = CONTENT_DIR / slug / date_str / "summary.md"
            if dry_run:
                print(
                    f"  [DRY RUN] summaries/{slug}/{date_str}.md "
                    f"→ content/{slug}/{date_str}/summary.md"
                )
            else:
                (CONTENT_DIR / slug / date_str).mkdir(parents=True, exist_ok=True)
                shutil.copy2(sum_path, dest)
                print(
                    f"  summaries/{slug}/{date_str}.md "
                    f"→ content/{slug}/{date_str}/summary.md"
                )

        if not dry_run:
            shutil.rmtree(SUMMARIES_DIR)
            print(f"\n  Removed {SUMMARIES_DIR}")
    else:
        print(f"\n{prefix}No summaries directory found — skipping.")

    # --- Step 4: Clean up empty transcripts/ tree ---
    if not dry_run and TRANSCRIPTS_DIR.is_dir():
        remaining = [f for f in TRANSCRIPTS_DIR.rglob("*") if f.is_file()]
        if not remaining:
            shutil.rmtree(TRANSCRIPTS_DIR)
            print(f"\n  Removed {TRANSCRIPTS_DIR}")
        else:
            print(
                f"\n  WARNING: {TRANSCRIPTS_DIR} still has "
                f"{len(remaining)} file(s) — not removed"
            )

    print(
        f"\n{prefix}Done: {len(transcript_files)} transcript(s) "
        f"({notes_count} with meeting notes)"
    )
    if dry_run:
        print("Run with --execute to apply changes.")
    return 0


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Migrate flat transcript files to per-meeting folder structure.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually write and delete files (default is dry-run only).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    sys.exit(migrate(dry_run=not args.execute))
