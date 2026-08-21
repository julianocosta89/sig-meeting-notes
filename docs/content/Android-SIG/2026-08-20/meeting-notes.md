## Meeting Notes

### Attendees
- Jason (Splunk)
- Cesar (Elastic)
- Ben (Grafana)
- Vishwan (Grafana)

### Agenda
- [jason] Architecture of smoke tests on-device
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1972](https://github.com/open-telemetry/opentelemetry-android/pull/1972)
  - We like this approach, think that merging as-is is probably ok for now
  - AI: Jason to create follow-up issue to circle back on this and wire up the upstream thing.
- [Vishwan] Native crash stack trace direction
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1940](https://github.com/open-telemetry/opentelemetry-android/issues/1940)
    - Choose between building the stack during the crash, saving a small crash snapshot and processing it later, or using Crashpad.
    - Decision needed: keep the strict crash-handler safety rules, and decide whether raw crash locations and binary IDs are enough for the first version.
    - Does Breakpad require a separate process?
    - Embrace implementation: [https://github.com/embrace-io/embrace-android-sdk/tree/main/embrace-android-instrumentation-crash-ndk/src/main/cpp](https://github.com/embrace-io/embrace-android-sdk/tree/main/embrace-android-instrumentation-crash-ndk/src/main/cpp)
    - Do we need a build id to associate a build with the telemetry?
      - [https://github.com/open-telemetry/opentelemetry-android/issues/1089](https://github.com/open-telemetry/opentelemetry-android/issues/1089)
- [vishwan] Session management work is ongoing.
  - Check out the client sig stuff
  - And #otel-client-side-telemetry
- [ben]
  - user attribution
    - End user / app user
    - Implies authentication / login
      - User log in is very common across all apps
    - [https://github.com/open-telemetry/semantic-conventions/blob/384d66161cb18704c729645fa8136a148df9571c/docs/registry/attributes/user.md](https://github.com/open-telemetry/semantic-conventions/blob/384d66161cb18704c729645fa8136a148df9571c/docs/registry/attributes/user.md)
    - Is the user tied to a session? How strongly should these two ideas be coupled?
    - Does this pose a privacy concern if we attach this to all data?
      - Can we provide an api that does anonymisation?
    - Global attribute?
      - Looking for something more standardized.
    - Can this be done today by generating a user-login event (which will have the session on it)?
    - Should we have an API that makes it easy/standard to track the user attributes?
    - Should a user be an otel entity?
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1909](https://github.com/open-telemetry/opentelemetry-android/issues/1909)
    - Please review and leave comments so that the contributor can be unblocked and get started on this
- [jason] version issue thingy
  - We should look into this [https://github.com/open-telemetry/opentelemetry-android/issues/1526](https://github.com/open-telemetry/opentelemetry-android/issues/1526)
  - Can we leverage the smoke tests for this?
  - [https://github.com/open-telemetry/opentelemetry-kotlin/blob/main/gradle-integration-test/src/test/kotlin/io/opentelemetry/kotlin/integration/gradle/MinSupportedVersionsTest.kt](https://github.com/open-telemetry/opentelemetry-kotlin/blob/main/gradle-integration-test/src/test/kotlin/io/opentelemetry/kotlin/integration/gradle/MinSupportedVersionsTest.kt)
