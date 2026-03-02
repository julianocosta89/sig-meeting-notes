## Meeting Notes

### Attendees
- Josh MacDonald (Microsoft)
- Albert Lockett (F5)
- Cijo Thomas (Microsoft)
- Tom Tan (Microsoft)
- Laurent Querel (F5)
- Jake Dern (Microsoft)
- Danny Chin (CMU)
- Drew Relmas (Microsoft)
- Gokhan Uslu (Microsoft)
- Aaron Marten (Microsoft)

### Agenda
- Issue triage:
- [Drew] [Issue Triage Process and Labels · Issue #1749 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/issues/1749)
  - Part 1: let’s triage, proposing Tom T. as a new triager
  - Part 2: considering a directory hierarchy of receivers, processors, exporters
- [Drew] About when we can publish [crates.io](http://crates.io) packages
  - LQ: requirement: have a prefix for all crates like `otap-df` or `opentelemetry-otap-*` etc
  - LQ: have no stability requirements, use of 0.x release series
  - LQ: finish a subset of our new internal telemetry guidelines, publish our entity semantic conventions
  - Note that there is no prefix reservation in crates system, “squatters” can take names
    - crates/pdata/src/proto is duplicative with opentelemetry-proto on [crates.io](http://crates.io)
    - otel-arrow-xxx
    - otap-df-xxx
- [Cijo] Question on data loss while stress testing/filter-testing
  - Can we explain small percentage data loss in tests?
  - (if not, will investigate)
  - Will add logs
  - [jmacd] want pipeline metrics:
    - [lq] we have this now at the batch level, not at the signal level
    - [jm] this is about what we count in the pipeline, “requests” (batches), “items” (signals), and “bytes”
  - [jmacd] not impossible it’s an OTLP->OTAP->OTLP bug?
  - [lquerel] about sublinear scaling observed in the tests:
- Important PRs to review:
  - ~~[jmacd]: not to review 1771 [Have already spent too much time talking about this PR today, it’s not ready to review!](https://github.com/open-telemetry/otel-arrow/pull/1771) I realized the new internal logging configuration belongs in a different place.~~
  - [aaronm]: [[otap-df-quiver] Quiver Subscriber API; quiver-e2e test tool #1764](https://github.com/open-telemetry/otel-arrow/pull/1764) (Josh has reviewed/approved already.)
- [Gokhan] Auth for exporters
  - Problem: we have some logic for e.g., Azure authorization, … we use this logic in the parquet explorer via object_store, for the azure monitor exporter, etc.
  - There is a cross-cutting concern.
  - Go collector: has “auth” extensions, which are protocol-specific.
  - For the Azure auth module,
    - there is a background task or thread needed to refresh
    - [jm] (How is this different from mTLS?)
    - [https://github.com/open-telemetry/otel-arrow/pull/1517/files](https://github.com/open-telemetry/otel-arrow/pull/1517/files)
  - [lq] Propose a design document
    - Also want multi-tenancy; some examples of a “complex” scenario
  - [jm] More about what “extensions” are in the Go Collector, Type, Name, Config struct, Start and Stop method, plus specific interfaces
