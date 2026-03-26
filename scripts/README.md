# scripts/

Utility scripts for one-off or maintenance operations. Not part of the regular pipeline.

## Files

| Script | Purpose |
|--------|---------|
| `backfill_meeting_notes.py` | Backfills `meeting-notes.md` for transcripts that are missing them. Reads each SIG's `metadata.md` for the Google Doc URL, fetches attendees and agenda, and writes the file. Supports `--execute` (default is dry run), `--force` (overwrite existing), and `--sig` (filter by slug substring). |
| `fix_merged_transcript_lines.py` | Detects and fixes transcript lines where multiple speakers were incorrectly merged. This can happen when Zoom's HTML wraps each `<li>` in a container div with no speaker class, causing all lines to appear as continuations — lines from different speakers get joined when the previous utterance ends with `…`. Default is dry-run; pass `--execute` to apply in-place. Supports `--sig` to target a specific SIG. |
| `send_digest.py` | Daily digest: detects new `summary.md` files via `git diff`, filters trivial meetings, asks OpenAI for a meta-summary narrative, and sends an HTML email via the Resend API. Requires `OPENAI_API_KEY`, `RESEND_API_KEY`, and `DIGEST_TO` env vars. |
| `digest_template.html` | Jinja2 HTML email template used by `send_digest.py` (table-based layout, inline CSS, external PNG logo URL). |
