## Meeting Notes

### Attendees
- Pavol Loffay (Red Hat)
- iBenedikt Bongartz (Red Hat)
- Arthur Sens (Grafana Labs)
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)(Elastic)

### Agenda
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [Arthur Silva Sens](mailto:arthur.silvasens@grafana.com) - Enabling installation of OTel Injector with the operator.
  - There's been discussions around the Instrumentation CR.
  - There's a big difference in other operators with our operator, we are opt-in instead of opt-out.
  - Suggestion:
    - take a well supported language in the injector and do a PoC.
    - Create a new internal package for this work, since the existing code is a bit hard to reason about.
    - If we use a specific label it's more efficient to decide if we're using the old injection strategy or the new one.
- [Pavol Loffay](mailto:ploffay@redhat.com) - TLS Profile [https://github.com/open-telemetry/opentelemetry-operator/pull/4669](https://github.com/open-telemetry/opentelemetry-operator/pull/4669)
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)
