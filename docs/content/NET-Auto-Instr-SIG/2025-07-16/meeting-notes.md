## Meeting Notes

### Attendees
- [Piotr Kiełkowicz](mailto:pkiekowicz@splunk.com) (Splunk)
- [Zach Montoya](mailto:zach.montoya@datadoghq.com) (Datadog)
- Yevhenii Solomchenko (Splunk)
- [Mateusz Lach](mailto:mateusza@splunk.com) (Splunk)
- Chris Ventura (New Relic)
- Matthew Hensley (Grafana Labs)

### Agenda
- [https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/issues/4186](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/issues/4186)
- File-based configuration discussion
  - Talked about building the prototype implementation either in the auto-instrumentation repo, sdk repo, or vendor-specific repo.
    - The eventual plan is to get the final implementation in one of the sdk repos
    - We are ok with the prototype being developed in the auto-instrumentation repo
      - Concerns
        - [ ] How many bigger changes will be necessary to get the final implementation in an SDK repo?
        - [ ] Will the final implementation have big deviations from what the auto-instrumentation repo needs?
      - Positives
        - [ ] We can ensure that the dependencies of this implementation are reasonable for usage within auto-instrumentation
- Check [opened pull requests](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pulls) ([non-dependabot PRs](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pulls?q=is%3Apr+is%3Aopen+-author%3Aapp%2Fdependabot))
- Discuss [new issues](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/issues?q=is%3Aopen+is%3Aissue+no%3Amilestone)
- Check  [discussions](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/discussions)
- Review [issues that should be assigned to the project](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/issues?q=is%3Aopen+is%3Aissue+no%3Aproject+milestone%3A1.13.0)
- Review [the project board](https://github.com/orgs/open-telemetry/projects/39)
