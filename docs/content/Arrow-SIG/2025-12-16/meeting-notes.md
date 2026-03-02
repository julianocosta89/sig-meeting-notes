## Meeting Notes

### Attendees
- Albert Lockett (F5)
- Joshua MacDonald (Microsoft)
- Cijo Thomas (Microsoft)
- Aaron Marten (Microsoft)
- Danny Chin (CMU)
- Venkat Allam

### Agenda
- FYI: [Quiver segment reader/writer major PR](https://github.com/open-telemetry/otel-arrow/pull/1643)
- Topic: Albert’s query-engine processor [https://github.com/open-telemetry/otel-arrow/pull/1638](https://github.com/open-telemetry/otel-arrow/pull/1638)
  - Name is “transformprocessor”
  - Question about eager validation
  - Current is “lazy” because we do not have an Arrow schema until data arrives
- Topic: Josh’s batch processor for OTLP bytes [[batch_processor] Support bytes-based batching via new `format = [otap|otlp|preserve]` by jmacd · Pull Request #1633 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/1633)
  - New `format` configuration supports “otap”, “otlp”, “preserve”.
- Topic: Josh’s query-engine processor (for KQL “recordset”) [https://github.com/open-telemetry/otel-arrow/pull/1642](https://github.com/open-telemetry/otel-arrow/pull/1642)
  - Note: there is a Python language, “IBIS-framework”, a framework for query that supports multiple SQL backends, PRQL, pipe-SQL
    - [https://github.com/ibis-project/ibis](https://github.com/ibis-project/ibis)
    - https://github.com/PRQL/prql
  - Talk of Greptime’s Prometheus parser, and its use of datafusion
    - [https://github.com/GreptimeTeam/promql-parser](https://github.com/GreptimeTeam/promql-parser)
    - https://github.com/GreptimeTeam/greptimedb/blob/main/src/query/src/planner.rs
