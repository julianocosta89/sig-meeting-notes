## Meeting Notes

### Attendees
- Sven Cowart (ElastiFlow)
- Liudmila Molkova (Google)
- Armin Ruech (Dynatrace)
- Trask Stalnaker
- Daniel Dyla (Dynatrace)
- Surbhi A (Cisco)
- Yordis Prieto (Straw Hat, LLC)
- Rob Cowart (ElastiFlow) - joined late, sorry

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/proje](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - [cts/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- [Sven]  [Proposal: New pattern for source/destination attribute ordering](https://github.com/open-telemetry/semantic-conventions/issues/3791)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4906](https://github.com/open-telemetry/opentelemetry-specification/pull/4906)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4815](https://github.com/open-telemetry/opentelemetry-specification/pull/4815)
  - [https://github.com/open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)
- [Surbhi A] Discuss semantic conventions PR - [https://github.com/open-telemetry/semantic-conventions/pull/3727](https://github.com/open-telemetry/semantic-conventions/pull/3727)
- [Liudmila, 5-15 min] Start migration to v2 schema
  - Liudmila will send skill to otel-weaver-packages
  - We can update conventions one-by-one
  - Need help migrating individual areas
  - Mostly trivial, but there might be bugs
  - Key changes:
    - Syntax simplifications
    - We can definite span/metrics refinements
    - Less/no nesting for attribute groups
