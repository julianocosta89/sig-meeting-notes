## Key Topics
- **Pull Request Ownership**: Discussion on the ownership issues related to PR #44378 and the lack of responsive reviewers.
- **Histogram Implementation**: Exploration of different approaches for handling histograms with fractional counts, including changing to float64, using a scaling factor, and probabilistic rounding.
- **Sampling Strategies**: Consideration of how to implement probabilistic rounding to maintain integer operations while accounting for fractional sampling.
- **Future Work**: Agreement on the need for microbenchmarks and potential development of a new histogram data type.

## Action Items
- **jmacdonald** to push for the review and potential merging of PR #44378.
- **Yuanyuan Zhao** to investigate Go SDK sampler support and report back in the next meeting.
- **Group** to explore microbenchmarks for the discussed histogram implementations.

## Participants
jmacdonald, Alf Kenny, Amar, Otmar Ertl, Yuanyuan Zhao, Peter Findeisen
