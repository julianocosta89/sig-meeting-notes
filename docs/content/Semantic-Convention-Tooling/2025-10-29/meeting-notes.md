## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Arthur Sens (Grafana Labs)
- Josh Suereth
- Jeremy Blythe
- Liudmila
- Alexandra Konrad (Elastic)

### Agenda
- Triage Project board: [https://github.com/orgs/open-telemetry/projects/84](https://github.com/orgs/open-telemetry/projects/84)
- Weaver Project board: [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
- General Discussion
  - [arthur] Prometheus + Weaver
    - Demo Pain Points
      - JINJA templates - hard due to not knowing jinja
        - These SHOULD be re-usable
        - We may WANT to expose these for folks who want to customize
        - Import remote templates:
          - the parameter -t can take local folders, git repo URL, or Git archive URL.
          - See [https://github.com/open-telemetry/weaver/blob/main/docs/usage.md#registry-generate](https://github.com/open-telemetry/weaver/blob/main/docs/usage.md#registry-generate)
      - Prometheus is huge codebase - want codeowners to own specific schemas
        - e.g. can there be one schema to import sub-schemas?
        - similar to metadata.yaml in collector
        - Example
          - Database
          - Parser
          - Service Discovery
        - What do sub-schemas mean?
        - Is there a common part between components?
        - Semantic-convention style:
          - have a `model/` directory
          - Have a `model/component` directory with codeowners for that component.
      - v2 schema
        - groups:
        - metrics:
  - [suereth] V2 Resolved Schema
    - Attribute Group questions
      - attribute_group:
      - span:
      - struct FooAttributes {
      - Today - attribute groups are JUST to document "loose" attributes that apply to other signals, e.g. code/thread.
    - Template-Resolved-Schema
