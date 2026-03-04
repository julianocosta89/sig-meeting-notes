## Key Topics
- **PR for Optional Fields**: Pablo Baeyens discussed a PR to introduce an "enabled" option for optional fields, allowing users to disable fields that are enabled by default.
- **Component Behavior Discussion**: Participants debated the implications of disabling components within the pipeline and the user experience related to enabling/disabling components.
- **Scalar Values and Backward Compatibility**: The group discussed the need for optional fields for scalar values and the potential inconsistencies with structs, emphasizing the importance of backward compatibility.
- **Breaking Change in Configurations**: Jade Guiton presented a PR that introduces a breaking change in configGRPC and configHTTP to align with the OpenTelemetry SDK's header representation, seeking feedback on the necessity of this change.

## Action Items
- **Review PR on Optional Fields**: Dmitrii Anoshin to review Pablo's PR regarding optional fields.
- **Create Issue for Component Enabling/Disabling**: Participants agreed to create a separate issue to discuss the user experience around enabling/disabling components.
- **Deprecation Warning Implementation**: Jade Guiton to consider adding a deprecation warning for the old header format in the PR for configGRPC and configHTTP.

## Participants
Pablo Baeyens, Dmitrii Anoshin, Paolo Janotti, Evan Bradley, Jade Guiton
