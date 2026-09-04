## Key Topics
- Discussion on JMX Metrics and their stability, including the need for a balance between the number of metrics sent by default and user customization.
- The importance of naming conventions and semantic compliance for metrics, particularly for Kafka and Tomcat.
- Plans for marking certain metrics as stable in the upcoming 3.0 release and the implications of breaking changes.
- The introduction of include/exclude functionality for metrics to enhance user control over what is emitted.
- Concerns about the volume of metrics, especially from systems like Kafka, and the need for a curated list of essential metrics.

## Action Items
- Jason Plumb to provide PR descriptions that highlight metrics with name changes.
- Sylvain Juge to ensure the include/exclude functionality works seamlessly with all metrics, including those from the Kafka bridge.
- Participants to review and finalize the list of metrics to be marked as stable before the 3.0 release.

## Participants
Trask Stalnaker, Jason Plumb, Sylvain Juge, Lauri Tulmin, Peter Findeisen
