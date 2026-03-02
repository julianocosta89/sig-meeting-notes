## Meeting Notes

### Attendees
- Mikołaj Świątek (Elastic)
- Antoine Toulme (Splunk)
- Benedikt Bongartz (Red Hat)
- David Ashpole (Google)
- Jacob Aronoff
- Pavol Loffay (Red Hat)

### Agenda
- Go through [feature gates](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) and check if any need to move forward or backward.
  - Move the sidecar featuregate to stable
    - [https://github.com/open-telemetry/opentelemetry-operator/issues/4451](https://github.com/open-telemetry/opentelemetry-operator/issues/4451)
  - Gomemlimit & maxprocs
    - [https://go.dev/blog/container-aware-gomaxprocs](https://go.dev/blog/container-aware-gomaxprocs)
    - Let’s enable this by default
    - [https://github.com/open-telemetry/opentelemetry-operator/issues/4452](https://github.com/open-telemetry/opentelemetry-operator/issues/4452)
  - Config defaulting
    - Let’s move it to Stable.
    - [https://github.com/open-telemetry/opentelemetry-operator/issues/4453](https://github.com/open-telemetry/opentelemetry-operator/issues/4453)
- Start a milestone for beta Instrumentation ([https://github.com/open-telemetry/opentelemetry-operator/milestone/5](https://github.com/open-telemetry/opentelemetry-operator/milestone/5))
  - Track instrumented workload
    - [https://github.com/open-telemetry/opentelemetry-operator/issues/544](https://github.com/open-telemetry/opentelemetry-operator/issues/544)
    - [https://github.com/open-telemetry/opentelemetry-operator/issues/1142](https://github.com/open-telemetry/opentelemetry-operator/issues/1142)
    - [https://github.com/open-telemetry/opentelemetry-operator/pull/1228](https://github.com/open-telemetry/opentelemetry-operator/pull/1228)
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is:issue+is:open+label:discuss-at-sig) (always last)
