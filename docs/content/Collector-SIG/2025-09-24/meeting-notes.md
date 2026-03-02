## Meeting Notes

### Attendees
- Edmo Vamerlatti (Elastic)
- João Duarte (Elastic)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- David Ashpole (Google)
- Tiffany Hrabusa (Grafana Labs)
- Dmitry Anoshin (Splunk)
- Curtis Robert (Splunk)
- Israel Blancas (Coralogix)
- Evan Bradley (Dynatrace)
- Bogdan Stancu (Adobe)
- Alex Boten (Honeycomb)
- Sam DeHaan (Grafana Labs)
- Roger Coll (Elastic)
- Paulo Dias (Five9)
- Jade Guiton (Datadog)
- [Pablo Baeyens](mailto:pablo.baeyens@datadoghq.com) (Datadog)

### Agenda
- [Joao] looking for sponsor for Enrichment Processor
  - Proposal: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41816](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/41816)
- [Israel] Is there anything missing from “Add URL sanitization feature to redaction processor” PR?
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/41774](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/41774)
  - Added information requested during Sept 10th call.
- [Gregor] I'm wondering if there's a need for a better integration test to catch things like [https://github.com/open-telemetry/opentelemetry-collector/issues/13727](https://github.com/open-telemetry/opentelemetry-collector/issues/13727) earlier
  - Slack: [https://cloud-native.slack.com/archives/C01N6P7KR6W/p1758625665805859](https://cloud-native.slack.com/archives/C01N6P7KR6W/p1758625665805859)
  - E.g. right now: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42902](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42902)
  - Testing tool used to detect the issue: [https://github.com/grafana/oats/](https://github.com/grafana/oats/)
    - Test suite: [https://github.com/grafana/docker-otel-lgtm/blob/main/examples/dotnet/oats.yaml](https://github.com/grafana/docker-otel-lgtm/blob/main/examples/dotnet/oats.yaml)
- [Roger] Plan for universal telemetry metrics? Should we start adding them to SemConv? V1? [https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/rfcs/component-universal-telemetry.md](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/rfcs/component-universal-telemetry.md)
  - Follow-up: [https://github.com/open-telemetry/opentelemetry-collector/issues/12909](https://github.com/open-telemetry/opentelemetry-collector/issues/12909) ?
  - “Trail of oteps”:
  - Semantic conventions
    - #otel-semantic-conventions
    - [OpenTelemetry: Semantic Conventions Working Group Meeting Notes](https://docs.google.com/document/d/10xG7DNKWRhxNmFGt3yYd3980a9uwS8lMl2LvQL3VNK8/edit?tab=t.0#heading=h.ylazl6464n0c) (calendar invite is at top)
- Yaten Dhingra
  - Interested in being a codeowner for awscloudwatchlogsexporter
- [Pablo] (Announcement) I want to stabilize configoptional.
  - See tracking issue: [https://github.com/open-telemetry/opentelemetry-collector/issues/13403](https://github.com/open-telemetry/opentelemetry-collector/issues/13403)
  - See PR: [https://github.com/open-telemetry/opentelemetry-collector/pull/13885](https://github.com/open-telemetry/opentelemetry-collector/pull/13885)
- Alf Kenny - tail sampling processor [proposal](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/42773), how can I appropriately invert a policy?
