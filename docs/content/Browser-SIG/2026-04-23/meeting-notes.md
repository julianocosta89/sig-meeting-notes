## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Martin Kuba (Grafana Labs)
- Surbhi A (Cisco)
- Hugo Levy (Datadog)
- Maxime Quentin (Datadog)

### Agenda
- [martin] Resource timing sem conv
  - proposal: use browser-specific semantics for now to unblock release
- [martin] Navigation timing sem conv
  - [https://github.com/open-telemetry/opentelemetry-browser/pull/241](https://github.com/open-telemetry/opentelemetry-browser/pull/241)
  - makes it consistent with other event namespaces
- [martin] Porting instrumentations from contrib
  - PR for the navigation instrumentation
  - also added this issue for errors (web-exception)
- [martin] Demo
  - reminder: [https://github.com/open-telemetry/opentelemetry-browser/discussions/208](https://github.com/open-telemetry/opentelemetry-browser/discussions/208)
  - primary goal: POC for the spec/semantic conventions folks
  - proposal: build it out on [this branch](https://github.com/open-telemetry/opentelemetry-browser/tree/prototype/browser-e2e-demo) without spending too much effort on polish
- [maxime] browser.document.url.full
  - [https://github.com/open-telemetry/semantic-conventions/pull/3633](https://github.com/open-telemetry/semantic-conventions/pull/3633)
  - Any blocker to validate this semantic ?
  - Will ask for a semantic conventions approval
- [Jared]
  - Core JS PR for review [https://github.com/open-telemetry/opentelemetry-js/pull/6623](https://github.com/open-telemetry/opentelemetry-js/pull/6623)
