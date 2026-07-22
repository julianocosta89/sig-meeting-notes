## Meeting Notes

### Attendees
- Trask
- Liudmila
- Huxing
- Steve
- John McBride (Paper Compute Co.)
- Ridhima Satam (Cisco/Splunk)
- Ankit Singhal (Microsoft)
- Josh Winerman (Cisco/Splunk)
- Keith Decker (Cisco/Splunk)
- Dat Ngo (Arize AI)
- Shuwen Pan (Cisco)
- Tammy Baylis (SolarWinds)
- Surya Teja
- Alolita Sharma (Apple)
- Aaron Abbott (Google)
- Chris Larsen (Netflix)
- Shubhanshu Surana (Apple)
- Krunal Jain (Apple)
- Jackson Weber (Microsoft)

### Agenda
- [Steve] Multimodal audio and video support
  - [https://github.com/open-telemetry/semantic-conventions-genai/pull/390](https://github.com/open-telemetry/semantic-conventions-genai/pull/390)
- [Steve] What types of spans need to have [gen_ai.conversation.id](http://.conversation.id)
  - Why workflow span does not have conversation id
    - OpenAI Agents ?
    - ADK
      - Has session (aka conversation)
    - Langchain - no conversation ?
    - Crewai - no conversation ?
  - Currently conversation id is used by inference api
    - OpenAI assistants (deprecated)
    - Responses API
    - ?
  - Can only stamp conversation id on your own spans because subagents may have its own conversation id
- [Huxing] Blog post: [https://docs.google.com/document/d/118x75XQsIxI3VjMAVwtcyJ4HJipgP5CqtFAfY5qhCxE/edit?tab=t.0#heading=h.lvj12xmaqyfb](https://docs.google.com/document/d/118x75XQsIxI3VjMAVwtcyJ4HJipgP5CqtFAfY5qhCxE/edit?tab=t.0#heading=h.lvj12xmaqyfb)
  - [https://github.com/trask/semantic-conventions-conformance](https://github.com/trask/semantic-conventions-conformance)
- —-
- [Jackson] Looking for one more reviewer on [gen-ai: add fetch_response operation and span](https://github.com/open-telemetry/semantic-conventions-genai/pull/353)
  - Delete: separate or the same span?
    - Delete has way less info [https://developers.openai.com/api/reference/resources/responses/methods/delete](https://developers.openai.com/api/reference/resources/responses/methods/delete)
- [Mohnish/ Marisa / Glen] Experiments & evals [https://github.com/open-telemetry/semantic-conventions-genai/pull/359](https://github.com/open-telemetry/semantic-conventions-genai/pull/359)
- [Ankit] [Add GenAI voice agent conventions (realtime audio tokens, end reason, cascade STT/TTS) by singankit · Pull Request #390 · open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai/pull/390)
- [Ridhima]
- [Liudmila] previous response id [https://github.com/open-telemetry/semantic-conventions-genai/pull/372](https://github.com/open-telemetry/semantic-conventions-genai/pull/372)
- [Surya]
