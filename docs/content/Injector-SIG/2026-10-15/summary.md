## Key Topics
- Discussion on the need for an image for the Injector to be used by the Operator.
- Proposal to have the Injector or the Packaging SIG handle the creation of the Docker image.
- Agreement on a multi-architecture setup for the Injector image.
- Consideration of two types of Injector images: a lean version for Kubernetes and a more comprehensive version for ECS and Lambda use cases.
- Automation of Docker image publishing linked to Injector version releases.

## Action Items
- Jacob Aronoff to write up the Dockerfile for the Injector image.
- Jack Berg to contribute automation for publishing Docker images in the Packaging repo.
- Antoine Toulme to document decisions and discussions in the relevant issue tracker.

## Participants
Jacob Aronoff, Jack Berg, Antoine Toulme, Michele Mancioppi
