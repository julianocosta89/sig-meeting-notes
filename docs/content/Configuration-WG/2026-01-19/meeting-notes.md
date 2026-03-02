## Meeting Notes

### Attendees
- Jack Berg (Grafana Labs)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana Labs)
- Alex Boten (Honeycomb)

### Agenda
- [Triage project board](https://github.com/orgs/open-telemetry/projects/38)
- [jack] Reminder to review declarative spec and raise issues. For reference, here is the scope we aim to stabilize: [https://github.com/open-telemetry/opentelemetry-specification/pull/4568](https://github.com/open-telemetry/opentelemetry-specification/pull/4568)
- [Gregor] [https://github.com/open-telemetry/opentelemetry-java/issues/7961](https://github.com/open-telemetry/opentelemetry-java/issues/7961)
  - [jack] Shouˇld return a NoopConfigProvider if none is installed, but the behavior of a NoopConfigProvider is underdefined in the spec. Should follow the lead of tracing, [metrics](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/noop.md), etc and add an explicit noop document with behavior.
