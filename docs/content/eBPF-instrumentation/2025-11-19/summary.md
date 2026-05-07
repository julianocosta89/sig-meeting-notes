## Key Topics
- Discussion on integrating artifact signing into the release process using Cosign for better security.
- Exploration of the integration of eBPF programs with the OpenTelemetry Collector and potential overlaps with AutoCollector.
- Updates on the Java support for TLS, including the development of a Java agent for better integration.
- Issues with trace submission failures and potential solutions for reducing trace loss during retries.
- Review of open pull requests and challenges faced with dependencies and CI/CD processes.

## Action Items
- Experiment with integrating Cosign into the release process and consider creating a PR.
- Investigate the trace submission issue further and document findings regarding queue sizes and back-off times.
- Consider switching from Alpine to a different base image for Docker to avoid compatibility issues.
- Follow up on the Java agent development and ensure the necessary packaging is completed.

## Participants
Nikola Grcevski, Giuseppe Ognibene, Florian Lehner, Stephen Lang, Mario Macias, Rafael Roquetto, Cheithanya PR
