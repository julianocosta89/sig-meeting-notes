## Meeting Notes

### Attendees
- Mike Blanchard (Microsoft)
- Laurent Querel (F5)
- Albert Lockett (F5)
- Drew Relmas (Microsoft)

### Agenda
- Discussion of PR [https://github.com/open-telemetry/otel-arrow/pull/1477](https://github.com/open-telemetry/otel-arrow/pull/1477) columnar query engine filtering
  - Uses datafusion physical expression to produce selection vectors & arrow compute functions to combine those together
  - Main motivation was b/c of difficulty of multiple tables encompassing a single batch
- View discussion
  - Attributes as virtual columns (similar to polarsignal’s dynparquet). Is it possible w/ custom Table Provider?
  - would need to implement Array for the virtual columns somehow
  - Not needed for now based on impl in #1477
- OPL Followup from MS side
  - Mission is not to tie current query language to a particular language -- having support in the AST expressions is the focus, less so transpiler of a new language
  - Discussion of [record set engine](https://github.com/open-telemetry/otel-arrow/tree/main/rust/experimental/query_engine/engine-recordset%20) - processes data that isn’t in the columnar format. It can process data that’s not structured as OTel. Record sets can have any schema, they’re more general than just OTel records. OTLP bridge links OTel logic to the record set engine.
