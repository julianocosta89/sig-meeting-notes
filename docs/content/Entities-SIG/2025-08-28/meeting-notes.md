## Meeting Notes

### Attendees
- Josh Suereth

### Agenda
- Dmitry's PR in SPEC - [https://github.com/open-telemetry/opentelemetry-specification/pull/4594](https://github.com/open-telemetry/opentelemetry-specification/pull/4594)
  - Action - defer to sections that don't exist which have TODOs.
- [https://github.com/open-telemetry/opentelemetry.io/pull/7386](https://github.com/open-telemetry/opentelemetry.io/pull/7386)
  - Resource
    - A collection of entities (link to concept) or attributes (link to concept) that identify or describe a physical or logical object that produces telemetry.
  - Entities
    - A collection of attributes that identify and describe a physical or logical object.  Entities are typically associated with telemetry, e.g. a CPU entity describes a physical CPU, a service entity describes a logical grouping of processes that compose an HTTP or other service.
- [suereth] Updated spec
  - What should we do when resource changes in SDK?
    - Metrics - flush old and create new
    - Traces - Probably want resource state from span-start
      - span-end could work
      - export worst option.
    - Event / Log - Just pull current ?
- [suereth] Update project status
  - Discussion on API vs. SDK and how to report against different resources simultaneously
