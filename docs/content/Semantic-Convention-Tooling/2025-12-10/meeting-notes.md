## Meeting Notes

### Attendees
- Josh Suereth
- Liudmila
- Jeremy Blythe

### Agenda
- Triage
  - Figured out to-consider for next release.
- [suereth] Release - V2 preview
  - [https://github.com/open-telemetry/weaver/issues/994](https://github.com/open-telemetry/weaver/issues/994)
  - Let's cut the release
    - Denote this is a preview for –v2 and link to the issue for all the commands that should work
    - We'll announce broadly after we have a chance to really dig in with semconv and update docs in main there.
- [suereth] V2 Conversion tool
  - [https://github.com/open-telemetry/weaver/compare/main...jsuereth:weaver:wip-v1-into-v2-tool](https://github.com/open-telemetry/weaver/compare/main...jsuereth:weaver:wip-v1-into-v2-tool)
- [jeremy] Demo?
- [suereth] Attribute Groups
  - Semantic convention "raw" attribute groups
    - cloudevents
    - log-exception aka log.record
    - server
    - client
    - source
    - destination
    - thread
    - profile.frame
    - session-id
    - opentracing
  - Two use cases:
    - "Raw Log-y  things" - "cloudevents", "exception"
    - Things like "thread" etc. where there's context that attaches.
