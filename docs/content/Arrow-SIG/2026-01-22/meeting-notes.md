## Meeting Notes

### Attendees
- Laurent Querel(F5)
- Josh MacDonald (Microsoft)
- Drew Relmas (Microsoft)
- Tom Tan (Microsoft)
- Jake Dern (Microsoft)
- Aaron Marten (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Albert Lockett (F5)

### Agenda
- [5min] Crate naming
  - [Folder structure changes should go first](https://github.com/open-telemetry/otel-arrow/issues/1847)
  - [https://github.com/open-telemetry/otel-arrow/pull/1851](https://github.com/open-telemetry/otel-arrow/pull/1851) open draft
  - Laurent’s alternative proposal in [https://github.com/open-telemetry/otel-arrow/issues/1847#issuecomment-3782296201](https://github.com/open-telemetry/otel-arrow/issues/1847#issuecomment-3782296201)
  - Categorization: “experimental” is orthogonal to core vs contrib.
  - Follow-up for Triage process - use label ‘not ready for work’ to indicate items still needing more discussion
  - About “nodes” vs “components”: LQ gives rationale for “nodes”
- [10-15min] Stabilization of the config model v1
  - Review of [https://github.com/open-telemetry/otel-arrow/issues/1827](https://github.com/open-telemetry/otel-arrow/issues/1827)
  - Propose to start with URN consistency [https://github.com/open-telemetry/otel-arrow/issues/1831](https://github.com/open-telemetry/otel-arrow/issues/1831)
  - About simplified outputs section:
- [10 min] Note about new internal telemetry system configuration,
  - [https://github.com/open-telemetry/otel-arrow/pull/1861#top](https://github.com/open-telemetry/otel-arrow/pull/1861#top)
- [5 min] Open discussion about multi-tenant
  - For nex time [https://db.in.tum.de/~leis/papers/morsels.pdf](https://db.in.tum.de/~leis/papers/morsels.pdf)
