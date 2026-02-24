## Meeting Notes

### Attendees
- Sergey Sergeev (Cisco/Splunk)
- Keith Decker (Cisco/Splunk)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Josh Winerman (Cisco/Splunk)
- Shuwen Pan (Cisco)
- Pradeep Nair (Cisco/Splunk)
- Victor Lu (Independent)
- Anirudha Jadhav “Ani” ( Opensearch-Project , AWS )
- Ridhima Satam (Cisco/Splunk)

### Agenda
- (Surya) boilerplate for Claude agent SDK [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4179](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4179)
  - Need reviews for the PR
  - Anirudha is reviewing it
- (Surya) create_agent vs invoke_agent
  - related to anthropic sdk
    - create subagent - when the AI agent starts or when an agent dynamically created
    - [https://platform.claude.com/docs/en/agent-sdk/subagents](https://platform.claude.com/docs/en/agent-sdk/subagents)
    - [https://platform.claude.com/docs/en/agent-sdk/subagents#programmatic-definition-recommended](https://platform.claude.com/docs/en/agent-sdk/subagents#programmatic-definition-recommended)
- (Victor) [Blog - Why Dataops - mldevsecagentops](https://docs.google.com/document/d/11rG9YHM6K9lSTVwCBE3iPUoGxYfxMlh2NsUlwdQzbCA/edit?tab=t.0#heading=h.dmn51ngr7jm1)   It is a BOF discussion about "dataops events" [https://cd.foundation/blog/2026/02/02/mldevsecagentops-discussion/](https://cd.foundation/blog/2026/02/02/mldevsecagentops-discussion/)
  - CI/CD events may be best defined in [https://opentelemetry.io/docs/specs/semconv/registry/attributes/cicd/](https://opentelemetry.io/docs/specs/semconv/registry/attributes/cicd/)
  - we can potentially define new conversation message type to support it, if needed
