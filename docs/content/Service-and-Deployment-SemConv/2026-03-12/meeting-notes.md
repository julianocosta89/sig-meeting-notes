## Meeting Notes

### Attendees
- [Ankit Bhadu](mailto:ankitbhadu@google.com) (Google)
- Josh Suereth
- Ayushi Asthana
- Anthony Mirabella (AWS)

### Agenda
- [Ayushi] “Data” entity proposal
  - Instrumentation considerations for data entity [Introduce "data" entity in OTEL](https://docs.google.com/document/d/13jCkwYxS6pHTFTAPXqMljp2lTkO3FXKzKf34BFB2YEA/edit?tab=t.0#heading=h.cnoqyoyrcz59)
  - Conclude on data vs data_source (reqd to formally create a proposal in [https://github.com/open-telemetry/semantic-conventions/issues](https://github.com/open-telemetry/semantic-conventions/issues) )
- [Ankit] Service.business_unit.id:
  - [https://github.com/open-telemetry/semantic-conventions/issues/3475](https://github.com/open-telemetry/semantic-conventions/issues/3475)
    - An OTel demo on how this attribute can be used (in grafana dashboard for example) would help with the case.
    - It is better to decide whether business_unit should be a different attribute or go inside service.owner.* when we have reached a conclusive definition for service.owner.* [PR for service.owner](https://github.com/open-telemetry/semantic-conventions/pull/3268)
