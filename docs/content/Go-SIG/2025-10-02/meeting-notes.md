## Meeting Notes

### Attendees
- Damien Mathieu (Elastic)
- Bryan Boreham (Grafana Labs)
- Tyler Yahn (Splunk)
- David Ashpole (Google)

### Agenda
- [Damien] Last week’s [go.opentelemetry.io](http://go.opentelemetry.io) incident, and refactor of go-vanityurls
  - [https://opentelemetry.io/blog/2025/go-opentelemetry-io-expired-certificate/](https://opentelemetry.io/blog/2025/go-opentelemetry-io-expired-certificate/)
  - [https://github.com/open-telemetry/opentelemetry-go-vanityurls/pull/87](https://github.com/open-telemetry/opentelemetry-go-vanityurls/pull/87)
  - AI Damien: follow up with a community issue
- [Tyler] [Add the internal/observ package to otlptracegrpc](https://github.com/open-telemetry/opentelemetry-go/pull/7404#top)
  - AI Robert: create an issue to standardize tracking the package being instrumented.
- [Tyler] [Support custom error type semantics](https://github.com/open-telemetry/opentelemetry-go/pull/7442)
- [dashpole] Counter performance improvements
  - [https://github.com/open-telemetry/opentelemetry-go/pull/7427](https://github.com/open-telemetry/opentelemetry-go/pull/7427)
- [dashpole] Exemplar reservoir performance improvements
  - Benchmarks: [https://github.com/open-telemetry/opentelemetry-go/pull/7441](https://github.com/open-telemetry/opentelemetry-go/pull/7441)
  - HistogramReservoir: [https://github.com/open-telemetry/opentelemetry-go/pull/7443](https://github.com/open-telemetry/opentelemetry-go/pull/7443)
  - FixedSizeReservoir: [https://github.com/open-telemetry/opentelemetry-go/pull/7447](https://github.com/open-telemetry/opentelemetry-go/pull/7447)
- [Tyler] Milestone v1.39.0 check-in:
  - [Otel](https://github.com/open-telemetry/opentelemetry-go/milestone/74)
  - [Contrib](https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/33)
