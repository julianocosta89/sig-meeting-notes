## Key Topics
- **Add-on scope:** Add-ons will be limited to non-executable files. Executable add-ons (e.g., JMX) are too close to full agents and will be handled in a broader discussion about supervisors managing multiple agents.
- **Available components and supervisor identity:** Participants debated whether the supervisor should report its own state or identity separately from the collector, and whether available components should carry add-on information. Mikołaj argued the supervisor should be reported as its own entity.
- **Multi-agent support:** Andy outlined two options: proxying OpAMP messages through the supervisor, or treating the group as one compound agent with a single config. Both are deferred to a later discussion.
- **Collector partial reload bug:** Mikołaj described a collector bug where component state machines leak during partial reloads, plus related work on dynamic reload interfaces.
- **Security advisory:** Tyler announced a CVE in the OpAMP Supervisor, fixed in collector v0.165.0. A bug in remote connection settings dropped TLS configuration. Users should upgrade.

## Action Items
- Kelsey to update the supervisor spec to document add-on messages, file location and access, and supervisor behavior, then post it in Slack when ready for review.
- Andy to note that Jessica volunteered Stanley for an approver/reviewer role, pending his return from PTO.
- Tyler to add the CVE advisory link to the meeting notes.
- Andy to return to the Anastasia-related work next week.

## Participants
Evan Bradley, Kelsey Ma, Tyler Helmuth, Andy Keller, Mikołaj Świątek, Jessica Yang
