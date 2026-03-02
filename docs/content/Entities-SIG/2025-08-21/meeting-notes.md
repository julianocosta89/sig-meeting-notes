## Meeting Notes

### Attendees
- [Daniel Dyla](mailto:dyladan@gmail.com)
- Dmitry Anoshin
- Josh Suereth

### Agenda
- [dan/josh from spec] entities to info metrics mapping (prom compatibility)
  - Is relationship a prereq for entities/info metric mapping
  - Kube_job_owner -> is this a relationship or a descriptive attribute
  - Representing owner as a descriptive attribute may cause issues
    - Owner type may vary based on which entity
  - We can likely unblock the simple _info metric by representing it as an entity
  - More complicated metrics like _owner or _state may require some relationship work in entities first
  - Entity signal implemented in collector as a log event
    - Should we represent these as a log, or does it require its own signal?
  - Relationships may be a separate set of events
- [dmitry]
  - updated [https://github.com/open-telemetry/opentelemetry-specification/pull/4594](https://github.com/open-telemetry/opentelemetry-specification/pull/4594)
  - discuss PRs like [https://github.com/open-telemetry/semantic-conventions/pull/2657](https://github.com/open-telemetry/semantic-conventions/pull/2657)
- [josh] host + cloud + vm semconv PRs
  - We should look into a mechanism to define descriptive attributes that could be on any entity.
- [josh] Update status + project
