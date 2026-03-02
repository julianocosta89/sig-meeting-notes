## Meeting Notes

### Attendees
- Bryce Buchanan
- Arriana Blais
- Alex Cohen
- Nacho Bonafonte

### Agenda
- Continuation of DataCompression discussion
  - [https://github.com/open-telemetry/opentelemetry-swift/pull/838](https://github.com/open-telemetry/opentelemetry-swift/pull/838)
  - Reconfigure PR to depend against: [https://github.com/mw99/DataCompression](https://github.com/mw99/DataCompression)
- Cocoapods still failing
  - fixed
- [Bryce] SemanticAttributes generation (swift 6)
  - update the template to use sendable
  - or try setting issue structs in SemanticAttributes as enums
  - Table swift 6 until swift 6.2 (october)
- [Nacho] Version 2.0
  - remove ‘stable’ from metrics
    - leave typealias for old stable names
  - Release by the 7th of August
- [Nacho] Thread race conditions in some metrics code
