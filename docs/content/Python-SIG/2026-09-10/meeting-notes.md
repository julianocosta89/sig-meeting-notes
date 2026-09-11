## Meeting Notes

### Attendees
- Diego Hurtado (Dash0)
- Aaron Abbott (Google)
- Tammy Baylis (SolarWinds)
- Dylan Russell (Google)
- Riccardo Magliocchetti (Elastic)
- Emídio (Independent)
- Leighton Chen (Microsoft)
- Pablo Collins (Cisco)

### Agenda
- [Diego] [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/5028](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/5028)
  - No objections, Diego will open a PR
- [Diego] [https://github.com/open-telemetry/opentelemetry-python/pull/5503](https://github.com/open-telemetry/opentelemetry-python/pull/5503)
  - [aaron]
    - Two main actually use cases to solve
        - Solved with not using official protobuf
        - Solved with using pure python
    - IMO JSON exporter solves both of these problems
- [Tammy] PTAL instrumentation HTTP semonv opt-in docs update [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4254](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4254)
  - More doc updates depend on this ([DB opt-in](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4980), [otel.io update](https://github.com/open-telemetry/opentelemetry.io/issues/11386))
- [Dylan] [Minor PR improving log messages when there’s a DependencyConflict:](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5025)
- [Emidio]  Anyone interested in [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4843](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4843) ?
  - Check if we really need a different package
  - Host is an entity in semconv
- [Emidio] Are we fine with this change [https://github.com/open-telemetry/opentelemetry-python/pull/5637](https://github.com/open-telemetry/opentelemetry-python/pull/5637) ?
  - No objections
