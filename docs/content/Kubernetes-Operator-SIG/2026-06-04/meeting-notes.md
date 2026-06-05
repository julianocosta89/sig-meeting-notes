## Meeting Notes

### Attendees
- Mikołaj Świątek (Elastic)
- Benedikt Bongartz (Red Hat)
- [Pavol Loffay](mailto:ploffay@redhat.com)(Red Hat)
- [Ozzy Walsh](mailto:ozwalsh@redhat.com)(Red Hat)

### Agenda
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)Using codecov for tracking e2e test results (and maybe coverage later)?
  - Our current E2E test result summary doesn’t work very well
  - It gives roughly the [output](https://github.com/swiatekm/opentelemetry-operator/pull/143#issuecomment-4601564512) we want, plus some additional features
  - Already used by otel, easy to integrate
  - 👍
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co) Add an annotation we own for tracking annotations we add, like the Prometheus ones ([#5069](https://github.com/open-telemetry/opentelemetry-operator/pull/5069))
  - Add our own annotation to track this
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)Publishing the api package ([#5175](https://github.com/open-telemetry/opentelemetry-operator/issues/5175))
  - Verify if we actually need to
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)Are we against allowing the container command to be set for OpenTelemetryCollector ([#4937](https://github.com/open-telemetry/opentelemetry-operator/pull/4973))?
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)
- [Ozzy Walsh](mailto:ozwalsh@redhat.com) OBI eBPF instrumentation implementation approaches; DaemonSet deployment example: [https://github.com/ozzywalsh/obi-poc](https://github.com/ozzywalsh/obi-poc)
- Otel Go Instrumentation - don’t deprecate until the upstream project is deprecated or we can replace with OBI
