## Key Topics
- **Demo of OpenTelemetry eBPF Instrumentation**: Nimrod presented a demo showcasing modifications to the OpenTelemetry demo, focusing on microservices and database communications.
- **Context Propagation Issues**: Discussion on challenges with context propagation between services, particularly regarding trace and span IDs.
- **Pull Request Review**: Review of open pull requests, including dependency updates and issues with the collector API.
- **HTTP Header and Body Extraction**: Proposal to enhance HTTP spans by including headers and payloads, with considerations for performance impacts.
- **Socket Programs Discussion**: Rafael shared insights on using socket message and string verdict programs for tracking socket lifecycles and improving observability.

## Action Items
- **Create Issues for Identified Bugs**: Document and create issues for the bugs and challenges discussed during the demo.
- **Update CI Checks for Copyright Headers**: Implement CI checks to ensure consistent copyright headers across all file types.
- **Benchmark Large Buffer Processing**: Develop benchmarks to assess the performance of large buffer processing in user space.
- **Explore Socket Iterators**: Investigate the use of socket iterators for tracking sockets and potentially filtering based on process IDs.

## Participants
Rafael Roquetto, Tyler Yahn, Nikola Grcevski, Nimrod Avni, Mattia Meleleo, Marc
