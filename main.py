#!/usr/bin/env python3
"""
OTel SIG Meeting Transcript Downloader
=======================================
Fetches OpenTelemetry SIG meeting recordings from the shared Google
Spreadsheet, visits each Zoom recording page, extracts the transcript,
and saves it organised by SIG name and meeting date.

Usage
-----
    uv run python main.py

Output
------
    transcripts/
      {sig-slug}/
        YYYY-MM-DD.txt
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from scraper.sheet import Meeting, fetch_csv, filter_meetings
from scraper.zoom import ZoomScrapeError, scrape_transcript

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("main")

TRANSCRIPTS_DIR = Path(__file__).parent / "transcripts"

SEPARATOR = "=" * 60


def make_output_path(meeting: Meeting) -> Path:
    date_str = meeting.start_date.strftime("%Y-%m-%d")
    return TRANSCRIPTS_DIR / meeting.sig_slug / f"{date_str}.txt"


def write_transcript(path: Path, meeting: Meeting, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        f"SIG: {meeting.sig_name}\n"
        f"Date: {meeting.start_date.strftime('%Y-%m-%d')}\n"
        f"Duration: {meeting.duration_minutes} minutes\n"
        f"Source URL: {meeting.url}\n"
        f"{SEPARATOR}\n\n"
    )
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")
    logger.info("Saved %s", path)


def process_meetings(meetings: list[Meeting]) -> int:
    """
    Scrape transcripts for all meetings.

    Returns the number of failures (0 = full success).
    """
    failures = 0

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        try:
            for meeting in meetings:
                out_path = make_output_path(meeting)

                if out_path.exists():
                    logger.info(
                        "Skipping %s %s — already downloaded",
                        meeting.sig_name,
                        meeting.start_date.date(),
                    )
                    continue

                logger.info(
                    "Processing: %s  %s  %s",
                    meeting.sig_name,
                    meeting.start_date.date(),
                    meeting.url,
                )

                # Fresh context + page per recording to avoid state leakage
                context = browser.new_context()
                page = context.new_page()
                try:
                    lines = scrape_transcript(page, meeting.url)
                    write_transcript(out_path, meeting, lines)
                except ZoomScrapeError as exc:
                    logger.warning("Skipped — %s", exc)
                    failures += 1
                except Exception as exc:  # noqa: BLE001
                    logger.error("Unexpected error for %s: %s", meeting.url, exc)
                    failures += 1
                finally:
                    page.close()
                    context.close()
        finally:
            browser.close()

    return failures


def main() -> int:
    logger.info("Fetching Google Sheet …")
    try:
        rows = fetch_csv()
    except Exception as exc:  # noqa: BLE001
        logger.error("Failed to fetch sheet: %s", exc)
        return 1

    meetings = filter_meetings(rows)
    logger.info("Found %d February 2026 meetings with Zoom URLs", len(meetings))

    if not meetings:
        logger.warning("No meetings found — check sheet URL and column names")
        return 0

    for m in meetings:
        logger.info(
            "  • %s  %s  %s",
            m.sig_name,
            m.start_date.strftime("%Y-%m-%d"),
            m.url,
        )

    failures = process_meetings(meetings)

    if failures:
        logger.warning(
            "Completed with %d failure(s) out of %d meetings",
            failures,
            len(meetings),
        )
        return 1

    logger.info("All %d meetings processed successfully", len(meetings))
    return 0


if __name__ == "__main__":
    sys.exit(main())
