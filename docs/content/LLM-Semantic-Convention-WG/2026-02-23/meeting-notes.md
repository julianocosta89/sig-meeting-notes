## Meeting Notes

### Attendees
- Sergey Sergeev (Cisco/Splunk)
- Wolfgang Therrien (Honeycomb.io)
- Keith Decker (Cisco/Splunk)
- Josh Winerman (Cisco/Splunk)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Dakota Paasman (Bindplane)
- Ridhima Satam (Cisco/Splunk)
- Shuwen Pan (Cisco)
- Nagkumar Arkalgud (Microsoft)
- Ricardo Pesciotta

### Agenda
- [Nagkumar, 3 mins]: Security Spec: [https://github.com/open-telemetry/semantic-conventions	/pull/3233](https://github.com/open-telemetry/semantic-conventions/pull/3233)
  - Aditiya to review/comment/approve it
  - Double-check that Cisco AI Defense adopted this convention
- [Nagkumar, 3 mins]: Memory Spec [https://github.com/open-telemetry/semantic-conventions/pull/3250](https://github.com/open-telemetry/semantic-conventions/pull/3250)
  - Josh to review/comment/approve on this how it is different from the Retrieval Span.
- [Sergey] Long running agents
  - i.e. co-pilot, etc.
- [Sergey] multi-agent protocols
  - Do we see any traction beyond MCP in real use?
  - Nagkumar to check with the broader Microsoft groups
- [Pradeep] Planner/Planning step
  - Planner is specific for some AI Agent frameworks
    - Lifecycle memory
  - Plan may be a type of memory
  - Is a planner the same as an “orchestrator” agent?
  - Is a plan a deterministic workflow or a prompt for the agent
  - An agent creates an initial plan and then improves it during the execution. So monitoring efficiency of the original plan may be helpful
  - What are the use cases for this telemetry?
