#!/usr/bin/env python3
"""One-time migration: convert transcript .txt files to the new .md format.

Usage
-----
    # Preview what would change (no files written):
    uv run python scripts/migrate_to_md.py

    # Apply the migration:
    uv run python scripts/migrate_to_md.py --execute

What it does
------------
For each transcripts/**/*.txt file:
  - Converts the 4-field plain-text header to the new Markdown header
    (renames 'Source URL:' → 'Zoom Recording URL:')
  - Wraps the transcript body in a '## Zoom Recording Transcript' section
  - Converts 'Speaker MM:SS utterance' lines to '**Speaker** MM:SS utterance'
  - Writes YYYY-MM-DD.md alongside the original, then removes the .txt file

For each SIG directory that has no metadata.md:
  - Bootstraps metadata.md from the community README (best-effort)
  - Leaves 'Meeting Notes:' and 'Repository:' empty if not found
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Allow running from any working directory
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scraper import community  # noqa: E402  (after sys.path fix)
from scraper.transcript_io import SEPARATOR, parse_header, parse_reference  # noqa: E402

TRANSCRIPTS_DIR = Path(__file__).resolve().parent.parent / "docs" / "transcripts"

_SPEAKER_LINE_RE = re.compile(r"^(.+?)\s+(\d{1,2}:\d{2})\s+(.*)$")


def _format_body_line(line: str) -> str:
    """Convert 'Speaker MM:SS utterance' → '**Speaker** MM:SS utterance'."""
    m = _SPEAKER_LINE_RE.match(line)
    if m:
        return f"**{m.group(1)}** {m.group(2)} {m.group(3)}"
    return line


def _build_md_content(header: dict[str, str | int], body_lines: list[str]) -> str:
    """Assemble the new .md content from a parsed header and body lines."""
    parts = [
        f"SIG: {header['sig_name']}",
        f"Date: {header['date']}",
        f"Duration: {header['duration_minutes']} minutes",
        f"Zoom Recording URL: {header['source_url']}",
        SEPARATOR,
        "",
        "## Meeting Notes",
        "",
        "## Zoom Recording Transcript",
        "",
    ]
    parts.extend(_format_body_line(line) for line in body_lines)
    if not parts or parts[-1] != "":
        parts.append("")
    return "\n".join(parts)


def migrate_file(txt_path: Path, dry_run: bool) -> bool:
    """Migrate one .txt file to .md.

    Returns True on success (or dry-run preview), False if the file is skipped.
    """
    header = parse_header(txt_path)
    if header is None:
        print(f"  SKIP (malformed header): {txt_path.name}")
        return False

    text = txt_path.read_text(encoding="utf-8")
    sep_idx = text.find(SEPARATOR)
    if sep_idx == -1:
        print(f"  SKIP (separator not found): {txt_path.name}")
        return False

    raw_body = text[sep_idx + len(SEPARATOR):].lstrip("\n")
    body_lines = raw_body.splitlines()

    content = _build_md_content(header, body_lines)
    md_path = txt_path.with_suffix(".md")

    if dry_run:
        print(f"  [DRY RUN] {txt_path.name} → {md_path.name}")
        return True

    md_path.write_text(content, encoding="utf-8")
    txt_path.unlink()
    print(f"  {txt_path.name} → {md_path.name}")
    return True


def ensure_metadata(sig_dir: Path, sig_name: str, dry_run: bool) -> None:
    """Create metadata.md for a SIG directory if it doesn't already exist."""
    metadata_path = sig_dir / "metadata.md"
    if metadata_path.exists():
        return

    notes_url = community.get_meeting_notes_url(sig_dir.name)
    content = (
        f"SIG: {sig_name}\n"
        f"Meeting Notes: {notes_url}\n"
        f"Repository: \n"
    )

    if dry_run:
        if notes_url:
            print(f"  [DRY RUN] Would create {metadata_path.name} (notes: {notes_url})")
        else:
            print(f"  [DRY RUN] Would create {metadata_path.name} (no notes URL — fill in manually)")
        return

    metadata_path.write_text(content, encoding="utf-8")
    if notes_url:
        print(f"  Created {metadata_path.name} (notes: {notes_url})")
    else:
        print(f"  Created {metadata_path.name} (no notes URL — fill in manually)")


def migrate(transcripts_dir: Path = TRANSCRIPTS_DIR, dry_run: bool = True) -> int:
    """Run the migration. Returns the number of failures (skipped files)."""
    txt_files = sorted(transcripts_dir.glob("**/*.txt"))

    if not txt_files:
        print("No .txt transcript files found — nothing to migrate.")
        return 0

    prefix = "[DRY RUN] " if dry_run else ""
    print(f"{prefix}Migrating {len(txt_files)} transcript(s) in {transcripts_dir}\n")

    # Track SIG dirs and a representative sig_name for each
    sig_dirs: dict[Path, str] = {}
    success = 0
    skipped = 0

    for txt_path in txt_files:
        header = parse_header(txt_path)
        if header is not None:
            sig_dirs.setdefault(txt_path.parent, header["sig_name"])

        if migrate_file(txt_path, dry_run):
            success += 1
        else:
            skipped += 1

    # Ensure every SIG directory has a metadata.md
    print()
    for sig_dir in sorted(sig_dirs):
        ensure_metadata(sig_dir, sig_dirs[sig_dir], dry_run)

    print(
        f"\n{prefix}Done: {success} migrated, {skipped} skipped"
        f" (out of {len(txt_files)} .txt files)."
    )
    if dry_run:
        print("Run with --execute to apply changes.")

    return skipped


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Migrate transcript .txt files to the new .md format.",
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
