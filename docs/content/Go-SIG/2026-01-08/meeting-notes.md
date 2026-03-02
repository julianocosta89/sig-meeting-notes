## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Robert Pająk (Splunk)
- Bryan Boreham (Grafana Labs)
- Damien Mathieu (Elastic)
- Sonal Gaud
- Bhupinder Singh
- David Ashpole (Google)

### Agenda
- [Tyler] Plan 2026 goals
  - Review [https://github.com/open-telemetry/opentelemetry-go/issues/6175](https://github.com/open-telemetry/opentelemetry-go/issues/6175) and close
  - Plan goals for 2026 (just continuation?)
    - [SDK self-observability signals](https://github.com/open-telemetry/opentelemetry-go/issues/2547)
    - [Go runtime metrics stabilization](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/5655)
    - [Logs API stable](https://github.com/orgs/open-telemetry/projects/43)
    - [otelhttp stabilization](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/8107)
    - [File-based configuration](https://github.com/open-telemetry/opentelemetry-go-contrib/issues?q=label%3A%22area%3A%20file-config%22)
    - [Enabled method for metrics](https://github.com/open-telemetry/opentelemetry-go/pull/7763)
      - Done?
- [Damien] LFX Mentorship project?
  - Possibly, the otelhttp stabilization and all its side changes?
  - [https://github.com/open-telemetry/opentelemetry-go-contrib/issues/8107](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/8107)
- [Robert] [Logs to reuse attribute.[Key]Value and remove log.[Key]Value types #7034](https://github.com/open-telemetry/opentelemetry-go/issues/7034)
  - Unblocked. Complex value types + empty are stable. Planning to work on it.
  - January release first?
- [Tyler] Release next Monday.
