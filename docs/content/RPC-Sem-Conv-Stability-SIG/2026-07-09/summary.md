## Key Topics
- **Issue Logging**: Madhav has logged several issues related to RPC method attributes and error types, with ongoing discussions about alignment on these topics.
- **RPC Method Originality**: Discussion on whether to maintain separate values for RPC methods in metrics versus spans, emphasizing the need for consistency in querying.
- **Error Type Handling**: Debate on how to categorize error types in gRPC, particularly around client-side errors like "not found" and their implications for metrics.
- **Metadata Naming**: Agreement on using "RPC Request Header" and "RPC Response Header" for clarity in metadata terminology.
- **Histogram Buckets**: Discussion on the appropriateness of current histogram bucket sizes for gRPC metrics and potential adjustments.

## Action Items
- Madhav to file an issue regarding RPC request and response metadata naming.
- Madhav to gather feedback from the gRPC team on error type handling and its historical context.
- Participants to review logged issues in the Slack channel for alignment before the next meeting.

## Participants
Steve Rao, Trask, Matthew Hensley, Madhav, Liudmila Molkova, jmacdonald
