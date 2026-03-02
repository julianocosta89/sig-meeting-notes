## Meeting Notes

### Attendees
- Martin Kuba - cannot attend this week
- Hanson Ho (Embrace)
- Joaquin Diaz (Embrace)
- Valentin Pertuisot (Datadog)
- Dan Gomez Blanco (New Relic)
- David Luna (Elastic)
- Maryam Saeidi (Elastic)
- Bee Klimt (Honeycomb)

### Agenda
- Could everyone who is working on an EntityProvider/SessionManager prototype post a link to it on the OTEP?
  - OTEP: [https://github.com/open-telemetry/opentelemetry-specification/pull/4316](https://github.com/open-telemetry/opentelemetry-specification/pull/4316)
  - Prototype in Java: [https://github.com/open-telemetry/opentelemetry-java/pull/7434](https://github.com/open-telemetry/opentelemetry-java/pull/7434)
  - Ted: not spec’d out - how to consume changes from the Entities
  - Jason: hard part is in the code that touches the resource and where it’s being consumed, and making that all consistent and performant
  - Ted: prototype of session manager to test out the consuming case should be done
  - Hanson: should we prototype a couple of Entities to see what the issues could be when we have a complicated consumption/update environment?
  - Ted: there may be issues in the spec that isn’t reversible if it’s out there that changes the interface and not just adds to it
  - Ted: using resources as indexes makes correctness a bit tricky (e.g. all this telemetry is associated with this session which has certain attributes). If it’s just tagging events, maybe not, but for aggregation, would this create a bias?
  - [https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk/trace/src/main/java/io/opentelemetry/sdk/trace/SdkSpan.java#L145](https://github.com/open-telemetry/opentelemetry-java/blob/main/sdk/trace/src/main/java/io/opentelemetry/sdk/trace/SdkSpan.java#L145)
- FYI - Android is planning on releasing v0.12.0 today (finally) [https://github.com/open-telemetry/opentelemetry-android/pull/1048](https://github.com/open-telemetry/opentelemetry-android/pull/1048)
