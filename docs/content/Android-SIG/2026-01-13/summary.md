## Key Topics
- **Release Process**: Discussion on the challenges faced during the transition from version 0.0 to 1.0, including issues with build automation and the need for manual changes.
- **Stabilization of APIs**: Conversations around which components (e.g., Core, Instrumentation API) should be stabilized next, with emphasis on maintaining backward compatibility.
- **Clock Implementation**: Introduction of a new API to override the default clock, addressing issues with time accuracy during device sleep.
- **Disk Buffering Behavior**: Proposal to change the iterator behavior in disk buffering to avoid automatic deletion of items, which would be a breaking change.
- **gRPC Support**: Discussion on potentially adding gRPC support alongside HTTP in the agent, with considerations on how to implement it without breaking existing functionality.

## Action Items
- Investigate and improve build automation to handle release candidates and patch releases more effectively.
- Review and potentially stabilize the Instrumentation API and Core components.
- Finalize the implementation of the custom clock API and document its usage.
- Implement the proposed change in disk buffering behavior and mark the library as stable afterward.
- Develop a strawman implementation for gRPC support in the agent.

## Participants
Jason Plumb, Jamie Lynch, João Oliveira, Cesar Munoz, Hanson Ho, Mustafa Haddara
