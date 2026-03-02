## Meeting Notes

### Attendees
- Drew Relmas (Microsoft)
- Mike Blanchard (Microsoft)
- Albert Lockett (F5)
- Laurent Querel (F5)
- Josh MacDonald (Microsoft)

### Agenda
- Syntax extension PR [https://github.com/open-telemetry/otel-arrow/pull/1734](https://github.com/open-telemetry/otel-arrow/pull/1734) and [https://github.com/open-telemetry/otel-arrow/pull/1722](https://github.com/open-telemetry/otel-arrow/pull/1722)
- Discussion about summary - record set engine supports it, and OTTL Bridge adds the summary as an additional log record [https://github.com/open-telemetry/otel-arrow/blob/a2b3698c369bc0ea91874aee3ba5ca43cbb0ed68/rust/experimental/query_engine/engine-recordset-otlp-bridge/src/bridge.rs#L311](https://github.com/open-telemetry/otel-arrow/blob/a2b3698c369bc0ea91874aee3ba5ca43cbb0ed68/rust/experimental/query_engine/engine-recordset-otlp-bridge/src/bridge.rs#L311)
  - It’s be nice if there was a place on the OTLP spec to put the summaries (analytical capabilities)
