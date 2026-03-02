## Meeting Notes

### Attendees
- Jason (Splunk)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- Hanson Ho (Embrace)
- cleverchuk(solarwinds)
- Cesar (Elastic)

### Agenda
- [https://github.com/open-telemetry/opentelemetry-android/pull/1002](https://github.com/open-telemetry/opentelemetry-android/pull/1002)
  - There is a compilation problem with newer versions.
  - Can we make a follow-up PR with an integration test to verify that the instrumentation applies cleanly and generates telemetry with newer compose runtime versions.
  - Does it make sense to try and stay up-to-date with the latest/newer versions of compose?
    - Do compose users stay mostly current?
  - AI: CleverChuk to open a new issue to explore writing an integration tests for the ui instrumentation (compose click)
