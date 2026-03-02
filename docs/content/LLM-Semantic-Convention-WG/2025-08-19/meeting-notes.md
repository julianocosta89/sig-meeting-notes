## Meeting Notes

### Attendees
- Liudmila Molkova (Grafana Labs)
- Shuwen Pan (Cisco)
- Josh Bonczkowski (New Relic)
- Sergey Sergeev (Cisco/Splunk)
- Pradeep Nair (Cisco/Splunk)
- Trent Mick (Elastic)
- Alex Hall (Pydantic)
- Aaron Abbott (Google)
- Dylan russell (google)
- Eric Han (AWS)
- Michael He (AWS)
- Shipra Jain (MS)
- Xander Song (Arize)
- Ankit Singhal (Microsoft)

### Agenda
- Standing topics:
  - Triage
    - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- [Ankit, 15 min] [Gen AI Evaluation Result Event](https://github.com/open-telemetry/semantic-conventions/pull/2563)
  - [https://github.com/open-telemetry/semantic-conventions/pull/2563#discussion_r2258068645](https://github.com/open-telemetry/semantic-conventions/pull/2563#discussion_r2258068645)
    - Close open comments about evaluation event attributes.
  - Let's start with events and potentially expand to spans separately (based on the past discussion)
  - Score is not  just a number, discussed having `score.number | value` ;
  - We could also add `score.category` in the future (where number doesn't make sense)
- [Liudmila, 5 min] Merge [https://github.com/open-telemetry/semantic-conventions/pull/2179](https://github.com/open-telemetry/semantic-conventions/pull/2179)
  - What's next?
    - Instrumentation update
      - Dylan to follow up on vertex
      - Liudmila to follow up on openai
    - Refs and upload?
      - Aaron is interested
    - Agent input/output?
      - Shipra is addressing it in the PR
    - Built-in tools?
      - [https://github.com/open-telemetry/semantic-conventions/issues/2585](https://github.com/open-telemetry/semantic-conventions/issues/2585)
    - Multi-modal content?
      - Should be straightforward
      - [https://githu	b.com/open-telemetry/semantic-conventions/issues/1556#issuecomment-3144699449](https://github.com/open-telemetry/semantic-conventions/issues/1556#issuecomment-3144699449)
- [Trent, 3min?] Anyone interested in being a codeowner for *JavaScript* instrumentation for OpenAI? [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2941](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2941)
- [Sergey, 5min] Langchain instrumentation - LLM Invocation [opentelemetry-python-contrib/pull/3665](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3665)
- [Liudmila, 5 min] agent chat history - [https://github.com/open-telemetry/semantic-conventions/issues/2632](https://github.com/open-telemetry/semantic-conventions/issues/2632)
  - Liudmila will take a look at A2A and see if chat history applies to it
