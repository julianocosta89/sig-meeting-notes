"""Google Docs meeting-notes scraper.

Fetches the Markdown export of a public Google Doc and extracts the
Attendees and Agenda content for a specific meeting date.

Everything is best-effort: if the doc is private, the date section is
missing, or the formatting is unexpected, empty lists are returned
without raising.
"""
from __future__ import annotations

import re
from datetime import datetime

import requests

_DOC_ID_RE = re.compile(r"docs\.google\.com/document/d/([^/?#]+)")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)")
_LIST_ITEM_RE = re.compile(r"^( *)[-*]\s+(.+)")

# Matches a line that is likely a meeting-date separator in plain-text docs.
# Handles formats like:
#   "Feb 19, 2026 8:00 AM - General meeting"  (month-first)
#   "Wed, Feb 18, 2026 (Pacific Time)"         (weekday prefix)
#   "17 Feb 2026 11:00 AM PST"                 (day-first)
#   "2026-02-18"  /  "2026/02/18"              (ISO / slash)
_DATE_SEPARATOR_RE = re.compile(
    r"^(?:\w{2,9},?\s+)?"                              # optional weekday + comma
    r"(?:"
    r"\d{4}[-/]\d{1,2}[-/]\d{1,2}"                    # 2026-02-18 or 2026/02/18
    r"|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z.]*\s+\d{1,2}"  # Feb 18
    r"|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"         # 17 Feb
    r")",
    re.IGNORECASE,
)

# Labels that delimit subsections (attendees, agenda, …)
_STOP_KEYWORDS = frozenset({"attendee", "agenda", "note", "action", "topic"})

# In-process cache: export_url -> document text.  Avoids re-fetching the
# same Google Doc when processing multiple transcript dates for the same SIG.
_DOC_CACHE: dict[str, str] = {}


def _to_export_url(doc_url: str) -> str | None:
    """Convert any Google Doc URL to its Markdown export URL.

    Accepts edit, view, or share URLs.  Returns None if no doc ID is found.
    """
    m = _DOC_ID_RE.search(doc_url)
    if not m:
        return None
    return f"https://docs.google.com/document/d/{m.group(1)}/export?format=md"


def _date_variants(iso_date: str) -> list[str]:
    """Return multiple text representations of an ISO date for heading matching.

    Handles the date formats commonly used by OTel SIG doc authors.
    """
    try:
        dt = datetime.strptime(iso_date, "%Y-%m-%d")
    except ValueError:
        return [iso_date]
    return [
        iso_date,                                            # 2026-02-05
        f"{dt.year}/{dt.month:02d}/{dt.day:02d}",           # 2026/02/05
        f"{dt.year}/{dt.month}/{dt.day}",                   # 2026/2/5
        f"{dt.month}/{dt.day}/{dt.year}",                   # 2/5/2026
        f"{dt.month:02d}/{dt.day:02d}/{dt.year}",           # 02/05/2026
        dt.strftime("%B %d, %Y"),                            # February 05, 2026
        f"{dt.strftime('%B')} {dt.day}, {dt.year}",         # February 5, 2026
        dt.strftime("%b %d, %Y"),                            # Feb 05, 2026
        f"{dt.strftime('%b')} {dt.day}, {dt.year}",         # Feb 5, 2026
        dt.strftime("%b. %d, %Y"),                           # Feb. 05, 2026
        f"{dt.strftime('%b.')} {dt.day}, {dt.year}",        # Feb. 5, 2026
        f"{dt.day} {dt.strftime('%b')} {dt.year}",          # 5 Feb 2026
        f"{dt.day:02d} {dt.strftime('%b')} {dt.year}",      # 05 Feb 2026
    ]


def _unescape_md(text: str) -> str:
    """Remove backslash escapes added by Google Docs markdown export.

    Google Docs escapes characters like #, [, ], *, - when they appear
    literally in list items (e.g. ``\\#4568`` → ``#4568``).
    """
    return re.sub(r"\\(.)", r"\1", text)


def _normalize_date_text(text: str) -> str:
    """Strip bold markers and ordinal suffixes to normalise date text.

    Converts ``**Wed, Feb 19th, 2026**`` → ``Wed, Feb 19, 2026`` so that
    date variants without ordinals match correctly.
    """
    text = text.replace("**", "")
    text = re.sub(r"(\d)(st|nd|rd|th)\b", r"\1", text, flags=re.IGNORECASE)
    return text


