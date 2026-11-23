## Key Topics
- **.NET Standard 2.0 breakage on unsupported runtimes:** A reported issue (Andrew Locke) shows the netstandard2.0 build fails on .NET 9 due to a DiagnosticSource/external init problem. Team agreed the bug sits with the runtime team, will wait for their response, and will keep the netstandard2.0 build as a fallback. The netstandard build is not tested in CI.
- **Large PR review and batching logic:** A large, agent-generated PR adds stateful batch splitting in the exporter. Reviewers found it hard to trace, and Matthew suggested estimating batch sizes up front. Martin will re-review it.
- **Third-party code attribution:** A Kafka instrumentation PR copied code from Aspire (MIT-licensed), raising questions about third-party notices. Martin pushed back and suggested backporting extras upstream. Matthew will check with CNCF Legal and other OTel projects.
- **Semantic conventions and test quality:** Instrumentation semantic conventions are lagging and contain correctness bugs (e.g., WCF activities left unstopped). Agent and Copilot review cycles are inconsistent. Ideas raised include advisory or quarantined tests, a flaky-test dashboard, and a triage skill.
- **Community contribution process:** Discussed making it easier to open issues, possibly using Discussions for early ideas, and revising the issue template with an AI disclosure note.

## Action Items
- Matthew Hensley: Investigate estimating batch sizes to simplify the batching PR, and review it.
- Martin Costello: Re-review the batching PR tomorrow and look for a simpler approach.
- Martin Costello: Keep the netstandard2.0 issue pending the runtime team's response.
- Matthew Hensley: Check with CNCF Legal and other OTel projects on third-party notice handling.
- Matthew Hensley: Consider adding advisory or skipped tests and a flaky-test tracking list.
- Martin Costello: Consider writing a skill for semantic convention upgrades and a triage skill for flaky tests.
- Team: Review the issue template and consider adding guidance on AI disclosure.

## Participants
Matthew Hensley, Martin Costello, Sean Li
