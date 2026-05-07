## Key Topics
- Discussion on adding new configuration options to Contrib components and the need for a policy to ensure consistency with core repo practices.
- Proposal for a "kitchen sink" example for instrumentation options, including challenges related to documenting default values and examples.
- Review of a PR addressing performance improvements for metric recording under contention, with considerations for potential trade-offs in single-threaded scenarios.
- Consideration of splitting the OKHTTP sender into separate versions for v4 and v5 to mitigate dependency resolution issues.
- Discussion on the complexity of concurrency and contention in OpenTelemetry metrics, including potential strategies for optimizing performance.

## Action Items
- Document the policy that declarative configuration should be a strict superset of system properties and environment variables.
- Explore the idea of generating a "kitchen sink" example with commented-out configurations and snippets for better user guidance.
- Investigate the feasibility of introducing a system property to toggle between performance modes in the metrics SDK.
- Follow up on the OKHTTP sender PR and gather more user feedback regarding the need for separate implementations.

## Participants
Trask Stalnaker, John Watson, Jack Berg, Chas, Jay DeLuca, Sylvain Juge, Pranav Sharma, Lauri
