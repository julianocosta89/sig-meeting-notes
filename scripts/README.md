# scripts/

Utility scripts for one-off or maintenance operations. Not part of the regular pipeline.

## Files

| Script | Purpose |
|--------|---------|
| `backfill_meeting_notes.py` | Backfills `meeting-notes.md` for transcripts that are missing them. Reads each SIG's `metadata.md` for the Google Doc URL, fetches attendees and agenda, and writes the file. Supports `--execute` (default is dry run), `--force` (overwrite existing), and `--sig` (filter by slug substring). |
