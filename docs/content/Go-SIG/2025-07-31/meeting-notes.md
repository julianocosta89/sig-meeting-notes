## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Bryan Boreham (Grafana Labs)
- Sam Xie (Splunk)

### Agenda
- [Tyler] Milestone v1.38.0:
  - [Otel](https://github.com/open-telemetry/opentelemetry-go/milestone/73)
    - Close [https://github.com/open-telemetry/opentelemetry-go/pull/6856](https://github.com/open-telemetry/opentelemetry-go/pull/6856) and track work as an issue. The PR looks abandoned.
  - [Contrib](https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/32)
- [Bryan] Performance of marshalling/unmarshalling OTLP in Go
  - [Java has hand-optimised code](https://github.com/open-telemetry/opentelemetry-specification/discussions/1996)
  - [So does .Net](https://github.com/open-telemetry/opentelemetry-dotnet/issues/5730)
  - How about Go?
    - Proposer would have to undertake to maintain
    - Code is actually owned by Collector SIG
