## Meeting Notes

### Attendees
- Robert Pająk (Splunk)
- Tyler Yahn (Splunk)
- David Ashpole (Google)
- Bryan Boreham (Grafana Labs)
- Sonal Gaud
- Sam Xie (Splunk)

### Agenda
- [dashpole] Follow-up on exemplar reservoir parallelism:
  - [https://github.com/open-telemetry/opentelemetry-go/pull/8257](https://github.com/open-telemetry/opentelemetry-go/pull/8257)
  - TL;DR You can’t have sharding and random bucket assignment without make it time-biased.
- [Robert] Release v1.44.0
  - [https://github.com/open-telemetry/opentelemetry-go/issues?q=is%3Aissue%20state%3Aopen%20milestone%3Av1.44.0](https://github.com/open-telemetry/opentelemetry-go/issues?q=is%3Aissue%20state%3Aopen%20milestone%3Av1.44.0)
  - [https://github.com/open-telemetry/opentelemetry-go/pulls?q=is%3Aopen+is%3Apr+milestone%3Av1.44.0](https://github.com/open-telemetry/opentelemetry-go/pulls?q=is%3Aopen+is%3Apr+milestone%3Av1.44.0)
  - [https://github.com/open-telemetry/opentelemetry-go-contrib/issues?q=is%3Aissue%20state%3Aopen%20milestone%3Av1.44.0](https://github.com/open-telemetry/opentelemetry-go-contrib/issues?q=is%3Aissue%20state%3Aopen%20milestone%3Av1.44.0)
  - [https://github.com/open-telemetry/opentelemetry-go-contrib/pulls?q=is%3Aopen+is%3Apr+milestone%3Av1.44.0](https://github.com/open-telemetry/opentelemetry-go-contrib/pulls?q=is%3Aopen+is%3Apr+milestone%3Av1.44.0)
  - [https://github.com/open-telemetry/opentelemetry-go/issues](https://github.com/open-telemetry/opentelemetry-go/issues)
  - [github.com/open-telemetry/opentelemetry-go/pulls](http://github.com/open-telemetry/opentelemetry-go/pulls)
  - [https://github.com/open-telemetry/opentelemetry-go-contrib/issues](https://github.com/open-telemetry/opentelemetry-go-contrib/issues)
  - [https://github.com/open-telemetry/opentelemetry-go-contrib/pulls](https://github.com/open-telemetry/opentelemetry-go-contrib/pulls)
- [dashpole] (FYI) Metrics SDK performance-related PRs ready for review:
  - AlwaysOff exemplar overhead: [https://github.com/open-telemetry/opentelemetry-go/pull/8267](https://github.com/open-telemetry/opentelemetry-go/pull/8267)
  - x.WithUnsafeAttributes part 1: [https://github.com/open-telemetry/opentelemetry-go/pull/8251](https://github.com/open-telemetry/opentelemetry-go/pull/8251)
  - Optimize Filters: [https://github.com/open-telemetry/opentelemetry-go/pull/8230](https://github.com/open-telemetry/opentelemetry-go/pull/8230)
