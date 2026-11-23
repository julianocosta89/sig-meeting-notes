## Key Topics
- Yash's PR on metrics allocator changes: Francesco explains why the unused allocator parameter should be dropped in Zig, and they agree to close the PR because it exposes a deeper issue with multiple readers on the same meter provider clobbering each other and unbounded memory growth from retaining all data points.
- Architecture direction: move pipeline and view processing into the SDK and keep the API module clean, with a new issue to track multi-reader isolation, possibly assigned to Yash.
- Path to the Zig SDK alpha release targeted for January 2027: remaining work includes spec conformance (currently at 1.48, targeting 1.62), the SAMConf/sampling package, OTLP exporter configuration to-do, and documentation for the OTel website, which needs guidance from the SIG liaisons.
- Yash's onboarding: first meeting, interest in learning the milestone, and Francesco offering mentoring slots on Zig and the SDK.
- Production status: Francesco deployed the first production application using the Zig SDK, exporting traces and metrics (no logs yet), and recently merged gRPC compression support.

## Action Items
- Francesco: Reply on the PR and close it, pending agreement with Yash.
- Francesco: Create a new issue on multi-reader isolation and moving pipeline/view processing into the SDK; assign to Yash if he wants it.
- Francesco: Work on remaining alpha issues, including spec conformance and the SAMConf package.
- Francesco: Send Yash the mentoring booking link via Slack.
- Yash: Add himself to the meeting agenda document and sync with Francesco on Slack about the new issue.
- Maintainers (Giovanni, Juan, Jacob, Emal, Francesco): Consult GC liaisons (Alolita, Josh) on the process for opening the OTel documentation PR.

## Participants
Francesco Gualazzi, Yash Raghubanshi
