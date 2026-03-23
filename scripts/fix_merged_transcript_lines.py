"""Detect and fix transcript lines where multiple speakers were incorrectly merged.

When the continuation-line merger in parse_transcript_html joins a speaker's
"…"-terminated utterance with the NEXT speaker's line (because Zoom wraps <li>
content in a container div with no "speaker" class, making all lines appear as
continuations), the result is a single line containing multiple speakers.

After _format_body_line runs, such lines look like:
  **Text… Speaker2** 13:43 Text2… Speaker3 13:45 Text3.
  **Speaker1** 13:46 Text1… Speaker2 13:49 Text2.

This script detects those patterns and splits them back into proper lines.

Usage:
    uv run python scripts/fix_merged_transcript_lines.py          # dry-run
    uv run python scripts/fix_merged_transcript_lines.py --execute # apply fixes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ── Pattern matching ──────────────────────────────────────────────────────────

# Matches display-name variants followed by a timestamp within merged text, e.g.:
#   "Name MM:SS "                      — single-word name
#   "First Last MM:SS "                — multi-word name
#   "Donal O'Sullivan MM:SS "          — apostrophe in name token
#   "First Last [Org] MM:SS "          — bracket org tag
#   "First Last | Org MM:SS "          — pipe-separated org
#   "First Last (Org) MM:SS "          — parenthesised org
# \w is Unicode-aware in Python 3 (covers diacritics, etc.).
# Single-word names (e.g. "Andrej") are matched because the second word group is
# optional (*).  The required timestamp keeps false positives low.
_SPEAKER_TS_RE = re.compile(
    r"([A-Z][\w']+(?:\s+[A-Z][\w']+)*"  # name tokens (apostrophes allowed)
    r"(?:\s+\[[^\]]+\])?"  # optional [Org] bracket tag
    r"(?:\s+\|[^|]*?)?"  # optional | Org pipe suffix
    r"(?:\s+\([^)]+\))?)"  # optional (Org) paren suffix (closes capture group)
    r"\s+(\d{1,2}:\d{2})\s+"  # timestamp (captured as group 2)
)

# Matches a fully-formatted transcript speaker line: **Name** MM:SS rest
_BOLD_LINE_RE = re.compile(r"^\*\*([^*]+)\*\*\s+(\d{1,2}:\d{2})\s+(.*)$", re.DOTALL)

# Used to reformat a raw segment as a bold speaker line
_FORMAT_RE = re.compile(r"^(.+?)\s+(\d{1,2}:\d{2})\s+(.*)$", re.DOTALL)

# Punctuation characters that legitimately end a speaker's turn
_TURN_ENDS = frozenset(".?!…")

# Transcript header separator (same constant used by transcript_io.py)
_SEPARATOR = "=" * 60


# ── Core split/fix logic ──────────────────────────────────────────────────────


def _pre_format_text(line: str) -> str:
    """Reconstruct the un-bolded text that _format_body_line received.

    **Name** MM:SS rest  →  Name MM:SS rest
    """
    m = _BOLD_LINE_RE.match(line)
    if m:
        return f"{m.group(1)} {m.group(2)} {m.group(3)}".rstrip()
    return line


def _format_segment(segment: str) -> str:
    """Wrap a segment in bold speaker notation if it starts with Name+Timestamp."""
    m = _FORMAT_RE.match(segment)
    if m:
        return f"**{m.group(1)}** {m.group(2)} {m.group(3)}"
    return segment


def _valid_split_matches(pre: str) -> list[re.Match]:
    """Return speaker-pattern matches that are valid split points.

    A match is valid when it is at the start of the text, or when the text
    immediately before it ends with sentence-ending punctuation (`.?!…`).
    This prevents false positives where part of a speaker name (e.g. "Elastic
    Observability" in "Andrew Wilkins @ Elastic Observability 00:23 …")
    incorrectly looks like a new speaker.
    """
    valid = []
    for m in _SPEAKER_TS_RE.finditer(pre):
        if m.start() == 0:
            valid.append(m)
            continue
        before = pre[: m.start()].rstrip()
        if before and before[-1] in _TURN_ENDS:
            valid.append(m)
    return valid


def _split_at_valid_boundaries(pre: str, matches: list) -> list[str]:
    """Split pre-format text at the given match positions."""
    starts = [m.start() for m in matches]
    ends = starts[1:] + [len(pre)]

    segments: list[str] = []

    # Text before the first match (plain continuation, if any)
    if starts[0] > 0:
        prefix = pre[: starts[0]].rstrip()
        if prefix:
            segments.append(prefix)

    for start, end in zip(starts, ends):
        segment = pre[start:end].strip()
        if segment:
            segments.append(segment)

    return segments


def fix_line(line: str) -> list[str]:
    """Return corrected replacement(s) for a (possibly merged) transcript line.

    Returns [line] unchanged when no merge is detected.  Returns 2+ properly
    formatted lines when a multi-speaker merge is detected.
    """
    pre = _pre_format_text(line)
    matches = _valid_split_matches(pre)

    # Not corrupted: zero patterns, or exactly one that starts at position 0
    if not matches:
        return [line]
    if len(matches) == 1 and matches[0].start() == 0:
        return [line]

    segments = _split_at_valid_boundaries(pre, matches)
    return [_format_segment(s) for s in segments]


# ── File-level helpers ────────────────────────────────────────────────────────


def _split_header_body(text: str) -> tuple[str, list[str]]:
    """Split a transcript file into (header, body_lines)."""
    sep_idx = text.find(_SEPARATOR)
    if sep_idx == -1:
        return "", text.splitlines()
    header_end = sep_idx + len(_SEPARATOR)
    header = text[:header_end]
    body_text = text[header_end:]
    return header, body_text.splitlines()


def fix_transcript_file(path: Path) -> tuple[list[tuple[int, str, list[str]]], str]:
    """Detect and fix all merged lines in a transcript file.

    Returns (changes, new_text) where changes is a list of
    (line_number, original_line, replacement_lines).  Line numbers are 1-based
    relative to the body section.  new_text is the corrected file content (or
    the original content when no changes are needed).
    """
    raw = path.read_text(encoding="utf-8")
    header, body = _split_header_body(raw)
    changes: list[tuple[int, str, list[str]]] = []
    new_body: list[str] = []

    for lineno, line in enumerate(body, 1):
        replacement = fix_line(line)
        if len(replacement) != 1 or replacement[0] != line:
            changes.append((lineno, line, replacement))
        new_body.extend(replacement)

    if changes:
        new_text = header + "\n".join(new_body) + "\n"
        return changes, new_text
    return changes, raw


# ── CLI ───────────────────────────────────────────────────────────────────────


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect (and optionally fix) merged multi-speaker transcript lines."
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Apply fixes in-place (default is dry-run).",
    )
    parser.add_argument(
        "--sig",
        default=None,
        help="Only process transcripts under this SIG slug (substring match).",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    content_dir = Path(__file__).parent.parent / "docs" / "content"

    transcript_files = sorted(content_dir.glob("**/transcript.md"))
    if args.sig:
        transcript_files = [p for p in transcript_files if args.sig.lower() in str(p).lower()]

    total_files = 0
    total_new_lines = 0

    for path in transcript_files:
        changes, new_text = fix_transcript_file(path)
        if not changes:
            continue
        total_files += 1
        total_new_lines += sum(len(r) - 1 for _, _, r in changes)
        rel = path.relative_to(content_dir.parent.parent)
        print(f"\n{rel}")
        for lineno, orig, replacement in changes:
            orig_preview = orig[:80] + ("…" if len(orig) > 80 else "")
            print(f"  Line {lineno}: {orig_preview!r}")
            for r in replacement:
                r_preview = r[:80] + ("…" if len(r) > 80 else "")
                print(f"    → {r_preview!r}")
        if args.execute:
            path.write_text(new_text, encoding="utf-8")

    if total_files == 0:
        print("No merged lines found.")
        return 0

    mode = "Fixed" if args.execute else "Would fix"
    print(f"\n{mode} {total_new_lines} merged line(s) across {total_files} file(s).")
    if not args.execute:
        print("Re-run with --execute to apply changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
