## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Albert Lockett (F5)
- Jake Dern (F5)
- Aaron Marten (Microsoft)
- Tom Tan (Microsoft)
- Drew Relmas (Microsoft)
- Gokhan Uslu (Microsoft)
- Pritish Nahar (Microsoft)

### Agenda
- [Triage]: success, we should update labels as we go–next time
- [Laurent]: Topic demo from #2147
  - Demo covers 3 scenarios where topics can be used to connect independent pipelines
  - Topic is close to a Kafka topic, e.g., to connect N core producers with M core consumers
  - E.g., to support live reconfiguration of a single pipeline
  - E.g., a multi-tenant scenario with per-tenant core allocation, four isolation and resource control
  - E.g., “mixed criticality” sending data to multiple destinations, allowing drop_oldest or drop_newest configuration to determine lag behavior
  - Planning for Quiver integration to support persistent topics.
  - Ack/Nack work is in progress, “ephemeral topics”
- [Laurent]: Embedded web UI discussion
  - A web-ui for summarizing engine performance, has SVG node diagram
  - App is built from scraping prometheus data from the engine, purely observed data
  - Test setup is like the continuous benchmark, but using topics to isolate producer and consumer
- [Jake]: OTAP Spec Draft: [docs: Initial OTAP Spec Draft by JakeDern · Pull Request #2040 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/2040)
- [Gokhan] Extension Support: [https://github.com/open-telemetry/otel-arrow/pull/2141](https://github.com/open-telemetry/otel-arrow/pull/2141)
