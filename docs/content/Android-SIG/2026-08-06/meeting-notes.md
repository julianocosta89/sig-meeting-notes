## Meeting Notes

### Attendees
- Jason (Splunk)
- Jamie (Embrace)
- Cesar (Elastic)
- Ben (Grafana)

### Agenda
- David - PR bump
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1841](https://github.com/open-telemetry/opentelemetry-android/pull/1841)
  - AI: Jason to update contributing to mention closing out (resolving) copilot review comments as a signal to maintainers.
  - AI: David to try modifying depth or publish conventions
- [ben]
  - I will join 30 min later. If you guys are still around, will discuss these otherwise next week
  - Discuss [https://opentelemetry.io/docs/specs/otel/schemas/](https://opentelemetry.io/docs/specs/otel/schemas/)
    - [https://github.com/open-telemetry/opentelemetry-android/issues/1960](https://github.com/open-telemetry/opentelemetry-android/issues/1960) placeholder issue to continue discussing
    - Where do we put our local semconv schema url in the telemetry?
      - InstrumentationScope?
      - Resource?
    - Should we use this url from our repo [https://github.com/open-telemetry/opentelemetry-android/blob/main/semconv/model/manifest.yaml#L3C13-L3C73](https://github.com/open-telemetry/opentelemetry-android/blob/main/semconv/model/manifest.yaml#L3C13-L3C73)
      - This doesn’t resolve to a valid resource
      - Is there a community convention for making this?
    - Do we already publish diffs for semconv?
    - Can we just use the same schema url in both places?
      - Maybe do this to start and see how it works for people
      - Still better than null…
  - PR bump -[https://github.com/open-telemetry/opentelemetry-android/pull/1964](https://github.com/open-telemetry/opentelemetry-android/pull/1964) - have one approval from Jamie already.
- Vishwan
  - PR bump: [#1956 - Run instrumented tests on pull requests](https://github.com/open-telemetry/opentelemetry-android/pull/1956)
    - We like it! thanks
  - Release question: Is there a timeline for the next release containing [#1939](https://github.com/open-telemetry/opentelemetry-android/pull/1939)? A downstream Grafana retest is waiting on it.
    - It will be part of the regular monthly release cadence.
    - Can you use the snapshot until then?
      - AI: Cesar - Document using snapshots
  - Next work: Is [#1955](https://github.com/open-telemetry/opentelemetry-android/issues/1955) the most useful CI follow-up or is another priority more helpful?
    - Seems like a good idea to us
    - We want it minified.
    - Mockserver for retrieving telemetry
      - okhttp
    - Jason thinks that upstream java instrumentation has a server that will get telemetry that you can fetch back in tests.
