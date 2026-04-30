# docs/

Static site served via GitHub Pages at [otelminutes.jcosta.dev](https://otelminutes.jcosta.dev/).

## Files

| File | Purpose |
|------|---------|
| `index.html` | Single-page app shell — sidebar navigation, search, and tabbed meeting view |
| `app.js` | Client-side logic — loads `manifest.json`, renders SIG lists, handles search and URL deep-linking |
| `style.css` | Styles and theming (light/dark mode) |
| `manifest.json` | Auto-generated JSON index of all SIGs and meetings, including `participants` extracted from AI summaries. Built by `build_site.py` |
| `speakers.json` | Auto-generated cross-reference index mapping speaker names to all meetings they attended. Built by `build_site.py` |
| `meetings.jsonl` | Auto-generated JSONL bulk export — one meeting per line with full summary and meeting-notes text. Ideal for RAG indexing and offline analysis. Built by `build_site.py` |
| `favicon.svg` | Site favicon |
| `llms.txt` | Machine-readable site description for LLM agents |
| `llms-full.txt` | Extended LLM reference with full schema docs, query walkthroughs, and example content |
| `robots.txt` | Search engine directives |
| `.gitkeep` | Ensures the directory is tracked even when empty |

## Subdirectories

| Directory | Contents |
|-----------|----------|
| `content/` | All SIG meeting transcripts, notes, and summaries — see [`content/README.md`](content/README.md) |
