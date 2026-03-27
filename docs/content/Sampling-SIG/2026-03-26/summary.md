## Key Topics
- Discussion on the implementation of trace ID ratio sampler in Go.
- Clarification of TH0 and its implications for sampling behavior, particularly in legacy cases.
- The introduction of attributes to distinguish how sampling counts are derived (extrapolated vs. counted).
- Consideration of user choice in counting unknown TH values and its impact on metrics.
- The relationship between TH values and randomness in sampling algorithms.

## Action Items
- Review and finalize the PR for adding the trace ID ratio sampler in Go.
- Further discussion on whether to support user-defined counting for unknown TH values.
- Evaluate the implications of modifying TH values in multi-stage sampling scenarios.

## Participants
jmacdonald, Chris Marchbanks, Yuanyuan Zhao, Peter Findeisen
