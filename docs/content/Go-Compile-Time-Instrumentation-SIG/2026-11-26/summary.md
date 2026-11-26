## Key Topics
- **Meeting link mix-up:** Calendar invite and docs linked to different Zoom/LFX URLs after the LFX migration. Kemal will try to fix the calendar entry, and the docs link will be corrected.
- **Contrib repo split and versioning:** Instrumentations moved to the new contrib repo, with releases decoupled from the core tool. The group agreed on per-integration Go module versioning via multimod, starting at V0 with a checklist for semantic convention compliance, metrics coverage, and attributes before V1. The registry is still hardcoded in OTel Compile-Time, pending Ecosystem Explorer support.
- **Integration tests and release cadence:** Integration tests will be grouped by instrumentation so PRs run only relevant tests, building on dd-trace-go's optimizations (a recent AST-check change gave up to 10x speedups). Proposed cadence: contrib every 2 to 4 weeks, core tool every 6 weeks, with releases skipped when nothing has changed. Merge queues were approved to prevent CI breakage on main.
- **Injector SIG and upstreaming:** Kemal will join the OTel injector SIG (next Thursday) to explore making Compile-Time the default Go compiler for auto-instrumentation packages. Huxing will draft a plan for moving Alibaba's integrations upstream, with some possibly staying in their own repo.
- **Maintainer Summit and KubeCon Barcelona:** The group will submit a project meeting proposal and explore talk submissions, including a possible Compile-Time talk from Azhar.

## Action Items
- Kemal Akkoyun: Fix the calendar meeting link so it matches the docs (Dario to update docs).
- Azhar Momin: Create issues for the instrumentation compliance checklist, README/signal and config doc generation, and Ecosystem Explorer registry support. Push pending PRs next week.
- Azhar Momin: Look into KubeCon/Maintainer Summit submission options and scholarships.
- Kemal Akkoyun: Review dd-trace-go's CI setup for applicable changes, fix instrumentation JSON sorting, and push updates.
- Kemal Akkoyun: Attend the injector SIG meeting next Thursday and post an update in Slack.
- Huxing Zhang: Draft a plan for upstreaming Alibaba integrations to OTel contrib.
- Huxing Zhang: Submit a project meeting proposal for Maintainer Summit Europe.
- Enable merge queues on the contrib repo (no objections raised).

## Participants
Kemal Akkoyun, Huxing Zhang, Dario Castañé, Azhar Momin, Xabier Martínez
