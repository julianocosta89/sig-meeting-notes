## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Gokhan Uslu (Microsoft)
- Josh MacDonald (Microsoft)
- Jake Dern (F5)
- Chanly Ly (F5)
- Aaron Marten (Microsoft)
- Camila Valdebenito (Microsoft)
- Nikhil Manchanda (Microsoft)
- Tom Tan (Microsoft)

### Agenda
- [Triage]
  - Issues that need to be discussed: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion)
  - Issues that have just been marked as stale: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale)
- [Drew, Laurent] - Status update on migrating `metric_set` to use enum-based attributes.
- [Chanly] - Extension system for the validation framework.
  - [https://github.com/open-telemetry/otel-arrow/issues/3510](https://github.com/open-telemetry/otel-arrow/issues/3510)
- [Laurent]
  - Metrics Temporality Processor [https://github.com/lquerel/otel-arrow/blob/e33e88d299820e73353e1cdcd0631df9571ec077/rust/otap-dataflow/docs/rfc/0003-temporality-processor.md](https://github.com/lquerel/otel-arrow/blob/e33e88d299820e73353e1cdcd0631df9571ec077/rust/otap-dataflow/docs/rfc/0003-temporality-processor.md)
  - Prometheus Exporter
- [Josh]  [Update on Multitenancy design](https://github.com/open-telemetry/otel-arrow/pull/3583)
  - State a priority: Macro-scale, not Micro-scale tenants. Routing before limiting.
  - [Discuss connection with Auth extension](https://github.com/open-telemetry/otel-arrow/pull/3581)
