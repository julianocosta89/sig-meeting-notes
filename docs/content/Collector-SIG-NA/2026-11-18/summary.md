## Key Topics
- **Stability phase one progress:** Transform processor is expected to be marked stable as early as December. Filter processor is next, with public config and API cleanup. Feature gates work for a component is in progress (Christos). A Prometheus-related item needs discussion with another SIG. Resource detection processor and file log receiver need more code owners.
- **File log receiver and stanza for 1.0:** The team agreed to stabilize the existing stanza operators as they are. Replacing stanza with OTTL is a post-1.0 effort, since stanza uses its own internal format and pipeline. The file log receiver cannot reach 1.0 without stanza reaching 1.0.
- **RFC on opt-in unstable components:** Jade presented a core RFC proposing a release channel that controls which component stability levels and beta feature gates are enabled by default.
- **Diff CLI proposal (Emilia Ferreyra, New Relic):** A `diff` subcommand, previously a proof of concept, shows the semantic change a processor config makes to a payload without running a full Collector. Maintainers debated whether it should be a subcommand of the OTel Collector binary or a separate binary, with security concerns favoring the latter.
- **Network listener and dialer extension:** Antoine presented an open PR for a listener extension that mirrors the dialer middleware, and a demo extension that binds outbound connections to a specific network interface. Future placement (possibly contrib) is still undecided.

## Action Items
- Assign Christos to the feature gates work for the component in progress (Antoine/Tyler).
- Tyler to create the transform processor stability tracking issue this week and start on the filter processor afterward.
- Find code owners for the file log receiver and resource detection processor.
- Braydon and Andrzej to drive file log receiver stabilization.
- Jade to announce the opt-in RFC in the Collector Dev channel and gather feedback.
- Emilia to gather feedback on the diff proposal in the core issue, including whether it should be a separate binary.
- Maintainers to review the network listener extension PR.
- Blake to get reviews on the partial reload Phase 2 (processors) PR.
- Braydon to look into whether the dialer approach works for a custom gRPC client connection.

## Participants
Ervin Wallin, Paulo Janotti, Antoine Toulme, Andrzej Stencel, Evan Bradley, Pablo Baeyens, Tyler Helmuth, Braydon Kains, Jade Guiton, Emilia Ferreyra, Kells Kearney, Blake Rouse
