## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- Antoine Toulme (Splunk)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- [Christos Kalkanis](mailto:christos.kalkanis@elastic.co) (Elastic)
- [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) (Datadog)
- [Elsa Keirouz](mailto:elsa.keirouz@datadoghq.com) (Datadog)
- [Daniel Schwartz-Narbonne](mailto:daniel.schwartznarbonne@datadoghq.com) (Datadog)
- [Kemal Akkoyun](mailto:kakkoyun@gmail.com)(Datadog)
- [Francesco Andreuzzi](mailto:andreuzzi.francesco@gmail.com)(AWS / Async-Profiler)
- cleverchuk(solarwinds)
- Morgan McLean (Splunk)

### Agenda
- Review action items:
- [Francesco] Is there any spec around `sample_type`? Like recommended type/units to make sure the profile is well interpreted by the consumer.
  - [https://github.com/grafana/pyroscope/blob/main/pkg/ingester/otlp/convert.go#L132](https://github.com/grafana/pyroscope/blob/main/pkg/ingester/otlp/convert.go#L132)
  - [https://github.com/open-telemetry/opentelemetry-ebpf-profiler/blob/main/reporter/internal/pdata/generate.go#L122](https://github.com/open-telemetry/opentelemetry-ebpf-profiler/blob/main/reporter/internal/pdata/generate.go#L122)
  - [Florian] There is no specification afaik. People follow comment in [https://github.com/open-telemetry/opentelemetry-proto/blob/b553517a730dc72097beb60292815ca221766598/opentelemetry/proto/profiles/v1development/profiles.proto#L222-L225](https://github.com/open-telemetry/opentelemetry-proto/blob/b553517a730dc72097beb60292815ca221766598/opentelemetry/proto/profiles/v1development/profiles.proto#L222-L225) or [https://github.com/google/pprof/blob/6e76a2b096b5fa52e4bb3f7f7a357bd6e6b3b7b1/proto/profile.proto#L48-L54](https://github.com/google/pprof/blob/6e76a2b096b5fa52e4bb3f7f7a357bd6e6b3b7b1/proto/profile.proto#L48-L54)
- [Antoine] pprof conversion [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40548](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/40548)
  - As [https://cloud-native.slack.com/archives/C03J794L0BV/p1750115751790599?thread_ts=1749398621.425369&cid=C03J794L0BV](https://cloud-native.slack.com/archives/C03J794L0BV/p1750115751790599?thread_ts=1749398621.425369&cid=C03J794L0BV)
  - I am not able to move forward at this time in my investigation as it appears that the .proto model for profiles is still in flux ; additionally, there is talk of organizing data by profile scope in ways that escape me.
  - I would like to file an issue to ask that the profiling SIG creates a set of tests that automate mapping from profile proto data to well known formats such as pprof, JFR and so on, as a way to work towards stability. Which project would be best to file such an issue?
    - [christos] Alexey’s personal repository is [here](https://github.com/aalexand/sig-profiling/tree/main/profcheck) but it needs to be moved to an OTel public repository which is currently blocked
    - [https://github.com/open-telemetry/community/issues/2862](https://github.com/open-telemetry/community/issues/2862) request for the sig-profiling repository
  - [jh] JFR->OTel will happen in the OTel Java SDK, it’s waiting on release of the updated .proto files. No plans for OTel->JFR as a) the JFR file format is not a standard, it’s a JDK impl detail and not stable (though async-profiler attempts to write it anyhow, but now also writes OTel) and b) nobody asked for it. :-)
- [Antoine] feedback on premature optimization [https://github.com/open-telemetry/opentelemetry-proto/issues/682](https://github.com/open-telemetry/opentelemetry-proto/issues/682)
  - [Nayef] We’ve discussed this multiple times and also went to the spec where advice was to continue with the current method as alternatives are still experimental. Profiling not like other signals, dedup is important to avoid ending up with gigabytes in OTel Collector memory.
- Some PRs seem to be stalling on not enough profiling-maintainers. How to promote the approvers (assuming they want to be…)?
  - [https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#becoming-a-maintainer](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#becoming-a-maintainer)
