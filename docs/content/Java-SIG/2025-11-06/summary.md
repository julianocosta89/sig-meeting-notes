## Key Topics
- **Release Management**: Discussion on the upcoming car repo release and responsibilities for merging changes.
- **Stabilization Efforts**: Conversations around stabilizing components, particularly regarding the use of wrappers in attributes extraction and the implications of generic types in SPI interfaces.
- **Global OpenTelemetry Instance**: Addressing the ability to check if a global OpenTelemetry instance is set without side effects and the necessity of a method to determine its state.
- **Invoke Dynamic Migration**: Proposal to enable Invoke Dynamic for instrumentation, with considerations for potential breaking changes and testing.
- **Complex Attributes Handling**: Discussion on supporting complex attributes in a way that retains their original structure without unnecessary conversions.

## Action Items
- Jack Berg to open a PR to add a method to check if the global OpenTelemetry instance is set.
- Jack Shirazi to conduct tests on existing extensions to ensure compatibility with the Invoke Dynamic migration.
- Trask Stalnaker to continue working on the implementation for complex attributes and share updates in future meetings.

## Participants
Gregor Zeitlinger, John Watson, Trask Stalnaker, Jason Plumb, Jack Berg, Bruno, Lori, Tyler Benson, Jack Shirazi.
