## Meeting Notes

### Attendees
- David Luna (Elastic)
- Trent Mick (Elastic)
- Jackson Weber (Microsoft)
- Hector Hernandez (Microsoft)
- Chengzhong Wu (Bloomberg)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [legendecas] [https://github.com/nodejs/node/pull/58874](https://github.com/nodejs/node/pull/58874) adding node:metrics
  - Main concern is about the current API is that it requires every consumer to hardcode metric by name about how to consume. High consumption barriers
  - [https://github.com/openjs-foundation/summit/issues/485](https://github.com/openjs-foundation/summit/issues/485)
  - [https://github.com/openjs-foundation/summit/issues/481](https://github.com/openjs-foundation/summit/issues/481)
  - Node.js Collab Summit In-Person Registration deadline is Apr 3.
  - No registration is needed for remote attendees.
  - [https://github.com/nodejs/node/pull/61907](https://github.com/nodejs/node/pull/61907) the PR adds OTel tracing API to Node.js
- [david] tracestate
  - [https://github.com/open-telemetry/opentelemetry-js/issues/790](https://github.com/open-telemetry/opentelemetry-js/issues/790)
  - Should we scope the set/unset/get API to only otel list members within the “ot” vendor key
  - I’ve seen usages of the TraceState constructor for in tests
  - Composite Sampler has its own parsing logic for `th` and `rv`
  - **Conclusion:** we should keep the class generic
- [marc] new API release 1.9.1, core and experimental released too
- [david] instrumentation scope in the instrumentations living in @opentelemetry/browser-instrumentations?
  - A good candidate would be the import needed. Ex @opentelemetry/browser-instrumentations/web-vitals
  - Path now contains “/experimental/”. Should we add it?
  - Ask in Browser SIG
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
