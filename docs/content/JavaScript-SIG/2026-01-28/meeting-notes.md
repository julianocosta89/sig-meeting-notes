## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Andrei Borza (Sentry)
- Raphaël Thériault (SolarWinds)
- David Luna (Elastic)
- Marylia Gutierrez (Grafana Labs)

### Agenda
- [trent] FYI: Provide input on the 2026 semconv roadmap if you have any: [https://github.com/open-telemetry/semantic-conventions/issues/3330](https://github.com/open-telemetry/semantic-conventions/issues/3330) (They are hoping to set a roadmap in the next couple of weeks.)
- [marc] shutdown behavior when OTLP endpoints are not available
  - From last week: [https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3349](https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3349)
  - I looked into shutdown behavior in OTel Java, behavior is the same
  - My draft PR for cancelling retries on shutdown does reduce the shutdown time significantly, but it seems to be going against the grain when comparing to other implementations [https://github.com/open-telemetry/opentelemetry-js/pull/6340](https://github.com/open-telemetry/opentelemetry-js/pull/6340)
    - Note: this is based my interpretation of [the exporter spec](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/sdk.md#forceflush-2) and the [processor spec](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/sdk.md#forceflush-1)
  - Options (WDYT is best?):
    - Close as won’t fix (keep status-quo)
    - Cancel retries on shutdown (go ahead with PR)
- [carlos][offline] OTEL_RESOURCES_ATTRIBUTE pr - please discuss if you have an opinion (we need feedback from the C++ and Rust SIGs too): [https://github.com/open-telemetry/opentelemetry-specification/pull/4856](https://github.com/open-telemetry/opentelemetry-specification/pull/4856)
  - We discussed a bit. The relaxation of the spec rules here sound good.
- [marylia] someone reported this bug to me today, if someone could review would be great: [https://github.com/open-telemetry/opentelemetry-js/pull/6345](https://github.com/open-telemetry/opentelemetry-js/pull/6345)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
