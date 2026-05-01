## Meeting Notes

### Attendees
- Dónal O’Sullivan (Elastic)
- Giuseppe Ognibene (Coralogix)
- Nimrod Avni (Coralogix)
- Pablo Baeyens (Datadog)
- Dmitry Anoshin (Splunk)

### Agenda
- [Christos] Where do we stand with metrics’ stability? Do we require entities to be stable for a metric to be declared as stable?
  - Relates to “Promoting process attributes to RC PR” [https://github.com/open-telemetry/semantic-conventions/pull/3564#discussion_r3148396511](https://github.com/open-telemetry/semantic-conventions/pull/3564#discussion_r3148396511)
- [Dónal] Versioned metrics: Issue [here](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45592)
  - Configurable attributes per metric: [https://github.com/open-telemetry/opentelemetry-collector/pull/14281](https://github.com/open-telemetry/opentelemetry-collector/pull/14281)
    - To support this user needs to add the versioned metric to their user config, do we want to do this?
    - If this is not possible, should we just not support configurable attributes in versioned metrics and return an error?
- [Giuseppe / Nimrod] - [tcp / udp metrics proposal](https://github.com/open-telemetry/semantic-conventions/issues/3682)
