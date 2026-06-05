## Meeting Notes

### Attendees
- Nikola Grcevski (Grafana)
- Mike Dame (Odigos)
- Tyler Yahn (Splunk)

### Agenda
- otel operator support
  - Sidecar
- OBI should support all command line options of Go auto
- Go auto SDK
  - OBI avoids bpf_probe_write_user and has a slightly different approach, but works just without full capabilities
  - can add manual spans but not set or modify ebpf tracer, spans are linked
  - OBI has test examples
  - only write is the internal API bool for auto sdk
  - could use ptrace – looked at it but maybe too complicated?
  - go.opentelemetry.io/auto/sdk import ..? https://github.com/kubernetes/kubernetes/blob/9fa4c1cfa3d761fad081ef413d0dc0f88b5569a9/go.mod#L211
  - question for Go maintainers
- Span differences between go-auto and obi
  - Compare attributes on Go auto and see if any are missing from OBI equivalent instrumentations
- 3 thing breakdown:
  - Dynamic stuff
  - Go Auto SDK
  - Compare library stuff
- Not blocking OBI stability
- Announce deprecation and shift users over faster
  - Give notice and start deprecation
  - Talk to operator – current issue open to add obi to operator?
