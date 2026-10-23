## Meeting Notes

### Attendees
- Riccardo Magliocchetti (Elastic)
- Lukas Hering (Oracle)
- Tammy Baylis (SolarWinds)
- Emidio (independent)
- Leighton Chen (Microsoft)
- Gaurav Ramnani (InterSystems)
- Hector Hernandez (Microsoft)
- Jackson Weber (Microsoft)

### Agenda
- [Riccardo] GC Elections next week [https://opentelemetry.io/blog/2026/gc-candidates/](https://opentelemetry.io/blog/2026/gc-candidates/)
- [emidio] - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5077](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5077)
- [Lukas + Aaron] - [https://github.com/open-telemetry/opentelemetry-python/pull/5797](https://github.com/open-telemetry/opentelemetry-python/pull/5797) / [https://github.com/open-telemetry/opentelemetry-python/issues/5785](https://github.com/open-telemetry/opentelemetry-python/issues/5785)
  - [https://docs.python.org/3/library/enum.html#enum.IntEnum](https://docs.python.org/3/library/enum.html#enum.IntEnum)
  - [Liudmila] Is it changing open/closed enum behavior?
    - Not sure, will check
    - [lukas] What’s the expected behavior?
    - [liudmila] not sure :)
    - [aaron] protobuf enums like [SeverityNumber](https://github.com/open-telemetry/opentelemetry-proto/blob/6c9dd787c3c5a5dae7d18ece0927581d5687f9c0/opentelemetry/proto/logs/v1/logs.proto#L87) are closed [https://protobuf.dev/programming-guides/enum/](https://protobuf.dev/programming-guides/enum/)
- [Lukas] - [https://github.com/open-telemetry/opentelemetry-python/pull/5792](https://github.com/open-telemetry/opentelemetry-python/pull/5792)
  - Weekly run? Follow up
- [Aaron] - PoC generating typed monkey patch code across many versions of instrumented library [https://github.com/aabmass/opentelemetry-python-contrib/pull/3/changes/ec019794e2825f06f6feaac7d2f7d8524adc41e3](https://github.com/aabmass/opentelemetry-python-contrib/pull/3/changes/ec019794e2825f06f6feaac7d2f7d8524adc41e3)
- [dylan] review release process in light of [lite llm incidents](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/)..
