## Meeting Notes

### Attendees
- Jamie - Embrace
- Cesar - Elastic
- Surbhi A - Cisco

### Agenda
- [Surbhi] - Bring up some open questions for discussion on [Unified Http metrics semantic conventions issue](https://github.com/open-telemetry/semantic-conventions/issues/3385).
  - It works correctly for the browser and browser folks are good with this proposal. We need to close open items from mobile on this now.
    - Complex vs simple attributes proposal by Jason.
    - All vs a curated list of original http attributes on this event proposed by Hanson.
    - Clarifications made on why deltas are better than absolute timestamp.
  - Prototype: [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15664](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15664)
- [Cesar] Stabilization effort: [https://github.com/open-telemetry/opentelemetry-android/pull/1645](https://github.com/open-telemetry/opentelemetry-android/pull/1645), [https://github.com/open-telemetry/opentelemetry-android/pull/1632](https://github.com/open-telemetry/opentelemetry-android/pull/1632) related to this issue: [https://github.com/open-telemetry/opentelemetry-android/issues/1541](https://github.com/open-telemetry/opentelemetry-android/issues/1541)
- [David] New instrumentation: [https://github.com/open-telemetry/opentelemetry-android/issues/1642](https://github.com/open-telemetry/opentelemetry-android/issues/1642)
  - Add docs on how to create a new instrumentation.
- [Surbhi] OTel might bring too many classes for Android apps? Or is it Java normal initialization process?
  - Jamie brought this up: [https://github.com/embrace-io/embrace-android-sdk/blob/709f6f68cb683ecddf9e4564aee9a754bfc07bb5/embrace-android-core/src/main/kotlin/io/embrace/android/embracesdk/internal/injection/OpenTelemetryModuleImpl.kt#L94](https://github.com/embrace-io/embrace-android-sdk/blob/709f6f68cb683ecddf9e4564aee9a754bfc07bb5/embrace-android-core/src/main/kotlin/io/embrace/android/embracesdk/internal/injection/OpenTelemetryModuleImpl.kt#L94)
  - StrictMode guidelines: [https://github.com/open-telemetry/opentelemetry-android/blob/main/docs/STRICTMODE.md](https://github.com/open-telemetry/opentelemetry-android/blob/main/docs/STRICTMODE.md)
