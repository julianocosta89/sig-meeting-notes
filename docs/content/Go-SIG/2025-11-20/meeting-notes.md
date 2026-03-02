## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- [Owen Williams](mailto:owen.williams@grafana.com)(Grafana)
- Sam Xie (Splunk)
- Bryan Boreham (Grafana)
- David Ashpole (Google)

### Agenda
- [Tyler] Release?
  - Holding on otelconf 1.0.0 RC support
- [Robert] [spec: Stabilize new attribute value types #4710](https://github.com/open-telemetry/opentelemetry-specification/issues/4710)
  - From our side, do we need a better prototype than [[Prototype] attribute: add complex value types #6809](https://github.com/open-telemetry/opentelemetry-go/pull/6809)?
  - Are we OK with the current proposals of attribute limits: [https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/common/README.md#attribute-limits](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/common/README.md#attribute-limits)
- [Robert] Proposal: [sdk/log: Move Enabled method from FilterProcessor to Processor interface #7617](https://github.com/open-telemetry/opentelemetry-go/issues/7617)
- [Robert] Any opinions on how to go forward with [Support OTEL_EXPORTER_OTLP_[LOGS|TRACE|METRICS]_INSECURE and OTEL_EXPORTER_OTLP_INSECURE env vars in OTLP HTTP exporters #7614](https://github.com/open-telemetry/opentelemetry-go/issues/7614)?
