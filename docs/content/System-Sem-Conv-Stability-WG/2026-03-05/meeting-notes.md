## Meeting Notes

### Attendees
- Dónal O’Sullivan (Elastic)
- Christos Markou (Elastic)
- Dmitry Anoshin (Splunk)
- Pablo Baeyens (Datadog)

### Agenda
- [dmitry] wrapping up the reaggregation PRs [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46627](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46627)
  - Next step is to make cpu an optional attribute according to semconv
- [Pablo] Are we ready to merge [https://github.com/open-telemetry/semantic-conventions/pull/3461](https://github.com/open-telemetry/semantic-conventions/pull/3461) ?
  - Remove fixes from PR, as we need to create a PR for metrics update.
- [Pablo] Could process.status be an additive change after GA? ([https://github.com/open-telemetry/semantic-conventions/issues/1181](https://github.com/open-telemetry/semantic-conventions/issues/1181))
- What are the pros/cons of moving process.executable to its own entity,
  - Dónal will create an issue about this and bring Thomson into the discussion.
