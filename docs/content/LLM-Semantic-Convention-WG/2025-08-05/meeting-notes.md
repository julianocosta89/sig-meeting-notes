## Meeting Notes

### Attendees
- Liudmila (will be ~30 min late)
- [Samuel Colvin](mailto:s@muelcolvin.com) (Pydantic)
- Alex Hall (Pydantic)
- Dat Ngo (Arize)
- Aaron Abbott (Google)
- Josh Bonczkowski (New Relic)
- Ridhima Satam (Cisco/Splunk)
- Sergey Sergeev (Cisco/Splunk)
- Michael He (AWS)
- Eric Han (AWS)
- Ankit Singhal (Microsoft)
- Guangya Liu (IBM)
- Austin Born (Shinzo)
- Keith Decker (Cisco/Splunk)
- Xander Song (Arize)

### Agenda
- Standing topics:
  - Triage
    - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
- [Samuel, 5mins 🤞] [https://github.com/open-telemetry/semantic-conventions/issues/1959](https://github.com/open-telemetry/semantic-conventions/issues/1959)
  - Samuel went through LLMs and this works for almost all models
- [Ankit ,10 mins] [Gen AI Evaluation Result Event](https://github.com/open-telemetry/semantic-conventions/pull/2563)
  - [Samuel] would there be one span per each type of eval?
  - [Ankit] Ya that’s the idea
- [Liudmila, 15 min, please postpone to the second half of the call] Remaining discussions on chat history:
  - Keeping json schema simple - [https://github.com/open-telemetry/semantic-conventions/pull/2179/files#r2195115802](https://github.com/open-telemetry/semantic-conventions/pull/2179/files#r2195115802)
  - Built-in tool call example [https://github.com/open-telemetry/semantic-conventions/pull/2179#discussion_r2243144052](https://github.com/open-telemetry/semantic-conventions/pull/2179#discussion_r2243144052)
  - Ready to go otherwise
  - [Alex] [https://github.com/open-telemetry/semantic-conventions/issues/2585](https://github.com/open-telemetry/semantic-conventions/issues/2585)
  - [Alex] [https://github.com/open-telemetry/semantic-conventions/issues/2584](https://github.com/open-telemetry/semantic-conventions/issues/2584)
- [Ridhima 2mins] - please review PR for langchain instrumentation adding span support for llm invocation - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3665](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3665)
- [Aaron, 2m] any updates on the GenAI Util library?
  - [Keith] - see structure PR here: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3672](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3672)
