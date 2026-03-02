## Meeting Notes

### Attendees
- Jay DeLuca (Grafana Labs)
- Liudmila Molkova
- Jeremy Blythe
- Josh Suereth

### Agenda
- Open PRs
- [https://github.com/open-telemetry/weaver/pull/849](https://github.com/open-telemetry/weaver/pull/849)
  - How do we define in yaml the free-form markdown we have around signal definitions
  - Namespace is not a unit of stability
  - We can fake namespaces today without defining them in yaml in JQ/jinja
  - Moving header/footer to yaml does not seem to be useful for codegen
  - Namespace is actually a document
  - Before we proceed with this and event/span/etc registry, it's be useful to outline the end-user experience on how the docs would look like and discuss this
    - Liudmila will comment
- [https://github.com/open-telemetry/weaver/issues/844](https://github.com/open-telemetry/weaver/issues/844)
  - What'd be the litmus test to put property into annotations vs top-level structured property
    - Properties: over the wire, instrumentation sets it, changing it has sufficient impact on consumers
  - Bucket boundaries: advisory param for instrumentations, not breaking to change, optional to set
    - Should be an annotation
- [suereth] Schema v2 Planning - reminder/FYI continued discussion
  - [https://github.com/open-telemetry/weaver/pull/829](https://github.com/open-telemetry/weaver/pull/829)
    - Roll out semconv (unresolved first)?
    - How long do we need to support v1
      - Currently starting from 1.26.0
    - Should we specify version in the yaml file header
      - May complicate parsing
      - Good to be explicit
      - We'll probably need to add it eventually, but not essential today
      - Let's try having version and disjoint set of models
