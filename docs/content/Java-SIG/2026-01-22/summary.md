## Key Topics
- **Indie Migration**: Discussion on switching the default to use Invoke Dynamic (Indy) for instrumentations, with considerations on how it affects extensions and backward compatibility.
- **Shared Internal Code**: Proposal to eliminate shared internal code in OpenTelemetry Java, with strategies for managing dependencies and ensuring API stability.
- **Declarative Configuration**: Exploration of how distributions can interact with declarative configuration, particularly in relation to samplers and runtime configuration.
- **Profiling Proposal**: Review of a proposal to export metadata for profiling, including the potential need for native libraries and compatibility with different Java versions.

## Action Items
- Gather feedback on the proposed switch to Indy and its implications for extensions.
- Continue discussions on the elimination of shared internal code and finalize tactics for implementation.
- Develop a draft for how to handle declarative configuration in relation to custom implementations.
- Consider creating a Java prototype for the profiling proposal once the OTEP is approved.

## Participants
Gregor Zeitlinger, John Watson, Trask Stalnaker, Sylvain Juge, Jack Shirazi, Jason Plumb, Jonathan Halliday, Jack Berg, Lauri
