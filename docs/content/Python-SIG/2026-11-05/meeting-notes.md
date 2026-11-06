## Meeting Notes

### Attendees
- Lukas Hering (Oracle)
- Emídio (Independent)
- Dylan Russell (google)
- Riccardo Magliocchetti (Elastic)
- Tammy Baylis (SolarWinds)
- Pablo Collins (Cisco)
- Liudmila Molkova (Google)
- Leighton Chen (Microsoft)

### Agenda
- [Emidio] Python 3.15 support
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5238](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5238)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5833](https://github.com/open-telemetry/opentelemetry-python/pull/5833)
  - We are ok with introducing this a bit earlier. Please review
- [Diego] Packaging updates [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5229#issuecomment-6504619857](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5229#issuecomment-6504619857)
  - A lot of code but much easier to maintain than [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4883](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4883)
  - Script will work with user env-specific version strings
  - Different approaches for different dependencies (that are causing conflicts)
    - Packaging -> Vendoring
    - Protobuf / grpc -> pure-python
    - Jsonschema -> generate a parser
  - [https://github.com/open-telemetry/opentelemetry-packaging/tree/main/packaging/common/python/vendor](https://github.com/open-telemetry/opentelemetry-packaging/tree/main/packaging/common/python/vendor)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/5308](https://github.com/open-telemetry/opentelemetry-specification/pull/5308)
  - opentelemetry-python-agent with all dependencies vendored
- [Lukas] [Enhancement: Add forward compatible instrument creation APIs](https://github.com/open-telemetry/opentelemetry-python/issues/5877)
  - Ptal [https://github.com/open-telemetry/opentelemetry-python/issues/5877#issuecomment-6664991272](https://github.com/open-telemetry/opentelemetry-python/issues/5877#issuecomment-6664991272)
- [Lukas] [feat: add Valkey instrumentation library](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5041)
  - Add conformance tests
- [Diego] documentation PRs [https://github.com/open-telemetry/opentelemetry-python/pull/5869](https://github.com/open-telemetry/opentelemetry-python/pull/5869)
- [Liudmila] OpenAI deprecation follow ups
  - Docs: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5262](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5262)
  - Drop 'experimental' (new path) support and remove dependency on util-genai [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5260](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5260)
  - When experimental mode is used, use new instrumentation [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5261](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5261)
  - Remove dead code: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5263](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5263)
  - Intend to release it and never release again
  - Related [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4927](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4927)
