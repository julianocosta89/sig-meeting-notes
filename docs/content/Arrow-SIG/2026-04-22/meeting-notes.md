## Meeting Notes

### Attendees
- Josh MacDonald (Microsoft)
- Laurent Querel (F5)
- Albert Lockett (F5)
- Gokhan Uslu (Microsoft)
- Jake Dern (F5)
- Aaron Marten (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Max Jacinto
- Cijo Thomas (Microsoft)
- Tom Tan (Microsoft)

### Agenda
- [Triage]
  - Note! Try to modify triage labels
  - Through #2725
- [About processor chain]
  - 2569 and 2669: initial requirements are much smaller in scope
  - We seem to have difficulty, consider just solving the instrumentation problem
- [About crates publishing: start with opentelemetry-otap-views
- [Live reconfiguration]
  - [https://github.com/open-telemetry/otel-arrow/pull/2618](https://github.com/open-telemetry/otel-arrow/pull/2618) will review next day or two, hoping to merge <= Friday
  - The two approaches
  - Proposal is to move forward with 2618; strengthen tests, especially shutdown under load for all components, to ensure clean shutdown.
  - Today, we have a low-level API for controlling the engine.
      - We could build an HTTP client or OpAmp or CLI with this.
