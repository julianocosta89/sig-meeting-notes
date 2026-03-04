## Key Topics
- Discussion on the implementation of declarative configuration in OpenTelemetry Java.
- Considerations for whether features should be applied globally or limited to specific components (Starter and Agent).
- Review of existing behavior and potential breaking changes in the instrumentation process.
- Exploration of the need for a declarative configuration bridge and its verbosity.
- Decisions on default settings and how they affect traditional vs. declarative configurations.

## Action Items
- Review comments from Gloria on the PR and resolve outstanding issues.
- Determine if the span processor should be modified for existing configurations.
- Clarify the list of settings that apply to declarative configuration.
- Assess the implications of making certain features globally available versus limited to specific distributions.

## Participants
Gregor Zeitlinger, Prasad Sawool, Jay DeLuca, Trask Stalnaker
