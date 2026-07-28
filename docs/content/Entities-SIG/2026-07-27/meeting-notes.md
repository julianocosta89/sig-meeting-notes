## Meeting Notes

### Attendees
- Josh
- Daniel
- Michele
- Krajo

### Agenda
- [krajo] Thinking about left-hand navigation. How will that work on the entities model ? How do I know which attribute is the "display" name?  I guess I can know the levels:
  - host
    - vm
      - container
  - But then when I click on host, how do I select which hosts to filter on? From the [examples](https://opentelemetry.io/docs/specs/otel/entities/data-model/#examples-of-entities) it is tempting to give a selection of <entity-type>.name , but why not <entity-type>.displayname or whatever? I doubt people would look at the identifying attributes. One could just list all the attributes and let the user pick the one they want (and we probably need to be able to do that), but it would be nice to be able to give a sensible default.
  - Possibly have a SHOULD rule on having .name or .displayname or something like that?
  - josh: model needs to be self contained -> ToString() ? This operator would be external to OTLP?
  - daniel: Should display name be specified? Is this a product/backend decision?  Would a product call it "host" or "virtual host"?  Not sure it's useful to be sent over the wire.  We could recommend it somewhere / need a way to refer to things in prose.
  - For prometheus - we don't want prometheus to maintain a huge list of rules for how to display-name entities.  We need something that makes sense and is reasonable.
    - krajo: for now we're ok picking the one with "name" in it or first attribute if none - good enough
    - krajo: later maybe ToString can be part of semantic conventions - we'll have to deal with it later anyway for promql transforms for accessing historic data
- [suereth] latest spec PRs
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5057](https://github.com/open-telemetry/opentelemetry-specification/pull/5057)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5147](https://github.com/open-telemetry/opentelemetry-specification/pull/5147)
  - Issue with SchemaURL - [https://github.com/open-telemetry/opentelemetry-specification/issues/3361](https://github.com/open-telemetry/opentelemetry-specification/issues/3361)
  - AI - Add SchemaURL to Entity datamodel.
  - AI - Update plan of record
    - Revert schema_url algorithm on Resource to match previous behavior (or whatever we decide it needs to do going forward).
    - Update docs to recommend ignoring Resource.schema_url and use EntityRef.schema_url instead.
  - [https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/4815-semantic-conventions-schema-v2.md](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/4815-semantic-conventions-schema-v2.md)
