## Meeting Notes

### Attendees
- Sergey (Cisco/Splunk)
- Keith Decker (Cisco/Splunk)
- Ridhima Satam (Cisco/Splunk)
- Nagkumar Arkalgud (Microsoft)
- Erdenesaikhan Tserendavga (Cisco/Splunk)

### Agenda
- [Nagkumar] - ]Memory spec - [https://github.com/open-telemetry/semantic-conventions/pull/3250](https://github.com/open-telemetry/semantic-conventions/pull/3250)
  - Spec to review [https://github.com/nagkumar91/semantic-conventions/blob/proposal/genai-memory-ops/docs/gen-ai/non-normative/memory_implementation_gen_ai_spec.md](https://github.com/nagkumar91/semantic-conventions/blob/proposal/genai-memory-ops/docs/gen-ai/non-normative/memory_implementation_gen_ai_spec.md)
  - Josh to review for the differentiation of mem vs retrieval
- session.id vs gen_ai.conversation.id
  - Propagation cross-rpc on gen-ai instrumentation level or otel instrumentation level
  - Nagkumar to review how it is done in the microsoft instrumentation
    - Is session.id of gen_ai.conversation.id stamped on every child span?
    - Is it propagated cross-rpc (i.e. on the http/grpc transport or mce/a2a protocol level)
  - Pavan/Sergey to present utils-genai example
- (Surya) security telemetry examples for the spec [https://github.com/open-telemetry/semantic-conventions/pull/3233](https://github.com/open-telemetry/semantic-conventions/pull/3233)
  - The spec to review [https://github.com/nagkumar91/semantic-conventions/blob/gen-ai-security-guardian/docs/gen-ai/non-normative/security_implementation_gen_ai_spec.md](https://github.com/nagkumar91/semantic-conventions/blob/gen-ai-security-guardian/docs/gen-ai/non-normative/security_implementation_gen_ai_spec.md)
- (Surya) remote agents in Antropic - do we need to do “create_agent”
  - create_agents - is it only remote?
  - When calude code working on a code, it creates a code review agent
    - We need to understand how create_agent is useful comparing to invoke_agent
  - We may want to provide some examples around create_agent
  - Action items: Surya to write down some use cases and share in the channel
