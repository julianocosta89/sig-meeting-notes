## Meeting Notes

### Attendees
- [Paulo Janotti](mailto:pjanotti@splunk.com) (Splunk)
- [Sam DeHaan](mailto:sam.dehaan@grafana.com) (Grafana)
- Douglas Camata (Coralogix)
- Jonathan Silva(Ollygarden)
- Evan Bradley (Dynatrace)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- [Pankaj Kumar](mailto:pankaj.kumar@sumologic.com) (Sumologic)
- Arianna Vespri (Ollygarden)
- Mikołaj Świątek (Elastic)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Israel Blancas (Coralogix)
- Dakota Paasman (Bindplane)
- Andy Keller (Bindplane)
- Tyler Helmuth (Honeycomb)
- Trent Vigar (MyDecisive)
- [Kyle Eckhart](mailto:kyle.eckhart@grafana.com) (Grafana Labs)
- [Pavol Loffay](mailto:p.loffay@gmail.com)(Red Hat)
- Ishay Shor (Tangent Logic)
- Curtis Robert (Splunk)
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)
- Justin Hunter ([MyDecisive.ai](http://MyDecisive.ai))
- Neil Fajardo ( New Relic )
- Jill Magsaysay (MyDecisive)

### Agenda
- [15 min] Go through high priority issues for [stability phase 1](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44130) listed on the [**board**](https://github.com/orgs/open-telemetry/projects/178)
- [Trent] Discuss next steps/ownership and approach for enabling collector config updates
  - I started [asking](https://cloud-native.slack.com/archives/C02J58HR58R/p1765395440077059) about this topic when I determined the supervisor approach wouldn’t work for me and wanted to find a way to do it in the collector
  - Approaches discussed
    - Opamp extension handles remote config update and sends SIGHUP (potentially SIGUSR2 for windows support)
    - [ChangeEvent](https://github.com/open-telemetry/opentelemetry-collector-contrib/compare/main...TylerHelmuth:opentelemetry-collector-contrib:tyler.experiment-with-opampprovider#diff-2bf0e688ad56a8b568141cc56036437fc05fd411dcc1d37d732c833a4f58d85aR152)
    - Adding the opamp client directly into the collector
      - More access?
    - Opamp [provider](https://github.com/open-telemetry/opentelemetry-collector-contrib/compare/main...TylerHelmuth:opentelemetry-collector-contrib:tyler.experiment-with-opampprovider)
  - Outstanding issues
    - Bad config updates (validation) not causing a shutdown
    - Reverting to good config
- [Pankaj] [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44423](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/44423)
  - [Paulo Janotti](mailto:pjanotti@splunk.com) will review the proposal
- [Mikołaj] Transitions between component statuses with the same value ([#14282](https://github.com/open-telemetry/opentelemetry-collector/issues/14282))
- [Andrewvc] Discuss routing connector inference / dynamic routing
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44762/](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/44762/)
  - Maybe borrow syntax from [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/36809#issuecomment-3666379191](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/36809#issuecomment-3666379191)
