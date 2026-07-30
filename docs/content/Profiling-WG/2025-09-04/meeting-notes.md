## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- [Christos Kalkanis](mailto:christos.kalkanis@elastic.co)(Elastic)
- [Alexey Alexandrov](mailto:aalexand@google.com) (Google)
- [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com)(Datadog)
- [Felix Geisendörfer](mailto:felix.geisendoerfer@datadoghq.com)(Datadog)
- [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) (Datadog)
- [Marc Sanmiquel](mailto:marcsanmiquel@gmail.com) (Grafana/Pyroscope)

### Agenda
- Review action items:
  - Signal boost: everyone to take a look at the context propagation documents, linked above in the action item list.
- [Christos] [Fabrizio Ferri Benedetti](mailto:fabri.ferribenedetti@elastic.co) has graciously volunteered to help us with documentation. Let’s coordinate with him to figure out what we need and create work items that we can further assign to people.
  - Fabrizio was not in the meeting, so we need to sync more on what to do.
- [Christos] What else do we need for rc/alpha? [#645](https://github.com/open-telemetry/opentelemetry-proto/pull/645) is done (merged indirectly through [#708](https://github.com/open-telemetry/opentelemetry-proto/pull/708), part of [1.8.0](https://github.com/open-telemetry/opentelemetry-proto/releases/tag/v1.8.0) proto release). AFAICT no more protocol breaking changes in the pipeline.
  - 1.8.0 for the proto and proto-go release is out, but waiting for the collector release to go out.
  - Christos: Any protocol breaking changes we need to make?
  - Alexey: Any field reordering we want to do? Related to the sample merge semantics item below.
  - pprof format compatibility - Antoine Toulme mentions there were problems.
    - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40548](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40548)
    - SIG members to take a look.
- [Alexey] Should we remove aggregation temporality for now? I don't think there is a clear thought-out use case for the field and the enum right now.
  - Alexey is to send a PR to remove the aggregation temporality field. Some other form of this might come out of the sample merge semantics discussion.
- [Alexey] Sample merge semantics - [#706](https://github.com/open-telemetry/opentelemetry-proto/issues/706)
  - [Alexey] Could be an enum, per sample type?
  - [Jonathan] Or we should assume a closed universe of sample types where the behavior can be inferred from the metric name.
  - [Alexey, all] We agree and should document that the values/timestamps shape should be the same for all samples in the given profile.
  - [All] Discussion around inefficiency in sample / dictionary encoding such as dupe keys - agreed that this is a warning, not an error at the schema level.
  - [All] Agreed to adjust the field ordering nevertheless.
- [Christos] Go build ID - keep it for now? Deprecate at some point (we already have it in semantic conventions).
  - Use cases:
    - Have a build ID for binaries built with Go <1.24 which don’t emit a GNU build ID
    - Detect when binaries are built with Bazel since even after Go 1.24, Bazel overrides the GNU build ID to a hash of the word `redacted`, and sets the Go build ID to `redacted`, so this allows detecting that case in the backend.
  - No objections to keep it for now.
- [Ivo] Update on context propagation
