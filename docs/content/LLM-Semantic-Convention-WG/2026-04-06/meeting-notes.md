## Meeting Notes

### Attendees
- Liudmila Molkova (Grafana Labs)
- Minghui Zhang (Alibaba)
- Huxing Zhang (Alibaba)
- Trask Stalnaker (Microsoft)
- Tiffany

### Agenda
- [Minghui] Need review for gen_ai.tool.defintions [https://github.com/open-telemetry/semantic-conventions/pull/3378](https://github.com/open-telemetry/semantic-conventions/pull/3378)
  - Need approval from trask -> Done
- [Minghui] Involve LoongSuite in conformance test
- [Minghui, 10min] Add semantic conventions for skill
  - Need a prototype
- [Minghui, 5min] Add agent context in existing metrics
  - Invoke_agent agent1
    - Chat model
      - gen_ai.agent.id
  - Tokens
  - Similar to
    - Db spans / metrics by HTTP route
  - Otel prior art: context scoped attributes  [https://github.com/open-telemetry/opentelemetry-specification/pull/4931](https://github.com/open-telemetry/opentelemetry-specification/pull/4931)
  - Implement it in loongsuite-util-genai for preview
- [Minghui, 10min] Add user interaction span [https://github.com/open-telemetry/semantic-conventions/issues/3418](https://github.com/open-telemetry/semantic-conventions/issues/3418)
  - Need a prototype
- [Minghui, 10min] Add ReAct iteration span
  - Need a prototype
