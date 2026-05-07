## Key Topics
- **Build Enhancements**: Discussion on improvements in build times, reducing from 40 minutes to 20 minutes.
- **Span Processor Reinitialization**: Need for the ability to shut down and restart the span processor for custom user sessions.
- **Multiple RUM Instances**: Concerns about supporting multiple instances of RUM and the implications of doing so.
- **Permission Management**: The decision to remove sensitive permissions from the SDK manifest and document their necessity for specific features.
- **Trace ID Propagation**: Clarification on the existing trace context propagation in HTTP requests and potential enhancements.

## Action Items
- **Investigate Shutdown Method**: Mustafa to explore the implementation of a shutdown method for the SDK to facilitate clean reinitialization.
- **Documentation Update**: Surbhi to update documentation to reflect changes in permissions and required configurations for network attributes.
- **Log Implementation**: Consider implementing logging when permissions are not granted to assist with debugging.

## Participants
Jason Plumb, Hanson Ho, Cesar Munoz, Mustafa Haddara, Surbhi, Cleverchuk
