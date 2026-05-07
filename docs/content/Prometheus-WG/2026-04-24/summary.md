## Key Topics
- Discussion on self-observability metrics for Prometheus receiver, focusing on how to report dropped data.
- Review of Braden's design document and its implications for the stability of components.
- Need for alignment on error types and definitions in metrics to avoid confusion.
- Ongoing discussions about stabilizing resource attributes and their impact on Prometheus SDK exporters.
- Challenges with the integration of entity attributes and their effect on target info metrics.

## Action Items
- David Ashpole to attend the collector stability meeting on Monday to discuss self-observability metrics.
- Review and finalize the PR for instrumentation scope, ensuring additional approvals.
- Clarify and potentially resolve naming conventions for metrics (e.g., "refused" vs. "rejected").
- Further investigate the impact of entity attributes on Prometheus metrics and address any inconsistencies.

## Participants
Arthur Silva Sens, krajo Krajcsovits, David Ashpole, Owen Williams, Arve Knudsen, Jonathan Santos, Braydon Kains.
