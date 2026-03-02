## Meeting Notes

### Attendees
- Aaron Abbott (google)
- Dat Ngo (Arize AI)
- Alex Hall (Pydantic)
- Kip Chelilim
- Liudmila Molkova (Grafana Labs)
- Joshua Winerman (Cisco/Splunk)
- Pradeep Nair (Cisco/Splunk)
- Surya
- Keith Decker (Cisco/Splunk)
- Ankit Singhal (Microsoft)
- Ridhima Satam (Cisco/Splunk)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- [Josh]: Retrieval Span Support PR for review :) [https://github.com/open-telemetry/semantic-conventions/pull/2924#issuecomment-3703227896](https://github.com/open-telemetry/semantic-conventions/pull/2924#issuecomment-3703227896)
- [Surya]: Anthrophic sync messages PR for review
- [Liudmila]: please review trivial PR - marking some of the gen-ai attributes as sampling-relevant (provided at start time)  [https://github.com/open-telemetry/semantic-conventions/pull/2994](https://github.com/open-telemetry/semantic-conventions/pull/2994)
  - Ankit will post findings from the previous discussion
- [Keith] - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3994](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3994)
  - Liudmila to comment that capturing mode should be taken into account
- [Liudmila] GenAI utils trivial PR [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4069](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4069)
- [Liudmila] weaver check
  - Span identity issue [https://github.com/open-telemetry/semantic-conventions/issues/2055](https://github.com/open-telemetry/semantic-conventions/issues/2055)
  - [Aaron] will file an issue capturing how our JSON schemas reduce to Any type because of generic part
