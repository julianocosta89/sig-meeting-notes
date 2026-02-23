#!/usr/bin/env python3
"""
OTel SIG Meeting Transcript Downloader
=======================================
Fetches OpenTelemetry SIG meeting recordings from the shared Google
Spreadsheet, visits each Zoom recording page, extracts the transcript,
and saves it organized by SIG name and meeting date.

Usage
-----
    uv run python main.py --since 2026-02-01

    Fetches all meetings from 2026-02-01 (inclusive) through today.
    Omit --since to default to the first day of the current month.

Output
------
    transcripts/
      {sig-slug}/
        YYYY-MM-DD.txt
"""
from __future__ import annotations

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

from scraper.sheet import Meeting, fetch_csv, filter_meetings
from scraper.zoom import ZoomScrapeError, scrape_transcript

logger = logging.getLogger(__name__)

TRANSCRIPTS_DIR = Path(__file__).parent / "transcripts"

SEPARATOR = "=" * 60

# Shorthand aliases expanded before matching SIG slugs.
# Keys are lowercase; values are the search terms tried against the slug.
_SIG_ALIASES: dict[str, list[str]] = {
    "otel":     ["opentelemetry", "otel"],
    "opentelemetry": ["opentelemetry", "otel"],
    "gc":       ["gc"],
    "tc":       ["technical-committee"],
    "semconv":              ["semantic-convention", "semconv", "sem-conv"],
    "sem-conv":             ["semantic-convention", "semconv", "sem-conv"],
    "semantic-convention":  ["semantic-convention", "semconv", "sem-conv"],
    "semantic-conventions": ["semantic-convention", "semconv", "sem-conv"],
    "devex":    ["developer-experience"],
    "browser":  ["client"],
    "cc":       ["cc"],
    "c":        ["cc"],
    "cpp":      ["cc"],
    "c++":      ["cc"],
    "k8s":      ["kubernetes", "k8s"],
    "js":       ["javascript"],
    "dotnet":   ["net-"],
    ".net":     ["net-"],
    "lambda":   ["faas"],
    "serverless": ["faas"],
}


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


def process_meetings(meetings: list[Meeting]) -> tuple[int, list[str]]:
    """
    Scrape transcripts for all meetings.

    Returns (failure_count, skipped_urls).
    """
    failures = 0
    skipped_urls: list[str] = []

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
                    skipped_urls.append(meeting.url)
                    failures += 1
                except Exception:  # noqa: BLE001
                    logger.exception("Unexpected error for %s", meeting.url)
                    skipped_urls.append(meeting.url)
                    failures += 1
                finally:
                    page.close()
                    context.close()
        finally:
            browser.close()

    return failures, skipped_urls


def _resolve_sig(meetings: list[Meeting], sig_filter: str) -> str | None:
    """
    Return the SIG slug to use given a user-supplied filter string.

    Known abbreviations (e.g. 'gc', 'semconv') are expanded to their full
    search terms before matching.  See _SIG_ALIASES for the full list.

    - No matches  → logs a warning and returns None (caller should exit).
    - One match   → returns it directly.
    - Many matches → prints a numbered list and prompts the user to pick one.
    """
    search_terms = _SIG_ALIASES.get(sig_filter.lower(), [sig_filter])
    matched = sorted({
        m.sig_slug for m in meetings
        if any(term.lower() in m.sig_slug.lower() for term in search_terms)
    })

    if not matched:
        logger.warning("No SIG matching %r found in the given date range", sig_filter)
        return None

    if len(matched) == 1:
        return matched[0]

    print(f"\nMultiple SIGs match {sig_filter!r}. Please choose one:\n")
    for i, slug in enumerate(matched, 1):
        print(f"  {i}. {slug}")

    while True:
        try:
            raw = input("\nEnter number: ").strip()
            idx = int(raw) - 1
            if 0 <= idx < len(matched):
                return matched[idx]
            print(f"Please enter a number between 1 and {len(matched)}.")
        except ValueError:
            print("Invalid input — please enter a number.")
        except (EOFError, KeyboardInterrupt):
            print("\nAborted.")
            return None


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download OTel SIG meeting transcripts from Zoom recordings."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--since",
        metavar="YYYY-MM-DD",
        default=None,
        help=(
            "Fetch meetings on or after this date (inclusive). "
            "Defaults to the first day of the current month."
        ),
    )
    group.add_argument(
        "--between",
        nargs=2,
        metavar=("START", "END"),
        default=None,
        help="Fetch meetings between START and END dates (both inclusive, YYYY-MM-DD).",
    )
    parser.add_argument(
        "--sig",
        metavar="SIG_SLUG",
        default=None,
        help=(
            "Case-insensitive substring filter on the SIG slug "
            "(e.g. 'Community-Demo-App-SIG' or just 'collector'). "
            "Shorthands are expanded automatically: "
            "otel→OpenTelemetry, gc→CC, tc→Technical-Committee, "
            "semconv/sem-conv→Semantic-Convention, devex→Developer-Experience, "
            "browser→Client, cc→CC, k8s→Kubernetes, js→JavaScript, "
            "dotnet/.net→NET, lambda/serverless→FaaS."
        ),
    )
    return parser.parse_args()


def _parse_date(value: str, flag: str) -> datetime | None:
    """Parse a YYYY-MM-DD string, logging a useful error on failure."""
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        logger.error("Invalid %s date %r — expected YYYY-MM-DD", flag, value)
        return None


def main() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
        datefmt="%H:%M:%S",
    )
    args = _parse_args()

    since: datetime | None = None
    until: datetime | None = None

    if args.between:
        since = _parse_date(args.between[0], "--between START")
        until = _parse_date(args.between[1], "--between END")
        if since is None or until is None:
            return 1
        if since > until:
            logger.error("--between START (%s) must not be after END (%s)", args.between[0], args.between[1])
            return 1
    elif args.since:
        since = _parse_date(args.since, "--since")
        if since is None:
            return 1

    logger.info("Fetching Google Sheet …")
    try:
        rows = fetch_csv()
    except Exception:  # noqa: BLE001
        logger.exception("Failed to fetch sheet")
        return 1

    meetings = filter_meetings(rows, since=since, until=until)

    if args.sig:
        resolved_slug = _resolve_sig(meetings, args.sig)
        if resolved_slug is None:
            return 1
        meetings = [m for m in meetings if m.sig_slug == resolved_slug]

    if args.between:
        range_label = f"{args.between[0]} → {args.between[1]}"
    elif since:
        range_label = f"since {since.strftime('%Y-%m-%d')}"
    else:
        range_label = "start of current month"
    logger.info("Found %d meetings with Zoom URLs (%s)", len(meetings), range_label)

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

    failures, skipped_urls = process_meetings(meetings)

    if skipped_urls:
        print("\nSkipped recordings (no transcript found):")
        for url in skipped_urls:
            print(f"  {url}")

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
