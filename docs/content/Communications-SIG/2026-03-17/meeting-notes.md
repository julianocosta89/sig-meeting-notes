## Meeting Notes

### Attendees
- Marylia Gutierrez (Grafana Labs)
- Tiffany Hrabusa (Grafana Labs)
- Vitor Vasconcellos (Mercado Libre)
- Jay DeLuca (Grafana Labs)
- Severin Neumann

### Agenda
- [Tiffany] I’d like to propose a section in the docs nav: Compatibility. Current idea is to put in under Concepts (see issue)
  - Context: [This PR](https://github.com/open-telemetry/opentelemetry.io/pull/9263) and the LFX mentorship on Prometheus-OTel interoperability highlight the need for a docs section that addresses this type of content. Concerns have been raised by some in the Prometheus community that the Migration section might not be the right place since it implies, if doesn’t actually mean, deprecation.
  - Issue for comments/discussion: [https://github.com/open-telemetry/opentelemetry.io/issues/9379](https://github.com/open-telemetry/opentelemetry.io/issues/9379)
- [Vitor] Can we have webhooks to integrate GitHub with our channel?
  - *“this Slack channel receives a reminder notice on the day when a post needs to be published. So once the PR has the necessary approvals and the publication date rolls around, we get a notification here.”*
  - [Action item] Vitor will explore what are the possibilities to integrate (CNCF ticket, maybe?)
  - [Action item] Tiffany will ping Austin about access to Buffer for more people
- [Vitor] Agentic skills? [Introduce agentic skills for OTel.io docs workflows #9397](https://github.com/open-telemetry/opentelemetry.io/issues/9397)
  - Instrumentation examples:
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/.github/agents](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/.github/agents)
    - [https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/.github/workflows/code-review-sweep.yml](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/.github/workflows/code-review-sweep.yml)
- [Jay] FYI: Upcoming Collector automation updates
  - Fix tests in CI
  - Add display names
  - Deprecated tables
- [Vitor] Spec compliance matrix - [docs(specs): Publish spec compliance matrix #9358](https://github.com/open-telemetry/opentelemetry.io/pull/9358)
  - How maintainable will this be in the long term?
  - Low priority, we should wait until Patrice is back
- [Tiffany] Mini Collector docs refactoring update
