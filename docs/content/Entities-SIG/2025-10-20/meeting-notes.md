## Meeting Notes

### Attendees
- Josh Suereth
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- [Daniel Dyla](mailto:dyladan@gmail.com) (Dynatrace)
- Ted Young (Grafana Labs)
- Dmitry Anoshin (Splunk)

### Agenda
- [dmitry] [https://github.com/open-telemetry/opentelemetry-specification/pull/4697](https://github.com/open-telemetry/opentelemetry-specification/pull/4697)
  - Add Entity Type Uniqueness and Attribute Ownership restrictions
  - While working on adding API for managing the Resource Entity references in collector pipelines, I found that it's very complicated to maintain data integrity if we don't explicitly impose the following restrictions on the data model:
- [Florian] [https://github.com/open-telemetry/semantic-conventions/issues/2561](https://github.com/open-telemetry/semantic-conventions/issues/2561)
  - Define semantic conventions for (process/context) labels
- [suereth] Updated OTEP -  [https://github.com/open-telemetry/opentelemetry-specification/pull/4665](https://github.com/open-telemetry/opentelemetry-specification/pull/4665)
  - Two major concerns
    - high cardinality + "close" method on API
    - Do we need an "OpenTelemetry" API that includes all Providers?
