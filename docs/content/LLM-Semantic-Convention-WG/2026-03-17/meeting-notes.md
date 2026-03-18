## Meeting Notes

### Attendees
- Keith Decker (Cisco/Splunk)
- Jamie Danielson (Honeycomb)
- Robb Kidd (Honeycomb)
- Aaron Abbott (Google)
- Ankit Singhal (Microsoft)
- Liudmila Molkova
- Josh Winerman (Cisco/Splunk)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - ReAct: [https://github.com/open-telemetry/semantic-conventions/issues/3419](https://github.com/open-telemetry/semantic-conventions/issues/3419)
    - Workflow
      - Invoke_agent
        - ReAct / chain
          - Llm
          - Execute_tool
    - Pros: better grouping for detailed debugging
    - Cons: noisy and can be
  - [everyone, 5 min]  Intro for new members
- [Trask, 5 min] [Split invoke_agent into separate client and internal spans, and split attributes from inference hierarchy](https://github.com/open-telemetry/semantic-conventions/pull/3514)
- [Ankit/Trask, 5 min] [Invoke agent server span](https://github.com/open-telemetry/semantic-conventions/pull/3473)
  - What’s the difference between invoke_agent server and internal spans?
  - A2A
    - Http or grpc
  - LangChain api_server
  - Would everyone do this:
    - Protocol-level server (HTTP, gRPC, stdio)
      - Invoke_agent internal
  - Different use-cases(?):
    - Cloud provider / managed AI agent servers
      - Protocol + Internal
      - Server
    - Self-hosted agents with A2A / langchain / etc
      - Protocol + Internal
  - Would MCP servers be similar?
- [Liudmila] KubeCon next week - GenAI SIG office hours
- [https://cloud-native.slack.com/archives/C06KR7ARS3X/p1773507150948619](https://cloud-native.slack.com/archives/C06KR7ARS3X/p1773507150948619)
- [Surya] Need review on this as I started using pydantic for parsing and validation of responses api
- [Aaron] [https://github.com/open-telemetry/semantic-conventions/pull/3233](https://github.com/open-telemetry/semantic-conventions/pull/3233)
- [Keith] Pending PRs on GenAI Utils types
  - ToolCall Type: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4218](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4218)
  - Embedding Type: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4219](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4219)
  - Agent Types: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4217](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4217)
