## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- David Ashpole (dashpole)
- Bryan Boreham (Grafana Labs)

### Agenda
- [Tyler] Next Release: [core](https://github.com/open-telemetry/opentelemetry-go/milestone/77), [contrib](https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/35)
  - [Comply with W3C Baggage specification limits](https://github.com/open-telemetry/opentelemetry-go/pull/7880#top)
  - [Document metric api interfaces that methods need to be safe to be called concurrently](https://github.com/open-telemetry/opentelemetry-go/pull/7952#top)
- [Robert (offline)] [Release v1.X.X version of the Logs API #7801](https://github.com/open-telemetry/opentelemetry-go/issues/7801): I plan to work on adding complex attributes starting the next release.
  - In [v1.42.0](https://github.com/open-telemetry/opentelemetry-go/milestone/78) release, I want to add support for EMPTY, BYTES, SLICE types
  - In [v1.43.0](https://github.com/open-telemetry/opentelemetry-go/milestone/79) release, I want to add support for MAP type (it is the hardest to implement and review, because of serialization and deduplication logic)
  - In [v1.44.0](https://github.com/open-telemetry/opentelemetry-go/milestone/80) release, I want to change the Logs API and SDK to use attribute package and remove log.KeyValue
- Exemplars and Prometheus exporter:
  - [https://github.com/open-telemetry/opentelemetry-go/pull/7883](https://github.com/open-telemetry/opentelemetry-go/pull/7883)
  - [https://github.com/open-telemetry/opentelemetry-go/issues/6718](https://github.com/open-telemetry/opentelemetry-go/issues/6718)
  - [https://github.com/prometheus/client_golang/issues/1953](https://github.com/prometheus/client_golang/issues/1953)
