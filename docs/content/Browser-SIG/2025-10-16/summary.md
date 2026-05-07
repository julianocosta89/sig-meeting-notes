## Key Topics
- Discussion on gathering metrics around network request phases (DNS lookup, connection setup, TLS handshake).
- Proposal to unify semantics across browser and mobile by adding individual timestamp attributes to the original HTTP span instead of using standalone events.
- The need for consistency in instrumentation between browser and mobile applications.
- Consideration of configuration properties for capturing specific timestamps and possibly using arrays for ordered attributes.
- Plans for migrating existing instrumentation to a new browser repository and improving the ecosystem around it.

## Action Items
- Surbhi Agarwal to join the browser SIG and tag Martin for his opinion on the proposed changes.
- Participants to discuss the proposal in the browser SIG Slack for broader input.
- Jared Freeze to compile a list of existing instrumentation that could be contributed back to the repository.

## Participants
Jared Freeze, Daniel Dyla, Surbhi Agarwal, Joaquín Díaz, Santosh Kumar Cheler, David Luna Bistuer, Benoît Zugmeyer
