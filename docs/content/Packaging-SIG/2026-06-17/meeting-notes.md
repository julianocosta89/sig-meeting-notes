## Meeting Notes

### Attendees
- Ted Young (Grafana Labs)
- Denys Sedchenko (Grafana Labs)
- Sina P (Canonical)
- Michele Mancioppi (Dash0)

### Agenda
- Change meeting time to take over half of the injector meeting
- Status of the metapackage spec: [https://github.com/open-telemetry/opentelemetry-packaging/pull/10](https://github.com/open-telemetry/opentelemetry-packaging/pull/10)
  - OpAMP discussions have not progressed yet
    - Michele to open issue on the OpAMP repo with proposal
  - Michele to reach out to Jakob about OTel Operator status
  - Single configuration file would be desirable, but unfeasible with the current status of the declarative configurations (see this [comment](https://github.com/open-telemetry/opentelemetry-packaging/pull/10/changes#r3429403577))
- Updates regarding [package hosting research](https://github.com/open-telemetry/opentelemetry-packaging/issues/4).
  - Cosign won’t work for DEB/RPM repos.
  - OpenBuildService access.
- Build and delivery of packages:
  - Try in parallel OBS and Launchpad to weigh pros and cons
    - Launchpad:
      - Will it be consumable by Debian as well?
      - Can we have own SSL certificate and CNAME like [packages.opentelemetry.io/apt](http://packages.opentelemetry.io/apt) or so
    - OBS: how complex is the setup?
  - Michele to open a PR with a local build of the packaging process
    - But we could already have a PoC with the initial packaging done in the Injector project: [https://github.com/open-telemetry/opentelemetry-injector/pull/239](https://github.com/open-telemetry/opentelemetry-injector/pull/239)
