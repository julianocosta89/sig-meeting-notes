## Meeting Notes

### Attendees
- Jim Porell
- Ruediger Schulze
- Kai Kirsch
- Richard Salac
- Greg Shriver
- Richard Nikula

### Agenda
- Input to [Semantic Conventions roadmap for 2026](https://github.com/open-telemetry/semantic-conventions/issues/3330):
  - What do you expect to ship in 2026?
    - Mainframe user resource/entities and curated list of metrics
      - services: transactions, databases, messaging, APIs, (HTTP)
      - Infrastructure: CPU (by host, and services), JVM
      - Metrics and attribute specification for metrics of the zHMC and the virtualization layers (and not covered elsewhere)
    - Basic resources/entities to represent mainframe concepts and z/OS systems software
    - Server spans for z/OS systems software (MQ, CICS, IMS, Db2)
  - Are there areas you're ready to stabilize in 2026?
  - Are there things you need from other parts of the semconv community?
    - Virtualization support, entities with relationships
- TPS PR [#1898](https://github.com/open-telemetry/semantic-conventions/pull/1898): Updated to only have a concise definition of TPS spans / attributes, i.e. removed TPS HTTP and RPC spans.
- Documentation PR [#8624](https://github.com/open-telemetry/opentelemetry.io/pull/8624#pullrequestreview-3715658597): Accept proposed changes and process further.
- Zowe API ML OTel Observations
