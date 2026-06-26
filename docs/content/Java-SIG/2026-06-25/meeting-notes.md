## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jonathan Halliday (IBM)
- Jack Shirazi (Elastic)
- Pranav Sharma (Google)
- Peter Findeisen (Cisco)
- Jay DeLuca (Grafana Labs)
- Lauri Tulmin (Splunk)
- Robert Niedziela (Splunk)

### Agenda
- Java Instrumentation v3 review
- [jack] Bound instruments: [https://github.com/open-telemetry/opentelemetry-java/pull/8527](https://github.com/open-telemetry/opentelemetry-java/pull/8527)
- [jack] [https://github.com/open-telemetry/opentelemetry-java/pull/8480](https://github.com/open-telemetry/opentelemetry-java/pull/8480)
- [Jay] Inform: Released first iteration of [java agent release comparison](https://explorer.opentelemetry.io/java-agent/releases?from=2.27.0&to=2.28.1) tool in the ecosystem explorer if anyone has feedback or feature requests
  - There’s some “false positives” around telemetry added/removed due to us fixing some of the labeling related to configuration options, it will be better in a couple releases when that is more stable
- [jack] FYI, am working on a variety of customizations to how the declarative config POJOs are generated in preparation for them becoming part of stable API
