## Meeting Notes

### Attendees
- Pablo Baeyens (Datadog)
- Braydon Kains (Google)
- Dmitry Anoshin (Splunk)
- Igor Peschinskii (Datadog)

### Agenda
- Recap of [host.id](http://host.id) discussion?
  - We will have different entities for host and cloud providers
  - is-a relationship and how you would join the host and another entity specific to a cloud provider makes sense to Entities SIG
  - host.id value remains contentious from an Entities SIG
    - Actual implementation on the resource detection processor remains weird since you would have to implement multiple detectors
  - We need to clarify the Entities Data Model but that's not a blocker for formalizing [host.id](http://host.id) value and stabilizing
  - "There must be another entity associated with the resource"
- (Pablo) Stabilizing attributes:
  - system.filesystem.type
  - system.filesystem.mountpoint
    - Maybe worth checking that this makes sense in a Windows context
  - system.filesystem.mode
- [Dmitry]
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/49162](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/49162)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/49325](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/49325)
