## Key Topics
- Discussion on the development of a common library for converting between Prometheus and OpenTelemetry formats.
- Issues with the Prometheus remote write exporter not sending custom buckets for histograms.
- Debate on the handling of info metrics and their naming conventions in relation to OpenTelemetry and Prometheus.
- Consideration of breaking changes and feature gating for metric suffix handling.

## Action Items
- Create an issue regarding the conversion logic for Prometheus and OpenTelemetry to consolidate it in one place.
- Explore the implementation of a feature gate for the suffix handling of info metrics in the Prometheus receiver.

## Participants
krajo, David Ashpole, Arthur Silva Sens, Owen Williams
