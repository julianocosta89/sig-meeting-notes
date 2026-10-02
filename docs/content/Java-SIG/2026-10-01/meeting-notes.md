## Meeting Notes

### Attendees
- .Jay DeLuca (Grafana Labs)
- Trask Stalnaker (Microsoft)
- [John Watson](mailto:jkwatson@gmail.com)(Sublime Security)
- Pranav Sharma (Google)
- Jack Berg (Grafana Labs)
- Peter Findeisen (Cisco)
- cleverchuk(solarwinds)
- Jonathan Halliday (IBM)

### Agenda
- Java Instrumentation v3 review
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14938](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14938)
- [jack] SdkResourceProvider proposal [https://github.com/open-telemetry/opentelemetry-java/pull/8865](https://github.com/open-telemetry/opentelemetry-java/pull/8865)
  - SdkAutoconfigureAccess.getResource(AutoConfiguredOpenTelemetrySdk)
- Trace profiling correlation - Thread context performance tuning
  - Serializing spanid and traceid
  - Serializing String to byte[]
  - SpanContext has accessors for both String and byte[]
    - Store both byte[] and String?
    - Initialize either way
    - Opposite could be lazily created on first access
