## Meeting Notes

### Attendees
- [Juliano Costa](mailto:juliano.costa@datadoghq.com)(Datadog)
- Felix George (IBM)
- Shenoy Pratik (OpenSearch)
- Charles (Cortex)
- Mathew (Grafana)

### Agenda
- [Juliano] K6 license
  - [https://github.com/cncf/foundation/issues/1482](https://github.com/cncf/foundation/issues/1482)
- [Felix] Adding a LLM service
  - [https://github.com/open-telemetry/opentelemetry-demo/pull/3788](https://github.com/open-telemetry/opentelemetry-demo/pull/3788)
  - [Juliano] Concerns
    - Memory
    - Instrumentation
  - [Shenoy]
    - Are we solving the fuzzy match cache problem
  - Possible solution here, use the LLM service with the start-minimal so we drop Kafka, accounting and fraud-detection.
- Start & Stop failure scenarios
  - [https://github.com/open-telemetry/opentelemetry-demo/issues/2375](https://github.com/open-telemetry/opentelemetry-demo/issues/2375)
