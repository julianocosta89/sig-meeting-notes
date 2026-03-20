## Meeting Notes

### Attendees
- Martin Kuba (Grafana)
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Maxime Quentin (Datadog)
- Hugo Levy (Datadog)
- Christopher Arredondo (MercadoLibre)
- David Luna (Elastic)

### Agenda
- [martin] Quick announcement: we had a first release last week!
  - [https://www.npmjs.com/package/@opentelemetry/browser-instrumentation](https://www.npmjs.com/package/@opentelemetry/browser-instrumentation)
- [martin] page URL attribute
  - [https://github.com/open-telemetry/semantic-conventions/pull/3519](https://github.com/open-telemetry/semantic-conventions/pull/3519)
  - any objections to merging this?
  - model page context as an entity?
- [david] follow up on moving instrumentations
  - All the browser ones?
  - **Action:** Let’s discuss it in an issue.
- [david] patch issue
  - [https://github.com/open-telemetry/opentelemetry-browser/issues/204](https://github.com/open-telemetry/opentelemetry-browser/issues/204)
  - Disabling an instrumentation can break others
    - Re-apply patches?
    - Tracing channel like?
    - **Note:** considered to completely remove unpatch. So maybe the way forward is just disable but not unpatch
- [martin] End-to-end prototype / demo
  - sessions as entities (page or others as well?)
  - metrics from events
  - SDK / configuration layer
  - include demo app, collector, backend
  - protocol optimization?
  - browser-optimized API
