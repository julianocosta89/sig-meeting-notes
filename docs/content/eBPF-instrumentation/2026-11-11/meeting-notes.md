## Meeting Notes

### Attendees
- Gregor Zeitlinger (Grafana)
- Roy Reshef (Kubex)
- Marc Tuduri (Grafana)
- Mario Macias (Grafana)
- Nikola Grcevski (Grafana)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana)
- Rafael Roquetto (Isovalent)
- Mario Macias (Grafana)
- Mattia Meleleo (Coralogix)
- Mike Dame (Odigos)
- Tyler Yahn (Splunk)
- Endre Sara (Causely)
- Nimrod Avni (Coralogix)
- Giuseppe Ognibene (Coralogix)
- Roy Reshef (Kubex)

### Agenda
- [Tyler] Next week’s meeting – KubeCon NA
  - Mario will lead next week.
  - [mike+rafael] [https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/program/schedule/?id=1247277](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/program/schedule/?id=1247277)
  - [mike+rafael observability day] [https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/cncf-hosted-co-located-schedule/?id=1247219](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/cncf-hosted-co-located-schedule/?id=1247219)
  - [tyler+nikola observability day] [https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/cncf-hosted-co-located-schedule/?id=1246975](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/cncf-hosted-co-located-schedule/?id=1246975)
- [Tyler] [Update OBI documentation for v1.0.0](https://github.com/open-telemetry/opentelemetry.io/pull/12496#top)
- [Tyler] [Align v1 policies and agent compatibility checks](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4005)
- [Tyler] Reverse breaking changes:
  - [Preserve frozen v1 attribute selection](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4029#top)
  - [Preserve v1 Route53 resolution behavior](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4028#top)
  - [Restore the public symbol matcher API](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4027)
  - [Preserve v1 selector implementations](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4026)
  - [Restore the v1 process watcher API](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4025)
  - [Restore the v1 cloud enrichment APIs](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4024)
  - [Restore the v1 SQL++ span API](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4023)
  - [Restore the v1 cgroup attachment API](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/4022)
- [Tyler] OTel contribfest at KubeCon 2026
  - Issues that are easy to understand and small enough for a new contributor to finish or make real progress on during the session. Docs, tests, examples, small bug fixes, and reproducing reported bugs all work well.
  - Tagged with `contribfest` and tagged with `needs-verification` if a reproduction is needed first
  - Unassigned
  - Leave a comment like:
- [Nikola] Local Linux host instrument everything mode
- [Mike] Embedded Extension Points [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/4047](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues/4047)
  - Custom swarm pipeline nodes
  - Custom protocol detection
