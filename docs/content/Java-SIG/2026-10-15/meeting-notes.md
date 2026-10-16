## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- [John Watson](mailto:john.watson@sublimesecurity.com)(Sublime Security)
- Bruno Baptista (IBM)
- Pranav Sharma (Google)
- Trask Stalnaker (Microsoft)
- Jack Shirazi (Elastic)
- Robert Niedziela (Splunk)
- Jason (AppDynamics)

### Agenda
- Java Instrumentation v3 review
- [pranav] Thoughts on [PR#8935](https://github.com/open-telemetry/opentelemetry-java/pull/8935) and related [spec proposal](https://github.com/open-telemetry/opentelemetry-specification/issues/5358).
  - Support PeriodicMetricReader maxExportBatchSize in autoconfigure
- [jack] SdkResourceProvider has approval from Josh S. Need an official approval if we want to move forward [https://github.com/open-telemetry/opentelemetry-java/pull/8865](https://github.com/open-telemetry/opentelemetry-java/pull/8865)
- [jason] Sorry last minute, but one idea is to drop support for otel.javaagent.configuration-file in 3.0?
  - Probably not until the declarative config bit is stabilized
  - Do all the “flat” deprecations at once
