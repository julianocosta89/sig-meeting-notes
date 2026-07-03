## Meeting Notes

### Attendees
- Harrison Fritz (Capital One)
- Cruise Hall (Capital One)
- Jacob Aronoff (Tero)
- Mikołaj Świątek (Elastic)
- Pavol Loffay (Red Hat)
- Ozzy Walsh (Red Hat)

### Agenda
- [Harrison] [10 min] Discuss OTel Kubernetes Multitenancy - [issue 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/48895), issue 2 [operator CR proposal](https://github.com/open-telemetry/opentelemetry-operator/issues/1906). Design doc in progress [here](https://github.com/harrisonfritz/otel-multitenant-design).
  - Also similar to the patch approach [https://github.com/open-telemetry/opentelemetry-operator/pull/5144](https://github.com/open-telemetry/opentelemetry-operator/pull/5144)
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)We now have [coverage](https://app.codecov.io/github/open-telemetry/opentelemetry-operator/tree/main) uploaded for unit tests
  - Woohoo!!
- [Ozzy Walsh](mailto:ozwalsh@redhat.com) Updates to OBI RFC based on feedback [https://github.com/ozzywalsh/opentelemetry-operator/blob/obi-rfc/docs/rfcs/obi-agent.md](https://github.com/ozzywalsh/opentelemetry-operator/blob/obi-rfc/docs/rfcs/obi-agent.md)
- Does OBI use declarative config?
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)
