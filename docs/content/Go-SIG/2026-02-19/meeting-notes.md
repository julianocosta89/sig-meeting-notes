## Meeting Notes

### Attendees
- Robert Pająk (Splunk)
- Tyler Yahn (Splunk)
- Sam Xie (Splunk)
- Damien Mathieu (Elastic)

### Agenda
- [Tyler] Next Release:
  - [https://github.com/open-telemetry/opentelemetry-go/milestone/77](https://github.com/open-telemetry/opentelemetry-go/milestone/77)
  - [https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/35](https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/35)
- [Sam] [Refactor benchmark CI](https://github.com/open-telemetry/opentelemetry-go/pull/7873)
- [Robert] Discuss [https://github.com/open-telemetry/opentelemetry-go/issues/7034#issuecomment-3891699140](https://github.com/open-telemetry/opentelemetry-go/issues/7034#issuecomment-3891699140)
  - Breaking change -> user can not bump immediately, problem with even naming the new methods
  - Side note: We can add “Unsafe” methods to attribute.KeyValue that would not make a copy of the slices to decrease the amount of copying
