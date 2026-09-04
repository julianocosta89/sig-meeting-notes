## Meeting Notes

### Attendees
- Vishwan Aranha
- Nacho Bonafonte
- Bryce Buchanan
- Billy Zhou
- Vinod Vydier
- Yasura Dodo
- Vladimir Kukushkin

### Agenda
- Swift Observability APIs integration - Doc shared for discussion
  - waiting for PR
- Issue cleanup
  - try to do after the pr and new issue reviews
- Next release of Otel Swift
  - early september for the last cocoapods
- [Vishwan] OTel Swift extension points for mobile session context and delayed MetricKit diagnostics
  - Separate metrics from delayed diagnostics
  - Trace the current behavior and document the exact gap.
- [Vishwan] Following last week’s discussion, I split the remaining cross-SDK session gaps into three stacked PRs.
  - [#1183](https://github.com/open-telemetry/opentelemetry-swift/pull/1183): lifecycle activity, expiry, and reset.
  - [#1184](https://github.com/open-telemetry/opentelemetry-swift/pull/1184): versioned persistence and process ownership; follows #1183.
  - [#118	5](https://github.com/open-telemetry/opentelemetry-swift/pull/1185): cross-signal sampling; follows #1184.
- [Yasura] Log and Metric exporter bug fix [#1146](https://github.com/open-telemetry/opentelemetry-swift/pull/1146)
  - Quick fix for log [#1187](https://github.com/open-telemetry/opentelemetry-swift/pull/1187)
  - Long-term solution with async
    - Refactoring [#1178](https://github.com/open-telemetry/opentelemetry-swift/pull/1178)
    - Coming more …
- Issue cleanup
  - try to do after the pr and new issue reviews
