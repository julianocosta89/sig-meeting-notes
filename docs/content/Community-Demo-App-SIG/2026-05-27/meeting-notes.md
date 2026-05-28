## Meeting Notes

### Attendees
- [Juliano Costa](mailto:juliano.costa@datadoghq.com)(Datadog)
- [Pierre Tessier](mailto:pierre@resolve.ai)(Resolve)
- Shenoy Pratik (OpenSearch)
- Jonathan Munz (Embrace)

### Agenda
- Given the breaking changes introduced with the new layered Docker compose files, attribute renames, and new services, the table listing Repository forks will be updated to only include “Active” repository forks. We will create a tracking issue and tag all fork codeowners, providing them 60 days to validate they have updated their fork.
- Telemetry tests: [https://github.com/open-telemetry/opentelemetry-demo/pull/3356](https://github.com/open-telemetry/opentelemetry-demo/pull/3356)
  - Looks to be ready. Take 1 more pass with target to merge by Friday May 29
  - Remove Tracetest stuff - will be in another PR as  a follow up
    - Also link on the main README
    - Update [design.md](http://design.md) to README
    - Update the README tag for CI
    - On pull request approve - run the tests + if the PR is from dependabot
- Tasks to 3.0
  - Bump dependencies
  - Update Grafana dashboards to cover attributes with the new naming `demo`.
  - Agentic Demo
    - [https://github.com/open-telemetry/opentelemetry-demo/pull/3148](https://github.com/open-telemetry/opentelemetry-demo/pull/3148)
  - Helm updates
  - Blog post announcing new release
