## Meeting Notes

### Attendees
- Liudmila Molkova (Microsoft)
- Ankit Singhal (Microsoft)
- Ridhima(Cisco/Splunk)
- Xander Song (Arize)
- Aaron Abbott (Google)
- Hardik Surana (Cisco/Splunk)
- Austin Born (Shinzo)
- Josh Bonczkowski (New Relic)
- Keith Decker (Cisco/Splunk)
- Alex Hall (Pydantic))
- [Sujay Solomon](mailto:sujaysolomon@google.com) (Google)
- Tao Chen (Microsoft)
- Pavan (Cisco)

### Agenda
- Standing topics:
  - Triage
    - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
- [liudmila, 1 min] Updates from APAC call
- [Ankit ,10 mins] [Gen AI Evaluation Result Event](https://github.com/open-telemetry/semantic-conventions/pull/2563)
  - Report alongside gen_ai span like LLM call, agent execution, tool call
  - Intends to record evaluation results
  - How evaluation would be conducted
    - GenAI or eval instrumentation would do it?
  - Why not a root span that parents everything that happens for evals
    - Spans have extra details
    - Eval results should be correlated with GenAI spans that produced evaluated data
    - Evaluator spans and their structure may be internal and intend to stay internal (IP)
    - Alex:
      - An overarching span to evaluate one particular approach across many cases.
      - A child span for each case (one row in a dataset), which contains both performing the task being evaluated and the evaluation of the results.
      - A child span of the above for executing the task. This may have just one child which is an agent run span, but not necessarily.
  - Should it also be a metric?
    - Evals are going lighter/cheaper
    - Metric as well would improve UX
    - It could be incremental change
    - Exemplars to correlate
  - Arize: most evals are computed async, some teams compute evals for all gen ai calls
  - Next steps: how others are doing it ?
    - Arize? - seems to be doing non-otel back-channel to the backend
    - New Relic - Result of eval is an event linked to the span (using NR tracing for now)
- [Liudmila, 15min] Inputs and outputs [https://github.com/open-telemetry/semantic-conventions/pull/2179](https://github.com/open-telemetry/semantic-conventions/pull/2179)
- [Pavan, 3 min] [https://github.com/open-telemetry/semantic-conventions/pull/2551](https://github.com/open-telemetry/semantic-conventions/pull/2551)
- [Keith Decker, 3 min] Weaviate instrumentation PR: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3646](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3646)
