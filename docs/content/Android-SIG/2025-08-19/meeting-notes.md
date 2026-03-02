## Meeting Notes

### Attendees
- Leonardo (Amazon)
- Jamie Lynch (Embrace)
- cleverchuk(solarwinds)
- Jason (Splunk)
- Cesar (Elastic)

### Agenda
- Leo: Thoughts on getting all spans that happen directly as result of a user interaction (click/scroll/etc) as a single trace id? For example, if I click a button and my app navigates to a new Activity, I should get Activity lifecycle spans, HTTP spans, etc. in one trace.
  - This (having lots of unrelated trace ids) can create some problems for backends
  - Parent/root span can be created in response to a user interaction (like a click)....
  - ….but when does it end? Maybe when the UI is “stable”? Some other criteria?
  - The session is the main thing that ties everything together
  - We could build something (annotation, method, etc) to create a scoped parent trace in order to help group “actions”.
  - It would be awesome if there were some open/free tool to do session viewing
    - Can [https://github.com/ymtdzzz/otel-tui](https://github.com/ymtdzzz/otel-tui) or similar add it?
- What happens when a crash happens with regard to a session?
  - Current behavior has crash being generated at crash time, so it gets the current session
  - Can a crash close a  long-running span?
    - It’s not the current behavior, I don’t think we have callbacks for it.
  - Some vendors have a fancy way of harvesting crash data from disk on next session, and I _think_ they persist session history to associate correctly.
    - It’s complicated because so much state is being tracked all over the place
  - Long running spans are hard to deal with for sure!
- Release this week
  - Gotta fix the build first [https://github.com/open-telemetry/opentelemetry-android/actions/runs/17073648730/job/48409085030](https://github.com/open-telemetry/opentelemetry-android/actions/runs/17073648730/job/48409085030)
  - Let’s try –no-build-cache on the snapshot builds as well then
  - We even have a milestone [https://github.com/open-telemetry/opentelemetry-android/pulls?q=is%3Aopen+is%3Apr+milestone%3A0.14.0](https://github.com/open-telemetry/opentelemetry-android/pulls?q=is%3Aopen+is%3Apr+milestone%3A0.14.0)
- Jason is working on a prototype related to [https://github.com/open-telemetry/semantic-conventions/pull/2552](https://github.com/open-telemetry/semantic-conventions/pull/2552) hope to have it out this week.
- Cesar’s [https://github.com/open-telemetry/semantic-conventions/pull/2591](https://github.com/open-telemetry/semantic-conventions/pull/2591) got merged
  - We don’t yet have code to generate this yet….PRs welcome.
- Disk buffering API [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2084](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2084)
  - Jason will circle back on it
