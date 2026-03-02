## Meeting Notes

### Attendees
- Trent Mick (Elastic)
- Jackson Weber (Microsoft)
- Raphaël Thériault (SolarWinds)
- Marylia Gutierrez (Grafana Labs)
- Hector Hernandez (Microsoft)
- Andrei Borza (Sentry)

### Agenda
- [marylia] OTel Unplugged: Feb 2nd Brussels: [https://events.humanitix.com/otelunplugged-eu2026](https://events.humanitix.com/otelunplugged-eu2026)
- [marc] Thanks to everyone who worked on the HTTP and DB Semconv stabilization efforts (dual-emit)
  - Next steps: enabling stable semconv by default (around June) [https://github.com/open-telemetry/opentelemetry-js/issues/6240](https://github.com/open-telemetry/opentelemetry-js/issues/6240)
  - New Focus Topics TBD
- [marc] planning to release a new feature version of the `@opentelemetry/api` package for the first time in ~1.5 years: this will cause SDK 1.x to not cleanly install with the latest `@opentelemetry/api` package anymore, due to peer-dependency constraints not being fulfilled.
  - The only change I’m considering a minor bump for is [https://github.com/open-telemetry/opentlemetry-js/pull/5478](https://github.com/open-telemetry/opentelemetry-js/pull/5478) - the rest is performance improvements.
  - Q: do you think it’d be acceptable to release it as a bugfix release instead?
- [jacksonweber] Looking for review on [feat(opentelemetry-resources): Update the Env Var Parsing Logic](https://github.com/open-telemetry/opentelemetry-js/pull/6261)
- [carlos] bringing up roadmap
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
