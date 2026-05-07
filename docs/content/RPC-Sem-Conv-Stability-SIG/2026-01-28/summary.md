## Key Topics
- Discussion on removing network protocol name and version from RPC semantic conventions.
- Proposal to make RPC request metadata opt-in for spans and metrics.
- Review of gRPC target string handling and capturing server address and port.
- Consideration of how to handle different schemes (e.g., Zookeeper, NACOS) in gRPC metrics.
- Clarification on the implications of capturing server addresses in the context of load balancing.

## Action Items
- Create a PR to remove network protocol name and version from RPC conventions.
- Document the opt-in approach for capturing RPC request metadata in spans and metrics.
- Update the PR regarding gRPC target handling based on the discussion.

## Participants
Steve Rao, Trask Stalnaker, Liudmila Molkova
