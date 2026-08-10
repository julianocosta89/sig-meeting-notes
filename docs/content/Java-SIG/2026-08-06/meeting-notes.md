## Meeting Notes

### Attendees
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Jason (Splunk)
- Jonathan Halliday (IBM)
- Jack Shirazi (Elastic)
- Trask Stalnaker (Microsoft)
- Peter Findeisen (Cisco)
- Jack Berg (Grafana Labs)
- [Bruce Bujon](mailto:bruce.bujon@datadoghq.com) (Datadog)
- Antoine Toulme (Splunk)
- Pranav Sharma (Google)
- Mohammed Abdessetar Elyagoubi (Sofrecom)
- Lauri Tulmin (Splunk)

### Agenda
- Java Instrumentation v3 review
- [jack s] declarative config transparent support for “node” where currently “node/development” ([thread](https://github.com/open-telemetry/opentelemetry-specification/pull/4900#issuecomment-5069953540))
  - PR embodying this for core data model generated pojos: [https://github.com/open-telemetry/opentelemetry-java/pull/8654](https://github.com/open-telemetry/opentelemetry-java/pull/8654)
  - Related [https://github.com/open-telemetry/opentelemetry-configuration/issues/689](https://github.com/open-telemetry/opentelemetry-configuration/issues/689)
- [jack b] 1.65.0 release - any requests?
  - Last-value-wins semantics for AtrributesMap [https://github.com/open-telemetry/opentelemetry-java/pull/8548](https://github.com/open-telemetry/opentelemetry-java/pull/8548)
- [pranav] Individual instrumentation libraries - path to stability in 3.0
  - Telemetry stability doc in spec: [https://github.com/open-telemetry/opentelemetry-specification/blob/7160e9b99e54e03312d840c860320442eeb11cf6/specification/telemetry-stability.md](https://github.com/open-telemetry/opentelemetry-specification/blob/7160e9b99e54e03312d840c860320442eeb11cf6/specification/telemetry-stability.md)
  - Examples of stabilization process:
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/12846](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/12846)
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/12608](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/12608)
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/16063](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/16063)
- [jonathan] [https://openjdk.org/projects/leyden/](https://openjdk.org/projects/leyden/) and agent behaviour
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/11068](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/11068)
