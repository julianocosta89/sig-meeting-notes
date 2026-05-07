## Key Topics
- Discussion on the migration guide and the need for distinct RPC service and method names.
- Review of a pull request regarding sampling attributes for spans.
- Proposal to merge service name and method name into a single attribute for consistency across frameworks.
- Consideration of method types (unary vs. streaming) and how to capture them in metrics.
- Agreement on non-breaking changes to add streaming attributes without disrupting existing metrics.

## Action Items
- Liudmila Molkova to update issues regarding the merging of service and method names.
- Explore the addition of a streaming type attribute in metrics while ensuring it remains non-breaking.

## Participants
Liudmila Molkova, Matthew Hensley, Steve Rao, Trask Stalnaker
