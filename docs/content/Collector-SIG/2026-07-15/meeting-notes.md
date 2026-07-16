## Meeting Notes

### Attendees
- Thomas Baldwin (Bloomberg)
- Mikiyas Bokan (Bloomberg)
- Matt Wear (Dash0)
- Marylia Gutierrez (Grafana)
- Blake Rouse (Elastic)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- Dylan Strohschein (Dynatrace)
- Yingrong Zhao (Honeycomb)
- Tyler Helmuth (Grafana Labs)
- Israel Blancas (Coralogix)
- Paulo Janotti (Splunk/Cisco)
- Mohammed ElDegwi
- Pablo Baeyens (Datadog)
- Ansen Garvin (New Relic)
- Curtis Robert (Splunk)
- Evan Bradley (Dynatrace)

### Agenda
- Inform [Marylia] Survey responses from the past 6 months
  - Collector
    - Total replies: 8
    - Avg Score: 4.4/5
    - Pros: Responsive, helpful maintainers; several contributors reported fast reviews and merges; positive, welcoming experience overall.
    - Improvements: Some requests for more timely reviews/merges and faster maintainer buy-in on issue comments before work begins.
  - Collector-contrib
    - Total replies: 76
    - Avg score: 4.25/5
    - Pros: Helpful and constructive reviewers when engaged; good CI checks and documentation; useful issues for newcomers; contributors learned a lot and several described the process as smooth or positive.
    - Improvements: Long and inconsistent review/merge times; inactive or unclear code owners; PRs idle for weeks or months; unclear escalation/bumping etiquette; stale bot feels demotivating; complex EasyCLA flow; CI and lint failures are hard to reproduce/fix; many contribution steps; large repository and frequent conflicts; unclear design expectations can cause major rework.
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/49274](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/49274)
- Discuss [Thomas / Mikiyas] Secrets Interface for extensions to use
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/48474](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/48474)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/49025](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/49025)
- Inform  [Pablo] I'll be migrating the Zoom link for this and other Collector SIG meetings to LFPCC see [https://github.com/open-telemetry/community/issues/3548](https://github.com/open-telemetry/community/issues/3548)
  - Recordings going forward will be available at [https://zoom-lfx.platform.linuxfoundation.org/meetings/opentelemetry](https://zoom-lfx.platform.linuxfoundation.org/meetings/opentelemetry?view=week)
  - You will need to join as a guest or log in to the LF platform
- Discuss [Evan] Configuring which statuses are retryable in the OTLP/HTTP exporter:
- Inform [Blake] Looking for more reviews on Partial Reload - Phase 1
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/15397](https://github.com/open-telemetry/opentelemetry-collector/pull/15397)
