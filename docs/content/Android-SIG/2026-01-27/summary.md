## Key Topics
- Discussion on implementing attributes in HTTP spans and challenges faced with response timing in OpenTelemetry Java instrumentation.
- Proposal for copying original HTTP span attributes to log records for better correlation with backends.
- Examination of the instrumentation API and the need for improvements to avoid workarounds in existing implementations.
- Consideration of how to handle forced log flushing during crashes and the responsibilities of the SDK versus instrumentation.

## Action Items
- Surbhi A to implement copying original HTTP span attributes to log records.
- Surbhi A to create an issue for tracking auto-instrumentation configuration changes.
- Participants to review and provide feedback on the proposed changes and PRs discussed.

## Participants
Jason Plumb, Cesar Munoz, Surbhi A, Hanson Ho, David Graff, Jamie Lynch
