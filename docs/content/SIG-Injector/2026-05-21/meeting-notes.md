## Meeting Notes

### Attendees
- Nikola Grcevski (Grafana)
- Bastian Krol (Dash0)
- Antoine Toulme (Splunk)

### Agenda
- Copy-relocation bug ([https://github.com/open-telemetry/opentelemetry-injector/issues/348](https://github.com/open-telemetry/opentelemetry-injector/issues/348))
  - Switch to getenv instead of reading from __environ
  - Do we use getenv in both branches or only in the fallback branch for old distribution (libc vs. libdl)? => For both branches.
  - Optionally with a feature flag for reverting back to reading __envirion? (Maybe not necessary)
- [Antoine] Revisit [https://github.com/open-telemetry/opentelemetry-injector/issues/176](https://github.com/open-telemetry/opentelemetry-injector/issues/176)
  - we would like to use the injector, but our distribution requires additional env vars that do not start with OTEL_.
    - We can use a compile-flag to override that default setting. It needs to be a list.
    - [https://github.com/open-telemetry/opentelemetry-injector/issues/351](https://github.com/open-telemetry/opentelemetry-injector/issues/351) filed
- [Antoine] sidebar on signing: [https://github.com/open-telemetry/opentelemetry-injector/issues/350](https://github.com/open-telemetry/opentelemetry-injector/issues/350) is open, low priority.
