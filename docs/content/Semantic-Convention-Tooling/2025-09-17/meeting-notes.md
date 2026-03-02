## Meeting Notes

### Attendees
- Josh Suereth

### Agenda
- Triage Project board: [https://github.com/orgs/open-telemetry/projects/84](https://github.com/orgs/open-telemetry/projects/84)
- Weaver Project board: [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
- General discussion
  - [Liudmila] Live-check report [https://github.com/open-telemetry/weaver/pull/943](https://github.com/open-telemetry/weaver/pull/943)
    - To consider for next release
    - Going to cut release this week, include this next.
  - [Liudmila] Attribute groups [https://github.com/open-telemetry/weaver/issues/933](https://github.com/open-telemetry/weaver/issues/933)
    - Draft ready, looking for feedback before cleaning up
    - Public and internal
    - Sampling-relevant only on spans (can add to group_ref later if needed)
    - We'll also need span_ref, let's tackle it separately
    - Future reference in <!-- semconv {id} →
      - span.{type}
      - metric.{name}
      - event.{name}
      - entity.{type}
      - attribute_group.{id}
      - span_ref.{id}
      - metric_ref.{id}
      - event_ref.{id}
      - entity_ref.{id}
    - span_ref:
