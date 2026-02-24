# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This tool downloads OpenTelemetry SIG meeting transcripts from Zoom recording pages. It reads a public Google Spreadsheet listing all OTel SIG recordings, then uses Playwright to scrape each Zoom recording page and extract the transcript, saving it as a plain-text file organized by SIG name and date.

## Commands

```bash
# Install dependencies and Playwright browser
make install

# Fetch transcripts from the start of the current month
make fetch

# Fetch transcripts since a specific date
make fetch SINCE=2026-02-01

# Fetch transcripts within a date range
make fetch BETWEEN=2026-01-01/2026-02-28

# Fetch a specific SIG only (substring match; prompts if ambiguous)
make fetch SIG=collector
make fetch SINCE=2026-02-01 SIG=go

# Run directly with uv
uv run python main.py --since 2026-02-01
uv run python main.py --between 2026-01-01 2026-02-28
uv run python main.py --sig collector
uv run python main.py --since 2026-02-01 --sig go
```

## Architecture

The pipeline has three stages:

1. **`scraper/sheet.py`** — Fetches the public Google Sheet as CSV (`SHEET_CSV_URL`), parses it into `Meeting` dataclasses, and filters by date range. Column detection is case-insensitive and tries multiple synonyms (e.g., `name`/`sig`/`topic` for the SIG name). `_CANONICAL_SLUGS` normalizes slugs for SIGs that appear under multiple names in the spreadsheet (e.g. `OpenTelemetry-CC-SIG` → `CC-SIG`).

2. **`scraper/zoom.py`** — Uses a Playwright `Page` to navigate to each Zoom recording URL. Handles Zoom's Vue SPA virtual-list rendering by scrolling the `.zm-scrollbar__wrap` container in steps so all transcript `<li>` elements are materialized in the DOM before extraction. Raises `ZoomScrapeError` for known failure modes (password-protected, expired, no transcript).

3. **`scraper/transcript.py`** — Parses the extracted `outerHTML` of `ul.transcript-list` using BeautifulSoup, producing lines in `"Speaker Name: utterance"` format.

**`main.py`** orchestrates the pipeline: fetches all date-range meetings, then runs `_resolve_sig()` when `--sig` is given. Before matching, the filter is looked up in `_SIG_ALIASES` (e.g. `gc` → `governance-committee`, `semconv` → `semantic-convention`/`semconv`/`sem-conv`); unrecognised values are used as-is. If the (expanded) terms match multiple SIG slugs it prints a numbered list and prompts the user to pick one interactively. After disambiguation it filters to the chosen slug, then processes recordings with one fresh Playwright browser context per recording (to avoid session state leakage), skipping already-downloaded transcripts, and writing output to `docs/transcripts/{sig-slug}/YYYY-MM-DD.md`.

## Output Structure

`docs/transcripts/` is the single source of truth — `main.py` writes there directly and `build_site.py` reads from there (no copy step).

```
docs/transcripts/
  {SIG-Slug}/
    metadata.md      # Stable SIG metadata (Meeting Notes URL, Repository URL)
    YYYY-MM-DD.md    # Header + Meeting Notes section + Zoom Recording Transcript
```

Slug is generated from the SIG name by stripping special characters and replacing spaces with hyphens. `_CANONICAL_SLUGS` in `sheet.py` then remaps certain slugs to a canonical form so that SIGs recorded under multiple names in the spreadsheet share one directory:

| Raw slug | Canonical slug |
|----------|---------------|
| `OpenTelemetry-CC-SIG` | `CC-SIG` |

To merge a new SIG, move its existing transcript files into the canonical directory and add an entry to `_CANONICAL_SLUGS`.
