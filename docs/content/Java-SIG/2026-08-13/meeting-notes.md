## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- Jay DeLuca (Grafana Labs)
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jack Shirazi (Elastic)
- Jason (Splunk)
- Peter Findeisen (Cisco)
- Pranav Sharma (Google)
- Sylvain Juge (Elastic)
- Lauri Tulmin (Splunk)

### Agenda
- Java Instrumentation v3 review
- [jack] Please review: explicit histogram contended performance [https://github.com/open-telemetry/opentelemetry-java/pull/8717](https://github.com/open-telemetry/opentelemetry-java/pull/8717)
- [jason] Speaking of micrometer….
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/7030](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/7030) (3rd most popular issue)
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19379](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19379) baby step
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/11354](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/11354)
- [Sylvain] jmx enable stable metrics, or use include/exclude as alternative ? [PR](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19344)
- [Jay] FYI: working on adding a nightly smoke test for declarative config kitchen sink config
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19562](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19562)
  - Found a bug: [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19561](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/19561)
