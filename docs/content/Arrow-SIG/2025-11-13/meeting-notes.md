## Meeting Notes

### Attendees
- Matthias Loibl
- Joshua MacDonald
- Aaron Marten
- Danny Chin
- Utkarsh Umesan Pillai
- Pablo Baeyens
- Jake Dern
- Albert Lockett
- Andres Borja
- Laurent Querel (joined mid Quiver conversation)

### Agenda
- Issue triage
  - About [crates.io](http://crates.io) and blockers for releasing (e.g., changelog, missing docs)
- Albert’s DataFusion planning exercise:
  - [https://github.com/open-telemetry/otel-arrow/issues/1394](https://github.com/open-telemetry/otel-arrow/issues/1394)
- Aaron’s Quiver proposal
  - [https://github.com/open-telemetry/otel-arrow/issues/1416](https://github.com/open-telemetry/otel-arrow/issues/1416)
  - About schema management: do we need one IPC log file per OTAP table?
  - Will we manage schema change the way OTAP-streams do?
  - How to manage references to on-disk segments, stream “state”
  - About how Parquet exporter addresses schema widening, sorting columns
  - LQ: Arrow has new encodings today; OTAP dynamic schemas were introduced because:
    - New encoding options: Run-end encoded arrows\
- Think about this until next time: What’s Phase 3 going to look like?
