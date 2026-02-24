## Meeting Notes

### Attendees
- Christophe Kamphaus
- Dotan Horovits (AWS, OpenSearch)
- Alan Clucas (Pipekit)
- Neil Yashinsky (Force Multiplier Labs / [ContextCore](http://contextcore.me/) )

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Project Board: [https://github.com/orgs/open-telemetry/projects/171](https://github.com/orgs/open-telemetry/projects/171)
- [Christophe, 10min] Long Running Spans
  - Which events should contain attributes?
    - Start event
    - End event
      - Attributes replace those from the start event (no merge semantics needed)
  - Heartbeat events don’t need to contain attributes, except for trace/span-IDs
- Go Environment Carrier
  - No update on the PR - but have adopted it into my incomplete work in argo-workflows where it works great.
- Discussed:
  - Otel Unplugged
  - [https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46069](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46069) GenAI processor
  - [https://github.com/open-telemetry/community/blob/main/projects/otel-blueprints.md](https://github.com/open-telemetry/community/blob/main/projects/otel-blueprints.md)
  - [https://github.com/orgs/open-telemetry/projects/181](https://github.com/orgs/open-telemetry/projects/181)
  - [https://opentelemetry.io/blog/2025/otel-weaver/](https://opentelemetry.io/blog/2025/otel-weaver/)
  - [https://github.com/open-telemetry/weaver/](https://github.com/open-telemetry/weaver/)
