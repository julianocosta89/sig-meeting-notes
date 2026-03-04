## Key Topics
- Discussion on adding artifacts to the release process using Cosign for signing binaries and eBPF programs.
- Integration of OpenTelemetry with AutoCollector and potential duplication of work.
- Development of a Java agent for TLS support in OpenTelemetry.
- Issues with trace submission failures and potential loss of traces during resubmission.

## Action Items
- Explore the implementation of Cosign in the release process and consider creating a PR for experimentation.
- Investigate the integration of OpenTelemetry with AutoCollector to avoid duplication of efforts.
- Continue development on the Java agent for TLS support and resolve packaging issues.
- Review the trace submission logic to address potential loss of traces during retries.

## Participants
Nikola Grcevski, Giuseppe Ognibene, Florian Lehner, Stephen Lang, Mario Macias, Rafael Roquetto
