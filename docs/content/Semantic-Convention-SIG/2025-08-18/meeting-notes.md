## Meeting Notes

### Attendees
- [Daniel Dyla](mailto:dyladan@gmail.com)
- [Josh Suereth (Big Nerd)](mailto:joshuasuereth@google.com)
- Armin Ruech (Dynatrace)
- Liudmila Molkova (Grafana Labs)
- Trask Stalnaker (Microsoft)
- Christophe Kamphaus
- Aaron Abbott (Google)
- Matthew Hensley (Grafana Labs)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/projects/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [Liudmila, 2 min] Announcement: RPC semconv stabilization -  [https://strawpoll.com/kjn1Dmoz0yQ](https://strawpoll.com/kjn1Dmoz0yQ), [https://github.com/open-telemetry/community/pull/2684](https://github.com/open-telemetry/community/pull/2684)
  - [Liudmila, 5 min] Planning to merge GenAI complex attributes soon [https://github.com/open-telemetry/semantic-conventions/pull/2179](https://github.com/open-telemetry/semantic-conventions/pull/2179)
  - [christophe 15] Info metrics [https://github.com/open-telemetry/semantic-conventions/issues/2595](https://github.com/open-telemetry/semantic-conventions/issues/2595)
    - PR split into two:
      - General guidance on pipeline-run metrics
      - info metrics are pure gauges
        - What are these needed for now?
        - link between entities
        - Cannot just add to resource attributes in all environments
          - e.g. in k8s, state metrics for container where pipeline runs, can't just add attributes here.
        - Can aggregate metrics across nodes into pipeline
  - [suereth, 10 min] What do we do with issues for owners that are not active?
    - Hopefully with [https://github.com/open-telemetry/semantic-conventions/pull/2648](https://github.com/open-telemetry/semantic-conventions/pull/2648) and some copilot help, we should be able to automatically comment on such PRs/issues that SIG is not active. At least that’s the wish :D
      - Automation:
        - When a feature request is raised against area that does not accept contributions
          - Automation adds a label and a comment saying that we don't accept it
          - Gives time to appeal
          - Closes the PR after time
