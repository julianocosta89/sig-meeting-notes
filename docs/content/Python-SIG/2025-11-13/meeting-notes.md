## Meeting Notes

### Attendees
- Hector Hernandez (Microsoft)
- Dylan russell (google)
- Aaron Abbott (Google)
- Riccardo Magliocchetti (Elastic)
- Leighton Chen (Microsoft)
- Tammy Baylis (Solarwinds)
- Sergey Sergeev (Cisco/Splunk)

### Agenda
- [Riccardo] Logs stabilization update
  - [https://github.com/open-telemetry/opentelemetry-python/pull/4676](https://github.com/open-telemetry/opentelemetry-python/pull/4676) merged! Thanks Hector!
  - Logging instrumentation injecting context into Python log records vs log shipping, filter these attributes in the log shipping code? [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3687#issuecomment-3526897181](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3687#issuecomment-3526897181)
    - Aaron: opentelemetry-instrumentation-logging ,ay not have much value and also it’s confusing to people
  - [aaron] [Consider moving `LoggingHandler` out of the SDK and into an instrumentation · Issue #4330 · open-telemetry/opentelemetry-python · GitHub](https://github.com/open-telemetry/opentelemetry-python/issues/4330)
    - Aaron: not confident to make the handler marked stable
    - Riccardo: no objection if this is still installed by bootstrap
    - Tammy: we have manual users  [https://github.com/open-telemetry/opentelemetry-python/blob/main/docs/examples/logs/example.py#L8](https://github.com/open-telemetry/opentelemetry-python/blob/main/docs/examples/logs/example.py#L8)
- [Riccardo] On logging: should we try to stringify attributes values that are not AnyValue or filter them in the instrumentations? [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3731](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3731)
  - Aaron: what other languages are doing? Anyway not opposed to move to api code
  - Rhadika: I can take a look at nodejs
- [Riccardo] Anyone interested in reviewing openai instrumentation PRs? Eventually becoming component owner
  - Hector: can help
  - [Dylan] happy to review some PRs
  - Aaron: I can bring the topic to genai meeting
