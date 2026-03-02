## Meeting Notes

### Attendees
- Benedikt Bongartz (Red Hat)
- Mikołaj Świątek (Elastic)
- Vincent Desbois (Ericsson)
- Jacob Aronoff
- [Pavol Loffay](mailto:p.loffay@gmail.com)(Red Hat)
- Simon Olander (SAP)

### Agenda
- Skip release v0.132.0
  - [https://github.com/open-telemetry/opentelemetry-operator/pull/4320](https://github.com/open-telemetry/opentelemetry-operator/pull/4320)
  - Dotnet auto-instr. Failing?
- Discuss [Support range of OpenTelemetry Collector versions · Issue #4307 · open-telemetry/opentelemetry-operator](https://github.com/open-telemetry/opentelemetry-operator/issues/4307)
- Feedback on hostPID addition [https://github.com/open-telemetry/opentelemetry-operator/issues/4214](https://github.com/open-telemetry/opentelemetry-operator/issues/4214),  [https://github.com/open-telemetry/opentelemetry-operator/pull/4280](https://github.com/open-telemetry/opentelemetry-operator/pull/4280)
  - Try out to see if a work around is to run a Deployment with sidecar injection that has the correct settings (hostPID, securityContext etc).
  - Auditlogs part of Managed CRD?
    - [https://github.com/open-telemetry/opentelemetry-operator/issues/3818](https://github.com/open-telemetry/opentelemetry-operator/issues/3818)
      - Config:
        - Platform:
          - Logs:
            - Audit: enabled
          - Metrics:
            - Hostmetrics: enabled
          - Traces:
        - Applications:
          - Logs:
            - Selector: => namespace: abc
        - Instrumentation:
        - Export:
          - Otlp:
            - endpoint: something
