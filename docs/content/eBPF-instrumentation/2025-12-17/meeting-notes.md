## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Stephen Lang (Grafana)
- Mattia Meleleo (Coralogix)
- Giuseppe Ognibene (Coralogix)
- Mario Macias (Grafana)
- Mihir Shah (Culver Max Entertainment Pvt Ltd)
- [Florian Lehner](mailto:florian.lehner@elastic.co) (Elastic)
- Mike Dame (Odigos)
- Nimrod Avni (Coralogix)

### Agenda
- [Tyler] Can OBI be used to replace the [OTel Injector](https://github.com/open-telemetry/opentelemetry-injector)?
  - OBI is able to easily discover all processes on a system
  - Can OBI set an environment for new .NET, Java, NodeJs, and python processes such that they start up with auto-instrumentation?
  - If so, can we merge these two projects?
- [Mario] MongoDB client crashing OBI
- [Tyler] [Open PRs Review](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pulls)
