# .github/workflows/

CI/CD workflows that automate transcript fetching, summarisation, testing, and deployment.

## Workflows

| File | Trigger | Purpose |
|------|---------|---------|
| `refresh.yml` | Weekdays 06:00 UTC / manual | Fetches new Zoom transcripts, rebuilds `manifest.json`, and commits to `main` |
| `summarize.yml` | After `refresh.yml` completes / manual | Generates AI summaries with Claude (requires `ANTHROPIC_KEY` secret), rebuilds manifest, and commits |
| `pages.yml` | Push to `main` (docs/ changes) or after refresh/summarize | Deploys the `docs/` directory to GitHub Pages |
| `test.yml` | Every PR and push to `main` / manual | Runs ruff lint + format check, then the full test suite with pytest |
| `upgrade-lockstep.yml` | Mondays 07:00 UTC / manual | Bumps the OpenTelemetry packages together (Dependabot can't, since they pin each other exactly) and opens a PR, then dispatches `test.yml` on it. Needs "Allow GitHub Actions to create and approve pull requests" enabled |

## Pipeline flow

```
refresh.yml  ──►  summarize.yml  ──►  pages.yml
                                         ▲
push to main (docs/) ───────────────────┘
```
