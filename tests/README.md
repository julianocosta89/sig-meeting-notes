# tests/

Test suite for the project. Run with `make test` or `uv run --group dev pytest tests/ -v`.

## Test files

| File | Covers |
|------|--------|
| `test_build_manifest.py` | `build_site.py` — manifest generation from the content tree (including `trivial` flag) |
| `test_speaker_boundaries.py` | `scraper/speaker_boundaries.py` — `speaker_name_info`, `is_new_speaker_start`, `should_suppress_embedded_boundary`, and the shared regex patterns |
| `test_transcript.py` | `scraper/transcript.py` — HTML parsing and mid-sentence continuation-line merging |
| `test_transcript_io.py` | `scraper/transcript_io.py` — `count_transcript_lines()` and related helpers |
| `test_community.py` | `scraper/community.py` — community README parsing and metadata bootstrapping |
| `test_gdoc.py` | `scraper/gdoc.py` — Google Doc fetching and meeting-notes extraction |
| `test_generate_summaries.py` | `generate_summaries.py` — AI summary generation pipeline |
| `test_sheet.py` | `scraper/sheet.py` — Zoom URL validation and meeting date filtering |
| `test_send_digest.py` | `scripts/send_digest.py` — daily digest pipeline (git diff, OpenAI narrative, Resend email) |
| `test_fix_merged_transcript_lines.py` | `scripts/fix_merged_transcript_lines.py` — speaker-merge detection and repair |
| `test_main.py` | `main.py` — `_write_meeting_notes` helper and the backfill path in `process_meetings` |
| `test_ui.py` | `docs/` web UI — browser-based tests for the single-page app |
