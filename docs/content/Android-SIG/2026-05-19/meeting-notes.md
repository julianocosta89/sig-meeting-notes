## Meeting Notes

### Attendees
- Jamie (Embrace)
- Hanson Ho (Embrace)
- Jason Plumb (Splunk)
- Cesar (Elastic)
- Cleverchuk (Solarwinds)

### Agenda
- Jamie - out for next 6 weeks
- All - What do we want to do with common module?
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1740](https://github.com/open-telemetry/opentelemetry-android/issues/1740)
  - AI: Jason hates that the app start span is hidden within the activity instrumentation. Maybe we should have new instrumentation to handle this. Jason will create an issue to address this.
  - RumConstants is public non-internal, we should at least annotate it. @Incubating
    - A bunch of those constants look like they should be moved closer to their usage (instrumentation mostly?)
  - Can we look at combining OtelAndroidClock and SystemTime, maybe remove SystemTime
  - Main goal now is to shrink its size and then reconsider (there’s not much to it)
  - AI: Jason will summarize in the issue
- Jamie - discuss stabilisation/what to do about services module
  - Intended to be internal
  - Do we discourage users from using the services module?
    - If not, should we?
    - Users should not use these directly – they are intended to abstract the platform from other internals and instrumentation….
    - 3rd party instrumentation developers should access the platform
  - We need a readme that sends a stronger message about this.
  - Maybe there is an opportunity to decompose this Services module as well.
    - Move some things into an internal instrumentation package?
  - We’re not trying to stabilize services yet, primarily because it’s internal.
- Jamie - discuss stabilisation/what to do about core module
  - Can we deprecate OpenTelemetryRumBuilder and the SdkPreconfiguredRumBuilder to send a signal?
    - We don’t have a clear path forward yet
  - SdkPreconfiguredRumBuilder is internal, so deprecating should be easier.
  - Is there really no way to BYO otel sdk?
    - Do we care?
  - Jason thinks core is maybe one of the last things that we want to stabilize
- [https://breedx-splk.github.io/when-is-the-next/](https://breedx-splk.github.io/when-is-the-next/)
- Release this week (today)
  - Cesar to start the release process this time.
