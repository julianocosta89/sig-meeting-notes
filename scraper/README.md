# scraper/

Python package that implements the three-stage transcript extraction pipeline.

## Modules

| File | Purpose |
|------|---------|
| `sheet.py` | Fetches the public OTel Google Sheet as CSV, parses rows into `Meeting` dataclasses, filters by date range, and normalises SIG slugs via `_CANONICAL_SLUGS` |
| `zoom.py` | Drives a headless Playwright browser to navigate Zoom recording pages, scrolls the virtual-list container to materialise all `<li>` elements, and extracts the transcript HTML |
| `transcript.py` | Parses the extracted `<ul class="transcript-list">` HTML with BeautifulSoup into plain-text `"Speaker Name: utterance"` lines |
| `transcript_io.py` | Shared I/O helpers — `parse_header()`, `parse_reference()`, `SEPARATOR` constant, `MIN_TRANSCRIPT_LINES` threshold, and `count_transcript_lines()` used by `build_site.py` and `generate_summaries.py` |
| `community.py` | One-shot community README parser that bootstraps `metadata.md` files by extracting Google Doc meeting-notes URLs from the OTel community repo |
| `gdoc.py` | Fetches and parses Google Docs to extract attendee lists and agenda items for a given meeting date |
| `__init__.py` | Package marker (empty) |
