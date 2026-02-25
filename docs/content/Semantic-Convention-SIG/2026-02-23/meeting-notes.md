## Meeting Notes

### Attendees
- Josh Suereth
- Christophe Kamphaus
- Matthew Hensley (Grafana Labs)

### Agenda
- Triage
- [Michele, ???] otel.trace.id, otel.span.id and otel.flags as log attribute fallback for tools that do not support setting OTLP fields
  - Logging layout, configure these
  - [https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/compatibility/logging_trace_context.md](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/compatibility/logging_trace_context.md)
- [carlos] semconv for spans lifecycle: [https://github.com/open-telemetry/semantic-conventions/issues/2133](https://github.com/open-telemetry/semantic-conventions/issues/2133)
  - Events: onStart/End + heartbeat (regular interval)
  - Need to attach the SpanContext of the related Span, parent SpanContext information, attributes and essentially all Span information (at least for Span Start).  Is there anything similar, serialization-wise for such information?
  - What information you'd be sending while spans is active
    - The same you'd export otherwise
    - Span name - attribute
    - Parent id
  - [suereth] FYI - prototype using span events to reconstruct spans - [https://github.com/jsuereth/otlp-mmap](https://github.com/jsuereth/otlp-mmap)
    - Span events in particular - [https://github.com/jsuereth/otlp-mmap/blob/main/specification/mmap.proto#L19](https://github.com/jsuereth/otlp-mmap/blob/main/specification/mmap.proto#L19)
- Please review trivial GenAI exception event PR [https://github.com/open-telemetry/semantic-conventions/pull/3436](https://github.com/open-telemetry/semantic-conventions/pull/3436)
- [Liudmila] `error.type` [https://github.com/open-telemetry/semantic-conventions/issues/3452](https://github.com/open-telemetry/semantic-conventions/issues/3452)
- [Liudmila] Federated semconv [https://github.com/open-telemetry/opentelemetry-weaver-examples/pull/33](https://github.com/open-telemetry/opentelemetry-weaver-examples/pull/33)
  - Time for a full sample with policies and docs ALL CAPS!
