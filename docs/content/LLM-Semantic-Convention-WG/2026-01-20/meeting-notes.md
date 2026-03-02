## Meeting Notes

### Attendees
- Ankit Singhal (Microsoft)
- Alex Boten (Honeycomb)
- Dat Ngo (Arize)
- Ridhima Satam (Cisco/Splunk)
- John McBride (Paper Compute)
- [Sujay Solomon](mailto:sujaysolomon@google.com) (Google)
- Aaron Abbott (Google)
- Jeff Luo (Google)
- Keith Decker (Cisco/Splunk)
- Jamie Danielson (Honeycomb)
- Zach Groves (Datadog)
- Pavan (Cisco)
- Joshua Winerman (Cisco/Splunk)
- Liudmila Molkova (Grafana LAbs)
- Neil Yashinsky ([Context Core](https://github.com/neil-the-nowledgable/contextcore/tree/main))
- Kyle Hounslow (AWS/OpenSearch)
- Shuwen Pan (Cisco)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- [Ankit]: [Built-in Tools Support by singankit · Pull Request #3038 · open-telemetry/semantic-conventions](https://github.com/open-telemetry/semantic-conventions/pull/3038)
- [Pavan, 5m] - continuing the session.id proposal discussion - [https://github.com/open-telemetry/semantic-conventions/issues/2883](https://github.com/open-telemetry/semantic-conventions/issues/2883)
  - Had a talk with Otel browser SIG last week, and they largely agreed that -
    - We could reuse the attribute within GenAI namespace as long it’s an user initiated task
    - **GenAI instrumentations**:
      - Read and attach `session.id` when present
      - Carried over by Otel baggage
        - via HTTP / manual context injection
        - via Agentic protocols.
- [Josh] No discussion, can I get some more review on [https://github.com/open-telemetry/semantic-conventions/pull/2924](https://github.com/open-telemetry/semantic-conventions/pull/2924)?
- [Ridhima] - No discussion, asking for reviews
  - Langchain llm invocation using utils - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3889](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3889)
  - Workflow operation name in agent span  [https://github.com/open-telemetry/semantic-conventions/pull/3249](https://github.com/open-telemetry/semantic-conventions/pull/3249)
