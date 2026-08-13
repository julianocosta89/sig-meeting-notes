#!/usr/bin/env python3
"""Send a daily digest email with key topics from new OTel SIG meeting summaries.

Detects new summary.md files via ``git diff`` and sends the digest via the
Resend email API.

Required env vars:
    RESEND_API_KEY  — Resend API key
    PRIVATE_EMAIL   — single visible recipient (``to`` field)
    DIGEST_TO       — comma-separated list of bcc recipient email addresses
"""

from __future__ import annotations

import os
import subprocess
import sys
from datetime import date
from pathlib import Path

import requests

from scraper.otel_setup import StatusCode, configure_tracer
from scraper.transcript_io import (
    MIN_TRANSCRIPT_LINES,
    count_transcript_lines,
    extract_transcript_body,
    read_transcript_body,
)

ROOT = Path(__file__).resolve().parent.parent
SITE_BASE_URL = "https://otelminutes.jcosta.dev/"
LOGO_URL = "https://raw.githubusercontent.com/julianocosta89/sig-meeting-notes/refs/heads/main/docs/OTelMinutes-logo.png"


def _run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    """Run a git command and fail fast on non-zero exit."""
    try:
        return subprocess.run(  # noqa: S603
            ["git", *args],  # noqa: S607
            capture_output=True,
            text=True,
            cwd=ROOT,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        cmd = "git " + " ".join(args)
        stderr = (exc.stderr or "").strip()
        print(f"ERROR: {cmd} failed ({exc.returncode}){': ' + stderr if stderr else ''}")
        raise SystemExit(1) from exc


def get_new_summary_paths() -> list[str]:
    """Return paths of new summary.md files committed by the triggering summarize run.

    When triggered via workflow_run, the workflow downloads the artifact written
    by summarize and passes:
      SUMMARIZE_COMMIT_SHA  — the exact commit that summarize pushed (empty if
                              summarize produced no new commit).
      SUMMARIZE_COMMIT_FOUND — "true" when this is a workflow_run trigger.

    If SUMMARIZE_COMMIT_FOUND is true and SUMMARIZE_COMMIT_SHA is empty,
    summarize pushed nothing this run → return [] immediately.  This correctly
    short-circuits summarize reruns/retries that produce no new commit, even
    though HEAD still differs from the pre-run SHA.

    If SUMMARIZE_COMMIT_SHA is set, diff only that specific commit so that
    reruns of the digest workflow always see the exact same file set.

    When SUMMARIZE_COMMIT_FOUND is false (workflow_dispatch / local runs), fall
    back to HEAD~1 so manual testing always proceeds to the diff.
    """
    commit_sha = os.environ.get("SUMMARIZE_COMMIT_SHA", "").strip()
    commit_found = os.environ.get("SUMMARIZE_COMMIT_FOUND", "false").lower() == "true"

    if commit_found:
        if not commit_sha:
            # Summarize ran but pushed no new commit → nothing to digest
            return []
        result = _run_git(
            ["diff", "--name-only", f"{commit_sha}~1", commit_sha, "--", "docs/content"]
        )
    else:
        # workflow_dispatch or local run → diff the last commit
        result = _run_git(["diff", "--name-only", "HEAD~1", "HEAD", "--", "docs/content"])
    return [line for line in result.stdout.strip().splitlines() if line.endswith("/summary.md")]


def parse_summary_info(path: str, commit_sha: str = "") -> dict[str, str]:
    """Extract slug, date, and content from a summary path.

    When commit_sha is provided, content is read directly from that commit via
    ``git show`` so the snapshot always matches the diff that identified the file,
    regardless of any subsequent commits on the branch.
    """
    # path looks like docs/content/{slug}/{date}/summary.md
    parts = Path(path).parts
    slug = parts[-3]
    meeting_date = parts[-2]
    if commit_sha:
        result = _run_git(["show", f"{commit_sha}:{path}"])
        content = result.stdout
    else:
        full_path = ROOT / path
        content = full_path.read_text(encoding="utf-8") if full_path.exists() else ""
    return {"slug": slug, "date": meeting_date, "content": content}


def parse_summary_sections(content: str) -> dict:
    """Parse a summary.md string into structured sections.

    Returns a dict with keys:
      - highlights: list[str] — bullets from ## Key Topics
      - action_items: list[str] — bullets from ## Action Items
      - participants: str — text from ## Participants
    """
    highlights: list[str] = []
    action_items: list[str] = []
    participants_lines: list[str] = []
    current_section: str | None = None

    for raw_line in content.splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            heading = line[3:].strip().lower()
            if "key topic" in heading:
                current_section = "highlights"
            elif "action item" in heading:
                current_section = "action_items"
            elif "participant" in heading:
                current_section = "participants"
            else:
                current_section = None
            continue
        if not line or current_section is None:
            continue
        if current_section == "highlights":
            highlights.append(line.lstrip("- ").strip() if line.startswith("- ") else line)
        elif current_section == "action_items":
            action_items.append(line.lstrip("- ").strip() if line.startswith("- ") else line)
        elif current_section == "participants":
            participants_lines.append(line)

    return {
        "highlights": highlights,
        "action_items": action_items,
        "participants": " ".join(participants_lines),
    }


def build_deep_link(slug: str, meeting_date: str) -> str:
    """Build a deep-link URL to the meeting on the site."""
    return f"{SITE_BASE_URL}?sig={slug}&date={meeting_date}"


def _render_html(template_vars: dict) -> str:  # pragma: no cover
    """Load and render the Jinja2 HTML email template with autoescaping enabled."""
    from jinja2 import (  # noqa: PLC0415 — deferred to avoid import error without summarize group
        Environment,
        FileSystemLoader,
    )

    template_dir = Path(__file__).resolve().parent
    env = Environment(loader=FileSystemLoader(str(template_dir)), autoescape=True)
    template = env.get_template("digest_template.html")
    return template.render(**template_vars)


def build_email(
    summaries: list[dict[str, str]], today: str, count: int
) -> dict[str, str]:
    """Build subject, HTML body, and plain-text body for the digest email."""
    subject = f"OTel SIG Daily Digest — {today} ({count} meetings)"

    # Build meetings list with highlights and links
    meetings = []
    for s in summaries:
        link = build_deep_link(s["slug"], s["date"])
        sections = parse_summary_sections(s["content"])
        meetings.append(
            {
                "slug": s["slug"],
                "date": s["date"],
                "content": s["content"],
                "link": link,
                "highlights": sections["highlights"],
            }
        )

    # HTML body via Jinja2 template
    html_body = _render_html(
        {
            "date": today,
            "count": count,
            "meetings": meetings,
            "logo_url": LOGO_URL,
        }
    )

    # Plain-text body
    text_parts = ["OTel SIG Daily Digest", "", "---", ""]
    for m in meetings:
        text_parts.append(f"{m['slug']} — {m['date']}")
        text_parts.append(m["content"])
        text_parts.append(f"Read more: {m['link']}")
        text_parts.append("")

    text_body = "\n".join(text_parts)

    return {"subject": subject, "html": html_body, "text": text_body}


def send_email(
    api_key: str,
    to_address: str,
    bcc: list[str],
    email: dict[str, str],
) -> None:
    """POST the email to the Resend API.

    ``to_address`` is the single visible recipient; ``bcc`` is the list of
    blind-copied recipients (omitted from the payload when empty).
    """
    payload: dict[str, object] = {
        "from": "digest@otelminutes.jcosta.dev",
        "to": [to_address],
        "subject": email["subject"],
        "html": email["html"],
        "text": email["text"],
    }
    if bcc:
        payload["bcc"] = bcc
    resp = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {api_key}"},
        json=payload,
        timeout=30,
    )
    if resp.status_code not in (200, 201):
        print(f"ERROR: Resend API returned {resp.status_code}: {resp.text}")
        sys.exit(1)


