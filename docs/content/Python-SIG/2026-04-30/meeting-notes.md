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

### Agenda
- Lukas - Open to Generalizing HTTP exporters?
  - [https://github.com/open-telemetry/opentelemetry-python/issues/3439](https://github.com/open-telemetry/opentelemetry-python/issues/3439)
  - [https://github.com/open-telemetry/opentelemetry-python/issues/4171](https://github.com/open-telemetry/opentelemetry-python/issues/4171)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5164](https://github.com/open-telemetry/opentelemetry-python/pull/5164)
    - Aaron: maybe we can do an overload to add a new experimental interface so it would be easier to back out if we found issues
- Lukas - Remove “importlib_metadata” for Python >= 3.12
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5156](https://github.com/open-telemetry/opentelemetry-python/pull/5156)
  - Context [https://github.com/open-telemetry/opentelemetry-python/pull/3217](https://github.com/open-telemetry/opentelemetry-python/pull/3217)
    - [https://github.com/open-telemetry/opentelemetry-python/issues/3167#issuecomment-1481335345](https://github.com/open-telemetry/opentelemetry-python/issues/3167#issuecomment-1481335345)
  - Aaron, Leighton: let’s wait a bit more
- [Liudmila] Python-genai repo proposal ​​[[EXTERNAL] opentelemetry-python-genai plan](https://docs.google.com/document/d/1qayEmzxeB1PlINbKBBZW5HKgA7_72WlZ-DGNfMZ5l9E/edit?tab=t.0)
  - Diego: thought on one repo per package?
    - Liudmila: unfeasible with the number of packages
- [Ridhima - 1min] Asking for reviews, Langchain workflow support - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4449](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4449)
- [Liudmila] Can we merge [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4315](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4315) ?
  - Also trivial [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4506](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4506)
- [Leighton] Updated based on feedback
  - [Fix/baggage propagator outbound limits by lzchen · Pull Request #5163 · open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python/pull/5163)
