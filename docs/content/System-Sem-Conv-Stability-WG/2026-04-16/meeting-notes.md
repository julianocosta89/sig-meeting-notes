## Meeting Notes

### Attendees
- Dónal O’Sullivan (Elastic)
- Dmitry Anoshin (Splunk)
- Braydon Kains (Google)

### Agenda
- [Roger] [https://github.com/open-telemetry/semantic-conventions/issues/3621](https://github.com/open-telemetry/semantic-conventions/issues/3621)
  - Join to spec SIG and see what there thoughts are.
  - Native field, can be part of the identity
  - Semantic convention guidance?
  - Window duration of some metrics is not added to the metric name, this is bad.
  - At least have a new field that can have the same meaning as unit.
- [Dónal] Process PRs:
  - Move process.executable to its own entity:
    - Need to resolve comments: [https://github.com/open-telemetry/semantic-conventions/pull/3536](https://github.com/open-telemetry/semantic-conventions/pull/3536)
  - Update process.executable.build_id.htlhash description:
    - [https://github.com/open-telemetry/semantic-conventions/pull/3609](https://github.com/open-telemetry/semantic-conventions/pull/3609)
    - Good to go.
  - Promote Process to RC:
    - [https://github.com/open-telemetry/semantic-conventions/pull/3564](https://github.com/open-telemetry/semantic-conventions/pull/3564)
    - Good to go.
