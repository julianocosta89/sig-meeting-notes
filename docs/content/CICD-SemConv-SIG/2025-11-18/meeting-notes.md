## Meeting Notes

### Attendees
- Christophe Kamphaus
- Dotan Horovits (OpenSearch, AWS)
- Carlos Alberto Cortez (OTel TC liaison)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Project Board: [https://github.com/orgs/open-telemetry/projects/171](https://github.com/orgs/open-telemetry/projects/171)
- General
  - [christophe, 5 min] - Feedback unified workflow semantics
    - Brought up in yesterday’s SemConv meeting
      - [https://github.com/open-telemetry/semantic-conventions/issues/1688](https://github.com/open-telemetry/semantic-conventions/issues/1688)
      - [https://github.com/thompson-tomo/semantic-conventions/pull/146](https://github.com/thompson-tomo/semantic-conventions/pull/146)
      - Cloudflare worker otel: [https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/)
      - [https://developers.cloudflare.com/workflows/reference/event-subscriptions/](https://developers.cloudflare.com/workflows/reference/event-subscriptions/)
  - Long-running traces issue [https://github.com/open-telemetry/semantic-conventions/issues/1648](https://github.com/open-telemetry/semantic-conventions/issues/1648)
    - Carlos to take it (Christophe to assign)
  - Outstanding PRs pending merge
    - Carlos looked into it:
      - Python for env carrier
      - Go for env propagator
      - Any others? Swift?
    - What would be the right way to track those on our (CI/CD SIG) end? (given that the SIG doesn’t own it) - Carlos thinks that as a github issue, but will take it with the TC to discuss and provide feedback.
      - Easier for OTel projects under same github org, but for external org’s it’s more challenging (e.g. on Jenkins, TeamCity etc.)
