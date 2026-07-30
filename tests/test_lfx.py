"""Tests for scraper/lfx.py: the LFX platform public meetings API client."""

from __future__ import annotations

from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from scraper.lfx import (
    LFX_API_BASE,
    PROJECT_SLUG,
    _parse_duration,
    _parse_start,
    fetch_past_meetings,
    filter_meetings,
)


def _row(
    title: str = "Example SIG",
    start: str = "2026-02-05T10:00:00Z",
    duration: int = 30,
    recording: str = "https://zoom.us/rec/share/abc123",
    **extra_props: object,
) -> dict:
    props = {
        "duration": duration,
        "recording": recording,
        "restricted": False,
        "visibility": "public",
        "meeting_id": 123456789,
        "project_slug": "opentelemetry",
    }
    props.update(extra_props)
    return {"id": 1234567890000, "title": title, "start": start, "extendedProps": props}


_RANGE = dict(since=datetime(2026, 2, 1), until=datetime(2026, 2, 28, 23, 59, 59))


# ---------------------------------------------------------------------------
# fetch_past_meetings
# ---------------------------------------------------------------------------


class TestFetchPastMeetings:
    def test_returns_meetings_list(self) -> None:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"meetings": [_row()]}
        mock_resp.raise_for_status = MagicMock()
        with patch("scraper.lfx.requests.get", return_value=mock_resp) as mock_get:
            meetings = fetch_past_meetings(datetime(2026, 2, 1), datetime(2026, 2, 28))

        assert len(meetings) == 1
        mock_get.assert_called_once_with(
            f"{LFX_API_BASE}/public/meetings/{PROJECT_SLUG}/past",
            params={"start_date": "2026-02-01", "end_date": "2026-02-28"},
            timeout=30,
        )

    def test_missing_meetings_key_returns_empty_list(self) -> None:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {}
        mock_resp.raise_for_status = MagicMock()
        with patch("scraper.lfx.requests.get", return_value=mock_resp):
            meetings = fetch_past_meetings(datetime(2026, 2, 1), datetime(2026, 2, 28))
        assert meetings == []

    def test_uses_custom_project_slug_and_base_url(self) -> None:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"meetings": []}
        mock_resp.raise_for_status = MagicMock()
        with patch("scraper.lfx.requests.get", return_value=mock_resp) as mock_get:
            fetch_past_meetings(
                datetime(2026, 2, 1),
                datetime(2026, 2, 28),
                project_slug="other-project",
                base_url="https://example.test/api",
            )
        mock_get.assert_called_once_with(
            "https://example.test/api/public/meetings/other-project/past",
            params={"start_date": "2026-02-01", "end_date": "2026-02-28"},
            timeout=30,
        )

    def test_raises_on_http_error(self) -> None:
        mock_resp = MagicMock()
        mock_resp.raise_for_status.side_effect = Exception("503 Service Unavailable")
        with patch("scraper.lfx.requests.get", return_value=mock_resp):
            with pytest.raises(Exception):
                fetch_past_meetings(datetime(2026, 2, 1), datetime(2026, 2, 28))


# ---------------------------------------------------------------------------
# _parse_start
# ---------------------------------------------------------------------------


class TestParseStart:
    def test_z_suffix_utc(self) -> None:
        assert _parse_start("2026-02-05T10:00:00Z") == datetime(2026, 2, 5, 10, 0, 0)

    def test_explicit_offset(self) -> None:
        assert _parse_start("2026-02-05T10:00:00+00:00") == datetime(2026, 2, 5, 10, 0, 0)

    def test_empty_returns_none(self) -> None:
        assert _parse_start("") is None

    def test_invalid_returns_none(self) -> None:
        assert _parse_start("not-a-date") is None


# ---------------------------------------------------------------------------
# _parse_duration
# ---------------------------------------------------------------------------


class TestParseDuration:
    def test_plain_int(self) -> None:
        assert _parse_duration(30) == 30

    def test_numeric_string(self) -> None:
        assert _parse_duration("45") == 45

    def test_none_returns_zero(self) -> None:
        assert _parse_duration(None) == 0

    def test_invalid_string_returns_zero(self) -> None:
        assert _parse_duration("abc") == 0


# ---------------------------------------------------------------------------
# filter_meetings
# ---------------------------------------------------------------------------


class TestFilterMeetings:
    def test_includes_valid_meeting_in_range(self) -> None:
        meetings = filter_meetings([_row()], **_RANGE)
        assert len(meetings) == 1
        m = meetings[0]
        assert m.sig_name == "Example SIG"
        assert m.sig_slug == "Example-SIG"
        assert m.start_date == datetime(2026, 2, 5, 10, 0, 0)
        assert m.duration_minutes == 30
        assert m.url == "https://zoom.us/rec/share/abc123"

    def test_excludes_missing_title(self) -> None:
        row = _row(title="")
        assert filter_meetings([row], **_RANGE) == []

    def test_excludes_missing_start(self) -> None:
        row = _row(start="")
        assert filter_meetings([row], **_RANGE) == []

    def test_excludes_out_of_range_start(self) -> None:
        row = _row(start="2026-03-05T10:00:00Z")
        assert filter_meetings([row], **_RANGE) == []

    def test_excludes_missing_recording(self) -> None:
        row = _row(recording="")
        assert filter_meetings([row], **_RANGE) == []

    def test_excludes_spoofed_recording_host(self) -> None:
        row = _row(recording="https://evil.example/path?next=zoom.us")
        assert filter_meetings([row], **_RANGE) == []

    def test_excludes_trivial_duration(self) -> None:
        row = _row(duration=5)
        assert filter_meetings([row], **_RANGE) == []

    def test_excludes_restricted(self) -> None:
        row = _row(restricted=True)
        assert filter_meetings([row], **_RANGE) == []

    def test_excludes_non_public_visibility(self) -> None:
        row = _row(visibility="private")
        assert filter_meetings([row], **_RANGE) == []

    def test_canonical_slug_mapping_applied(self) -> None:
        row = _row(title="OpenTelemetry CC-SIG")
        meetings = filter_meetings([row], **_RANGE)
        assert len(meetings) == 1
        assert meetings[0].sig_slug == "CC-SIG"

    def test_sorted_by_sig_then_date(self) -> None:
        rows = [
            _row(title="Zebra SIG", start="2026-02-05T10:00:00Z"),
            _row(title="Alpha SIG", start="2026-02-10T10:00:00Z"),
            _row(title="Alpha SIG", start="2026-02-05T10:00:00Z"),
        ]
        meetings = filter_meetings(rows, **_RANGE)
        assert meetings[0].sig_name == "Alpha SIG"
        assert meetings[0].start_date == datetime(2026, 2, 5, 10, 0)
        assert meetings[1].sig_name == "Alpha SIG"
        assert meetings[1].start_date == datetime(2026, 2, 10, 10, 0)
        assert meetings[2].sig_name == "Zebra SIG"

    def test_default_dates_includes_recent(self) -> None:
        from datetime import timedelta

        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        row = _row(title="Recent SIG", start=yesterday)
        meetings = filter_meetings([row])
        assert len(meetings) == 1
        assert meetings[0].sig_name == "Recent SIG"

    def test_default_dates_excludes_old(self) -> None:
        from datetime import timedelta

        old_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        row = _row(title="Old SIG", start=old_date)
        assert filter_meetings([row]) == []
