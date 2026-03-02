## Meeting Notes

### Attendees
- Liudmila
- Alex
- Keith Decker (Cisco/Splunk)
- Pradeep Nair (Cisco/Splunk)
- Dat Ngo (Arize)
- Aaron Abbott
- Xander Song (Arize)
- Bruno Baptista (IBM)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
    - Task/workflow:
      - AI: Liudmila will setup official OTel agents call
      - Start with Mon 9am-9:30 am PT and group can decide if to reschedule it
        - Let’s make sure Dani and IBM folks have a chance to join
  - [everyone, 5 min]  Intro for new members
- [Liudmila] Python GenAI reviews and component owners - need revamp and people committed to reviewing PRs
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pulls?q=is%3Apr+is%3Aopen+gen-ai](https://github.com/open-telemetry/opentelemetry-python-contrib/pulls?q=is%3Apr+is%3Aopen+gen-ai)
    - Liudmila will send a PR to update component owners
    - Let's prioritize reviewing PRs
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/blob/1d9728297742f5e772e33a70290307685ae0da2c/.github/component_owners.yml#L25](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/1d9728297742f5e772e33a70290307685ae0da2c/.github/component_owners.yml#L25)
- [Liudmila] MCP: https://github.com/open-telemetry/semantic-conventions/pull/2083
  - Params: per-each-key vs all
    - Would people want to capture all or individual properties?
  - Upload large - add section?
  - Will follow-up in separate PR
- [Teja] Add instrumentation for anthrophic sdk [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3949](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3949)
- [Keith] Two GenAI PRs for review
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891)
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3862](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3862)
    - Ready to merge
- [Liudmila] From CI/CD group: Unified workflow conventions
  - [https://github.com/open-telemetry/semantic-conventions/issues/1688](https://github.com/open-telemetry/semantic-conventions/issues/1688)
  - [https://github.com/thompson-tomo/semantic-conventions/pull/146](https://github.com/thompson-tomo/semantic-conventions/pull/146)
  - Cloudflare worker otel: [https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/](https://developers.cloudflare.com/workers/observability/traces/spans-and-attributes/)
  - [https://developers.cloudflare.com/workflows/reference/event-subscriptions/](https://developers.cloudflare.com/workflows/reference/event-subscriptions/)
