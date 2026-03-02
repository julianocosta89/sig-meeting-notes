## Meeting Notes

### Attendees
- [Daniel Dyla](mailto:dyladan@gmail.com)
- Christos Markou (Elastic)
- Christophe Kamphaus
- Trask Stalnaker (Microsoft)
- Armin Ruech (Dynatrace)
- Alexandra Konrad (Elastic)
- Sam Xie (Cisco)
- Josh Suereth *[joining late]*

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [trask] [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14024](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/14024)
    - Should Baggage be propagated when consumer span is only linked to producer span?
  - [sam, 1m] please review [https://github.com/open-telemetry/semantic-conventions/pull/2363](https://github.com/open-telemetry/semantic-conventions/pull/2363)
  - [suereth] Entities Modeling guide: [https://github.com/open-telemetry/semantic-conventions/pull/2328](https://github.com/open-telemetry/semantic-conventions/pull/2328)
    - Refinement vs. Extend
      - Creating a new group that is the same as another, but optimised for a specific vendor or implementation.
      - See: [https://github.com/open-telemetry/weaver/issues/785](https://github.com/open-telemetry/weaver/issues/785)
  - [suereth] Please review: [https://github.com/open-telemetry/semantic-conventions/pull/2378](https://github.com/open-telemetry/semantic-conventions/pull/2378)
  - [braydonk] Question about dynamic units
    - CPU utilization
      - Leaning toward recommending against using it
      - Different windows (not matching the collection interval)
  - [trask] [https://github.com/open-telemetry/semantic-conventions/pull/2317](https://github.com/open-telemetry/semantic-conventions/pull/2317)
    - Can we simplify to just no pluralization
    - We need k8s folks to provide feedback, pushing to the next meeting
  - [braydonk] Best place to put design guidance for status metrics