def _find_date_section(md_text: str, date_variants: list[str]) -> str | None:
    """Return the text between the date marker and the next section boundary.

    Handles several formats:
    - Heading-based: ``# 2026-02-05`` — ends at next same-or-higher heading.
    - Plain-text ISO: ``2026-02-05`` on its own line — ends at the next
      date-separator line or end-of-document.
    - Plain-text with extra content: ``Feb 19, 2026 8:00 AM - General`` —
      detected when a line matches ``_DATE_SEPARATOR_RE`` and contains a
      date variant (after ordinal/bold normalisation).

    Returns None if no matching date is found.
    """
    lines = md_text.split("\n")
    section_start: int | None = None
    section_level: int | None = None
    is_plain = False  # True when matched via plain-text date line (no heading)
    section_has_content = False  # True once a real (non-separator) line is seen

    for i, line in enumerate(lines):
        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            text = _normalize_date_text(m.group(2).strip())

            # End a heading-based section at the next same-or-higher heading
            if section_start is not None and not is_plain and level <= section_level:
                return "\n".join(lines[section_start:i])

            for variant in date_variants:
                if variant in text:
                    section_start = i + 1
                    section_level = level
                    is_plain = False
                    section_has_content = False
                    break
        else:
            stripped = line.strip()
            if not stripped or re.match(r"^[-*]\s", stripped):
                continue  # skip empty lines and list items

            normalized = _normalize_date_text(stripped)
            is_target = any(v in normalized for v in date_variants)
            is_date_sep = bool(_DATE_SEPARATOR_RE.match(normalized))

            if is_target and is_date_sep:
                if section_start is not None:
                    return "\n".join(lines[section_start:i])
                section_start = i + 1
                section_level = None
                is_plain = True
                section_has_content = False
            elif is_plain and section_start is not None and is_date_sep and section_has_content:
                # Boundary: only fire after actual content has been seen,
                # so that multi-line date headers (e.g. Pacific/China timezone
                # pairs) don't prematurely end the section.
                return "\n".join(lines[section_start:i])
            elif is_plain and section_start is not None and not is_date_sep:
                section_has_content = True

    if section_start is not None:
        return "\n".join(lines[section_start:])
    return None


def _extract_subsection_md(section_text: str, keyword: str) -> list[str]:
    """Extract list items from the named subsection within a date section.

    Scans for a label line containing *keyword* (e.g. "Attendee:" or
    "Agenda:" or "**Attendees:**" or "Topics"), then collects list items
    (``*`` or ``-`` prefixed), preserving indentation depth as ``  - ``
    prefixes.  Stops when another known section label is encountered.
    """
    in_target = False
    items: list[str] = []

    for line in section_text.split("\n"):
        stripped = line.strip()

        # Section label: non-list line containing the keyword.
        # Use re.match to distinguish "* list item" from "**Bold label:**".
        # Allow up to 200 chars so inline-enriched labels (e.g. long Attendees
        # lines) are still recognised as labels.
        if (
            stripped
            and not re.match(r"^[-*]\s", stripped)
            and keyword.lower() in stripped.lower()
            and len(stripped) < 200
        ):
            in_target = True
            # Also capture content inline on the label line, e.g. "Attendees: Alice, Bob"
            inline_match = re.search(
                rf'\b{re.escape(keyword)}\w*\s*:\s*(.+)',
                stripped,
                re.IGNORECASE,
            )
            if inline_match:
                inline = inline_match.group(1).strip()
                # Discard if it's only formatting characters (e.g. "**" from "**Attendees:**")
                if re.search(r'\w', inline):
                    for part in re.split(r",\s*", inline):
                        part = part.strip()
                        if part:
                            items.append("- " + _unescape_md(part))
            continue

        # Stop at another known section label
        if in_target and stripped and not re.match(r"^[-*]\s", stripped):
            if any(kw in stripped.lower() for kw in _STOP_KEYWORDS) and len(stripped) < 200:
                break

        # Collect list items
        if in_target:
            m = _LIST_ITEM_RE.match(line.rstrip())
            if m:
                depth = len(m.group(1)) // 2
                text = _unescape_md(m.group(2).rstrip())
                items.append("  " * depth + "- " + text)

    return items


def fetch_meeting_notes(doc_url: str, date: str) -> dict[str, list[str]]:
    """Return {attendees: list[str], agenda: list[str]} for the given ISO date.

    Fetches the Google Doc Markdown export (read-only) and extracts the
    Attendees and Agenda content for the given meeting date.  Returns empty
    lists on any failure: private doc, missing date section, network error,
    or parse error.

    Agenda extraction tries the "Agenda" label first, then falls back to
    "Topics" and "Notes" for SIGs that use non-standard section names.
    """
    empty: dict[str, list[str]] = {"attendees": [], "agenda": []}

    export_url = _to_export_url(doc_url)
    if not export_url:
        return empty

    try:
        if export_url not in _DOC_CACHE:
            resp = requests.get(export_url, timeout=20)
            resp.raise_for_status()
            _DOC_CACHE[export_url] = resp.text
    except requests.RequestException:
        return empty

    try:
        section = _find_date_section(_DOC_CACHE[export_url], _date_variants(date))
        if not section:
            return empty

        agenda = _extract_subsection_md(section, "agenda")
        if not agenda:
            agenda = _extract_subsection_md(section, "topic")
        if not agenda:
            agenda = _extract_subsection_md(section, "note")

        return {
            "attendees": _extract_subsection_md(section, "attendee"),
            "agenda": agenda,
        }
    except Exception:  # noqa: BLE001
        return empty
