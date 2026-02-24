## Meeting Notes

### Attendees
- Trent Mick (Elastic)
- Abdelrahman Awad (Sentry)
- Andrei Borza (Sentry)
- Marylia (Grafana)
- Jackson Weber (Microsoft)
- Marc Pichler (Dynatrace)

### Agenda
- [martin] Diagnostics logger and Console instrumentation
  - [Browser console instrumentation PR](https://github.com/open-telemetry/opentelemetry-browser/pull/98)
  - [Comment](https://github.com/open-telemetry/opentelemetry-browser/pull/98#discussion_r2735811124) for context
  - Two options to address this
    - [PR to temporarily suppress logging](https://github.com/open-telemetry/opentelemetry-js/pull/6355)
    - [PR to make DiagConsoleLogger save and use original console methods](https://github.com/open-telemetry/opentelemetry-js/pull/6395)
- [marylia] from otel unplugged (js context): people are interested and want “OpenTelemetry Browser Support” and “Prepare for better JS ESM Support” ([full list](https://github.com/open-telemetry/community/issues/3253))
- [Awad] initial thoughts on [attach/detach](https://github.com/open-telemetry/opentelemetry-js/pull/6387/changes) API with tracing channels.
- [marc] any opinions on [https://github.com/open-telemetry/opentelemetry-js/pull/6385#discussion_r2786876427](https://github.com/open-telemetry/opentelemetry-js/pull/6385#discussion_r2786876427)?
  - TL;DR: spec feature; typing (and naming question):
    - Use `unknown` type for recording errors?
    - Name property `exception`, `error` (something else) to improve ergonomics?
- [carlos][offline] OTEL_RESOURCE_ATTRIBUTES update PR was merged and will be released soon, FYI: [https://github.com/open-telemetry/opentelemetry-specification/pull/4856](https://github.com/open-telemetry/opentelemetry-specification/pull/4856)  \
- [jacksonweber] Need review on [fix(opentelemetry-resources): Update the Env Var Parsing Logic to Match Spec](https://github.com/open-telemetry/opentelemetry-js/pull/6261) post update to match the updated spec.
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
