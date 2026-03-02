## Meeting Notes

### Attendees
- Trask Stalnaker (Microsoft)
- Janhvi (Google)
- Neil Yashinsky ( ContextCore)

### Agenda
- PRs up for review:
  - jpkroehling - [https://github.com/open-telemetry/semantic-conventions/pull/3268](https://github.com/open-telemetry/semantic-conventions/pull/3268)
    - Previous action item: Janhvi and Eimear to add use cases of this attribute on the PR
    - jpkroehling: I’d love to get an initial review of this PR. I’d then rebase it to fix the merge conflicts. If there’s anything else pending (use cases?), I can also add them based on what I’ve seen in the real-world.
    - Eimear: Putting something together internally at the moment but the primary use-cases for owner we have would be billing, business ownership, incident response, development team.
    - Janhvi:
      - Defines a generic service.owner with simple attributes like name, url, and contact. It implies a single "owner". Does not distinguish what kind of owner it is.
        - Type of owners:
          - developer_owners: The team responsible for coding and development.
          - operator_owners: The team responsible for runtime integrity and operations.
          - business_owners: The team responsible for quality and business expectations.
    - What is the SOT of this data? More use cases around each category?
  - [https://github.com/open-telemetry/semantic-conventions/pull/3348](https://github.com/open-telemetry/semantic-conventions/pull/3348) - Move service.criticality to opt-in
    - Since it is a descriptive attribute; adding this attribute may not be a breaking change
    - When to use opt-in
      - Not a common use case in opentelemetry
      - High cardinality
      - Sensitive pii info
    - Josh to respond back on the PR
  - [https://github.com/open-telemetry/semantic-conventions/pull/3253](https://github.com/open-telemetry/semantic-conventions/pull/3253) - Service.instance.id stability - needs reviewers
  - [https://github.com/open-telemetry/semantic-conventions/pull/3352](https://github.com/open-telemetry/semantic-conventions/pull/3352) - service.peer.name / service.peer.namespace stabilization
  - [https://github.com/open-telemetry/semantic-conventions/pull/3254](https://github.com/open-telemetry/semantic-conventions/pull/3254) - Stabilize service.namespace - needs reviewers
- [Arnav] Discuss [Standardization of Deployment Environment Semantics in OpenTelemetry](https://docs.google.com/document/d/1uYTLqwRrPJqmTcS61IjBbsDwgfZS50tX4Fzns_pojMg/edit?tab=t.0)
- [Liudmila Molkova ] We’re starting to put together a **Semantic Conventions roadmap for 2026** and would love input from your SIG.
  - In particular:
  - What do you expect to ship in 2026?
  - Are there areas you're ready to stabilize in 2026?
  - Are there things you need from other parts of the semconv community?
