## Key Topics
- Proposal to remove the Traceos metric from OpenTelemetry codebase due to its Grafana-specific nature.
- Discussion on improving CI efficiency by merging integration tests into a single Docker image.
- Consideration of enabling large buffers by default in OpenTelemetry to improve data parsing and trace accuracy.
- Update on the status of various bugs and features ahead of the V1 release, including duplicate trace IDs and telemetry contract definitions.
- Exploration of adding dynamic manual spans through configuration without modifying application code.

## Action Items
- Mario Macias to submit a PR for removing the Traceos metric by tomorrow.
- Nikola Grcevski to create an issue for enabling large buffers by default and align it with the current milestone.
- Tyler Yahn to assist Nimrod Avni with the telemetry.md documentation and review.
- Nikola Grcevski to track the dynamic manual spans feature for future development.

## Participants
Tyler Yahn, Nikola Grcevski, Mario Macias, Nimrod Avni, Giuseppe Ognibene, Matt, Mike Dame
