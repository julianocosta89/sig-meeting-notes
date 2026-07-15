## Meeting Notes

### Attendees
- Jason (Splunk)
- Ben (Grafana)
- Jamie Lynch (Embrace)
- Cesar (Elastic)
- João Oliveira (Datadog)
- David
- Hanson Ho (Embrace)

### Agenda
- [ben] - Compose navigation instrumentation
  - Other implementations hook into the Navigation and detect composables
  - What should the approach be?
    - Custom spans?
    - Hanson: Navigation should be events not spans –
    - Do we want to measure the timing of loads for a component?
    - “What screen we’re on” is metadata (attached to other signals)
    - It may not make sense to try and follow the existing instrumentation for compose/Composables.
    - These can/should be built independently
    - Jetpack Navigation (nav2, nav3), loading destinations
  - API as a first step
    - wrapper/facade around what nav provides
    - Listener to track navigation events
  - Jason: How do we know which composable we actually care about?
    - Auto-instrumentation vs. api
    - Is there room for an annotation to help here?
  - Embrace implementation: [https://github.com/embrace-io/embrace-android-sdk/tree/main/embrace-android-instrumentation-androidx-navigation](https://github.com/embrace-io/embrace-android-sdk/tree/main/embrace-android-instrumentation-androidx-navigation)
- Native crash handling - [https://github.com/open-telemetry/opentelemetry-android/pull/1887](https://github.com/open-telemetry/opentelemetry-android/pull/1887)
  - The events for bespoke android conventions now have events
  - But not for upstream semconv events
- AI: Jason to follow up on AppJankEvent and wire up from kotlin
  - No can do – kotlin Logger is not the java Logger. Doh!
- [Hanson] - Federated semantic conventions
  - Do we want to generate all non-core OTel semconv for now?
  - [Draft sample repo](https://github.com/bidetofevil/semantic-conventions-end-user-client)
  - [Draft consumption](https://github.com/open-telemetry/opentelemetry-android/pull/1884)
  - Attribute groups are a thing
- [jason] - Roadmap
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1893](https://github.com/open-telemetry/opentelemetry-android/pull/1893)
