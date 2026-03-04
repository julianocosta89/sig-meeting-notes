## Key Topics
- Merging of a PR for new internal telemetry following experimental semantic conventions.
- Discussion on handling configuration properties in instrumentation, specifically regarding type mismatches (null vs. exception).
- Considerations on the impact of failing fast versus graceful degradation in the Java agent during startup.
- Clarification on how YAML parsing affects configuration properties and their types.
- The implications of instrumentation installation timing and its relation to application startup.

## Action Items
- Jack to explore options for opting into new telemetry formats via declarative config.
- Team to define clear behavior for type mismatches in configuration properties.
- Further investigation needed on the consequences of failing fast versus allowing the Java agent to continue running.

## Participants
Jack Berg, John Watson, Trask Stalnaker, Jay DeLuca, Lauri
