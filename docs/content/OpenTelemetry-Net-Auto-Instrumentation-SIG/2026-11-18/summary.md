## Key Topics
- **.NET 11 support is ready for release:** The team agreed no blockers remain for publishing a new package with .NET 11 support, including the runtime async support fix. Zach will review and merge the pending PR first.
- **Runtime async limitation (hardening, not urgent):** The instrumentation's end-method handler cannot run async code paths when the library is compiled as runtime async. This is not blocking because no current handlers use async/await, but it will need addressing eventually.
- **Open PRs and issues:** Matthew's PR has addressed feedback, with two comments deferred to follow-ups. The IBM MQ PR was judged too broad and will be split into a generic infrastructure PR plus IBM-specific work. Kafka and IBM MQ items remain in the backlog, and a new .NET Framework support issue is being tracked.
- **Maintainer update:** A new direct channel to the OTel GC liaison is available for escalating issues to OTel leadership.

## Action Items
- Zach Montoya: Review and merge the pending PR, then cut the .NET 11 release.
- Zach Montoya: Create a new issue for the IBM MQ generic infrastructure work and keep the IBM-specific work separate.
- eftiquar: Create a follow-up issue for the profile capture PR review feedback.
- Matthew Hensley: Track the two deferred review comments as follow-up work.
- Team: Close the .NET 11 tracking issue once the release is published and declare latest .NET support.

## Participants
eftiquar, Alexey Pukhov, Rhynier Myburgh, Matthew Hensley, Zach Montoya
