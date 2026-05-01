## Meeting Notes

### Attendees
- Diego Hurtado
- Lukas Hering
- Dylan Russell
- Mike Goldsmith (Honeycomb)
- Aaron Abbott (Google)
- Liudmila Molkova (Grafana Labs)
- Riccardo Magliocchetti (Elastic)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Tammy Baylis (SolarWinds)
- Emidio
- Keith Decker (Cisco/Splunk)
- Jeff Luo (Google)
- Shuwen Pan (Cisco)
- Ridhima Satam (Cisco/Splunk)
- Leighton Chen (Microsoft)
- Pablo Collins (Cisco/Splunk)
- https://github.com/orgs/open-telemetry/projects/88/views/1
- Lukas - JSON Exporters + Prometheus Stabalization
- Mike - Declarative Config, last push before working on API 🎉
- Liudmila - GenAI utils (completion hook) and OpenAI polish, new repo proposal
- Aaron - GenAI plan reserving packages, reviewing all of your PRs :)
- Leighton - GenAI reviews, refactoring

### Agenda
- Lukas - Open to Generalizing HTTP exporters?
  - https://github.com/open-telemetry/opentelemetry-python/issues/3439
  - https://github.com/open-telemetry/opentelemetry-python/issues/4171
  - https://github.com/open-telemetry/opentelemetry-python/pull/5164
      - Aaron: maybe we can do an overload to add a new experimental interface so it would be easier to back out if we found issues
      - * Lukas - Remove “importlib_metadata” for Python >= 3.12
  - https://github.com/open-telemetry/opentelemetry-python/pull/5156
  - Context https://github.com/open-telemetry/opentelemetry-python/pull/3217
      - https://github.com/open-telemetry/opentelemetry-python/issues/3167#issuecomment-1481335345
  - Aaron, Leighton: let’s wait a bit more
- [Liudmila] Python-genai repo proposal ​​opentelemetry-python-genai plan
  - Diego: thought on one repo per package?
      - Liudmila: unfeasible with the number of packages
- [Ridhima - 1min] Asking for reviews, Langchain workflow support - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4449
- [Liudmila] Can we merge https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4315 ?
  - Also trivial https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4506
- [Leighton] Updated based on feedback
  - Fix/baggage propagator outbound limits by lzchen · Pull Request #5163 · open-telemetry/opentelemetry-python
