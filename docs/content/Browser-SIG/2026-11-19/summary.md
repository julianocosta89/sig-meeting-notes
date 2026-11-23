## Key Topics
- **Base URL configuration:** Agreed that Quick Start keeps a single base URL, while the Browser SDK requires exact per-signal URLs. Users can still set a full path if needed.
- **Deprecating duplicate instrumentation packages:** Plan is to add a README notice and a deprecation warning in the constructor, and mark exports as deprecated. Then run `npm deprecate` after a grace period. Full removal from the repo is not planned for this year.
- **Roadmap after consolidation:** Consolidation is nearly complete. Next priorities include semantic convention stability (registry spin-off), SDK improvements, browser compatibility docs, examples in the sandbox, and metric strategy and API surface.
- **Sessions and page context:** Entities for sessions and pages remain an open design question that may require spec work. A sessions working group may be restarted to share an API with other clients such as mobile. Joaquin will lead a discussion on a consolidated definition of "page."

## Action Items
- Martin: Merge the approved server-side stitching PR after the meeting.
- Martin: Tell the PR author to apply the agreed base URL changes.
- Martin: Review the follow-up document PR and the typing/context PR.
- Maxime: Deprecate the duplicate navigation instrumentation in contrib (find or create the issue).
- David: Coordinate the deprecation PRs (add warnings, exports, and README notices), recruit help in the Browser channel, update the roadmap document, and share sessions material next week.
- Joaquin: Open an issue on page use cases and a consolidated page definition.
- Martin: Continue driving semantic convention stability, and pair with David on a sessions prototype.

## Participants
Martin Kuba, Maxime Quentin, Chris Chestnut, Aditya Reddy, Joaquin Diaz, David Luna Bistuer
