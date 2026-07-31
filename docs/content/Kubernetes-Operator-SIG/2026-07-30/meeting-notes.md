## Meeting Notes

### Attendees
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)(Elastic)
- [Pavol Loffay](mailto:ploffay@redhat.com)(Red Hat)
- Jacob Aronoff (Tero)

### Agenda
- [Mikołaj] Using a cp binary built straight from GNU coreutils in instrumentation images
  - 👍
- [Mikołaj] PSA: [Preparation underway](https://github.com/open-telemetry/opentelemetry-operator/pull/5348) for Go e2e tests
- [[Pavol Loffay](mailto:ploffay@redhat.com)] Test collector components:
  - In the operator we should test only components that are operator and/or kubernetes specific (e.g. no filterprocessor)
  - Run the tests nightly and collector upgrade
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
  - [https://github.com/open-telemetry/opentelemetry-operator/issues/5394](https://github.com/open-telemetry/opentelemetry-operator/issues/5394)
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)
