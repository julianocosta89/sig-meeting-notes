## Meeting Notes

### Attendees
- [Ted Young](mailto:theodore.young@grafana.com)(Grafana Labs)
- Josh Suereth
- Dmitry Anoshin (Splunk)

### Agenda
- Prototype in progress for browser implementation of Entities & Sessions
  - [https://github.com/martinkuba/opentelemetry-browser/pull/1](https://github.com/martinkuba/opentelemetry-browser/pull/1)
  - Questions
    - [https://github.com/open-telemetry/opentelemetry-specification/pull/4665#issuecomment-3981225836](https://github.com/open-telemetry/opentelemetry-specification/pull/4665#issuecomment-3981225836)
    - If I understand correctly, this proposal works when the caller of **forEntity()** is the only emitter of the telemetry bound to that entity. How would this work for entities that should be applied to all telemetry (all instrumentations, and user application)? Browser sessions fall into this category.
    - When a browser session is rotated, the new session entity needs to be updated for all instrumentations. Instrumentations (typically) use the globally-registered providers. They would all either need to be notified when it changes, or the global provider itself would need to allow the entity to be updated. Is this use case purposefully excluded from the proposal? Would this be part of the API or SDK?
    - How would this work with multiple entities? Is the intent to chain forEntity() calls?
    - AIs - we'll divide the problem so that browser/client can focus on log/span APIs, as metrics are not well suited to the problem.
    - [dmitryax] We may have a similar issue in the collector.
- [dmitryax]
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4836](https://github.com/open-telemetry/opentelemetry-specification/pull/4836)
  - Collector updates: [https://github.com/open-telemetry/opentelemetry-collector/pull/14660](https://github.com/open-telemetry/opentelemetry-collector/pull/14660) and [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46542](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46542)
