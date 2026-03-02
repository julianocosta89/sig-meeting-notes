## Meeting Notes

### Attendees
- Jason (Splunk)
- Cesar (Elastic)
- Hanson Ho (Embrace)
- Jamie Lynch (Embrace)
- Mustafa Haddara (Honeycomb)
- Jairo (Honeycomb)

### Agenda
- Changes in the registry around kotlin [https://opentelemetry.io/ecosystem/registry/?language=kotlin](https://opentelemetry.io/ecosystem/registry/?language=kotlin)
- Please review [https://github.com/open-telemetry/community/issues/2975](https://github.com/open-telemetry/community/issues/2975) donation request if you haven’t yet thanks!
- [Cesar] Gradle plugin for the OTel agent.
  - We should consider publishing a plugin for the agent
  - Pros:
    - Allows for one-liner installation of the agent
    - All of the instrumentation, but with build-time weaving where needed
    - Natural fit for developers to use plugins
    - Feat: Mapping files and build IDs
    - Feat: File based config
  - Cons:
    - Yet another module to maintain
    - Gradle is complicated
- AI: Jason to bring this up in java SIG re: okhttp jvm vs android
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1294](https://github.com/open-telemetry/opentelemetry-android/issues/1294)
  - [https://github.com/open-telemetry/opentelemetry-java/pull/7681/files](https://github.com/open-telemetry/opentelemetry-java/pull/7681/files)
  - Can we just make a new module that publishes with the kotlin dependency and make it explicit?
    - Then android can use it as its dependency
- [Hanson] [Additional HTTP info semantic conventions](https://github.com/open-telemetry/semantic-conventions/issues/2827) - Surhbi’s proposal
  - [https://github.com/open-telemetry/opentelemetry-specification/blob/f31acdf68b1c886269ab39011a338a8d72dbebea/oteps/4430-span-event-api-deprecation-plan.md](https://github.com/open-telemetry/opentelemetry-specification/blob/f31acdf68b1c886269ab39011a338a8d72dbebea/oteps/4430-span-event-api-deprecation-plan.md)
- Context vs. Application PR
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1284](https://github.com/open-telemetry/opentelemetry-android/pull/1284)
