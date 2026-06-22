## Key Topics
- Discussion on the implementation of a bridge between Prometheus and OpenTelemetry (OTel) SDKs, particularly focusing on the Rust implementation.
- The need for a gatherer interface in the Rust SDK to facilitate metric reading and translation.
- Concerns about the implications of a proposed PR that changes how job and instance attributes are handled when translating between Prometheus and OTel.
- The importance of defining use cases and justifications for changes in the PR to avoid breaking existing functionality.
- The ongoing challenges in stabilizing the OpenTelemetry collector and Prometheus receiver due to dependencies on the evolving specifications.

## Action Items
- Krisztian Fekete to implement the gatherer interface and move REST code to the client model.
- Arve Knudsen to provide feedback on the PR regarding job and instance attributes in Slack.
- Discussion on the round trip with entities to be added to the agenda for the next meeting.

## Participants
Arthur Silva Sens, Krajo Krajcsovits, Jonathan Santos, Krisztian Fekete, Arve Knudsen
