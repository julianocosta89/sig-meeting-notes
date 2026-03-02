## Meeting Notes

### Attendees
- Jason (Splunk)
- Mustafa (Honeycomb)
- Hanson Ho (Embrace)
- cleverchuk(solarwinds)

### Agenda
- [jason] (Maybe we defer this or revisit after Cesar is back?) ….What about additional customizations in core/OTRB?
  - Seems like people want more of this…
    - Example: [https://github.com/open-telemetry/opentelemetry-android/pull/1389](https://github.com/open-telemetry/opentelemetry-android/pull/1389)
    - Example: [https://github.com/open-telemetry/opentelemetry-android/issues/1378#issuecomment-3533044820](https://github.com/open-telemetry/opentelemetry-android/issues/1378#issuecomment-3533044820)
    - Think about exposing OTRB on the initializer interface going forward (“baby kitchen sink”)
      - ​​[https://github.com/open-telemetry/opentelemetry-android/blob/main/android-agent/src/main/kotlin/io/opentelemetry/android/agent/OpenTelemetryRumInitializer.kt#L86](https://github.com/open-telemetry/opentelemetry-android/blob/main/android-agent/src/main/kotlin/io/opentelemetry/android/agent/OpenTelemetryRumInitializer.kt#L86)
    - Also we will probably want to find a way to allow users to customize/specify (parts of) the Resource via the Initializer (no real way to to do this yet)
      - [https://github.com/open-telemetry/opentelemetry-android/issues/1257#issuecomment-3617125034](https://github.com/open-telemetry/opentelemetry-android/issues/1257#issuecomment-3617125034)
      - AI: Jason to open issue
- [Jamie] Google Play SDK Console registration: [https://github.com/open-telemetry/opentelemetry-android/issues/379](https://github.com/open-telemetry/opentelemetry-android/issues/379)
  - [https://play.google.com/sdk-console/about/](https://play.google.com/sdk-console/about/)
  - We should see what’s necessary to get signed up for this
  - Can we see if we can keep this out of a single maintainer email? (shared responsibility)
  - ![][image2]
  - AI: Jason to ask if we can get/use an otel identity for this.
- [jason] - What do people think about this change? [https://github.com/open-telemetry/opentelemetry-android/pull/1465](https://github.com/open-telemetry/opentelemetry-android/pull/1465)
  - What should we do in the multi-sim card case?
  - It’s weird to be reporting stuff about a network that you’re not actively using
  - Isn’t it a waste of data?
  - We’re not convinced (yet) that we want this.
- [jason] - What do we think about adopting a similar PR template to this one
  - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15563/files](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15563/files)
  - It helps to encourage people to disclose their usage of GenAI for issues/PRs. (well just PRs)
  - Maybe we can reuse parts but distill it and keep it smaller.
