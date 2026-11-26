## Key Topics
- **Unregistering SDKs for testing:** The OTel Lambda team asked for a way to undo `NodeSDK` start, mainly for tests. Participants agreed the spec shouldn't add an unregister mechanism. Callers can call `.disable()` on the global providers themselves.
- **Migrating OTel Lambda to `startNodeSDK`:** Participants agreed the migration should be straightforward if Lambda doesn't expose SDK options. Past startup slowness that blocked the switch may have improved.
- **Community and SIG logistics:** The OTel Autumn Unplugged event returns next February, with registration open. Meetings will be canceled for the last two weeks of December. A proposal to shorten SIG meetings to 30 minutes was raised for trial, with mixed feedback.
- **Declarative config and `startNodeSDK` docs:** Trent is documenting `startNodeSDK` in the README and linking to API docs rather than type files. A proposed `customizeConfig` option, modeled on the Java implementation, is under review. Participants questioned whether exposing `createSDK` would make it unnecessary. A release is planned after these decisions, likely next week, avoiding Black Friday risk.
- **Browser instrumentation deprecation and PR backlog:** Jared merged a TypeScript deprecation hint for fetch/XHR instrumentations, but delaying npm deprecation until a later major. Many low-value PRs from AI-assisted submissions are piling up, and maintainers are focusing on browser work.

## Action Items
- Marc: Summarize the unregister discussion and post a comment on the OTel Lambda thread.
- Marc: Review Trent's custom component provider PR feedback and look for alternatives to `customizeConfig`.
- Marc: Check the meeting-links spreadsheet for typical meeting durations before revisiting the 30-minute proposal.
- Marc: Plan an OTelJS release next week once declarative config decisions are made.
- Trent: Update the README to link to API docs for `startNodeSDK` options, and make sure the relevant types are exported and included in TypeDoc entry points.
- Trent: Add the `customizeConfig` PR and address Marc's review comments.
- Trent: Review Jackson's pending PR.
- Jared: Post in Slack when a release is imminent so the pending deprecation-hint PR can be expedited (currently blocked on Martin's review).
- Marylia: Add a "no meeting" note to the meeting notes for the last two weeks of December. Share the 30-minute meeting proposal with other SIGs.

## Participants
Marc Pichler, Trent Mick, Jared Freeze, Marylia Gutierrez, Jackson Weber
