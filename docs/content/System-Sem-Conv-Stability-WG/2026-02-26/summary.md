## Key Topics
- Discussion on the PR to update process attribute requirements in OpenTelemetry, focusing on making descriptive attributes opt-in.
- Debate on whether to create a separate entity for process executables or keep them as part of the process entity.
- Importance of service name and service instance ID in Prometheus scraping and how it relates to process metrics.
- Concerns about potential conflicts between metrics from the host metrics receiver and those from instrumented processes.

## Action Items
- Donal O'Sullivan to comment on the PR to clarify that the focus is on requirement levels, with a separate follow-up for the executable entity discussion.
- Further exploration of how to handle service name and instance ID for processes in the context of Prometheus scraping.

## Participants
Donal O'Sullivan, Dmitrii Anoshin, Braydon Kains (Google), Christos Markou
