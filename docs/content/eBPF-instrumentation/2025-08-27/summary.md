## Key Topics
- Discussion on removing the third-party licenses file to streamline contributions.
- Proposal to parallelize CI workflows to reduce integration test times.
- Review of open pull requests, including Kafka integration tests and Prometheus metrics export.
- Addressing flaky tests and tracking issues related to them.
- Exploration of alternatives to BPF loops for context propagation in kernel 5.10 support.

## Action Items
- Tyler to remove the third-party licenses file and create a licenses directory for dependencies.
- Stephen to investigate parallelizing integration tests and report back on findings.
- Mattia to open an issue tracking flaky tests, specifically for JSON RPC and Elixir tests.
- Rafael to provide references for alternatives to BPF loops for context propagation.

## Participants
Tyler Yahn, Stephen Lang, Mike Dame, Rafael Roquetto, Mario Macias, Mattia Meleleo, Nimrod Avni
