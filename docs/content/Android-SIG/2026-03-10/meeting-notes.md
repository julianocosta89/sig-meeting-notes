## Meeting Notes

### Attendees
- Cesar (Elastic)
- Hanson Ho (Embrace)
- Jason (Splunk)
- Jamie (Embrace)

### Agenda
- [jason] - NTP server vs. Android clock
  - This comment: [https://github.com/open-telemetry/opentelemetry-android/issues/197#issuecomment-3675231273](https://github.com/open-telemetry/opentelemetry-android/issues/197#issuecomment-3675231273)
  - I’ve been keeping this issue open, but maybe we’re fine closing it now?
  - Doesn’t the phone sync os time via gps or something else
  - Maybe android uses its own NTP server
  - The sync is often not good enough for distributed tracing purposes
    - Drift is real and can grow over time
    - server span starts before client span
    - Gap between client span and server span
  - Is it important to have consistency between os clock and telemetry clock?
  - Internal consistency vs. distributed tracing
  - SNTP spec recommends polling every minute
    - Leap seconds can mess with this
  - There are other additional os clocks at our disposal
    - They are unreliable tho, so would necessitate a fallback clock
  - Same clock instance should be used for all tracing calls
  - It’s complicated and are people asking for this?
  - Maybe we give users options to choose the current (mostly simple) implementation, or other pluggable complex/fancy implementations?
  - Let’s leave it open for continued consideration
- [jason] - AndroidInstrumentation installation
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1632](https://github.com/open-telemetry/opentelemetry-android/pull/1632)
  - Should users be allowed (encouraged?) to call install() at any old time?
    - Maybe we discourage this? ← should document this
- [jason] - unreliable for the next 2 weeks, can’t run the SIG meeting
