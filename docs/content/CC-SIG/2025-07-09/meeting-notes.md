## Meeting Notes

### Attendees
- Marc Alff (Oracle) – absent, time conflict
- Doug Barker
- Lalit Kumar Bhasin
- Tom Tan
- ~~Rafael Roquetto (Grafana) -> away~~

### Agenda
- Upstream
  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)
    - LogProcessor::OnEmit() support in otel-cpp
    - AnyValue can be heterogeneous list / complex types for span attributes. (OTEP approved, will be added in specs).
  - [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
    - Semconv 1.35.0 released, but broken:
      - Please DO NOT release SemConv artifacts based on v1.35.0
  - [Configuration](https://github.com/open-telemetry/opentelemetry-configuration)
  - [Proto](https://github.com/open-telemetry/opentelemetry-proto)
  - [Weaver](https://github.com/open-telemetry/weaver)
- Opentelemetry-cpp
  - Issues
  - PR
  - Misc
    - [Marc] - Discuss usage of generative AI (copilot)
      - Concerns about intellectual property for the repo
      - Concerns about licensing, is the generated code compatible with the license for opentelemetry-cpp ?
      - EasyCLA for generated code ?
      - Where (URL) / When was this discussed with TC / GC ?
- Opentelemetry-cpp-contrib
  - Misc
- Opentelemetry-cpp-buildtools
  - Misc
