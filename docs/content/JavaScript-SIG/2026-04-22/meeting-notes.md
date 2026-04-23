## Meeting Notes

### Attendees
- Trent Mick
- Marc Pichler
- Jan Peer Stöcklmair
- Marylia Gutierrez

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [trent] [host-metrics](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/packages/host-metrics) possible changes to discuss:
  - Context is this PR to include it in auto-instrumentations-node: [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3484](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3484)
  - Opinions on adding language to the package that the more common recommendation is to use a *local Collector and its [Host Metrics Receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/hostmetricsreceiver/README.md)* for collecting host metrics? That is my understanding of the recommendation, but I don’t have a good reference.
  - Opinions on changing `host-metrics` to be `instrumentation-host-metrics`? I think it should be implemented as an instrumentation. My guess is it wasn’t originally an instrumentation by accident: it was the first metrics-only instr.
  - Opinions on adding it to `auto-instrumentations-node`? I recommend *off* by default, if included.
- [trent] Enable [SDK metrics](https://opentelemetry.io/docs/specs/semconv/otel/sdk-metrics/) by default? [https://github.com/open-telemetry/opentelemetry-js/pull/6607#discussion_r3114128055](https://github.com/open-telemetry/opentelemetry-js/pull/6607#discussion_r3114128055)
- [marylia] can I get an approval on [https://github.com/open-telemetry/opentelemetry-js/pull/6601](https://github.com/open-telemetry/opentelemetry-js/pull/6601)
- [marylia] can someone look into [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3454](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3454) ?
- [carlos][offline] [https://github.com/open-telemetry/opentelemetry-js/issues/6621](https://github.com/open-telemetry/opentelemetry-js/issues/6621) for your api-logs stabilization (will follow up with the SDK review part).
  - Out of curiosity: The API seems to expose BOTH NoopLogger and NOOP_LOGGER. Is this really needed?
    - [marc] probably not intentional, we’d need to look into removing it
- [marylia] sharing some great news, the due diligence is now completed for OTel graduation!! "The TOC concludes that OpenTelemetry has met all criteria for Graduation."
  - [https://github.com/TheFoxAtWork/toc/blob/980496083ba7538f1269b99773ae125e6f50d242/projects/open-telemetry/otel-graduation-dd.md](https://github.com/TheFoxAtWork/toc/blob/980496083ba7538f1269b99773ae125e6f50d242/projects/open-telemetry/otel-graduation-dd.md)
- **Moved to next week:**
  - [marc] thoughts on [https://github.com/open-telemetry/opentelemetry-js/pull/6466](https://github.com/open-telemetry/opentelemetry-js/pull/6466)?
    - Requests like this pop up from time to time - the idea being that vendors want to “tack on” features to OTel SDKs.
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
