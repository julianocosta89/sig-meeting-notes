## Key Topics
- Proposal for adding detailed events to HTTP spans to capture various network request durations (DNS resolution, TLS setup, connection time, server processing time).
- Discussion on the implementation of these events as span events versus standalone events.
- Agreement on the opt-in nature of the proposed events to avoid impacting existing users.
- Consideration of feedback regarding the future deprecation of span events in favor of standalone events.

## Action Items
- Surbhi A to start working on the implementation of the proposed events in the Java instrumentation and semantic conventions.
- Jason Plumb to assign the task to Surbhi A for tracking progress.

## Participants
Jason Plumb, Martin Kuba, VP Valentin Pertuisot, Surbhi A
