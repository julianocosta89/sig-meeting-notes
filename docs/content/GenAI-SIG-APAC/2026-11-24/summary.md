## Key Topics
- **Semantic convention release:** The GenAI repository released its first version last week. Steve Rao's team needs releases to update their instrumentation to the latest conventions.
- **Token usage and cost:** Some coding agents and SDKs calculate token usage or cost differently than the current conventions. Liudmila Molkova noted that instrumentations generally don't know customer-specific pricing, so cost reporting may need a collector processor or manual instrumentation. No new attributes were agreed without concrete use cases.
- **User ID attribute:** Steve proposed a "GenAI user ID" attribute, populated from agentic frameworks such as AgentScope, to avoid conflicting with the general `user.id` attribute. Liudmila agreed it fits the GenAI scope and suggested describing it as user information provided by the framework, with examples.

## Action Items
- Steve Rao: Update the user ID PR to use the GenAI user ID attribute, with the scope described as framework-provided user information and examples added.
- Liudmila Molkova: Review the updated user ID PR.

## Participants
Steve Rao, Liudmila Molkova
