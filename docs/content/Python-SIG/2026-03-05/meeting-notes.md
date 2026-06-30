## Meeting Notes

### Attendees
- …
- Dylan russell (google)
- Keith Decker (Cisco/Splunk)
- Aaron Abbott (Google)
- Mike Goldsmith (Honeycomb)
- Paulo Vital (IBM)
- Surya Teja
- Riccardo Magliocchetti (Elastic)
- Lukas Hering (Capital One)
- Tammy Baylis (SolarWinds)
- Shuning Chen (Cisco/Splunk)
- Nagkumar Arkalgud (Microsoft)
- Josh Winerman (Cisco/Splunk)
- Pablo Collins (Cisco/Splunk)
- Ridhima Satam (Cisco/Splunk)

### Agenda
- Riccardo: 1.40.0 is out
  - 2+ months of work including moving of LoggingHandler in logging instrumentation
  - Hiccup in the release process:
    - Some genai instrumentations not excluded from packages to release: easy to fix but found only in review  [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4301](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4301)
  - After release some CI issues [https://github.com/open-telemetry/opentelemetry-python/actions/runs/22674628343/job/65732801711?pr=4938](https://github.com/open-telemetry/opentelemetry-python/actions/runs/22674628343/job/65732801711?pr=4938)
    - I guess fixed after a newer commit on -contrib main
- [Josh] convo on log handler config in autoinstrumentation
  - Current WIP PR: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4298](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4298)
  - Open issue in core: [https://github.com/open-telemetry/opentelemetry-python/issues/4034](https://github.com/open-telemetry/opentelemetry-python/issues/4034)
  - Related PRs to log configuration [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4204](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4204)
- [Surya] Adding [skills.md](http://skills.md) for verifying the accuracy otel span attributes with Copilot
  - Aaron: there were other experiments with using weaver
  - Could enable [https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
    - Surya: will dig more and I’ll open a PR
      - Aaron: ask Trask if you need something around this
- [Surya] Review on these two prs
- Aaron: will merge after CI pass
- [Shuning]Review on Embedding PR [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4219](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4219)
- [Keith] Review on ToolCall Type PR: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4218](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4218)
- [Lukas] Reminder for reviews on following PRs:
  - [https://github.com/open-telemetry/opentelemetry-python/pull/4910](https://github.com/open-telemetry/opentelemetry-python/pull/4910)
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4216](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4216)
