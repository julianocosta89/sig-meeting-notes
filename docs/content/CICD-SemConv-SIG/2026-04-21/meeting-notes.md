## Meeting Notes

### Attendees
- Adriel Perkins (Grainger)
- Christophe Kamphaus
- Robert Pająk (Splunk)
- Alan Clucas (Pipekit)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Project Board: [https://github.com/orgs/open-telemetry/projects/171](https://github.com/orgs/open-telemetry/projects/171)
- General
  - [Robert, 10 min] Stabilization of [https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/context/env-carriers.md](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/context/env-carriers.md) (issue: [https://github.com/open-telemetry/opentelemetry-specification/issues/5040](https://github.com/open-telemetry/opentelemetry-specification/issues/5040))
    - Please review if this is ready to get stable:
      - Should it be included in the Core or can it be in Contrib?
        - We prefer to have it in Core the core repository as instrumentations want to use ut
    - I am planning reviewing/improving OTel C++ and Java implementations
    - Double check if OTel PHP implements it
    - I could also looking into implementing it in OTel .NET
    - [https://github.com/open-telemetry/opentelemetry-specification/issues/4771](https://github.com/open-telemetry/opentelemetry-specification/issues/4771)
  - [name, est. speaking time] - subject
