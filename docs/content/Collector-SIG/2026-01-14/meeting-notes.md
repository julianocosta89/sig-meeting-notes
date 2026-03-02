## Meeting Notes

### Attendees
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- Israel Blancas (Coralogix)
- Damien Mathieu (Elastic)
- Christos Markou (Elastic)
- [Edmo Vamerlatti](mailto:edmo.vamerlatti@elastic.co)(Elastic)
- [Perk Stożek (Marcin)](mailto:marcin.stozek@elastic.co)(Elastic)
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- [Bejal Lewis](mailto:bejal.lewis@grafana.com)(Grafana Labs)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
  - Pablo: [RFC for semantic conventions](https://github.com/open-telemetry/opentelemetry-collector/pull/14273) in progress
- [Andrzej] [Rename components to match naming convention #45339](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45339)
  - Thoughts on this? Next steps clear?
  - Update docs at [opentelemetry.io](http://opentelemetry.io)?
- [Israel] awsecsattributesd processor:
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44476](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44476)
  - Christos suggested splitting it into two processors. One would be a generic docker attributes processor. Would somebody be interested in sponsoring that new component?
- [Pablo] If you are attending [OTel Unplugged](https://events.humanitix.com/otelunplugged-eu2026) (February 2nd @ Brussels, right after FOSDEM), feel free to join [#otel-unplugged-eu-26](https://cloud-native.slack.com/archives/C0A8N53P0QJ) on the CNCF Slack
- [Pablo] Discussion about JSON schema generation happening later today, if you want to join DM me/Evan/Dmitrii
- [Evan] We are planning to make substantial breaking changes to OTTL’s API so we can add better type safety to the language. If you heavily use the API or like programming languages, we would appreciate your input.
