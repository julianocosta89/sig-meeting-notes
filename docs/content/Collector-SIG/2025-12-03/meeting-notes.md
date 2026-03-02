## Meeting Notes

### Attendees
- [Pankaj Kumar](mailto:pankaj.kumar@sumologic.com) (Sumologic)
- [Laurent Dufresne](mailto:laurent.dufresne@grafana.com) (Grafana Labs)
- Douglas Camata (Coralogix)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Israel Blancas (Coralogix)
- Christos Markou (elastic)
- [Pavol Loffay](mailto:p.loffay@gmail.com)(Red Hat)
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- João Duarte (Elastic)
- Rob Bavey (Elastic)
- Edmo Vamerlatti (Elastic)
- Evan Bradley (Dynatrace)
- Antoine Toulme (Splunk)
- [Marcin “Perk” Stożek](mailto:perk@elastic.co)(Elastic)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- [Pankaj] [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44423](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44423)
- [Laurent] [https://github.com/open-telemetry/opentelemetry-collector/issues/14246](https://github.com/open-telemetry/opentelemetry-collector/issues/14246)
- [Douglas] Still waiting for review/comments on:
  - Report config file content via opamp: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44341](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44341)
    - Implementation plan would be very helpful.
    - Detail more the writing in the issue
      - Potential for secrets to appear, even before env var expansion
      - No plan for running env var expansion
      - Could make this an opt-in feature with a warning that secrets can be leaked
  - Fallback config for Supervisor: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44368](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44368)
- [Douglas] I bring many opamp related topics to this call due to incompatibility with the time of the OpAMP SIG call.
  - Open an issue to talk about it in [https://github.com/open-telemetry/community](https://github.com/open-telemetry/community)
- [Pavol] collector config schema
  - What is the status of improving collector config schema?
  - [https://github.com/open-telemetry/opentelemetry-collector/issues/9769](https://github.com/open-telemetry/opentelemetry-collector/issues/9769)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42214](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42214)
  - I am working on MCP server to simplify collector configuration
  - [https://github.com/pavolloffay/opentelemetry-mcp-server/tree/main/modules/collectorschema](https://github.com/pavolloffay/opentelemetry-mcp-server/tree/main/modules/collectorschema)
  - Example schema: [https://github.com/pavolloffay/opentelemetry-mcp-server/blob/main/modules/collectorschema/schemas/0.139.0/receiver_otlp.yaml](https://github.com/pavolloffay/opentelemetry-mcp-server/blob/main/modules/collectorschema/schemas/0.139.0/receiver_otlp.yaml)
- [Israel] Please review this PR from the redaction processor to improve the db and url sanitization:
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44577](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44577)
  - Multiple improvements
  - Fix issue when all the db statements are enabled
