## Meeting Notes

### Attendees
- Trask Stalnaker (Microsoft)
- Josh Suereth (Google)
- Janhvi (Google)
- Kartik (Google)
- Joao Grassi (Dynatrace)

### Agenda
- (5 min) Welcome & Introductions
- SIG Scope & Phases overview
  - [janhvi] Phases:
    - Phase 1: Extend the [Service entity](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/registry/attributes/service.md) with new attributes (service.owner, service.criticality).
    - Phase 2: Stabilize [deployment.environment.name](http://deployment.environment.name) attribute and finish model for deployment related entities.
    - Phase 3: Formulate a plan for tagging resources with sensitivity labels, and interaction with other telemetry.
  - [suereth] Scoping questions - We need to have strong answers to the following:
    - What is a service?  When is an attribute a service attribute vs. e.g. a k8s.service attribute? Who "owns" the service entity?
    - AI(suereth): PR to migrate service.instance / service / service.namespace entity split.
    - What is a deployment?  When is an attribute a deployment attribute vs. e.g. a k8s.deployment? Who "owns" the deployment entity?
      - Probably the only entity we need to stabilize is "deployment.environment"
      - AI(joao) - Define [deployment.environment.name](http://deployment.environment.name) as an *enum* where we can reliably understand "production" vs. "test" etc.  Open an issue for discussion and broadcast across Semconv community
        - Created the issue: [https://github.com/open-telemetry/semantic-conventions/issues/2910](https://github.com/open-telemetry/semantic-conventions/issues/2910)
  - [suereth] Service + Deployment backlog issues: [https://github.com/orgs/open-telemetry/projects/168](https://github.com/orgs/open-telemetry/projects/168)
- Phase 1 Deep Dive: Stabilizing Service Entity
  - [suereth] Concerns around stabilizing
    - service.namespace
    - service.instance.id - [https://github.com/open-telemetry/semantic-conventions/issues/2880](https://github.com/open-telemetry/semantic-conventions/issues/2880)
      - Confirm where this is implemented.
- Phase 1 Deep Dive: Extending Service entity
  - Proposed attributes: `service.owner`, `service.criticality`
  - Use cases & rationale
  - Naming discussion & feedback
- Risks, Concerns, and Open Questions
  - Reservations about naming or adoption?
- Wrap-up & Next Steps
