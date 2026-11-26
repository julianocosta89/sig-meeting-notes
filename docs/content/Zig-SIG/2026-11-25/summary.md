## Key Topics
- **Multiple metric readers bug:** Francesco opened an issue on independent aggregation for multiple metric readers. Readers sharing a meter provider currently consume each other's data because aggregation output is chained rather than fanned out. This is added to the alpha milestone, and a blocked PR awaits review.
- **Alpha release scope:** The group debated whether to include development-stage features in the alpha. They agreed to target stable features and conformance, with the alpha needing to be a working SDK, not necessarily feature-complete. Issue 195 (a breaking API inconsistency) was discussed as a candidate for inclusion.
- **Conformance and Giovanni's work:** Giovanni has been working on the stable-spec conformance table and will open issues for missing items. He plans to be more active this month despite PTO.
- **gRPC and other modules:** Francesco reported successfully using the gRPC exporter in a production service. Documentation comes last, and the alpha will release the other modules (semconv, proto) together.

## Action Items
- Giovanni: Review Francesco's blocked PR on independent aggregation for multiple metric readers.
- Giovanni: Open missing conformance issues for stable features.
- Antoine: Finalize which issues go into the alpha milestone, including issue 195, and add them as needed.
- Francesco: Create follow-up PRs for the metrics aggregation fix after the blocking PR merges.
- Francesco: Handle the semconv configuration work for the alpha.

## Participants
Francesco Gualazzi, Antoine Gagniere, Giovanni
