## Key Topics
- Discussion on language injectability and the challenges of auto-injecting OpenTelemetry in Ruby, particularly with gRPC dependencies.
- Progress on logs and metrics signals, with ongoing development and milestones for spec compliance.
- Exploration of the potential benefits of using hand-rolled proto instead of gRPC to avoid dependency conflicts and improve performance.
- The need for better tooling and support for instrumentation in Ruby, including the possibility of integrating C++ dependencies.
- Review of a proposed change to improve re-entry behavior in spans, which is related to trace stability.

## Action Items
- Robb to review the proposed change regarding mutex behavior and its impact on trace stability.
- Xuan to share PRs for metrics in Slack when ready for review.
- Ted to follow up on the spec issue regarding bundling criteria for language implementations.

## Participants
Robb Kidd, Xuan Cao, Ted Young
