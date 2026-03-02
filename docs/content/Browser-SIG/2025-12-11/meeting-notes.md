## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Marco Schaefer (Grafana Labs)
- Jared Freeze (Embrace)
- Wolfgang Therrien (Honeycomb)
- Benoit Zugmeyer (Datadog)
- Hugo Levy (Datadog)
- David Luna (Elastic)
- Trent Mick (Elastic)

### Agenda
- [david] Proposal of a new API to create instrumentations
  - Decouples from `InstrumentationBase` and `InstrumentationAbstract` classes
  - Fixes [#1989](https://github.com/open-telemetry/opentelemetry-js/issues/1989)
  - Will affect web instrumentations also (going to share in browser SIG)
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6163](https://github.com/open-telemetry/opentelemetry-js/pull/6163)
- [Benoit] Telemetry document/screen/page/view id proposal
  - [https://github.com/open-telemetry/opentelemetry-browser/issues/84](https://github.com/open-telemetry/opentelemetry-browser/issues/84)
- [Jared] Reminder on PR reviews already in browser: [https://github.com/open-telemetry/opentelemetry-browser/pulls](https://github.com/open-telemetry/opentelemetry-browser/pulls)
  - Trace and Span ID speedup in core: [https://github.com/open-telemetry/opentelemetry-js/pull/6209](https://github.com/open-telemetry/opentelemetry-js/pull/6209)
- [Jared] [https://pkg.pr.new/](https://pkg.pr.new/) would allow us to install any commit as a proper package (npm pack under the hood)
  - This may help solve cross-repo testing without needing to checkout and build the main repos
