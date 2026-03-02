## Meeting Notes

### Attendees
- Josh Suereth
- Jeremy Blythe
- Liudmila Molkova (Grafana Labs)

### Agenda
- Triage Project board: [https://github.com/orgs/open-telemetry/projects/84](https://github.com/orgs/open-telemetry/projects/84)
- Weaver Project board: [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
  - First PR - less interesting, easy to fix
  - Second PR - Auth - this is a good first step, but we need to sort out multi-registry.
- General Discussion
  - [suereth] V2 Resolved Schema Design
    - Catalog - Initial Concept
      - Make unique instances of signal descriptions.
      - Can use the same base signal in different contexts, with variations.
      - Want to minimize duplication in delivered artifact.
    - Registry - Used for documentation + conformance checking (live-check)
      - Attributes
      - Attribute Groups
      - Metrics
      - Events
      - Entities
      - Spans
    - Refinements - Used for codegen, references catalog.
      - Metric Refinements
      - Event Refinements
      - Entity Refinements
      - Span Refinements
    - Think about generic vs. specialized
      - SO generating for a specific library - only uses refinements
- [suereth] V2 - Attribute ref and attribute registry
  - Goal: only include "intrinsic" properties of attribute in attribute registry
  - AI - look into setting up a benchmark for resolving semconv registry we can use to look for inefficiencies.
