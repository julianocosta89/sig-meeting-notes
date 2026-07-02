## Meeting Notes

### Attendees
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)(Elastic)
- Douglas Camata (Coralogix)
- Israel Blancas (Coralogix)
- [Blake Rouse](mailto:blake.rouse@elastic.co)(Elastic)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Christos Markou
- [Ravishankar Gnanaprakasam](mailto:r.gnanaprakasam@sumologic.com)(Sumologic)
- Mohammed ElDegwi
- Pablo Baeyens (Datadog)
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
  - Inform K8s attributes processor graduation issue [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/49274](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/49274)
- Inform [Blake Rouse](mailto:blake.rouse@elastic.co) Partial reload phase 1 - receivers only
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/15397](https://github.com/open-telemetry/opentelemetry-collector/pull/15397)
- Discuss [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co)As a receiver author, how do I interact with exporterhelper queues to guarantee durability? (leave for end)
  - Open an issue to recommend an approach similar to the otlp receiver
