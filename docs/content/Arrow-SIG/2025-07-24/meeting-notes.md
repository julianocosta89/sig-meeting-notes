## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Drew Relmas (Microsoft)
- Jake Dern (Microsoft)
- Albert Lockett (F5)
- Tristan Sloughter (MyDecisiveAI)
- David Dahl (F5)
- Utkarsh Umesan Pillai (Microsoft)

### Agenda
- [Laurent] Demo first operational mini pipeline.
  - This is ready for review. [First version of the engine capable of creating and executing a pipeline from a configuration by lquerel · Pull Request #532 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/532)
- [Drew] Release Process: [[Process] Improving otel-arrow Release process · Issue #737 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/737)
  - [[DRAFT] Release process improvements using otelbot by drewrelmas · Pull Request #739 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/739)
- [Jake] Missing delta dictionary support in arrow-rs
  - [Support delta-encoded dictionaries in the Arrow IPC format · Issue #6783 · apache/arrow-rs](https://github.com/apache/arrow-rs/issues/6783)
  - [arrow-rs/arrow-ipc/src/reader.rs at 16794ab14fa62ecf67de0da9460cc5752a9358f4 · apache/arrow-rs](https://github.com/apache/arrow-rs/blob/16794ab14fa62ecf67de0da9460cc5752a9358f4/arrow-ipc/src/reader.rs#L683)
- [Josh] FYI Rust/Go proposal shared with Collector SIG [[OTel-Arrow RFC]: Mixing Golang/Rust components by jmacd · Pull Request #13369 · open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector/pull/13369)
