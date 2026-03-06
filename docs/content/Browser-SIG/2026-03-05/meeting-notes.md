## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Benoit Zugmeyer (Datadog)
- Maxime Quentin
- Martin Kuba (Grafana Labs)
- Marco Schaefer (Grafana Labs)
- David Luna (Elastic)

### Agenda
- [Maxime] Instrument browser app screen url #174
  - [https://github.com/open-telemetry/opentelemetry-browser/issues/174](https://github.com/open-telemetry/opentelemetry-browser/issues/174)
  - Notes:
    - browser.* namespace might be too specific for react native as an example but browser.url.full seems the best option so far
      - Would also enable such field addition like browser.navigation.type
      - Question about which browser.url.full do you use for the span if it changes ?
    - app.url does not really fit browser either
    - Question to bring to the client SIG ?
- [Martin] Release/publish process
  - request for review - consolidate instrumentations into a single package
    - [https://github.com/open-telemetry/opentelemetry-browser/pull/175](https://github.com/open-telemetry/opentelemetry-browser/pull/175)
  - please review last proposal for adding an `@opentelemetry/browser` package
    - [https://github.com/open-telemetry/opentelemetry-browser/issues/131](https://github.com/open-telemetry/opentelemetry-browser/issues/131)
- [Ted] Session management and entities
  - New design was focused on metrics, which we don’t need
  - We’re just going to build what we need as a demo and present it to the community to finish the specification.
