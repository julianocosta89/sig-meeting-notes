## Meeting Notes

### Attendees
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)
- Alex Boten (Honeycomb)
- Dhruv Shah (Sumologic)
- Dylan Strohschein (Bindplane)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Tigran Najaryan
- [Sam DeHaan](mailto:sam.dehaan@grafana.com) (Grafana Labs)
- Arianna Vespri (OllyGarden)
- Kai Levin (Ericsson)
- Edmo Vamerlatti (Elastic)
- Israel Blancas (Coralogix)
- Blake Rouse (Elastic)
- Dmitry Anoshin (Splunk)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- Pavol Loffay (Red Hat)
- Neil Fajardo (New Relic)
- Douglas Camata (Coralogix)
- Curtis Robert (Splunk)
- Christos Markou (Elastic)
- [Kyle Eckhart](mailto:kyle.eckhart@grafana.com) (Grafana Labs)
- Mohammed ElDegwi
- Mikołaj Świątek (Elastic)
- David Ashpole (Google, 20 min late)
- Paulo Dias (Five9)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
  - [christos] how to link benchmark runs in the docs? [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44585#issuecomment-3920728270](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44585#issuecomment-3920728270)
- [Tigran, 15 min] Looking for collaborators to work on [STEF](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/stefexporter).
  - Presentation with relevant links here [STEF](https://docs.google.com/presentation/d/1VOO0xGHz5GEyipeIw-Y2vfwiO4wnJHvKSz83X1wUgzs/edit?slide=id.p#slide=id.p)
- [Dhruv Shah]
  - [Support config option under routing connector to copy data to only non-default pipelines](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45690)
    - [PR to understand the code changes required](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46106)
  - [[receiver/k8sObjects] Add support to persist resourceVersion across collector restart](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46017%20)
- [Kai] Understand community’s view on:
  - [Proposal: configurable mapping of Prometheus "job" label to service.name / prometheus.job.name · Issue #45982 · open-telemetry/opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/45982)
  - [Replace the `RemoteWriteQueue` and `WAL` with the exporterhelper queue (sending_queue) in Prometheusremotewriteexporter · Issue #33137 · open-telemetry/opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/33137?utm_source=chatgpt.com)
- [Pavol] Collector MCP / agentic workflow project [https://github.com/open-telemetry/community/pull/3128](https://github.com/open-telemetry/community/pull/3128)
- [Tiffany, can’t be present] FYI, if anyone has time to review, there’s a docs PR for the Phase 2 refactoring ready for eyes: [https://github.com/open-telemetry/opentelemetry.io/pull/9173](https://github.com/open-telemetry/opentelemetry.io/pull/9173)
