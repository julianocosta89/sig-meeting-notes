## Key Topics
- Discussion on Go instrumentation for TCP and HTTP, including the need for consistent pipelines and handling of large buffers.
- Updates on .NET work regarding header injection and the challenges faced with kernel manipulation.
- Proposal for sharing service metadata through protocols to enhance observability, particularly in non-Kubernetes environments.
- Plans for the next release, including embedding the Java agent and optimizing large buffer handling.
- Considerations for enabling large buffers automatically based on observed traffic patterns.

## Action Items
- Nimrod to create a PR for HTTP instrumentation that ensures consistent processing through the same pipeline.
- Rafael to finalize changes to large buffer settings to be per request rather than per buffer.
- Nikola to prototype metadata sharing between services and evaluate header naming conventions.
- Participants to review and provide feedback on outstanding PRs and issues for the next release.

## Participants
Tyler, Rafael Roquetto, Nikola Grcevski, Nimrod Avni, Giuseppe Ognibene, Mattia Meleleo, Stephen Lang, Florian Lehner
