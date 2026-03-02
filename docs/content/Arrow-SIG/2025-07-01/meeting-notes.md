## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Utkarsh Umesan Pillai (Microsoft)
- Jake Dern (Microsoft)
- David Dahl (F5)
- Mike Blanchard (Microsoft)
- Jacob Abraham (F5)

### Agenda
- [Laurent] on behalf of Albert: Implementation of the direct OTAP encoding for logs
  - Conclusion: based on the benchmark results, we will only maintain OTAP pipeline engine
- [Utkarsh] [[otap-dataflow] Add SyslogCEFReceiver by utpilla · Pull Request #655 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/655)
- [Laurent] on behalf of Joshua: Go Collector ← → Rust dataflow engine interop
- [Laurent]: First working version of the Rust dataflow engine
- [Blanch]: Query engine update
  - Pipeline expression (Rust construct)
  - Expression tree abstraction in order to run the query over multiple backends (apache arrow+datafusion, basic “OTLP query engine”)
  - OTTL -> Expression tree -> Query Engine -> Output
  - KQL -> Expression tree
  - Expose this processor to the Go Collector (explored by Tom)
