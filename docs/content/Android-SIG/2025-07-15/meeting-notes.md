## Meeting Notes

### Attendees
- Jason (Splunk)
- Cesar (Elastic)
- Hanson Ho (Embrace)
- Mustafa Haddara (Honeycomb)
- Jairo (honeycomb)
- cleverchuk(solarwinds)

### Agenda
- (jason) I hear you like metrics. [https://github.com/open-telemetry/opentelemetry-android/pull/1064](https://github.com/open-telemetry/opentelemetry-android/pull/1064)
- (jason) GITHUB_TOKEN losing root read/write permissions  [https://github.com/open-telemetry/community/issues/2860](https://github.com/open-telemetry/community/issues/2860)
  - Does this impact us?
    - Probably yes
  - Which workflows need to request write?
    - Seems like the bot already did this! [https://github.com/open-telemetry/opentelemetry-android/pull/1035](https://github.com/open-telemetry/opentelemetry-android/pull/1035)
- (mustafa) is the android sdk supposed to be a singleton?
  - Yes! :) Not enforced through code, but one instance, created at app startup, was the intent.
  - Use case is that they want to set up the SDK when the user logs in, and then tear it back down when the user logs out.
    - Right now it errors out when they attempt to initialize the second time
      - `java.lang.IllegalStateException: An instance is already set. You can only set it once.`
      - `at io.opentelemetry.android.features.diskbuffering.SignalFromDiskExporter$Companion.set(SignalFromDiskExporter.kt:101)`
      - `at io.opentelemetry.android.features.diskbuffering.SignalFromDiskExporter.set(Unknown Source:2)`
      - `at io.opentelemetry.android.OpenTelemetryRumBuilder.scheduleDiskTelemetryReader(OpenTelemetryRumBuilder.java:462)`
      - `at io.opentelemetry.android.OpenTelemetryRumBuilder.initializeExporters(OpenTelemetryRumBuilder.java:403)`
      - `at io.opentelemetry.android.OpenTelemetryRumBuilder.lambda$build$9$io-opentelemetry-android-OpenTelemetryRumBuilder(OpenTelemetryRumBuilder.java:351)`
      - `at io.opentelemetry.android.OpenTelemetryRumBuilder$$ExternalSyntheticLambda12.run(D8$$SyntheticClass:0)`
      - `at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)`
      - `at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:644)`
    - They inject a custom SpanProcessor, and want to re-inject a new one on user login
      - Workaround is to make the custom SpanProcessor internals mutable or delegate or something
  - There is no close/shutdown on the OpenTelemetryRum instance.
    - But the otel java sdk definitely is closeable and would allow creating several instances
      - [https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk/all/src/main/java/io/opentelemetry/sdk/OpenTelemetrySdk.java#L105](https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk/all/src/main/java/io/opentelemetry/sdk/OpenTelemetrySdk.java#L105)
    - Dunno how relevant this is but here’s an issue about this on the java sdk [https://github.com/open-telemetry/opentelemetry-java/issues/7013](https://github.com/open-telemetry/opentelemetry-java/issues/7013)
  - We could use docs help on this
  - This also touches on the idea of RUM (user monitoring) vs App monitoring.
    - Can a new session be created when a user logs in? Most devs probably want this.
  - AI: Mustafa to file an issue to track interest and discussion about this over time.
- TBD (your items here)
