## Meeting Notes

### Attendees
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Mikołaj Świątek (Elastic)
- Christos Markou (Elastic)
- Pablo Baeyens (Datadog)
- Israel Blancas (Coralogix)
- Vojta Vojacek (SolarWinds)
- [Ravishankar Gnanaprakasam](mailto:r.gnanaprakasam@sumologic.com)(Sumologic)
- Mohammed ElDegwi
- Edmo Vamerlatti (Elastic)
- Dónal O’Sullivan (Elastic)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
  - Inform  [Pablo] Please review [https://github.com/open-telemetry/opentelemetry-collector/pull/15175](https://github.com/open-telemetry/opentelemetry-collector/pull/15175)!
    - Note that it is still marked as draft
  - Inform  [Pablo] Consumer error partial success discussion underway but not ready for RFC yet, talk to Braydon if you want an early version
  - Discuss  [Mikolaj] Changes to configuration in stable components that are not 1.x
    - There is nothing specific on the confighttp documentation that says it is unstable
      - Mikolaj would err on the side of stability
      - Evan volunteered to write something, it is difficult to write something specific
      - Pablo to ping Evan and Mikolaj on Slack as a follow up
- Discuss [Ravishankar] Discuss regarding [comment](https://github.com/open-telemetry/opentelemetry-collector/issues/8122#issuecomment-4304452455)
  - [Jade] Suggestion: An option in the persistent queue specifically, to delay writes in order to sync multiple at once, without changes to the overall queue functionality
- Discuss [Mikołaj] Expanding the storage client interface ([issue](https://github.com/open-telemetry/opentelemetry-collector/issues/15191))
  - Casting seems like a good way of accessing this
