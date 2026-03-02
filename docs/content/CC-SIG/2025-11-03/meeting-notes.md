## Meeting Notes

### Attendees
- Marc Alff (Oracle)
- xxx

### Agenda
- Upstream
  - [Spec](https://github.com/open-telemetry/opentelemetry-specification)
    - Deprecate ZIPKIN exporter ?
      - To consider, if zipkin accepts OTLP.
  - [Semantic conventions](https://github.com/open-telemetry/semantic-conventions)
    - Release 1.38, adopted in otel-cpp
  - [Configuration](https://github.com/open-telemetry/opentelemetry-configuration)
    - Lot of recent activity, converging on 1.0.0 stability
  - [Proto](https://github.com/open-telemetry/opentelemetry-proto)
    - New release 1.9.0, needs upgrade in bcr and otel-cpp
  - [Weaver](https://github.com/open-telemetry/weaver)
    - Release 0.18.0, adopted in otel-cpp
- Opentelemetry-cpp
  - Issues
  - PR
  - Misc
    - [Marc] - Plan next release
      - PR for views from Tom
    - [Tom] - Clarify/cleanup compile flags dependencies in header files, due to build options. Install config.h ?
      - Related to packaging
- Opentelemetry-cpp-contrib
  - Misc
- Opentelemetry-cpp-buildtools
  - Misc
