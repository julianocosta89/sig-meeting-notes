## Meeting Notes

### Attendees
- [John Watson](mailto:john.watson@sublimesecurity.com)(Sublime Security)
- Jonathan Halliday (IBM)
- Trask Stalnaker (Microsoft)
- Jason Plumb (AppDynamics)
- Jay DeLuca (Grafana Labs)
- Jack Shirazi (Elastic)
- Pranav Sharma (Google)
- Peter Findeisen (Cisco)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana Labs)
- Lauri Tulmin (Splunk)
- Prasad Sawool (Ascendion)

### Agenda
- Java Instrumentation v3 review
- [jack] Last call for 1.67.0 release tomorrow
  - I may try to get this merged [https://github.com/open-telemetry/opentelemetry-java/pull/8854](https://github.com/open-telemetry/opentelemetry-java/pull/8854)
  - Trying to land entities prototype [https://github.com/open-telemetry/opentelemetry-java/pull/8464](https://github.com/open-telemetry/opentelemetry-java/pull/8464)
    - Latest
      - No opt in / opt out - entities are serialized to OTLP whenever entity-aware resources are present
      - Nothing happens on merge, but users can start specifying `OTEL_ENTITIES` and instrumentation can start emitting entity aware resources
    - Rules of thumb
      - Later writes win, whether attributes come from an entity or an ordinary write.
      - When incoming and existing entities have the same type, matching IDs and schemas, merge descriptions. Different IDs or schemas replace the whole old entity, including all its attributes.
      - When an incoming entity takes attributes from a different entity type, or an ordinary write changes any entity-owned attribute, remove the affected association and keep its non-conflicting attributes as ordinary attributes. An unchanged ordinary write preserves association. This includes descriptive attributes, not just identifiers. Removing any identifying attribute also removes the association.
      - Existing resource APIs operate on all attributes. Filtering removes selected attributes and preserves the rest; it does not bypass the identity rule.
      - Log at `WARNING` whenever an entity is modified / deleted
- [trask] [Adopt Towncrier for release notes](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/20437)
- [gregor] FYI - I’ve joined the Grafana Beyla team and will work mostly on [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation) in the future
- Java Contrib
  - Create retirement and component owner policy
  - - prometheus-client-bridge
  - - runtime-attach
  - - noop-api
  - - micrometer-meter-provider
  - - jfr-events
