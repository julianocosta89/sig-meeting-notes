## Key Topics
- **KubeCon Talk Feedback**: Discussion on the recent KubeCon talk and the surprising level of interest and questions received.
- **Configuration Stabilization**: Ongoing issues regarding the stabilization of Prometheus Receiver configuration and its implications for the target allocator.
- **Target Allocator Feature Flag**: Concerns about the readiness of the TLS feature in the target allocator and its potential impact on users.
- **Instrumentation V1 Beta 1**: Plans to align the instrumentation CR with the SDK config and discussions on the upcoming injector's impact on the operator.
- **Versioning and Migration Strategies**: Strategies for handling breaking changes in instrumentation versions and how to manage user migrations effectively.

## Action Items
- Review the target allocator configuration for potential backward-incompatible changes.
- Open an issue regarding the semantic convention changes and how they will be handled in future versions.
- Discuss the implications of the new injector and how it will affect the operator's codebase.
- Plan for a migration strategy for users transitioning from annotations to labels in the instrumentation CR.

## Participants
Mikołaj Świątek, Joe Sirianni, David Ashpole, Benedikt Bongartz, PL Pavol Loffay, jea
