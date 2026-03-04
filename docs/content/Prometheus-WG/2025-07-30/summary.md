## Key Topics
- Discussion on stabilizing the OpenTelemetry collector before the release of version 1.0.
- Importance of maintaining consistent metrics emitted by the collector to avoid breaking changes.
- Challenges with metric name changes and the need for a testing platform to ensure stability.
- Differentiation between OpenTelemetry metrics and Prometheus translation metrics.
- Proposed solutions for automation and end-to-end testing to ensure metric consistency.

## Action Items
- Develop a testing platform to assert that metric names do not change with new PRs.
- Explore automation solutions to help maintain metric stability across components.
- Consider creating unit tests to cover the translation of metrics to Prometheus format.

## Participants
Juraj Michalek, krajo Krajcsovits, Arthur Silva Sens, Owen Williams, Jonathan (jojo)
