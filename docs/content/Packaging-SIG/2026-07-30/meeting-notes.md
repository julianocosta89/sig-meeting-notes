## Meeting Notes

### Attendees
- Antoine Toulme (Splunk)
- Denys Sedchenko (Grafana Labs)
- Diego Hurtado [ocelot](Dash0)
- Michele Mancioppi (Dash0)

### Agenda
- Antoine: [https://github.com/open-telemetry/opentelemetry-packaging/issues/52](https://github.com/open-telemetry/opentelemetry-packaging/issues/52)
- Denys: Second COPR PoC build, based on opentelementry-packaging:
  - COPR repo: [https://copr.fedorainfracloud.org/coprs/x1unix/opentelemetry-packaging/](https://copr.fedorainfracloud.org/coprs/x1unix/opentelemetry-packaging/)
  - GitHub fork: [https://github.com/x1unix/opentelemetry-packaging](https://github.com/x1unix/opentelemetry-packaging)
  - Build: [https://github.com/x1unix/opentelemetry-packaging/actions/runs/30514516950](https://github.com/x1unix/opentelemetry-packaging/actions/runs/30514516950)
  - Known Issues:
    - Build cannot be airgapped. COPR builds are running with internet access.
    - Python bundle is pinned to particular CPython 3.11 ABI. Fedora ships 3.14.
