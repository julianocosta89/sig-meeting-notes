## Meeting Notes

### Attendees
- Josh Suereth
- Dmitry Anoshin

### Agenda
- [dmitryax] Entity events spec [https://github.com/open-telemetry/opentelemetry-specification/pull/4836](https://github.com/open-telemetry/opentelemetry-specification/pull/4836)
  - AI - Let's look into Relationships as their own thing and determine which way we want to model this.
  - Do we allow relationships to change without changing the entity?  I.e. what's the cost of removing one relationship for an entity?
  - What do we do if there's a huge amount of state we're tracking?
    - In Collector - don't send all cluster state.
    - E.g. send information every 15min
    - If pod didn't change, don't send on the next sync.
  - How do we deal with local-ids?
    - e.g. can I have an entity relationship *between* entities in K8s clusters.
  - Hard problem to figure out
    - Load balance balancing between two k8s.service's running in two k8s.clusters.  The "global" load balancer needs to point at two different clusters and the services in there.
  - Will this use instrumentation scope? - would be needed for schema version.
- [suereth] Merge Algorithm: [https://github.com/open-telemetry/opentelemetry-specification/pull/4768](https://github.com/open-telemetry/opentelemetry-specification/pull/4768)
