## Meeting Notes

### Attendees
- John McBride (Paper Compute Co)
- Chris Larsen (Netflix)
- Trask Stalnaker (Microsoft)
- Matt Durham (grafana)
- Dylan russell (google)
- Marisa Boston (Reins AI)
- Mohnish (ReinsAI)
- Liudmila Molkova (Google)
- Keith Decker (Cisco/Splunk)
- Endre Sara (Causely)
- Shubhanshu Surana (Apple)
- Josh Winerman (Cisco/Splunk)
- Alolita Sharma (OTel, Apple)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Imma Valls (Grafana)
- Josh Bonczkowski (New Relic)
- Tammy Baylis (SolarWinds)
- Wolfgang Therrien (Honeycomb)

### Agenda
- [Steve] How to collect identifiers(gen_ai.conversation.id?) and store related fields in multi-turn conversation scenarios, we want to achieve multi-turn conversation evaluation. [https://github.com/open-telemetry/semantic-conventions-genai/issues/356](https://github.com/open-telemetry/semantic-conventions-genai/issues/356)
  - Multi turn conversation == session?
  - This is some scenarios case [https://github.com/open-telemetry/semantic-conventions-genai/blob/main/reference/scenarios/google-adk/scenario.py](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/reference/scenarios/google-adk/scenario.py)
- [Liudmila] Usage metrics [https://github.com/open-telemetry/semantic-conventions-genai/pull/374](https://github.com/open-telemetry/semantic-conventions-genai/pull/374)
- [Liudmila] Don't emit inference scenarios from agentic reference instrumentations [https://github.com/open-telemetry/semantic-conventions-genai/pull/351](https://github.com/open-telemetry/semantic-conventions-genai/pull/351)
- [dylan] Planning to propose a new sem conv for [execution steps](https://ai.google.dev/gemini-api/docs/interactions-overview#how-it-works).
  - Naming: AAIF Taxonomy WG?
    - AI Trask to find links
- [Mohnish & Marisa] [Experimental Result PR](https://github.com/open-telemetry/semantic-conventions-genai/pull/359/) (only if it doesn’t come up in triage)
- FYI: python-genai first release is out
- Triage
