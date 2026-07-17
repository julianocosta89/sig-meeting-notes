## Meeting Notes

### Attendees
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)(Elastic)
- Jacob Aronoff (Tero)
- Israel Blancas (Coralogix)
- Tyler Helmuth (Grafana Labs)

### Agenda
- [Tyler]: [Instrumentation CR default image version](https://github.com/open-telemetry/opentelemetry-operator/issues/5255)
  - We want to do this, need to solve the packages problem. New autoinstrumentation packages are not discoverable. Need to define when we release new packages, what the version scheme is.
  - The otel injector helps us too. But the injector doesn’t target all the architectures our auto-instrumentation images target.
  - We want to do this for v1beta1. Tyler will update the issue with a plan for how to address maturity/discovery issues.
  - Release process ideas for images:
    - Make it like helm chart, publish a new version on every change
    - Versioning could follow linux package distribution pattern
      - So for java we could do `v2.29.0-1` or something similar
    - Document packages better in the repo and in published destinations
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)
