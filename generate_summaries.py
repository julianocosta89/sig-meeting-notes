#!/usr/bin/env python3
"""
Generate AI summaries for OTel SIG meeting transcripts.

Walks docs/transcripts/, calls OpenAI gpt-4o-mini for each transcript
that doesn't already have a summary, and writes the result to
docs/summaries/{slug}/{date}.md.
"""
from __future__ import annotations

import os
import time
from pathlib import Path

from openai import OpenAI

from scraper.transcript_io import SEPARATOR, parse_header

ROOT = Path(__file__).parent
DOCS_TRANSCRIPTS_DIR = ROOT / "docs" / "transcripts"
SUMMARIES_DIR = ROOT / "docs" / "summaries"

MAX_TRANSCRIPT_CHARS = 12_000
_API_RATE_LIMIT_S = 1


def read_transcript_body(path: Path) -> str:
    """Read a transcript file and return only the body (after the separator line).

    Truncates to MAX_TRANSCRIPT_CHARS to stay within token limits.
    """
    text = path.read_text(encoding="utf-8")
    sep_idx = text.find(SEPARATOR)
    if sep_idx == -1:
        return ""
    body = text[sep_idx + len(SEPARATOR):]
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
        f"({duration} minutes). Format your response EXACTLY as:\n\n"
        f"# {sig_name} — {date}\n\n"
        f"**Duration:** {duration} minutes\n"
        f"**Source:** {source_url}\n\n"
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
    summaries_dir: Path = SUMMARIES_DIR,
) -> tuple[int, int]:
    """Process all transcripts and generate missing summaries.

    Returns (generated_count, skipped_count).
    """
    generated = 0
    skipped = 0

    for txt_path in sorted(transcripts_dir.glob("*/*.txt")):
        slug = txt_path.parent.name
        date_stem = txt_path.stem  # e.g. "2026-02-05"

        summary_path = summaries_dir / slug / f"{date_stem}.md"
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

        print(f"  Generating summary for {slug}/{date_stem}...")
        summary_text = generate_summary(
            client,
            header["sig_name"],
            header["date"],
            str(header["duration_minutes"]),
            header["source_url"],
            body,
        )

        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(summary_text + "\n", encoding="utf-8")
        generated += 1

        time.sleep(_API_RATE_LIMIT_S)

    return generated, skipped


def main() -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable is not set")
        raise SystemExit(1)

    client = OpenAI(api_key=api_key)
    generated, skipped = process_transcripts(client)
    print(f"Generated {generated} summaries, skipped {skipped} existing")


if __name__ == "__main__":
    main()
