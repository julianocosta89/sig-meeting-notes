## Meeting Notes

### Attendees
- [Andrew Wilkins](mailto:axw@elastic.co) (Elastic)
- [Dmitrii Anoshin](mailto:danoshin@splunk.com) (Splunk)
- [Antoine Toulme](mailto:atoulme@splunk.com) (Splunk)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- ~~[Andrew] :forever-alone:~~
- [Dmitrii/Andrew] Partitioning & ARC
  - Intra-batch partitioning: [https://github.com/open-telemetry/opentelemetry-collector/issues/12795#issuecomment-3631214646](https://github.com/open-telemetry/opentelemetry-collector/issues/12795#issuecomment-3631214646)
  - ARC: [https://github.com/open-telemetry/opentelemetry-collector/issues/14080](https://github.com/open-telemetry/opentelemetry-collector/issues/14080)
  - Should we have an extension interface for injecting these behaviours into exporters?
  - Andrew to come back with a more detailed comparison of a partitioner extension interface vs. partitioner processor + metadata partition config
- [Dmitrii] metadata.yaml: metrics & resource attribute changes to accommodate entities
- [Andrew] confignet in confighttp
  - [https://github.com/open-telemetry/opentelemetry-collector/pull/14248](https://github.com/open-telemetry/opentelemetry-collector/pull/14248)
  - Look into policies around embedding
  - Keep and deprecate Endpoint field?
  - Hold off on ReusePort PR?
