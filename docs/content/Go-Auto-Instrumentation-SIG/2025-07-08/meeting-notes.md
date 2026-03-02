## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Rafael Roquetto (Grafana)
- Nikola Grcevski (Grafana)
- Ron Federman (Odigos)

### Agenda
- [Nikola] Discuss project [plan](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/245) to bring multi-process functionality so we can vendor directly from OBI
  - Offsets table per executable
  - Adding process information to events
  - Sharing maps using file descriptor rewrite for avoiding BPF file system SYS_ADMIN requirements
  - Discussion:
    - Start with one probe:
      - Database
    - First step: vendor the C
    - Build in the OBI user-space
    - Reuse the probes
    - Prior art: Beyla vendoring OBI
      - Go auto will be a sub-module for OBI
  - AI (Nikola): capture this in an issue
- [Nikola] Discuss how we fully reuse the Manager/Probe, can we extend support for different eBPF probes and [where this should live](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/245#issuecomment-3036547604).
- [Tyler] [Open PRs](https://github.com/open-telemetry/opentelemetry-go-instrumentation/pulls)
