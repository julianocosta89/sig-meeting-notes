## Meeting Notes

### Attendees
- Hanson Ho (Embrace)
- Jason (Splunk)
- Grace Lim (AWS)
- David Luna (Elastic)
- Bee Klimt (Honeycomb)
- Martin Kuba (Grafana Labs)
- Santosh Cheler (Splunk)

### Agenda
- [screen.name](http://screen.name) for both Android and Swift SDKs (Grace L)
  - We’ll need to settle on a semantic convention for this. [view.name](http://view.name) is def out. [screen.name](http://screen.name) might also be out even though it’s being used in Android. Proposal: [app.screen.name](http://app.name)
  - Add as attribute for now. Can consider whether it should be a resource attribute at a later time.
  - Starting point: [https://github.com/open-telemetry/semantic-conventions/blob/main/CONTRIBUTING.md](https://github.com/open-telemetry/semantic-conventions/blob/main/CONTRIBUTING.md)
  - CNCF slack #otel-client-side-telemetry (above)
- Android SIG has been talking about metrics….specifically caused by events that are metric-shaped
  - instigated by [https://github.com/open-telemetry/semantic-conventions/pull/2157](https://github.com/open-telemetry/semantic-conventions/pull/2157)
  - and demonstrated with [https://github.com/open-telemetry/opentelemetry-android/pull/1064](https://github.com/open-telemetry/opentelemetry-android/pull/1064)
  - tl;dr, we are not doing OTel metrics after this thought exercise
  - backends really do want to do their own aggregation anyway (to generate metrics)
  - the client-side metrics aggregation may not give enough precision on mobile/client platforms
    - default 1 minute aggregation in otel, for example
  - AI: Jason will open a new minimal jank PR to continue as well.
    - [https://github.com/open-telemetry/semantic-conventions/pull/2552](https://github.com/open-telemetry/semantic-conventions/pull/2552)
