## Meeting Notes

### Attendees
- Michele Mancioppi (Dash0)
- Liudmila Molkova (Grafana Labs)
- Josh Suereth
- Christophe Kamphaus

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
    - [https://github.com/open-telemetry/semantic-conventions/pull/2619](https://github.com/open-telemetry/semantic-conventions/pull/2619)
      - Let's add GCP approver team
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - Status of the [Introduce service.peer.name and service.peer.namespace; deprecate peer.service](https://github.com/open-telemetry/semantic-conventions/pull/3097) PR
    - Comments addressed
    - Michele will make a case
      - Strong data supporting service.namespace
      - DashO would support setting service.peer.namespace
      - service.peer.name could be stabilized soon
  - [https://github.com/open-telemetry/community/issues/3189](https://github.com/open-telemetry/community/issues/3189) // Sudarshan Soma from Oracle.
    - Group for oracle db
    - Alternative (recommendation): host Oracle DB semconv in oracle ecosystem, importing otel
      - We could add a link to external oracle conventions
      - We'd support you in the process being an early adopter
  - [https://github.com/open-telemetry/semantic-conventions/pull/3212](https://github.com/open-telemetry/semantic-conventions/pull/3212) Kai
    - Adding ibmmq as messaging.system
    - Messaging group is on pause
  - Last call of the year, see you in 2026!
