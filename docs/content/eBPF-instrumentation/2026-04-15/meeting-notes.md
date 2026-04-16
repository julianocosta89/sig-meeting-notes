## Meeting Notes

### Attendees
- Mario Macias (Grafana)
- Tyler Yahn (Splunk)
- Nikola Grcevski (Grafana)
- Rafael Roquetto (Grafana)
- Mattia Meleleo (Coralogix)
- Mike Dame (Odigos)
- Giuseppe Ognibene (Coralogix)
- Stephen Lang (Grafana)
- Robert Pająk (Splunk)
- Ron Federman (Odigos)

### Agenda
- [Nimrod] Managing [issues](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/issues)
  - Marking issues as stale
  - Closing issues after a long stale period
  - Manually go over open issues and close solved ones
  - Template to open new issues
    - Bug / feature / documentation - mark with correct label
    - Redirect questions to [discussions](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/discussions) / slack?
- [Rafael] Our config reminds me of a [Concorde Cockpit](https://i.redd.it/3bvh6zld3bb61.png) - we should start to think about simplifying it, too many knobs (that are not orthogonal to each other)
  - [Tyler] [Config v2.0](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1351#top)
  - [Nikola] Can the config generation help us with AI generating configs?
- [Giuseppe|Nimrod] We have stat metrics like obi.stat.tcp.rtt (with more coming like obi.stat.tcp.failed.connections and so on) that use custom OBI names because no OTel semantic convention covers metrics like that. I checked:
  - the existing semconv for hardware network metrics [https://opentelemetry.io/docs/specs/semconv/hardware/network/](https://opentelemetry.io/docs/specs/semconv/hardware/network/)
  - the existing semconv for system metrics [https://opentelemetry.io/docs/specs/semconv/system/system-metrics/](https://opentelemetry.io/docs/specs/semconv/system/system-metrics/)
  - open/closed issues/prs here [https://github.com/open-telemetry/opentelemetry-specification](https://github.com/open-telemetry/opentelemetry-specification)
- [Tyler] [Roadmap](https://github.com/orgs/open-telemetry/projects/187/views/1) check-in
- [Rafael] Socktracer
  - [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1834](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1834)
