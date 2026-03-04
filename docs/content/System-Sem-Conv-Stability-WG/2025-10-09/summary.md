## Key Topics
- Discussion on the stability levels of metrics in the OpenTelemetry collector and the need for clear rules for defining these levels.
- The importance of linking metrics to semantic conventions and the implications of marking metrics as stable.
- Challenges surrounding the communication of metric changes and the need for a mechanism to enforce stability.
- The potential for defining stable metrics within the collector that may not be included in semantic conventions.

## Action Items
- Christos Markou to revisit and prepare PR #13920 for review.
- Establish clear rules for changing stability levels of metrics in the collector.
- Explore the integration of metadata YAML and Weaver for better stability enforcement.

## Participants
Pablo Baeyens, Braydon Kains, Christos Markou, Josh Suereth
