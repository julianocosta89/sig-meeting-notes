## Key Topics
- Discussion on consolidating the trace SDK into a single version for browsers and nodes, targeting a major release by the end of June.
- Proposal to remove span events in favor of using log correlation for better instrumentation.
- Concerns about maintaining backward compatibility for existing instrumentations and the implications of breaking changes.
- Exploration of integrating resource timing with fetch and XHR instrumentation to enhance data collection.
- Need for a clear distinction between browser SDK and the existing OpenTelemetry specifications due to unique challenges in the browser environment.

## Action Items
- David to prepare a PR for the proposed changes and discuss implementation details with the team.
- Team to document design decisions and deviations from the OpenTelemetry spec for clarity and future reference.
- Santosh and others to explore ways to encourage migration to the new SDK by highlighting its benefits.

## Participants
Jared Freeze, Joaquín Díaz, David Luna Bistuer, Martin Kuba, Santosh, Ted Young
