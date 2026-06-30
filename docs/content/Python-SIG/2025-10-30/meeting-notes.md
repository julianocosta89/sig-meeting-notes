## Meeting Notes

### Attendees
- Dylan Russell (google)
- Keith Decker (Cisco/Splunk)
- Marcelo Trylesinski (Pydantic)
- Riccardo Magliocchetti (Elastic)
- Tammy Baylis (SolarWinds)
- Aaron Abbott (Google)

### Agenda
- Log Breaking changes and release plan, every year we have release freeze starting mid November in Microsoft, so it would be great to have some plan for these soon.
  - Hopefully we are able to release with the breaking changes PR in two weeks
  - Some feedback from the warnings [https://github.com/open-telemetry/opentelemetry-python/issues/4783](https://github.com/open-telemetry/opentelemetry-python/issues/4783)
- (Hector: I will not be able to join SIG meeting as I have a conflict, just want to know what is current plan for breaking changes coming and rough ETA so we can prepare on Azure side)
  - Riccardo will look at PR but others please take a look too
- [Keith] PR for review: Additional semconv attributes in GenAI Utils: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3862](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3862)
  - Should genai utils set errors or defer to instrumentation? [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3862/files/309d348563e1af40a729fbe0ae53e11457aecc3f#r2470827475](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3862/files/309d348563e1af40a729fbe0ae53e11457aecc3f#r2470827475)
  - Aaron: anyone following up on precise definition in yaml on required attributes #otel-genai-instrumentation / #otel-semantic-conventions?
- Logger Configurator and log filtering- [Implement filtering logic for min_severity and trace_based parameters by rads-1996 · Pull Request #4765 · open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python/pull/4765)
- [Keith] PR for review: Adding metrics to GenAI Utils: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891)
- [Marcelo]: Python 3.14? [https://github.com/open-telemetry/opentelemetry-python/issues/4789](https://github.com/open-telemetry/opentelemetry-python/issues/4789)
  - No volunteers
- [Marcelo]: line length too short
  - [https://github.com/open-telemetry/opentelemetry-python/blob/75c8d67bf1727687a63294383499830f7eed281f/pyproject.toml#L63C1-L64C1](https://github.com/open-telemetry/opentelemetry-python/blob/75c8d67bf1727687a63294383499830f7eed281f/pyproject.toml#L63C1-L64C1) 79 lines
