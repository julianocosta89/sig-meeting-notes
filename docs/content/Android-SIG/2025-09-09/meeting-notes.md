## Meeting Notes

### Attendees
- Hanson Ho (Embrace)
- Leonardo (Amazon)
- Mustafa Haddara (Honeycomb)
- Jason (Splunk)
- Cesar (Elastic)
- Jairo (honeycomb)
- Surbhi A (Cisco)

### Agenda
- (Jason) Is detekt making small PRs considerably more difficult to review?
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1199/files](https://github.com/open-telemetry/opentelemetry-android/pull/1199/files) for example
  - What can we do to improve this?
  - Maybe I’m just twitchy about it and it’ll reach a more steady state soon?
  - Detekt is highly configurable – we think that maybe a few tweaks can get past most of these
  - Ideally we’d have one top-level small config
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1187](https://github.com/open-telemetry/opentelemetry-android/issues/1187) please help!
- (Surbhi) Network detection is [triggered when the SDK is initialized](https://github.com/open-telemetry/opentelemetry-android/blob/75ae9500dace57dac2f0da09976ccc4cffa7033e/core/src/main/java/io/opentelemetry/android/OpenTelemetryRumBuilder.java#L500) in the Application.onCreate but permission can only be requested when the MainActivity shows up. So, network details requiring permission (subtype, modern APIs for carrier name) are null or use legacy API even when the user grants the permission as it is granted later to when first detection happens and only app restart or network change will trigger another detection. As a solution we can perhaps expose this [refreshNetworkStatus](https://github.com/open-telemetry/opentelemetry-android/blob/75ae9500dace57dac2f0da09976ccc4cffa7033e/services/src/main/java/io/opentelemetry/android/internal/services/network/CurrentNetworkProvider.java#L100) API so it can be called by the app if permission is granted.
  - Is there a way to make this less of a burden for the application developer?
    - Are there permission change callbacks?
    - Activity listeners may not be correct due to timing challenges
  - Is it really so bad that we miss the network information on the first session?
    - API 24-33 will exhibit this
  - We should document this!
  - It would be reasonable still to have an API for the developers who really need to capture network things accurately on older APIs
  - Should users be able to opt out of the network attrs on all spans/events anyway?
  - AI: Surbhi to create issue to track this
    - Created this issue - [https://github.com/open-telemetry/opentelemetry-android/issues/1216](https://github.com/open-telemetry/opentelemetry-android/issues/1216)
- [Leo] Client tracing? Thoughts on trace ~~id~~ as session ~~id~~?
  - What is the root operation? Session? Activity?
  - Less about the actual IDs here and more of a conceptual discussion
  - There’s no good off the shelf tool right now to view this telemetry all associated.
  - It’s a natural instinct to want to group telemetry and trace is a common concept for doing this
  - Starting a span in activity onCreate, attach to main thread, other spans should be children of that activity span
  - In APM world, long-running spans / traces look like a bug.
- [Jamie] - [Kotlin API/SDK donation proposal](https://github.com/open-telemetry/community/issues/2975)
  - Context does not use thread locals currently
  - Context management is currently not fully implemented/wired?
  - Help wanted! Tell your friends!
  - Newer java might have “scope values” to replace thread locals (which were probably a mistake in hindsight?)
- [Mustafa] - path to 1.0?
  - What’s the roadmap?
  - AWS and Splunk and Honeycomb are directly consuming it
  - The initializer API is the thing that might still want to evolve
    - Service name example
  - Killer bugs vs. api surface
  - D O C U M E N T A T I O N
