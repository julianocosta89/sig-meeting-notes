## Meeting Notes

### Attendees
- Jim
- Antoine
- Ruediger
- Morgan
- Anand
- Richard

### Agenda
- Check with Semantic Convention SIG on opening a project for the Mainframe SIG in their repro, using same filters
- Virtualization - check with Semantic Conventions SIG
- OpenTelemetry Collector - linux/s390x -[https://github.com/open-telemetry/opentelemetry-collector/issues/13905](https://github.com/open-telemetry/opentelemetry-collector/issues/13905)
  - Specific agreement - about using the service ?
  - GitHub installed, needs to be IBM internally approved now
  - Once approved, run a PR on it and test behavior, then take it back to OTel Collector SIG
- For SDK support, create a template what needs to be done
  - Then approach language maintainers, to allow to build a plan (build, test, adopt Otel Semantic Conventions)
  - GRPC dependencies
- C++ SDK - may have a C compatibility layer - needs to be checked
- Semantic Conventions for metrics - open initial PRs to get feedback on
