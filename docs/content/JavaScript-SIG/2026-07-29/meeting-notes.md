## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Marylia (Grafana)
- David Luna (Elastic)
- Matt Wear (Dash0)
- Jamie Danielson (Honeycomb)
- Jackson Weber (Microsoft)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [marc] we likely won’t be able to use Symbol.dispose for the token returned by context.attach() as it requires esnext.disposable, which is / will be included in ES2026 and our documentation claims support for ES2022.
  - Alternatives:
    - Proceed without disposable tokens
    - Move that functionality to experimental entrypoint
- [marc] looking at [https://github.com/open-telemetry/opentelemetry-js/pull/6901](https://github.com/open-telemetry/opentelemetry-js/pull/6901) - the instrumentation package seems to be the wrong flight-level and I think this should be handled on a reverse proxy or similar instead (stripping tracestate/traceparent), WDYT?
  - [trent] Agree this is at the wrong level. Other instrumentations can also be creating root spans for incoming requests. See this spec proposal for a “trace continuation strategy”: [https://github.com/open-telemetry/opentelemetry-specification/pull/5055/changes](https://github.com/open-telemetry/opentelemetry-specification/pull/5055/changes). Alternatively a user could configure the Propagator for their public-facing service to not extract from incoming headers, I think. I haven’t tried this myself.
  - [trent] Go http instrumentation has something like this: [https://github.com/open-telemetry/opentelemetry-go-contrib/blob/e3dc9d9daf2179c0ce57b86984e4b927022a3279/instrumentation/net/http/otelhttp/config.go#L95-L103](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/e3dc9d9daf2179c0ce57b86984e4b927022a3279/instrumentation/net/http/otelhttp/config.go#L95-L103) `WithPublicEndpointFn`
- [marc] anybody interested in a /semconv-review skill?
  - Usually reviewing instrumentation PRs is tedious because it requires finding and reading multiple Semantic Conventions docs. I’ve been testing a skill for that and it is really helpful to skip the back-and-forth between tabs
  - [jamie] also we should try to add in weaver live-check!
- [trent] Some sdk-metrics Qs on [https://github.com/open-telemetry/opentelemetry-js/issues/6957](https://github.com/open-telemetry/opentelemetry-js/issues/6957)
  - [https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/sdk_exporters/otlp.md#additional-environment-variable-configuration](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/sdk_exporters/otlp.md#additional-environment-variable-configuration)
- [trent] [https://github.com/open-telemetry/opentelemetry-js/pull/6868](https://github.com/open-telemetry/opentelemetry-js/pull/6868)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4900](https://github.com/open-telemetry/opentelemetry-specification/pull/4900) Coming spec PR that might be interesting for when/how to configure instrumentations.
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [SDK 3.0 Milestone Triage and Refinement](https://github.com/open-telemetry/opentelemetry-js/milestone/20)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
