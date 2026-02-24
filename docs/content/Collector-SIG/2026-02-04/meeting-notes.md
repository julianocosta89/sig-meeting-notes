## Meeting Notes

### Attendees
- Israel Blancas (Coralogix)
- Douglas Camata (Coralogix)
- Ulysses Souza (Coralogix)
- Dakota Paasman (Bindplane)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Pierre Prinetti (Datadog)
- [Blake Rouse](mailto:blake.rouse@elastic.co) (Elastic)
- Edmo Vamerlatti (Elastic)
- Christos Markou (Elastic)
- Mark Sta Ana (Smart Pension)
- Vojta Vojacek (SolarWinds)
- Marcin “Perk” Stożek (Elastic)
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co)(Elastic)
- Mikołaj Świątek (Elastic)
- Kai Levin (Ericsson)
- [Paulo Dias](mailto:paulodias.gm@gmail.com) (Five9)
- Dhruv Shah (Sumologic)
- Damien Mathieu (Elastic)
- Donal O’Sullivan (Elastic)
- Jordi Vilaseca (Tinybird)
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)
- Pablo Baeyens (Datadog)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14479/files](https://github.com/open-telemetry/opentelemetry-collector/pull/14479/files)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44175](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44175)
- [Israel] Can we have [this PR](https://github.com/open-telemetry/opentelemetry-collector/pull/14247) merged? It is has been marked as “ready to merge” for some time
- [Blake] - Enable partial pipeline reload to reduce downtime
  - [https://github.com/open-telemetry/opentelemetry-collector/issues/14529](https://github.com/open-telemetry/opentelemetry-collector/issues/14529)
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14490](https://github.com/open-telemetry/opentelemetry-collector/pull/14490)
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14513](https://github.com/open-telemetry/opentelemetry-collector/pull/14513)
- [Dhruv] Need inputs on feature request:
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45690](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45690)
- [Perk] does the contrib collector API (aka configuration) seem inconsistent a bit?
  - Food for thought
  - Start with filing an issue
  - Maybe we should have guidelines for how components are structured and named
