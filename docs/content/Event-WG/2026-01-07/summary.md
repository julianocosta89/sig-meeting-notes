## Key Topics
- Discussion on how to record Errors vs. Exceptions in OpenTelemetry, particularly in logs.
- The plan to deprecate span events at the API level while maintaining them over OTLP for a transitional period.
- Need for clarity and consistency in terminology and implementation across different programming languages regarding error handling.
- Stabilization of HTTP instrumentation and the importance of resolving ambiguities around error and exception recording.
- The distinction between errors and exceptions and its implications for current and future specifications.

## Action Items
- Clarify the definitions and handling of errors and exceptions in the documentation.
- Unblock Robert's progress on HTTP instrumentation by reaching consensus on recording errors on spans.
- Review and potentially revise the existing proposals regarding error recording before stabilization.

## Participants
Trask Stalnaker, Pellared, Alex Hall, Liudmila Molkova, Alan West
