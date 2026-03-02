## Meeting Notes

### Attendees
- Edmo Vamerlatti (Elastic)
- Dmitry Anoshin (Splunk)
- [Paulo Janotti](mailto:pjanotti@splunk.com) (Splunk)
- Douglas Camata (Coralogix)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- Israel Blancas (Coralogix)
- Alex Boten (Honeycomb)
- Evan Bradley (Dynatrace)
- Constanca Manteigas (Elastic)
- David Ashpole (Google)
- Bogdan Stancu (Adobe)
- Tiago Queiroz (Elastic)
- Josh MacDonald (Microsoft)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Antoine Toulme (Splunk)

### Agenda
- [Pablo (may arrive later, if so please move further down] Allow passing `enabled` to `configoptional.Optional` fields so that we can have enabled-by-default fields [https://github.com/open-telemetry/opentelemetry-collector/pull/13995](https://github.com/open-telemetry/opentelemetry-collector/pull/13995)
- [Jade] Supporting lists of name/value pairs for configgrpc/confighttp headers
- [Evan] Revisiting UnmarshalV2
- [Bogdan] Looking for sponsors for [circuitbreakerextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/43028)
- [Bogdan] Questions about defining Collector SLIs
- [Douglas] OpAMP Supervisor Linux packages (deb/rpm)
  - Will require user intervention to put the Supervisor and Collector configs in place to work.
- [Paulo] Removing Windows 2022 from large test matrices [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/43436](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/43436)
- [Josh M] Requesting reviews for RFC on extension APIs and patterns in the code base [https://github.com/open-telemetry/opentelemetry-collector/pull/13902](https://github.com/open-telemetry/opentelemetry-collector/pull/13902)
