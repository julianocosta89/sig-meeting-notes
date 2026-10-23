## Meeting Notes

### Attendees
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- [John Watson](mailto:john.watson@sublimesecurity.com)(Sublime Security)
- Jason (Splunk)
- Jack Berg (Grafana Labs)
- Pranav Sharma (Google)
- Cleverchuk (Solarwinds)
- Jonathan Halliday (IBM)
- Peter Findeisen (Cisco)
- Robert Niedziela (Splunk)

### Agenda
- Java Instrumentation v3 review
- [jack] Merging HostIdResource and HostResource to facilitate host entity [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/20816](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/20816)
  - AI: changelog entry for breaking change
- [jack] contrib maintenance policy [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/3156](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/3156)
- [cleverchuk] - Proxy config in declarative config
  - OTLP Specification for configuration properties
  - Declarative config follows that
- [jack] Exporter backpressure to enable concurrent export! [https://github.com/open-telemetry/opentelemetry-java/pull/8928](https://github.com/open-telemetry/opentelemetry-java/pull/8928)
- [jason via cesar] We use reflection a bunch in extensions, right?
  - [https://github.com/open-telemetry/opentelemetry-java/pull/8865](https://github.com/open-telemetry/opentelemetry-java/pull/8865)
  - Cesar suggested that maybe this demonstrated to be breaking when minified?
  - Only when used tho? I dunno.
  - We have a very basic minified app smoke test in Android.
  - Core publishes reflect-config.json and maybe that can be used?
- [Abiy Asfaw] Would like for a share feature request issue to get feedback on the approach, and guidance on moving forward [https://github.com/open-telemetry/opentelemetry-java/issues/8976](https://github.com/open-telemetry/opentelemetry-java/issues/8976)
- [jack] OTel JS published v3 of SDK
