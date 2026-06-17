## Meeting Notes

### Attendees
- Jason Plumb (Splunk)
- Ben Joseph (Grafana)
- Jason Morris (Embrace)
- Hanson Ho (Embrace)
- David

### Agenda
- [jason] I’ll be out next week, can someone else run the SIG call then please?
- [jason] Does screen-orientation need src/main/java/AndroidManifest.xml?
  - Nobody has a good reason let’s try removing it.
  - AI: Jason to remove
- [jason] are we ready to rename screen.name to app.screen.name?
- Notes: This is distinct from upstream-standard [app.screen.name](https://github.com/open-telemetry/semantic-conventions/blob/a8d77fc47c47499105569e6770cc0529e6a97814/model/app/registry.yaml#L91)…but semantically distinct?
- References:
  - [RumConstants.kt#L17](https://github.com/open-telemetry/opentelemetry-android/blob/fec75d216ede41a45e8a506bb2bb5685f7721369/common/src/main/java/io/opentelemetry/android/common/RumConstants.kt#L17)
  - [ScreenAttributesSpanProcessor.kt#L26](https://github.com/open-telemetry/opentelemetry-android/blob/fec75d216ede41a45e8a506bb2bb5685f7721369/core/src/main/java/io/opentelemetry/android/ScreenAttributesSpanProcessor.kt#L26)
  - [ScreenAttributesLogRecordProcessor.kt#L22](https://github.com/open-telemetry/opentelemetry-android/blob/fec75d216ede41a45e8a506bb2bb5685f7721369/core/src/main/java/io/opentelemetry/android/internal/processors/ScreenAttributesLogRecordProcessor.kt#L22)
  - [ActivityTracer.kt#L93](https://github.com/open-telemetry/opentelemetry-android/blob/fec75d216ede41a45e8a506bb2bb5685f7721369/instrumentation/activity/src/main/java/io/opentelemetry/android/instrumentation/activity/ActivityTracer.kt#L93)
  - [FragmentTracer.kt#L44](https://github.com/open-telemetry/opentelemetry-android/blob/fec75d216ede41a45e8a506bb2bb5685f7721369/instrumentation/fragment/src/main/java/io/opentelemetry/android/instrumentation/fragment/FragmentTracer.kt#L44)
  - [RumScreenName.kt#L9](https://github.com/open-telemetry/opentelemetry-android/blob/fec75d216ede41a45e8a506bb2bb5685f7721369/instrumentation/common-api/src/main/java/io/opentelemetry/android/instrumentation/annotations/RumScreenName.kt#L9)
  - [instrumentation/activity/README.md#L38](https://github.com/open-telemetry/opentelemetry-android/blob/fec75d216ede41a45e8a506bb2bb5685f7721369/instrumentation/activity/README.md#L38)
  - [instrumentation/fragment/README.md#L23](https://github.com/open-telemetry/opentelemetry-android/blob/fec75d216ede41a45e8a506bb2bb5685f7721369/instrumentation/fragment/README.md#L23)
- We should be nice and not change this without notice or a way to going back
- Sounds like there’s no push back to changing this.
- Probably want to be “stable by default” – which means putting a flag in front of these kinds of semconv changes
  - Opt in vs. opt out?.
- We already broke device.crash
  - Whatever we decide we should go back and treat this the same way
- Do we even bother if we’re going from development to development (experimental)
  - AI: Jason to ask other SIGs how they handle this
  - AI: Jason to add this (at least device.crash) to the milestone
- [jason] We should switch to [env secrets](https://cloud-native.slack.com/archives/C01NJ7V1KRC/p1779975433850719)
- Should we wait until after the next release?
- [jason] Let’s talk about federated semantic conventions
- [https://github.com/open-telemetry/opentelemetry-android/issues/1814](https://github.com/open-telemetry/opentelemetry-android/issues/1814)
- [Hanson] Google Play SDK Index Update
- Hurry up and wait
- Next release when/what?
