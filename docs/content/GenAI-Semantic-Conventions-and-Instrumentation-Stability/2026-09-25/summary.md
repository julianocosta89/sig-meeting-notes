## Key Topics
- Discussion on breaking changes and the mechanism for implementing them in OpenTelemetry, including the potential use of a Stability opt-in environment variable.
- The need for a standardized versioning approach for GenAI conventions to manage rapid changes effectively.
- Clarification on the distinction between inference spans and chat spans in telemetry, particularly regarding server-side operations and tool calls.
- The implications of server-side tool loops on the existing conventions and the need for a clear definition of what constitutes an inference call versus a chat request.

## Action Items
- Aaron Abbott to file an issue regarding the Stability opt-in approach and its applicability to the GenAI repo.
- Discussion to be scheduled for further exploration of the distinction between inference and chat spans, including potential changes to the schema.
- Trask Stalnaker to add the topic of server-side operations and their implications to the project board for further consideration.

## Participants
Aaron Abbott, Christopher Cordi, Trask Stalnaker, Felix Becker, Dylan Russell, Surya Teja, Iwa Wong
