"""Google Sheet access: fetch public CSV export and filter meetings by date range."""

from __future__ import annotations

import csv
import io
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from urllib.parse import urlparse

import requests

SHEET_CSV_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s"
    "/gviz/tq?tqx=out:csv"
)


@dataclass(frozen=True)
class Meeting:
    sig_name: str
    sig_slug: str
    start_date: datetime
    duration_minutes: int
    url: str


# Maps generated slugs to a canonical slug so that SIGs recorded under
# multiple names in the spreadsheet always land in the same directory.
_CANONICAL_SLUGS: dict[str, str] = {
    "OpenTelemetry-CC-SIG": "CC-SIG",
    "GC-Project-Management-EU": "Governance-Committee",
}

_SLUG_STRIP_RE = re.compile(r"[^\w\s-]")
_SLUG_SPACE_RE = re.compile(r"\s+")
_ALLOWED_ZOOM_HOSTS = ("zoom.us", "zoom.com")


def sanitize_sig_name(name: str) -> str:
    """Convert a SIG name into a filesystem-safe directory name."""
    slug = _SLUG_STRIP_RE.sub("", name)
    slug = _SLUG_SPACE_RE.sub("-", slug.strip())
    return _CANONICAL_SLUGS.get(slug, slug)


def fetch_csv(url: str = SHEET_CSV_URL) -> list[dict[str, str]]:
    """Download the public CSV export and return rows as dicts."""
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    reader = csv.DictReader(io.StringIO(resp.text))
    return list(reader)


def _is_zoom_recording_url(url: str) -> bool:
    """Return True when URL is an HTTP(S) URL hosted on a Zoom domain."""
    # urlparse rarely raises, but can on malformed IPv6 literals.
    # None/empty hostname is handled below via `(parsed.hostname or "")`.
    try:
        parsed = urlparse(url.strip())
    except ValueError:
        return False

    if parsed.scheme not in ("http", "https"):
        return False

    host = (parsed.hostname or "").lower()
    if not host:
        return False

    return any(host == domain or host.endswith("." + domain) for domain in _ALLOWED_ZOOM_HOSTS)


def _parse_date(value: str) -> datetime | None:
    """Try several date formats that may appear in the sheet."""
    formats = [
        "%m/%d/%Y %H:%M:%S",
        "%m/%d/%Y %H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%m/%d/%Y",
        "%Y-%m-%d",
    ]
    value = value.strip()
    for fmt in formats:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def _parse_duration(value: str) -> int:
    """Return duration in minutes from a string like '60', '1:30' (H:MM), or '1:00:00' (H:MM:SS)."""
    value = value.strip()
    if not value:
        return 0
    if ":" in value:
        parts = value.split(":")
        try:
            if len(parts) == 3:
                return int(parts[0]) * 60 + int(parts[1])
            if len(parts) == 2:
                return int(parts[0]) * 60 + int(parts[1])
        except ValueError:
            return 0
    try:
        return int(float(value))
    except ValueError:
        return 0


def filter_meetings(
    rows: list[dict[str, str]],
    since: datetime | None = None,
    until: datetime | None = None,
) -> list[Meeting]:
    """
    Filter sheet rows to meetings in [since, until] that have a Zoom URL.

    Parameters
    ----------
    rows:
        Raw CSV rows from the sheet.
    since:
        Include meetings on or after this date (inclusive). Defaults to
        14 days ago.
    until:
        Include meetings on or before this date (inclusive). Defaults to now.
    """
    now = datetime.now()
    if since is None:
        since = (now - timedelta(days=14)).replace(hour=0, minute=0, second=0, microsecond=0)
    if until is None:
        until = now

    meetings: list[Meeting] = []
    for row in rows:
        # Normalize keys (strip whitespace, lowercase) for case-insensitive lookup
        row_lower = {k.strip().lower(): v.strip() for k, v in row.items() if k is not None}

        sig_name = (
            row_lower.get("name")
            or row_lower.get("sig")
            or row_lower.get("topic")
            or row_lower.get("meeting name")
            or ""
        ).strip()

        start_raw = (
            row_lower.get("start time") or row_lower.get("start") or row_lower.get("date") or ""
        ).strip()

        duration_raw = (
            row_lower.get("duration") or row_lower.get("duration (minutes)") or "0"
        ).strip()

        url = (
            row_lower.get("url")
            or row_lower.get("recording url")
            or row_lower.get("link")
            or row_lower.get("zoom url")
            or ""
        ).strip()

        if not url or not sig_name or not start_raw:
            continue

        # Only Zoom recording URLs hosted on official Zoom domains
        if not _is_zoom_recording_url(url):
            continue

        start_date = _parse_date(start_raw)
        if start_date is None:
            continue

        if start_date < since or start_date > until:
            continue

        duration = _parse_duration(duration_raw)
        if duration <= 5:
            continue

        meetings.append(
            Meeting(
                sig_name=sig_name,
                sig_slug=sanitize_sig_name(sig_name),
                start_date=start_date,
                duration_minutes=duration,
                url=url,
            )
        )

    # Sort by SIG name then date for deterministic output
    meetings.sort(key=lambda m: (m.sig_name, m.start_date))
    return meetings
