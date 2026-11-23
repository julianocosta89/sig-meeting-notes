## Key Topics
- Splitting the large mainframe PR (originally 20 changes) into 37 smaller PRs, with PR 47 as the entry point that other PRs depend on.
- Naming: PR 46 proposes "partition" instead of "LPAR" to align with the broader OpenTelemetry ecosystem. Matt proposes changing "Mainframe" to "S390X" for consistency.
- Virtualization: Rüdiger wants VMware-side input from Matt's organization on whether the virtualization model fits.
- Governance and community contacts: a new Slack channel from the governance committee, plus following up with a semantic conventions contact.
- Test infrastructure: requesting an IBM zVDT instance for the OpenTelemetry mainframe project through the TAC, following the pattern the zOTel project used.

## Action Items
- Matt: Review the split PRs, starting with PR 47 and the others Rüdiger flagged, and comment on the naming change (S390X) in PR 54.
- Matt: Ask VMware colleagues to review the virtualization approach.
- Matt: Request a zVDT instance from the TAC for the project.
- Rüdiger: Post comments in the Slack channels (mainframe and the new governance channel) and swap Matt in for Craig on the new channel.
- Rüdiger: Set up the GitHub repo and share access with the team (planned for the next day).

## Participants
Rüdiger Schulze, Matt Hogstrom
