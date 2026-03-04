## Key Topics
- Status update on migrating eBPF codebase to OpenTelemetry, with significant progress made in removing internal code.
- Discussion on open pull requests, including the need for updates on service name templates and MySQL data parsing in kernel space.
- Performance improvements through potential eBPF space detection for unknown TCP traffic, reducing user space overhead.
- Configurability of data buffers for user-specific needs, including the ability to analyze full payloads and headers.

## Action Items
- Review and clean up open pull requests, particularly the service name template and MySQL data parsing.
- Investigate the possibility of configuring dependency updates to reduce the number of individual pull requests.

## Participants
Mattia Meleleo, Rafael Roquetto, Tyler Yahn, Nikola Grcevski, Mario Macias, Marc
