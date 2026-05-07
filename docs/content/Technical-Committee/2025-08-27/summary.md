## Key Topics
- **OpenTelemetry PHP Due Diligence**: Discussion on the zero-code instrumentation for PHP, its features, and integration with existing systems.
- **Security Concerns**: Addressing potential security vulnerabilities and supply chain issues related to the integration of C++ components.
- **Action Items for Future Development**: Establishing requirements for the new PHP instrumentation, including collaboration with other APM vendors and maintaining consistency in resource detection.
- **Metrics Phase Two Proposal**: Discussion on the need for a dedicated project to address outstanding metrics issues and how to manage existing PRs.
- **Proto Repository Cleanup**: Plans to document and improve the usage and packaging of the proto files for better clarity and usability.

## Action Items
- Work with PHP maintainers to define zero-code instrumentation requirements.
- Investigate the integration of existing C++ OTLP exporter with the PHP implementation.
- Ensure that the new PHP instrumentation supports file-based configuration as defined by the configuration SIG.
- Form a dedicated team to address the outstanding metrics issues and propose a Metrics Phase Two project.
- Document the state of the proto repository and improve its packaging and usability.

## Participants
Reiley, Bob Strecansky, Tigran Najaryan, Severin Neumann, Josh Suereth, Brett McBride, Carlos Alberto Cortez, Liudmila Molkova.
