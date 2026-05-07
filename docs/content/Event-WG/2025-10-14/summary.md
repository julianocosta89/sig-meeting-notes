## Key Topics
- Discussion on the stabilization of the event name attribute and its implications for the OpenTelemetry specification.
- Consideration of the differences between using `event.name` as an attribute versus a proto field.
- The need for clear documentation on how event names should be handled in various logging frameworks.
- Agreement on the introduction of `otel.event.name` for clarity and backward compatibility.
- The importance of semantic conventions in defining event attributes and ensuring consistency across implementations.

## Action Items
- Liudmila Molkova to create an issue for stabilizing the event name attribute.
- Robert Pająk to revert the commit introducing the deprecated event name and create a new PR for the new attribute.
- Participants to update documentation to clarify the handling of event names in logging frameworks.

## Participants
Robert Pająk, Trask Stalnaker, Liudmila Molkova, Austin Parker
