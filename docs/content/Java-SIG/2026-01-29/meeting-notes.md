## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jay DeLuca (Grafana Labs)
- Jonathan Halliday (IBM)
- Jason (Splunk)
- Trask Stalnaker (Microsoft)
- Jack Berg (Grafana Labs)
- Peter Findeisen (Cisco)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- Surbhi A (Cisco)
- Lauri Tulmin (Splunk)
- Pranav Sharma (Google)
- Robert Niedziela (Splunk)
- Jack Shirazi (Elastic)
- Bruno Baptista (IBM)
- Cleverchuk (Solarwinds)
- Jean Bisutti (Microsoft)

### Agenda
- [jack] Talk about okhttp sender strategy with respect to okhttp major version bumps: [https://github.com/open-telemetry/opentelemetry-java/issues/8001](https://github.com/open-telemetry/opentelemetry-java/issues/8001)
  - okhttp 4.x branches: [https://github.com/square/okhttp/branches/all?query=4](https://github.com/square/okhttp/branches/all?query=4). Old old old
  - Importance of BOM alignment: [https://github.com/open-telemetry/opentelemetry-java/issues/6970](https://github.com/open-telemetry/opentelemetry-java/issues/6970)
- [pranav] Have a question about the [internal log level (JUL) mapping](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/b4bd148b45bae57bcfda454c74aab669707e4a45/javaagent-bootstrap/src/main/java/io/opentelemetry/javaagent/bootstrap/PatchLogger.java#L185) of the OTel Java Agent. This is related to [an upstream issue opened against GCP OTel exporter](https://github.com/GoogleCloudPlatform/opentelemetry-operations-java/issues/430%20).
  - Update the internal JUL mapping in the OTel Java Agent to map INFO to INFO.
- [Surbhi] Discuss the open question on PR (regarding okhttp3 library version bump again) - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15664](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15664)
- [Trask] Java Instrumentation 3.0
  - Stable semantic conventions
    - Code
    - Database
    - RPC
    - peer.service -> service.peer.name
    - Log based exceptions (instead of span events)
  - Invoke dynamic
  - Declarative configuration
  - ~~Drop java 8~~
- [Gregor] Who is coming to OTel Unplugged on Monday?
