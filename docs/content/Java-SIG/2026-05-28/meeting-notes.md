## Meeting Notes

### Attendees
- Jack Berg (Grafana Labs)
- Jason (Splunk)
- Trask Stalnaker (Microsoft)
- Jonathan Halliday (IBM)
- Jack Shirazi (Elastic)
- Peter Findeisen (Cisco)
- Pranav Sharma (Google)
- Lauri Tulmin (Splunk)

### Agenda
- [jason] pretty please [https://github.com/open-telemetry/semantic-conventions-java/pull/489](https://github.com/open-telemetry/semantic-conventions-java/pull/489)
  - [jack] Speaking of which [https://github.com/open-telemetry/semantic-conventions-java/pull/483](https://github.com/open-telemetry/semantic-conventions-java/pull/483)
  - Related [https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/ibm-mq-metrics/src/main/java/io/opentelemetry/ibm/mq/metrics/MetricProducer.java](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/ibm-mq-metrics/src/main/java/io/opentelemetry/ibm/mq/metrics/MetricProducer.java)
  - Also related [https://github.com/open-telemetry/opentelemetry-android/pull/1773](https://github.com/open-telemetry/opentelemetry-android/pull/1773)
- [jack] Capture log bridge name as scope attributes [https://github.com/open-telemetry/opentelemetry-specification/pull/5089](https://github.com/open-telemetry/opentelemetry-specification/pull/5089)
- [Pranav] Question about implementing something that does not exist in spec?
- [jason] How do we feel about these incubating span processors?
  - [https://github.com/open-telemetry/opentelemetry-java/tree/bfb17f7c4d1d461149ac163ad46207f7ade6e746/sdk-extensions/incubator/src/main/java/io/opentelemetry/sdk/extension/incubator/trace](https://github.com/open-telemetry/opentelemetry-java/tree/bfb17f7c4d1d461149ac163ad46207f7ade6e746/sdk-extensions/incubator/src/main/java/io/opentelemetry/sdk/extension/incubator/trace)
- [trask] [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2785](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2785)
