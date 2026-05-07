## Key Topics
- Discussion on updating semantic conventions for EF Core and SQL Client instrumentation, emphasizing the need for coordination between the two.
- Clarification on the approach for handling semantic convention updates on a library-by-library basis.
- Consideration of the Redis instrumentation's handling of activity context in asynchronous operations and whether to set the current activity.
- Exploration of potential collaboration on SQL Client and EF Core instrumentation improvements.
- Discussion on the performance implications of the Redis instrumentation and the philosophical considerations of using filters and enrichers.

## Action Items
- Martin Costello to research the environment variable for semantic conventions and update the EF Core instrumentation accordingly.
- Matthew Hensley to investigate the Redis instrumentation further and assess the necessity of setting the current activity.

## Participants
Alan West, Martin Costello, Julius Koval, Matthew Hensley, Mike "Blanch" Blanchard
