## Meeting Notes

### Attendees
- Ben (Grafana)
- Jason (Splunk)
- Jamie Lynch (Embrace)
- Hanson Ho (Embrace)
- Cesar (Elastic)
- Jason Morris (Embrace)
- João Oliveira (Datadog)
- Vishwan Aranha (Grafana)
- David

### Agenda
- [jason] This meeting has always been at this time slot on this day, but it has also always conflicted with the “spec/maintainer sig” meeting. Can we move it?
  - There is an increasing interest in having the “client group” (android, ios, web, flutter) checking in regularly.
  - **PROPOSE**: Thursday at the same time (8am PST)?
    - Action item: Jason to follow up with moving this to Thursday (we agreed)
  - Does another day work better?
  - (scheduling is impossible)
- [ben] Signal shape for Compose navigation instrumentation
  - Next steps after [https://github.com/open-telemetry/opentelemetry-android/pull/1901](https://github.com/open-telemetry/opentelemetry-android/pull/1901)
    - An event is a great start
    - Navigation destination events, so it maps at least somewhat conceptually to “screen”
    - Is it a problem (confusing) that the new event would have the existing “screen” stamped into it from the ScreenAttributesLogRecordAppender?
    - In the new compose event –
      - Event name -> ??? **app.navigation.complete**
      - “Screen attribute” ->
        - app.screen.name (already exists in upstream, currently used)
        - app.navigation.destination
        - **app.navigation.destination.name**
  - Looking for input on approach to getting “current screen” within Compose apps
    - Like with the existing VisibleScreenTracker
  - Events for navigation
  - Screen is not entirely accurate, especially within the context of compose
  - The ordering between Activity and Composables is hard to enforce/guarantee
  - We might need to rework the existing Activity instrumentation
    - The existing activity lifecycle is not a great proxy for “screen”
  - Are we conflating some lower level constructs when talking about a higher level “screen” abstraction
  - Maybe we need a definition of a “screen” and an API for expressing this
    - Instrumentation and/or user code could call this to indicate screen start/stop
  - Activity spans are currently within the “lifecycle” scope.
  - AI: Jason will track down [screen.name](http://screen.name) in our federated semconv and try to remove it
- [Vishwan/Ben] Maintainer help for [#1899](https://github.com/open-telemetry/opentelemetry-android/pull/1899) and [#1901](https://github.com/open-telemetry/opentelemetry-android/pull/1901). Both have two approvals, green checks and completed waiting periods, but neither author has merge access. The concerns on #1899 are addressed, but Jason’s formal change request still needs to be cleared. #1901 is ready for a maintainer merge.
- Release
  - AI: Jason to start it today
