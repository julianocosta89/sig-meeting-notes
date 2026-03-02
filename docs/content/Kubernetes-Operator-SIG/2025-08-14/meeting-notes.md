## Meeting Notes

### Attendees
- [Pavol Loffay](mailto:ploffay@redhat.com)(Red Hat)
- Antoine Toulme (Splunk)
- Jacob Aronoff

### Agenda
- Discuss the intent of [https://github.com/open-telemetry/opentelemetry-operator/pull/4201](https://github.com/open-telemetry/opentelemetry-operator/pull/4201)
- Discuss the managed CR implementation
  - Have the CR spawn CRs
    - Preferred as we have hooks for upgrades and maintenance.
  - Have the CR run the whole deployment
- Discuss [https://github.com/open-telemetry/opentelemetry-operator/issues/3340](https://github.com/open-telemetry/opentelemetry-operator/issues/3340) and a possible solution [https://github.com/open-telemetry/opentelemetry-operator/compare/main...jaronoff97:opentelemetry-operator:instrumentation-refactor](https://github.com/open-telemetry/opentelemetry-operator/compare/main...jaronoff97:opentelemetry-operator:instrumentation-refactor)
