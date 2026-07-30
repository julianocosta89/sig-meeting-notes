"""LFX platform access: fetch the public LFX meetings API and filter by date range.

Replaces the Google Sheet as the meeting-discovery source going forward.
Unlike the Sheet, the ``/past`` endpoint only reliably returns roughly the
last few weeks of meetings regardless of how far back ``start_date`` is
set — historical data older than that must still come from the Sheet while
it remains available.
"""

from __future__ import annotations

from datetime import datetime, timedelta

import requests

from scraper.sheet import Meeting, _is_zoom_recording_url, sanitize_sig_name

LFX_API_BASE = "https://pcc-bff.platform.linuxfoundation.org/production/api/v2/itx-services"
PROJECT_SLUG = "opentelemetry"


def fetch_past_meetings(
    since: datetime,
    until: datetime,
    project_slug: str = PROJECT_SLUG,
    base_url: str = LFX_API_BASE,
) -> list[dict]:
    """Download raw past-meeting records from the public LFX API."""
    resp = requests.get(
        f"{base_url}/public/meetings/{project_slug}/past",
        params={
            "start_date": since.date().isoformat(),
            "end_date": until.date().isoformat(),
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json().get("meetings", [])


def _parse_start(value: str) -> datetime | None:
    """Parse the API's ISO 8601 start timestamp into a naive datetime."""
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    return parsed.replace(tzinfo=None)


def _parse_duration(value: object) -> int:
    """Return an int duration in minutes; non-numeric input yields 0."""
    try:
        return int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def filter_meetings(
    rows: list[dict],
    since: datetime | None = None,
    until: datetime | None = None,
) -> list[Meeting]:
    """
    Filter raw LFX API records to meetings in [since, until] with a recording.

    Mirrors scraper.sheet.filter_meetings: defaults to the last 14 days,
    requires a Zoom recording URL, and excludes trivial (<=5 min) meetings.
    Also skips any record flagged restricted/non-public, since this feeds a
    public archive site.
    """
    now = datetime.now()
    if since is None:
        since = (now - timedelta(days=14)).replace(hour=0, minute=0, second=0, microsecond=0)
    if until is None:
        until = now

    meetings: list[Meeting] = []
    for row in rows:
        sig_name = (row.get("title") or "").strip()
        if not sig_name:
            continue

        start_date = _parse_start(row.get("start") or "")
        if start_date is None:
            continue

        if start_date < since or start_date > until:
            continue

        props = row.get("extendedProps") or {}

        if props.get("restricted") or props.get("visibility", "public") != "public":
            continue

        url = (props.get("recording") or "").strip()
        if not url or not _is_zoom_recording_url(url):
            continue

        duration = _parse_duration(props.get("duration"))
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

    meetings.sort(key=lambda m: (m.sig_name, m.start_date))
    return meetings
