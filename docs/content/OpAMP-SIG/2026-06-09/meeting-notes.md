## Meeting Notes

### Attendees
- Michel Laterman (Elastic)
- Tigran Najaryan
- Juande Manjon
- Evan Bradley (Dynatrace)
- Douglas Camata (Coralogix)
- Israel Blancas (Coralogix)
- Kelsey Ma (Splunk)

### Agenda
- [Juande] Addressing feedback to restore .proto. at *opamp.proto.v1* like OTLP protocol does.
  - I would like to have a clear direction about OpAmp independent specs from maintainers. In which cases OpAmp should be independent of other protocols, and which cases should follow OTLP specs. [Restructure proto folders to align with versioned packages #338](https://github.com/open-telemetry/opamp-spec/issues/338)
- [Michel] Change websocket library to coder/websocket: [https://github.com/open-telemetry/opamp-go/pull/576](https://github.com/open-telemetry/opamp-go/pull/576)
- [Kelsey] Supervisor PR in need of review: [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/48723](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/48723)
- [Israel] Supervisor lacks of context after failure starting the agent: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44836](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44836)
- [Juande] Publishing OpAmp protos like OTEL does into the Buf registry.
