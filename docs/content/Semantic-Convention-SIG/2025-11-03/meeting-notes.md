## Meeting Notes

### Attendees
- Josh Suereth
- Liudmila Molkova
- Alexandra Konrad (Elastic)
- Armin Ruech (Dynatrace)
- Christophe Kamphaus

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
    - App - client or not [https://github.com/open-telemetry/semantic-conventions/pull/2430](https://github.com/open-telemetry/semantic-conventions/pull/2430)
    - K8s has a convention to call services apps - [https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/)
    - All solutions are not great
    - We need to at least document and have otel-community level agreement on different terms
    - AI: Trask will invite mobile folks on this call in 2 weeks
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [trask] [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15144#discussion_r2463027255](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15144#discussion_r2463027255)
    - Should schema url be the most recent version of schema that an instrumentation conforms to? I.e. keep auto-incrementing it with each new schema version even if no changes to the instrumentation?
      - Stable and unstable might have different behaviors
      - Stable:
        - It's ok to keep auto(almost)-incrementing within the same major version
  - [Liudmila]  Rename *.linux.memory to *.memory.linux
  - [Liudmila] KubeCon next week
    - let's cancel the call
  - Process:
    - blocked is "blocked by maintainer / general approver"
    - SIG blocked is different, maybe clocked on their board
