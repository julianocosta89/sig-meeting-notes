## Key Topics
- Discussion on declarative configuration stability guarantees for the OpenTelemetry collector and Prometheus exporter.
- Introduction of a new config provider based on environment variables, aiming for consistency across configuration methods.
- Proposal for dynamic configuration of authentication headers for exporters, particularly for GCP.
- Ongoing tracking of language implementations and stabilization of declarative configuration.
- Need for a clear mapping of environment variables to configuration schema in semantic conventions.

## Action Items
- Gregor to find and tag the existing issue related to the authenticator proposal in the specification repository.
- Tyler to check the related spec issue and discuss the concept of authenticators in the next spec meeting.
- Marylia to continue developing the config provider and share updates on its progress.
- Gregor to add the new environment variable settings to the semantic conventions issue.

## Participants
Gregor Zeitlinger, Tyler Yahn, Alex Boten, Marylia Gutierrez, Tristan
