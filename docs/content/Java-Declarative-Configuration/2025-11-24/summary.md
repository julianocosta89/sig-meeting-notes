## Key Topics
- Discussion on the new instrumentation bridge and its implementation in the OpenTelemetry Java SDK.
- Exploration of using declarative configuration API versus system properties for configuration management.
- Consideration of the impact on library instrumentation and the need to minimize reliance on system properties.
- Review of existing PRs and their alignment with the proposed changes to configuration handling.

## Action Items
- Gregor to check how many library instrumentation cases currently use system properties and assess the impact of changes.
- Trask to ensure that any new usages of configuration in libraries utilize the declarative config API.
- Both to follow up on testing coverage for the new configuration properties.

## Participants
Gregor Zeitlinger, Trask Stalnaker
