## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Cleo Schneider (Google/Firebase)
- Martin Kuba (Grafana Labs)
- Wolfgang Therrien (Honeycomb)
- Hugo Levy (Datadog)
- Trent Mick (Elastic)
- David Luna (Elastic)

### Agenda
- [david] document-load instrumentation. Yes or no
  - Issue: [https://github.com/open-telemetry/opentelemetry-browser/issues/327](https://github.com/open-telemetry/opentelemetry-browser/issues/327)
  - Slack: [https://cloud-native.slack.com/archives/C093P0AMP0T/p1786348568225079](https://cloud-native.slack.com/archives/C093P0AMP0T/p1786348568225079)
  - Notes:
    - Valid use case for it is propagating context form the backend (server side rendered page)
    - W3C proposal to add server-timings headers in resource entries
    - Decision: Jared to post doc-load draft PR and review existing vs proposed together
- [cleo] github workflow
  - David raised some good questions about the rebase workflow that I added to the onboarding doc, let's discuss
  - PR: [https://github.com/open-telemetry/opentelemetry-browser/pull/380](https://github.com/open-telemetry/opentelemetry-browser/pull/380)
  - Decision: REbase to your heart's content until you get review comment
- [cleo] remaining onboarding doc todos - issue triage and recommended toolchain
  - PR: [https://github.com/open-telemetry/opentelemetry-browser/pull/380](https://github.com/open-telemetry/opentelemetry-browser/pull/380)
  - issue triage - yes, set expectations for contributors
  - talk with Jared about how to document toolchain and what customers need to know
  - update npm and node section to recommend using .nvmrc
- [Joaquin] xhr instrumentation:
  - Starting span in open vs send
  - Keeping span events
  - Decision: Not keeping span events and start span on send
- [Wolfgang]
  - Gauge interest on updating `web-vitals` instr to support soft nav
    - [https://github.com/GoogleChrome/web-vitals#report-metrics-for-soft-navigations](https://github.com/GoogleChrome/web-vitals#report-metrics-for-soft-navigations)
    - Happy to open issue/PR
