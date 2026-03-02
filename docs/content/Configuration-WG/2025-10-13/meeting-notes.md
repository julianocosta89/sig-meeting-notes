## Meeting Notes

### Attendees
- Jack Berg (Grafana Labs)
- Tyler Yahn (Splunk)

### Agenda
- [jack] Meta schema presentation: [https://github.com/open-telemetry/opentelemetry-configuration/pull/312](https://github.com/open-telemetry/opentelemetry-configuration/pull/312)
  - Tracks data that doesn’t fit neatly into JSON schema
    - Type / property semantics (including default values)
    - SDK extension plugin interface types
    - Language implementation status
  - Tooling ensures meta schema is kept in sync with JSON schema
    - Adds missing types / properties to meta schema
    - Removes extra types / properties from meta schema
    - Build fails if tooling hasn’t been run
  - Facilitates schema markdown generation
  - Facilitates example comment generation
- [Triage project board](https://github.com/orgs/open-telemetry/projects/38)
