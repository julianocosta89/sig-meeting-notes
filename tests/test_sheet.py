"""Tests for scraper/sheet.py URL filtering and meeting selection."""

from __future__ import annotations

from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest

from scraper.sheet import (
    _is_zoom_recording_url,
    _parse_date,
    _parse_duration,
    fetch_csv,
    filter_meetings,
    sanitize_sig_name,
)


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


# ---------------------------------------------------------------------------
# sanitize_sig_name
# ---------------------------------------------------------------------------


class TestSanitizeSigName:
    def test_basic_name(self) -> None:
        assert sanitize_sig_name("Go SIG") == "Go-SIG"

    def test_strips_special_chars(self) -> None:
        assert sanitize_sig_name("Go SIG (Extra)") == "Go-SIG-Extra"

    def test_collapses_multiple_spaces(self) -> None:
        result = sanitize_sig_name("Go  SIG")
        assert result == "Go-SIG"

    def test_canonical_cc_sig(self) -> None:
        assert sanitize_sig_name("OpenTelemetry CC-SIG") == "CC-SIG"

    def test_canonical_governance(self) -> None:
        assert sanitize_sig_name("GC Project Management EU") == "Governance-Committee"


# ---------------------------------------------------------------------------
# fetch_csv
# ---------------------------------------------------------------------------


class TestFetchCsv:
    def test_returns_parsed_rows(self) -> None:
        csv_text = (
            "Name,Start Time,Duration,URL\nGo SIG,2026-02-05 10:00,60,https://zoom.us/rec/share/x\n"
        )
        mock_resp = MagicMock()
        mock_resp.text = csv_text
        mock_resp.raise_for_status = MagicMock()
        with patch("scraper.sheet.requests.get", return_value=mock_resp):
            rows = fetch_csv()
        assert len(rows) == 1
        assert rows[0]["Name"] == "Go SIG"

    def test_raises_on_http_error(self) -> None:
        mock_resp = MagicMock()
        mock_resp.raise_for_status.side_effect = Exception("403 Forbidden")
        with patch("scraper.sheet.requests.get", return_value=mock_resp):
            with pytest.raises(Exception):
                fetch_csv()


# ---------------------------------------------------------------------------
# _parse_date
# ---------------------------------------------------------------------------


class TestParseDate:
    def test_mm_dd_yyyy_hhmmss(self) -> None:
        assert _parse_date("02/05/2026 10:00:00") == datetime(2026, 2, 5, 10, 0, 0)

    def test_mm_dd_yyyy_hhmm(self) -> None:
        assert _parse_date("02/05/2026 10:00") == datetime(2026, 2, 5, 10, 0)

    def test_yyyy_mm_dd_hhmmss(self) -> None:
        assert _parse_date("2026-02-05 10:00:00") == datetime(2026, 2, 5, 10, 0, 0)

    def test_yyyy_mm_dd_hhmm(self) -> None:
        assert _parse_date("2026-02-05 10:00") == datetime(2026, 2, 5, 10, 0)

    def test_mm_dd_yyyy(self) -> None:
        assert _parse_date("02/05/2026") == datetime(2026, 2, 5)

    def test_yyyy_mm_dd(self) -> None:
        assert _parse_date("2026-02-05") == datetime(2026, 2, 5)

    def test_invalid_returns_none(self) -> None:
        assert _parse_date("not-a-date") is None

    def test_strips_whitespace(self) -> None:
        assert _parse_date("  2026-02-05  ") == datetime(2026, 2, 5)


# ---------------------------------------------------------------------------
# _parse_duration
# ---------------------------------------------------------------------------


class TestParseDuration:
    def test_plain_integer(self) -> None:
        assert _parse_duration("60") == 60

    def test_float_truncates(self) -> None:
        assert _parse_duration("60.5") == 60

    def test_h_mm_format(self) -> None:
        assert _parse_duration("1:30") == 90

    def test_h_mm_ss_format(self) -> None:
        assert _parse_duration("1:30:00") == 90

    def test_empty_returns_zero(self) -> None:
        assert _parse_duration("") == 0

    def test_whitespace_only_returns_zero(self) -> None:
        assert _parse_duration("  ") == 0

    def test_invalid_colon_format(self) -> None:
        assert _parse_duration("a:b") == 0

    def test_invalid_plain(self) -> None:
        assert _parse_duration("abc") == 0


