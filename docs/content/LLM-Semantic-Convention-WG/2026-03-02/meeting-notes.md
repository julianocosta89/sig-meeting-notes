## Meeting Notes

### Attendees
- Sergey Sergeev (Cisco/Splunk)
- Tao Chen (Microsoft)
- Keith Decker (Cisco/Splunk)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Nagkumar Arkalgud (Microsoft)
- Aditya Mehra (Cisco/Splunk)

### Agenda
- Does semantic kernel/microsoft agentic framework extend semconv
  - Workflows are extending the semconv, but not prefixing with gen_ai. …
  - Workflows are a more generic than GenAI
  - Workflow may be one node sending messages to other nodes
  - Workflow is composed of multiple agents, each agent may do other GenAI ops. Sequentially or in parallel, loops, conditions, etc. Many patterns. It can be a mix of Agent/non-agent, any graph.
  - Q: When span parent-child is not sufficient, or trace_id is not sufficient?
    - when agents  communicate using messages, MS team is using span link.
  - Tao and the team to review invoke_workflow span PR [https://github.com/open-telemetry/semantic-conventions/pulls/wrisa](https://github.com/open-telemetry/semantic-conventions/pulls/wrisa)
- [Erden] Add Agent type into GenAI Utils based on [semconv](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/gen-ai-agent-spans.md)
  - Create_agent span [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4217](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4217)
  - Invoke_agent span https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4274
- [Surya] Understanding scenarios where create_agent span is used. Should we update the docs with examples and scenarios.
