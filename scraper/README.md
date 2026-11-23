# scraper/

Python package that implements the transcript extraction pipeline: discovery (LFX + Google Sheet), Zoom scraping, and transcript parsing.

## Modules

| File | Purpose |
|------|---------|
| `lfx.py` | Primary meeting-discovery source: fetches the LFX platform's public past-meetings API for the `opentelemetry` project and turns records into `Meeting`s, skipping restricted/non-public meetings |
| `sheet.py` | Legacy discovery source: fetches the public OTel Google Sheet as CSV, parses rows into `Meeting` dataclasses, filters by date range, and normalises SIG slugs via `_CANONICAL_SLUGS` (also used for LFX titles) |
| `zoom.py` | Drives a headless Playwright browser to navigate Zoom recording pages, handles both of Zoom's player layouts (newer `data-testid` list and `oldStyle` `ul.transcript-list`), and scrolls the virtual-list container, snapshotting every `.transcript-list-item` at each step |
| `transcript.py` | Parses the collected `.transcript-list-item` HTML with BeautifulSoup into plain-text `"Speaker Name MM:SS utterance"` lines, merging mid-sentence continuation items (no speaker header, previous line not ending in `.`/`?`/`!`) into the previous line; falls back to the legacy `<ul class="transcript-list">` `<li>` layout |
| `speaker_boundaries.py` | Shared speaker-boundary detection helpers used by both `transcript.py` and `scripts/fix_merged_transcript_lines.py` — regex patterns (`SPEAKER_LIKE_RE`, `EMBEDDED_SPEAKER_RE`, `SPEAKER_TS_RE`), the `SpeakerNameInfo` dataclass, and the `is_new_speaker_start` / `should_suppress_embedded_boundary` functions |
| `transcript_io.py` | Shared I/O helpers — `parse_header()`, `parse_reference()`, `SEPARATOR` constant, `MIN_TRANSCRIPT_LINES` threshold, and `count_transcript_lines()` used by `build_site.py` and `generate_summaries.py` |
| `community.py` | One-shot community README parser that bootstraps `metadata.md` files by extracting Google Doc meeting-notes URLs from the OTel community repo |
| `gdoc.py` | Fetches and parses Google Docs to extract attendee lists and agenda items for a given meeting date |
| `__init__.py` | Package marker (empty) |
