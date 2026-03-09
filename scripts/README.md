# scripts/

Utility scripts for one-off or maintenance operations. Not part of the regular pipeline.

## Files

| Script | Purpose |
|--------|---------|
| `backfill_meeting_notes.py` | Backfills `meeting-notes.md` for transcripts that are missing them. Reads each SIG's `metadata.md` for the Google Doc URL, fetches attendees and agenda, and writes the file. Supports `--execute` (default is dry run), `--force` (overwrite existing), and `--sig` (filter by slug substring). |
| `send_digest.py` | Daily digest: detects new `summary.md` files via `git diff`, asks OpenAI for a meta-summary narrative, and sends an HTML email via the Resend API. Requires `OPENAI_API_KEY`, `RESEND_API_KEY`, and `DIGEST_TO` env vars. |
| `digest_template.html` | Jinja2 HTML email template used by `send_digest.py` (table-based layout, inline CSS, base64 SVG logo). |
