## Key Topics
- Discussion on dropping support for the old `bottle` instrumentation due to lack of users.
- Introduction of a basic OpenTelemetry Management Protocol (OPMP) client, with ongoing development and testing.
- Consideration of supporting Protobuf 6, including options to relax dependencies or focus solely on version 6.
- Discussion on the potential need for different versions of exporters as Protobuf versions evolve.

## Action Items
- Create an issue to formally drop the `bottle` instrumentation from CI.
- Review the draft PR for the OPMP client once it's ready.
- Test compatibility with Protobuf 6 and relax the dependency as a short-term solution.
- Update the issue regarding Protobuf support with the discussed points.

## Participants
Riccardo Magliocchetti, Tammy Baylis, Ezio Moreira, Dan Gomez Blanco, Emídio, Le Chen
