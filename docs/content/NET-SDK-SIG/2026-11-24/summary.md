## Key Topics
- **Hangfire/batch-processing instrumentation PRs:** Several open contrib PRs add Hangfire instrumentation without semantic conventions, which don't exist for this domain. A linked convention proposal is stale and was rejected for lack of a sponsoring SIG. Alan suggested directing contributors to the semantic conventions process, while Matt noted that messaging conventions have stalled since June 2024.
- **Precedent for unstable conventions:** The team debated whether to follow the Ruby or Java approach. Alan considers Java the stronger precedent given its community involvement. They agreed contributors should gather evidence of community interest and groundwork before proceeding.
- **Kafka messaging instrumentation:** A new contributor is aligning Kafka instrumentation with the Java messaging conventions. Microsoft has vendored similar Kafka instrumentation, e.g., in .NET Aspire. Matt will tell the contributor that upstream conventions work is needed.
- **Security scan findings:** Anthropic security scan results were reviewed. Matt estimates about 10% are actionable, with none urgent. Some optimizations were identified.
- **OTel Unplugged conference:** The event returns February 1 in Brussels. Matt reports strong end-user interest from KubeCon and has printed promotional materials. Alan is undecided on attending.

## Action Items
- Matt Hensley: Reply to the Hangfire PR contributors, asking them to gather evidence of community interest and to consider upstreaming through semantic conventions.
- Matt Hensley: Inform the Kafka contributor that upstream semantic conventions work is needed.
- Matt Hensley: Review the two newly opened PRs waiting for reviewers this afternoon.
- Alan West: Research other SIGs' prior attempts at Hangfire/batch-processing conventions and gather input from Peter and Raj before any decision.
- Matt Hensley: Continue promoting OTel Unplugged to the group.
- Alan West: Confirm whether he will attend OTel Unplugged.

## Participants
Alan West, Matthew Hensley, Sean Li
