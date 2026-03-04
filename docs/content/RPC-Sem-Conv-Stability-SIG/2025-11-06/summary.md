## Key Topics
- **Meeting Time Adjustment**: Discussion on moving the meeting time an hour earlier for winter.
- **Stability Targets**: Agreement on focusing on gRPC, ConnectRPC, and Dubbo for stability, with considerations on JSON RPC's relevance.
- **RPC Status Codes**: Decision to unify RPC status codes to a single `rpc.statuscode` to avoid confusion and potential sensitive information exposure.
- **Duration Metrics**: Proposal to align duration metrics with existing Java instrumentation and gRPC metrics, focusing on the logical layer and call duration.
- **Streaming vs Non-Streaming Metrics**: Exploration of how to handle metrics for different types of RPC calls, including streaming scenarios.

## Action Items
- **Meeting Time Update**: Liudmila Molkova to update the meeting calendar to reflect the new time.
- **Documentation Review**: Review and finalize the status code unification PR and address sensitive information concerns.
- **Metric Naming**: Consider naming conventions for duration metrics to ensure clarity and consistency.

## Participants
Trask Stalnaker, Steve Rao, Matthew Hensley, Liudmila Molkova, Albumen Kevin
