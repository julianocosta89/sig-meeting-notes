## Key Topics
- Progress on Rust implementation for OpenTelemetry sampling.
- Discussion on handling metrics for traces that were not initially sampled but later accessed.
- Proposal for a standard way to filter out traces that shouldn't count towards metrics.
- Need for semantic conventions for metrics derived from spans in both SDK and collector.
- Exploration of zero count indicators in trace states to avoid double counting.

## Action Items
- Chris Marchbanks to experiment with implementing a zero count indicator in their system.
- Further discussion on the implications of zero count and its integration into the OpenTelemetry specifications.

## Participants
Joshua MacDonald, Chris Marchbanks, Peter Findeisen, Juan Vega, Otmar Ertl
