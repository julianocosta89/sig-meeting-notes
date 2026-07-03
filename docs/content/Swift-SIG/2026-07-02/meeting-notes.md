## Meeting Notes

### Attendees
- Bryce Buchanan
- Robert Magnusson (Grafana Labs)

### Agenda
- Dart/Flutter for OTel
  - [https://github.com/open-telemetry/community/pull/3517/](https://github.com/open-telemetry/community/pull/3517/)
- [Concurrency issue](https://github.com/open-telemetry/opentelemetry-swift-core/issues/53)
  - Still working on this,
- Issues with API types hiding extensions in SDK
  - Review this later
- Review Cocoapods [Deprecation Plan](https://docs.google.com/document/d/1Q9ZYnW5jcM57fgZnoZ3wgJ5MxrN-1z64bQGmwtOV_1w/edit?usp=sharing)
  - release document, blog post?
    - Bryce to publish blogpost
  - Ari to create an issue.
- CodeQL analysis is breaking in opentelemetry-swift
  - Ariel will review
  - concurrency issues [this PR](https://github.com/open-telemetry/opentelemetry-swift-core/pull/87) ought to fix it
- swift-core todo: create an issue for adding feedback-handler to stubbed error message locations
  - also add issue for swift main to add log messages using swift-log
- Review PRs etc
- Otel-core/otel-swift pain points discussion
  - distribute frameworks of sdk & api?
  - duplicate code
