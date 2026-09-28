## Meeting Notes

### Attendees
- Jason Plumb (Splunk)
- David
- Ben (Grafana)
- Cesar (Elastic)
- Vishwan (Grafana)

### Agenda
- [Jamie] - Discuss what DSL should look like for specifying custom processors, samplers, and propagators: [https://github.com/open-telemetry/opentelemetry-android/issues/2042](https://github.com/open-telemetry/opentelemetry-android/issues/2042)
  - Pros and cons are laid out pretty well in the issue
  - There’s nothing requiring us to adopt the same patterns as core.
  - Doing the #2 option allows us to go more incrementally
  - I think in general it sounds like we prefer option 2 for the reasons above and what’s in the issue.
  - Please comment on the issue
- [David] - Finally updated the gesture rework
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1841](https://github.com/open-telemetry/opentelemetry-android/pull/1841)
  - The issue was most likely with name clashing: click and common
  - Please review if you have not yet
- (some talk about the demo app)
  - Why do we want to move it out of the project?
    - Use a real backend
    - Makes it more “real” and shows client side telemetry in a broader scope
  - Does this make the contributor experience worse?
    - Yeah probably yes
  - Local maven publish can help
  - Are we using it for tests?
    - Jason: I don’t think so?
  - https://github.com/open-telemetry/opentelemetry-android/issues/1724
- [Ben] - [https://github.com/open-telemetry/opentelemetry-android/pull/2074](https://github.com/open-telemetry/opentelemetry-android/pull/2074)
  - Filtering HTTP telemetry/spans
  - “httpTelemetry” is there a better name?
  - Does it break redirects? Do redirects break it?
  - Can we mark this as @Incubating for some time?
  - Does this cover both allowlist AND ignorelist
    - Can we use a predicate to cover both?
- [Vishwan]
  - [https://github.com/open-telemetry/opentelemetry-android/pull/2061](https://github.com/open-telemetry/opentelemetry-android/pull/2061)
  - [https://github.com/open-telemetry/opentelemetry-android/pull/2052](https://github.com/open-telemetry/opentelemetry-android/pull/2052)
    - Please have a look and provide feedback
    - What should be the behavior in the repeated crash case?
    - Please review in order and provide feedback.
