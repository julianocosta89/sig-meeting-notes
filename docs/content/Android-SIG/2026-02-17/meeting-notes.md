## Meeting Notes

### Attendees
- Jason (Splunk)
- Hanson Ho (Embrace)
- Cesar (Elastic)
- Jamie Lynch (Embrace)

### Agenda
- Release this week – probably wednesday Feb 18th.
- How do we want to handle additional customizations in the initializer DSL/API?
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1586](https://github.com/open-telemetry/opentelemetry-android/pull/1586)
  - Java SDK autoconfigure has been stable for more than 2 years
  - It’s a big hammer indeed
    - Maybe we can solve the more specific problems without the big hammer?
  - Incubating/experimental APIs? How might we do this effectively?
  - Should we make a rule that says “no java sdk classes in the agent apis”?
    - Is this not also a problem with the java apis? (eg. SpanProcessor)
    - Do we already have this problem? Probably….
    - Can we  just try and avoid this to make things worse/harder?
  - AI: Jason to reply to issue to recommend using the globalAttributes { } feature to do geo appending
  - AI: Jason to move PR to draft
- [Cesar] Adding crash event to the semantic conventions repo: [https://github.com/open-telemetry/semantic-conventions/pull/3441](https://github.com/open-telemetry/semantic-conventions/pull/3441)
  - device.crash isn’t a good name anymore?
    - device.app.crash being considered
    - app.crash seems the most straightforward
  - Do we need the device namespace at all?
    - Future convo
- [santosh] Metrics guidance in RUM instrumentations - [https://github.com/open-telemetry/opentelemetry-specification/issues/4604](https://github.com/open-telemetry/opentelemetry-specification/issues/4604)
