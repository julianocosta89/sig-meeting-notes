## Key Topics
- Upcoming release planned for the week, with no critical issues reported.
- Warre Pessers presented a draft on context propagation for AWS Lambda, including SQS event handling.
- Discussion on span linking and the hierarchy of spans in tracing, particularly between Lambda invocation spans and processing spans.
- Concerns raised about the compatibility of trace linking with various tracing backends.

## Action Items
- Warre to share the JSON file and export traces to a tracing backend for visual verification.
- Test the implementation with different tracing backends (Grafana, Zipkin, etc.) to assess support for trace linking.
- Consider additional properties for identifying SQS events to enhance robustness.

## Participants
Serkan Özal, Tyler Benson, Warre Pessers
