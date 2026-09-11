## Meeting Notes

### Attendees
- Vishwan( Grafana)
- Bryce Buchanan
- Ben (Grafana)
- Vladimir (Apple)

### Agenda
- Issue clean up
- [Vishwan] Following last week’s discussion, I split the remaining cross-SDK session gaps into three stacked PRs.
  - [#1183](https://github.com/open-telemetry/opentelemetry-swift/pull/1183): lifecycle activity, expiry, and reset.
  - [#1184](https://github.com/open-telemetry/opentelemetry-swift/pull/1184): versioned persistence and process ownership; follows #1183.
  - [#118	5](https://github.com/open-telemetry/opentelemetry-swift/pull/1185): cross-signal sampling; follows #1184.
- Approver access request for Ben Joseph ([benjoseph-grafana](https://github.com/benjoseph-grafana)) and Vishwan Aranha (aranhave)
- [Vishwan] Session PR review: [#1183](https://github.com/open-telemetry/opentelemetry-swift/pull/1183) now focuses on linked reset and keeps the existing activity behavior. Is anything else needed before it can land? Can we review persistence [#1184](https://github.com/open-telemetry/opentelemetry-swift/pull/1184), then sampling [#1185](https://github.com/open-telemetry/opentelemetry-swift/pull/1185), next?
- HTTP Log & Metric exporter bug fix PRs
  - Core: [opentelemetry-swift-core/pull/107](https://github.com/open-telemetry/opentelemetry-swift-core/pull/107)
  - Log Exporter: [opentelemetry-swift/pull/1187](https://github.com/open-telemetry/opentelemetry-swift/pull/1187)
  - Metric Exporter: [opentelemetry-swift/pull/1189](https://github.com/open-telemetry/opentelemetry-swift/pull/1189)
    - Need a new release of core
  - Q: When can we release the new version of OTel Swift with the bug fixes?
    - we’ll work on merging this so an intermediate release can be done before the final cocoapods release.
- Thread sanitization
  - [https://github.com/open-telemetry/opentelemetry-swift-core/pull/70](https://github.com/open-telemetry/opentelemetry-swift-core/pull/70)
  - [https://github.com/open-telemetry/opentelemetry-swift/pull/1188](https://github.com/open-telemetry/opentelemetry-swift/pull/1188)
- Review issues & PRs
