## Key Topics
- Improvements in build times for OpenTelemetry Android SDK.
- Discussion on the ability to shut down and restart the span processor.
- Need for supporting multiple RUM (Real User Monitoring) instances and changing API tokens/endpoints dynamically.
- Exploration of using supplier patterns for dynamic configuration changes.
- Consideration of technical limitations versus conceptual design decisions regarding SDK reinitialization.

## Action Items
- Investigate the feasibility of supporting the shutdown and restart of the span processor.
- Explore the implementation of a delegating exporter for easier dynamic configuration.
- Consider providing examples or documentation on using supplier patterns for API tokens and endpoints.

## Participants
Jason Plumb, Hanson Ho, Cesar Munoz, Mustafa Haddara, Cleverchuk
