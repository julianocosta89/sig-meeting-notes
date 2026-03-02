## Meeting Notes

### Attendees
- Liudmila Molkova (Microsoft)
- Ridhima Satam (Cisco/Splunk)
- Austin Born (Shinzo Labs)
- Alex Hall (Pydantic)
- Tao Chen (Microsoft)
- Paul Shealy (Microsoft)
- Shipra Jain (Microsoft)
- Aaron Abbott (Google)
- Aishwarya (Nutanix)
- Guangya Liu (IBM)
- Xander Song (Arize)
- Matthew Hensley (Grafana Labs)

### Agenda
- Standing topics:
  - Triage
    - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
- Ridhima - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3600](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3600)
- [liudmila, 5 min] Call to review openai instrumentation  for JS
- [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2941](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2941)
  - Please review, Sergey will ask Splunk approver to take a look
  - Please consider being component owner
- [liudmila, 15 min] [Inputs and outputs PR](https://github.com/open-telemetry/semantic-conventions/pull/2179): open discussions
  - Couple of PRs depend on it (chat history representation)
    - [https://github.com/open-telemetry/semantic-conventions/pull/2551](https://github.com/open-telemetry/semantic-conventions/pull/2551)
    - [10 mins] [https://github.com/open-telemetry/semantic-conventions/pull/2528](https://github.com/open-telemetry/semantic-conventions/pull/2528)
  - Instructions
    - naming
    - Sensitivity - usually not sensitive, but sometimes are
    - Parametrized prompts will come via specific structured type inside instructions attribute (`any` today)
  - define agent input and output better:
    - Do we record intermediate llm and tool calls on the agent span (they are duplicated on nested spans)
    - When openai API returns info about tools called, where do we put it (output or input)
      - Let's put built-in tool into output
      - Liudmila will update PR to include built-in tool example
      - Let's at least for now not try to address all agent concerns in the LLM PR.
- [everyone, 20min] Agent PRs
  - [https://github.com/open-telemetry/semantic-conventions/pull/2528](https://github.com/open-telemetry/semantic-conventions/pull/2528)
  - [https://github.com/open-telemetry/semantic-conventions/pull/2551](https://github.com/open-telemetry/semantic-conventions/pull/2551)
    - Targeting lanchain, llamaindex
- Sergey/Ridhima[2 mins] - genAI utils proposal - [https://docs.google.com/document/d/1w9TbtKjuRX_wymS8DRSwPA03_VhrGlyx65hHAdNik1E/edit?tab=t.qneb4vabc1wc](https://docs.google.com/document/d/1w9TbtKjuRX_wymS8DRSwPA03_VhrGlyx65hHAdNik1E/edit?tab=t.qneb4vabc1wc)
- [Guangya 3 mins] feat: New GenAI agent entity spans that records information like the span kind, input, output, outcome etc
  - Do we need this entity type? The benefit is filtering and querying
  - [https://github.com/open-telemetry/semantic-conventions/pull/2551](https://github.com/open-telemetry/semantic-conventions/pull/2551)
