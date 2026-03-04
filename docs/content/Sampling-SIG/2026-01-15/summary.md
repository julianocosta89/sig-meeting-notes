## Key Topics
- **Pull Request Ownership Issues**: Discussion on the lack of responsiveness from code reviewers regarding Alf's PR (44378) and the need for clearer ownership.
- **Histogram Implementation Challenges**: Yuanyuan presented issues with the current histogram implementation in relation to fractional counts due to new probabilistic sampling.
- **Proposed Solutions**: Three approaches to handle fractional counts were discussed: changing counts to float64, using a fractional scaling factor, and implementing probabilistic rounding.
- **Consensus on Next Steps**: Agreement to explore the proposed solutions further and conduct microbenchmarks.

## Action Items
- **jmacdonald** to push for a resolution on Alf's PR and potentially become a code owner.
- **Yuanyuan Zhao** to implement and benchmark one or more of the proposed histogram solutions.

## Participants
jmacdonald, Alf Kenny, Otmar Ertl, Yuanyuan Zhao
