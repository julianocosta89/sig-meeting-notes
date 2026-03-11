#!/usr/bin/env python3
"""Remove summary.md files for trivial meetings (fewer than MIN_TRANSCRIPT_LINES).

Usage:
  uv run python scripts/cleanup_trivial_meetings.py           # dry-run
  uv run python scripts/cleanup_trivial_meetings.py --execute  # apply
"""

from __future__ import annotations

import argparse
from pathlib import Path

from scraper.transcript_io import (
    MIN_TRANSCRIPT_LINES,
    count_transcript_lines,
    read_transcript_body,
)

ROOT = Path(__file__).resolve().parent.parent
DOCS_CONTENT_DIR = ROOT / "docs" / "content"


def find_trivial_summaries(content_dir: Path) -> list[Path]:
    """Find summary.md files belonging to trivial meetings."""
    affected: list[Path] = []
    for transcript_path in sorted(content_dir.glob("*/*/transcript.md")):
        summary_path = transcript_path.parent / "summary.md"
        if not summary_path.exists():
            continue
        body = read_transcript_body(transcript_path)
        if count_transcript_lines(body) < MIN_TRANSCRIPT_LINES:
            affected.append(summary_path)
    return affected


def main() -> None:
    parser = argparse.ArgumentParser(description="Remove summary.md files for trivial meetings.")
    parser.add_argument(
        "--execute", action="store_true", help="Actually delete files (default is dry-run)."
    )
    args = parser.parse_args()

    affected = find_trivial_summaries(DOCS_CONTENT_DIR)

    if not affected:
        print("No trivial meetings with summaries found.")
        return

    for path in affected:
        rel = path.relative_to(ROOT)
        if args.execute:
            path.unlink()
            print(f"Deleted: {rel}")
        else:
            print(f"Would delete: {rel}")

    print(f"\n{'Deleted' if args.execute else 'Found'} {len(affected)} trivial summary file(s).")


if __name__ == "__main__":
    main()
