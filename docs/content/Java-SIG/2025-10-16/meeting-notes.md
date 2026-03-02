## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Cloudera)
- Trask Stalnaker (Microsoft)
- Jason (Splunk)
- Jack Berg (Grafana Labs)
- cleverchuk(solarwinds)
- Jack Shirazi (Elastic)
- Jonathan Halliday (IBM)
- Peter Findeisen (Cisco)
- Bruno Baptista (IBM)
- Lauri Tulmin (Splunk)

### Agenda
- Instrumentation and Contrib releases
- [jason] - What do folks think about this idea of a unified agent config page?
  - [https://github.com/open-telemetry/opentelemetry.io/issues/7985#issuecomment-3402821237](https://github.com/open-telemetry/opentelemetry.io/issues/7985#issuecomment-3402821237)
  - I agree that ^F is powerful.
  - [https://quarkus.io/guides/all-config](https://quarkus.io/guides/all-config)
  - Would it also include sdk configs?
  - We could keep the existing “pages” and this would be an additional reference. I dunno.
  - [jack] Related wrinkle: in declarative config I’m working on generated docs [https://github.com/jack-berg/opentelemetry-configuration/blob/language-implementation-status/schema-docs.md](https://github.com/jack-berg/opentelemetry-configuration/blob/language-implementation-status/schema-docs.md)
- [jason] - Are we suggesting that we’re only going to add new configurations to declarative? Seems like a mistake.
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7562#issuecomment-3403413625](https://github.com/open-telemetry/opentelemetry-java/pull/7562#issuecomment-3403413625)
- [trask] [https://github.com/open-telemetry/semantic-conventions-java/pull/317](https://github.com/open-telemetry/semantic-conventions-java/pull/317)
- Env var / declarative config compatibility
  - Env vars accept time unit
  - Declarative config doesn’t (only milliseconds), so can’t provide migration yaml that references those env vars
- Trace context propagator
  - What does “none,w3c” mean?
  - [https://github.com/open-telemetry/opentelemetry-specification/issues/4682](https://github.com/open-telemetry/opentelemetry-specification/issues/4682)
