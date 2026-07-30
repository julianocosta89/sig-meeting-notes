## Meeting Notes

### Attendees
- Pablo Baeyens (Datadog)
- Douglas Camata (Coralogix)
- Evan Bradley (Dynatrace)
- Israel Blancas (Coralogix)
- Shaun Remekie (Coralogix)
- Braydon Kains (Google)
- João Duarte (Elastic)
- Rob Bavey (Elastic)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- [Sam DeHaan](mailto:sam.dehaan@grafana.com)(Grafana Labs)
- Christos Markou (Elastic)
- Alex Boten (Honeycomb)
- [Justin Hunter](mailto:justin@mydecisive.ai) (MyDecisive.ai)
- [Amanda Murphy](mailto:amurphy@hydrolix.io)(Hydrolix)
- [Chris Kirkwood-Watts](mailto:kirkwood@hydrolix.io)(Hydrolix)
- [Kyle Eckhart](mailto:kyle.eckhart@grafana.com) (Grafana Labs)
- Dmitry Anoshin (Splunk)
- Paulo Dias (Five9)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
  - Let's review the current states and make sure they are accurate
  - We need volunteers for fleshing out the required issues for each component issue (see [here](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130)) according to the [component stability guidelines](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/component-stability.md#stable)
    - Prometheus receiver: DONE by Arthur
    - Transform and filter processor: Evan will volunteer
    - Hostmetrics receiver: Mostly done by Braydon
    - K8sattributes processor: Christos
    - Resourcedetection processor: Pablo
    - Filelog receiver: Braydon will volunteer
  - Codeowners for the components
    - Filelog receiver only has one codeowner
    - Resource detection processor only has one active codeowner
    - ~~Pablo~~ Alex will volunteer to open a PR for adding the 'seeking codeowners' label ([https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44558](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44558)) (thanks Alex!)
- [Pablo] Wording change for requirements for new components [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44453](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44453)
- [Douglas] Request for reviews/opinions
  - Opampextension: somehow report the raw configuration files
    - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44341](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44341)
  - Supervisor: fallback configuration for starting Collectors
    - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44368](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44368)
  - Ebpf Profiler distro: adding pprof and health_check extensions
    - [https://github.com/open-telemetry/opentelemetry-collector-releases/pull/1274](https://github.com/open-telemetry/opentelemetry-collector-releases/pull/1274)
- [Evan] Set default time limit for holding data points in the cumulative-to-delta processor
  - [braydonk] If anybody wants to see this in action I did a talk that shows this problem with pprof profiles [https://youtu.be/qMxxjB4meXo?si=minA6CVpskgOIODv&t=261](https://youtu.be/qMxxjB4meXo?si=minA6CVpskgOIODv&t=261)
- [Shaun] Sponsorship for new component awsecsattributesd: [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44476](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44476)
- [Amanda] Sponsorship for Hydrolix exporter:  [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44327](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44327)
