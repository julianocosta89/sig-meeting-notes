## Meeting Notes

### Attendees
- Diego Hurtado (Dash0)
- Tammy Baylis (SolarWinds)
- Riccardo Magliocchetti (Elastic)
- Carlos Cortez (Dash0)
- Aaron Abbott (google)
- Keith Decker (Cisco/Splunk)
- Liudmila Molkova (Google) first 30 mins
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Emídio
- Shuwen Pan (Cisco)
- Pablo Collins (Cisco)
- Lukas Hering (Oracle)

### Agenda
- [carlos] Status of stale PRs
  - Applied feedback but no activity afterwards
    - [https://github.com/open-telemetry/opentelemetry-python/pull/4822](https://github.com/open-telemetry/opentelemetry-python/pull/4822)
    - [https://github.com/open-telemetry/opentelemetry-python/pull/4995](https://github.com/open-telemetry/opentelemetry-python/pull/4995)
  - Need some action (maybe close?) from maintainers
    - [https://github.com/open-telemetry/opentelemetry-python/pull/4841](https://github.com/open-telemetry/opentelemetry-python/pull/4841)
    - [https://github.com/open-telemetry/opentelemetry-python/pull/5296](https://github.com/open-telemetry/opentelemetry-python/pull/5296)
    - [https://github.com/open-telemetry/opentelemetry-python/pull/5323](https://github.com/open-telemetry/opentelemetry-python/pull/5323)
- [Diego] 6 approvals, please merge: [https://github.com/open-telemetry/opentelemetry-python/pull/5293](https://github.com/open-telemetry/opentelemetry-python/pull/5293)
  - Let’s remove then
- [Diego] [https://github.com/open-telemetry/opentelemetry-python/issues/5385#issuecomment-4927072278](https://github.com/open-telemetry/opentelemetry-python/issues/5385#issuecomment-4927072278)
  - Leighton: I’d prefer to use labels instead of assignment
    - Carlos: we use labels in specification
  - Riccardo: I think we have more low handing fruit lille github settings for limiting number of open PRs from new contributors
    - Leighton: i actually prefer contributors split up large prs into multiple so the pr limitation might discourage that.
      - Not a huge opinion ^ perhaps if we find a reasonable limitation amount, this is non-issue
  - Let’s discuss again next week or offline before that
- [carlos] Strategy for declarative config changes, e.g. separate package, language specific instrumentation
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5356](https://github.com/open-telemetry/opentelemetry-python/pull/5356)
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5372](https://github.com/open-telemetry/opentelemetry-python/pull/5372)
  - Will merge Diego PR first and then do the move to the separate package
