## Meeting Notes

### Attendees
- Nacho Bonafonte
- Bryce Buchanan
- Ben Joseph
- Vishwan Aranha
- Yasura Dodo

### Agenda
- Review Cocoapods [Deprecation Plan](https://docs.google.com/document/d/1Q9ZYnW5jcM57fgZnoZ3wgJ5MxrN-1z64bQGmwtOV_1w/edit?usp=sharing)
  - next deadline: client migration
- Merging Swift-core back into swift main
  - [https://github.com/open-telemetry/opentelemetry-swift/issues/1137](https://github.com/open-telemetry/opentelemetry-swift/issues/1137)
  - Steps to migration:
    - create branch in opentelemetry-swift re-integrating API/SDK
      - priority
    - Create a job that does the release copying (as a PR?) back to swift-core (to a temporary branch for testing initially)
      - exploration needs to be done on the best way to do this
      - This can be done later (lower priority)
    - Target after cocoapods deprecation is completed. ASAP
- GRPC 2.+ upgrade
  - related issue : [https://github.com/open-telemetry/opentelemetry-swift/issues/729](https://github.com/open-telemetry/opentelemetry-swift/issues/729)
  - todo: review minimum supported version [Vinod]
    - additionally, check swift 6 minimum supported version ( for documentation updates)
- Review request: [#1143 - Log OTLP trace export failures](https://github.com/open-telemetry/opentelemetry-swift/pull/1143). Adds diagnostic logging for failures and partial-success responses. ready for maintainer review. [Vishwan]
  - to be merged
- Zoom link updated!
- Review new issues:
  - https://github.com/open-telemetry/opentelemetry-swift/pull/1146
  - https://github.com/open-telemetry/opentelemetry-swift/issues/1147
  - [https://github.com/open-telemetry/opentelemetry-swift-core/pull/99](https://github.com/open-telemetry/opentelemetry-swift-core/pull/99)
- MetricKit instrumentation: crash reports are incorrectly format (Ben to add issue)
