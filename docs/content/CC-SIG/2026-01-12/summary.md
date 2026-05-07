## Key Topics
- **Deprecation of Jaeger Propagator and Zipkin Exporter**: The Jaeger propagator is now optional, and the Zipkin exporter is deprecated due to Zipkin's support for the OTLP protocol.
- **Changes in Logger Configuration**: A breaking change in the spec regarding logger configuration was discussed, specifically the renaming of the property for enabling/disabling the tracer.
- **Upcoming Semantic Conventions Release**: An upcoming release of Semantic Convention was mentioned, with code generation adjustments expected.
- **CI Improvements and Code Cleanup**: Discussion on cleaning up CI issues and warnings in the codebase to enhance code quality.
- **Contribution Opportunities**: A new contributor is interested in adding unit tests, and there was a discussion on supporting mixed C++ standards in builds.

## Action Items
- Prepare a small PR to adjust the logger configuration in the CPP area to align with spec changes.
- Address CI warnings and clean up the codebase as part of ongoing maintenance.
- Clarify the intent behind a PR related to mixed C++ standards and decide on support for this practice.

## Participants
malff, Tom Tan, Ehsan, Ali Sedighi
