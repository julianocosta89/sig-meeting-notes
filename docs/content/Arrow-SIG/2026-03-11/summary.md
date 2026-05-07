## Key Topics
- Discussion on PR 2190 regarding nested pipelines and pipeline function expressions.
- Changes to the optimization method for the pipeline expression to ensure proper folding of data expressions.
- Challenges with implementing discard functionality in the record set engine.
- Benchmarking performance comparisons between different filter engine implementations.
- Strategies for normalizing data structures to improve performance.

## Action Items
- Albert to back out the discard implementation as a to-do and make necessary changes to the PR.
- Albert to implement a mutable value expression target in the discard expression for future use.
- Mike to push his local changes to the branch for review and further feedback.

## Participants
Mike "Blanch" Blanchard, Albert Lockett
