## Meeting Notes

### Attendees
- Jason (Splunk)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com)(Grafana)
- Hanson Ho (Embrace)
- Mustafa Haddara (Honeycomb)
- Jamie Lynch (Embrace)
- Jairo (honeycomb)

### Agenda
- Build speed is still slow
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1076](https://github.com/open-telemetry/opentelemetry-android/pull/1076)
  - Gregor: Have we considered using a more parallel build, similar to what we do in the instrumentation repo
    - Test1
    - Test2
    - ![][image3]
    - Etc.
  - It doesn’t seem like we’re doing too much, so why is it so slow?
  - Kapt is being replaced with ksp
    - Supposed to be faster!
    - References?
- API 26 or lower is now what requires desurgaring
  - Due to some android clock issue?
  - Need to update readme to let users know this
  - AI: Hanson to open an issue on this (or PR)
- Jason is going to open a new jank PR in semconv sometime this week
