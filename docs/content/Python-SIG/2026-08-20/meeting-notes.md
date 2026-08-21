## Meeting Notes

### Attendees
- Dylan Russell (Google	)
- Tammy Baylis (SolarWinds)
- Diego Hurtado (Dash0)
- Riccardo Magliocchetti (Elastic)
- Lukas Hering (Oracle)
- Shuwen Pan (Cisco)
- Carlos Cortez (Dash0)
- Josh Winerman (Cisco/Splunk)
- Leighton Chen (Microsoft)
- Pablo Collins (Cisco)
- Hector Hernandez (Microsoft)

### Agenda
- [Lukas] OracleDB Instrumentation (bringing this into contrib)
  - [https://github.com/herin049/opentelemetry-instrumentation-oracledb](https://github.com/herin049/opentelemetry-instrumentation-oracledb)
  - Pablo: +1
  - Riccardo: is having native support in the client an option?
  - Leighton: adding native support could be a different workstream
  - Tammy: any plan to implement sqlcommenter? +1
    - Lukas: it’s using the dbapi so should be possible
    - Lukas: there should be another way to do tracepropagation without sql commenting
- Diego: [https://cloud-native.slack.com/archives/C0AD17NMBLZ/p1786632144815569?thread_ts=1785918548.209679&cid=C0AD17NMBLZ](https://cloud-native.slack.com/archives/C0AD17NMBLZ/p1786632144815569?thread_ts=1785918548.209679&cid=C0AD17NMBLZ)
  - [https://github.com/open-telemetry/opentelemetry-packaging/pull/64](https://github.com/open-telemetry/opentelemetry-packaging/pull/64)
  - Diego: proposal: relax instrumentations dependencies to ~=
    - Request:
      - Can we have a last release for elasticsearch instrumentation with the relaxed dependency?
        - Riccardo: I would like to not have downstream users cherry-picking instrumentation versions
        - Riccardo: I don’t think dependabot / renovate tools suffice to bump
      - Can we have a stable release for opentelemetry-instrumentation?
        - We discussed this when bumping instrumentations to 1.x outputting stable semconv where available
    - Aaron: please open an issue
- Diego: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4966](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4966)
  - See [https://github.com/open-telemetry/semantic-conventions-conformance](https://github.com/open-telemetry/semantic-conventions-conformance)
  - Tammy: noticed this [https://github.com/open-telemetry/semantic-conventions-conformance/pull/41](https://github.com/open-telemetry/semantic-conventions-conformance/pull/41)
  - Lukas: how is this related to our own weaver wrapper?
    - Possible improvement: Testing with realistic application
  - Carlos: worried about duplicated work
    - [aaron] we do it in the python-genai repo in CI already [https://github.com/open-telemetry/opentelemetry-python-genai/blob/b8c40bbe34e2475523b42bf1b34423a94d9ad949/tox.ini#L14](https://github.com/open-telemetry/opentelemetry-python-genai/blob/b8c40bbe34e2475523b42bf1b34423a94d9ad949/tox.ini#L14)
  - [Aaron] concerned about CI footprint already: [Long Github Actions queue wait times · Issue #3622 · open-telemetry/community](https://github.com/open-telemetry/community/issues/3622)
    - Already running too many checks
    - [Lukas] Maybe only run semconv checks on merge/nightly runs?
  - Riccardo: did e2e using weaver helper we have in core test utils [https://github.com/xrmx/opentelemetry-python-contrib/tree/weaver-e2e-tests](https://github.com/xrmx/opentelemetry-python-contrib/tree/weaver-e2e-tests)
