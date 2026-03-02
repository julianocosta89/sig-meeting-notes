## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- Bruno Baptista (IBM)
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jay DeLuca (Grafana Labs)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- [Bruce Bujon](mailto:bruce.bujon@datadoghq.com) (Datadog)
- Jack Shirazi (Elastic)
- Trask Stalnaker (Microsoft)
- Peter Findeisen (Cisco)
- Jason (Splunk)
- Jack Berg (Grafana Labs)
- Robert Niedziela (Splunk)
- Pranav Sharma (Google)
- cleverchuk(solarwinds)

### Agenda
- [Bruno] [20m] Present preliminary results on the Quarkus OpenTelemetry Performance work.
  - Is this published? Can we get a link?
  - Code: [https://github.com/brunobat/quarkus-observability-perf/tree/quarkus-3.24-otel](https://github.com/brunobat/quarkus-observability-perf/tree/quarkus-3.24-otel)
  - Slides: [https://speakerdeck.com/brunobat75/quarkus-opentelemetry-performance-otel-java-jan-2026-small](https://speakerdeck.com/brunobat75/quarkus-opentelemetry-performance-otel-java-jan-2026-small)
- [Gregor] Have a ConfigProvider that allows access to system properties or declarative config to be used for extensions and distros
  - [https://github.com/open-telemetry/opentelemetry-java/issues/7961](https://github.com/open-telemetry/opentelemetry-java/issues/7961)
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/15810](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/15810)
  - What to do for users who want to continue using config properties?
    - Library instrumentation
- [Gregor] Thread details in declarative configuration
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15209](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15209)
  - Should it also be moved to “distribution”?
- [Gregor] Checking in a [claude.md](http://claude.md) / [agents.md](http://agents.md) - or any other AI helper?
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14770](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/14770)
  - Who would be interested in this?
