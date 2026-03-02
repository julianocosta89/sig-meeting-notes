## Meeting Notes

### Attendees
- cleverchuk(solarwinds)
- Sylvain Juge (Elastic)
- [John Watson](mailto:jkwatson@gmail.com)(Cloudera)
- Trask Stalnaker (Microsoft)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)
- [Prasad Sawool](mailto:thc.prasads@gmail.com) (Jio)
- Jay DeLuca (Grafana Labs)
- Peter Findeisen (Cisco)
- Lauri Tulmin(Splunk)
- Tyler Benson (ServiceNow)
- Robert Niedziela (Splunk)
- Jason (Splunk)
- Bruno Baptista (IBM)

### Agenda
- [jack b] SLF4J bridge [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15572](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15572)
  - Why do users want to send these logs to their traditional logging SDK?
  - Most users want to see logs in the console / local file
  - Why not use otel console logging exporter?
    - Consistent formatting with your other log statements
    - Helpful for scraping / parsing (e.g. splunk/elastic/etc.)
- [jack b] Ergonomic log API [https://github.com/open-telemetry/opentelemetry-java/pull/7907](https://github.com/open-telemetry/opentelemetry-java/pull/7907)
- [Gregor] System Properties bridge: [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15339](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15339)
  - distribution:
    - java_agent:
      - enabled: true
    - splunk:
      - …
- [cleverchuk] This block of [logic](https://github.com/open-telemetry/opentelemetry-java/blob/0e646e849045bc912c4ca79b7433233b756dafc0/sdk-extensions/autoconfigure/src/main/java/io/opentelemetry/sdk/autoconfigure/ResourceConfiguration.java#L101-L104) is incorrect because it disables all resource providers unless they’re explicitly configured in that list. It should be changed or removed entirely because I don’t expect users to know all the resource providers and enumerate them when they’re only trying to add additional providers.’
  - [jack b] This is by design. **Ignore - misinterpreted this as related to declarative config**
    - What you see is what you get philosophy: [https://github.com/open-telemetry/opentelemetry-configuration/blob/main/CONTRIBUTING.md#what-you-see-is-what-you-get](https://github.com/open-telemetry/opentelemetry-configuration/blob/main/CONTRIBUTING.md#what-you-see-is-what-you-get)
    - [ExperimentalResourceDetection.detectors](https://github.com/open-telemetry/opentelemetry-configuration/blob/main/schema-docs.md#experimentalresourcedetection) “If omitted, no resource detectors are enabled.”
    - Need to rely on [starter templates](https://github.com/open-telemetry/opentelemetry-configuration/tree/main?tab=readme-ov-file#starter-templates) referencing common values and documentation
    - Can use higher order tools like helm for curated presets
    - Related conversation: [https://github.com/open-telemetry/opentelemetry-configuration/issues/334](https://github.com/open-telemetry/opentelemetry-configuration/issues/334)
- [Sylvain] lower priority for bridged metrics vs instrumentation metrics [#15451](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/15451) (out of time)
  - I would suggest a common exclude list for all bridged metrics
