"""Shared transcript I/O helpers.

Provides the canonical header parser and separator constant used by
both build_site.py and generate_summaries.py.
"""

from __future__ import annotations

import re
from pathlib import Path

SEPARATOR = "=" * 60

MIN_TRANSCRIPT_LINES = 3  # non-blank, non-heading lines required for a real meeting

_TRANSCRIPT_SECTION_RE = re.compile(r"^## Zoom Recording Transcript\s*$", re.MULTILINE)


def count_transcript_lines(body: str) -> int:
    """Count non-blank, non-Markdown-heading lines in a transcript body."""
    return sum(1 for line in body.splitlines() if line.strip() and not line.strip().startswith("#"))


def read_transcript_body(path: Path) -> str:
    """Read a transcript file and return only the Zoom Recording Transcript section.

    Finds the '## Zoom Recording Transcript' heading and returns the content
    that follows, keeping any Meeting Notes out of the body.

    Falls back to all content after the separator for legacy plain-text files.
    """
    text = path.read_text(encoding="utf-8")
    sep_idx = text.find(SEPARATOR)
    if sep_idx == -1:
        return ""
    body = text[sep_idx + len(SEPARATOR) :]
    m = _TRANSCRIPT_SECTION_RE.search(body)
    if m:
        body = body[m.end() :].lstrip("\n")
    else:
        body = body.lstrip("\n")
    return body


_DURATION_RE = re.compile(r"(\d+)\s+minutes?")


def _parse_kv_block(path: Path, max_lines: int = 20) -> dict[str, str] | None:
    """Read key-value lines from a file up to the SEPARATOR or max_lines.

    Splits each line on the first colon only, so URLs in values are preserved
    correctly. Keys are lowercased and stripped; values are stripped.
    Returns None on OS error.
    """
    try:
        with open(path, encoding="utf-8") as f:
            kv: dict[str, str] = {}
            for _ in range(max_lines):
                line = f.readline()
                if not line:
                    break
                stripped = line.strip()
                if stripped == SEPARATOR:
                    break
                if ":" in stripped:
                    key, _, val = stripped.partition(":")
                    kv[key.strip().lower()] = val.strip()
            return kv
    except OSError:
        return None


def parse_header(path: Path) -> dict | None:
    """Parse the header of a transcript file.

    Supports both the legacy format (Source URL:) and the new format
    (Zoom Recording URL:). Fields are parsed as key-value pairs split
    on the first colon, so URLs in values are handled correctly.

    Returns a dict with keys: sig_name, date, duration_minutes, source_url.
    Returns None if required fields are missing or the file cannot be read.
    """
    kv = _parse_kv_block(path)
    if kv is None:
        return None

    sig_name = kv.get("sig")
    if not sig_name:
        return None

    date_str = kv.get("date")
    if not date_str:
        return None

    dur_match = _DURATION_RE.search(kv.get("duration", ""))
    if not dur_match:
        return None
    duration_minutes = int(dur_match.group(1))

    source_url = kv.get("zoom recording url") or kv.get("source url", "")
    if not source_url:
        return None

    return {
        "sig_name": sig_name,
        "date": date_str,
        "duration_minutes": duration_minutes,
        "source_url": source_url,
    }


def parse_reference(path: Path) -> dict | None:
    """Parse a metadata.md file containing stable SIG metadata.

    Returns a dict with keys: sig_name, meeting_notes_url, repository_url.
    Missing optional fields default to empty strings.
    Returns None if the file cannot be read.
    """
    kv = _parse_kv_block(path)
    if kv is None:
        return None

    return {
        "sig_name": kv.get("sig", ""),
        "meeting_notes_url": kv.get("meeting notes", ""),
        "repository_url": kv.get("repository", ""),
    }
