## Meeting Notes

### Attendees
- Josh Suereth
- Dotan Horovits
- Trask Stalnaker
- Joao Grassi (Dynatrace)

### Agenda
- Calendar confusion - We need to make sure both calendar invites are on the "global" otel calendar vs. the specific entity calendar entry.
- [suereth] Formalizing "Service" entities - [https://github.com/open-telemetry/semantic-conventions/pull/2963](https://github.com/open-telemetry/semantic-conventions/pull/2963)
  - Previously:
    - Service Namespace -> Service -> Service Instance
  - Thoughts
  - Application -> Service -> Instance?
  - <other term> -> Service -> Instance
  - Discussion
    - Focus that a service is a logical entity, an instance is not - it's an actual thing
    - Namespace is used in kubernetes and may confuse
      - Is a K8s service / namespace the same or different than service.namespace / service.name?
      - Should systems running in k8s default service.namespace to be k8s.namespace and k8s.deployment -> service.name >
    - Concern -
      - Service + Namespace are *logical* but you can't see it tangibly somewhere, but Instance is more physical.
    - Looking at [https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/)
      - This looks to match our definition
    - ISTIO adds "canonical" service name in OTEL instrumentation - may use this instead of default service name.
    - What is a "prototype" for service here?https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/
