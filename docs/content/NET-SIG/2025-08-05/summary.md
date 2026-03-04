## Key Topics
- Discussion on updating the EF Core call provider to align with SQL client semantic conventions.
- Clarification on the policy for handling semantic convention updates on a library-by-library basis.
- Consideration of the value of having both EF Core and SQL client instrumentation or potentially toggling one off.
- Introduction of bytecode instrumentation to address gaps in the .NET framework.
- Issues with Redis instrumentation losing context when commands are executed asynchronously.

## Action Items
- Martin Costello to research the environment variable for semantic conventions and update the EF Core issue accordingly.
- Alan West to follow up with Steve Gordon regarding bytecode instrumentation and potential collaboration.
- Matthew Hensley to finalize PR adjustments for Redis instrumentation context handling.

## Participants
Alan West, Martin Costello, Julius Koval, Matthew Hensley, Steve Gordon
