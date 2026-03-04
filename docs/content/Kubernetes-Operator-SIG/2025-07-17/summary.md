## Key Topics
- Discussion on breaking changes in HTTP semantic conventions and their impact on instrumentation libraries.
- Proposed strategies for managing version upgrades and user notifications regarding breaking changes.
- Consideration of creating new CRD versions to handle breaking changes while ensuring user awareness.
- Challenges faced by the operator in managing disparate behaviors across different instrumentation libraries.

## Action Items
- Explore the possibility of introducing a new CRD version to handle breaking changes effectively.
- Implement a mechanism to automatically upgrade instrumentation versions for new users while preserving existing configurations.
- Consider adding warnings or status updates in the operator to inform users about potential breaking changes.

## Participants
Mikołaj Świątek, Benedikt Bongartz, Jacob Aronoff, Antoine Toulme, yurioliveirasa
