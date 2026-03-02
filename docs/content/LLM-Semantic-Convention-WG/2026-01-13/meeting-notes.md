## Meeting Notes

### Attendees
- Liudmila
- Josh Bonczkowski (New Relic)
- Keith Decker (Cisco/Splunk)
- Aaron Abbott (Google)
- Ridhima Satam (Cisco/Splunk)
- Joshua Winerman (Cisco/Splunk)
- Pavan (Cisco)
- Zach Groves (Datadog)
- Aishwarya (Nutanix AI)
- Shuning Chen (Cisco/Splunk)
- Ankit Singhal (Microsoft)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- [Ridhima] -
  - crio/lanchain/azure ai projects
    - Workflow - useful to separate from regular invoke agent because it's end-to-end operation, but invoke_agent can be either (small or big)
      - Invoke_agent 1
        - Llm
        - Tools
      - Invoke agent 2
  - ADK
    - Invoke_agent orchestrator
      - Invoke_agent 1
      - Invoke_agent 2
  - How to record framework
    - [https://github.com/open-telemetry/semantic-conventions/issues/1229](https://github.com/open-telemetry/semantic-conventions/issues/1229)
    - Instrumentation scope
      - Name  - trace name - name of instrumentation library (otel-instr-langchain-v2)
      - Attributes: name and version of instrumented library
        - Lanchain
- [Surya] - Anthropic instrumentation review [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4034](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4034)
- Let's ask all new contributions to use utils
  - Liudmila will check which ones don't use gen-ai-utls. Create issues - this would be good opportunity to contribute something
- [Minghui] Proposal: allow instrumentations to record individual multimodal data. [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4097](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4097)
  - Liudmila to share in the GenAI call, ask Aaron to take a look
- [Pavan] continuing [session.id](http://session.id) proposal discussion - [https://github.com/open-telemetry/semantic-conventions/issues/2883](https://github.com/open-telemetry/semantic-conventions/issues/2883)
  - How can we document session.id propagation?
  - Should we stamp it in otel instrumentations
  - Liudmila will start a chat with browser sig and ask
- [Aishwarya] ITL in GenAI SemConv for model server metrics [https://github.com/open-telemetry/semantic-conventions/issues/3252](https://github.com/open-telemetry/semantic-conventions/issues/3252)
- [Ankit]: [Built-in Tools Support by singankit · Pull Request #3038 · open-telemetry/semantic-conventions](https://github.com/open-telemetry/semantic-conventions/pull/3038)
