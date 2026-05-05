## Meeting Notes

### Attendees
- Liudmila Molkova (Grafana Labs)
- Trask Stalnaker (Microsoft)
- [Scott Gerring](mailto:scott@datadoghq.com)(Datadog)
- Armin Ruech (Dynatrace)
- Joao Grassi (Dynatrace)
- Christophe Kamphaus
- Daniel Dyla (Dynatrace)
- Yordis Prieto (Straw Hat, LLC)
- Michele Mancioppi (Dash0)

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/proje](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - [cts/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
- Profiling SIG context OTEPs and semantic conventions ([Scott Gerring](mailto:scott@datadoghq.com))
  - [OTEP-4719](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/profiles/4719-process-ctx.md) added support for for sharing process-wide context - Resource and custom other - with an out of process reader (e.g. the full host profiler)
  - [OTEP-4947](https://github.com/open-telemetry/opentelemetry-specification/pull/4947) aims to build on this to share request/thread context information, using OTEP-4719 to expose additional configuration information
  - To do this, we need to agree on the name for an attribute here and it seems like this might be a good thing to have in the semconv. Some discussion [here](https://github.com/open-telemetry/opentelemetry-specification/pull/4947#discussion_r3100465935)
- [trask] GenAI
  - [https://github.com/open-telemetry/semantic-conventions/pull/3696](https://github.com/open-telemetry/semantic-conventions/pull/3696)
  - [https://github.com/open-telemetry/admin/pull/630](https://github.com/open-telemetry/admin/pull/630)
  - Preserving history in new repo
- [joao] Metric requirement level in YAML
  - Weaver part is merged [https://github.com/open-telemetry/weaver/pull/1381](https://github.com/open-telemetry/weaver/pull/1381)
  - I will start preparing semconv and update yaml files to include it. Leave as a draft PR until we release Weaver
- [yordis] Monolithic Deployment
  - Service and Namespaces
  - Event Sourcing and Messaging System tagging
