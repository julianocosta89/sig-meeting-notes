## Meeting Notes

### Attendees
- Aaron Abbott (Google)
- Sergey Sergeev (Cisco/Splunk)
- Xander Song (Arize)
- Keith Decker (Cisco/Splunk)
- Ridhima Satam (Cisco/Splunk)
- Alex Hall (Pydantic)
- Shuwen Pan (Cisco)
- Susan Chang (Elastic)
- Dat Ngo (Arize)
- Antoine Toulme (Splunk)
- Pablo Collins (Splunk)
- Ankit Singhal (Microsoft)

### Agenda
- Standing topics:
  - Triage
    - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
- [let’s postpone it to the next APAC meeting][Minghui, 10min] MCP PR: [https://github.com/open-telemetry/semantic-conventions/pull/2083#discussion_r2204555762](https://github.com/open-telemetry/semantic-conventions/pull/2083#discussion_r2204555762)
  - short name of unix domain socket
  - why we need the first layer of arguments
  - record the output of mcp
- [Ankit, 15 min] [Gen AI Evaluation Result Event](https://github.com/open-telemetry/semantic-conventions/pull/2563)
  - [https://github.com/open-telemetry/semantic-conventions/pull/2563#discussion_r2258068645](https://github.com/open-telemetry/semantic-conventions/pull/2563#discussion_r2258068645)
    - Close on Event, Span or Event + Span for capturing Evaluation Result.
  - Ankit to open a separate issue for representing eval scores on spans, and go ahead with the existing event approach
- [Ridhima 2mins] - please review PR for langchain instrumentation adding span support for llm invocation - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3665](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3665)
  - Question about gen ai provider vs gen ai system.
  - Thinking of recording gen_ai.framework with langchain in order to show which framework is in use in the AI
  - [Alex] we had a discussion about system vs provider but didn’t resolve it completely on the PR which added provider name
  - [aaron] is propagation working with Lanchain? I remember an issue with callbacks
  - [Aaron] I had some concerns around double capturing the completion events
    - What happens if openai-v2 and langchain are installed?
      - [Sergey] you would get double for now
      - Maybe users can install one or the other, we can have some guidance
      - [aaron] I don’t love that because the agent level spans are really important (tools, conversation id, invocation spans, etc.). So shouldn’t have to choose one or the other
    - We can make them coexist as previously discussed with a context attribute
- [Keith 2min] - Maintainer Review of GenAI Utils Structure PR- [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3672](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3672)
- [Aaron, 5m] [https://github.com/open-telemetry/semantic-conventions/pull/2179](https://github.com/open-telemetry/semantic-conventions/pull/2179)
  - [Ankit] is tool name sufficient to identify tools?
    - Maybe not, especially if you have server side tool calls
    - Maybe we can use a separate “type” message to create namespaces for server side tool, function calling, etc. to keep names unique
  - [Alex] (already commented) I thought we agreed to remove the prompt/response details from the agent spans
    - [Aaron] +1
  - [Alex] I forget the context of having completion and span events. I’m not very invested but it is weird
    - [Aaron] we want them in the case of sampling or as server side events emitted by a model provider. But mainly sampling. We have customers who want 100% capturing for compliance purposes
    - Aaron will dig up the context in old threads
