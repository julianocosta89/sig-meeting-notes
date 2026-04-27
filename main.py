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
    Omit --since to default to the last 14 days.

Output
------
    docs/content/
      {sig-slug}/
        metadata.md                    (stable SIG metadata; created once)
        YYYY-MM-DD/
          transcript.md                (header + ## Zoom Recording Transcript)
          meeting-notes.md             (attendees + agenda, only if non-empty)
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

from scraper import community, gdoc
from scraper.otel_setup import StatusCode, configure_tracer
from scraper.sheet import Meeting, fetch_csv, filter_meetings
from scraper.transcript_io import SEPARATOR, parse_reference
from scraper.zoom import ZoomScrapeError, scrape_transcript

logger = logging.getLogger(__name__)

TRANSCRIPTS_DIR = Path(__file__).parent / "docs" / "content"

# Shorthand aliases expanded before matching SIG slugs.
# Keys are lowercase; values are the search terms tried against the slug.
_SIG_ALIASES: dict[str, list[str]] = {
    "otel": ["opentelemetry", "otel"],
    "opentelemetry": ["opentelemetry", "otel"],
    "gc": ["gc"],
    "tc": ["technical-committee"],
    "semconv": ["semantic-convention", "semconv", "sem-conv"],
    "sem-conv": ["semantic-convention", "semconv", "sem-conv"],
    "semantic-convention": ["semantic-convention", "semconv", "sem-conv"],
    "semantic-conventions": ["semantic-convention", "semconv", "sem-conv"],
    "devex": ["developer-experience"],
    "cc": ["cc"],
    "c": ["cc"],
    "cpp": ["cc"],
    "c++": ["cc"],
    "k8s": ["kubernetes", "k8s"],
    "js": ["javascript"],
    "dotnet": ["net-"],
    ".net": ["net-"],
    "lambda": ["faas"],
    "serverless": ["faas"],
}


_SPEAKER_LINE_RE = re.compile(r"^(.+?)\s+(\d{1,2}:\d{2})\s+(.*)$")


def make_output_path(meeting: Meeting) -> Path:
    date_str = meeting.start_date.strftime("%Y-%m-%d")
    return TRANSCRIPTS_DIR / meeting.sig_slug / date_str / "transcript.md"


def _format_body_line(line: str) -> str:
    """Convert 'Speaker MM:SS utterance' to '**Speaker** MM:SS utterance'.

    Lines that don't match the speaker-timestamp pattern are returned as-is.
    """
    m = _SPEAKER_LINE_RE.match(line)
    if m:
        return f"**{m.group(1)}** {m.group(2)} {m.group(3)}"
    return line


def _ensure_metadata(meeting: Meeting, transcript_path: Path) -> str:
    """Return the meeting-notes URL for the SIG; bootstrap metadata.md if absent.

    If metadata.md doesn't exist in the SIG directory, fetches the URL from
    the community README once and writes the file. Returns "" if the URL
    cannot be determined (user can fill it in manually).
    """
    sig_dir = transcript_path.parent.parent
    metadata_path = sig_dir / "metadata.md"

    if metadata_path.exists():
        ref = parse_reference(metadata_path)
        return ref["meeting_notes_url"] if ref else ""

    notes_url = community.get_meeting_notes_url(meeting.sig_slug)
    sig_dir.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(
        f"SIG: {meeting.sig_name}\nMeeting Notes: {notes_url}\nRepository: \n",
        encoding="utf-8",
    )
    if notes_url:
        logger.info("Created metadata.md for %s", meeting.sig_slug)
    else:
        logger.info(
            "Created metadata.md for %s (no notes URL found — fill in manually)",
            meeting.sig_slug,
        )
    return notes_url


def write_transcript(
    path: Path,
    meeting: Meeting,
    lines: list[str],
    notes: dict[str, list[str]] | None = None,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    date_str = meeting.start_date.strftime("%Y-%m-%d")

    parts = [
        f"SIG: {meeting.sig_name}",
        f"Date: {date_str}",
        f"Duration: {meeting.duration_minutes} minutes",
        f"Zoom Recording URL: {meeting.url}",
        SEPARATOR,
        "",
        "## Zoom Recording Transcript",
        "",
    ]

    parts.extend(_format_body_line(line) for line in lines)
    parts.append("")

    path.write_text("\n".join(parts), encoding="utf-8")
    logger.info("Saved %s", path)

    # Write meeting-notes.md only if we have content
    has_attendees = notes and notes.get("attendees")
    has_agenda = notes and notes.get("agenda")
    if has_attendees or has_agenda:
        notes_parts = ["## Meeting Notes", ""]
        if has_attendees:
            notes_parts.append("### Attendees")
            notes_parts.extend(notes["attendees"])
            notes_parts.append("")
        if has_agenda:
            notes_parts.append("### Agenda")
            notes_parts.extend(notes["agenda"])
            notes_parts.append("")
        notes_path = path.parent / "meeting-notes.md"
        notes_path.write_text("\n".join(notes_parts), encoding="utf-8")
        logger.info("Saved %s", notes_path)


def process_meetings(meetings: list[Meeting], tracer: object) -> tuple[int, int, list[str]]:
    """
    Scrape transcripts for all meetings.

    Returns (error_count, skipped_count, skipped_urls).
    error_count   — unexpected exceptions (should fail the workflow).
    skipped_count — expected skips, e.g. no transcript available on Zoom.
    skipped_urls  — URLs for all skipped recordings (both kinds).
    """
    errors = 0
    skipped = 0
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

                date_str = meeting.start_date.strftime("%Y-%m-%d")
                with tracer.start_as_current_span("process meeting") as span:
                    span.set_attribute("sig.name", meeting.sig_name)
                    span.set_attribute("meeting.date", date_str)
                    span.set_attribute("meeting.url", meeting.url)

                    notes_url = _ensure_metadata(meeting, out_path)
                    notes = (
                        gdoc.fetch_meeting_notes(notes_url, date_str)
                        if notes_url
                        else {"attendees": [], "agenda": []}
                    )

                    # Fresh context + page per recording to avoid state leakage
                    context = browser.new_context()
                    page = context.new_page()
                    try:
                        lines = scrape_transcript(page, meeting.url)
                        write_transcript(out_path, meeting, lines, notes)
                    except ZoomScrapeError as exc:
                        logger.warning("Skipped — %s", exc)
                        skipped_urls.append(meeting.url)
                        skipped += 1
                        span.set_attribute("meeting.skipped", True)
                        span.set_attribute("meeting.skip.reason", str(exc))
                    except Exception as exc:  # noqa: BLE001
                        logger.exception("Unexpected error for %s", meeting.url)
                        skipped_urls.append(meeting.url)
                        errors += 1
                        span.record_exception(exc)
                        span.set_status(StatusCode.ERROR, str(exc))
                    finally:
                        page.close()
                        context.close()
        finally:
            browser.close()

    return errors, skipped, skipped_urls


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
    matched = sorted(
        {
            m.sig_slug
            for m in meetings
            if any(term.lower() in m.sig_slug.lower() for term in search_terms)
        }
    )

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
        except EOFError, KeyboardInterrupt:
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
        help=("Fetch meetings on or after this date (inclusive). Defaults to 14 days ago."),
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
    tracer = configure_tracer("otel-recordings-refresh")

    since: datetime | None = None
    until: datetime | None = None

    if args.between:
        since = _parse_date(args.between[0], "--between START")
        until = _parse_date(args.between[1], "--between END")
        if since is None or until is None:
            return 1
        if since > until:
            logger.error(
                "--between START (%s) must not be after END (%s)",
                args.between[0],
                args.between[1],
            )
            return 1
    elif args.since:
        since = _parse_date(args.since, "--since")
        if since is None:
            return 1

    with tracer.start_as_current_span("fetch transcripts") as span:
        if args.since:
            span.set_attribute("filter.since_date", args.since)
        if args.between:
            span.set_attribute("filter.since_date", args.between[0])
            span.set_attribute("filter.until_date", args.between[1])
        if args.sig:
            span.set_attribute("filter.sig", args.sig)

        logger.info("Fetching Google Sheet …")
        try:
            rows = fetch_csv()
        except Exception as exc:  # noqa: BLE001
            logger.exception("Failed to fetch sheet")
            span.record_exception(exc)
            span.set_status(StatusCode.ERROR, str(exc))
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
            range_label = "last 14 days"
        logger.info("Found %d meetings with Zoom URLs (%s)", len(meetings), range_label)

        span.set_attribute("meetings.count", len(meetings))

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

        errors, skipped, skipped_urls = process_meetings(meetings, tracer)

        span.set_attribute("meetings.processed", len(meetings) - skipped - errors)
        span.set_attribute("meetings.skipped", skipped)
        span.set_attribute("meetings.errors", errors)

        if skipped_urls:
            print("\nSkipped recordings (no transcript available):")
            for url in skipped_urls:
                print(f"  {url}")

        if skipped:
            logger.warning(
                "%d recording(s) had no transcript — skipped (not a failure)",
                skipped,
            )

        if errors:
            logger.error(
                "Completed with %d unexpected error(s) out of %d meetings",
                errors,
                len(meetings),
            )
            span.set_status(StatusCode.ERROR, f"{errors} unexpected error(s)")
            return 1

        logger.info(
            "Done: %d meeting(s) processed, %d skipped (no transcript)",
            len(meetings) - skipped,
            skipped,
        )
        return 0


if __name__ == "__main__":
    sys.exit(main())
