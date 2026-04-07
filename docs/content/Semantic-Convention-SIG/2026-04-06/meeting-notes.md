## Meeting Notes

### Attendees
- …
- Josh Suereth
- Christophe Kamphaus
- Liudmila Molkova
- Dotan Horovits

### Agenda
- Triage
- [victor] OCSF / AI conventions
  - Guardrails - [https://github.com/open-telemetry/semantic-conventions/pull/3233](https://github.com/open-telemetry/semantic-conventions/pull/3233)
  - CNCF slack [https://cloud-native.slack.com/archives/C0715DWUW7L](https://cloud-native.slack.com/archives/C0715DWUW7L)
    - OCSF has new mapping meeting for agent security.
    - Trask will join mapping meetings
- [adriel / christophe 15 minutes] - discuss moving forward with stabilization of CICD semantic conventions and potential breaking changes if we move forward now.
  - Follow up to in-person kubecon discussions with Christophe and Liudmila
  - [https://github.com/open-telemetry/semantic-conventions/issues/1688](https://github.com/open-telemetry/semantic-conventions/issues/1688) – potential blocker/breaking change
    - Usage: People are starting to experiment with workflow visualizations for Agents
    - Long spans / tail-based sampling - not generic to workflows.
- [adriel / christophe 10 minutes] - How do we migrate people for breaking changes if they come up leveraging Weaver/OTel Collector [https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/schemaprocessor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/schemaprocessor)
  - Look into new collector schema-translation component (one for GenAI proposed for collector, Braydon Kains looking into making something more generic)
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46447](https://github.com/open-telemetry/opentelemetry-collector-contrib/pull/46447)
- Liudmila: AI usage disclosure in PR template  [https://github.com/open-telemetry/semantic-conventions/pull/3596](https://github.com/open-telemetry/semantic-conventions/pull/3596)
  - [another attempt] [https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15563](https://github.com/open-telemetry/opentelemetry-java-instrumentation/pull/15563)
    - “have you thoroughly reviewed and understand all of the code written by AI?”
  - Using AI to reply to comments?
    - We do not prefer AI automatically [remove this? addressing and] responding to review comments
  - Github Coding agent only works w/ folks who have write permission (maintainers)
  - Example in Java instrumentation: [https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/.github/agents](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/.github/agents)
- Liudmila: GraphQL conventions - keep them in semconv or explore federating? [https://github.com/open-telemetry/semantic-conventions/pull/3515](https://github.com/open-telemetry/semantic-conventions/pull/3515)
  - Should we see if we can use "federated semconv" for this?
