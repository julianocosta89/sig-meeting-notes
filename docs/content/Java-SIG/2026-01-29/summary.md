## Key Topics
- **Sender Compatibility Issues**: Discussion on the challenges faced by a Google Cloud SDK user regarding version conflicts with OKHTTP due to OpenTelemetry's dependencies.
- **Dependency Management**: The need for OpenTelemetry to potentially downgrade its version to accommodate users still on OKHTTP4.
- **Logging Configuration**: Addressing concerns about sensitive information being logged and the need to adjust logging levels in the Java agent.
- **Network Timing Attributes**: Debating the best approach to implement timing attributes for network phases in the Java Instrumentation repo.
- **Future Releases**: Planning for the upcoming 3.0 release and discussing breaking changes related to semantic conventions and dependency updates.

## Action Items
- **Documentation Update**: Create clearer documentation for users on how to manage dependencies and resolve version conflicts.
- **Investigate Dependency Options**: Explore the possibility of downgrading OpenTelemetry for specific users while maintaining compatibility with newer versions.
- **Logging Level Adjustment**: Implement changes to ensure sensitive information is not logged at the info level.
- **Semantic Conventions Proposal**: Develop a proposal for how to model timing attributes and discuss it in the semantic conventions group.

## Participants
Robert Niedziela, Gregor Zeitlinger, Trask Stalnaker, Peter Findeisen, Jason Plumb, Jack Berg, Blake Li, John Watson, Lauri, Pranav Sharma, Surbhi Agarwal, Bruno Baptista
