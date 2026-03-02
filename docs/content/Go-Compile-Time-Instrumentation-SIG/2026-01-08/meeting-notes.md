## Meeting Notes

### Attendees
- Przemek Delewski (Quesma)
- Huxing Zhang(Alibaba); **Facilitator**
- Yang Yi(Alibaba)
- Haibin Zhang(Alibaba)
- Dario Castañé (Datadog)
- Xabier Martinez (Cabify)

### Agenda
- Instrumentation Model – Final Shape
- Desired structure of the instrumentation package
- Specification and lifecycle of a **Hook**
- How people will write, test, and document instrumentations
- Governance: process for external packages to be imported and used
- Instrumentations scope
- Priority libraries: **Redis, MySQL, Kafka, Kubernetes, etc.**
- Migration guidelines from Loongsuite and Orchestrion
- Possible alignment with **go-contrib** instrumentation
- Integration with the external instrumentation concept
- Tooling
- Lowering the barrier to entry / reducing friction
- YAML → Go and related tooling ideas
- Release Cadence
- Discuss proposal of monthly releases leading up to v1.0.0