def _is_trivial_transcript(summary_path: str, commit_sha: str = "") -> bool:
    """Check if the transcript for a summary path has too few lines.

    When commit_sha is provided, reads the transcript from that commit snapshot
    so the trivial check is evaluated against the same revision as the summaries
    being digested (consistent with parse_summary_info).
    """
    transcript_git_path = str(Path(summary_path).parent / "transcript.md")
    if commit_sha:
        try:
            result = _run_git(["show", f"{commit_sha}:{transcript_git_path}"])
        except SystemExit:
            return False
        body = extract_transcript_body(result.stdout)
    else:
        transcript_path = ROOT / transcript_git_path
        if not transcript_path.exists():
            return False
        body = read_transcript_body(transcript_path)
    return count_transcript_lines(body) < MIN_TRANSCRIPT_LINES


def main() -> None:
    tracer = configure_tracer("otel-recordings-digest")

    summary_paths = get_new_summary_paths()
    if not summary_paths:
        print("No new summaries, skipping.")
        sys.exit(0)

    private_email = os.environ.get("PRIVATE_EMAIL", "").strip()
    if not private_email:
        print("PRIVATE_EMAIL not set, skipping.")
        sys.exit(0)

    digest_to = os.environ.get("DIGEST_TO", "").strip()
    if not digest_to:
        print("DIGEST_TO not set, skipping.")
        sys.exit(0)

    bcc_recipients = [r.strip() for r in digest_to.split(",") if r.strip()]
    if not bcc_recipients:
        print("DIGEST_TO contains no valid addresses, skipping.")
        sys.exit(0)

    resend_key = os.environ.get("RESEND_API_KEY", "").strip()
    if not resend_key:
        print("ERROR: RESEND_API_KEY not set")
        sys.exit(1)

    commit_sha = os.environ.get("SUMMARIZE_COMMIT_SHA", "").strip()

    # Filter out trivial meetings before building summaries
    non_trivial_paths = [p for p in summary_paths if not _is_trivial_transcript(p, commit_sha)]
    if not non_trivial_paths:
        print("No non-trivial summaries, skipping.")
        sys.exit(0)

    summaries = [parse_summary_info(p, commit_sha) for p in non_trivial_paths]

    with tracer.start_as_current_span("send digest") as span:
        span.set_attribute("digest.summary.count", len(summaries))
        span.set_attribute("digest.recipient.count", 1 + len(bcc_recipients))
        try:
            today = date.today().isoformat()
            email = build_email(summaries, today, len(summaries))
            send_email(resend_key, private_email, bcc_recipients, email)
        except Exception as exc:  # noqa: BLE001
            span.record_exception(exc)
            span.set_status(StatusCode.ERROR, str(exc))
            raise

    print(f"Digest sent with {len(summaries)} meetings included.")


if __name__ == "__main__":  # pragma: no cover
    main()
