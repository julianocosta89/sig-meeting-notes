## Meeting Notes

### Attendees
- Liudmila Molkova
- Christophe Kamphaus
- Ayushi Asthana
- Armin Ruech (Dynatrace)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
- [trask] [https://github.com/open-telemetry/semantic-conventions-genai/pull/96#discussion_r3253221521](https://github.com/open-telemetry/semantic-conventions-genai/pull/96#discussion_r3253221521)
  - Histogram: `gen_ai.client.token.usage`
    - Attribute: `gen_ai.token.type`
    - Splits the value
      - `input` / `output`
    - 80 input 20 output, total is 100, but aggregation is meaningless
  - ~~CI pipeline~~ VCS metrics switched from histogram to gauges
- [[Ayushi Asthana](mailto:asthana.ayushi12@gmail.com)] [https://github.com/open-telemetry/semantic-conventions/issues/3579](https://github.com/open-telemetry/semantic-conventions/issues/3579)
  - [https://github.com/open-telemetry/semantic-conventions/pull/3645](https://github.com/open-telemetry/semantic-conventions/pull/3645)
  - [Introduce "data" attribute group in OTEL](https://docs.google.com/document/d/13jCkwYxS6pHTFTAPXqMljp2lTkO3FXKzKf34BFB2YEA/edit?usp=sharing)
  - What's the right root namespace?
    - Data is a big commitment
    - Resource / entity attributes: service.data.*
    - Dynamic:
      - Options
        - sensitivity.*
          - Probably per-attribute not about the flow
          - Very broad too
        - Allow `data` but limit use-cases
        - Use prefix depending on use-case
- [Liudmila] Stabilize process entities [https://github.com/open-telemetry/semantic-conventions/pull/3564](https://github.com/open-telemetry/semantic-conventions/pull/3564)
