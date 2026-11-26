## Meeting Notes

### Attendees
- Marc Pichler (Dynatrace)
- Trent Mick (Elastic)
- Marylia (Grafana Labs)
- Pranav Sharma (Google)
- Jared Freeze (Palo Alto Networks)
- Jackson Weber (Microsoft)

### Agenda
- Feel free to add your topics below ↙️ 🙂
- [marc] do we want this? [https://github.com/open-telemetry/opentelemetry-js/issues/7326](https://github.com/open-telemetry/opentelemetry-js/issues/7326)
  - I think we should not add this as disabling already registered SDKs is not specified - shutdown is the way to go.
    - [trent] agreed on *not* adding this. Perhaps at most mention in README docs how to undo.
  - For re-configuration, I think we’d want to implement that in SDK components directly, rather than work around with re-registering new SDKs
  - [trent] Hrm, lambda having moved to `new NodeSDK` so near when I’d like to switch to `startNodeSdk()` is perhaps unfortunate. I haven’t looked closely. IIRC, earlier lambda-nodejs work had intentionally not used, at least, auto-instrumentations-node, and was *bundling* the SDK bootstrap for faster Lambda cold start times.
- [marylia] OTel Unplugged Feb 1st 2027, Brussels: [https://events.humanitix.com/otel-unplugged-2027](https://events.humanitix.com/otel-unplugged-2027)
- [marylia] FYI, break end of the year:  2 last weeks with no meetings
  - [marc] 🎉
- [marylia] considering changing meeting times to 30min, how people feel about that?
- [trent] Promoting `startNodeSdk()` in sdk-node: Thoughts on not [re-documenting every option in the README](https://github.com/open-telemetry/opentelemetry-js/blob/main/experimental/packages/opentelemetry-sdk-node/README.md#configuration)? For example `views` there is currently out of date. I don’t object to dropping in the current accurate doc for each option… or could instead refer to the TypeScript type and document a subset of interesting ones.
  - [marc] probably linking to the API docs page is fine: [https://open-telemetry.github.io/opentelemetry-js/functions/_opentelemetry_sdk-node.startNodeSdk.html](https://open-telemetry.github.io/opentelemetry-js/functions/_opentelemetry_sdk-node.startNodeSdk.html) (not sure why the current options type is not there, maybe needs some config)
- [trent] PTAL at PRs for declarative config and `startNodeSdk()` getting over the line
  - (Ah, I see Marc added some reviews just now that I haven’t read yet. :) )
  - [https://github.com/open-telemetry/opentelemetry-js/pull/7352](https://github.com/open-telemetry/opentelemetry-js/pull/7352) custom component providers
  - customConfig option for distros to use: [https://github.com/open-telemetry/opentelemetry-js/pull/7375](https://github.com/open-telemetry/opentelemetry-js/pull/7375)
  - A coming PR to document `startNodeSdk()` in the README
  - A draft PR (until we have a release of the above) to have auto-instr-node use startNodeSdk: [https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3924](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3924)
- [Untriaged bugs](https://github.com/open-telemetry/opentelemetry-js/issues?q=is%3Aissue+is%3Aopen+label%3Atriage+label%3Abug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4+)
- [Untriaged contrib bugs](https://github.com/open-telemetry/opentelemetry-js-contrib/issues?q=is%3Aissue+is%3Aopen+label%3Atriage%2Cbug+-label%3Apriority%3Ap1++-label%3Apriority%3Ap2++-label%3Apriority%3Ap3++-label%3Apriority%3Ap4)
- [Old Contrib PR Triage](https://github.com/open-telemetry/opentelemetry-js-contrib/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
- [Old Core PR Triage](https://github.com/open-telemetry/opentelemetry-js/pulls?q=is%3Apr+is%3Aopen+sort%3Acreated-asc)
