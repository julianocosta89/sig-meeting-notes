## Meeting Notes

### Attendees
- Josh Suereth
- Dmitry Anoshin
- Ted Young (Grafana Labs)

### Agenda
- Prioritization Concerns
  - Browser / Client SIG Needs
- [dmitryax] Follow up on [https://github.com/open-telemetry/opentelemetry-specification/pull/4836](https://github.com/open-telemetry/opentelemetry-specification/pull/4836)
  - Will update with blocking comments and make some changes to data model?
- [suereth] Merge Algorithm: [https://github.com/open-telemetry/opentelemetry-specification/pull/4768](https://github.com/open-telemetry/opentelemetry-specification/pull/4768)
  - Will update and push
- [suereth] [https://github.com/orgs/open-telemetry/projects/85](https://github.com/orgs/open-telemetry/projects/85)
  - Collector work
    - Transform processor work hard
      - Currently low-level support in pdata
      - Users probably want high-level API, e.g. on Entity directly
    - Two options:
      - Add low-level to transform processor + create new entity processor
      - Only add high-level to transform processor
    - Will move forward with high level
