## Meeting Notes

### Attendees
- Armin Ruech (Dynatrace)
- [Florian Lehner](mailto:florian.lehner@elastic.co)(Elastic)
- Joao Grassi (Dynatrace)
- Christophe Kamphaus
- Christos Markou (Elastic)
- Liudmila Molkova (Grafana Labs)
- [Daniel Dyla](mailto:dyladan@gmail.com)
- Bertrand Martin (MetricsHub)
- Alexandra Konrad (Elastic)
- James Thompson
- Matthew Hensley (Grafana Labs)
- Josh Suereth [30min late]

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [Florian] pprof specific attributes for Profiling:
  - [christophe 5m] [https://github.com/open-telemetry/semantic-conventions/issues/1714](https://github.com/open-telemetry/semantic-conventions/issues/1714) SemConv for CICD logs
    - Let's document how CI/CD instr can capture logs and associate them with entities
  - [alexandra, 2 min] [https://github.com/open-telemetry/semantic-conventions/issues/2714](https://github.com/open-telemetry/semantic-conventions/issues/2714) - guidance on device namespace
    - Is device mobile-specific?
      - Hardware vs device
        - Device is a very generic namespace - may be confusing
        - Device sounds like something on edge
      - ECS also has it as mobile device
    - Use-case: security, inventory - add info about the machine
    - Need to discuss with client instrumentation
      - Do they even plan to use the `device`?
  - [Liudmila] Schema v2 demo
  - [james] [https://github.com/open-telemetry/semantic-conventions/pull/2422/files](https://github.com/open-telemetry/semantic-conventions/pull/2422/files)
