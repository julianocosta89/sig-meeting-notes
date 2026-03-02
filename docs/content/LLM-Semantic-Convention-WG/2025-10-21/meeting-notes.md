## Meeting Notes

### Attendees
- Aaron Abbott (Google)
- Alex Hall (Pydantic)
- Dylan Russell (google)
- Dat Ngo (Arize)
- Xander Song (Arize)
- Liudmila Molkova (Grafana Labs)
- Bruno Baptista (IBM)
- Michael He (AWS)
- Joshua Winerman (Cisco/Splunk)
- Keith Decker (Cisco/Splunk)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
    - Task/workflow:
      - AI: Liudmila will setup official OTel agents call
      - Start with Mon 9am-9:30 am PT and group can decide if to reschedule it
        - Let’s make sure Dani and IBM folks have a chance to join
  - [everyone, 5 min]  Intro for new members
- Open PRs to review
  - [https://github.com/open-telemetry/semantic-conventions/issues/2907](https://github.com/open-telemetry/semantic-conventions/issues/2907)
    - Retrieval span: lanchain has a higher level retrieval operation
      - Does embedding and search
      - What semantics this span should follow
      - Duplication question also arizes
    - [https://arize.com/docs/ax/observe/tracing/tracing-concepts/openinference-semantic-conventions#document](https://arize.com/docs/ax/observe/tracing/tracing-concepts/openinference-semantic-conventions#document)
    - Next steps:
      - We need some new attributes (top-k, scores, etc) - which namespace they should be in? `search.*` `db.*`
      - Are there 2 spans: retrieval and DB/search
        - Which conventions higher level abstraction span should follow ?
        - Are there other framework that would have abstraction: llama index, haystack do
      - Liudmila will re-review the PR
      - Let's have a demo for langchain retrieval -> embedding + llm
  - [Minghui, 5min] PR Review: schema of tool.definitions: [https://github.com/open-telemetry/semantic-conventions/pull/2942](https://github.com/open-telemetry/semantic-conventions/pull/2942)
    - Capture tool definitions in a simplified format if content capturing is disabled. (just capturing `name` and `type`)
  - [Minghui, 5min] PR Review: Add participant’s name on ChatMessage
  - [Aaron, 5min?] [Add multimodal uri, file, and blob parts to GenAI JSON Schemas #2754](https://github.com/open-telemetry/semantic-conventions/pull/2754)
  - ADDRESSED :) [Josh, 5min] [Retrieval Span Support by JWinermaSplunk · Pull Request #2924 · open-telemetry/semantic-conventions](https://github.com/open-telemetry/semantic-conventions/pull/2924#pullrequestreview-3354593558)
    - Way to move forward here and potentially get genai attributes?
- General discussions
  - [Keith] - Issue for adding workflows/tasks [https://github.com/open-telemetry/semantic-conventions/issues/2912](https://github.com/open-telemetry/semantic-conventions/issues/2912)
    - The goal is to instrument langgraph and groups things?
    - Document framework concepts mapping to workflow / task
