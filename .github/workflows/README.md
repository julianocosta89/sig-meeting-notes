# .github/workflows/

CI/CD workflows that automate transcript fetching, summarisation, testing, and deployment.

## Workflows

| File | Trigger | Purpose |
|------|---------|---------|
| `refresh.yml` | Weekdays 06:00 UTC / manual | Fetches new Zoom transcripts, rebuilds `manifest.json`, and commits to `main` |
| `summarize.yml` | After `refresh.yml` completes / manual | Generates AI summaries (requires `OPENAI_API_KEY` secret), rebuilds manifest, and commits |
| `pages.yml` | Push to `main` (docs/ changes) or after refresh/summarize | Deploys the `docs/` directory to GitHub Pages |
| `test.yml` | Every PR and push to `main` | Runs the full test suite with pytest |

## Pipeline flow

```
refresh.yml  ──►  summarize.yml  ──►  pages.yml
                                         ▲
push to main (docs/) ───────────────────┘
```
