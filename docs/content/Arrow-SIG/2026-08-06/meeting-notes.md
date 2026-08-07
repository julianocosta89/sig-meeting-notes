## Meeting Notes

### Attendees
- Drew Relmas (Microsoft)
- Stephen Lang (Grafana)
- Laurent Querel (F5)
- Jake Dern (F5)
- Utkarsh Umesan Pillai (Microsoft)
- Max Jacinto
- Tom Tan (Microsoft)
- Niamh Gowran (Microsoft)
- Matt Wear (Dash0)
- Josh MacDonald (Microsoft)
- Aaron Marten (Microsoft)
- Kennedy Bushnell (Microsoft)
- Swapnil Ashtekar (Microsoft)

### Agenda
- [Triage]
  - Issues that need to be discussed: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion)
  - Issues that have just been marked as stale: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale)
- [Stephen] Open question - does OTAP support unsigned 64-bit ints?
  - Client SDK support?
  - Potentially an OTel spec-level issue
  - Backends are also a challenge (float64 in Prometheus for example)
- [Kennedy] PR Velocity
  - Investing in an AI PR review process - update rules based on observed recurrent issues in PR reviews.
    - Derive new instrumentation-related rules
  - Incentivize contributors to review PRs
  - Using PR to level up Rust/Project skills
