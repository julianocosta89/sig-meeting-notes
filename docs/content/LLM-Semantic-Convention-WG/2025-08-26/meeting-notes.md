## Meeting Notes

### Attendees
- Sergey Sergeev (Cisco/Splunk)
- Shipra Jain (Microsoft)
- Aaron Abbott (Google)
- Liudmila Molkova (Grafana Labs)
- Samuel Colvin (Pydantic)
- Dylan russell (google)
- Josh Bonczkowski (New Relic)
- Eric Han (AWS)
- Shuwen Pan (Cisco)
- Joshua Winerman (Cisco/Splunk)
- Ankit Singhal (Microsoft)
- Xander Song (Arize)
- Austin Born (Shinzo)
- Pradeep Nair (Cisco/Splunk)
- Pavan (Cisco)
- Ranjan (base14)

### Agenda
- Standing topics:
  - Triage
    - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- [Ankit, 15 min] Gen AI Evaluation Result Event
- Review ongoing PR for adding new attributes to invoke_span / execute_tool span for Single and Multi-Agent system - [New attributes in execute-tool and llm span for Single and Multi-Agent traceability by ShipraJain01 · Pull Request #2528 · open-telemetry/semantic-conventions](https://github.com/open-telemetry/semantic-conventions/pull/2528)
- [Sergey, 10m] [Conversation data + eval results event (EXTERNAL)](https://docs.google.com/document/d/1llRzeIi0bMMquTrd-perCzBh_QVqTKNMRngpplpnTes/edit?tab=t.0)
  - Q: Can we add it as an optional event type optimized for backend processing?
  - Q: What is the best way to append evaluated LLM span attributes to the event?
  - Q: multiple-results support format:
    - Option 1 (preferred): "gen_ai.evaluation.<category>.score”: 4
    - Option 2: "gen_ai.evaluation.1.name": "bias", "gen_ai.evaluation.1.score": 4,
- [Dylan and Liudmila] implementing config options [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3709](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3709)
