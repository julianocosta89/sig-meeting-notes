## Meeting Notes

### Attendees
- Utkarsh (Microsoft)
- Josh M (Microsoft)
- Jake Dern (Microsoft)
- Albert Lockett (F5)
- Danny Chin (CMU)
- Aaron Marten (Microsoft)

### Agenda
- Issue triage
- Open discussions
  - About [Internal telemetry metrics dispatcher · Issue #1378 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/1378)
    - Goals? Are we replacing the OTel SDK
    - Or are we taking shortcuts
    - Choices:
      - Use the otap-dataflow engine pipeline for egress
      - Use the OTel-Rust SDK for egress, with views configuration
      - Use custom logic / configuration for egress
    - Potentially, use of otap_df_config structs to build internal telemetry graph
