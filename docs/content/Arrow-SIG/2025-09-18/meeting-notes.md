## Meeting Notes

### Attendees
- Albert Lockett (F5)
- Josh MacDonald (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Tristan Sloughter (Groq)
- Jake Dern (Microsoft)

### Agenda
- [jmacd] Talk about [https://github.com/open-telemetry/otel-arrow/issues/1126](https://github.com/open-telemetry/otel-arrow/issues/1126)
  - Somewhat stuck on Sync + Send in admin control messages
  - Action: wait for Laurent, Josh will ask LQ how to attack this next week
- [jmacd] About this hackathon
  - Josh’s question is about which Arrow primitives would be useful for translating the Parquet exporter’s format back into OTAP.
  - E.g., we have read a set of primary logs from the logs parquet, want to read the log_attrs (or scope_attrs or resource_attrs) table.
  - Arrow schema is written to Parquet metadata. The arrow-rs schema is encoded in parquet metadata so that we expect the proper types. Question is sort of how to be efficient about slicing a part of the record batch (e.g., of log_attrs) to place them in a new OTAP batch.
  - Think about using the Arrow kernel that subtracts a constant from an array. Arrow::compute::cast, see this [https://docs.rs/arrow/latest/arrow/compute/kernels/numeric/fn.add.html](https://docs.rs/arrow/latest/arrow/compute/kernels/numeric/fn.add.html)
- [albert] albert hackathon
  - Demo of a KQL to datafusion logic query plan!
  - [https://github.com/open-telemetry/otel-arrow/compare/main...albertlockett:otel-arrow:albert/kql-to-df-poc?expand=1](https://github.com/open-telemetry/otel-arrow/compare/main...albertlockett:otel-arrow:albert/kql-to-df-poc?expand=1)
