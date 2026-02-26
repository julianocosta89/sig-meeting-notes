## Meeting Notes

### Attendees
- Josh Suereth
- Dmitry Anoshin

### Agenda
- [suereth] Project check-in and open items
  - [https://github.com/orgs/open-telemetry/projects/85](https://github.com/orgs/open-telemetry/projects/85)
  - Rework "definition of done"
    - Specification for SDK detecting entities
    - at least three SDKs producing OTLP w/ entities, and detectors being focused around entities
    - Collector able to use entities in processors to handle local vs. remote issue -
- [dmitry] Entity Relationship model
  - Concerns are addressed
  - We can add "delta update" events later, in non-breaking way
  - Do not need a mechanism to aggregate changes and send them in a batch.
