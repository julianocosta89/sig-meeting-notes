## Meeting Notes

### Attendees
- Josh
- Liudmila
- Jeremy (second half)

### Agenda
- Release
  - Can cut now and update rust later
  - Jeremy's problem A -> B -> C
    - B & C on the top level too
  - Please review [https://github.com/open-telemetry/weaver/pull/1720](https://github.com/open-telemetry/weaver/pull/1720)
  - Liudmila will cut
- V2 timeline
  - Publishing is the last big piece
    - otel.io design - [Liudmila Molkova](mailto:neskazu@gmail.com)
    - Spec changes - [joshuasuereth@google.com](mailto:joshuasuereth@google.com)
    - Finish semconv migration - [Liudmila Molkova](mailto:neskazu@gmail.com)
    - Publish
  - 0. Start breaking weaver in v1 and v2, duplicate everything - [joshuasuereth@google.com](mailto:joshuasuereth@google.com)
  - 1. Onboard core semconv & publish dev
  - 2. Onboard genai and use published semconv
  - 3. We can make v2 a default then
  - 4. After X (3?) weaver releases / months we can call it stable
  - 5. Things to fix:
    - Live-check is not usable, dependency part
- Concerns:
  - Non-otel people - how long transition period should be
- Add agents.md / claude / gemini [joshuasuereth@google.com](mailto:joshuasuereth@google.com)
  - Skills too
