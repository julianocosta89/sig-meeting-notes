## Meeting Notes

### Attendees
- Sergey Sergeev (Cisco/Splunk)
- Keith Decker (Cisco/Splunk)
- Josh Bonczkowski (New Relic)
- Alex Hall (Pydantic)
- Michael He (AWS)
- Aaron Abbott (Google)
- Xander Song (Arize)
- Joseph Wang(Roblox)
- Shuwen Pan (Cisco)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- Open PRs to review
  - Please review embedding instr - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3461](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3461)
  - Reasoning part - [https://github.com/open-telemetry/semantic-conventions/pull/2797](https://github.com/open-telemetry/semantic-conventions/pull/2797)
  - Blob / file parts [https://github.com/open-telemetry/semantic-conventions/pull/2754](https://github.com/open-telemetry/semantic-conventions/pull/2754)
  - GenAI Utils Inference PR: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768)
- [sergey, 15m] util-genai update and request for feedback
  - OTel flavors support with Emitters:
    - Messages on span attributes vs events
    - Traceloop instrumentation donation and backward compatibility support
      - We have completion hooks that contain chat history, we can add more input params to the hook. Traceloop / Logfire / etc can leverage them to include not-in-conventions things
      - The hook can take llm-invocation-object
        - All the interesting things (for extensibility) on this object are not-in-conventions yet
      - Can we have a hook / API that's agnostic to instr?
    - 3rd-party vendor extensions (Splunk Evaluation Result support
      - [Ludmila] - Metrics can be configured by setting or not metrics provider
        - Emitter is unconventional, we should not do it for metrics
  - Packaging structure and extensibility
  - Instrumentation-side evaluators support
- [?, Keith] GenAI Utils Inference PR: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768)
  - Please review
- [michael, 5m] pr review request - adding agent span support to langchain instrumentation
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3788](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3788)
  - Liudmila will take a look and try to come up with a good modeling for chains
- [10m] Blob / file parts [https://github.com/open-telemetry/semantic-conventions/pull/2754](https://github.com/open-telemetry/semantic-conventions/pull/2754)
