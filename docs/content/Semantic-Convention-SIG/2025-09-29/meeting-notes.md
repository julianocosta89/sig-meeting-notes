## Meeting Notes

### Attendees
- Armin Ruech (Dynatrace)
- Trask Stalnaker (Microsoft)
- Liudmila Molkova (Grafana Labs)
- Michele Mancioppi (Dash0)
- James Thompson
- Christophe Kamphaus
- Daniel Dyla (Dynatrace)
- Braydon Kains (Google)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [Liudmila, 10 min] Reorg doc structure (separate semconv and not-semconv) [https://github.com/open-telemetry/semantic-conventions/issues/2802#issuecomment-3329873876](https://github.com/open-telemetry/semantic-conventions/issues/2802#issuecomment-3329873876)
    - “OpenTelemetry Registry”
    - Semantic Convention Registry
    - [https://opentelemetry.io/docs/specs/semconv/registry/](https://opentelemetry.io/docs/specs/semconv/registry/)
      - “Semantic Convention” Registry
    - Why is version in the TOC?
    - version less visible, changelog more visible
    - Maybe version in a  badge?
    - “version since stable” in a badge
    - Move stability badge to the attribute name column?
    - Requirement level is next most important?
    - Stability badge can be two part, e.g. stability level | version/date since
  - [Michele, 10min] How to evolve peer.* to support service namespaces [https://github.com/open-telemetry/semantic-conventions/pull/2807](https://github.com/open-telemetry/semantic-conventions/pull/2807)
    - [https://github.com/open-telemetry/community/blob/main/projects/service-and-deployment-semconv.md](https://github.com/open-telemetry/community/blob/main/projects/service-and-deployment-semconv.md)
    - [https://cloud-native.slack.com/archives/C09HLNSSJSE](https://cloud-native.slack.com/archives/C09HLNSSJSE)
