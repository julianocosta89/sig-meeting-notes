## Meeting Notes

### Attendees
- Nacho Bonafonte
- Vinod Vydier
- Vishwan Aranha
- Ben Joseph

### Agenda
- Review Cocoapods [Deprecation Plan](https://docs.google.com/document/d/1Q9ZYnW5jcM57fgZnoZ3wgJ5MxrN-1z64bQGmwtOV_1w/edit?usp=sharing)
- Merging Swift-core back into swift main
  - [https://github.com/open-telemetry/opentelemetry-swift/issues/1137](https://github.com/open-telemetry/opentelemetry-swift/issues/1137)
- GRPC 2.+ upgrade
  - now that swift 6 updates have been made can we look at updating the GPRC dependency?
  - related issue : [https://github.com/open-telemetry/opentelemetry-swift/issues/729](https://github.com/open-telemetry/opentelemetry-swift/issues/729)
  - We are open to PRs updating it, what are the minimum ios and macoS version supported?
- Review request: [#1143 - Log OTLP trace export failures](https://github.com/open-telemetry/opentelemetry-swift/pull/1143). Adds diagnostic logging for failures and partial-success responses. ready for maintainer review. [Vishwan]
