## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Robert Pająk (Splunk)
- Sam Xie (Splunk)
- Alex Kats (Capital One)
- Bryan Boreham (Grafana Labs)

### Agenda
- [Tyler] [Updated EC2 detector to use v2 aws sdk](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/6878)
  - [Upstream is deprecated](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/7644)
  - We already have a v2
  - We should deprecate and release that deprecation of the v1 module
  - We should remove the v1 once that release has been made to have renovatebot skip this
  - AI (Tyler): add to issue to track
- [Robert] Discuss [Add minimum_severity and trace_based logger configuration parameters #4612](https://github.com/open-telemetry/opentelemetry-specification/pull/4612#issuecomment-3143778711) versus [LoggerConfigurator](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/sdk.md#loggerconfigurator)
- [Alex] SQS context propagator [https://github.com/open-telemetry/opentelemetry-go-contrib/issues/7620](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/7620)
- [Tyler] Milestone v1.38.0:
  - [Otel](https://github.com/open-telemetry/opentelemetry-go/milestone/73)
  - [Contrib](https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/32)
