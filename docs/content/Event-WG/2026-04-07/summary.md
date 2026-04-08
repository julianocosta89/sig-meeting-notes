## Key Topics
- Discussion on the requirement for configuration changes accompanying spec PRs.
- Review of PRs related to unwrapping exceptions and handling span events from logs.
- Concerns regarding dual emitting of events and the need for differentiation between error and non-error span events.
- Proposal for a processor to convert log events into span events, with considerations for user configuration options.
- Ongoing discussions about the stability of the logs API and its implications for merging changes.

## Action Items
- Draft a PR for configuration changes related to spec PRs.
- Follow up on the implementation of the unwrapping process for exceptions.
- Create a separate issue to address concerns about dual pumping of events.
- Explore the possibility of filtering events through a separate processor in the pipeline.

## Participants
Liudmila Molkova, Pellared, Trask Stalnaker
