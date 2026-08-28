## Meeting Notes

### Attendees
- Ben (Grafana)
- Jamie (Embrace)
- Vishwan (Grafana)
- Hanson Ho (Embrace)
- Cesar (Elastic)

### Agenda
- [ben] - [https://github.com/open-telemetry/opentelemetry-android/issues/1909](https://github.com/open-telemetry/opentelemetry-android/issues/1909)
  - New compose nav event uses a new attribute, but then the visible screen tracker doesn’t (yet) know anything about compose, and continues only to report the activity/fragment.
  - Should we deprecate the activity and fragment instrumentation?
    - Can we keep these but allow them to just report their respective things (activity, fragment)?
  - Is VisibleScreenTracker intended to be the higher level “screen” tracking abstraction?
    - Should it have its own api?
      - Is it user facing or does it remain internal?
    - Current api and impl are in an internal package.
    - Can we just make a new one instead of trying to wrangle the existing one, which is all about lifecycle.
  - [screen.name](http://screen.name) vs [app.screen.name](http://app.screen.name)
  - There’s no consistent/reliable way in Android to define a “screen”
  - Imagine user application code driving a web view – they might want control of the “screen”.
  - We want users to leverage auto-instrumentation – and it should work for most users
    - And in rare cases users have an api to fall back on for overrides or more control.
    - Can we just do the auto-instrumentation first and expose an api later?
  - We need to be careful about breaking the existing (we should not break the existing)
    - …until 2.x
- [jamie] what else should we think about stabilising?
  - [https://github.com/open-telemetry/opentelemetry-android/blob/e6d8ce108f5a2fd4142b60433ebc51216b827746/docs/ROADMAP.md?plain=1#L47](https://github.com/open-telemetry/opentelemetry-android/blob/e6d8ce108f5a2fd4142b60433ebc51216b827746/docs/ROADMAP.md?plain=1#L47)
  - The 3 are next - common, core, services
    - Common [https://github.com/open-telemetry/opentelemetry-android/issues/1740](https://github.com/open-telemetry/opentelemetry-android/issues/1740)
    - Cesar thinks we can get rid of core by 2.x! BOLD!
    - We barely know what is even in here, lol.
    - We still want to support java, and the agent is all kotlin
      - Maybe we need a java version of the agent dsl then?
    - We need an issue to start breaking apart or reworking core
      - Documentation can help with this as well
- [cesar] [https://github.com/open-telemetry/opentelemetry-android/issues/2020](https://github.com/open-telemetry/opentelemetry-android/issues/2020)
  - Leverage the in-memory telemetry collector used in instrumentation tests
  - Then dedupe and write metadata
- [https://github.com/open-telemetry/semantic-conventions-client-side](https://github.com/open-telemetry/semantic-conventions-client-side) has been created!
