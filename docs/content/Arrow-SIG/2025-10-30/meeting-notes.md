## Meeting Notes

### Attendees
- Utkarsh (Microsoft)
- Josh M (Microsoft)
- Jake Dern (Microsoft)
- Danny Chin (CMU)
- Matthias Loibl (Polar Signals)

### Agenda
- Issue triage
  - One new issue about logs filter API
- About Datafusion
  - About Datafusion [https://www.youtube.com/watch?v=iJhRbDFJjbg](https://www.youtube.com/watch?v=iJhRbDFJjbg)
  - Talking about abstractions for observability query languages
    - PromQL: [promql_parser - Rust](https://docs.rs/promql-parser/latest/promql_parser/)
    - TraceQL
    - KQL
    - OTTL
    - Some more metrics:
      - Google “Monarch” : focus on “align” and “reduce”
      - Lightstep “UQL”
      - APL
      - OxQL
    - Note there is a Prometheus effort to store in Parquet files (SIG-Parquet)
- Josh’s question
  - Taking on the batch processor.
    - About optional ID columns in the logs signal
    - The code was being inconsistent about this detail
    - Josh will open a PR with more detailed questions outlined
- Question: on query
  - KQL, OTTL, and an intermediate representation
  - Likely: the intermediate representation is a logical plan tied with the OTAP model
