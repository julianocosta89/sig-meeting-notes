## Meeting Notes

### Attendees
- Ben (Grafana)
- Hanson Ho (Embrace)
- Jason (Splunk)
- Cesar (Elastic)
- Jamie (Embrace)
- Jason Morris (Embrace)
- João Oliveira (Datadog)
- Vishwan ( Grafana)

### Agenda
- [jason] - Contribfest will be happening as part of Kubecon in November.
  - Let’s tee up some issues in the next month
- [Hanson] Visibility tracker update PR comments
  - [https://github.com/open-telemetry/opentelemetry-android/pull/2011](https://github.com/open-telemetry/opentelemetry-android/pull/2011)
  - Looking for more feedback on this
  - We have lots of concepts of screen, but no formal semantic definition
    - Activity, fragment, nav target, etc.
  - Is it ok for this to overwrite the activity/fragment with the compose “screen” name?
    - It’s a loss of visibility
  - Related api pr [https://github.com/open-telemetry/opentelemetry-android/pull/2037](https://github.com/open-telemetry/opentelemetry-android/pull/2037)
  - We should get rid of the “[last.screen.name](http://last.screen.name)” semconv because “last” is a terrible namespace lol
    - Done! [https://github.com/open-telemetry/opentelemetry-android/blob/main/semconv/model/android/registry.yaml#L120](https://github.com/open-telemetry/opentelemetry-android/blob/main/semconv/model/android/registry.yaml#L120)
  - “Screen” semconv is broad, contrast with “Activity”, “Fragment”, “ComposeNavTarget” etc. which are very specific.
  - With the new screen API when it’s called it replaces the existing.
    - We think that having more detail is probably overengineered/overkill
  - Autoinstrumentation is nice to have, we don’t want it to all be manual
- [Vishwan]    -      [https://github.com/open-telemetry/opentelemetry-android/pull/2089](https://github.com/open-telemetry/opentelemetry-android/pull/2089)
  - [https://github.com/open-telemetry/opentelemetry-android/pull/2095](https://github.com/open-telemetry/opentelemetry-android/pull/2095)
    - Please give a review so we can move these forward.
