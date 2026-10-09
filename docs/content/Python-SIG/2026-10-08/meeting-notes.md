## Meeting Notes

### Attendees
- Aaron Abbott (Google)
- Riccardo Magliocchetti (Elastic)
- Diego Hurtado (Dash0)
- Lukas Hering (Oracle)
- Emídio (Independent)
- Leighton Chen (Microsoft)
- Tammy Baylis (SolarWinds)

### Agenda
- [Lukas] Logs stabilization
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5731](https://github.com/open-telemetry/opentelemetry-python/pull/5731)
  - [Aaron] We should create benchmark tests for the api layer prior to stable
    - Concerned about perf for no-op impl and making sure it’s feasible to implement a performant SDK (not locking ourselves out)
    - [aaron] will file an issue
  - It would be a shame to release a 1.0 and have to change the api surface after.
- [carlos] PRs that are (probably) ready to be merged:
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5613](https://github.com/open-telemetry/opentelemetry-python/pull/5613)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5696](https://github.com/open-telemetry/opentelemetry-python/pull/5696)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5650](https://github.com/open-telemetry/opentelemetry-python/pull/5650)
