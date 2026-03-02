## Meeting Notes

### Attendees
- Josh Suereth
- Tyler Yahn
- Daniel Dyla
- Dmitry Anoshin

### Agenda
- [suereth] Specification PR: [https://github.com/open-telemetry/opentelemetry-specification/pull/4565](https://github.com/open-telemetry/opentelemetry-specification/pull/4565)
  - Should we have an API?
    - Benefits
      - Codegen / Weaver becomes easier
      - Stability for Resource detection
    - Concerns
      - How to have a stable Resource before sending signals?
    - Strawman:
      - *LoggerProvider -> GetLogger, MeterProvider -> GetMeter, TracerProvider -> GetTracer*
      - ResourceProvider
        - GetResource() -> Resource
      - api.Resource
        - RegisterEntityDetector(EntityDetector, options)  *(similar to async metric instruments)*
        - *[future] For Browser/Client SIG*
          - AddEntity(Entity)
          - ReplaceEntity(Entity)
          - RemoveEntity(Entity)
      - api.EntityDetector
        - DetectEntities() -> Set<Entity>
      - api.Entity
        - schema_url
        - type
        - id
        - description
    - Discussion
      - Motivation: Do we want this?
        - Entity data *is* telemetry data.  API is how we collect telemetry in OpenTelemetry.
        - Could have had resource there first, but didn't expect it to change.  This expectation changes how things work.
        - SDK should be mainly configuration, not data.
        - Possible future use cases: Could even have this in a database driver that describes the database you're interacting with.
      - Actual proposed API
        - Remove "register entity detector"
        - Instead, instrumentation calls "add entity".
      - Is Async option required?
        - start-span is synchronous API.
        - Instrumentation determines when to call it.
        - recommend starting without async API.
      - Codegen from Weaver
- Other Topics
- Triage / Next steps
  - [https://github.com/orgs/open-telemetry/projects/85](https://github.com/orgs/open-telemetry/projects/85)
