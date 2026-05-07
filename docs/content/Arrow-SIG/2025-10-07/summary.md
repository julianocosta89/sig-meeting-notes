## Key Topics
- Discussion on issue triage and new requirements for OTLP, including TLS support and compression configuration.
- Updates on the development of a basic filter processor and KQL language for the OTAP pipeline.
- Multi-pipeline deployment strategies and the need for isolation in pipeline configurations.
- Handling invalid UTF-8 data in pipelines and the implications for data integrity and processing.
- Introduction of a back pressure mechanism and the need for admission control to manage memory usage effectively.

## Action Items
- Laurent to propose a solution for managing unbounded channels introduced by delayed processing.
- Team to consider implementing a configurable policy for handling invalid UTF-8 data.
- Further exploration of integrating OpenZL for improved compression in the OTAP protocol.

## Participants
Albert Lockett, Danny Chin, Josh Macdonald, Laurent Quérel, Utkarsh Pilla, Bill Zuo