# ---------------------------------------------------------------------------
# filter_meetings — additional cases
# ---------------------------------------------------------------------------


_RANGE = dict(since=datetime(2026, 2, 1), until=datetime(2026, 2, 28, 23, 59))


class TestFilterMeetingsColumnSynonyms:
    def test_sig_column_for_name(self) -> None:
        row = {
            "SIG": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_topic_column_for_name(self) -> None:
        row = {
            "Topic": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_meeting_name_column(self) -> None:
        row = {
            "Meeting Name": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_start_column_for_date(self) -> None:
        row = {
            "Name": "Example SIG",
            "Start": "2026-02-05 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_date_column_for_start(self) -> None:
        row = {
            "Name": "Example SIG",
            "Date": "2026-02-05",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_recording_url_column(self) -> None:
        row = {
            "Name": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "Recording URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_link_column(self) -> None:
        row = {
            "Name": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "Link": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_zoom_url_column(self) -> None:
        row = {
            "Name": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "Zoom URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_duration_minutes_column(self) -> None:
        row = {
            "Name": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration (minutes)": "30",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1

    def test_duration_too_short_excluded(self) -> None:
        row = {
            "Name": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "5",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert filter_meetings([row], **_RANGE) == []

    def test_missing_url_excluded(self) -> None:
        row = {"Name": "Example SIG", "Start Time": "2026-02-05 10:00", "Duration": "30"}
        assert filter_meetings([row], **_RANGE) == []

    def test_missing_name_excluded(self) -> None:
        row = {
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert filter_meetings([row], **_RANGE) == []

    def test_none_key_rows_handled(self) -> None:
        row = {
            None: "junk",
            "Name": "Example SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/x",
        }
        assert len(filter_meetings([row], **_RANGE)) == 1


def test_filter_meetings_default_dates_includes_recent() -> None:
    """A meeting from yesterday should be included when since/until are defaulted."""
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    row = {
        "Name": "Recent SIG",
        "Start Time": yesterday,
        "Duration": "30",
        "URL": "https://zoom.us/rec/share/recent",
    }
    meetings = filter_meetings([row])
    assert len(meetings) == 1
    assert meetings[0].sig_name == "Recent SIG"


def test_filter_meetings_default_dates_excludes_old() -> None:
    """A meeting 30 days ago is beyond the 14-day default window."""
    old_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d %H:%M")
    row = {
        "Name": "Old SIG",
        "Start Time": old_date,
        "Duration": "30",
        "URL": "https://zoom.us/rec/share/old",
    }
    assert filter_meetings([row]) == []


def test_filter_meetings_sorted_by_sig_then_date() -> None:
    rows = [
        {
            "Name": "Zebra SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/z",
        },
        {
            "Name": "Alpha SIG",
            "Start Time": "2026-02-10 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/a1",
        },
        {
            "Name": "Alpha SIG",
            "Start Time": "2026-02-05 10:00",
            "Duration": "30",
            "URL": "https://zoom.us/rec/share/a2",
        },
    ]
    meetings = filter_meetings(rows, **_RANGE)
    assert meetings[0].sig_name == "Alpha SIG"
    assert meetings[0].start_date == datetime(2026, 2, 5, 10, 0)
    assert meetings[1].sig_name == "Alpha SIG"
    assert meetings[1].start_date == datetime(2026, 2, 10, 10, 0)
    assert meetings[2].sig_name == "Zebra SIG"


def test_is_zoom_url_handles_valueerror() -> None:
    """urlparse raising ValueError should be caught and return False."""
    with patch("scraper.sheet.urlparse", side_effect=ValueError("malformed IPv6")):
        assert not _is_zoom_recording_url("https://[malformed")
