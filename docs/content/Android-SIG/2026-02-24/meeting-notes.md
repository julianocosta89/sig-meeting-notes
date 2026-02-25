## Meeting Notes

### Attendees
- Jason (Splunk)
- Jamie (Embrace)
- Francisco (Canary)
- Cesar (Elastic)

### Agenda
- Jason - What do we think about an OpenTelemetryRumReadyListener (or maybe with a better name?)
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1585#issuecomment-3923874004](https://github.com/open-telemetry/opentelemetry-android/issues/1585#issuecomment-3923874004)
  - OpenTelemetryRumInitListener?
  - Don’t we already have one of these?
    - Similar: [https://github.com/open-telemetry/opentelemetry-android/blob/main/core/src/main/java/io/opentelemetry/android/OpenTelemetryRumBuilder.kt#L109](https://github.com/open-telemetry/opentelemetry-android/blob/main/core/src/main/java/io/opentelemetry/android/OpenTelemetryRumBuilder.kt#L109)
    - Related: [https://github.com/open-telemetry/opentelemetry-android/issues/1541](https://github.com/open-telemetry/opentelemetry-android/issues/1541)
  - Are we worried about anyone with the instance calling shutdown()?
  - Would the listener also need to know when the instance is invalid/shutdown?
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1071](https://github.com/open-telemetry/opentelemetry-android/issues/1071) was the original request for shutdown/reinitialize.
  - Hanson’s alt idea that remove shutdown and adds install
    - [https://github.com/open-telemetry/opentelemetry-android/pull/1580/changes#diff-8bb05033d6a0fd560cce21afa4a55b1348801d9197fe51206c18e98ed8a7f011](https://github.com/open-telemetry/opentelemetry-android/pull/1580/changes#diff-8bb05033d6a0fd560cce21afa4a55b1348801d9197fe51206c18e98ed8a7f011)
- Jason - The “agent-api” module is not yet stable (it’s the one that contains the OpenTelemetryRum interface).
  - Should we just make it stable since it’s returned by the agent api (initializer)?
  - We probably should – a stable API should return a stable component
  - Related to the instrumentation api
  - We have consensus about this, let’s do it.
    - Jason to PR this
- Jason - Do we have ANY data yet in the Google Play SDK Console about the last release?
  - Maybe Hanson and/or Severin are the only folks who can see this?
  - Takes a little time, let’s revisit this next week.
- Jamie - Rules for merging approved PRs?
  - Can we base these rules on the scope of the change?
  - Dependencies/renovate are easy
  - Large API changes probably need more reviews/thought/time
    - Not just lines of code, but importance/risk of the change
  - We should write something down, probably in [CONTRIBUTING.md](http://CONTRIBUTING.md).
    - Jamie to take a crack at it
