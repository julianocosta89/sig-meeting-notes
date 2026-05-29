## Key Topics
- Discussion on the new feature for CPU metrics in the OpenTelemetry force metric receiver, focusing on reducing decimal precision for better storage efficiency.
- Concerns raised about the complexity of moving calculations from GOPS utils to the receiver and the implications for maintenance.
- Consideration of a unified approach for handling metric precision across different components instead of implementing changes in each receiver.
- Updates on the pull request for version metrics in mDataGen, particularly regarding handling attribute type changes.

## Action Items
- Review the pull request related to CPU metrics and discuss its implications in the next meeting.
- Explore the possibility of contributing upstream to GOPS utils regarding the precision and calculation methods.
- Clarify the handling of attribute type changes in mDataGen and consider adding it to the RFC if necessary.

## Participants
Donal O'Sullivan, Dmitrii Anoshin, Roger Coll, N'at, Christos Markou
