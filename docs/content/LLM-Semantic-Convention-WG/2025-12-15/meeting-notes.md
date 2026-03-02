## Meeting Notes

### Attendees
- [Sergey Sergeev](mailto:zhirafovod@gmail.com) (Cisco/Splunk)
- Pradeep Nair (Cisco/Splunk)
- Keith Decker (Cisco/Splunk)
- Shuwen Pan (Cisco)
- Surya Teja

### Agenda
- Review Agentic issues
- Semantic conventions
  - Workflow and Session to highlight different use cases. It will replace:
    - Session [https://github.com/open-telemetry/semantic-conventions/issues/2883](https://github.com/open-telemetry/semantic-conventions/issues/2883)
    - Workflow [https://github.com/keith-decker/semantic-conventions/blob/7c295bedcc918b00ca37f3124211bd5adee838d9/docs/gen-ai/gen-ai-agent-proposal.md](https://github.com/keith-decker/semantic-conventions/blob/7c295bedcc918b00ca37f3124211bd5adee838d9/docs/gen-ai/gen-ai-agent-proposal.md)
    - Step (todo)
- Instrumentation
  - Utils GenAI types
    - Inference
      - ✅span
      - ✅metric
      - (in-progress) events
    - InvokeTool (not started)
    - InvokeAgent (not started)
    - CreateAgent (not started)
    - Embeddings (not started)
    - Step (missing semantic conventions)
    - Workflow (missing semantic conventions)
  - action item: Cisco/Splunk discuss internally if we can contribute to it, create github issues with the proposals
- Agentic Frameworks
  - Surya is interested in contributing to Anthropic Agents SDK
    - we have a ticket for Claud SDK [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3949](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3949)
    - Claude Agents is a newer SDK, Surya created a github issue for it.
  - LlamaIndex
  - CrewAI
