## Meeting Notes

### Attendees
- Ben (Grafana)
- Jason Plumb (Splunk)
- Jason Morris (Embrace)
- Hanson Ho (Embrace)
- Cesar (Elastic)
- Jamie (Embrace)

### Agenda
- [Ben] - Filtering for HTTP instrumentation - [https://github.com/open-telemetry/opentelemetry-android/issues/1686#issuecomment-5688998606](https://github.com/open-telemetry/opentelemetry-android/issues/1686#issuecomment-5688998606)
  - Sounds like there are some use cases for inhibiting trace context propagation as well
    - Not just setting the sampled flag?
  - Don’t necessarily want client metrics about 3rd party / unimportant services
  - Can we do this at the sdk level instead of at the instrumentation level?
    - Sampler seems to make sense to inhibit spans
    - Can we use a metric view to suppress metric data points for a host/url?
      - A couple of years ago I managed to use metric view to filter some metrics, it was cumbersome but not impossible, though I’m not sure it’s still the case since it was a long time ago
    - How do we suppress context propagation from a client root span that’s sampled?
      - How necessary is this really?
      - Some prior art: [https://github.com/open-telemetry/opentelemetry-specification/issues/3799](https://github.com/open-telemetry/opentelemetry-specification/issues/3799)
- [Hanson] Client side federate semantic conventions
  - [https://github.com/open-telemetry/semantic-conventions-client-side/](https://github.com/open-telemetry/semantic-conventions-client-side/)
  - Start thinking about the path to move (some) android conventions to this repo
  - Our publish story for semantic conventions from our android repo is kinda weak right now
    - Does it matter tho? Who would even consume these?
      - Probably automation/tooling that wants to know about changes/updates?
      - Vendors/distros
      - Remapping use cases
  - This new repo should be the real eternal publication source long term
- [jason p] [https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/19954](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/19954)
- [Jamie] By popular request, PRs that use opentelemetry-kotlin within opentelemetry-android: [https://github.com/open-telemetry/opentelemetry-android/pull/2062](https://github.com/open-telemetry/opentelemetry-android/pull/2062) [https://github.com/open-telemetry/opentelemetry-android/pull/2063](https://github.com/open-telemetry/opentelemetry-android/pull/2063)
