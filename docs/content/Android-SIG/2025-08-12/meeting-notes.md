## Meeting Notes

### Attendees
- Leonardo (Amazon)
- Jason (Splunk)
- Hanson Ho (Embrace)
- Mustafa Haddara (honeycomb)
- Cesar (Elastic)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana)
- Jamie Lynch (Embrace)
- Jairo (honeycomb)

### Agenda
- Leo: A few issues to look at! Would like opinions before I start submitting out some prototype PRs for these:
  - First draw instrumentation: [https://github.com/open-telemetry/opentelemetry-android/issues/1143](https://github.com/open-telemetry/opentelemetry-android/issues/1143)
    - Embrace has time to first draw similar data
    - Version-specific peculiarities to deal with when implementing
    - Does [ViewTreeObserver.addOnDrawListener](https://developer.android.com/reference/android/view/ViewTreeObserver#addOnDrawListener(android.view.ViewTreeObserver.OnDrawListener))  handle all cases (are there non-activity apps? etc?)
    - Example instrumentation that uses some of this data:
      - [Embrace App Startup implementation](https://github.com/embrace-io/embrace-android-sdk/tree/main/embrace-android-features/src/main/kotlin/io/embrace/android/embracesdk/internal/capture/startup)
    - Do we have a clear use case for this? It could be wasteful to build/maintain features that aren’t being asked for by users.
    - Let’s start with the simple thing and enhance it as needed over time.
    - If there are edge cases (version support) not accounted for, that’s fine.
  - Monitoring relative cpu utilization for client spans: [https://github.com/open-telemetry/opentelemetry-android/issues/1142](https://github.com/open-telemetry/opentelemetry-android/issues/1142)
    - Does this fall under the responsibility of metrics? I would argue no, since this tries to find the process cpu utilization for the *span’s duration* specifically.
    - It’s really hard to attribute CPU to a given span behavior
    - Maybe it’s more helpful to see what the CPU was doing during a span, especially for cases when the span performance is abnormal.
    - getElapsedCpuTime might not be actual cpu time
    - Might relate to those perfetto issues as well
    - Metrics discussion ongoing [https://github.com/open-telemetry/opentelemetry-specification/issues/4604](https://github.com/open-telemetry/opentelemetry-specification/issues/4604)
  - Zero-code instrumentation with ContentProvider: [https://github.com/open-telemetry/opentelemetry-android/issues/1144](https://github.com/open-telemetry/opentelemetry-android/issues/1144)
    - Expected to have a Gradle plugin for the initializer
    - Upstream SDK ongoing effort to have config file based experience
    - We generally like this idea
- [Cesar] Disk buffering API changes to become stable: [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2084](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2084)
  - PLEASE REVIEW
  - alpha / beta / stable discussion [https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2078](https://github.com/open-telemetry/opentelemetry-java-contrib/issues/2078)
- [Cesar] Issue with swapping grpc exporters: [https://github.com/open-telemetry/opentelemetry-java/pull/7557](https://github.com/open-telemetry/opentelemetry-java/pull/7557)
  - PLEASE REVIEW
- [Cesar] Semconv PR to add “app.build_id” attr: [https://github.com/open-telemetry/semantic-conventions/pull/2591](https://github.com/open-telemetry/semantic-conventions/pull/2591)
  - PLEASE REVIEW
- [jason] Should we keep volley instrumentation?
  - AI: Jason to deprecate Volley [https://github.com/open-telemetry/opentelemetry-android/pull/1145](https://github.com/open-telemetry/opentelemetry-android/pull/1145)
