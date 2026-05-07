## Key Topics
- Discussion on adding debug-level logs for errors in consume calls.
- Proposal for a new OTTL function to split batched JSON logs from CloudTrail into individual events.
- Ongoing conversation about the deprecation of the OpenCensus Receiver and Exporter, with concerns from users about its removal.
- Plans for building Windows ARM support and potential concurrency issues in tests.
- Discussion on improving the onboarding process for first-time contributors to the project.

## Action Items
- Jade Guiton to add a link to the RFC amendment regarding debug logs in the GitHub issue.
- Arthur Silva Sens to investigate existing automation for testing metric name changes and consider how to integrate it into the collector core.
- Raj Nishtala to find a sponsor for the proposed OTTL function for splitting logs.
- Heitor (Huawei) to clarify the need for a custom logs receiver and provide use case details in the issue.
- Paulo Janotti to continue working on Windows ARM support and ensure thorough testing before integration into the releases repository.

## Participants
Sylvain, Antoine Toulme, Sean Marciniak, Andrzej Stencel, Jade Guiton, Arthur Silva Sens, Pablo Baeyens, Dmitrii Anoshin, Israel Blancas, Raj Nishtala, Tyler Helmuth, Heitor (Huawei), Paulo Janotti, Evan Bradley.
