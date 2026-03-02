## Meeting Notes

### Attendees
- Drew Relmas (Microsoft)
- Jake Dern (Microsoft)
- Albert Lockett (F5)
- Utkarsh Umesan Pillai (Microsoft)
- Josh MacDonald (Microsoft)

### Agenda
- Laurent: review scenarios for testing performance
  - OTLP-to-OTLP: no deserialize case (e.g., signal type router)
  - OTAP-to-OTAP: no deserialize case
  - Syslog-Attributes-Batch-OTLP: rename attribute, etc.
  - Syslog-Attributes-Batch-Parquet: to OTAP (“Barquet”), (difficult in Go)
  - Synthetic signal generator-to-OTAP or OTLP
  - Stretch goal:
    - Live reconfigure: to reconfig the individual node
    - Stretch^2: reconfigure the graph. T.B.D.
- Utkarsh/Josh: Talk about batching with Syslog receiver, UDP or TCP
  - To use views for singleton message?
  - Instead, use “embedded batching”
  - LQ: proposes a low-level batch, like Vec<Vec<u8>>, with async appender
  - Josh: looks like we have a pattern involving appending a PData to another PData
    - LQ: we have (Albert writing) a Pdata wrapper abstraction with state
    - JM: how about a simple approach, just build OTAP directly (Syslog-to-OTAP)
    - LQ: we could call this an “incremental view”.
    - Group: don’t do this first, just use a Vec<_> or binary buffer, have a multi-record view.
- Gokhan: saying hello, new member.
  - Q: must we run benchmarks (rust) on every CI/CD run? (only when rust changes, etc.)
  - LQ: no, the microbenchmarks we have are expensive and not very significant
  - LQ: we do want to have macrobenchmarks with historical performance, what Chris and Cijo are working on
