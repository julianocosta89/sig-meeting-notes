## Key Topics
- Discussion on naming conventions for JMX metrics, particularly the use of "mean" vs. "average."
- Concerns about the implementation of `AttributesMap` extending `HashMap` without specifying initial capacity or load factor.
- Potential performance implications of current attribute handling in spans and suggestions for optimization.
- Exploration of how instrumentation can size attributes based on typical usage patterns.

## Action Items
- Participants to provide feedback on the naming convention for JMX metrics.
- Further investigation into the `AttributesMap` implementation and its impact on performance.

## Participants
John Watson, Trask Stalnaker, Robert Niedziela, Jason Plumb, Lauri
