## Meeting Notes

### Attendees
- Benedikt Bongartz (Red Hat)
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)(Elastic)
- Pavol Loffay (Red Hat)
- Israel Blancas (Coralogix)
- Antoine Toulme (Splunk)

### Agenda
- Review [feature gate](https://github.com/open-telemetry/opentelemetry-operator/blob/main/pkg/featuregate/featuregate.go) stability
- [Pavol Loffay](mailto:ploffay@redhat.com)[https://github.com/open-telemetry/opentelemetry-operator/pull/4583](https://github.com/open-telemetry/opentelemetry-operator/pull/4583)
  - Declarative config is only supported for some languages
  - A hybrid approach might be the best - keep the env vars and add declarative config.
  - Selector:  [https://github.com/open-telemetry/opentelemetry-operator/issues/2744](https://github.com/open-telemetry/opentelemetry-operator/issues/2744)
- [Benedikt Bongartz](mailto:bbongart@redhat.com)[https://github.com/open-telemetry/opentelemetry-operator/issues/4646](https://github.com/open-telemetry/opentelemetry-operator/issues/4646)
  - [https://github.com/open-telemetry/opentelemetry-operator/issues/2542#issuecomment-3079020579](https://github.com/open-telemetry/opentelemetry-operator/issues/2542#issuecomment-3079020579)
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is%3Aopen%20label%3Adiscuss-at-sig) (always last)
