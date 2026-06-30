## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Pranav Sharma
- Jackson Weber (Microsoft)
- David Luna (Elastic)

### Agenda
- [david] Inspect implementation
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6690](https://github.com/open-telemetry/opentelemetry-js/pull/6690)
  - Useful feature but specific to Node.js. Should trace SDK be runtime agnostic? If so, how to have runtime specific features like this one?
  - Okay to have it
  - Nice if the types are not exposed
    - tsconfig.json stripInternal
    - Use API types as return types from the factory functions (ex. getTracer(): api.Tracer)
  - Check the dependencies, they may need the inspect symbol too (resource, …)
- [david] feature freeze for SDK 3.0. Should we start?
  - Prep release workflow for 2.x (and backport)
  - Then create an issue to notify about feat freeze
- [Pranav] requesting review for metrics batching support to the SDK
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6655](https://github.com/open-telemetry/opentelemetry-js/pull/6655)
- FYI: new versions released, Semconv 1.41.1/ Experimental 0.218 + Contrib
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
