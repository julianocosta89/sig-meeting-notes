## Key Topics
- Discussion on telemetry emitted from the Supervisor, focusing on logs, metrics, and traces.
- Customer feedback emphasizing the need for more metrics from the Supervisor for better monitoring.
- Proposal for a telemetry payload using the OP Amp connection to streamline data transmission.
- Consideration of long polling HTTP connections for clients unable to use WebSockets.
- Review of ongoing PRs related to connection settings and WebSocket library changes.

## Action Items
- Evan to evaluate the proposed metrics for the Supervisor and contribute to the discussion.
- Andy to draft a proposal for the telemetry payload over OP Amp.
- Michel to explore alternative WebSocket libraries and update PRs accordingly.
- Team to discuss the potential for long polling in the spec and its implications.

## Participants
Michel Laterman, Andy Keller, dpaasman, Evan Bradley
