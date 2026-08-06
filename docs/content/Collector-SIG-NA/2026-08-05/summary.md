## Key Topics
- Discussion on the Kubernetes attributes PR and its importance for the 1.0 release.
- Proposal for a configuration file for mDataGen to manage linting and code coverage targets.
- Review of PRs related to the Export Helper and shutdown behavior in the retry sender.
- Concerns about data loss during shutdown and the handling of persistent queues.

## Action Items
- Participants to review the PR for the mDataGen configuration file and provide feedback.
- Blake Rouse to investigate the shutdown behavior of the Export Helper and confirm if it flushes the persistent queue on shutdown.
- Jade Guiton to review Blake's PR and provide insights on the handling of the persistent queue.

## Participants
Pablo Baeyens, Evan Bradley, Tyler Helmuth, Jade Guiton, Ravishankar Gnanaprakasam, Blake Rouse
