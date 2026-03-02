## Meeting Notes

### Attendees
- Josh Suereth
- Ted Young
- Dan Dyla
- Nathan Smith

### Agenda
- [josh] New OTEP - [https://github.com/open-telemetry/opentelemetry-specification/pull/4665](https://github.com/open-telemetry/opentelemetry-specification/pull/4665)
  - Initial Discussion
    - [dmitry] Why is this required?  Is this a limitation of the SDK?
      - We should have rules for when things go in scope vs resource.  What does this mean for the Collector?
      - Why would we not just have separate resources vs. process?
      - [dan] Less duplication in OTLP data model.
      - Conceptually - Resource takes entities that survive over the course of the SDK (or collector).  Scope are things that can come and go (or we need to monitor more than one from the same SDK/observer)
        - In collector it's easy to just create resources for each.
        - minor OTLP size benefit
      - Resource-as-mutable is considered a breaking change
    - [ted] How does this solve the issue with mutable resources?
      - Instrumentation scope is lexical, this is contextual scope, feels wrong.
  - Open Comments
    - Using `{Signal}Provider.bindEntity(e)` as a means of denoting a new entity to group data. [[link]](https://github.com/open-telemetry/opentelemetry-specification/pull/4665#discussion_r2372847929)
    - Related - why should the data model change, can we still have multiple resources but new SDK tracking mechanism? [[link]](https://github.com/open-telemetry/opentelemetry-specification/pull/4665#discussion_r2372854243)
  - [dan]
    - Implied relationships?
      - If there is an entity on the scope, is there a specific implied relationship to the entities on the resource? In the call you used “runs-on”, but there could be a more generic way to phrase it that makes it more clear to everyone when you should use a scope attribute? “Nested-within” is sort of what i’m going for, but i can’t think of a good generic relationship.
    - user/instr grabbing a scope with an entity may not be aware of what is in resource. Conflict resolution?
      - If an instrumentation creates a scope with an entity, how do they know if there is already that entity on the resource? Your OTEP says it is disallowed, but it may be impossible for the instrumentation author to guarantee that.
    - Flag/config for mutable resource descriptions?
      - I was going to propose the idea that all initialization attributes (both descriptive and identifying) are put on the resource and _never change_. Changing descriptive attributes are sent over entity signal. We can have a configuration flag which allows the resource to mutate the descriptive attributes over time as an opt-in feature for people who don’t want to have to join the entity signal with other signals to see changes.
