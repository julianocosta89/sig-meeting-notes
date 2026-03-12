## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Hector Hernandez (Microsoft)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [trent] instr-sequelize TAV test fail in CI: [https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3418](https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3418)
- [trent] review please: [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3417](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3417)
- [trent] Regarding [https://github.com/open-telemetry/opentelemetry-js/pull/6480](https://github.com/open-telemetry/opentelemetry-js/pull/6480) do we need to maintain the jaeger or zipkin exporters “much”?
- [carlos, only the first 20 min] Just FYI, trying to stabilize the AlwaysRecord sampler (there’s a PR for that in the js repo): [https://github.com/open-telemetry/opentelemetry-specification/pull/4934](https://github.com/open-telemetry/opentelemetry-specification/pull/4934)
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6168](https://github.com/open-telemetry/opentelemetry-js/pull/6168)  Discussing putting it in existing (sdk-trace-base?) package with `@experimental` tag.
- [david] Web instrumentations (user interaction, browser navigation) already try to wrap the same APIs (history). It seems one wins over the other (need to prepare a repro)
  - Double wrapping possible? In theory should work
  - Should we allow it? YES
  - **TODO:** Prepare a repro and a attach to an issue
- [andrei] _httpPatched guard breaks ESM instrumentation (on aws-lambda): [https://github.com/open-telemetry/opentelemetry-js/issues/6489](https://github.com/open-telemetry/opentelemetry-js/issues/6489)
- [marc] [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3132](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3132)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
