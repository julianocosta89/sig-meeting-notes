## Key Topics
- **Semantic conventions release:** The team plans a release candidate by year end, with a first GenAI semconv release beforehand to practice the release process and fix the OpenTelemetry docs site. Trask will prepare a stabilization update, and the team agreed few further breaking changes are expected.
- **Fetch response usage and token counting:** Summing input tokens across spans risks double-counting, especially with nested inference and async polling. The group leaned toward documenting how to query correctly and holding off on new token metrics for this operation. Async inference instrumentation guidance was flagged for the inference docs.
- **Evaluation results:** Emitting evaluation result events is still favored even when a third-party evaluation system stores results, to keep observability data correlated. Linking back to the source system was raised but not yet specified.
- **Content capture configuration:** Radhika prototyped programmatic setting of content capture mode. Precedence between programmatic config and environment variables differs across languages, so the team will align with each language's existing behavior.
- **Agent identity and credentials:** Victor presented a draft document on agent identity, credential, and skill concepts, drawing on OpenID Foundation and OCSF work. The team wants GenAI agent ID attributes aligned with OCSF. Discussion was deferred to the next meeting.

## Action Items
- Trask: Review the fetch response PR and prepare a semconv release status update for the stabilization meeting.
- Liudmila: Create an issue on async inference instrumentation guidance and check how far the Python GenAI repo is behind the latest semconv version.
- Surya: Open a PR pinning the GenAI util to the latest semconv commit and fix resulting conformance findings, then update the utils for the Workflow span changes.
- Radhika: Confirm the Python and JavaScript precedence behavior for content capture config, finish the prototype for other instrumentations, and ping Slack when ready for review.
- Dylan: Locate the open issue on more granular content capture options.
- Victor: Make the agent identity document commentable and share it for the next meeting.

## Participants
Liudmila Molkova, Tammy Baylis, Pam Dixon, Shuwen Pan, Trask Stalnaker, Josh Bonczkowski, Jamie Danielson, Surya Teja, Aaron Abbott, Radhika Gupta, Dylan Russell, Victor Lu, Don Branson
