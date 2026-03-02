## Meeting Notes

### Attendees
- [Zach Montoya](mailto:zach.montoya@datadoghq.com) (Datadog)
- Rajkumar Rangaraj (Microsoft)
- [Yevhenii Solomchenko](mailto:ysolomchenko@splunk.com) (Splunk)
- Chris Ventura (New Relic)

### Agenda
- File Based Configuration for Internal Logging ([PR #4574](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pull/4574))
  - Short-Term: We can continue to rely only on environment variables
  - Medium-Term: Needs more investigation / testing
    - One approach: Be able to read configuration in the profiler (may still need separate startup hook approach)
      - The AssemblyLoader is only needed for .net framework where the profiler is a requirement
      - The StartupHook may or may not have a profiler present
        - If profiler is present the logs could be directed to the profiler
        - If the profiler is not present we need a different solution for the logs
          - Lightweight potentially brittle yaml parser for the handful of settings that are necessary
            - Might have too many edge cases and be more difficult to maintain
          - Only support the environment variables in this scenario
          - Having logging in the startuphook disabled by default unless new environment variables specific to capturing these logs are configured
    - Include the full yaml library into the startup hook and get a better understanding of the side effects
      - For example, does it become too big to use as an embedded resource in the native library?
    - Create a separate assembly for the configuration, that can be dynamically loaded by the assemblyloader, the startuphook, and the main assembly
    - Have logging off by default for the assemblyloader and startuphook unless someone configures new environment variables for enabling log capture for those libraries.
- Check [opened pull requests](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pulls) ([non-dependabot PRs](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/pulls?q=is%3Apr+is%3Aopen+-author%3Aapp%2Fdependabot))
- Discuss [new issues](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/issues?q=is%3Aopen+is%3Aissue+no%3Amilestone)
- Check  [discussions](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/discussions)
- Review [issues that should be assigned to the project](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/issues?q=is%3Aopen+is%3Aissue+no%3Aproject+milestone%3A1.13.0)
- Review [the project board](https://github.com/orgs/open-telemetry/projects/39)
