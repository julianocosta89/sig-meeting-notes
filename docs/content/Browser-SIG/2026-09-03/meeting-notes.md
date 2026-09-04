## Meeting Notes

### Attendees
- Jared Freeze (Palo Alto Networks)
- Joaquin Diaz (Palo Alto Networks)
- David Luna (Elastic)
- Trent Mick (Elastic)
- Maxime Quentin (Datadog)
- Catalina Syddall (Ollygarden)

### Agenda
- [jared] Should we commit to snake_case in browser semconv or take keys from the client as they come like Web Vitals’ `navigationType` `largestTarget` etc
  - Convert all to underscore, explicit semconv keys
- [david] [https://github.com/open-telemetry/opentelemetry-browser/pull/415](https://github.com/open-telemetry/opentelemetry-browser/pull/415)
  - `registerInstrumentations` nuances. Should an instrumentation with {enabled: false} be enabled at registration time?
  - Also enable = patch + emit data. We may want to patch right away to get the right reference to the API (no other patches) but maybe we’re not interested in the data yet (enable it later).
- [maxime] [https://github.com/open-telemetry/opentelemetry-browser/pull/357](https://github.com/open-telemetry/opentelemetry-browser/pull/357)
  - feat(sdk): validate all export URLs before starting the SDK
