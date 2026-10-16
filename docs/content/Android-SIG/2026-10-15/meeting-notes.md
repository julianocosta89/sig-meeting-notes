## Meeting Notes

### Attendees
- Ben (Grafana)
- Jason (Splunk)
- Vishwan (Grafana)
- Hanson Ho (Embrace)
- Cesar (Elastic)
- Jason Morris (Embrace)
- Jamie (Embrace)

### Agenda
- [Vishwan]
  - Sampler configuration: [#2096](https://github.com/open-telemetry/opentelemetry-android/pull/2096). Should we expose a general sampler option in the DSL? How should session-based samplers access the initialized session provider?
  - Restart linking: [#2087](https://github.com/open-telemetry/opentelemetry-android/pull/2087). Can we add a small `previousSession(...)` hook for the first session-start event, keeping persistence and restart policy outside the SDK?
  - Cross-signal sampling: [#970](https://github.com/open-telemetry/opentelemetry-android/issues/970)**.** How should traces and logs share the same session sampling decision? What should we do when a recovered crash’s original decision is unavailable?
  - How about ordering of session sampling? Should it go first? Is that fine?
    - I think we think it’s ok to place session sampler first.
- [Jamie] Shall we enable Github PR stacks?
  - It doesn’t work across forks!
  - This allows maintainers and approvers to push branches to the repo
  - Branches have to be named <your-gh-id>/brach-name
  - Sounds like yes
