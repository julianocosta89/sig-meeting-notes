## Key Topics
- **Target info join in the remote write receiver:** The spec PR was resolved and merged. Attaching target info to requests is now MUST within the same request and MAY across requests, which covers cache-based lookups without mandating a specific implementation.
- **Pending spec PRs:** The exponential histogram to Prometheus PR was held off because it touches the same changelog as the merged PR. A PR specifying the Prometheus exporter bridge needs one more approval. A PR on conflict handling (keeping the most recent value by timestamp instead of joining with commas) remains a draft until the change lands upstream in the Collector.
- **Relabel configs for the remote write exporter:** Michael Burt proposed supporting relabel configs. The group leaned toward implementing them as an OTel Collector processor, not in the exporter, but noted that a processor may be slower because it converts between OTLP and the Prometheus data model. Michael will build a prototype and design proposal so performance can be measured. Arthur Silva Sens offered to help, and mentioned a possible refactor of Prometheus remote write code for reuse.
- **PromQL receiver idea:** The group was skeptical. Concerns included performance risk to backends, the mismatch between PromQL and a transport protocol, and the overlap with recording rules. The conclusion was that it probably isn't worth building without better use-case understanding.
- **Resource attribute proposals:** The group agreed to open competing draft PRs, one per proposal, so they can be evaluated. Arve Knudsen will sync with krajo on Monday. The goal is draft PRs for the two main proposals by the next SIG meeting. Arthur is out for a week after surgery, and the next meeting falls in the US Thanksgiving holiday week.

## Action Items
- Michael Burt: Build a prototype of the relabel processor and write a design proposal in the GitHub issue.
- David Ashpole: Measure the prototype's performance against alternatives. Verify whether Prometheus remote write internals can be reused. Open a draft PR for a resource attribute proposal.
- Arve Knudsen: Check in with krajo on Monday about the resource attribute proposal PRs and sync with the WG.
- krajo: Help spread the resource attribute proposal PRs across the group. Continue the JavaScript client maintainer work.
- Arthur Silva Sens: Support the relabel processor effort once he returns from leave.
- All: Aim for draft PRs on the two main resource attribute proposals by the next SIG meeting. Get the bridge spec PR a second approval and merge.

## Participants
David Ashpole, krajo, Arthur Silva Sens, Arve Knudsen, Michael Burt
