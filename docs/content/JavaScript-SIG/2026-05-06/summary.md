## Key Topics
- **Security Advisory on Prometheus Exporter**: Discussion on a vulnerability related to malformed HTTP requests and the importance of updating to patched versions.
- **Threat Model Definition**: Proposal to define a threat model to clarify what constitutes a vulnerability and the responsibilities of users versus the project.
- **Synchronous Hooks Support**: Discussion on the need for support of synchronous hooks in instrumentation, especially with the deprecation of older APIs.
- **Orchestrian Integration**: Consideration of integrating Orchestrian for new instrumentations while maintaining support for existing ones.
- **Default Settings for New APIs**: Debate on enabling new APIs by default to ease user experience, especially for ESM applications.

## Action Items
- Participants to review and provide feedback on the draft threat model PR.
- Raphaël Thériault to explore adding support for synchronous hooks in the import-in-the-middle library and open a PR.
- Daniel Dyla to consider the implications of trusted export destinations in the context of security vulnerabilities.

## Participants
Marc Pichler, Raphaël Thériault, Trent Mick, Daniel Dyla, David Luna Bistuer
