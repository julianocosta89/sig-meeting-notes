## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Albert Lockett (F5)
- Jake D (Microsoft)
- Tristan Sloughter
- Ray Jenkins (rotel/streamfold)
- Utkarsh Umesan Pillai (Microsoft)
- Drew Relmas (Microsoft)
- Josh MacDonald (Microsoft)

### Agenda
- Issue roundup
  - Josh broke several tests, added #[ignore], will not do again
  - Albert has filed a couple of bugs, one w/ Go components
    - We may need to encode version info
- Rotel
  - Coming from librato, snowflake
  - Performance concerns in OTel Collector
  - Discussion about OTAP architecture and motivations
  - Talk about plugins and componentization, interoperability
    - [[OTel-Arrow RFC]: Mixing Golang/Rust components by jmacd · Pull Request #13369 · open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector/pull/13369)
  - Talk about OTel-Arrow differences with the Go collector, hyper-edges, DAG
    - Josh: This is all sort of possible w/ Go collector, just not very formalized
  - To be continued.
- Instrumentation/Multivariate metrics framework
  - LQ presents a draft [[WIP] Internal metrics system by lquerel · Pull Request #946 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/946)
  - Strongly typed, multivariate, NUMA-aware.
  - Constant-value attributes
- AttributeProcessor and PData related operations
