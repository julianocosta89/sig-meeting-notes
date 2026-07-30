## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- [Florian Lehner](mailto:florian.lehner@elastic.co)(Elastic)
- [Felix Geisendörfer](mailto:felix.geisendoerfer@datadoghq.com) (Datadog)
- Josh Suereth (Google)
- [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) (Datadog)
- [Christian Simon](mailto:christian.simon@grafana.com) (Grafana Labs / Pyroscope)
- [Francesco Andreuzzi](mailto:andreuzzi.francesco@gmail.com) (AWS/Async-Profiler)
- Frederic Branczyk (Polar Signals)

### Agenda
- Review action items:
  - [https://github.com/open-telemetry/opentelemetry-proto/pull/672](https://github.com/open-telemetry/opentelemetry-proto/pull/672)
    - [Metric Attributes](https://opentelemetry.io/docs/specs/semconv/system/hardware-metrics/#hwmemory---memory-module-metrics) in OTel SemConv do have a Unit defined but are mostly used around the Metric protocol.
    - [josh] [Metrics as an example](https://github.com/open-telemetry/opentelemetry-proto/blob/main/opentelemetry/proto/metrics/v1/metrics.proto#L196)
    - [jh] encode unit as part of [KeyValueAndUnit](https://github.com/open-telemetry/opentelemetry-proto/pull/672#discussion_r2198148492)
    - TODO action on JH to update PR with KeyValueAndUnit, new PR to factor out the original indexing change, maintainers to review both. (done 2025-07-25, #672 and #688)
  - Profile consistency check
    - [https://github.com/aalexand/sig-profiling/tree/main/profcheck](https://github.com/aalexand/sig-profiling/tree/main/profcheck)
    - [Alexey] Question around OTEP complex types
    - Decision: start with simple attributes
  - [simple stack trace id](https://github.com/open-telemetry/opentelemetry-proto/pull/645) PR is ready - please review
- [Alexey] In ProfilesDictionary we require zero value at index 0 for mapping_table, link_table and string_table, but not for location_table and function_table. Is this intentional? I think yes, but double-checking.
  - [Christos] Functions and Locations are (implicitly) non-optional (Functions through Lines, every Line is currently required to have a Function e.g. if we have a Line then we should also have an associated Function)
  - [jh] decision was for ALL dictionary fields to have it, see [https://github.com/open-telemetry/opentelemetry-proto/pull/672](https://github.com/open-telemetry/opentelemetry-proto/pull/672) (following from #659), merge is held up by the need to decide what to do with AttributeUnits, a more difficult discussion that got bundled in with the straightforward indexing docs comment change. #scope_drift
- [Christos] Clarify required status of  [link_table](https://github.com/open-telemetry/opentelemetry-proto/blob/6199584450839e30e66881f436df1c0e3a0bee37/opentelemetry/proto/profiles/v1development/profiles.proto#L108-L110) (with zeroed-out first element) if no links are present in the message. Documentation string implies it should always be present but that seems a bit ugly as it’s not needed in this case. Also, a consumer could use the absence of a link_table as a shortcut to skip any link-related processing.
  - To maintain some consistency, keep the [0] for link_table
- [Alexey] dropped_attributes_count field - what are the exact semantics? Do we really need it?
  - [jh] some reasons for dropping attrs don’t make sense - it doesn’t save much space because of the dictionary approach. However, config may still cause SDK/collector to drop e.g. very long keys, which causes invisible data loss if we don’t have this field. Weakly in favor of removing it on grounds of near uselessness, whilst acknowledging that takes us even further from consistency with the design of every other OTel signal type.
  - [josh] dropped_attributes_count is a OTel SDK feature
  - Looks like the main purpose of this field in other signals is to provide memory-bound collection capabilities. For profiling having just this field is not enough for that. We decided to remove this field for now and approach this problem post 1.0 release holistically. Josh to confirm with the OTel committee that it's OK to drop the field.
- [Alexey] Go generated code repo is old ([file](https://github.com/open-telemetry/opentelemetry-proto-go/blob/main/otlp/profiles/v1development/profiles.pb.go)) - e.g. Location.mapping_index is a pointer (from the "optional" times). How to get that updated?
  - [Florian] Generated code is using [OTel proto v1.7.0](https://github.com/open-telemetry/opentelemetry-proto/releases/tag/v1.7.0) (May 21, 2025). Newer and more recent changes are not yet included. Should we aim to get all our changes in for v1.8.0 and if there are no changes (in the OTel profiling signal) between v1.8.0 and v1.9.0, try to declare the protocol stable?
