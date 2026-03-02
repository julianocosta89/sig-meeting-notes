## Meeting Notes

### Attendees
      - Aaron Abbott (Google)
      - Dylan russell (google)
      - Riccardo Magliocchetti (Elastic)
      - Sergey Sergeev (Cisco/Splunk)
      - Nagkumar Arkalgud (Microsoft)
      - Keith Decker (Cisco/Splunk)
      - Joshua Winerman (Cisco/Splunk)
      - Hector Hernandez (Microsoft)

### Agenda
      - Riccardo: log stabilization https://github.com/open-telemetry/opentelemetry-python/issues/4750
      - We merged botocore, gen-ai and vertexai instrumentations move from Event API to Logs, missing only openai
      - Merging https://github.com/open-telemetry/opentelemetry-python/pull/4676 will break openllmetry tests if they test against latest
      - We can open an issue on their repo with our plan
      - Sergey: we can ask them to use utils-genai?
      - Leighton: this can be a separate issue
      - Leighton: could use more reviews
      - Nagkumar: OpenAI Agents SDK instrumentation - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3817
      - 2nd PR as discussed the previous week.
      - https://github.com/open-telemetry/semantic-conventions/blob/v1.37.0/docs/gen-ai/gen-ai-agent-spans.md#invoke-agent-span
      - Aaron: take a look at how ADK handles that root span
      - Nagkumar: Langchain agents tracing update to latest spec - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3813
      - Sergey: Rhidima is taking a look at moving this instrumentation to genai utils, you may want to brainstorm together
      - Please join GenAI SIG meetings, Tuesdays at 12PM (https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md it’s out of date, please check official OTel calendar)
      - * Keith - Reminder for GenAI Inference PR Review - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768
      - Aaron; For the context manager see https://github.com/open-telemetry/opentelemetry-python/blob/main/opentelemetry-api/src/opentelemetry/trace/__init__.py#L566
