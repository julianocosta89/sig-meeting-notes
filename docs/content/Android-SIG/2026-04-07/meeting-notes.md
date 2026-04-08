## Meeting Notes

### Attendees
- Jamie (Embrace)
- Jason (Splunk)
- Surbhi (Cisco)
- Cesar (Elastic)
- Hanson Ho (Embrace)

### Agenda
- [Surbhi] - ignoreUrls config in okhttp3 instrumentation
  - Sampler is an option but not ideal, should be built into the instrumentation.
    - Samplers are at the trace level
  - Use case is unclear, but we can speculate about security use cases or frequent unwanted requests
    - Why can’t we just filter these in the collector/backend?
      - Because it means we’ve done extra client work
  - Shouldn’t this then be for all instrumentations, not just for okhttp?
    - This exists today: [https://github.com/open-telemetry/opentelemetry-android/blob/main/core/src/main/java/io/opentelemetry/android/export/FilteringSpanExporterBuilder.kt](https://github.com/open-telemetry/opentelemetry-android/blob/main/core/src/main/java/io/opentelemetry/android/export/FilteringSpanExporterBuilder.kt)
  - AI: Surbhi to create an issue
- [surbhi] unified semantic convention issue
  - [https://github.com/open-telemetry/semantic-conventions/issues/3385](https://github.com/open-telemetry/semantic-conventions/issues/3385)
  - There is also an implementation challenge – when different pieces come in at different times, you want to be able to set the small attribute at any time.
    - Does the complex attribute require then walking the tree and doing type trickery at every stage?
  - We should probably just flatten it.
    - AI: Jason to reply with this and give general approval
  - If modeled as an event, can we require the context?
    - The event is kinda useless without it
- Removing [https://github.com/open-telemetry/opentelemetry-android/issues/1663](https://github.com/open-telemetry/opentelemetry-android/issues/1663) from the 1.3 milestone in favor of getting a release out.
  - There is a workaround – users can pin the lower version
