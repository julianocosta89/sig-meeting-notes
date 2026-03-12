## Key Topics
- Discussion on PR 2190 regarding nested pipelines and their implementation using pipeline function expressions.
- Challenges with the calendar query engine and the folding of data expressions within pipeline functions.
- The handling of discard expressions in the record set engine and the decision to leave certain implementations as to-dos.
- Clarification on the expected behavior of discard expressions and their impact on function return values.
- Review of OPL query structure and its application to log attributes.

## Action Items
- Albert to back out the changes related to the discard expression and its tests, leaving it as a to-do for future implementation.
- Albert to revert changes to the folding logic for invoke functions that were dependent on the discard expression.
- Mike to review the OPL query and provide feedback on the implementation.

## Participants
Mike "Blanch" Blanchard, Albert Lockett
