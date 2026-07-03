## Key Topics
- Discussion on the Azure Container Apps detector in the Go SDK and the appropriate resource attribute to use (service.instanceID vs. fast.instance).
- Proposal for status remapping in gRPC to allow custom error code handling at the method level.
- Review of the logs API stability and the process for compliance auditing.
- The need for consistency across different language implementations regarding semantic conventions.

## Action Items
- Kathie Huang to update the PR with the chosen resource attribute for the Azure Container Apps detector and communicate with Azure teams if necessary.
- Puneet Singh to explore the implementation of error code mapping in gRPC and consider how it aligns with semantic conventions.
- Pellared to conduct an audit of the logs API compliance and document findings.

## Participants
Tyler Yahn, Kathie Huang, Puneet Singh, Israel Blancas, Pellared
