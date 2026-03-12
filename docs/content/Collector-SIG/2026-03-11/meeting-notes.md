## Meeting Notes

### Attendees
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Andy Keller (Bindplane)
- [João Duarte](mailto:joao@elastic.co) (Elastic)
- Antoine Toulme (Splunk)
- Paulo Janotti (Splunk)
- Dylan Strohschein (Bindplane)
- Curtis Robert (Splunk)
- [Blake Rouse](mailto:blake.rouse@elastic.co) (Elastic)
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co) (Elastic)
- Mohammed ElDegwi
- Christos Markou (Elastic)
- Edmo Vamerlatti (Elastic)
- Josh MacDonald (Microsoft)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- [Paulo Janotti] Windows tier support:
  - windows/amd64 currently tier 2, would like to move to tier 1 - [https://github.com/open-telemetry/opentelemetry-collector/issues/11567](https://github.com/open-telemetry/opentelemetry-collector/issues/11567)
  - windows/arm64 currently tier 3, would like to move to tier 2 - (specific issue created after the SIG meeting [https://github.com/open-telemetry/opentelemetry-collector/issues/14758](https://github.com/open-telemetry/opentelemetry-collector/issues/14758) )
- [Blake Rouse](mailto:blake.rouse@elastic.co) [RFC] Partial reload
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14640](https://github.com/open-telemetry/opentelemetry-collector/pull/14640)
  - Discussion about the scope of the change, the size of the change, the levels of reload that are possible.
- [Mikołaj Świątek](mailto:mikolaj.swiatek@elastic.co) Component status reporting for shared components ([#14692](https://github.com/open-telemetry/opentelemetry-collector/issues/14692))
  - See notes in the issue.
- [Kai, can’t be present] FYI — if anyone can review [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45982#issuecomment-3967015182](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45982#issuecomment-3967015182), it’s a blocker for us. Any maintainer feedback on whether the proposed direction is worth pursuing(so we know whether to invest in a PR) would be greatly appreciated. Thanks!
