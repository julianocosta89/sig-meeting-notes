## Meeting Notes

### Attendees
- Nikola Grcevski (Grafana)
- Rafael Roquetto (Grafana)
- Mario Macias (Grafana)
- Mattia Meleleo (Coralogix)
- Giuseppe Ognibene (Coralogix)
- Tyler Yahn (Splunk)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- Marc Tudurí (Grafana)
- Mike Dame (Odigos)

### Agenda
- [Nikola] How to investigate bpf probe overhead - demo
  - Get base idea of what probe is expensive with bpftop
  - Since the names are short in bpftop, get the ID of the probe and find the full name with
  - Profile with perf to see what inside the probe is expensive
- [Mike] obi-goauto follow up
- [Giuseppe] resize ebpf maps from userspace
  - [Nikola] YES!
  - Is this something we need?
  - Idea already implemented: during loading, change the size of all maps with max_entries of the following values: MAX_CONCURRENT_REQUESTS, MAX_CONCURRENT_SHARED_REQUESTS, and MAX_CONCURRENT_CUSTOM_SPANS
  - Idea almost implemented: divide the maps by tracer. Pros: more granularity. Cons: there are maps shared between various tracers (even if they're perhaps not used, for example, listening_ports between tpinjector and generictracer). This could be solved by cleaning up the ebpf code and making each tracer only use its own things or common data structures but not those of another tracer.
  - Technically, we could get to the point where the size of each map can be changed during configuration. I don't know how necessary this is because I think there are maps whose optimal size has already been found, but in that case, it's enough to not make them changeable.
  - [Florian] There is change happening upstream: [https://lore.kernel.org/bpf/20260205-rhash-v1-0-30dd6d63c462@meta.com/T/#t](https://lore.kernel.org/bpf/20260205-rhash-v1-0-30dd6d63c462@meta.com/T/#t)
- [Tyler] Release v0.5.0
- [Tyler] [Open PRs Review](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
