## Meeting Notes

### Attendees
- Nikola Grcevski (Grafana Labs)
- Pavol Loffay (Red Hat)

### Agenda
- [Nikola] porting some of the integration tests from OBI (OpenTelemetry eBPF Instrumentation) to the injector. These would be end to end tests with various technologies, some that are not supported by the injector. It should help confirm that injection works, and for the unsupported technologies that there’s no side-effects.
- [Pavol Loffay](mailto:ploffay@redhat.com) using the injector in the OTEL operator
  - Dash0 operator. Init container contains all instrumentations, for .net both libc
  - Set LD_PRELOAD to load a shared library when a process starts
  - Then the injector sets JAVA_TOOL_OPTIONS… NODE…
  - It solves the problem with env vars coming from dockerfile, config map, script…
  - conf [https://github.com/open-telemetry/opentelemetry-injector/blob/main/packaging/fpm/etc/opentelemetry/otelinject.conf](https://github.com/open-telemetry/opentelemetry-injector/blob/main/packaging/fpm/etc/opentelemetry/otelinject.conf)
  - Supported langs: java, .net, [node.js](http://node.js), coming python, maybe ruby
  - Injector needs libc
