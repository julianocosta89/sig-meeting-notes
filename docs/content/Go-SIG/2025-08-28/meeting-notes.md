## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Robert Pająk (Splunk)
- Bryan Boreham (Grafana Labs)
- Sam Xie (Splunk)

### Agenda
- [Tyler] [SDK Observability Best Practices](https://github.com/open-telemetry/opentelemetry-go/issues/2547#issuecomment-3234179600):
  - [Bind stdouttrace self-observability instruments](https://github.com/open-telemetry/opentelemetry-go/pull/7226#top)
- [Tyler] Milestone v1.38.0:
  - [Otel](https://github.com/open-telemetry/opentelemetry-go/milestone/73)
  - [Contrib](https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/32)
- [Robert] PTAL [proto: all: drop attribute values restrictions #707](https://github.com/open-telemetry/opentelemetry-proto/pull/707)
  - Necessary towards unblocking [Logs to reuse attribute.[Key]Value and remove log.[Key]Value types #7034](https://github.com/open-telemetry/opentelemetry-go/issues/7034)
    - TODO: add “important” notices and information that OTLP consumers should handle the attribute types which were previously considered as not valid.
