## Key Topics
- Discussion on the experimental SDK and the use of options to add features without affecting the stability of the public API.
- Review of the meter configurator and issues related to self-instrumentation leading to potential deadlocks.
- Consideration of the definition and implications of no-op meters and their internal state management.
- Exploration of the interaction between the bind and finish methods for metrics, including performance implications and API design.
- Need for further discussions in the spec meeting regarding the reading side of metrics and improvements to the spec.

## Action Items
- Puneet to create issues and raise concerns in the spec meeting regarding no-op meters and their definitions.
- Tyler and David to review the PRs related to the bound instrument API and finish method.
- Further exploration of the interaction between bind and finish methods to be discussed in future meetings.

## Participants
Tyler Yahn, Puneet Singh, David Ashpole
