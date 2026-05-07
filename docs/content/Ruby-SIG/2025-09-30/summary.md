## Key Topics
- Discussion on the User Facing Logging API and its potential impact on existing logging implementations.
- Update on the deprecation of the trace ratio-based probability sampler and its replacement with a new probability sampler.
- Upcoming changes in the OpenTelemetry Ruby Contrib library, including raising the minimum Ruby version to 3.2 and updating the minimum OpenTelemetry Ruby API to 1.7.
- Concerns regarding a PR that proposes changing version constraints in the Instrumentation All gem, with discussions on its implications for users.
- Ongoing issues with installation errors and the need for clearer documentation regarding the use of the "all" gem in production environments.

## Action Items
- Review and address feedback on the PR related to version constraints in Instrumentation All.
- Update the README and documentation to clarify that the "all" gem is a convenience package and not recommended for production use.
- Investigate the logging issue raised by Wendy Smoak and consider adding checks for UTF-8 encoding earlier in the pipeline.

## Participants
Kayla Reopelle, Robb Kidd, Wendy Smoak
