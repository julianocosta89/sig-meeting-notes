## Meeting Notes

### Attendees
- Jack Berg (Grafana)
- Alex Boten (Honeycomb)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana)

### Agenda
- What if there’s no declarative config?
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7927#pullrequestreview-3627364643](https://github.com/open-telemetry/opentelemetry-java/pull/7927#pullrequestreview-3627364643)
  - How should ConfigProvider behave when declarative config is not used?
  - Feedback from meeting
    - ConfigProvider is also meant to be used when declarative config is not used
      - But maybe we don’t need to spec out how env variables are mapped - unless other languages (than Java) would benefit from it
    - Could delete this sentence - as it doesn’t seem to be needed based on Java experience
      - *If the .instrumentation node is not set, get instrumentation config MUST return nil, null, undefined or another language-specific idiomatic pattern denoting empty.*
    - Implementation for Java PR
      - Move default methods back to ConfigProvider
      - SDK has to supply env var based implementation of ConfigProvider
        - But that has java agent specific rules in there right now
        - Could create a stripped down version for the SDK repo
- Status of stability
  - Implementations update to 1.0.0-rc.3
  - Drop $id from schema: [https://github.com/open-telemetry/opentelemetry-configuration/pull/487](https://github.com/open-telemetry/opentelemetry-configuration/pull/487)
  - Consistent vocabulary [https://github.com/open-telemetry/opentelemetry-specification/pull/4806](https://github.com/open-telemetry/opentelemetry-specification/pull/4806)
