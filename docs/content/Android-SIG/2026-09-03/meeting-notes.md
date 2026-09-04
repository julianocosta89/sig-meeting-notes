## Meeting Notes

### Attendees
- Jason Plumb (Splunk)
- Hanson Ho (Embrace)
- Vishwan ( Grafana)
- Cesar (Elastic)
- Jason Morris (Embrace)
- Jamie Lynch (Embrace)

### Agenda
- [jason] - why are these builds passing now when they were broken for a while!?!
  - androidx.core [https://github.com/open-telemetry/opentelemetry-android/pull/1788](https://github.com/open-telemetry/opentelemetry-android/pull/1788)
  - androidx.lifecycle [https://github.com/open-telemetry/opentelemetry-android/pull/1824](https://github.com/open-telemetry/opentelemetry-android/pull/1824)
- [Vishwan] - Where should manual session controls live?
  - [#910](https://github.com/open-telemetry/opentelemetry-android/issues/910) needs a way for apps to signal active/inactive state.
  - Should this follow a shared manual API pattern with screen tracking or live in the session API?
    - It’s different than screen tracking
    - Screen tracking is probably more complicated
  - [#2035](https://github.com/open-telemetry/opentelemetry-android/pull/2035) is back in draft until we agree.
  - How should manual signals interact with the default lifecycle behavior?
  - Should passive attribution remain in #2035 or move separately?
  - Should the same control surface support an explicit linked session reset?
- [Vishwan] - Sequence for the remaining session work
  - Should I open a focused upstream issue for versioned persistence and process ownership, independently of #910/#2035?
  - For persisted sampling across signals, do [#841](https://github.com/open-telemetry/opentelemetry-android/issues/841), [#970](https://github.com/open-telemetry/opentelemetry-android/issues/970), and [#1006](https://github.com/open-telemetry/opentelemetry-android/issues/1006) cover the work or should we create one focused tracker after persistence?
- [Cesar] Manual APIs extensions proposal: [https://github.com/open-telemetry/opentelemetry-android/pull/2037](https://github.com/open-telemetry/opentelemetry-android/pull/2037)
- [Cesar] Telemetry docs proposal: [https://github.com/open-telemetry/opentelemetry-android/pull/2028](https://github.com/open-telemetry/opentelemetry-android/pull/2028)
  - How can we be sure that we’ve got coverage?
  - Telemetry could be missing.
- [jason] The next release is overdue
  - Jason will start this later today, probably finish today or tomorrow
- [jamie] Created a few issues that track features that aren’t in the DSL but are in the core module [https://github.com/open-telemetry/opentelemetry-android/issues?q=is%3Aissue%20state%3Aopen%20label%3Aagent-dsl-enhancement](https://github.com/open-telemetry/opentelemetry-android/issues?q=is%3Aissue%20state%3Aopen%20label%3Aagent-dsl-enhancement)
