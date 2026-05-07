## Key Topics
- Discussion on the batching and partitioning of data in the OpenTelemetry Collector, including the implications of splitting by instrumentation scope and metadata keys.
- The need for a clear interface for entities in the configuration to avoid breaking changes and improve usability.
- Review of ongoing issues related to configuration changes, particularly around the stability phase and the impact of changes on existing configurations.
- The potential for harmonizing configuration between HTTP and gRPC to improve consistency and security.
- The challenges faced with merging PRs and the importance of maintaining clear communication among maintainers regarding readiness for merging.

## Action Items
- Dmitrii Anoshin to draft an issue regarding the suggested interface for entities before declaring stability.
- Andrew Wilkins to prepare a more detailed proposal for the next meeting regarding partitioning and metadata handling.
- Antoine to label the PR related to config changes as a release blocker for tracking purposes.
- All participants to review ongoing PRs and issues, particularly those affecting the upcoming release.

## Participants
Dmitrii Anoshin, Andrew Wilkins, Antoine Toulme
