## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Albert Lockett (F5)
- Utkarsh Umesan Pillai (Microsoft)
- Mike Heffner (streamfold/rotel)
- Ray Jenkins (rotel/streamfold)
- Josh MacDonald (Microsoft)
- Gokhan Uslu (Microsoft)
- Jake Dern (Microsoft)

### Agenda
- [Group] Issue triage:
  - [OtapPdata equivalence testing · Issue #1003 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/1003) discussed
- [Laurent] Telemetry System PR
  - About PR 946 [Generic, high-performance, type-safe metric instrumentation framework by lquerel · Pull Request #946 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/946)
  - Roughly speaking, this is a multivariate metric SDK
    - Hot path (thread pinned to a core: no synchronization)
    - Cool path (may cross a thread boundary)
    - Concept of a MetricSet, AttributeSet
    - Live telemetry schema computed from all attributes, all metric sets
  - Static registry: knows about all Metric/Attribute sets
    - Metadata can be reported once using registration data
    - Node and pipeline control messages are used to exchange metrics across threads
    - Prometheus-compat export on HTTP servlet, capable of aggregation
  - Discussion about delta vs cumulative output mode
    - Josh refers to “lightstep-metrics SDK” which has a similar design
    - How you can choose cumulative vs delta on output, most users prefer cumulative
    - “Slot value” mechanism, question of whether to use real timestamps or …
  - Talk about dynamic attributes
- [Rotel/OTel] talk about how to organize collaboration
  - High-level ideas about next year of project priorities
  - Potential for non-Arrow data
  - Mike and Ray looking for ways to contribute
- [Josh] Engine type changes ⚠️as part of adding Nack including Option<PData> for return
  - Error<T> to Error, TypedError<T>: most errors do not need <T>, only where SendError<T> is involved, and only then a subset
  - NodeControlMsg to NodeControlMsg<PData>
  - [https://github.com/open-telemetry/otel-arrow/pull/1017](https://github.com/open-telemetry/otel-arrow/pull/1017)
