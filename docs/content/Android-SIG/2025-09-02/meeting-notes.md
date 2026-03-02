## Meeting Notes

### Attendees
- Jason (Splunk)
- Jamie (Embrace)
- Hanson Ho (Embrace)
- Tyler Benson (ServiceNow)
- Mustafa Haddara (Honeycomb)
- Cesar (Elastic)
- [Gregor Zeitlinger](mailto:gregor.zeitlinger@grafana.com) (Grafana Labs)

### Agenda
- Jason - Holding Activity references and SlowRenderListener
  - [https://github.com/open-telemetry/opentelemetry-android/issues/1192](https://github.com/open-telemetry/opentelemetry-android/issues/1192)
  - We still think it’s a good idea, probably not a great idea
  - Help welcome on this
  - We might be holding references to Activity elsewhere, so if anybody wants to audit or help find these, also a welcome addition
    - Feel free to file an issue with those references.
- [Tyler] Making Disk Buffering contrib more efficient [https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2190](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2190)
  - Current implementation unmarshalles back into objects
  - Then we serialize back to protobufs
  - Can we avoid that de/re serialization step to make things more efficient?
  - Can we do it without needing to read the entire buffer into memory?
    - Using streaming pipe-like
  - Seems like this is a new feature
  - The timing of this optimization is challenging because it’s in the middle of an api change
  - Existing implementation has shortcomings, so we’re trying to make that better for users, better ergonomics and maintainability.
  - SpanStorage might be a good extension interface point
    - Split out / separate the reading and writing interfaces
  - Consider json case – if it’s serialized to json on disk, then reading shouldn’t require deserialization.
  - We conclude that the implementation in [2183](https://github.com/open-telemetry/opentelemetry-java-contrib/pull/2183) helps with usability but limits the extensibility.
    - There is a path forward.
