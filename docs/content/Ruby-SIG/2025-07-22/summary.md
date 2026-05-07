## Key Topics
- Discussion on the stability and refactoring of the trace ID based ratio, with plans to rename it and mark the current version as deprecated.
- Proposal to record exceptions using logs instead of span events, with a request for reviews from languages without exceptions.
- Updates on the Jaeger remote sampling issue, including Goutham's interest in contributing to it and the challenges faced with the current sampling strategy.
- Review of configuration options for the 0 code auto instrumentation PR and alignment with Node.js naming conventions.
- Ongoing issues with the CI system and GitHub Actions, including a persistent test failure and a recent mistake in merging PRs.

## Action Items
- Goutham to document the information regarding rack and span names to assist in tackling the Jaeger remote sampling issue.
- Xuan to create detailed issues for missing features in the OTLP exporter.
- Kayla to follow up on the logger patch PR and address any RuboCop failures.
- Hannah to open a new PR to replace the one that was mistakenly closed.

## Participants
Goutham, Eric Mustin, Kayla Reopelle, Xuan Cao, Hannah Ramadan
