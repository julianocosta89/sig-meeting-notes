## Key Topics
- Next release discussion, including sunsetting support for Go 1.24 and addressing a security issue.
- Updates on the baggage implementation and error handling in the OpenTelemetry Go SDK.
- Review of the concurrency guarantees in the API documentation.
- Discussion on the deprecation of the labeler in favor of new metric attributes.
- Plans for refactoring the benchmark CI and addressing CI flakiness.

## Action Items
- Sam to resolve comments on the baggage PR and provide updates.
- David to update documentation on concurrency guarantees for the tracer provider, tracer, and span.
- Damien and Pellared to document the decision to deprecate the labeler and transition to metric attributes.
- Robert to explore the implementation of unsafe methods for attributes to improve performance.

## Participants
Tyler, Damien Mathieu, Sam Xie, David Ashpole, Pellared
