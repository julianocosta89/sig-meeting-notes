## Key Topics
- Discussion on skipping OpenTelemetry version 0.32.0 due to late issue creation and release timing.
- Compatibility concerns regarding OpenTelemetry collector versions and the operator's ability to support a range of versions.
- Introduction of a proposal for adding the host PID field to the collector configuration.
- Exploration of the implications of allowing host PID access for security and usability.
- Consideration of creating a separate custom resource for audit log collection to manage permissions and configurations better.

## Action Items
- Vincent Desbois to provide input on version compatibility and potential milestone for stability in the issue tracker.
- Simon Olander to investigate conflicts in his pull request regarding the host PID field and explore sidecar deployment as a workaround.
- Team to consider updating documentation to clarify compatibility guidelines and sensitive areas that may affect stability.

## Participants
Mikołaj Świątek, Vincent Desbois, Jacob Aronoff, Benedikt Bongartz, Simon Olander, PL Pavol Loffay
