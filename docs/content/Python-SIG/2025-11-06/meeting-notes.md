## Meeting Notes

### Attendees
- Riccardo Magliocchetti (Elastic)
- Aaron Abbott (Google)
- Keith Decker (Cisco/Splunk)
- Tammy Baylis (SolarWinds)
- Dylan russell (google)
- Bhaska Banerjee (CapitalOne)
- Hector Hernandez (Microsoft)

### Agenda
- [Riccardo] LGTM but we should fix type checking before merging [https://github.com/open-telemetry/opentelemetry-python/pull/4676#issuecomment-3472783613](https://github.com/open-telemetry/opentelemetry-python/pull/4676#issuecomment-3472783613)
- [Bhaskar] We want to inquire about the support for otlp/stdout exporter in JSON format for Python. Java already has this available In experimental phase . [Context](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/configuration/sdk-environment-variables.md#in-development-exporter-selection)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/4556](https://github.com/open-telemetry/opentelemetry-python/pull/4556)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/4470](https://github.com/open-telemetry/opentelemetry-python/pull/4470)
  - Riccardo:
    - If you can please try a protobuf less encoder, would be helpful for integration with other OTel projects like the operator and the injector
    - You can start from the other PR adding an http json exporter, even without the http exporter
  - Aaron: please use typechecking
