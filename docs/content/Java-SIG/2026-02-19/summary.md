## Key Topics
- Discussion on naming conventions for JMX metrics, specifically the use of "mean" vs. "average."
- Concerns regarding the implementation of `AttributesMap` extending `HashMap` and its potential inefficiencies.
- Exploration of how to optimize attribute handling in spans and instrumentation.
- Consideration of how many attributes are typically captured and their impact on memory allocation.

## Action Items
- Participants to provide feedback on the naming convention for JMX metrics.
- Further investigation into the `AttributesMap` implementation and its performance implications.
- Consideration of smarter sizing for attributes in instrumentation based on typical usage.

## Participants
John Watson, Trask Stalnaker, Robert Niedziela, Jason Plumb, Lauri
