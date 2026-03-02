## Meeting Notes

### Attendees
- [Mateusz Lach](mailto:mateusza@splunk.com) (Splunk)
- Chris Ventura (New Relic)

### Agenda
- Support for MongoDB 3.5.0
  - Does not need to be part of this next release, but can be investigated for the following release
- Framework specific dependencies for .net framework versions
  - Most of the questions have been addressed
- Instrumentation configuration
  - Call for additional reviewers on the PR
  - Discussed the related spec proposal for presets, and how the current configuration behavior diverges from the experience that many vendors have with their historical auto configuration solutions
- [Igor] Discovered a way to investigate TPM assemblies for .NET apps to try to improve the assembly loading experience for .NET.
  - Proposal likely to be brought forward in parallel with the .net framework assembly loading changes.
- Check [opened pull requests](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pulls) ([non-dependabot PRs](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pulls?q=is%3Apr+is%3Aopen+-author%3Aapp%2Fdependabot))
- Discuss [new issues](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/issues?q=is%3Aopen+is%3Aissue+no%3Amilestone)
- Check  [discussions](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/discussions)
- Review [issues that should be assigned to the project](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/issues?q=is%3Aopen+is%3Aissue+no%3Aproject+milestone%3A1.13.0)
- Review [the project board](https://github.com/orgs/open-telemetry/projects/39)
