## Meeting Notes

### Attendees
- Samuel Colvin (Pydantic)
- Alex Hall (Pydantic)
- Ridhima Satam (Cisco/Splunk)
- Paul Shealy (Microsoft)
- Shipra Jain (Microsoft)
- Josh Bonczkowski (New Relic)
- Hardik Surana (Cisco/Splunk)
- Tao Chen (Microsoft)
- Sergey Sergeev (Cisco/Splunk)
- Austin Born (Shinzo)

### Agenda
- Standing topics:
  - Triage
    - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
- Multi-agent update from Cisco and MS
- (Ridhima) Langchain instrumentation - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3600](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3600)
- Attributes and events - ready for review - [https://github.com/open-telemetry/semantic-conventions/pull/2179](https://github.com/open-telemetry/semantic-conventions/pull/2179)
- Project priorities/planning
  - [GenAI project priorities](https://docs.google.com/spreadsheets/d/1aN8ClAisO2gWvobt__DaeJOV3TJbM-oO5logCBSKh-s/edit?gid=0#gid=0)
- LLM pricing database
  - Logfire.cost.amount - single cost of a span
    - Operation.price.amount
  - Logfire.cost.details - cost of tokens
    - operation.price.details
