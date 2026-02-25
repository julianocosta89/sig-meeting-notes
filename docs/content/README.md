# docs/content/

Single source of truth for all SIG meeting content. This directory is auto-generated — do not manually edit files here.

## Structure

```
content/
  {SIG-Slug}/                  # One directory per SIG (e.g. Collector-SIG, Go-SIG)
    metadata.md                # Stable SIG metadata (Meeting Notes URL, Repository URL)
    {YYYY-MM-DD}/              # One directory per meeting date
      transcript.md            # Zoom recording transcript with header metadata
      meeting-notes.md         # Attendees and agenda (optional, from Google Docs)
      summary.md               # AI-generated summary (optional, from gpt-4o-mini)
```

## How content arrives

1. **`main.py`** writes `transcript.md` (and optionally `meeting-notes.md`) during the fetch stage
2. **`generate_summaries.py`** adds `summary.md` files for meetings that have transcripts but no summary yet
3. **`build_site.py`** reads this tree to produce `manifest.json` for the web UI

## Conventions

- **SIG slugs** are derived from the SIG name by stripping special characters and replacing spaces with hyphens. Some slugs are further canonicalised in `scraper/sheet.py` (e.g. `OpenTelemetry-CC-SIG` → `CC-SIG`).
- **Already-downloaded** transcripts are skipped on subsequent runs — the presence of `transcript.md` is the deduplication signal.
- **metadata.md** is a simple key-value file (`SIG:`, `Meeting Notes:`, `Repository:`).

## SIGs

<!-- This list is manually maintained. Add new entries when new SIGs appear. -->

`Agent-Management-WG` ·
`Android-SIG` ·
`Arrow-SIG` ·
`Browser-SIG` ·
`CC-SIG` ·
`CICD-SemConv-SIG` ·
`Client-Instrumentation-SIG` ·
`Collector-SIG` ·
`Communications-SIG` ·
`Community-Demo-App-SIG` ·
`Configuration-WG` ·
`Contributor-Experience-SIG` ·
`Developer-Experience-SIG-Meeting` ·
`eBPF-instrumentation` ·
`End-User-SIG` ·
`End-User-SIG-OTel-Blueprints` ·
`Entities-SIG` ·
`Event-WG` ·
`FAAS-WG` ·
`Go-Auto-Instrumentation-SIG` ·
`Go-Compile-Time-Instrumentation-SIG` ·
`Go-SIG` ·
`Governance-Committee` ·
`ja-JA-Localization-SIG-Communications` ·
`Java-Declarative-Configuration` ·
`Java-SIG` ·
`JavaScript-SIG` ·
`K8s-Semantic-Convention-SIG` ·
`Kotlin-SIG` ·
`Kubernetes-Operator-SIG` ·
`LLM-Semantic-Convention-WG` ·
`NET-Auto-Instr-SIG` ·
`NET-SIG` ·
`OpenTelemetry-on-Mainframes-Weekly-Meeting` ·
`PHP-SIG` ·
`Profiling-WG` ·
`Project-Tooling-SIG` ·
`Prometheus-WG` ·
`Python-SIG` ·
`RPC-Sem-Conv-Stability-SIG` ·
`Ruby-SIG` ·
`Rust-SIG` ·
`Sampling-SIG` ·
`Security-Governance-SIG` ·
`Semantic-Convention-SIG` ·
`Semantic-Convention-Tooling` ·
`Service-and-Deployment-SemConv` ·
`SIG-Injector` ·
`Specification-SIG` ·
`Swift-SIG` ·
`System-Sem-Conv-Stability-WG` ·
`Technical-Committee`
