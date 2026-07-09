## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Matt Wear (Dash0)
- Trent Mick (Elastic)
- Marylia Gutierrez (Grafana)
- Raphaël Thériault (SW)
- Abhinav Mathur ( Splunk Appdynamics )
- Hector Hernandez (Microsoft)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [marc] mentioned last week that disposable pattern for context.attach/detach may be worse performance-wise:
  - Ran some tests and [impact of the extra allocation is negligible](https://github.com/open-telemetry/opentelemetry-js/pull/6845#discussion_r3529985012) - looks like enterWith/withScope completely dominate allocations
  - I will therefore pursue using a disposable pattern, but need TypeScript >=5.2 + some uncertainty about if that could cause problem on browsers (Symbol.dispose is not baseline widely available)
- [marc] Opened [https://github.com/open-telemetry/opentelemetry-js/pull/6881](https://github.com/open-telemetry/opentelemetry-js/pull/6881) to announce 3.0 work, it is intended to become a pinned issue. Please review :)
- [marc] FYI, I opened [https://github.com/open-telemetry/opentelemetry-js/issues/6894](https://github.com/open-telemetry/opentelemetry-js/issues/6894) to track prerequisites for SDK 3.0 (feel free to add missing things if you have Triage permissions)
- [marylia] any custom messages that I should add here:
  - [https://github.com/open-telemetry/opentelemetry-js/pull/6896](https://github.com/open-telemetry/opentelemetry-js/pull/6896)
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3613](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3613)
- [marylia] Can I volunteer this SIG to test the new zoom accounts?
  - Deep notes: yolo, go for it
- [matt] Declarative config for instrumentation: [https://github.com/open-telemetry/opentelemetry-js/pull/6868](https://github.com/open-telemetry/opentelemetry-js/pull/6868)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [SDK 3.0 Milestone Triage and Refinement](https://github.com/open-telemetry/opentelemetry-js/milestone/20)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
