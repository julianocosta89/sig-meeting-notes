## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Trent Mick
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- David Luna (Elastic)

### Agenda
- [martin] Prototype of proposed packages and tree shaking
  - [https://github.com/martinkuba/opentelemetry-browser/tree/packages-prototype](https://github.com/martinkuba/opentelemetry-browser/tree/packages-prototype)
    - draft PR to see the diff: [https://github.com/open-telemetry/opentelemetry-browser/pull/170](https://github.com/open-telemetry/opentelemetry-browser/pull/170)
- [martin] Naming of packages
  - browser-sdk/browser-instrumentations vs sdk-browser/instrumentation-browser
    - one orients around browser namespace, the other around type of package (that makes sense in the opentelemetry-js context, but outside?)
- [jared] fetchLater support in exporter
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6217](https://github.com/open-telemetry/opentelemetry-js/pull/6217)
- [Ted] Session / Entity update?
