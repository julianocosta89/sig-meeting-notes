## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Martin Kuba (Grafana Labs)
- Santosh Cheler (Cisco/ Splunk)
- David Luna (Elastic)
- Ted Young (Grafana Labs)

### Agenda
- [david] SDK 3.0 will have some breaking changes
  - Consider drop of addSpanNetworkEvents and Span#addEvent for instrumentations? [https://github.com/open-telemetry/opentelemetry-js/issues/3174](https://github.com/open-telemetry/opentelemetry-js/issues/3174)
  - [Joaquin] Currently working on the migration, should we just use logs?
  - [david] working on PoC of fetch without span events [https://github.com/open-telemetry/opentelemetry-browser/issues/259](https://github.com/open-telemetry/opentelemetry-browser/issues/259)
- [jared] InstrumentationBase refactor for discussion - purely brainstorming
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/278](https://github.com/open-telemetry/opentelemetry-browser/pull/278)
- [Ted] The browser needs to go it’s own way, and not conform to the SDK spec
  - The browser environment is too different from other runtimes, in a way that violates core assumptions in the spec. For example, there is no context object available in the browser.
  - As long as the APIs are the same, and correct OTLP is emitted on the other side of a Collector processor, it’s ok for the browser to make it’s own design decisions.
  - The tradeoff is that the Browser SIG should put extra effort into documenting both the design and reasoning behind the design choices.
