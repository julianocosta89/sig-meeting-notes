## Meeting Notes

### Attendees
- Jason (Splunk)
- Jamie (Embrace)
- Hanson Ho (Embrace)
- Cesar (Elastic)
- Ben (Grafana)
- Vishwan ( Grafana)
- João (Datadog)

### Agenda
- [Ben and Vishwan] - Approver request
  - [https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#approver](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#approver)
- [Vishwan] Session next steps: [#2048](https://github.com/open-telemetry/opentelemetry-android/issues/2048) and [#2049](https://github.com/open-telemetry/opentelemetry-android/issues/2049).
  - 2048 - 3 open questions:
    - Session storage hook
      - Should it be an implicit part of the session handling or a separate/external component?
      - Cesar thought we were already storing the session id on disk
        - [https://github.com/open-telemetry/opentelemetry-android/blob/93755b7f02dc24fb6c90f0996c837fcefb2e4a52/android-agent/src/main/kotlin/io/opentelemetry/android/agent/session/SessionStorage.kt#L4](https://github.com/open-telemetry/opentelemetry-android/blob/93755b7f02dc24fb6c90f0996c837fcefb2e4a52/android-agent/src/main/kotlin/io/opentelemetry/android/agent/session/SessionStorage.kt#L4)
        - We only have the in-memory implementation right now
        - Users could provide their own SessionStorage impl via DSL (doesn’t exist yet)
    - Session - new or linked?
    - How to handle failed storage?
      - Should the storage handle its own failures?
    - What are the use cases?
      - Older phones that may terminate apps when switching between apps (resource constrained)
      - Can also be used in native crash handling
  - Can we settle restart behavior and storage-failure handling for persistence? For passive lookup, should it change the default behavior or be opt-in, and can it proceed separately from the manual API proposal?
  - Should persistence use a storage option on the existing manager or a built-in persistent session provider? Either way, can we reuse the existing session rules?
- [Hanson] Criteria for adopting Kotlin API
  - Only api, not sdk
  - Api would still (in the short term) be backed by the java sdk impl
  - Do we need metrics?
  - [https://github.com/open-telemetry/opentelemetry-android/blob/main/agent-api/src/main/java/io/opentelemetry/android/OpenTelemetryRum.kt#L21](https://github.com/open-telemetry/opentelemetry-android/blob/main/agent-api/src/main/java/io/opentelemetry/android/OpenTelemetryRum.kt#L21) is the highest level api exposure to the user, and it’s the java package
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1617/changes](https://github.com/open-telemetry/opentelemetry-android/pull/1617/changes) related
    - Maybe resurrect this or something similar
