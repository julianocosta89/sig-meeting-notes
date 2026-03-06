#!/usr/bin/env python3
"""Send a daily digest email summarising new OTel SIG meeting summaries.

Detects new summary.md files via ``git diff``, asks OpenAI to produce a
meta-summary narrative, and sends the digest via the Resend email API.

Required env vars:
    OPENAI_API_KEY  — OpenAI API key
    RESEND_API_KEY  — Resend API key
    DIGEST_TO       — comma-separated list of recipient email addresses
"""
from __future__ import annotations

import base64
import os
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

import requests
from jinja2 import Template

if TYPE_CHECKING:
    from openai import OpenAI


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "docs" / "content"
SITE_BASE_URL = "https://otelminutes.jcosta.dev/"


def get_new_summary_paths() -> list[str]:
    """Return paths of new summary.md files from the last commit."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD", "--", "docs/content"],
        capture_output=True, text=True, cwd=ROOT,
    )
    return [
        line for line in result.stdout.strip().splitlines()
        if line.endswith("/summary.md")
    ]


def parse_summary_info(path: str) -> dict[str, str]:
    """Extract slug, date, and content from a summary path."""
    # path looks like docs/content/{slug}/{date}/summary.md
    parts = Path(path).parts
    slug = parts[-3]
    meeting_date = parts[-2]
    full_path = ROOT / path
    content = full_path.read_text(encoding="utf-8") if full_path.exists() else ""
    return {"slug": slug, "date": meeting_date, "content": content}


def generate_digest_narrative(client: OpenAI, summaries: list[dict[str, str]]) -> str:
    """Call OpenAI to produce a concise meta-summary narrative."""
    combined = "\n\n".join(
        f"### {s['slug']} ({s['date']})\n{s['content']}" for s in summaries
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an editor writing a concise daily digest for the OpenTelemetry community.",
            },
            {
                "role": "user",
                "content": (
                    "Write a concise digest of today's OpenTelemetry SIG meetings "
                    f"based on these summaries:\n\n{combined}"
                ),
            },
        ],
        temperature=0.3,
        max_tokens=1024,
    )
    return response.choices[0].message.content


def build_deep_link(slug: str, meeting_date: str) -> str:
    """Build a deep-link URL to the meeting on the site."""
    return f"{SITE_BASE_URL}?sig={slug}&date={meeting_date}"


def _load_logo_b64() -> str:
    """Read the SVG logo and return a base64 data URI string."""
    logo_path = ROOT / "docs" / "OTelMinutes-logo.svg"
    svg_bytes = logo_path.read_bytes()
    encoded = base64.b64encode(svg_bytes).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def _make_excerpt(content: str) -> str:
    """Extract a plain-text excerpt from summary content."""
    lines = content.strip().splitlines()
    # Skip markdown headings, take the first real content
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("##"):
            return stripped[:300]
    return content[:300].strip()


def _render_html(template_vars: dict) -> str:
    """Load and render the Jinja2 HTML email template."""
    template_path = Path(__file__).resolve().parent / "digest_template.html"
    template_src = template_path.read_text(encoding="utf-8")
    template = Template(template_src)
    return template.render(**template_vars)


def build_email(
    narrative: str, summaries: list[dict[str, str]], today: str, count: int
) -> dict[str, str]:
    """Build subject, HTML body, and plain-text body for the digest email."""
    subject = f"OTel SIG Daily Digest — {today} ({count} meetings)"

    # Build meetings list with excerpts and links
    meetings = []
    for s in summaries:
        link = build_deep_link(s["slug"], s["date"])
        meetings.append({
            "slug": s["slug"],
            "date": s["date"],
            "content": s["content"],
            "link": link,
            "excerpt": _make_excerpt(s["content"]),
        })

    # HTML body via Jinja2 template
    html_body = _render_html({
        "narrative": narrative,
        "date": today,
        "count": count,
        "meetings": meetings,
        "logo_b64": _load_logo_b64(),
    })

    # Plain-text body
    text_parts = ["OTel SIG Daily Digest", "", narrative, "", "---", ""]
    for s in summaries:
        link = build_deep_link(s["slug"], s["date"])
        text_parts.append(f"{s['slug']} — {s['date']}")
        text_parts.append(s["content"])
        text_parts.append(f"Read more: {link}")
        text_parts.append("")

    text_body = "\n".join(text_parts)

    return {"subject": subject, "html": html_body, "text": text_body}


def send_email(api_key: str, recipients: list[str], email: dict[str, str]) -> None:
    """POST the email to the Resend API."""
    resp = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "from": "digest@otelminutes.jcosta.dev",
            "to": recipients,
            "subject": email["subject"],
            "html": email["html"],
            "text": email["text"],
        },
        timeout=30,
    )
    if resp.status_code not in (200, 201):
        print(f"ERROR: Resend API returned {resp.status_code}: {resp.text}")
        sys.exit(1)


def _create_openai_client(cls: type, api_key: str) -> OpenAI:
    """Create an OpenAI client instance (seam for testing)."""
    return cls(api_key=api_key)


def main() -> None:
    summary_paths = get_new_summary_paths()
    if not summary_paths:
        print("No new summaries, skipping.")
        sys.exit(0)

    digest_to = os.environ.get("DIGEST_TO", "").strip()
    if not digest_to:
        print("DIGEST_TO not set, skipping.")
        sys.exit(0)

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set")
        sys.exit(1)

    resend_key = os.environ.get("RESEND_API_KEY", "").strip()
    if not resend_key:
        print("ERROR: RESEND_API_KEY not set")
        sys.exit(1)

    summaries = [parse_summary_info(p) for p in summary_paths]

    from openai import OpenAI as _OpenAI  # noqa: PLC0415

    client = _create_openai_client(_OpenAI, api_key)
    narrative = generate_digest_narrative(client, summaries)

    today = date.today().isoformat()
    recipients = [r.strip() for r in digest_to.split(",")]
    email = build_email(narrative, summaries, today, len(summaries))
    send_email(resend_key, recipients, email)

    print(f"Digest sent with {len(summaries)} meetings included.")


if __name__ == "__main__":
    main()
