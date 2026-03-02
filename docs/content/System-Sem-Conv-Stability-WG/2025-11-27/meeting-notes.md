## Meeting Notes

### Attendees
- Braydon Kains (Google)
- Pablo Baeyens (Datadog)
- Christos Markou (Elastic)
- Roger Coll (Elastic)

### Agenda
- [https://github.com/open-telemetry/semantic-conventions/pull/3107#discussion_r2560674645](https://github.com/open-telemetry/semantic-conventions/pull/3107#discussion_r2560674645)
  - We can remove the brief
- Process.status metric
  - There is no per-process status on Windows, only per-thread status
  - Statuses are broadly similar though the waiting state is a bit more granular on Linux
