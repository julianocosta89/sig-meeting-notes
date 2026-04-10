## Meeting Notes

### Attendees
- [Ankit Bhadu](mailto:ankitbhadu@google.com) (Google)
- Josh Suereth
- Ayushi Asthana
- Anthony Mirabella (AWS)
- Dotan Horovits
- Tyler Kight (Microsoft)

### Agenda
- [Review required]  Stablize deployment environment attribute - [https://github.com/open-telemetry/semantic-conventions/pull/3584](https://github.com/open-telemetry/semantic-conventions/pull/3584)
- [Ayushi] Proposed “data” as an attribute group - [Introduce "data" attribute group in OTEL](https://docs.google.com/document/d/13jCkwYxS6pHTFTAPXqMljp2lTkO3FXKzKf34BFB2YEA/edit?usp=sharing)
  - Data.sensitivity demo : [https://github.com/open-telemetry/opentelemetry-demo/pull/3210](https://github.com/open-telemetry/opentelemetry-demo/pull/3210)
  - Data.category demo: [https://github.com/open-telemetry/opentelemetry-demo/pull/3215](https://github.com/open-telemetry/opentelemetry-demo/pull/3215)
  - Propagating data.sensitivity in baggage context - in progress.
- [Ayushi] Service.owner attribute - Can we zero down on open concerns from the group and the next steps?
- [Ayushi] Stabilizing service.criticality, earlier research on live use cases covered in [Criticality Semantics](https://docs.google.com/document/d/1-CpYLvDno6xb0eOw8bRvGwoac4kVtNXMZEF5ZXX0crs/edit?usp=sharing)
- [Dotan] otel community demo added attribute for service.criticality - merged
  - [https://github.com/open-telemetry/opentelemetry-demo/pull/2950#pullrequestreview-4076609847](https://github.com/open-telemetry/opentelemetry-demo/pull/2950#pullrequestreview-4076609847)
- [Tyler] (If time permits) question around standardization of AuthZ + AuthN as part of using standardized resource attributes in multi-cloud scenarios
