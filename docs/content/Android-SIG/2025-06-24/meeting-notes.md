## Meeting Notes

### Attendees
- cleverchuk(solarwinds)
- Hanson Ho (Embrace)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- Jason (Splunk)
- Jairo (honeycomb)

### Agenda
- [cleverchuk] - what do we think about having an instrumentation-all module which will contain all available instrumentation?
  - Top-level module that sits next to agent
  - Would it be possible to still use the build-time bytecode weaving instrumentations from this jar?
    - Sounds like no?
    - Actually bytebuddy will apply all available, which is probably what you wanted anyway if you applied the “-all” module.
    - [https://github.com/open-telemetry/opentelemetry-android/blob/main/instrumentation/okhttp3/agent/src/main/resources/META-INF/net.bytebuddy/build.plugins](https://github.com/open-telemetry/opentelemetry-android/blob/main/instrumentation/okhttp3/agent/src/main/resources/META-INF/net.bytebuddy/build.plugins) would all get merged (we hope).
    - Alternate approach is to NOT include the build-time resources and then require the user to include the specific build-time modules they depend on
  - We do still publish a bom :)
- Where is view-click instrumentation?
  - Snapshot is [https://oss.sonatype.org/content/repositories/snapshots/io/opentelemetry/android/instrumentation/view-click/](https://oss.sonatype.org/content/repositories/snapshots/io/opentelemetry/android/instrumentation/view-click/)
- [Hanson] Kotlin API usage plan
  - Work in progress
    - End goal is to support kotlin multiplatform
      - Where jvm classes are not allowed
    - It’s a lot of work.
  - Side by side (java android and kotlin android)?
  - Incremental vs. all-at-once?
  - AI: Hanson to link us to the existing kotlin otel api project
- [Leonardo] SpanEvents - when will they be deprecated? Anyone working on this?
  - Yes! [https://github.com/open-telemetry/opentelemetry-specification/pull/4430](https://github.com/open-telemetry/opentelemetry-specification/pull/4430)
  - AI: Leonardo to create an issue on android repo to migrate these
- Please sonatype be good to us
  - You can track this build to see if it thinks it published a snap [https://github.com/open-telemetry/opentelemetry-android/actions/runs/15854597472](https://github.com/open-telemetry/opentelemetry-android/actions/runs/15854597472)
