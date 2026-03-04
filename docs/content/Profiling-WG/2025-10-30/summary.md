## Key Topics
- Discussion on identifying executables in OpenTelemetry profiling using build IDs versus executable names.
- Proposal to use a custom hashing scheme for unique identification of executables.
- The relationship between build IDs and resource attributes, particularly in containerized environments.
- Considerations for grouping resources based on build ID and additional metadata.

## Action Items
- Develop a proposal to model executables with a unique ID based on a custom hashing scheme.
- Ensure the algorithm for generating build IDs is shared across all signals for correlation purposes.
- Clarify how multiple entities can participate in a resource, particularly in relation to container metadata.

## Participants
Josh Suereth, Felix Geisendörfer, Braden (Fraggle Rock), Christos Kalkanis
