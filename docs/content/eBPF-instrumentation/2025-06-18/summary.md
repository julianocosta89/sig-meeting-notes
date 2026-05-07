## Key Topics
- Status update on migrating the Bela codebase to OpenTelemetry, with significant progress reported.
- Discussion on open pull requests, including updates on MySQL data parsing and service name template.
- Proposal for enhanced configurability in telemetry instrumentation, allowing users to selectively enable traces and metrics.
- Review of dependency updates and suggestions for improving the management of pull requests related to them.
- Addressing a bug related to Go HTTP context propagation that could crash servers.

## Action Items
- Review and clean up open pull requests, particularly those related to MySQL data parsing and service name templates.
- Investigate grouping dependency updates into fewer pull requests to streamline the process.
- Open an issue to track the proposal for configurable telemetry instrumentation options.
- Add defensive coding checks to prevent crashes related to Go HTTP context propagation.

## Participants
Mattia Meleleo, Rafael Roquetto, Tyler Yahn, Nikola Grcevski, Mario Macias, Marc
