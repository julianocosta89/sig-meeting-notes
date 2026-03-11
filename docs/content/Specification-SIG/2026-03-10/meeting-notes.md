## Meeting Notes

### Attendees
- Josh Suereth
- Arve Knudsen
- Ted Young
- Petr Langr
- Daniel Dyla

### Agenda
- [review] [https://github.com/orgs/open-telemetry/projects/85](https://github.com/orgs/open-telemetry/projects/85)
- [tc discussion] SDK multi-resource OTEP.
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4665](https://github.com/open-telemetry/opentelemetry-specification/pull/4665)
  - TL;DR; This is useful, but doesn't solve all of Browser's issues
- Browser related concerns
  - Browser doesn't care about session details / resource changes, they just want to grab "latest" bundle and report.
  - Will be doing "log/events", not necessarily more.
