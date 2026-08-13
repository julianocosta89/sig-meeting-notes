## Meeting Notes

### Attendees
- Trent Mick (Elastic)
- Abhinav Mathur ( Splunk )
- Jamie Danielson (Honeycomb)
- Jackson Weber (Microsoft)
- Matt Wear (Dash0)
- Marylia (Grafana)
- Pranav Sharma (Google)
- Raphaël Thériault (SolarWinds)

### Agenda
- **Feel free to add your topics below ↙️ 🙂**
- [trent] contrib P1: [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3653#pullrequestreview-4910843755](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3653#pullrequestreview-4910843755)
  - Looking for browser eyes, approved and merged
- [marylia] need someone to collaborate to create/update documentation on [otel.io](http://otel.io) to test new flow ([https://github.com/open-telemetry/opentelemetry.io/issues/10972](https://github.com/open-telemetry/opentelemetry.io/issues/10972) )
  - Trent has volunteered as tribute
  - Tldr changes to public docs on javascript content can be approved and merged by javascript approver (not required to have docs maintainer to merge)
- [trent] Other reviews on an instr-http P1 would be welcome: [https://github.com/open-telemetry/opentelemetry-js/pull/6969](https://github.com/open-telemetry/opentelemetry-js/pull/6969)
- [pranav] OpenInference GenAI instrumentation donation  - JS port
  - [https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3668](https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3668)
  - Anthropic instrumentation pr [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3664](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3664)
  - For semconv follow guidance ot directly import stable semconv, use a local hardcoded file for experimental semconv
  - No genai semconv released yet.
- [abhinav] [https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3563](https://github.com/open-telemetry/opentelemetry-js-contrib/issues/3563)
  - Assigned to work on microservice support, take guidance from the initial PR that has some comments
- [mwear] PTAL: [https://github.com/open-telemetry/opentelemetry-js/pull/6868](https://github.com/open-telemetry/opentelemetry-js/pull/6868)
- [trent] Discuss SDK resource creation:
  - The spec has (in "Development") some reserved detector names that overlap in name and meaning with detectors in the stable `@opentelemetry/resources` package (and, FWIW, in the OTel Java equivalent) and names used by `OTEL_NODE_RESOURCE_DETECTORS`
  - "host" maps to `OTEL_NODE_RESOURCE_DETECTORS=host,os`
  - "service" cannot be mapped exactly: it is our "serviceinstance" detector and *part* of our "env" detector
  - Setting `service.name` when using NodeSDK, in order of prio (highest first):
    - 1. `opts.serviceName` to `new NodeSDK(opts)`
    - 2. `OTEL_SERVICE_NAME` if "env" detector enabled (or "service" detector in spec naming)
    - 3. `OTEL_RESOURCE_ATTRIBUTES` if "env" detector (or MUST, always, in spec)
    - 4. `opts.resource` to `new NodeSDK(opts)`
    - 5. the required fallback `unknown_service:...` (via `defaultResource()`)
  - Example declarative config “resource:” section: [https://gist.github.com/trentm/44cb6a5804215a98f7911833624dcd08](https://gist.github.com/trentm/44cb6a5804215a98f7911833624dcd08)
  - Related issues:
    - Jackson's PR: [https://github.com/open-telemetry/opentelemetry-js/pull/6988#discussion_r3753565518](https://github.com/open-telemetry/opentelemetry-js/pull/6988#discussion_r3753565518)
    - Trent's PR: [https://github.com/open-telemetry/opentelemetry-js/pull/6989](https://github.com/open-telemetry/opentelemetry-js/pull/6989)
    - [https://github.com/open-telemetry/opentelemetry-js/issues/6488](https://github.com/open-telemetry/opentelemetry-js/issues/6488)
  - Currently: Jackson’s PR has the breaking change on resources. We may want that for SDK 3.0. Trent’s PR is non-breaking and may happen first, with Jackson’s as the followup later in 3.0. Generally both need review and opinions.
  - [https://github.com/orgs/open-telemetry/projects/157](https://github.com/orgs/open-telemetry/projects/157) is the project board for declarative config in JS
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [SDK 3.0 Milestone Triage and Refinement](https://github.com/open-telemetry/opentelemetry-js/milestone/20)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
