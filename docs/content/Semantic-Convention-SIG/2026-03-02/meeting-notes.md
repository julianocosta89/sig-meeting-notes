## Meeting Notes

### Attendees
- Josh Suereth
- Christophe Kamphaus
- Ruediger Schulze (IBM)
- Liudmila Molkova (Grafana Labs)
- Neil Yashinsky

### Agenda
- Triage
  - PR Triage Board: [https://github.com/orgs/open-telemetry/proje](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - [cts/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- [Liudmila] FYI exception events naming and severity [https://github.com/open-telemetry/semantic-conventions/pull/3311](https://github.com/open-telemetry/semantic-conventions/pull/3311)
  - What to do with background jobs?
- [trask] [Stabilize](https://github.com/open-telemetry/semantic-conventions/pull/3471) [`otel.event.name`](http://otel.event.name)
  - Supports java logging bridge.
- [trask] [Rename `service.peer.*` to `server.service.*` and `client.service.*`](https://github.com/open-telemetry/semantic-conventions/pull/3482)
  - AI - finalize the bikeshed on naming
    - SERVICE VS. APPLICATION (again) vs. something else.
    - [service.server.name](http://service.server.name) better than [server.service.name](http://server.service.name)?
- Thread in semconv channel - [https://cloud-native.slack.com/archives/C041APFBYQP/p1771941501331409](https://cloud-native.slack.com/archives/C041APFBYQP/p1771941501331409)
  - Should we make special "cancelled" option?
- Log type [https://github.com/open-telemetry/semantic-conventions/pull/3469](https://github.com/open-telemetry/semantic-conventions/pull/3469)
