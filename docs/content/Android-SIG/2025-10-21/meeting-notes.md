## Meeting Notes

### Attendees
- Jason (Splunk)
- Hanson Ho (Embrace)
- Jamie Lynch (Embrace)
- Cesar (Elastic)
- Francisco Prieto (Embrace)
- Mustafa Haddara (Honeycomb)
- Manoel (PostHog)
- cleverchuk(solarwinds)

### Agenda
- Release rc1 this week
  - [https://github.com/open-telemetry/opentelemetry.io/issues/7932](https://github.com/open-telemetry/opentelemetry.io/issues/7932)
  - Don’t forget to add the otel.stable=true to gradle.properties in the android-agent
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1323](https://github.com/open-telemetry/opentelemetry-android/issues/1323)
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1313](https://github.com/open-telemetry/opentelemetry-android/pull/1313)
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1321](https://github.com/open-telemetry/opentelemetry-android/pull/1321)
- We really do need to flesh out [https://opentelemetry.io/docs/platforms/client-apps/android/](https://opentelemetry.io/docs/platforms/client-apps/android/)
  - Jason: I was a brief summary of features and a code-level howto, advanced config and direct use of (unstable) core.
  - **AI: Jason to create ticket in .io repo**
  - Related [https://github.com/open-telemetry/opentelemetry.io/issues/6136](https://github.com/open-telemetry/opentelemetry.io/issues/6136)
- [cleverchuk] Do we consider slow networks and how much bandwidth we’re consuming because there are some places where data is very expensive?
  - We don’t consider this today
  - Can we cause the user to run out of data?
  - We should see if we’re gzipping on the wire by default
    - Maybe okhttp doesn’t do this by default, but does our upstream otlp exporter?
    - Telemetry shouldn’t really be all that much data.
    - **AI: Hanson to create issue to allow user-configurable gzip export**
    - Shouldn’t be a breaking change because the capability should be based on the Accepts header.
  - Should we allow developers to configure what network types allow export?
    - Might lead to data loss / aggregated sampling bias on slow networks
    - This might be a foot gun, Hanson is opinionated on this!
  - Measuring the internet bandwidth is hard/impossible
    - Knowing your capacity is hard, network type is only a hint
  - Are those slow networks also asymmetric in terms of bandwidth?
    - Yes probably?
  - This should be considered if/when we do screenshotting as well
  - Can we build/recommend tools to help developers to measure the data usage?
    - Would be an interesting experiment to measure data usage from the demo app
  - We still need the ability to throttle export data when reading from disk
    - [https://github.com/open-telemetry/opentelemetry-android/issues/638](https://github.com/open-telemetry/opentelemetry-android/issues/638)
