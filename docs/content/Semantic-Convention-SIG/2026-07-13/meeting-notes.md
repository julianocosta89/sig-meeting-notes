## Meeting Notes

### Attendees
- Josh Suereth
- Michele Mancioppi (Dash0)
- Christophe Kamphaus
- Daniel Dyla (Dynatrace)
- Ruediger Schulze (IBM)
- Liudmila Molkova (Google)
- Armin Ruech (Dynatrace)
- Kathie Huang [Datadog]

### Agenda
- [Kathie] Azure Container App replica name PR [https://github.com/open-telemetry/semantic-conventions/pull/3860](https://github.com/open-telemetry/semantic-conventions/pull/3860)
  - Next Steps
    - Cloud-Semconv SIG proposal
    - Continue issuing point-fixes and uses exception process
- [Liudmila] v2 migration [https://github.com/open-telemetry/semantic-conventions/issues/3808](https://github.com/open-telemetry/semantic-conventions/issues/3808)
  - Zos entities: need refinement for entities (with or without federation)
  - Minor plan revision
    - Convert some problematic definitions to v2 initially
      - Public attribute groups: exceptions, server, client, etc
      - Messaging - define proper spans - big change
      - Faas - same
      - Azure and browser events - body fields to attributes
    - Alternative: support side-by-side v1 and v2 rendering
    - AI: Liudmila to start a thread in public semconv slack and post PRs there
- [Lewis] Azure Functions instance Id !=  Azure receiver collector instance id, and so on
  - AzFunc covered by AppService id
  - Maybe also logic apps
  - Collector assigns uuid?
  - Can we override the default
  - Does collector need to do resource detection for FaaS - probably not
  - Liudmila will tag Azure Functions OTel people on the PRs
- [Liudmila] Shared weaver packages
  - AI: Liudmila to finish weaver-packages PR
    - Semconv GenAI will be the first target
