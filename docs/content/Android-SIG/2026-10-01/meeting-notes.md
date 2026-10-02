## Meeting Notes

### Attendees
- Hanson Ho (Embrace)
- ‘Jamie Lynch (Embrace)
- Vishwan (Grafana)
- Ben (Grafana)
- Jason Morris (Embrace)
- Cesar (Elastic)

### Agenda
- [Vishwan] - [https://github.com/open-telemetry/opentelemetry-android/pull/2078](https://github.com/open-telemetry/opentelemetry-android/pull/2078)
- [https://github.com/open-telemetry/opentelemetry-android/pull/2011](https://github.com/open-telemetry/opentelemetry-android/pull/2011)
  - Action: feedback on PR welcome, please take a look
- [Hanson Ho] Federated semantic conventions
  - Client-side federated registry and about to be ready for new conventions: [https://github.com/open-telemetry/semantic-conventions-client-side/](https://github.com/open-telemetry/semantic-conventions-client-side/)
  - Migration includes the following steps:
    - Port existing registry and tooling to v2
      - Do we publish it as a versioned artifact? I’m thinking no but we can discuss
    - Import client-side registry so our code generation can consume conventions from it
    - Move conventions defined in our registry that we want to make public semantic conventions over to client-side (i.e. deprecate in this registry and point to new definitions in client-side).
      - What happens in this project will depend on whether the conventions were changed during the migration
        - Keep convention name and semantic meaning
          - Define directly in client-side registry - no change to instrumentation needed
        - Change convention name or redefine meaning
          - We have to decide whether we provide a fall-back mode to write the attributes (name and values) the old way or just document the change.
          - Cesar brought up an interesting point about creating a new major version 2.x where we drop all old stuff and only rely on instrumentation where all public attributes are defined in semantic conventions - a big reset. We can lump in features and Kotlin API changes to make it enticing and worthwhile.
      - For attributes that are not in our registry, we should move them into it and take the appropriate migration path
      - For conventions we don’t want to make public (e.g. diagnostics, not useful, etc), we should make them internal
    - Existing infra to generate source code from the imported registries can stay the same and not change for the time being
  - Once client-side is ready to accept new conventions, the workflow to add instrumentation that uses new conventions should be as follows:
    - Define new conventions in client-side
    - Wait for client-side to make a new release and update this project to depend on it
    - Consume newly generated artifacts, which will create an implicit dependency on that version of the client-side semantic convention
      - Until a new published client-side version is ready to be consumed, just declare it as an internal convention first so the same source code is generated and can be consumed as if it were defined in client-side. Just make sure you don’t release it until the convention is moved - or you’ll have to do the same migration as above.
  - Action Items:
    - [Hanson] Put up PR to migration registry to v2 and pull in client-side when it’s ready
    - [Hanson] Create issues to track and discuss the migration of various clusters of conventions (e.g. per component/instrumentation, per namespace, etc.)
