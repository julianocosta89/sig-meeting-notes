## Meeting Notes

### Attendees
- Aaron Abbott (Google)
- Joshua Winerman (Cisco/Splunk)
- Dat Ngo (Arize)
- Liudmila Molkova (Grafana Labs)
- Keith Decker (Cisco/Splunk)
- Shuwen Pan (Cisco)
- Xander Song (Arize)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- [Liudmila] MCP: [https://github.com/open-telemetry/semantic-conventions/pull/2083](https://github.com/open-telemetry/semantic-conventions/pull/2083)
  - New comment about conflicting HTTP and _meta traceparent e.g.
    - [Alex] if I have both, HTTP propagation makes a mess
    - With MCP propagation overriding the HTTP makes it work much better
  - [Aaron] would be great to have some prototypes
- [Keith] Review for Inference Metrics in GenAI Utils: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891)
- [Josh] Review for retrieval db span semconv:
