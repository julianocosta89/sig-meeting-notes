## Key Topics
- Stabilization of the Prometheus receiver and its integration with the OpenTelemetry Collector.
- Discussion on the need for additional metrics to track dropped series and processing performance.
- Proposal to stabilize portions of the Prometheus to OTLP spec while keeping some parts experimental.
- Consideration of build tags for service discovery to reduce memory footprint in the collector.

## Action Items
- Create a GitHub project to track stabilization tasks for the Prometheus receiver.
- Open an issue in the Prometheus repository to discuss including commit duration in scrape duration metrics.
- Investigate the feasibility of using build tags to manage service discovery dependencies in the collector.

## Participants
Arthur Silva Sens, Owen Williams, David Ashpole, krajo Krajcsovits, Adam Bernot, Kyle Eckhart
