## Key Topics
- Ongoing issues with Prometheus receiver and dependency management in OpenTelemetry.
- Discussion on running end-to-end tests on the latest contrib image daily to catch issues early.
- Proposal to embed instrumentation CRDs in a YAML config file for operator configuration, with concerns about code duplication.
- Introduction of network policies for the operator and collector to enhance security, with discussions on defaults and feature flags.

## Action Items
- Jacob to write a PR for running contrib tests daily.
- Tyler to handle the release of the collector artifacts and address the dependency issue.
- Further discussion needed on Antoine's proposal regarding embedding instrumentation CRDs.
- Evaluate the implementation of network policies and their default settings.

## Participants
Jacob Aronoff, Benedikt Bongartz, Tyler Helmuth, Pavel, Yuri Oliveira, and others.
