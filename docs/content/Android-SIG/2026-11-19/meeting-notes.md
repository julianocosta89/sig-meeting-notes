## Meeting Notes

### Attendees
- Ben (Grafana)
- Vishwan (Grafana)
- Cesar (Elastic)
- Jason Morris (Embrace)
- Hanson Ho (Embrace)

### Agenda
- What to do when we start getting too many defensive PRs
  - If the architecture isn’t affected, we should go ahead
  - It depends on the author
  - Ideas are welcome, we still don’t have this issue but it might happen at some point
  - CI checks
  - Agent instructions
  - Always prefer deterministic checks over AI instructions whenever possible
- [Ben] What’s the process to add API breaking changes
  - Depends on the stability level of the module, it should be fine if it’s not stable
  - If the module is stable, we should mark the old APIs as deprecated so that we remove them in the next major version
  - Add breaking issues into the 2.0.0 milestone: [https://github.com/open-telemetry/opentelemetry-android/milestone/4](https://github.com/open-telemetry/opentelemetry-android/milestone/4)
- [Ben] Sampling support
  - If something “interesting” happens during a period of time, we take it as a decision to sampling the last couple of minutes of data
  - OTel sampling what does it support (traces)
  - Do we want to sample all signals, or a subset chosen at the time of exporting?
- Next release
