## Meeting Notes

### Attendees
- Joshua MacDonald (Microsoft)
- Pablo Baeyens (Datadog)
- Danny Chin (CMU)
- Jake Dern (Microsoft)
- Cijo Thomas (Microsoft)
- Luke Steensen (Datadog)
- Albert Lockett (F5)
- Aaron Marten (Microsoft)
- Evan Torrie

### Agenda
- This is a special “Phase 3” planning discussion!
- (place your talking points below…)
- …
- suggest to skip recent issues, however to advertise: (1) Danny’s research report, (2) Albert’s columnar query engine.
- …
- Josh’s big topics!
  - Making OTAP an official alternative, see [Josh’s very rough OTEP](https://github.com/open-telemetry/opentelemetry-specification/pull/4791) and Tigran’s doc in #otel-specification. The “overnight” upgrade.
  - “Collector” and OTAP-dataflow?, see [Josh’s very rough Collector RFC](https://github.com/open-telemetry/opentelemetry-collector/pull/13369) on Rust/Go interop
  - Go Collector: OTLP bytes, OTAP PData options? Plugins, distribution building, extension components
- Rate limits & memory limits, see [Collector issue](https://github.com/open-telemetry/opentelemetry-collector/issues/12603) on this topic
- Opaque and/or “Simple OTLP” PData, non-Arrow e.g., JSON formats, (no issue filed)
- OTAP-direct OTel SDK
- SDK with embedded OTAP-dataflow
- Profiling support
- Entity support
- Multivariate metrics
- [Crates.io](http://Crates.io) release
- [Cijo] Internal Logs/Traces -  [https://github.com/open-telemetry/otel-arrow/pull/1584](https://github.com/open-telemetry/otel-arrow/pull/1584)
- Administrative:
  - We need more code reviewers!
