## Meeting Notes

### Attendees
- Reiley Yang
- Trask
- Jeremy Corley

### Agenda
- [trask] projects in flight
  - Minimum token permissions
    - [https://github.com/open-telemetry/sig-security/issues/148](https://github.com/open-telemetry/sig-security/issues/148)
    - [https://github.com/open-telemetry/community/issues/2860](https://github.com/open-telemetry/community/issues/2860)
  - security-advisories repository
    - Instead of open-telemetry-private org and Grafana dashboard
    - [https://github.com/open-telemetry/community/issues/2869](https://github.com/open-telemetry/community/issues/2869)
- [reiley] security dashboard and maintainers’ accountability definition?
  - [https://github.com/orgs/open-telemetry/security/overview](https://github.com/orgs/open-telemetry/security/overview) has the Dependabot security scan results.
  - Escalate to maintainers:
    - Advisories
      - That haven’t been triaged in X days
      - That have been open (since creation) for more than Y days
    - Dependabot alerts
    - Container images?
    - Ask maintainers
      - What are all artifacts you publish, what tools do you use to check supply chain security
    - SBOMs?
      - This would give us standard thing to scan
    - [https://trivy.dev/latest/](https://trivy.dev/latest/)
