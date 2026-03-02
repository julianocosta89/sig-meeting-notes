## Meeting Notes

### Attendees
- James Thompson
- Liudmila Molkova (Microsoft)
- Ruediger Schulze (IBM)
- Josh Suereth (Google)
- Joao Grassi (Dynatrace)
- Armin Ruech (Dynatrace)
- Matthew Hensley (Grafana Labs)
- Alexandra Konrad (Elastic)
- Nick Moore (Grafana Labs)
- Sam Xie (Splunk)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [trask, 5 min] [https://github.com/open-telemetry/semantic-conventions/issues/2505](https://github.com/open-telemetry/semantic-conventions/issues/2505)
    - Options: normalize in tooling vs enforce with the policy
    - Trask will send a PR
  - [james, 5min] span kind -> is there a use case for supporting implementor changing the span kind, or should it be handled like instrumentation type
    - Span kinds is sometimes SHOULD sometimes MUST
    - Client and internal sometimes are interchangeable (in memory databases)
      - Same with server and internal (multiple server layers, background jobs)
    - Span kind need more guidance (are nested server/client allowed)
    - Dan to create/find issue on nested spans
  - [james, 5min] hw.vendor vs hw.vendor.name as well as hw.model vs hw.model.name vs hw.description -> [move all hardware metrics to their own yaml files by trisch-me · Pull Request #2380 · open-telemetry/semantic-conventions](https://github.com/open-telemetry/semantic-conventions/pull/2380)
    - This PR is moving md to yaml, no new scope should be added
    - Substantial changes to hardware should be done via a HW SIG following project proposal [https://github.com/open-telemetry/community/blob/main/project-management.md](https://github.com/open-telemetry/community/blob/main/project-management.md)
  - [james, 10min] Documentation registry
    - Registry of events -> [Create an event registry #2382 by thompson-tomo · Pull Request #2464 · open-telemetry/semantic-conventions](https://github.com/open-telemetry/semantic-conventions/pull/2464)
      - Let's not split events and logs - there are no logs in semconv
      - MD has more context, we need to preserve it
        - Req level
        - versioning/warning notes
        - Examples?
      - Let's keep working on the PR and try to resolve big questions
  - [suereth, 5 min] Moving "how to contribute": [https://github.com/open-telemetry/semantic-conventions/pull/2501](https://github.com/open-telemetry/semantic-conventions/pull/2501)
    - Adding more guides over time.
  - [liudmila, 5 min] Prototyping requirements for substantial contributions
    - Merged!
    - Joao to follow up on triage/general project management proposal
