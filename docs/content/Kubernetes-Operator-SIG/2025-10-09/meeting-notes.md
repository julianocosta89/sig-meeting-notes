## Meeting Notes

### Attendees
- Jacob Aronoff
- Timo Johner (SAP)
- David Ashpole (Google)
- Yuri Oliveira (OllyGarden)
- Pavol Loffay (Red Hat)

### Agenda
- [dashpole] I’m your new TC liaison!
- Adding spec.HostPID for all collector modes PR [#4280](https://github.com/open-telemetry/opentelemetry-operator/pull/4280) (picking up from 28th Aug)
  - [Elastic may have something to say about this?](https://www.elastic.co/docs/reference/security/prebuilt-rules/rules/integrations/kubernetes/privilege_escalation_pod_created_with_hostpid)
  - [Privileged: true](https://pkg.go.dev/k8s.io/api/core/v1#SecurityContext.Privileged)
  - Is there a way to get the audit logs without setting the hostPID: true? Or do it with the security context?
- [all] [Issues to discuss at sig](https://github.com/open-telemetry/opentelemetry-operator/issues?q=is:issue+is:open+label:discuss-at-sig) (always last)
