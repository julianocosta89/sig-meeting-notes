## Meeting Notes

### Attendees
- Jason (Splunk)
- Manoel (PostHog)
- Hanson Ho (Embrace)
- Cesar (Elastic)
- Jamie (Embrace)

### Agenda
- [Cesar] - Bumping min Kotlin version: [https://github.com/open-telemetry/opentelemetry-android/pull/1489](https://github.com/open-telemetry/opentelemetry-android/pull/1489)
  - Kotlin only supports the last 4 minor versions for backwards compilation targets
  - [Context about Kotlin](https://mbonnin.net/2026-02-22-kotlin-versions/)
  - A lot of the tooling has already been bumped to min kotlin 2.0
  - If we don’t follow, we get in a pinch.
  - Okhttp just requires users to stay on older version if the need the older version
  - Jamie to revise the [versioning.md](http://versioning.md) to mention that we can break without major version in those 3 cases…
  - Also call out as breaking change in the changelog.md
- [Cesar] - Animal sniffer issue: [https://github.com/open-toast/gummy-bears/issues/168](https://github.com/open-toast/gummy-bears/issues/168)
  - Manifests itself as a runtime problem/crash
  - Api 23 is required to pick up *some*(?) of the classes
    - CompletableFuture, requires api 24
  - API26 is similar to java 8
  - Option 1: whoever is maintaining the lib can put in protections
  - Option 2: android emulator tests for disk buffering
    - Or we can do that in our repo
  - Option 3: Can we use or make something similar to [https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk/common/src/main/java/io/opentelemetry/sdk/common/CompletableResultCode.java](https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk/common/src/main/java/io/opentelemetry/sdk/common/CompletableResultCode.java) ?
  - 21 -> 26 is a aggressive – should have a separate tracking issue for this
- [Cesar] - “apiDump” is broken: [https://github.com/Kotlin/binary-compatibility-validator/issues/312](https://github.com/Kotlin/binary-compatibility-validator/issues/312)
  - Potential workaround: [https://github.com/embrace-io/embrace-android-sdk/pull/3103](https://github.com/embrace-io/embrace-android-sdk/pull/3103)
  - Embrace to copypasta the fix/workaround! <3
- [Jamie] - POC showing instrumentation module that uses Kotlin API:  [https://github.com/open-telemetry/opentelemetry-android/pull/1617](https://github.com/open-telemetry/opentelemetry-android/pull/1617)
  - Metrics api is missing in otel-kotlin
  - What’s it going to take for us to start using pieces of otel-kotlin?
    - Stability levels? Signal availability?
    - Right now we are sketching to see how it feels, not yet ready, but looking like we’re on track
- [Hanson] Google Play SDK Console update
  - No update lol\
- Jason - Declarative config yaml
