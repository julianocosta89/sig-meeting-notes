## Key Topics
- Discussion on the proposal to enable host metrics collection in Auto Instrumentation, including the potential renaming of the host metrics package to "Instrumentation Host Metrics."
- Agreement on the preference for using OpenTelemetry Collector for host metrics collection rather than language-specific SDKs.
- Debate on whether SDK metrics should be enabled by default or require opt-in configuration, particularly in relation to the declarative config schema.
- Updates on ongoing PRs related to SDK metrics and the need for clearer documentation on configuration options.
- Announcement of progress towards graduation for the OpenTelemetry project.

## Action Items
- Follow up on the host metrics package renaming proposal and update the README to include references to the OpenTelemetry Collector.
- Open an issue in the JavaScript repo to track discussions on SDK metrics configuration.
- Review and provide feedback on open PRs related to log stabilization and SDK metrics.
- Explore the addition of a Boolean option in the declarative config schema for enabling SDK metrics.

## Participants
Trent Mick, Marylia Gutierrez, Marc Pichler (Dynatrace), Daniel Dyla (Dynatrace), Jamie Danielson, Marten Hennoch
