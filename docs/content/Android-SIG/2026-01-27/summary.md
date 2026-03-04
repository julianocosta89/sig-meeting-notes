## Key Topics
- Updates on the implementation of attributes in HTTP spans for OKHTTP3 manual instrumentation.
- Discussion on the challenges faced with closing spans and correlating logs with spans.
- Proposal to create standalone log records containing timing attributes to address backend limitations.
- Clarification on the use of trace ID and span ID in log records and the distinction between logs and events.
- Review of the ongoing work to enhance metrics for HTTP requests linked to trace contexts.

## Action Items
- Surbhi A to implement the copying of HTTP span attributes to log records.
- Surbhi A to adjust the log record to use the setContext API for trace and span IDs.
- Team to provide feedback on whether to treat the log record as an event or maintain it as a log.

## Participants
Jason Plumb, Cesar Munoz, Surbhi A, David Graff, Hanson Ho
