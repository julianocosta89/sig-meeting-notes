## Meeting Notes

### Attendees
- Jack Berg (Grafana Labs)
- [Nikola Grcevski](mailto:grcevski@gmail.com) (Grafana Labs)
- Antoine Toulme (Splunk)

### Agenda
- [Nikola] set node name via env var
  - To make this part of the code instead of having the operator doing it
  - OTEL_INJECTOR_K8S_POD_NAME exists, so we add OTEL_INJECTOR_K8S_NODE_NAME
  - [Antoine] - why do we have all those OTEL_INJECTOR_* env vars vs OTEL_INJECTOR_RESOURCE_ATTRIBUTES ?
  - [Jack] make it programmatic - any OTEL_INJECTOR_ env var, strip “INJECTOR_” and inject
  - [jack] default_auto_instrumentation_env.conf is great for injector running in the linux context, allowing users to inject any `OTEL_` into their application. Need the equivalent for the k8s context, where setting env vars is significantly more convenient than writing to a file and mounting to the file system.
- [Ted] What should I tell people to try when I’m at FOSDEM/Unplugged?
  - [https://github.com/breedx-splk/injector-demo](https://github.com/breedx-splk/injector-demo)
- Goals for this year
  - Coverage for
    - Java
    - .NET
    - Python
    - NodeJS
    - Collector
    - OBI
  - Operator
  - Debian and Red Hat packages
