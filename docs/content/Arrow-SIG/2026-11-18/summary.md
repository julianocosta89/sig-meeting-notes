## Key Topics
- **Issue triage:** Reviewed open issues, including HTTP header capture for the context propagation RFC, a dashboard gap for OTLP receive rates in the Geneva Exporter, and a shutdown log-flushing bug. Josh flagged that the proposed fix (PR 4375) adds complexity and needs more discussion. The Phase 3 scope was kept open for governance discussions about positioning against the Go Collector.
- **Telemetry policies (OTEP 4738):** Albert and David each have Rust implementations that perform well. Laurent sees a strong fit with the columnar OTAP model. Josh raised a link to Prometheus metric relabel configs, which could become a standalone OTel processor.
- **Entities RFC:** Jake Dern (F5) proposed aligning the data flow engine's entity model with the OTel entity SIG. The RFC separates ambient entities (on the resource) from internal entities (on the scope). It may require OTAP changes for entity refs and scope-level entities.
- **Qualified metric names:** A proposed change to metric naming would break existing users. Laurent asked that it be coordinated with the entity work into a single transition, since few production users exist outside Microsoft and F5.
- **Technical blog and Go exporter scope IDs:** Laurent proposed a repo-hosted technical blog (GitHub Pages) for design and benchmark posts, not news. Albert confirmed that the Go exporter's scope-ID deduplication was an intentional, optional optimization.

## Action Items
- Josh to draft and post a community repo issue on the technical blog proposal, after reviewing it with Laurent.
- Laurent to prototype the blog setup using Markdown and GitHub Actions.
- Albert to review David's policy engine PR.
- Laurent to review PR 4375 and keep the shutdown-log issue open. Josh to discuss how to flush logs at process end.
- Josh to review Jake's entity RFC and follow up with the entity SIG.
- Josh to follow up with Bartek on a standalone metric relabel config processor.
- Governance discussion on Phase 3 scope and positioning against the Go Collector to be scheduled.

## Participants
Laurent Querel, Pierre Mariani, Tatiana Ermolaeva, Drew Relmas, Joshua MacDonald, Jake Dern, Albert Albert, Narine Mossikyan, Bhala Ranganathan
