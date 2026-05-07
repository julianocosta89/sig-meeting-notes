## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Antonio Jimenez (ThousandEyes)
- Nikola Grcevski (Grafana)
- Rafael Roquetto (Grafana)
- Nimrod Avni (Coralogix)
- Giuseppe Ognibene (Coralogix)
- Mario Macias (Grafana)
- Stephen Lang (Grafana)
- Marc Tudurí (Grafana)
- Michele Mancioppi (Dash0)
- Mike Dame (Odigos)

### Agenda
- [Nimrod] OBI / eBPF (OBI + profiler) [Collector distribution](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions) while OBI is blocked from contrib
  - [Tyler] OBI is not blocked from contrib, it is blocked from the distribution: [https://github.com/open-telemetry/opentelemetry-collector-releases/pull/1386](https://github.com/open-telemetry/opentelemetry-collector-releases/pull/1386)
  - [Tyler] It is blocked on configuration updates, which are still blocked on review: [https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1351](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1351)
- [Rafael] Harden AI policy (too much noise, low effort, low quality PRs lately)
  - Can we have an agent to enforce the guidelines (both the contributing guidelines and [AGENTS.md](http://AGENTS.md)) and pre-filter noisy PRs?
  - We should consider banning AI generated PR descriptions, comments and perhaps issues.
    - People are responding to genuine human text with AI generated text, including AI plans (which violates our policy)
      - I can ask my own AI agent myself if I want that kind of feedback (because AI feedback can be useful)
  - [Tyler] [https://clawsweeper.bot/](https://clawsweeper.bot/)
- [Tyler] Next release [v0.9.0](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/milestone/11)
- [Nikola] Open PRs review (if we don’t run out of time)
