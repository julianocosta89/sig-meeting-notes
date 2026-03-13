## Meeting Notes

### Attendees
- Martin Kuba (Grafana Labs)
- Jared Freeze (Embrace)
- João Oliveira (Datadog)
- David Luna (Elastic)
- Benoit Zugmeyer (Datadog)
- Hugo Levy (Datadog)
- Trent Mick (Elastic)

### Agenda
- [martin] Update on release
  - instrumentations consolidated into a single package now ([PR](https://github.com/open-telemetry/opentelemetry-browser/pull/175))
  - release workflow in progress ([PR](https://github.com/open-telemetry/opentelemetry-browser/pull/189))
- [martin] Moving instrumentations from js-contrib
  - [navigation](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/packages/instrumentation-browser-navigation)
  - [errors](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/packages/instrumentation-web-exception)
- [ted] Entities SIG
  - Would like more participation form Browser SIG
  - Treat entities design as logs, tracing, metrics. Not browser vs other components.
  - (also, vacation)
- [ted] Spec SIG could use an update at some point as well
  - What order do we plan to do everything
- [david] possible issues with “wrap”
  - Example: **user-interaction** and **browser-navigation** wrapping history API
  - Working on a repro (will create an issue with it)
  - Thoughts on wrap? look for a different way of patching?
- [benoit] `browser.url.full` vs `app.page.url.full`? [https://github.com/open-telemetry/semantic-conventions/pull/3519#discussion_r2910300533](https://github.com/open-telemetry/semantic-conventions/pull/3519#discussion_r2910300533)
  - `browser.url.full`, as `app.page` is a loaded term and can mean different things
  - We can probably go for `browser.url.full` and revisit based on user feedback
