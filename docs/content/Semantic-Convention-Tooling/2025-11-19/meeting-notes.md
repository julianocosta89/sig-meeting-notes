## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Josh Suereth
- Liudmila Molkova
- Jeremy Blythe

### Agenda
- Triage Project board: [https://github.com/orgs/open-telemetry/projects/84](https://github.com/orgs/open-telemetry/projects/84)
  - TODO [suereth] Move all this to weaver board or close.
- Weaver Project board: [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
  - [suereth] Move to renovate?
    - Yes we'll move to renovate.
- General Discussion
  - [suereth] Stability in OTEL discussion
    - [https://opentelemetry.io/blog/2025/stability-proposal-announcement/](https://opentelemetry.io/blog/2025/stability-proposal-announcement/)
    - FEDERATION of semconv
    - Need to ramp-up key deliverables
      - Features
        - V2 Schema ASAP
        - Multi-registry MAY be enough - may need multiple-dependencies
        - Identifying Span in OTLP?
      - Collector/Java need to publish on their own
        - How does this work with extra information beyond semconv
        - Publishing schemas - we need a repeatable way to do this.
      - RECIPES
        - Templates for custom registries
          - Shared across all otel
            - Docgen
            - Policies
          - Shared for each language - if possible
            - Codegen (challenges: governance, security, packaging)
        - CI / CD
          - live check
        - Release Process
          - schema_url generation?
  - [suereth] V2 Schema
    - PR - [https://github.com/open-telemetry/weaver/pull/980](https://github.com/open-telemetry/weaver/pull/980)
    - Next steps - [https://github.com/open-telemetry/weaver/issues/994](https://github.com/open-telemetry/weaver/issues/994)
      - Always provide entire context to JINJA and have JQ be on top of this.
      - Deprecate `weaver search`?
  - [suereth] Custom Policies + Violations
    - [https://github.com/open-telemetry/weaver/pull/1012](https://github.com/open-telemetry/weaver/pull/1012)
