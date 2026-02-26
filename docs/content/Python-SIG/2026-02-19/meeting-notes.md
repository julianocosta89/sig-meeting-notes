## Meeting Notes

### Attendees
- Ridhima Satam (Cisco/Splunk)
- Mike Goldsmith (Honeycomb)
- Lukas Hering (Capital One)
- Aaron Abbott (Google)
- Keith Decker (Cisco/Splunk)
- Shuning Chen (Cisco/Splunk)
- Tammy Baylis (SolarWinds)
- Josh Winerman (Cisco/Splunk)
- Liudmila Molkova (Grafana Labs)
- Pablo Collins (Cisco/Splunk)

### Agenda
- [Mike] Add stalebot to mark stale PRs then close
  - Java SDK uses a Github action
  - [Aaron + Leighton] in favor, will double check with Riccardo
  - [Liudmila] +1 we use it in core
  - Let’s do something less aggressive than 7
- [Ridhima] - add log and metrics support to langchain
  - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4214
- [Mike] Started on OTel declarative Config, first PR open to introduce generated models from schema - https://github.com/open-telemetry/opentelemetry-python/pull/4879
- [emidio] - -contrib Python 3.14 PR ready to review (added trove classifiers as well) https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4193
- [Shuning] Add Embedding Type and Span Creation to opentelemetry/genai-utils: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4219
- [Josh] Any traction on triagers? (or an extension of what Liudmila brought up last week regarding reviews)
  - [emidio] maybe get some feedback from opentelemetry.io maintainers team since they need to maintain a lot of groups for localization approvers and triagers https://github.com/orgs/open-telemetry/teams?query=docs
  - Also see https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#membership-levels
  - We have a defacto triage board https://github.com/orgs/open-telemetry/projects/88/views/1
  - [Tammy] I can try to be the main triager person, need to check with company
  - [Aaron] What if we do a 5 minute slot at the beginning of the meeting to go over the board. Tammy can run it :)
  - [emidio] implement automated label assigning – eg.,https://github.com/open-telemetry/opentelemetry.io/blob/main/.github/component-label-map.yml – can populate project board based on that
  - [aaron] a couple of people are not approvers but are interested in becoming triagers
- [Liudmila] Looking for eyes on OpenAI v2 https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3715
- [Riccardo - WON’T ATTEND, keep this as last]
  - Downstream IdGenerator implementors PTAL https://github.com/open-telemetry/opentelemetry-python/pull/4854
  - Drafted move of LoggingHandler out of sdk https://github.com/open-telemetry/opentelemetry-python/issues/4330#issuecomment-3914329753 , PTAL
      - JWinermaSplunk ping me on slack please!
- [Surya] Need help with reviews on:
