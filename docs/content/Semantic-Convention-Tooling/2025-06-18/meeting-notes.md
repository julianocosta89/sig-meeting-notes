## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Liudmila Molkova (Microsoft)
- Jeremy Blythe
- Nicolas Takashi (Coralogix)

### Agenda
- Triage Semconv Project board: [https://github.com/orgs/open-telemetry/projects/84](https://github.com/orgs/open-telemetry/projects/84)
- Triage Weaver Project board: [https://github.com/orgs/open-telemetry/projects/74](https://github.com/orgs/open-telemetry/projects/74)
  - Decision on #769, the `imports` section will be more structured. See the last comment in this PR for more details -> [https://github.com/open-telemetry/weaver/pull/769](https://github.com/open-telemetry/weaver/pull/769)
- General Discussion
  - [Nicolas] Tallycat [https://github.com/nicolastakashi/tallycat](https://github.com/nicolastakashi/tallycat)
    - Nicolas described his project Tallycat
      - Registry inference generating a resolved registry output
      - Web UI to search, navigate, and edit the inferred registry
    - Suggested next steps
      - Create a Weaver GH issue to describe how these capabilities could be integrated into Weaver
      - Web UI for Weaver:
        - `weaver registry ui`
        - or `weaver registry browse` ?
      - Registry inference: `weaver registry live-infer`
      - OTEL Collector processor for semconv schema inference
