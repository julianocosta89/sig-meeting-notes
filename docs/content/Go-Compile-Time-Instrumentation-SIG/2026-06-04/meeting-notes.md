## Meeting Notes

### Attendees
- Kemal Akkoyun (Datadog); **Facilitator**
- Yang Yi (Alibaba)
- Huxing Zhang (Alibaba)
- Haibin Zhang (Alibaba)
- Dario Castañé (Datadog)
- Xabier Martinez (Cabify)
- Azhar Momin
- vyagh

### Agenda
- Xabier: [https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/500](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/500)
  - CONSENSUS - Integrations:
    - Have a limited number of instrumentations in our repo for quality assurance
      - grpc, nethttp, db, etc (standard library instrumentations, and the most popular)
      - (long-term) Alternative: Support [https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation) by adding `otelc` files and e2e-test. And assign our SIG as codeowners. We need to talk to the Go SDK SIG
    - Make [https://github.com/alibaba/loongsuite-go-agent/tree/main/pkg/rules](https://github.com/alibaba/loongsuite-go-agent/tree/main/pkg/rules) instrumentation completely compatible with `otelc` and provide `otelc.yaml` files in the modules and use the [https://opentelemetry.io/ecosystem/registry/](https://opentelemetry.io/ecosystem/registry/) to advertise them [https://opentelemetry.io/ecosystem/registry/adding/](https://opentelemetry.io/ecosystem/registry/adding/)
    - Version support:
      - The last major TWO versions need to be supported
- Huxing: Observability Day at KubeCon NA
  - [https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/observability-day/#registration-details](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/observability-day/#registration-details)
    - *Submit a proposal to speak! Submissions are being accepted through **Sunday, June 21, 2026.***
    - Also the maintainers day [https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/features-add-ons/project-opportunities/#dates-to-remember](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/features-add-ons/project-opportunities/#dates-to-remember)
    - Juraci:
      - Focus on the high-level value, not just the engineering problems
        - E.g. Seeing cool java auto-instrumentation and trying to build the same thing for Go
      - Problem Statement
      - Title is important
      - Abstract is critical
      - Find a TRUE (not related to a vendor) end-user to be on the stage
- Kemal: Remaining for V1 [https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/261](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/261)
