## Meeting Notes

### Attendees
- Joao Grassi (Dynatrace)
- Josh Suereth
- James Thompson
- Matthew Hensley (Grafana Labs)
- Liudmila
- Armin Ruech (Dynatrace)
- Christophe Kamphaus

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
    - Updated a few issues
    - Looking for Heroku owners
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [trask, 25 min] [https://github.com/open-telemetry/opentelemetry.io/pull/8208](https://github.com/open-telemetry/opentelemetry.io/pull/8208)
    - Should instr stability be tight to semconv stability ?
      - Instr regardless of semconv can be stable and then must follow semver
    - Stable instrumentation
      - Advertise telemetry shape
        - Can be documented locally
      - Shouldn’t break users or alerts without major version
      - Communicate major version bumps
        - Schema versions / transformations?
          - Custom java schema-url
          - SchemaUrl 1.X.Y-dev
    - Once semconv is marked stable, any new stable instrumentation should implement it
    - Will discuss more in the Specification meeting.
  - [suereth, 5min] Entity rendering cleanups / improvements
    - [https://github.com/open-telemetry/semantic-conventions/pull/2970](https://github.com/open-telemetry/semantic-conventions/pull/2970)
  - [liudmila, 3 min] Release time
    - Liudmila will cut the release
  - [james, 5min] [https://github.com/open-telemetry/semantic-conventions/pull/2867](https://github.com/open-telemetry/semantic-conventions/pull/2867)
  - [mackjmr, 5min] [https://github.com/open-telemetry/semantic-conventions/issues/2017](https://github.com/open-telemetry/semantic-conventions/issues/2017)
    - reopen - Josh will sponsor
    - Note: Issues that need AWS approvers.
  - GC elections are open, please vote if you're eligible  - [https://vote.heliosvoting.org/helios/elections/f94a7c58-990b-11f0-a16d-5270fb641b4c/view](https://vote.heliosvoting.org/helios/elections/f94a7c58-990b-11f0-a16d-5270fb641b4c/view)
