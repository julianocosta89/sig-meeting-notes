## Meeting Notes

### Attendees
- Tammy Baylis (SolarWinds)
- Aaron Abbott (Google)
- Riccardo Magliocchetti (Elastic)
- Lukas Hering (Oracle)
- Radhika Gupta (Microsoft)
- Keith Decker (Cisco/Splunk)
- Dylan russell (google)
- Ridhima Satam (Cisco/Splunk)

### Agenda
- Diego [https://github.com/open-telemetry/opentelemetry-python/issues/4524#issuecomment-4849367998](https://github.com/open-telemetry/opentelemetry-python/issues/4524#issuecomment-4849367998)
  - We can close one as duplicate
- Diego non protobuf HTTP exporter performance
  - Pure python protobuf implementation 50X slower on microbenchmark, ~2X on real usage
    - Lukas: we can make the binary part optional
    - Diego: we also have a grpcio pure python implementation
  - Aaron: buf release a rust based protobuf implementation with pure python backport [https://buf.build/blog/protobuf-py](https://buf.build/blog/protobuf-py)
  - JSON exporter solves the issue? [https://github.com/open-telemetry/opentelemetry-python/pull/5374](https://github.com/open-telemetry/opentelemetry-python/pull/5374)
    - Riccardo: The default should be http/proto though
  - Liudmila: another option is vendoring the current protobuf instrumentation, java vendors a bunch of stuff
  - Lukas: another option would be to ship for injector/operator scenarios the python wrapper of the cpp opentelemetry sdk that Alex Boten showed
    - Diego: we’ll lose the dynamicity of entry points and pluggability
  - [https://github.com/open-telemetry/opentelemetry-python/issues/4226](https://github.com/open-telemetry/opentelemetry-python/issues/4226)
- Radhika: Logs stabilization. Any outstanding tasks?
  - [https://github.com/open-telemetry/community/issues/1751](https://github.com/open-telemetry/community/issues/1751)
- Lukas: Dependence on incubating attributes in exporters: [https://github.com/open-telemetry/opentelemetry-python/pull/5387](https://github.com/open-telemetry/opentelemetry-python/pull/5387)
  - Liudmila: alternative could be to test for oldest version of semconv we support
  - Riccardo: also testing against oldest sdk that introduced these metrics  could be useful since we had breakages already in the past
  - Riccardo: let me check if we can stabilize with sdk health metrics
