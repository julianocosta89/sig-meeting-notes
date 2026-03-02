## Meeting Notes

### Attendees
- Josh
- Dan

### Agenda
- [josh] Meeting times - Expand time we have together
- [josh] OTEP updates + comments:
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4316](https://github.com/open-telemetry/opentelemetry-specification/pull/4316)
  - Added churn protection
  - Added timeout protection
  - Added breaking change description and plan
  - Concerns over mutable resource and breaking changes
    - Resource remain immutable after "initialization"
    - InstrumentationScope now allows EntityRef + entities for its attributes.
    - When dealing with "mutable" entities in OpenTelemetry, we pass them in when grabbing Meter/Tracer/Logger/etc.
      - MeterProvider p = …… <- this discovers the immutable resource.
      - p.getMeterFor("meter name", Entity….{session}....) <- This obtains a scope that will report against a mutable entity.  That entity is considered bound / internal / scoped to the immutable resource entities.
    - Problem: We need a way to allow "Scope cleanup"
      - When an entity is "killed" the instrumentation scope needs to be cleaned (e.g. removing in-memory storage for metrics).
    - Problem: When instrumentation gets meter for session, instrumentation needs to pass an entity.
      - **Option 1 - Construct itself?**
      - Option 2 - Ask for it from EntityProvider?
    - Problem: What if the Scope wants to report an entity that is already in the resource?
      - Option 1 - Allow, backend allows
      - Option 2 - Prevent this.
- … your topics here …
- [josh] [LAST TOPIC] project board updates: [https://github.com/orgs/open-telemetry/projects/85](https://github.com/orgs/open-telemetry/projects/85)
  - Will add counter-OTEP
