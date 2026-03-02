## Meeting Notes

### Attendees
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)(Elastic)
- Israel Blancas (Coralogix)
- Joe Sirianni (Bindplane)
- Jacob Aronoff (Tero)
- Benedikt Bongartz (Red Hat)
- David Ashpole (Google)
- Pavol Loffay (Red Hat)

### Agenda
- Managed CRD
  - [https://github.com/open-telemetry/opentelemetry-operator/pull/4475](https://github.com/open-telemetry/opentelemetry-operator/pull/4475)
- Stabilizing prometheus receiver config: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44182](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44182)
- [Pavol Loffay](mailto:ploffay@redhat.com)TA feature flag operator.targetallocator.mtls
  - It only makes the secure connection between TA and collector
  - [https://github.com/open-telemetry/opentelemetry-operator/tree/main/cmd/otel-allocator#service--pod-monitor-endpoint-credentials](https://github.com/open-telemetry/opentelemetry-operator/tree/main/cmd/otel-allocator#service--pod-monitor-endpoint-credentials)
  - Secrets from the SA/pod are exposed in the TA endpoint (not related to the FF)
- [Pavol Loffay](mailto:ploffay@redhat.com)Instrumentation v1/v1beta1
  - [https://github.com/open-telemetry/opentelemetry-operator/milestone/5](https://github.com/open-telemetry/opentelemetry-operator/milestone/5)
  - Avoid conversion webhook - issues with namespace defined in the CRD for the webhook
  - CRDs should be installed before the operator?
    - [https://github.com/open-telemetry/opentelemetry-helm-charts/issues/1184](https://github.com/open-telemetry/opentelemetry-helm-charts/issues/1184)
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is:issue+is:open+label:discuss-at-sig) (always last)
