## Meeting Notes

### Attendees
- Liudmila (will be 20 mins late)
- Dylan russell (google)
- Jason Loaptecki (Arize)
- Xander Song (Arize)
- Aaron Abbott (Google)
- Tao Chen (Microsoft)
- Shipra Jain (Microsoft)
- Paul Shealy (Microsoft)
- Josh Bonczkowski (New Relic)
- [Sujay Solomon](mailto:sujaysolomon@google.com) (Google)
- Alex Hall (Pydantic)
- Sergey Sergeev (Cisco/Splunk)
- Hardik Surana (Cisco/Splunk)
- Samuel Colvin	(Pydantic)

### Agenda
- Standing topics:
  - Triage
- [Sergey] - Common instrumentation & evaluations SDK
  - support either span-only or span, metrics, events telemetry
    - base python sdk to provide proper genai types: llm, tools, task, workflow, agent, retrieval, embedding
    - standardized implementations for different telemetry
    - [aaron] which vendors don’t like metrics?
      - [sergey] will follow up
      - [aaron] would like to hear the span only point of view. OTel is somewhat opinionated based on different SLOs and sampling requirements between signals
    - [sergey] lets define some LLM types for events and such which can be separate from telemetry
    - Instrumentation library can convert between span attributes (request/response) and separate span + event (request/response)
  - integrates with evaluations sdk (ootb, enabled by an env variable)
    - Doing evals at runtime. You could use the callback mechanism to do the runtime evals
    - pydantic-evals has functionality for
- [[Sujay Solomon](mailto:sujaysolomon@google.com), 5m] Billing units for multimodal
  - Images – billing by image count
  - Audio / Video - billing by seconds
  - Other things that bill differently: number of OpenAI builtin tool calls like web/file search
  - Suggested convention for costs in general, beyond gen AI even: [https://github.com/open-telemetry/semantic-conventions/issues/2312](https://github.com/open-telemetry/semantic-conventions/issues/2312)
- [Shipra Jain, 10 m]: Present proposal for Standardizing Multi-Agentic Tracing
  - Google Doc for review - [https://docs.google.com/document/d/1fcPe3SB_koRNeOoioq28RbA1BC7MNA7-/edit](https://docs.google.com/document/d/1fcPe3SB_koRNeOoioq28RbA1BC7MNA7-/edit)
  - [aaron] could you give open comment permission?
    - [Shipra] Done
- [Liudmila] Project planning
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [https://docs.google.com/document/d/1jLVSlJojWFiVBRDSd9jsySjrV4O98eIMYeG7q_odlLA/edit?usp=sharing](https://docs.google.com/document/d/1jLVSlJojWFiVBRDSd9jsySjrV4O98eIMYeG7q_odlLA/edit?usp=sharing)
