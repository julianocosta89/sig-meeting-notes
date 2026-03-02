## Meeting Notes

### Attendees
- ~~Liudmila~~
- Aaron Abbott (Google)
- Keith Decker (Cisco/Splunk)
- Dat Ngo (Arize AI)
- Josh Winerman (Cisco/Splunk)
- Josh Bonczkowski (New Relic)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- [Liudmila]  Added agent call to the calendar and community repo - [https://github.com/open-telemetry/community/pull/3167](https://github.com/open-telemetry/community/pull/3167). Please make sure to use this document to capture notes
- [Liudmila] MCP: [https://github.com/open-telemetry/semantic-conventions/pull/2083](https://github.com/open-telemetry/semantic-conventions/pull/2083)
  - New comment about conflicting HTTP and _meta traceparent e.g.
    - [Alex] if I have both, HTTP propagation makes a mess
    - With MCP propagation overriding the HTTP makes it work much better
  - [Aaron] would be great to have some prototypes
- [Keith] Review for Inference Metrics in GenAI Utils: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3891)
- [Josh] Review for retrieval db span semconv:
