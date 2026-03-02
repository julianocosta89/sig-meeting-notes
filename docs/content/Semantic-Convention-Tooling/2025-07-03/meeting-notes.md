## Meeting Notes

### Attendees
- Josh
- Laurent
- Liudmila

### Agenda
- Schema v2 Planning
  - Resolution process for trees: [https://github.com/open-telemetry/weaver/blob/main/docs/specs/multi-registry/multi_registry.md](https://github.com/open-telemetry/weaver/blob/main/docs/specs/multi-registry/multi_registry.md)
  - Lidumila's demo: [https://github.com/open-telemetry/semantic-conventions/pull/2469](https://github.com/open-telemetry/semantic-conventions/pull/2469)
    - Problems found so far:
      - diff data has no stability properties, not possible to generate stable one
      - a lot of meaningless null in resolved schema
        - having `span_kind: null` on metric is not great
        - *AI - Remove null values in resolved schema.*
      - I'm not sure if lineage is really important on the resolved schema, do we actually need it checked in?
        - Can be pretty big
        - Where is it used?
          - linking to attribute registry (e.g. [here](https://github.com/open-telemetry/semantic-conventions/blob/83b55440146a1978699bc79b1c88b8a73085478c/templates/registry/markdown/snippet.md.j2#L24))
          - UI features
          - If we publish it for the world - where do we put it?
        - *AI - Let's open a ticket to figure out how to optimise it.*
          - Thinking of this like a "symbol table"
      - some problems with toyaml filter in jinja
        - *AI - Will open a bug.*
      - some discrepancies in weaver commands
        - *AI - Need to sort out consistency in weaver, existing open bugs we can sort out.*
    - Splitting "stable" from "unstable" registry components
      - {version} vs. {version}-dev for semconv
      - What does SchemaURL look like on the wire?
        - If I'm using {version}-dev, but stable things in it, do I get {version}-dev or {version}?
      - AI - Let's keep these completely separate registries for now
        - AI - add stability filtering in weaver (in JQ)
        - Evaluate friction reduction later.
  - Tracking Issue: [https://github.com/open-telemetry/opentelemetry-specification/issues/4427](https://github.com/open-telemetry/opentelemetry-specification/issues/4427)
