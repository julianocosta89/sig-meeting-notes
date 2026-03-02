## Meeting Notes

### Attendees
- [Michael Safyan](mailto:michaelsafyan@google.com) (Google)
- Trask Stalnaker (Microsoft)
- Liudmila Molkova (Grafana Labs)
- Joao Grassi (Dynatrace)
- Josh Suereth
- Armin Ruech (Dynatrace)
- Christophe Kamphaus
- Matthew Hensley (Grafana Labs)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [Gregor and Liudmila, 10 min]  Semconv and declarative config [https://github.com/open-telemetry/semantic-conventions/pull/2504](https://github.com/open-telemetry/semantic-conventions/pull/2504)
    - The proposal is to own declarative config in semconv
    - Liudmila to bring it up on the spec call - we should not duplicate config in two places
    - Trask to ask  Gregor if he could propose a way to formally capture config in the yaml
  - [Michael Safyan, 5 min] Minor AppHub doc update: [https://github.com/open-telemetry/semantic-conventions/pull/2663](https://github.com/open-telemetry/semantic-conventions/pull/2663)
    - AI(michaelsafyan): To add the *.yaml changes, also, to the PR
    - Let's document that a group of attributes is applicable to any span
  - [Michael Safyan, 5 min] GCP client/server spans: [https://github.com/open-telemetry/semantic-conventions/pull/2384](https://github.com/open-telemetry/semantic-conventions/pull/2384)
  - [Liudmila, 1 min] Release is still blocked, some changelog linting issues
    - [https://github.com/open-telemetry/semantic-conventions/actions/runs/17212678905/job/48828289198](https://github.com/open-telemetry/semantic-conventions/actions/runs/17212678905/job/48828289198)
  - [Liudmila, 5 min] SQL commenter [https://github.com/open-telemetry/semantic-conventions/pull/2495](https://github.com/open-telemetry/semantic-conventions/pull/2495)
    - Propagators
      - Normally give carrier and headers, propagator injects headers into carrier
      - After propagator runs, instrumentation doesn’t do anything else
      - In SQL commenter, you want to have map as carrier
        - Propagator injects into the map
        - Then instrumentation serializes it into String (updating the query)
      - Liudmila to create spec issue and link to this PR
  - [10 min] Revive event.name [https://github.com/open-telemetry/semantic-conventions/issues/2597](https://github.com/open-telemetry/semantic-conventions/issues/2597)
    - Event to metric pipelines ([event.name](http://event.name) is good)
    - [metric.name](http://metric.name) also
    - Generally useful in the future
  - [ 5min] Briefs on enum members in yaml [https://github.com/open-telemetry/semantic-conventions/pull/2560](https://github.com/open-telemetry/semantic-conventions/pull/2560)
