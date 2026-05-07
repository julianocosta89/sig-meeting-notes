## Key Topics
- Review of open PRs, including Kafka integration testing and trace export internal metrics.
- Discussion on enabling internal metrics for trace exporters and potential issues with generating unnecessary spans.
- Updates on fixing Docker RM command and CI issues related to code coverage reports.
- Cardinality limits for span metrics to prevent high cardinality issues in customers with many routes.
- Reminder about KubeCon and the Maintainer Summit for project contributors.

## Action Items
- Rerun integration tests for Kafka 2.8 and 4.0 after syncing with main.
- Nimrod to check on the internal metrics for trace exporters to ensure no unnecessary spans are generated.
- Mario to review Steven's Docker RM PR and ensure it works across environments.
- Team to continue monitoring flaky tests and address issues as they arise.
- Participants to consider attending KubeCon and the Maintainer Summit.

## Participants
Mattia Meleleo, Tyler Yahn, Nikola Grcevski, Mike Dame, Nimrod Avni, MM Mario Macias, Rafael Roquetto, Stephen Lang.
