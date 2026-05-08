## Meeting Notes

### Attendees
- Robert Pająk (Splunk)
- Tyler Yahn (Splunk)
- Sam Xie (Splunk)
- David Ashpole (Google)
- Israel Blancas (Coralogix)

### Agenda
- [dashpole] Collector resource detectors:
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/48159#issuecomment-4398109381](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/48159#issuecomment-4398109381)
- [Tyler] Next [release](https://github.com/open-telemetry/opentelemetry-go/milestone/80)?
- [Tyler] Out the week after next
- [Israel] Can we have this pr merged before next release? ​​[https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8913](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8913) It is blocking some work on the collector
- [dashpole] Interceptors for otelgrpc
  - We need both stats handler and interceptors. Need to figure out what a clean API surface for that looks like.
