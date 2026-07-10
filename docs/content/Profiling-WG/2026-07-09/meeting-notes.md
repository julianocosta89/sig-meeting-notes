## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) (Datadog)
- [Christos Kalkanis](mailto:christos.kalkanis@elastic.co) (Elastic).
- [Christian Simon](mailto:christian.simon@grafana.com) (Grafana Pyroscope)
- Roger Coll (Elastic)
- Nikola Grcevski (Grafana)
- [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) (Datadog)
- .
- .
- .

### Agenda
- Review action items:
  - [Alexey Alexandrov](mailto:aalexand@google.com) Add orphan checks to the conformance checker.
  - [Florian Lehner](mailto:florian.lehner@elastic.co) Add duplicate checks to the conformance checker.
  - [Alexey Alexandrov](mailto:aalexand@google.com) Clarify Profile.period_type and Profile.period semantics). See [this discussion](#bookmark=id.9nkv5styhrxf) below. And later discussion [here](#bookmark=id.j6n3lln9n34g).
    - Sent [#791](https://github.com/open-telemetry/opentelemetry-proto/pull/791)
  - [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) Open GH issue on including OTLP version in payloads.
  - [Christos Kalkanis](mailto:christos.kalkanis@elastic.co) Data Format PR
  - [Alexey Alexandrov](mailto:aalexand@google.com) Figure out what to do with this [older Profiles OTEP](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/profiles/0239-profiles-data-model.md). See [this discussion below](#bookmark=id.mjn7dj4yyazk).
    - Depends on [https://github.com/open-telemetry/opentelemetry-specification/pull/4965](https://github.com/open-telemetry/opentelemetry-specification/pull/4965)
    - This is blocked by christos PRs above. When they land, we can update the OTEP and point to these newer docs.
  - [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) Update thread context OTEP with appendix about go support
