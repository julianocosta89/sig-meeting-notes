## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- David Luna (Elastic)
- Maxime Quentin (Datadog)
- Hector Hernandez (Microsoft)
- Cleo Schneider (Google/Firebase)

### Agenda
- [david] log level fix. Please review
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/437](https://github.com/open-telemetry/opentelemetry-browser/pull/437)
- [martin] Browser conventions PR moved to the new repo
  - [https://github.com/open-telemetry/semantic-conventions-client-side/pull/14](https://github.com/open-telemetry/semantic-conventions-client-side/pull/14)
  - originally here [https://github.com/open-telemetry/opentelemetry-browser/pull/404](https://github.com/open-telemetry/opentelemetry-browser/pull/404)
- [Instrumentation base PR](https://github.com/open-telemetry/opentelemetry-browser/pull/278). Could be simplified if it’s not required to implement Node’s instrumentation interface
  - Action: Ping Jared about this
- Migration guide from old JS instrumentations
  - especially for document load
    - spans vs logs
  - action items:
    - create issue for migration documentation
    - create issue for discussion whether we need span-based document-load instrumentation
