## Key Topics
- Review of PRs: Discussion on the status of various pull requests (PRs) and the need for improved workflows to manage closed PRs.
- API Behavior Changes: Addressed issues related to changes in behavior after the last release, particularly with the Tracer and memory consumption concerns.
- Metric Reader Implementation: Debate on whether to log warnings or raise exceptions when adding/removing metric readers that already exist or do not exist.
- Memory Leak Concerns: Discussion on reported memory leaks and the potential need for caching mechanisms to optimize memory usage.

## Action Items
- Mike Goldsmith to implement automation for managing PR statuses in the workflow.
- Further investigation into the memory consumption issues and potential caching solutions for the Tracer, Logger, and Meter APIs.

## Participants
Riccardo Magliocchetti, Tammy Baylis, Paulo Vital, Keith Decker, Aaron Abbott, Mike Goldsmith, Yazdankhah Mani
