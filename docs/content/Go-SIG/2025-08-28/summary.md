## Key Topics
- **SDK Observability**: Discussion on improving SDK observability, documenting design and best practices, and addressing performance concerns.
- **Performance Optimization**: Emphasis on minimizing performance overhead in observability setups and the importance of efficient attribute handling.
- **Release Planning**: Urgency to release version 1.38 and address outstanding PRs, particularly regarding instrument attributes and semantic conventions.
- **Proto Attribute Value Restrictions**: Proposal to remove restrictions on attribute value types in proto definitions, with a focus on transparency for consumers.
- **Batching Metrics**: Discussion on the lack of built-in batching in the Go SDK and the need for custom exporters to handle large metric payloads.

## Action Items
- Tyler to submit observations on SDK observability to the BAPR for documentation.
- Review and finalize the release of version 1.38, addressing outstanding PRs.
- Robert to create a changelog for the upcoming 1.80 release, incorporating comments on the proto changes.

## Participants
Tyler Yahn, Robert Pająk, Sam Xie, Bryan Boreham
