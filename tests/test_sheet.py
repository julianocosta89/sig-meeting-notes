"""Tests for scraper/sheet.py URL filtering and meeting selection."""
from __future__ import annotations

from datetime import datetime

from scraper.sheet import _is_zoom_recording_url, filter_meetings


def _row(url: str) -> dict[str, str]:
    return {
        "Name": "Example SIG",
        "Start Time": "2026-02-05 10:00",
        "Duration": "30",
        "URL": url,
    }


def test_is_zoom_recording_url_accepts_zoom_subdomains() -> None:
    assert _is_zoom_recording_url("https://us02web.zoom.us/rec/share/abc123")
    assert _is_zoom_recording_url("https://zoom.com/rec/share/abc123")


def test_is_zoom_recording_url_rejects_non_http_schemes() -> None:
    assert not _is_zoom_recording_url("javascript:alert(1)")
    assert not _is_zoom_recording_url("data:text/plain,zoom.us")


def test_is_zoom_recording_url_rejects_substring_spoofing() -> None:
    assert not _is_zoom_recording_url("https://evil.example/path?next=zoom.us")
    assert not _is_zoom_recording_url("https://zoom.us.evil.example/rec/share/abc123")


def test_filter_meetings_includes_valid_zoom_host() -> None:
    meetings = filter_meetings(
        [_row("https://us06web.zoom.us/rec/share/ok")],
        since=datetime(2026, 2, 1),
        until=datetime(2026, 2, 28, 23, 59, 59),
    )
    assert len(meetings) == 1
    assert meetings[0].url == "https://us06web.zoom.us/rec/share/ok"


def test_filter_meetings_excludes_spoofed_zoom_url() -> None:
    meetings = filter_meetings(
        [_row("https://evil.example/path?next=zoom.us")],
        since=datetime(2026, 2, 1),
        until=datetime(2026, 2, 28, 23, 59, 59),
    )
    assert meetings == []

