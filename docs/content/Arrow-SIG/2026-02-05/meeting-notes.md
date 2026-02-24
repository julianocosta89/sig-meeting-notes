## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Albert Lockett (F5)
- Jake Dern (F5)
- Aaron Marten (Microsoft)
- Tom Tan (Microsoft)
- Josh MacDonald (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Drew Relmas (Microsoft)
- Lalit Bhasin (Microsoft)

### Agenda
- Issue triage
  - (skip for today)
- Discussion:
  - [Laurent - 10-15min] Improved configuration format
  - [Jake 5-10 min]: [[Documentation] Create a formal OTAP spec · Issue #1957 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/1957)
    - Formal spec describing the behavior of the OTAP protocol
      - Related: Josh had proposed a path to making OTAP an official OpenTelemetry protocol [in this OTEP](https://github.com/open-telemetry/opentelemetry-specification/pull/4791). This requires content negotiation at a higher-level, would be a separate project.
    - Adding a set of validations in the OtapArrowRecord in the construction phase so some invariants/properties are guarantees (avoid defensive code in various places)
  - [Tom]: Issue labels renaming: [https://github.com/open-telemetry/otel-arrow/issues/1749#issuecomment-3850267431](https://github.com/open-telemetry/otel-arrow/issues/1749#issuecomment-3850267431)
    - Focus on triage-oriented labels
  - [Drew]: Require Rust-CI status checks for non-Ubuntu OS? Related to [Commits · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/1939)
    - Add some non-required targets such as macos,
  - [Josh or Gokhan; 5 minutes] Extension interfaces
