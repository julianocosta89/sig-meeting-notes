## Key Topics
- **Condensing Attributes**: Discussion on the new experimental processor for condensing non-well-known Ceph extensions into a single attribute.
- **Error Handling**: Ongoing concerns about internal error handling in components and the need for better instrumentation.
- **Weaver Dependencies**: Issues with Cargo Deny blocking CI work due to dependency advisories and the need for updates in Weaver.
- **Syslog Parsing Discrepancies**: Identifying differences in syslog parsing between Rust and Go implementations, specifically regarding app name and process ID attributes.

## Action Items
- Drew to provide more details on the condensing attributes issue for clarity.
- Follow up on the status of the attributes processor's ability to insert new attributes.
- Investigate the impact of Cargo Deny on development work and explore options for distinguishing between production and development dependencies.
- Consider implementing changes to the Rust syslog receiver to parse app name and process ID attributes similar to the Go implementation.

## Participants
Joshua MacDonald, Drew Relmas, Tom Tan, Utkarsh Umesan Pillai, Laurent, Lowlet
