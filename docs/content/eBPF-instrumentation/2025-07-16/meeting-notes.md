## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Stephen Lang (Grafana)
- Rafael Roquetto (Grafana)
- Nikola Grcevski (Grafana)
- Mattia Meleleo (Coralogix)
- Mike Dame (Odigos)

### Agenda
- [Nikola] Java TLS support discussion
  - Why? Being able to produce baseline instrumentation without any additional intervention by the end user, no restarts.
    - The OTel Java SDK can be dynamically injected, but not all instrumentations work if you do so, e.g. [gRPC and others](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/11586) don't. It’s not officially supported mode.
    - Without TLS support, common use-cases like connecting to cloud databases doesn’t work
  - What we intended to do a while back is a lot of work
    - Uprobes cannot be set on anonymous code regions, they require inode number
    - Adding an inode number to the JVM code cache requires
      - PTrace to stop the JVM
      - PTrace to execute syscalls to remap the anonymous regions to a memory mapped file
      - May not always work
    - Java can run in multiple modes, handling references is tricky
      - Full 64bit vs compressed oops
      - Lilliput vs normal headers
    - Java offsets to code-cache data structures have changed in the past quite a bit
  - The [approach presented](https://www.youtube.com/watch?v=sG72GWdo9Hs) by Valeri Pliskin at KubeCon EU 2024 is much easier to implement
    - I’ve implemented this approach and I wanted to see if there are any objections to adding it to OBI.
- [Rafael] [CONTRIBUTING.md](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/blob/main/CONTRIBUTING.md)
- [Stephen] Looking for a sponsor for [community membership](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md) (contributions [here](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues?q=author%3Askl+) and [another example](https://github.com/open-telemetry/semantic-conventions/pull/2488?notification_referrer_id=NT_kwDOAAfZJ7IxNzQyODMyODY3OTo1MTQzNDM&notifications_query=is%3Adone#discussion_r2197654928))
  - Nikola and Tyler volunteered
- [Tyler] [Milestone 0.1.0](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/1) review
- [Nikola] Kernel 5.4 support opened issue.
- [Tyler] [Open PRs](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
