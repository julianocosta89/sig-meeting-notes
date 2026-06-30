## Meeting Notes

### Attendees
- Mani Yazdankha (JP Morgan)
- Lukas Hering (Capital One)
- Dylan Russell (google)
- Liudmila Molkova (Grafana Labs)
- Keith Decker (Cisco/Splunk)
- Munir Abdinur (Datadog)
- Shuwen Pan (Cisco)
- Riccardo Magliocchetti (Elastic)
- Ridhima Satam (Cisco/Splunk)
- Aaron Abbott (Google)
- Pablo Collins (Cisco/Splunk)
- Josh Winerman (Cisco/Splunk)
- Hector Hernandez (Microsoft)
- Emídio (Independent)

### Agenda
- [Riccardo] setting the instrumentation scope to a global variable instead of using plain __name__: wdyt on adding that to each instrumentation [package.py](http://package.py)?
  - On instrumentation scope names [https://github.com/open-telemetry/opentelemetry-python/pull/4894](https://github.com/open-telemetry/opentelemetry-python/pull/4894)
  - Liudmila: makes sense, we should also test that
  - Lukas: we can create an issue about that: [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4173](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4173)
- [Riccardo] Plan for http stable semconv by default? [https://github.com/open-telemetry/community/issues/3254](https://github.com/open-telemetry/community/issues/3254)
  - Riccardo: two concerns: our tooling to handle different versions for instrumentations and losing some freedom after bumping to 1.x
  - Lukas: [https://opentelemetry.io/docs/specs/semconv/http/](https://opentelemetry.io/docs/specs/semconv/http/) -> bump major release on breaking changes
  - Aaron: reuse some of the tooling but maybe move to independent versioning for each instrumentation
  - Liudmila: OTEP stable by default being discussed [https://github.com/open-telemetry/opentelemetry-specification/pull/4813](https://github.com/open-telemetry/opentelemetry-specification/pull/4813)
  - Project board: [https://github.com/orgs/open-telemetry/projects/66/views/1](https://github.com/orgs/open-telemetry/projects/66/views/1)
  - Opt-in to stable might not currently be documented: [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/2453#issuecomment-3320515119](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/2453#issuecomment-3320515119)
- [Mani] review reminder for [https://github.com/open-telemetry/opentelemetry-python/pull/4863](https://github.com/open-telemetry/opentelemetry-python/pull/4863)
- [Lukas] OTLP JSON Protoc plugin? From [https://github.com/open-telemetry/opentelemetry-python/pull/4886](https://github.com/open-telemetry/opentelemetry-python/pull/4886)
  - [Aaron] Preference for code code generation, also don’t duplicate efforts
  - [Lukas] Talk about code structure
    - [Aaron] We can start with just bundling everything in the exporter and then split
- [Lukas] Slow imports of OTLP HTTP exporters
  - [https://github.com/open-telemetry/opentelemetry-python/issues/4171](https://github.com/open-telemetry/opentelemetry-python/issues/4171)
  - [Dylan] There may stuff that would not be easily translatable, also gcp auth probably tied to request Session
  - [Aaron] We want to keep api compatibility
  - [Aaron] Prior work of rust exporters wrapped by python
    - [https://crates.io/crates/otlp-stdout-span-exporter/0.10.0](https://crates.io/crates/otlp-stdout-span-exporter/0.10.0)
