## Meeting Notes

### Attendees
- Israel Blancas (Coralogix)
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- Dmitry Anoshin (Splunk)
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)
- Pablo Baeyens (Datadog)
- Alex Boten (Honeycomb)
- Kalman Meth (IBM)
- Douglas Camata (Coralogix)
- Christos Markou (Elastic)
- Tiffany Hrabusa (Grafana Labs)
- Curtis Robert (Splunk)
- [Paulo Janotti](mailto:pjanotti@splunk.com) (Splunk)
- Sam DeHaan (Grafana Labs)

### Agenda
- [Pablo] v0.134.0 release post-mortem
  - Problems
    - [https://github.com/open-telemetry/opentelemetry-collector-releases/issues/1156](https://github.com/open-telemetry/opentelemetry-collector-releases/issues/1156)
    - [https://github.com/open-telemetry/opentelemetry-collector-releases/releases/tag/v0.134.0-nightly.202508310234](https://github.com/open-telemetry/opentelemetry-collector-releases/releases/tag/v0.134.0-nightly.202508310234)
    - [Douglas]: [https://github.com/open-telemetry/opentelemetry-collector/pull/13737](https://github.com/open-telemetry/opentelemetry-collector/pull/13737)
      - The versions in the release schedule got bumped without an explanation. Example: on 2025/09/08 (week after this call) the plan was to release 0.134.0, but now it will be 0.135.0? **Why?**
  - Proposals
    - Immediate fixes needed
      - Release v0.134.1
    - Changes in process/docs
      - [https://github.com/open-telemetry/opentelemetry-collector/pull/13749](https://github.com/open-telemetry/opentelemetry-collector/pull/13749)
      - [https://github.com/open-telemetry/opentelemetry-collector/issues/10797](https://github.com/open-telemetry/opentelemetry-collector/issues/10797)
      - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42465](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42465)
      - [https://github.com/open-telemetry/opentelemetry-collector-releases/issues/1160](https://github.com/open-telemetry/opentelemetry-collector-releases/issues/1160)
- [Andreas Tsarida] Looking for sponsor [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42384](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42384#issuecomment-3243107519) PR ready - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/42371](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/42371)
- [Yaten] For recording [`CLUSTER INFO`](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/42406) cmd metrics, should it be added in the [Scrape](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/redisreceiver/redis_scraper.go#L81) func? As for `INFO` cmd, why aren't all the metrics recorded (do we’ve to do the same for cluster_info)?
- [Tiffany] I’m looking for stakeholder feedback and approval on [this proposal](https://www.mindomo.com/mindmap/c6ececd0512d46edb8f5048d19f18de1) for rearchitecting the Collector documentation. There’s a [Slack thread](https://cloud-native.slack.com/archives/C01N6P7KR6W/p1756843654525619) if you’d like to leave feedback asynchronously.
- [Pablo - announcement] Intent to stabilize exporter (not exporterhelper) [https://github.com/open-telemetry/opentelemetry-collector/issues/12978](https://github.com/open-telemetry/opentelemetry-collector/issues/12978)
- [Raj] Adding the unroll processor to collector-contrib
  - [https://github.com/observIQ/bindplane-otel-collector/tree/main/processor/unrollprocessor](https://github.com/observIQ/bindplane-otel-collector/tree/main/processor/unrollprocessor)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41791#issuecomment-3211397778](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41791#issuecomment-3211397778)
- [Israel Blancas] Please review “Add URL sanitization feature to redaction processor”
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/41774](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/41774)
  - Jorge (thanks) addressed the concerns related to old dependency
  - Simplified config
- [Jean-Hadrien] [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41985](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41985)
- [Jmacd] Call for review on print-command improvements: [Revise the print-config command by jmacd · Pull Request #13679 · open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector/pull/13679)
