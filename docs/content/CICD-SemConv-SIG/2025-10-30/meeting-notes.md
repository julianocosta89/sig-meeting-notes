## Meeting Notes

### Attendees
- Dotan Horovits (AWS, OpenSearch)
- Dan Gomez Blanco (New Relic)
- Johannes Koch (FICO)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Project Board: [https://github.com/orgs/open-telemetry/projects/79](https://github.com/orgs/open-telemetry/projects/79)
- General
  - [Dan, 5 min] - New board and archiving existing board - Dan to share the doc with the instructions
    - Propose actions:
      - Create new GitHub Project (i.e. board) for CI/CD Phase 2
        - Add description, README and start/target date as an update (see Phase 1 for reference)
      - Move “No Status” and “Todo” tasks from old project to new project
      - Add a status update to Phase 1 project board to move it to “complete”. This will change OpenTelemetry Roadmap issue to closed.
      - Create PR to community repo to:
        - Move ci-cd.md to completed-projects dir
        - Update board link in ci-cd-phase-2.md
        - Add project ID (i.e. number in URL) to sigs.yml in the corresponding roadmapProjectIDs (you can leave the existing project there to signal in the roadmap that the work is finished if you want)
      - More info on OpenTelemetry Roadmap management in [https://github.com/open-telemetry/community/blob/main/roadmap-management.md](https://github.com/open-telemetry/community/blob/main/roadmap-management.md)
  - [Dan, 5min] New OTel Roadmap is auto-synched from the project board issue (short description, status etc.)
  - [Johannes, 5min] How do we pitch to vendors to adopt - the blog post is useful: [https://www.cncf.io/blog/2024/11/04/opentelemetry-is-expanding-into-ci-cd-observability/](https://www.cncf.io/blog/2024/11/04/opentelemetry-is-expanding-into-ci-cd-observability/)
  - Should we cancel the meeting during kubecon? And can we get SIG presence on the ground at the conf? (at OTEL Observatory?)
