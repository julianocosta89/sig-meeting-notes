## Key Topics
- Discussion on updating Grafana's OpenTelemetry libraries from version 1.9 to 1.12, and the implications of .NET 9 on compatibility.
- Challenges faced by .NET Framework users due to binding redirects and the complexities introduced by new APIs in .NET 9.
- Consideration of future strategies for supporting .NET Framework alongside newer .NET versions, including potential pinning to specific versions.
- The need for clarity on the support lifecycle of extension packages in relation to .NET Framework.

## Action Items
- Mike "Blanch" Blanchard to inquire with the .NET team about ideal extension package versions for .NET Framework and present the friction caused by the current policy of always using the latest versions.
- Martin Costello to provide feedback on the proposed stance for future .NET versions and their implications for .NET Framework users.

## Participants
Alan West, Martin Costello, Mike "Blanch" Blanchard
