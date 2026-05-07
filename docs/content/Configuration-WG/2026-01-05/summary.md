## Key Topics
- **Stability Status**: Discussion on the current status of stability for OpenTelemetry, including a draft PR to mark declarative config as stable and dependencies on other PRs for consistency.
- **ID Field in Schema**: Concerns raised about the ID field in the schema, whether to keep it, remove it, or embed versioning information.
- **Prometheus Exporter Issues**: Challenges with the Prometheus exporter affecting the ability to use the collector as a test implementation for configuration.
- **Config Provider Behavior**: Discussion on how the config provider should behave when declarative configuration is not used, including potential changes to the specification for clarity.
- **Environment Variable Mapping**: Consideration of whether to standardize how environment variables map to the config provider across different languages.

## Action Items
- **Review and Update PRs**: Participants to review the draft PR for declarative config and address comments from Robert.
- **Clarify Config Provider Behavior**: Create an issue to clarify the behavior of the config provider when declarative configuration is not used.
- **Explore Environment Variable Mapping**: Assess the need for standardizing environment variable mapping in the config provider across languages before formalizing it in the specification.

## Participants
Jack Berg, Gregor Zeitlinger, Alex Boten
