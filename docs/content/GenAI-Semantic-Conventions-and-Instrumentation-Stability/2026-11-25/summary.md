## Key Topics
- **CI and review policy:** Workflows on PRs needed approval, so Trask will change the default setting. The group also discussed letting a PR author who is an approver count toward the non-Googler review requirement.
- **Token usage metric for streams:** The group agreed to keep recording token counters at operation end, not per chunk, and to skip error-type attributes for abandoned or mid-stream-crashed streams. In-stream reporting could come later as a chunk-level metric. Service tier is recorded per chunk, and Liudmila will check whether Google GenAI reports it early in the stream.
- **AI review automation:** Trask demoed an experimental review bot that uses GPT and Opus and flags simplifications. He is also tracking human and bot review comments to generate Copilot review instructions, with a draft PR in the conformance repo.
- **Agent name on inference metrics:** Mikolaj's PR adds agent name to inference metrics. The group found that agent name was already allowed to propagate, so the PR was mostly a reference-group addition. They agreed to simplify the wording and remove a redundant note. Rollup discussion is planned for after Thanksgiving.
- **Semconv file organization:** The group discussed using one metric per file, separating auto-generated from handwritten content, and making GitHub reviews easier, possibly by hiding auto-generated files.

## Action Items
- Trask: Change the default workflow approval setting and send a PR to count author-approvers toward the non-Googler review policy.
- Liudmila: Comment on the token usage chunk-metric PR, and check with Google GenAI on when service tier is reported.
- Liudmila: Ping Dio and Aaron to review the OpenAI refinement removal and the other PR needing non-Trask approval.
- Mikolaj: Update the agent name brief, remove the redundant note, and clean up the AI-generated markdown in the agent name PR.
- Group: Discuss token usage rollup at the next meeting after Thanksgiving. Friday's meeting is canceled.

## Participants
Liudmila Molkova, Trask Stalnaker, Matt Spiekerman, Mikolaj Knap
