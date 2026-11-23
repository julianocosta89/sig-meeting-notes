## Key Topics
- **Version 3.0 pre-release plan:** Semantic conventions are updated and the traces package is merged into the unified repo, removing the separate OpenTelemetry Swift Core dependency. A pre-release is planned for next week, with a go/no-go decision for a final release on December 1.
- **Optional traces package:** This package reduces dependency overhead for users, and the team agreed it's needed for 3.0.
- **Launch instrumentation (Billy Zhou):** The PR will land as experimental for 3.0 to gather feedback. Billy still needs cleanup, device testing, and a TestFlight build, plus an Apple ticket for approach clarity.
- **Pull request backlog:** Seven PRs remain open. Several are approved and ready to merge, while others need CLA fixes, conflict resolution, or review. The MetricKit updates for iOS 27 need reviewers.
- **Issue triage:** The missing documentation issue is low priority and shouldn't block 3.0. Vishwan suggested adding priority labels.

## Action Items
- Nacho Bonafonte: Create and publish the 3.0 pre-release next week, and join the meeting during the US Thanksgiving break.
- Vishwan Aranha: Check the open Xcode local development PR, answer the outstanding question, and push updates if needed.
- Vishwan Aranha: Look into adding priority labels for issues.
- Billy Zhou: Clean up the launch instrumentation PR, run device testing and a TestFlight build on an iPhone 16, and open the Apple ticket with Vladimir.
- Nacho Bonafonte: Ping the PR author who hasn't signed the CLA, and follow up with Vladimir on his CLA and commit cleanup.
- Marius Ciocanel: Look at the missing documentation issue if time allows (low priority).
- All: Test the 3.0 pre-release in your projects and review the MetricKit PRs.

## Participants
Ben Joseph, Marius Ciocanel, Vishwan Aranha, Vladimir Kukushkin (Apple), Nacho Bonafonte, Vinod Vydier, Billy Zhou
