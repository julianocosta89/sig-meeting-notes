## Meeting Notes

### Attendees
- Aaron Abbott (Google)
- Dylan Russell (Google)
- Leighton Chen (Microsoft)
- Lukas Hering (Oracle)
- Tammy Baylis (SolarWinds)
- Emídio (Independent)
- Riccardo Magliocchetti (Elastic)
- Pablo Collinks (Cisco)

### Agenda
- [Leighton] Introducing new Python SIG maintainers!
  - Lukas and Emídio!
- [Tammy] DB instrumentation metrics are mostly missing. To add them, what do we think of OPT_IN gating and proposed calculations?
  - OP and general discussion: [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/1158#issuecomment-5703555608](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/1158#issuecomment-5703555608)
    - [Lukas] Context: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4481](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4481)
      - We should create common utils because logic should be the same
      - Tammy: doing concrete first in SqlAlchemy and then make them generic may be easier
        - Lukas: the connection related may be concrete only since db api has no connection pool
    - Lukas: No need for opt-in since this are already stable and no previous implementation if they match schema version
      - Leighton: agree
  - We should update semconv version to include this: [https://github.com/open-telemetry/semantic-conventions/pull/4073](https://github.com/open-telemetry/semantic-conventions/pull/4073)
  - Update SQLAlchemy first to modernize one existing metric with opt-in: [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/5060](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/5060)
    - PR for that: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5063](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/5063)
- [Lukas] Populate Resource schema URL from semantic convention version
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5665](https://github.com/open-telemetry/opentelemetry-python/pull/5665)
    - Let’s keep some clarification in the spec before changing implementation
    - Also check what other languages sdks do
