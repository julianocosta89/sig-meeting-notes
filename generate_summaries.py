#!/usr/bin/env python3
"""
Generate AI summaries for OTel SIG meeting transcripts.

Walks docs/content/, calls OpenAI gpt-4o-mini for each transcript
that doesn't already have a summary, and writes the result to
docs/content/{slug}/{date}/summary.md.
"""

from __future__ import annotations

import argparse
import os
import re
import time
from datetime import date, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

from scraper.transcript_io import MIN_TRANSCRIPT_LINES, SEPARATOR, count_transcript_lines, parse_header

_TRANSCRIPT_SECTION_RE = re.compile(r"^## Zoom Recording Transcript\s*$", re.MULTILINE)

if TYPE_CHECKING:
    from openai import OpenAI

ROOT = Path(__file__).parent
DOCS_TRANSCRIPTS_DIR = ROOT / "docs" / "content"

MAX_TRANSCRIPT_CHARS = 12_000
_API_RATE_LIMIT_S = 1


def read_transcript_body(path: Path) -> str:
    """Read a transcript and return only the Zoom Recording Transcript section.

    Finds the '## Zoom Recording Transcript' heading and returns the content
    that follows, keeping any Meeting Notes out of the AI summary context.

    Falls back to all content after the separator for legacy plain-text files.
    Truncates to MAX_TRANSCRIPT_CHARS to stay within token limits.
    """
    text = path.read_text(encoding="utf-8")
    sep_idx = text.find(SEPARATOR)
    if sep_idx == -1:
        return ""
    body = text[sep_idx + len(SEPARATOR) :]

    m = _TRANSCRIPT_SECTION_RE.search(body)
    if m:
        body = body[m.end() :].lstrip("\n")
    else:
        body = body.lstrip("\n")

    if len(body) > MAX_TRANSCRIPT_CHARS:
        body = body[:MAX_TRANSCRIPT_CHARS]
    return body


def generate_summary(
    client: OpenAI,
    sig_name: str,
    date: str,
    duration: str,
    source_url: str,
    transcript_body: str,
) -> str:
    """Call OpenAI to generate a summary of the transcript."""
    prompt = (
        f"Summarize this OpenTelemetry {sig_name} meeting transcript from {date} "
        f"({duration} minutes). Format your response EXACTLY as Markdown with these sections:\n\n"
        "## Key Topics\n- ...\n\n"
        "## Action Items\n- ...\n\n"
        "## Participants\nName1, Name2, ...\n\n"
        "Be concise. List 3-5 key topics and any action items mentioned."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You summarize meeting transcripts concisely."},
            {"role": "user", "content": f"{prompt}\n\n---\n\n{transcript_body}"},
        ],
        temperature=0.3,
        max_tokens=1024,
    )
    return response.choices[0].message.content


def process_transcripts(
    client: OpenAI,
    transcripts_dir: Path = DOCS_TRANSCRIPTS_DIR,
    since: date | None = None,
    until: date | None = None,
) -> tuple[int, int]:
    """Process transcripts in the given date range and generate missing summaries.

    When neither ``since`` nor ``until`` is provided, defaults to the last 2 weeks.
    Returns (generated_count, skipped_count).
    """
    generated = 0
    skipped = 0

    if since is None and until is None:
        since = date.today() - timedelta(weeks=2)

    for txt_path in sorted(transcripts_dir.glob("*/*/transcript.md")):
        slug = txt_path.parent.parent.name
        date_str = txt_path.parent.name

        try:
            meeting_date = date.fromisoformat(date_str)
        except ValueError:
            continue
        if since is not None and meeting_date < since:
            skipped += 1
            continue
        if until is not None and meeting_date > until:
            skipped += 1
            continue

        summary_path = txt_path.parent / "summary.md"
        if summary_path.exists():
            skipped += 1
            continue

        header = parse_header(txt_path)
        if header is None:
            print(f"  WARNING: skipping {txt_path} (unparseable header)")
            continue

        body = read_transcript_body(txt_path)
        if not body.strip():
            print(f"  WARNING: skipping {txt_path} (empty transcript body)")
            continue

        line_count = count_transcript_lines(body)
        if line_count < MIN_TRANSCRIPT_LINES:
            print(f"  WARNING: skipping {txt_path} (trivial transcript: {line_count} lines)")
            skipped += 1
            continue

        print(f"  Generating summary for {slug}/{date_str}...")
        summary_text = generate_summary(
            client,
            header["sig_name"],
            header["date"],
            str(header["duration_minutes"]),
            header["source_url"],
            body,
        )

        summary_path.write_text(summary_text + "\n", encoding="utf-8")
        generated += 1

        time.sleep(_API_RATE_LIMIT_S)

    return generated, skipped


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate AI summaries for OTel SIG transcripts.")
    parser.add_argument(
        "--since", metavar="YYYY-MM-DD", help="Only process meetings on or after this date."
    )
    parser.add_argument(
        "--until", metavar="YYYY-MM-DD", help="Only process meetings on or before this date."
    )
    args = parser.parse_args()

    since = date.fromisoformat(args.since) if args.since else None
    until = date.fromisoformat(args.until) if args.until else None

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable is not set")
        raise SystemExit(1)

    from openai import OpenAI  # noqa: PLC0415 — deferred to avoid import error in dev envs

    client = OpenAI(api_key=api_key)
    generated, skipped = process_transcripts(client, since=since, until=until)
    print(f"Generated {generated} summaries, skipped {skipped} existing")


if __name__ == "__main__":
    main()
