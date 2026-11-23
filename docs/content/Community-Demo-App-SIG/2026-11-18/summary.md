## Key Topics
- **Bugs in the agent telemetry example:** Som Banerjee reported three small issues. One is a mismatch where the cart service expects session ID but the request sends user ID. Maintainers are short-staffed, so PRs are preferred over issues.
- **Retrieval/RAG extension:** Shenoy Pratik suggested adding a retrieval operation to the existing agent to show retrieval telemetry. The current product search is keyword-only with no embedding store. Both agreed to keep the demo minimal.
- **Oodle backend integration:** Som plans to evaluate Oodle and build a fork of the OTel demo that exports through the OTel Collector. Shenoy recommended working with Oodle to host an official repo and then linking it, rather than adding a new backend upstream.
- **Tsuga bidder/ad auction service proposal:** Antonin Bruneau proposed a fake bidder service that shows observing an uninstrumented external dependency and correlating profiling data with spans for business metrics. Shenoy saw value in the profiling-plus-spans correlation and asked for the value-adds to be documented in the issue, with screenshots and a link to the fork. Other maintainers will weigh in before a decision.

## Action Items
- Som Banerjee: Submit PRs for the three bug fixes within a couple of days and ping the Slack channel.
- Som Banerjee: Submit any further issues as issues or small PRs.
- Som Banerjee: Evaluate the Oodle integration, then contact Oodle about an official repo and submit a PR to update the link.
- Antonin Bruneau: Update the GitHub issue with the three value-adds (external dependency observation, profiling-plus-span correlation, business metrics), plus screenshots and a link to the dashboard in the fork.
- Shenoy Pratik: Review Som's PRs before the next meeting.
- Shenoy Pratik: Review Antonin's issue and fork, and ask the other maintainers and approvers for feedback on the bidder service.

## Participants
Shenoy Pratik, Som Banerjee, Antonin Bruneau (Tsuga)
