## Key Topics
- Discussion on the Prometheus to OpenTelemetry conversion code and its implementation.
- Issues with the Prometheus remote write exporter converting OpenTelemetry histograms to Prometheus histograms.
- Review of PR regarding info metrics and the handling of suffixes in metric names.
- Updates on Prometheus receiver configurations and feature flags.
- Introduction of sync testing in the OpenTelemetry collector.

## Action Items
- Create an issue for the conversion code to ensure consistency across implementations.
- Address the PR on info metrics to clarify suffix handling and potentially add feature gates.
- Review and finalize the deprecation of certain configurations in the Prometheus receiver.
- Explore the implementation of sync testing in the OpenTelemetry collector.

## Participants
krajo, David Ashpole, Arthur Silva Sens, Owen Williams
