## Meeting Notes

### Attendees
- Marc
- Trent Mick (Elastic)
- Raphaël Thériault (SW)
- David Luna (Elastic)
- Marylia (Grafana)
- Jackson Weber (Microsoft)

### Agenda
- [marc] FYI Prometheus exporter DoS
  - [https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-q7rr-3cgh-j5r3](https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-q7rr-3cgh-j5r3)
- [marc] considering adding a Threat Model to our security policy
  - We may want to write down what defines a vulnerability, which actors we trust/don’t trust as security reports will likely increase in the future and many things can be made to look like a vulnerability.
  - I opened a draft here, we can use it as a place for discussion :)
    - [https://github.com/open-telemetry/opentelemetry-js/pull/6676](https://github.com/open-telemetry/opentelemetry-js/pull/6676)
- [raph] Node 26 and `module.registerHooks`
  - I opened [https://github.com/nodejs/import-in-the-middle/issues/249](https://github.com/nodejs/import-in-the-middle/issues/249)
  - Will probably affect both IITM and RITM
  - Should it be enabled by default in the auto instrumentation package once available ?
  - Somewhat related discussion on [https://github.com/open-telemetry/opentelemetry-js/issues/4933](https://github.com/open-telemetry/opentelemetry-js/issues/4933)
- [david] need review on [https://github.com/open-telemetry/opentelemetry-js/pull/6640](https://github.com/open-telemetry/opentelemetry-js/pull/6640)
- [carlos][offline] Ongoing SDK logs review (prior to stability)
  - LoggerConfiguratior should be marked as experimental/hidden by default: [https://github.com/open-telemetry/opentelemetry-js/issues/6677](https://github.com/open-telemetry/opentelemetry-js/issues/6677)
  - (optional) Logger’s emit() and enabled() repeat filtering logic: [https://github.com/open-telemetry/opentelemetry-js/issues/6678](https://github.com/open-telemetry/opentelemetry-js/issues/6678)
  - Missing the export pipeline next.
- [trent] dropping “Model” suffix
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
