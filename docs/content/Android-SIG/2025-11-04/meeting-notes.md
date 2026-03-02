## Meeting Notes

### Attendees
- Hanson Ho (Embrace)
- Jamie Lynch (Embrace)
- Manoel (PostHog)
- Jason (Splunk)
- Jairo (honeycomb)
- Cesar (Elastic)

### Agenda
- [Trask] Invitation to join Semantic Convention SIG meeting Monday, Nov 17 8am PST to discuss confusion between app.* namespace and Kubernetes app.* [https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/#labels)
- [Mustafa] are we still working on kotlin async context propagation?
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1308](https://github.com/open-telemetry/opentelemetry-android/issues/1308)
  - Mixing and matching thread locals with coroutine context is tricky
  - Make and document a manual api might be the best
  - Trying to automate all of it is super tricky
  - Extension function in java core [https://github.com/open-telemetry/opentelemetry-java/blob/36ca9b85b799939b6cb650c5fe95e90ee2f87059/extensions/kotlin/src/main/kotlin/io/opentelemetry/extension/kotlin/ContextExtensions.kt#L13](https://github.com/open-telemetry/opentelemetry-java/blob/36ca9b85b799939b6cb650c5fe95e90ee2f87059/extensions/kotlin/src/main/kotlin/io/opentelemetry/extension/kotlin/ContextExtensions.kt#L13)
  - Some examples would be nice, maybe in the demo app as well
    - We have an example that uses the extension: [https://github.com/open-telemetry/opentelemetry-java-examples/blob/main/kotlin-extension/src/main/kotlin/io/opentelemetry/example/kotlinextension/CoroutineContextExample.kt#L29](https://github.com/open-telemetry/opentelemetry-java-examples/blob/main/kotlin-extension/src/main/kotlin/io/opentelemetry/example/kotlinextension/CoroutineContextExample.kt#L29)
  - Maybe the issue is a bug? AI [Cesar Munoz](mailto:cesar@elastic.co) to follow-up [here](https://github.com/open-telemetry/opentelemetry-android/issues/1308).
- Let’s talk release candidate again
  - Stability is still uncertain, but users want it
  - Opt-in flags for alpha/beta?
  - We still want to release a stable initializer.
