## Key Topics
- Discussion on the relationship between identifying labels for Prometheus and OpenTelemetry entities.
- The need for consistency in identifying attributes across metrics, logs, and traces.
- Proposal for a layer of identity in OpenTelemetry resources to resolve multiple unique identities.
- Introduction of native metadata in Prometheus to improve metadata representation and correlation.
- Exploration of how Prometheus can effectively handle multiple sets of identifying attributes.

## Action Items
- Investigate the implementation of native metadata in Prometheus for better representation of resource attributes.
- Explore the possibility of Prometheus supporting entities and their integration with existing metrics.
- Dmitrii to submit a revised proposal regarding the relationship between parent and child attributes in entity events.

## Participants
krajo, Arve Knudsen, Josh Suereth, Dmitrii Anoshin
