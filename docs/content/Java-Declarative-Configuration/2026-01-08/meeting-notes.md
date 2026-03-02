## Meeting Notes

### Attendees
- Jason - Splunk
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jay DeLuca (Grafana Labs)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Robert Niedziela (Splunk)
- cleverchuk(solarwinds)
- Peter Findeisen (Cisco)
- Lauri Tulmin (Splunk)
- Jonathan Halliday (IBM)
- Pranav Sharma (Google)
- Matthew Li (Datadog)
- Jean Bisutti (Microsoft)
- Bruno Baptista (IBM)

### Agenda
- [Bruno] [20m] Present preliminary results on the Quarkus OpenTelemetry Performance work.
  - Is this published? Can we get a link?
- [Trask] Java SDK release
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7947](https://github.com/open-telemetry/opentelemetry-java/pull/7947)
  - [add method to retrieve instrumentation configuration by name](https://github.com/open-telemetry/opentelemetry-java/pull/7927)
- [Gregor] [move module enabled to "agent" in declarative config](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/15796)
- [jack] Finally bit the bullet and learned about OSGi [https://github.com/open-telemetry/opentelemetry-java/pull/7964](https://github.com/open-telemetry/opentelemetry-java/pull/7964)
- [Robert] Discussion on [https://github.com/open-telemetry/opentelemetry-specification/pull/4800](https://github.com/open-telemetry/opentelemetry-specification/pull/4800)dded support for distribution config in ConfigProvider
