## Key Topics
- Discussion on the implementation of a mutable configuration provider and its placement within the repository structure.
- Exploration of whether to integrate an `isMutable` method into the existing config provider or create a separate mutable config provider.
- Consideration of callbacks for configuration updates and their integration with the instrumentation layer.
- Proposal for a policies node in the declarative config to facilitate runtime updates, particularly for components like samplers.

## Action Items
- Jack Shirazi to draft a PR for the core and update the spec regarding the mutable configuration provider and callbacks.
- Further discussions on the structure and implementation of the policies node in the declarative configuration.

## Participants
Gregor Zeitlinger, Jack Shirazi, Trask Stalnaker, Jack Berg
