## Meeting Notes

### Attendees
- Diego Hurtado (Dash0)
- Hector Hernandez (Microsoft)
- Lukas Hering (Oracle)
- Tammy Baylis (SolarWinds)
- Riccardo Magliocchetti (Elastic)
- Emídio (Independent)
- Aaron
- Pablo Collins (Cisco)

### Agenda
- [Lukas] [opentelemetry-sdk: add support for advisory attributes on metric instruments](https://github.com/open-telemetry/opentelemetry-python/pull/5444)
  - Pros and cons to API *and* SDK
- [Lukas] [opentelemetry-configuration: parse YAML 1.2 with ruamel.yaml instead of PyYAML](https://github.com/open-telemetry/opentelemetry-python/pull/5908)
  - Riccardo - Can we extend pyyaml to parse in the format for 1.2
- [Lukas] [Otel Agent](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5316)
- [Hector] Logs Stabilization tracking, is this the correct place to track this?
  - Some remaining little issues e.g. ​​[https://github.com/open-telemetry/opentelemetry-python/issues/5785](https://github.com/open-telemetry/opentelemetry-python/issues/5785)
  - And above KW args PR
  - Liudmila already did reviews [https://github.com/open-telemetry/community/issues/1751](https://github.com/open-telemetry/community/issues/1751)
  - Target stable next release?
  - LoggingInstrumentor should not block SDK stabilization
- [Diego] [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5221](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5221)
  - Lots of vulnerabilities resolved already!
  - Need to address [https://github.com/open-telemetry/opentelemetry-python-contrib/security/dependabot/1195](https://github.com/open-telemetry/opentelemetry-python-contrib/security/dependabot/1195)
