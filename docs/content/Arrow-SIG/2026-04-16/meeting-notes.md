## Meeting Notes

### Attendees
- Josh MacDonald (Microsoft)
- Laurent Querel (F5)
- Drew Relmas (Microsoft)
- Albert Lockett (F5)
- Gokhan Uslu (Microsoft)
- Jake Dern (F5)
- Utkarsh Umesan Pillai (Microsoft)
- Aaron Marten (Microsoft)

### Agenda
- [Triage]
  - Note! Try to modify triage labels
  - Through #2687
- [Laurent] Live reconfiguration demo
  - New dfctl command with ratatui very cool.
- [Drew] Processor chain
  - [Implement `NodeKind::ProcessorChain` · Issue #2556 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/2556)
  - [feat(otap-dataflow): Implement `processor_chain:inlined` for channel elimination and composite metric reporting by drewrelmas · Pull Request #2669 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/2669)
  - Discuss the several approaches already studied.
    - Having a stopwatch in the Context is likely not the best approach for this case
    - Avoiding the memory of a PData queue between processors is good
    - Why is the processor trait defined the way it is? To enable this!
    - Drew’s latest inline-processor approach defines a new trait
    - Probably not necessary to define a new trait though
    - Still evaluating!
