## Key Topics
- Discussion on profiling use cases and SDK implications, including support for async Profiler and JFR.
- The need for a profiling SDK and internal API for building data to be exported.
- Introduction of a rule-based sampler into the core Java agent distribution, addressing security concerns.
- Consideration of creating a project for version 3.0 and the status of existing PRs and issues.
- Discussion on the integration of declarative configuration and potential contributions for the micrometer bridge.

## Action Items
- Evaluate the support for async Profiler and JFR in the SDK and determine the necessary configurations.
- Create a separate module for the rule-based sampler to avoid security risks associated with arbitrary code execution.
- Establish a project for version 3.0 and clarify priorities for upcoming work.
- Investigate the feasibility of integrating the micrometer bridge into the project and address the public API surface.

## Participants
Trask Stalnaker, Jay DeLuca, Jason Plumb, Jonathan Halliday, Lauri Tulmin, John Watson, Peter Findeisen.
