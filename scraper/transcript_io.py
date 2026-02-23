"""Shared transcript I/O helpers.

Provides the canonical header parser and separator constant used by
both build_site.py and generate_summaries.py.
"""
from __future__ import annotations

import re
from pathlib import Path

SEPARATOR = "=" * 60

_DURATION_RE = re.compile(r"(\d+)\s+minutes?")


def parse_header(path: Path) -> dict | None:
    """Parse the 4-line header of a transcript file.

    Returns a dict with keys: sig_name, date, duration_minutes, source_url.
    Returns None if the header cannot be parsed.
    """
    try:
        with open(path, encoding="utf-8") as f:
            lines = [f.readline() for _ in range(5)]
    except OSError:
        return None

    if len(lines) < 5:
        return None

    sig_line = lines[0].strip()
    date_line = lines[1].strip()
    duration_line = lines[2].strip()
    url_line = lines[3].strip()

    if not sig_line.startswith("SIG:"):
        return None
    sig_name = sig_line[len("SIG:"):].strip()

    if not date_line.startswith("Date:"):
        return None
    date_str = date_line[len("Date:"):].strip()

    if not duration_line.startswith("Duration:"):
        return None
    dur_match = _DURATION_RE.search(duration_line)
    if not dur_match:
        return None
    duration_minutes = int(dur_match.group(1))

    if not url_line.startswith("Source URL:"):
        return None
    source_url = url_line[len("Source URL:"):].strip()

    return {
        "sig_name": sig_name,
        "date": date_str,
        "duration_minutes": duration_minutes,
        "source_url": source_url,
    }
