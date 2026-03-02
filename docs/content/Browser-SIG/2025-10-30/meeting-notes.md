## Meeting Notes

### Attendees
- Ted Young (Grafana Labs)
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Daniel Dyla (Dynatrace)
- Martin Kuba (Grafana Labs)
- Wolfgang Therrien (Honeycomb.io)
- Dan Gomez Blanco (New Relic)
- Elliot Kirk (Grafana Labs)
- Abinet Debele (Cisco)
- David Luna (Elastic)

### Agenda
- [Joaquin] [https://github.com/open-telemetry/semantic-conventions/pull/2992](https://github.com/open-telemetry/semantic-conventions/pull/2992)
  - Adding a specific event for clicks instead of a generic user action event
  - Add triage accepted label?
  - Should we extend app.widget.click?
  - Should we use CSS selectors instead of XPath? ✅
- [Joaquin] Unit testing framework
  - Using vitest with jsdom here [https://github.com/open-telemetry/opentelemetry-browser/pull/35](https://github.com/open-telemetry/opentelemetry-browser/pull/35)
  - [vitest-browser](https://vitest.dev/guide/browser/) ?
    - If not, web-test-runner + mocha + chai?
  - Should we run against headless browsers for all tests or only when using specific APIs?
    - Set up vitest browser
- [Martin] Documenting use cases for the navigation event
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/41](https://github.com/open-telemetry/opentelemetry-browser/pull/41)
- [Ted] Quick review of open semconv issues tagged with browser:
  - [https://github.com/open-telemetry/semantic-conventions/issues?q=state%3Aopen%20label%3Aarea%3Abrowser](https://github.com/open-telemetry/semantic-conventions/issues?q=state%3Aopen%20label%3Aarea%3Abrowser)
