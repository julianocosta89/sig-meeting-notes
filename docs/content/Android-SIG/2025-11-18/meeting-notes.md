## Meeting Notes

### Attendees
- Hanson Ho (Embrace)
- Jamie Lynch (Embrace)
- Mustafa Haddara (Honeycomb)
- Bee Klimt (Honeycomb)
- Cesar (Elastic)
- Jairo (Honeycomb)

### Agenda
- [Hanson] Plan for getting to stable
  - The plan is to release an rc.1 this week, as we had hoped to do last month
  - With a real non-rc 1.x.0 stable release following within a month or two or ? (depending on feedback/issues)
  - Documentation and examples are still needed
  - Example of how to disable instrumentation would also help here
- [Cesar] Users using builder from core
  - Also users are using java perhaps way more than expected
  - Related: [https://github.com/open-telemetry/opentelemetry-android/pull/1387](https://github.com/open-telemetry/opentelemetry-android/pull/1387)
  - AI: Hanson to file an issue about explaining our rationale around kotlin-first (we don’t have this yet do we?)
  - Candidate to add to the decision explaining doc: [https://github.com/open-telemetry/opentelemetry-android/pull/1373#discussion_r2513482547](https://github.com/open-telemetry/opentelemetry-android/pull/1373#discussion_r2513482547)
- [Cesar] - Taking some time off - back in January (December off, starting Friday)
  - We don’t need to stabilize disk buffering
- Next week Thursday is Thanksgiving in the US.
  - We will still meet next week on Tuesday.
- What is our formal triaging process?
  - Applying “Bug” and other basic labels, also removing Bug when it’s not a bug
  - Should we have a “triaged” or “triaged:accepted” or similar  label to indicate that someone has looked at it?
