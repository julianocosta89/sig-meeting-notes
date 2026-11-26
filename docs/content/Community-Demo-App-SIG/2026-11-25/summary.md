## Key Topics
- **Pinned release image pulls:** Som Banerjee reported that Docker Compose pulls `latest` images instead of the pinned release, which can cause drift in forks. Shenoy Pratik noted the Helm/Kubernetes path is the main supported route, and the issue is fine when pulling `main`.
- **Secrets handling in the demo:** Som asked where to store credentials for LLM and backend connections. Shenoy said the demo uses `.env` and `.env.override` for local use, and production deployments should use Docker or Kubernetes secrets.
- **Backlog cleanup and triage:** Matthew Wimpelberg built a project board in his own GitHub account to categorize and trim stale issues. The group agreed to move it into the OpenTelemetry Demo org, add good-first-issue labels, and close outdated items. Creating the new project hit a GitHub 500 error.
- **Onboarding a new contributor:** Srinjoy M, a first-time attendee, plans to open a PR this week. Shenoy pointed him to the board's good-first-issue labels and the Slack channel, and advised opening issues for large features and direct PRs for small fixes.
- **GenAI telemetry gaps:** Shenoy identified missing conversation IDs on agent spans and the lack of evaluation data. He proposed storing evaluation results from the GenAI SIG's data model in OpenSearch and building a Grafana dashboard, and will open a holistic tracking issue.

## Action Items
- Shenoy Pratik: Review Matthew's backlog board, close stale issues, add good-first-issue labels, and check issues older than one year for relevance this week.
- Matthew Wimpelberg: Send a Slack message requesting the board be moved into the OpenTelemetry Demo org; after the cutover, delete his personal project.
- Shenoy Pratik: Create a holistic GenAI telemetry issue covering conversation IDs, evaluation results, and other gaps versus the GenAI semantic conventions.
- Som Banerjee: Work on a fix for the Compose latest-image pull issue once the group agrees on an approach.
- Srinjoy M: Open a first PR this week and join the OpenTelemetry Demo Slack channel.

## Participants
Matthew Wimpelberg, Srinjoy M, Som Banerjee, Shenoy Pratik
