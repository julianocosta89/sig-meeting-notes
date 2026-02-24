"""Community README parser for bootstrapping SIG metadata.

Fetches the OTel community README once per session and extracts the
Google Doc meeting-notes URL for each SIG from the Markdown tables.
This module is used only to bootstrap missing metadata.md files; it is
NOT called on every scraper run.

Repository column is absent from the community README tables, so
repository_url is always returned as an empty string (fill in manually).
"""
from __future__ import annotations

import re

import requests

README_URL = (
    "https://raw.githubusercontent.com/open-telemetry/community/main/README.md"
)

# Matches: [Google Doc](https://docs.google.com/...)
_GDOC_RE = re.compile(r"\[Google Doc\]\((https://docs\.google\.com/[^)]+)\)")

# Used to strip inline HTML from table cells (e.g. anchor tags, <sup>)
_HTML_RE = re.compile(r"<[^>]+>")

# HTML entities (e.g. &nbsp;)
_ENTITY_RE = re.compile(r"&\w+;")

# Special characters to strip when building a slug key (keep word chars, spaces, hyphens)
_NONWORD_RE = re.compile(r"[^\w\s-]")

# Collapse whitespace
_SPACE_RE = re.compile(r"\s+")

# Module-level cache: populated on first call to get_meeting_notes_url()
_cache: dict[str, str] | None = None


def _cell_to_key(cell: str) -> str:
    """Derive a normalised slug key from a README table name cell.

    Examples:
      'Java: SDK + Instrumentation<a …>' → 'java'
      'Semantic Conventions: …'          → 'semantic-conventions'
      'Go: SDK + Automatic …'            → 'go'
    """
    # Strip HTML tags and entities
    cell = _HTML_RE.sub("", cell)
    cell = _ENTITY_RE.sub(" ", cell).strip()

    # Use only the part before the first colon (e.g. "Java" from "Java: SDK + …")
    if ":" in cell:
        cell = cell.split(":")[0].strip()

    # Apply the same slug normalisation as sheet.sanitize_sig_name()
    cell = _NONWORD_RE.sub("", cell)
    cell = _SPACE_RE.sub("-", cell.strip())
    return cell.lower()


def _parse_readme(text: str) -> dict[str, str]:
    """Return a name-key → notes_url mapping parsed from the README markdown.

    Only rows where the third pipe-delimited cell contains a Google Doc link
    are considered; header/separator rows are skipped automatically.
    """
    sig_map: dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        # Split on '|' and drop the empty strings at both ends
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 3:
            continue
        gdoc_match = _GDOC_RE.search(cells[2])
        if not gdoc_match:
            continue
        key = _cell_to_key(cells[0])
        # Skip the header row (key would be "name") and separator rows
        if not key or key == "name" or set(key) <= {"-"}:
            continue
        sig_map[key] = gdoc_match.group(1)
    return sig_map


def _load(readme_url: str = README_URL) -> dict[str, str]:
    """Fetch and parse the README; return empty dict on any network error."""
    try:
        resp = requests.get(readme_url, timeout=15)
        resp.raise_for_status()
    except requests.RequestException:
        return {}
    return _parse_readme(resp.text)


def get_meeting_notes_url(slug: str, readme_url: str = README_URL) -> str:
    """Return the Google Doc meeting-notes URL for the given SIG slug.

    Fetches and caches the community README on the first call. Returns an
    empty string if no match is found or if the README cannot be fetched.

    Matching strategy (in order):
    1. Exact match: slug key == name key (e.g. 'go' == 'go')
    2. Prefix match: slug starts with name key + '-' (e.g. 'go-sig' → 'go')
    3. Reverse prefix: name key starts with slug + '-' (e.g. 'collector' in 'collector-sig')
    """
    global _cache
    if _cache is None:
        _cache = _load(readme_url)

    target = slug.lower()
    for key, url in _cache.items():
        if target == key:
            return url
        if target.startswith(key + "-"):
            return url
        if key.startswith(target + "-"):
            return url

    return ""
