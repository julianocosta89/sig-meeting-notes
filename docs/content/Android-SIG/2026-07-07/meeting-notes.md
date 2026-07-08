## Meeting Notes

### Attendees
- Jason (Splunk)
- Jason Morris (Embrace)
- Cesar (Elastic)
- Hanson Ho (Embrae)
- Jamie Lynch (Embrace)
- Ben Joseph (Grafana)
- David
- Vishwan (Grafana)

### Agenda
- [jason] Why is everyone scared to review [https://github.com/open-telemetry/opentelemetry-android/pull/1783](https://github.com/open-telemetry/opentelemetry-android/pull/1783) ?
- [jason] CodeQL jobs are broken due to kotlin 2.4.0 merge
- [jason] Committing generated semconv sources.
  - This comment [https://github.com/open-telemetry/opentelemetry-android/pull/1828#discussion_r3441641237](https://github.com/open-telemetry/opentelemetry-android/pull/1828#discussion_r3441641237)
  - pros/cons – I think the  are enough to just keep adding generated sources
  - cons: “the build” will need weaver if we don’t commit the source files. New contributors will need weaver. This strongly couples our build to weaver, whereas the other approach makes it looser. Files could get out of sync
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1876](https://github.com/open-telemetry/opentelemetry-android/pull/1876) Caesar alternative that builds
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1850](https://github.com/open-telemetry/opentelemetry-android/pull/1850) build check to enforce weaver regeneration
- [David] NTP issue seems to have been inadvertently closed
  - Some tools have been created by google in the interim (mentioned by manoel already in the thread)
  - We will have to figure out how to handle cases where NTP is unavailable/inconsistent.
  - We still think it’s better than purely using the wall clock
  - What about GNSS clocks?
- [David] Minor issue: why is observers a synchronized list?
  - JavaDoc says that synchronized is compulsory when iterating, yet it doesn’t happen in notifyObserversOfSessionUpdate
  - Or is the intended benefit of the list gotten even without locking the iterations?
  - It’s probably not correct in its current state
  - We might benefit from a copy on write array list or whatever
  - AI: David to open an issue
- [jason] - Environment secrets
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1870](https://github.com/open-telemetry/opentelemetry-android/pull/1870)
  - Maybe we can limit the environment to steps and not the entire job
  - AI: Jason to reply
- [jason] Linting snafu
  - ugh!
- [Ben/Vishwan - Grafana] - Native/NDK crash reporting support and upstream path
  - Grafana demo-side spike: [https://github.com/grafana/mobile-o11y-demo/pull/86](https://github.com/grafana/mobile-o11y-demo/pull/86)
- Yes we want this!
- We probably don’t want to wait for semconv,
- But we do have local federated semconv
