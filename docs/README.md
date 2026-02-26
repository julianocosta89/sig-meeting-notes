# docs/

Static site served via GitHub Pages at [julianocosta89.github.io/sig-meeting-notes](https://julianocosta89.github.io/sig-meeting-notes/).

## Files

| File | Purpose |
|------|---------|
| `index.html` | Single-page app shell — sidebar navigation, search, and tabbed meeting view |
| `app.js` | Client-side logic — loads `manifest.json`, renders SIG lists, handles search and URL deep-linking |
| `style.css` | Styles and theming (light/dark mode) |
| `manifest.json` | Auto-generated JSON index of all SIGs, meeting dates, durations, and content paths. Built by `build_site.py` |
| `favicon.svg` | Site favicon |
| `llms.txt` | Machine-readable site description for LLM crawlers |
| `robots.txt` | Search engine directives |
| `.gitkeep` | Ensures the directory is tracked even when empty |

## Subdirectories

| Directory | Contents |
|-----------|----------|
| `content/` | All SIG meeting transcripts, notes, and summaries — see [`content/README.md`](content/README.md) |
