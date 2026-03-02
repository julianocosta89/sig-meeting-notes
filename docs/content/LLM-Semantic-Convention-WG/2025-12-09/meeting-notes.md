## Meeting Notes

### Attendees
- Ridhima Satam (Cisco/Splunk)
- Dylan russell (google)
- Aaron Abbott (Google)
- Dat Ngo (Arize)
- Xander Song (Arize)
- Shuwen Pan (Cisco)
- Ankit Singhal (Microsoft)
- Alex Hall (Pydantic)
- Pradeep Nair (Cisco/Splunk)
- Pavan (Cisco)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- [Liudmila] MCP: [https://github.com/open-telemetry/semantic-conventions/pull/2083](https://github.com/open-telemetry/semantic-conventions/pull/2083)
- [Teja] Need help with merging this PR
- [Ridhima] -
  - Proposal for below 2 PRs - [https://github.com/keith-decker/semantic-conventions/blob/7c295bedcc918b00ca37f3124211bd5adee838d9/docs/gen-ai/gen-ai-agent-proposal.md](https://github.com/keith-decker/semantic-conventions/blob/7c295bedcc918b00ca37f3124211bd5adee838d9/docs/gen-ai/gen-ai-agent-proposal.md)
    - Workflow vs invoke_agent
      - Some frameworks have extra layer: crio.ai kick-off, langchain/langgraph (first chain)
      - Aaron: For google ADK there is always a root agent that wraps the orchestration.
        - you create a "workflow agent" [https://google.github.io/adk-docs/agents/workflow-agents/](https://google.github.io/adk-docs/agents/workflow-agents/)
      - Alex: should OpenAI agents have outer layer?
      - Workflow is outer layer, there will be nested invoke_agents,  workflow duration is interesting (e2e), most fx will have means to differentiate outer from innerx
    - Step vs invoke agent
      - Maybe specific to framework
  - New spans for Agentic systems PR for review - https://github.com/open-telemetry/semantic-conventions/pull/3179
  - New metrics for agentic systems PR for review - [https://github.com/open-telemetry/semantic-conventions/pull/3189](https://github.com/open-telemetry/semantic-conventions/pull/3189)
- [Pradeep / Pavan] Go over the scenarios for `[session.id](http://session.id)` we have documented in our new doc - [https://github.com/open-telemetry/semantic-conventions/issues/2883](https://github.com/open-telemetry/semantic-conventions/issues/2883)
  - [aaron] My understanding as A2A also considers session == conversation [A2A docs](https://a2a-protocol.org/latest/specification/#341-context-identifier-semantics:~:text=All%20tasks%20and%20messages%20with%20the%20same%20contextId%20SHOULD%20be%20treated%20as%20part%20of%20the%20same%20conversational%20session)
  - > All tasks and messages with the same contextId SHOULD be treated as part of the same conversational session
- [Ankit]: [Built-in Tools Support by singankit · Pull Request #3038 · open-telemetry/semantic-conventions](https://github.com/open-telemetry/semantic-conventions/pull/3038)
  - We can't realistically define all possible tools for all providers
  - There might be a few like code interpreter
  - Still need discriminator
- PRs to review:
  - Cached tokens [https://github.com/open-telemetry/semantic-conventions/pull/3163](https://github.com/open-telemetry/semantic-conventions/pull/3163)
    - Built-in tools [https://github.com/open-telemetry/semantic-conventions/pull/3038](https://github.com/open-telemetry/semantic-conventions/pull/3038)
    - Retrieval span: [https://github.com/open-telemetry/semantic-conventions/pull/2924](https://github.com/open-telemetry/semantic-conventions/pull/2924)
    - Workflow [https://github.com/open-telemetry/semantic-conventions/pull/3179](https://github.com/open-telemetry/semantic-conventions/pull/3179)
