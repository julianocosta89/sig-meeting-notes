## Meeting Notes

### Attendees
- Christos Markou (Elastic)
- Braydon Kains (Google)
- Donal O’Sullivan (Elastic)
- Pablo Baeyens (Datadog)
- Dmitry Anoshin (Splunk)
- Neil Yashinsky (Force Multiplier Labs / [ContextCore](http://contextcore.me/) )

### Agenda
- Plan for multiple metadata schema configs
  - Cannot emit 2 metrics of the same name.
    - If we emit 2 metrics of the same name with different attributes it may break some backends
  - This may or may not be an issue.
  - Do we need to open an issue against the RFC for dual feature gates to not allow emitting 2 metrics of the same name and different types at the same time. Avoiding double writes.
  - 2 issues
    - Same name different attributes
    - Same name different types
