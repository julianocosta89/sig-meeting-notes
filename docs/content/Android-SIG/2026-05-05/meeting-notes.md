## Meeting Notes

### Attendees
- Jason (Splunk)
- Jamie (Embrace)
- Hanson Ho (Embrace)
- Cleverchuk (Solarwinds)

### Agenda
- (jason) - What do we want to call this thing that suppresses instrumentations by name?
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1714](https://github.com/open-telemetry/opentelemetry-android/pull/1714)
  - Does this also work for built-ins (defaults)? Hmmm, I didn’t think about that….
    - It should!
  - Lots of bike shedding, resulting in just keeping “suppressing”
- (jason) - What do we want in the first set of “how do I…” docs? I want to start writing the first few…
  - Ideas:
    - “How can I tell when the session changes?”
    - “How can I add some additional Attributes to the Resource?”
    - “My ingest endpoint requires an auth header to validate incoming requests. How can I add a header to the OTLP exporter?”
    - TLS/encryption customizations (customisations)
    - “How do I set a global attribute that can change over time?”
    - Customizing HTTP client span attributes.
    - Can you inject a span processor yet thru the DSL?
      - We think we don’t have this yet…
    - AI: Jason to create an issue in [opentelemetry.io](http://opentelemetry.io) with this list for checking things off and further discussion.
      - [https://github.com/open-telemetry/opentelemetry.io/issues/9832](https://github.com/open-telemetry/opentelemetry.io/issues/9832)
    - Other ideas please…
- AI: Jason - create issue to move demo app to the otel demo.
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1724](https://github.com/open-telemetry/opentelemetry-android/issues/1724)
- AI: Jason - revert the signed commits thing (I hallucinated it)
  - [https://github.com/open-telemetry/opentelemetry-android/pull/1717](https://github.com/open-telemetry/opentelemetry-android/pull/1717)
  - Revert PR now here: [https://github.com/open-telemetry/opentelemetry-android/pull/1721](https://github.com/open-telemetry/opentelemetry-android/pull/1721)
