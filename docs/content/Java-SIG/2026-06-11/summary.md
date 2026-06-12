## Key Topics
- Discussion on the implementation of entities in the Java SDK, including changes to resource handling and OTLP exporter updates.
- Review of the upcoming 3.0 release, focusing on the stability of features and potential last-minute changes.
- Examination of the need for flags in resource detection and entity handling, with considerations for backward compatibility.
- Updates on semantic conventions and the handling of event names and metrics in the Java and Kotlin SDKs.

## Action Items
- Josh Suereth to create a PR for resource changes and OTLP exporter updates without modifying resource detection initially.
- Review and finalize the handling of flags for entity inclusion in the Java SDK.
- Trask Stalnaker to check on the status of the open PR regarding thread detail configuration.
- Jason Plumb to proceed with merging the metrics PR that publishes to the incubating artifact.

## Participants
Gregor Zeitlinger, John Watson, Jason Plumb, Jack Berg, Josh Suereth, Trask Stalnaker, Jay DeLuca, Pranav Sharma.
