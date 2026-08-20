## Meeting Notes

### Attendees
- Jeremy
- Josh
- Laurent

### Agenda
- [josh] What we want for next release
  - Ok to start doing faster releases
  - Will fix nightly + entity ref final bug fixes before cutting one this week
- [josh] Conformance / Next live-check
  - [https://github.com/open-telemetry/semantic-conventions-conformance](https://github.com/open-telemetry/semantic-conventions-conformance)
  - Concerns from Spec meeting
    - Live check explores large amounts of semconv - leading to lots of warnings/errors from too much data when doing compliance testing for an instrumentation
    - Ensuring schema_url is the thing you validate.
  - Discussions from slack
    - In V2 - going to be more precise in matching, locked down.
    - What do we do for folks who want broad/loose sense?
  - Need to write up matching rules - and then start working on it.
