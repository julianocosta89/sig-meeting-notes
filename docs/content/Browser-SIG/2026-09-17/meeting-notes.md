## Meeting Notes

### Attendees
- David Luna (Elastic)
- Martin Kuba (Grafana Labs)
- Cleo Schneider (Google/Firebase)
- Joaquin Diaz (Palo Alto Networks)
- Jared Freeze (Palo Alto Networks)
- Maxime Quentin (Datadog)
- Abinet Debele (Cisco)
- Michael Bushe (Mindful Software)
- Wolfgang Therrien (Honeycomb.io)

### Agenda
- [martin] Update on sem conventions
  - [PR in progress](https://github.com/open-telemetry/opentelemetry-browser/pull/404)
  - [New repository](https://github.com/open-telemetry/semantic-conventions-client-side) for client-side sem conv being bootstrapped
- [david] ignore export URLs
  - [https://github.com/open-telemetry/opentelemetry-browser/blob/main/sandbox/src/otel.ts#L158-L175](https://github.com/open-telemetry/opentelemetry-browser/blob/main/sandbox/src/otel.ts#L158-L175)
  - IMO shouldn’t be necessary
    - Suppress tracing for spans might be the way [https://github.com/open-telemetry/opentelemetry-js/pull/6948](https://github.com/open-telemetry/opentelemetry-js/pull/6948)
    - It might work for correlated logs too
    - Last case is no fetch/XHR instrumentations and resource timings active
  - Decision: by default do not collect this info. In future allow users to enable it in debug/diagnostics mode
- [martin] Validating export URLs [PR](https://github.com/open-telemetry/opentelemetry-browser/pull/357)
  - one pending [comment](https://github.com/open-telemetry/opentelemetry-browser/pull/357/changes#r3968078361) needs decision
- [jared] Core PR for fetch keepalive needs review [https://github.com/open-telemetry/opentelemetry-js/pull/7070](https://github.com/open-telemetry/opentelemetry-js/pull/7070)
- [jared] who’s going to KubeCon?
- [maxime] NavigationTimingInstrumentation‘s regression since the 10th of Sept
  - refactors of the instrumentation registration need to be merged first
  - Fix the bug of the instrumentation before the refactor
