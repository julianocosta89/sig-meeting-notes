## Key Topics
- Discussion on client-side instrumentation keys and the potential move to a dedicated repository.
- Debate over the use of snake_case vs. camelCase for attribute naming conventions in OpenTelemetry.
- Concerns about the behavior of the SDK regarding enabling instrumentation and the implications for data management.
- Proposal for dynamic configuration of instrumentation to allow enabling/disabling at runtime.
- Consideration of separating instrumentation patching from enabling/disabling functionality.

## Action Items
- Review and potentially approve the PR related to adding instrumentation to the SDK.
- Explore the creation of a new base class for browser instrumentation that could be shared with Node.js.
- Discuss the implications of the current PR on instrumentation behavior and whether it should be merged or postponed.

## Participants
David Luna Bistuer, Trent Mick, Jared Freeze, Joaquin, Maxime
