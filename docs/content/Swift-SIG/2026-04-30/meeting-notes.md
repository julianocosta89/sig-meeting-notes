## Meeting Notes

### Attendees
- Nacho Bonafonte
- Bryce Buchanan
- Ari
- Vinod Vydier
- Vladimir Kukushin (Apple)
- Si Beaumont (Apple)
- Moritz
- Alolita (OTel, Apple)

### Agenda
- Release `2.4.1`. It depends on:
  - Released core package, will release main library now once updated
- Rebased SwiftV6 PR - [https://github.com/open-telemetry/opentelemetry-swift/pull/988](https://github.com/open-telemetry/opentelemetry-swift/pull/988)
  - Will fix linux build then ship
- Swift Server Apple folks join for the first time, discussing how we can make the Swift telemetry ecosystem better together.
- Intro of OTel Swift library and what we are focused on
  - Move to Swift 6 ongoing currently
- Vision
  - Method for keeping maintaining context on threads - for active context on threads could be handled with async methods
  - Instrumentation - async methods don’t handle some core iOS issues
  - Apple’s tracing library uses methods which are not necessarily available to 3P client developers
  - Swift metrics and tracing is being added to OTel Swift using structs (PRs in progress)
- Questions
  - What’s the vision for the entry points for OTel SDK
  - SPM pulls in a large dependency tree, Swift traits was tried but doesn’t provide the low footprint expected
  - v13 of iOS, v12 of MacOS - deployment targets are currently supported
  - Is there plan of supporting otel in https://github.com/apple/swift-distributed-tracing ? I see an issue https://github.com/apple/swift-distributed-tracing/issues/115  for otel support..
  - The Package.swift is at tools version 5.9: https://github.com/open-telemetry/opentelemetry-swift/blob/30c1468d385bf4485d93ca12c4b71aaeb9c974a6/Package.swift#L1
  - XCFramework support has been asked for multiple times
- Users
  - Multi-platform developers using many languages
  - Do not want vendor lock-in
  - Want a single pane of glass for observability across client-side, server-side and infrastructure components
  - Use open, standardized instrumentation once, use everywhere
