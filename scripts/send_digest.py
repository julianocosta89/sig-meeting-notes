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

import os
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

import requests

from scraper.transcript_io import (
    MIN_TRANSCRIPT_LINES,
    count_transcript_lines,
    extract_transcript_body,
    read_transcript_body,
)

if TYPE_CHECKING:
    from openai import OpenAI


ROOT = Path(__file__).resolve().parent.parent
SITE_BASE_URL = "https://otelminutes.jcosta.dev/"
LOGO_URL = "https://raw.githubusercontent.com/julianocosta89/sig-meeting-notes/refs/heads/main/docs/OTelMinutes-logo.png"
DEFAULT_DIGEST_MODEL = "gpt-5-mini"
DIGEST_MAX_OUTPUT_TOKENS = 2048
DIGEST_RETRY_MAX_OUTPUT_TOKENS = 4096


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


def build_digest_source(summaries: list[dict[str, str]]) -> str:
    """Render only digest-relevant summary sections for the model input."""
    rendered: list[str] = []

    for summary in summaries:
        sections = parse_summary_sections(summary["content"])
        lines = [f"### {summary['slug']} ({summary['date']})"]

        if sections["highlights"]:
            lines.append("Key topics:")
            lines.extend(f"- {item}" for item in sections["highlights"])

        if sections["action_items"]:
            lines.append("Action items:")
            lines.extend(f"- {item}" for item in sections["action_items"])

        if len(lines) == 1:
            lines.append(summary["content"].strip())

        rendered.append("\n".join(lines))

    return "\n\n".join(rendered)


def _get_incomplete_reason(response: object) -> str | None:
    """Extract the incomplete reason from a Responses API object."""
    details = getattr(response, "incomplete_details", None)
    if isinstance(details, dict):
        return details.get("reason")
    if details is not None:
        return getattr(details, "reason", None)
    return None


def _trim_to_complete_sentences(text: str) -> str:
    """Return only the completed sentence prefix from a truncated response."""
    stripped = text.strip()
    if not stripped:
        return ""

    last_sentence_end = max(stripped.rfind("."), stripped.rfind("!"), stripped.rfind("?"))
    if last_sentence_end == -1:
        return ""
    return stripped[: last_sentence_end + 1].strip()


def _request_digest_narrative(client: OpenAI, *, model: str, prompt: str, max_output_tokens: int):
    """Issue a digest generation request to OpenAI."""
    return client.responses.create(
        model=model,
        instructions=(
            "You are an editor writing a concise daily digest for the OpenTelemetry"
            " community. Prefer concrete, neutral prose over hype."
        ),
        input=prompt,
        max_output_tokens=max_output_tokens,
    )


def generate_digest_narrative(client: OpenAI, summaries: list[dict[str, str]]) -> str:
    """Call OpenAI to produce a concise cross-SIG narrative."""
    combined = build_digest_source(summaries)
    model = os.environ.get("OPENAI_DIGEST_MODEL", DEFAULT_DIGEST_MODEL).strip() or (
        DEFAULT_DIGEST_MODEL
    )

    if len(summaries) == 1:
        user_prompt = """Write a 2-3 sentence email-ready digest paragraph
about this OpenTelemetry SIG meeting.

Focus on the most important themes, decisions, or follow-ups.
Do not mention any person's name or attribute anything to a specific individual.
Do not use markdown, bullets, or headings.
Do not mention that you were given summaries.
Do not invent details that are not present in the source material.

Source material:
"""
    else:
        user_prompt = """Write a single 3-4 sentence email-ready digest paragraph
connecting these OpenTelemetry SIG meetings.

Synthesize shared themes, dependencies, and action-oriented work across meetings.
Do not turn the paragraph into a meeting-by-meeting list.
Only mention SIG names when they materially help clarity.
Do not mention any person's name or attribute anything to a specific individual.
Do not use markdown, bullets, or headings.
Do not mention that you were given summaries.
Do not invent details that are not present in the source material.

Source material:
"""
    prompt = f"{user_prompt}\n\n{combined}"
    response = _request_digest_narrative(
        client,
        model=model,
        prompt=prompt,
        max_output_tokens=DIGEST_MAX_OUTPUT_TOKENS,
    )
    if response.status == "incomplete":
        reason = _get_incomplete_reason(response)
        if reason == "max_output_tokens":
            print("WARNING: OpenAI digest response hit max_output_tokens; retrying once.")
            retry_response = _request_digest_narrative(
                client,
                model=model,
                prompt=prompt,
                max_output_tokens=DIGEST_RETRY_MAX_OUTPUT_TOKENS,
            )
            if retry_response.status != "incomplete":
                if not retry_response.output_text:
                    raise ValueError("OpenAI returned no output text")
                return retry_response.output_text.strip()

            retry_reason = _get_incomplete_reason(retry_response)
            if retry_reason == "max_output_tokens":
                salvaged = _trim_to_complete_sentences(retry_response.output_text) or (
                    _trim_to_complete_sentences(response.output_text)
                )
                if salvaged:
                    print(
                        "WARNING: OpenAI digest response remained truncated; using completed"
                        " sentences from the partial output."
                    )
                    return salvaged

            response = retry_response
            reason = retry_reason

        suffix = f": {reason}" if reason else ""
        raise ValueError(f"OpenAI response incomplete{suffix}")
    if not response.output_text:
        raise ValueError("OpenAI returned no output text")
    return response.output_text.strip()


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
    narrative: str, summaries: list[dict[str, str]], today: str, count: int
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
            "narrative": narrative,
            "date": today,
            "count": count,
            "meetings": meetings,
            "logo_url": LOGO_URL,
        }
    )

    # Plain-text body
    text_parts = ["OTel SIG Daily Digest", "", narrative, "", "---", ""]
    for m in meetings:
        text_parts.append(f"{m['slug']} — {m['date']}")
        text_parts.append(m["content"])
        text_parts.append(f"Read more: {m['link']}")
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


def _create_openai_client(api_key: str) -> OpenAI:
    """Create an OpenAI client instance (seam for testing)."""
    from openai import OpenAI as _OpenAI  # noqa: PLC0415  # pragma: no cover

    return _OpenAI(api_key=api_key)  # pragma: no cover


def main() -> None:
    summary_paths = get_new_summary_paths()
    if not summary_paths:
        print("No new summaries, skipping.")
        sys.exit(0)

    digest_to = os.environ.get("DIGEST_TO", "").strip()
    if not digest_to:
        print("DIGEST_TO not set, skipping.")
        sys.exit(0)

    recipients = [r.strip() for r in digest_to.split(",") if r.strip()]
    if not recipients:
        print("DIGEST_TO contains no valid addresses, skipping.")
        sys.exit(0)

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set")
        sys.exit(1)

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

    client = _create_openai_client(api_key)
    narrative = generate_digest_narrative(client, summaries)

    today = date.today().isoformat()
    email = build_email(narrative, summaries, today, len(summaries))
    send_email(resend_key, recipients, email)

    print(f"Digest sent with {len(summaries)} meetings included.")


if __name__ == "__main__":  # pragma: no cover
    main()
