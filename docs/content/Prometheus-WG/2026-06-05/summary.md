## Key Topics
- Discussion on issues with the Prometheus Remote Write Exporter, specifically regarding metadata loss during batching.
- Proposal to replace the existing remote write queue with the Exporter Helper to improve functionality.
- Need for guaranteed order delivery in the Exporter Helper and the potential for a feature gate for testing.
- Action items related to opening issues for in-order support and landing existing PRs for metadata keys.

## Action Items
- Open an issue in the core repository requesting in-order support for the Exporter Helper.
- Land the PR for supporting metadata keys in the existing remote write queue.
- Explore the implementation of a feature gate for the Exporter Helper.

## Participants
Arve Knudsen, David Ashpole, Andreas Gkizas, Arthur Silva Sens, Himanshu Singh
