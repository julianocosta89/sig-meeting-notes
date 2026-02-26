# tests/

Test suite for the project. Run with `make test` or `uv run --group dev pytest tests/ -v`.

## Test files

| File | Covers |
|------|--------|
| `test_build_manifest.py` | `build_site.py` — manifest generation from the content tree |
| `test_community.py` | `scraper/community.py` — community README parsing and metadata bootstrapping |
| `test_gdoc.py` | `scraper/gdoc.py` — Google Doc fetching and meeting-notes extraction |
| `test_generate_summaries.py` | `generate_summaries.py` — AI summary generation pipeline |
| `test_ui.py` | `docs/` web UI — browser-based tests for the single-page app |
