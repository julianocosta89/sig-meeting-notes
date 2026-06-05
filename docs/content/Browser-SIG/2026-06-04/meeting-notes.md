## Meeting Notes

### Attendees
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- David Luna (Elastic)
- Martin Kuba (Grafana Labs)
- Maxime Quentin (Datadog)

### Agenda
- [david] new sdk-trace package in the PR list. Plan is to deprecate others
  - I think Trent needs input in [https://github.com/open-telemetry/opentelemetry-js/pull/6775/changes/BASE..feeaf93a9983dc67d6fd1ec0c3bcfc41c3a28983#r3342830171](https://github.com/open-telemetry/opentelemetry-js/pull/6775/changes/BASE..feeaf93a9983dc67d6fd1ec0c3bcfc41c3a28983#r3342830171)
- [david] Browser SDK
  - Decide package/folder name [https://github.com/open-telemetry/opentelemetry-browser/pull/288#issuecomment-4618798562](https://github.com/open-telemetry/opentelemetry-browser/pull/288#issuecomment-4618798562)
  - Processors. Should the processor config option remove the default or append?
    - [https://github.com/open-telemetry/opentelemetry-browser/pull/288/changes/BASE..0e5ae83bcb8f9b07846a20edd27d01a3c3d12c3a#r3318291251](https://github.com/open-telemetry/opentelemetry-browser/pull/288/changes/BASE..0e5ae83bcb8f9b07846a20edd27d01a3c3d12c3a#r3318291251)
    - yes/no
    - Alternative: if we have user defined processors. Append the Batch*Processor to the list only if exportConfig is set explicitly in the options param.
    - **Proposal:** provide different top level functions with easier/smaller config options
- [Joaquin] fetch instrumentation migration
  - Decide what we want to do with resource timing, include in the fetch instrumentation or new instrumentation?
