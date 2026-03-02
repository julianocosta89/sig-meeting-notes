## Meeting Notes

### Attendees
- Liudmila
- Dat Ngo (Arize AI)
- Alex Hall (Pydantic)
- Keith Decker (Cisco/Splunk)
- Xander Song (Arize)
- Josh Winerman (Cisco/Splunk)
- Pavan (Cisco)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
    - Task/workflow:
      - AI: Liudmila will setup official OTel agents call
      - Start with Mon 9am-9:30 am PT and group can decide if to reschedule it
        - Let’s make sure Dani and IBM folks have a chance to join
  - [everyone, 5 min]  Intro for new members
  - KubeCon NA - how's there?
    - GenAI SIG office hours at OTel observatory  on Wed at 3pm[Kubecon NA 2025 OpenTelemetry Observatory Schedule](https://docs.google.com/spreadsheets/d/1Kk6io9V6Q1nluq6H05zGjwvWlXwxh9IwjiThBGJP1Rw/edit?gid=1588415436#gid=1588415436)
- [Liudmila] MCP conventions
  - Mcp.input.param._meta.foo = {}
  - mcp.input.param.foo
- [Josh] Retrieval PR ([https://github.com/open-telemetry/semantic-conventions/pull/2924](https://github.com/open-telemetry/semantic-conventions/pull/2924)) Added a few purposed examples in the PR from trace loop existing instrumentation and our purposed instrumentation. End goal is a retrieval span (type could be genai or db) that wraps a db and embedding child span, has both db and genai attributes, could potentially be enabled/disabled to get rid of additional layer.
