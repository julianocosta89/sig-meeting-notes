## Meeting Notes

### Attendees
- Trask Stalnaker (Microsoft)
- Ridhima Satam (Cisco/Splunk)
- Aaron Abbott (Google)
- Josh Winerman (Cisco/Splunk)
- Josh Bonczkowski (New Relic)
- Nagkumar Arkalgud (Microsoft)
- Ankit Singhal (Microsoft)
- Habiba Mohamed (Microsoft)
- Surya Teja
- Dat (Arize AI)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Nikhil Pallepati
- Shuwen Pan (Cisco)
- Leighton Chen (Microsoft)
- Mike Goldsmith (Honeycomb)
- Jamie Danielson (Honeycomb)

### Agenda
- OpenInference donation proposal
  - [https://github.com/open-telemetry/community/issues/3467](https://github.com/open-telemetry/community/issues/3467)
  - [https://docs.google.com/document/d/1gDEkuw7HXg_0H9Q3z85jKV3H_GeTSIWeURn-9N2q0Ok/edit?tab=t.0](https://docs.google.com/document/d/1gDEkuw7HXg_0H9Q3z85jKV3H_GeTSIWeURn-9N2q0Ok/edit?tab=t.0)
- [Liudmila] Metric & naming [https://github.com/open-telemetry/semantic-conventions-genai/issues/249](https://github.com/open-telemetry/semantic-conventions-genai/issues/249)
- [Liudmila] [agent.id](https://github.com/open-telemetry/semantic-conventions-genai/pull/242)
  - static / stable id
  - remove from internal spans (local agents)
  - What should we do when recording acting agent along with target agent [https://github.com/open-telemetry/semantic-conventions-genai/issues/243](https://github.com/open-telemetry/semantic-conventions-genai/issues/243)
  - [aaron] draft “Agent entity” for specifying resource attributes [https://github.com/open-telemetry/semantic-conventions-genai/pull/270](https://github.com/open-telemetry/semantic-conventions-genai/pull/270)
- [Ankit] [Agent Invocation Id](https://github.com/open-telemetry/semantic-conventions-genai/pull/250)
  - Agent Invocation identifier similar to gen_ai[.response.id](http://.response.id)
- [Ankit] [Invoke Agent Server Span](https://github.com/open-telemetry/semantic-conventions-genai/pull/252)
  - Invoke Agent Span for Server for E2E tracing.
  - Ported from [PR](https://github.com/open-telemetry/semantic-conventions/pull/3473) in old Repo
- [dylan] Removal of old “stable” GenAi instrumentation code..
  - Code is being removed from all the instrumentations.
  - Trask updated docs to remove [the big warning in the docs](https://opentelemetry.io/docs/specs/semconv/gen-ai/).. Do we want to mark any of the spans / events / metrics as “stable” ?
  - When do we plan to do a release?
- [Surya] How are we thinking about agent security? There is an open issue and Nagkumar had a pr. Here is another pr [https://github.com/open-telemetry/semantic-conventions-genai/pull/165](https://github.com/open-telemetry/semantic-conventions-genai/pull/165) from someone who maintains an open-source agent security framework.
- [https://github.com/open-telemetry/semantic-conventions-genai/pull/262](https://github.com/open-telemetry/semantic-conventions-genai/pull/262) apply guardrail is now run guardrail
- Had a convo with google, cisco. need to finalize the discussion around target - flat structure vs nested
- [Nikhil] Unblock follow-up work for agent finish reason issue #[171](https://github.com/open-telemetry/semantic-conventions-genai/issues/171)
