## Meeting Notes

### Attendees
      - Dylan russell (google)
      - Marcelo Trylesinski (Pydantic)
      - Aaron Abbott (Google)
      - Keith Decker (Cisco/Splunk)
      - Sergey Sergeev (Cisco Splunk)
      - Riccardo Magliocchetti (Elastic)
      - Ridhima Satam (Cisco/Splunk)
      - Tammy Baylis (SolarWinds)
      - Shuwen Pan (Cisco)
      - Leighton Chen (Microsoft)
      - Joshua Winerman (Cisco/Splunk)
      - Hector Hernandez (Microsoft)

### Agenda
      - Riccardo: log stabilization planning https://github.com/open-telemetry/opentelemetry-python/issues/4750
      - Aaron: add a few @overload variants of the emit method as we have done for tracing wrt context
      - Riccardo: will take a look next week
      - Riccardo: we can start merging PRs for our own instrumentations
      - [Keith] - Updates done to GenAI Utils Inference PR: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768
      - Removed the parent run_id, use OTEL context to manage parent/child relationships on spans
      - Aaron: can you keep this pure without run_id and just add that to the langchain instrumentation?
      - Aaron: PTAL at vertex-ai context manager design
      - Sergey: feel free to get in touch with us if you need clarification
      - Dylan: do we plan to release genai-utils?
      - Aaron: I have one more PR but yes
