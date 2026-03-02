## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Raphaël Thériault (SolarWinds)
- Trent Mick (Elastic)
- David Luna (Elastic)
- Andrei Borza (Sentry)
- Marylia Gutierrez (Grafana)
- Aaron Abbott (Google)[
- Jonathan Munz (Embrace)
- Jackson Weber (Microsoft)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [trent] [https://github.com/open-telemetry/opentelemetry-js/pull/5839](https://github.com/open-telemetry/opentelemetry-js/pull/5839) adds support for some of the [new composable samplers](https://opentelemetry.io/docs/specs/otel/trace/sdk/#compositesampler) and newer [consistent sampling spec](https://opentelemetry.io/docs/specs/otel/trace/tracestate-probability-sampling/) via a new “sampler-composite” package. It would be nice to have a second reviewer on this.
  - [ ] Carlos: Not a js approver but I would like to review this, as I’m in the sampling SIG.
- [Aaron] [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3007](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3007)
- [Marylia] for our logs, do we have a pattern implemented?
  - [ ] E.g. Java `{{.severity_text}} [{{.thread_name}}] {{.scope_name}} {{__line__}}- {{.exception_type}} {{.exception_message}} <<otellog.attributes>>`
  - [ ] E.g. .NET `{{.severity_text}} [{{.scope_name}}] {{__line__}} {{.exception_type}} {{.exception_message}}  <<otellog.attributes>>`
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
