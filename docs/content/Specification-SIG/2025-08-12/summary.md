## Key Topics
- Conflict in stability guarantees between OpenTelemetry components, specifically regarding configuration changes in the Prometheus exporter and OTEL Collector.
- Discussion on deprecating an existing configuration option in favor of a new one and how to manage backward compatibility.
- Proposal to formalize the handling of deprecated configurations in the declarative config.
- Review of two pending PRs related to proto changes and clarification of breaking changes in the specification.

## Action Items
- Owen Williams and Arthur Silva to explore how to phase out deprecated configuration options and report back.
- Robert Pająk to add a prominent note in the changelog regarding the change in breaking change status for extending attributes.
- Participants to consider how to better communicate spec changes to less engaged users.

## Participants
Armin (Dynatrace), Owen Williams, Artur Silva Sens, Trask Stalnaker, Robert Pająk, Josh Suereth, Tyler Yahn, Reiley Yang
