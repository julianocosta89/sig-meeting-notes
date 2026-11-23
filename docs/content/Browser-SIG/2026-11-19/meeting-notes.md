## Meeting Notes

### Attendees
- Aditya
- maxime quentin (datadog)
- Chris Chestnut (Google/Firebase)
- Martin Kuba (Grafana Labs)
- David Luna (Elastic)
- Joaquin Diaz (Palo Alto Networks)
- Jackson Weber (Microsoft)

### Agenda
- [Aditya] Require another approval and merge [#486](https://github.com/open-telemetry/opentelemetry-browser/pull/486) and server-trace stitching [#564](https://github.com/open-telemetry/opentelemetry-browser/pull/564).
- [martin] Base URL
  - one more check on alignment
    - [https://github.com/open-telemetry/opentelemetry-browser/issues/493#issuecomment-7014837824](https://github.com/open-telemetry/opentelemetry-browser/issues/493#issuecomment-7014837824)
- [david] Roadmap review and focus topics
  - Instrumentations consolidation
    - [https://github.com/open-telemetry/opentelemetry-browser/issues/209](https://github.com/open-telemetry/opentelemetry-browser/issues/209)
    - Actions
      - Soft deprecate package: README, diag.warn and types
      - Wait for a period of time (to be defined)
      - Run npm deprecate for all packages
  - Sessions & Page context
    - Design proposals
      - Sessions (David)
      - Page Context (Joaquin)
    - Session working group
      - Prior work
        - [https://github.com/elastic/elastic-otel-rum-js/pull/194](https://github.com/elastic/elastic-otel-rum-js/pull/194)
