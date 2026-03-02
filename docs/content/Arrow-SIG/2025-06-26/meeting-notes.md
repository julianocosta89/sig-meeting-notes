## Meeting Notes

### Attendees
- Albert Lockett (F5)
- Jake Dern (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Drew Relmas (Microsoft)
- David Dahl (F5)
- Josh MacDonald (Microsoft)
- Tristan Sloughter (MyDecisiveAI)
- Mihir (Culver Max Entertainment Pvt Ltd)
- Laurent Querel (F5)

### Agenda
- [Albert] - OTAP Encoding from proto structs & bytes
  - Discuss [feat: OTAP Logs Encoding from proto Structs with Views by albertlockett · Pull Request #625 · open-telemetry/otel-arrow · GitHub](https://github.com/open-telemetry/otel-arrow/pull/625)
  - This PR produces OTAP frames from Prost message objects directly via the trait
  - This week, working on decoding OTLP bytes as an implementation of the same trait
  - Performance? “OK”. Benchmarks showing cost of black_box visitor.
    - visit bytes directly vs visit bytes after decoding Prost objects: 20% improvement
    - Perf is not as great as we would like: there is some cost associated with random-access via the View which is being deserialized
    - Ownership complexity, use of a RefCell which may be hurting perf. Will continue.
    - Josh thinks this is good! We’re avoiding two passes
- [Josh/Drew] Can we begin to use the KQL query engine to write simple queries for our own logs?
  - LQ has asked for simple tools to filter events from our own datafusion
    - Laurent’s PR [Internal tracing proposal by lquerel · Pull Request #633 · open-telemetry/otel-arrow · GitHub](https://github.com/open-telemetry/otel-arrow/pull/633)
    - Laurent is interested in actually using our own query language for our own instrumentation.
    - See also [opentelemetry-collector/docs/rfcs/component-universal-telemetry.md at main · open-telemetry/opentelemetry-collector · GitHub](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/rfcs/component-universal-telemetry.md)
    - There will be differences in how we reason about and debug the dataflow engine because of the two channels (control and data). We will not tie ourselves to the Golang collector’s instrumentation design at this time, though they are similar.
- [Group] We are close to having a bare-bones Rust pipeline!
  - We also have a test framework; this is exciting.
  - Josh would like to run a test of the Go collector’s memorylimiterprocessor on throughput/latency. (for example)
  - Stay tuned! LQ is working on synchronization-aware connectors, getting close.
  - We will connect Albert’s view-parser work with an OTLP receiver.
- [Josh’s update] Will be working on Go/Rust interoperability, looking at the [rust2go](https://github.com/ihciah/rust2go) crate.
- [About yaml] Nevermind
- [About interop] Many ways to interoperate, at the “pipeline” or “node” level.
  - By “pipeline” level, we mean to separate pipelines into Rust and Go separately. In this model, we basically have two different runtimes.
  - By “node” level, we mean direct FFI-type integration.
