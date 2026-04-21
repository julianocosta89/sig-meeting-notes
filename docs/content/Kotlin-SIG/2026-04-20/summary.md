## Key Topics
- **Branch Protection Settings**: Discussion on implementing branch protection for the release branch and its impact on CI workflows.
- **Bug Report on Protobuf Export**: Identified an issue where integer values in attributes cause exceptions; proposed solutions to handle integer values.
- **Handling Complex Attributes**: Explored how complex attributes are serialized and the need for better type handling in the exporter.

## Action Items
- Jamie to link the PR for branch protection to Jason for review.
- Investigate how integers are being set in attributes and ensure proper type handling in both SDK and exporter.
- Document the need for coercing integers to long in the codebase.

## Participants
Jason Plumb, Hanson, Jamie Lynch
