## Meeting Notes

### Attendees
- Jonathan Halliday (IBM)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- [Scott Gerring](mailto:scott@datadoghq.com)(Datadog)
- Roger Coll (Elastic)
- [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) (Datadog)
- [Christian Simon](mailto:christian.simon@grafana.com) (Grafana Pyroscope)
- [Alexey Alexandrov](mailto:aalexand@google.com) (Google)
- [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) (Datadog)
- [Frederic Branczyk](mailto:frederic.branczyk@polarsignals.com) (Polar Signals); dropped at :50
- [Christos Kalkanis](mailto:christos.kalkanis@elastic.co) (Elastic)

### Agenda
- Review action items.
  - [Alexey Alexandrov](mailto:aalexand@google.com) Add orphan checks to the conformance checker.
  - [Florian Lehner](mailto:florian.lehner@elastic.co) sig-profiling/profcheck work:
    - Add duplicate checks to the conformance checker.
    - [https://github.com/open-telemetry/sig-profiling/pull/108](https://github.com/open-telemetry/sig-profiling/pull/108) check duplicate mappings
  - [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) Open GH issue on including OTLP version in payloads.
    - **Update**: Drafted a document: [Versioning OTLP Profiles](https://docs.google.com/document/d/1ZYf5CvxphaAXHzDxnC5PQr7Petn78-EImxjNiagwzF0/edit?tab=t.0)
  - [Alexey Alexandrov](mailto:aalexand@google.com) Figure out what to do with this [older Profiles OTEP](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/profiles/0239-profiles-data-model.md). See [this discussion below](#bookmark=id.mjn7dj4yyazk).
    - Depends on [https://github.com/open-telemetry/opentelemetry-specification/pull/4965](https://github.com/open-telemetry/opentelemetry-specification/pull/4965)
    - This is blocked by christos PRs above. When they land, we can update the OTEP and point to these newer docs. (Christos: #4965 was merged)
- [Shivanshu Raj Shrivastava](mailto:shivanshu@odigos.io) support nested PID namespace for profiling - [https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pull/1654](https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pull/1654)
  - Try to solve issues related to environments like kind
  - In general, a similar problem exists for file paths
  - Follow up PR with [https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pull/1657](https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pull/1657)
- [Scott Gerring](mailto:scott@datadoghq.com)[Nayef Ghattas](mailto:nayef@datadoghq.com) - [memory profiling proposal](https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pull/1672)! We propose a mechanism to sample allocations & live heap from running processes using a USDT contract and a user-space sampling process
  - Request: review and provide feedback
  - Frederic: we experimented with mimalloc
- [Ivo Anjo](mailto:ivo.anjo@datadoghq.com) Quick recap of where we are on context sharing work:
  - OTEP has been merged [https://github.com/open-telemetry/opentelemetry-specification/pull/4947](https://github.com/open-telemetry/opentelemetry-specification/pull/4947)
  - We're iterating on the eBPF Profiler implementation PRs [https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pulls/nsavoire](https://github.com/open-telemetry/opentelemetry-ebpf-profiler/pulls/nsavoire)
  - WIP adapting Polar Signals' custom-labels Node.js support for OTel ([library side first](https://github.com/polarsignals/custom-labels/tree/otel-thread-ctx-wip), then eBPF profiler)
  - WIP otel-rust SDK implementation ([PR #3460](https://github.com/open-telemetry/opentelemetry-rust/pull/3460), [PR #3585](https://github.com/open-telemetry/opentelemetry-rust/pull/3585))
  - There's an otel-python SDK PR [https://github.com/open-telemetry/opentelemetry-python/pull/5337](https://github.com/open-telemetry/opentelemetry-python/pull/5337) (Ivo: I plan to review it soon)
  - We've been able to get it working end-to-end without issues at Datadog
  - Java SDK implementation is under discussion
- [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) Including the opentelemetry-ebpf-profiler in the contrib distribution, and security implications:
  - [https://github.com/open-telemetry/opentelemetry-collector-releases/pull/1553](https://github.com/open-telemetry/opentelemetry-collector-releases/pull/1553)
  - [[Draft] Least privilege setup for the eBPF profiler](https://docs.google.com/document/d/1aJQd6nXqU2DMXLsU933G11dweNhoVHEbxL8CQLAyWsc/edit?tab=t.0)
  - Going forward, present this topic to the Collector SIG and let Antoine know/involve
- [Nayef Ghattas](mailto:nayef.ghattas@datadoghq.com) Optional, if time permits, go over the OTLP profiles development versioning proposal: [Versioning OTLP Profiles](https://docs.google.com/document/d/1ZYf5CvxphaAXHzDxnC5PQr7Petn78-EImxjNiagwzF0/edit?tab=t.0).
  - Try to avoid OTEP as this versioning is OTLP Profiles specific
