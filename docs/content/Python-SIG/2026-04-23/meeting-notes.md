## Meeting Notes

### Attendees
- Diego Hurtado
- Jayesh Hire
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Mike Goldsmith (Honeycomb)
- Riccardo Magliocchetti (Elastic)
- Jeff Luo (Google)
- Shuwen Pan (Cisco)
- Lukas Hering (Oracle)
- Surya Teja
- Keith Decker (Cisco/Splunk)
- Leighton Chen (Microsoft)
- Aaron Abbott (Google)
- Tammy Baylis (SolarWinds)
- https://github.com/orgs/open-telemetry/projects/88/views/1
  - Riccardo: added ready for merge column, to be used by maintainers; testing if it’s useful
- Mike - Declarative config, this PR is foundation for others, already approved, I think it’s ready to merge
  - https://github.com/open-telemetry/opentelemetry-python/pull/5131
- Surya - Working on adding a github actions job to label gen-ai prs.
- Lukas - JSON OTLP Exporters + Prometheus Exporter changes. This PR is ready to Merge:
  - https://github.com/open-telemetry/opentelemetry-python/pull/4996
- Tammy - DB instrumentation semconv stabilization
  - Redis (I have to make changes): https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4370/
  - “Everything else” e.g. postgres, mysql (Ready): https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4109/

### Agenda
- [Jayesh] I am trying to implement the Flake8-Simplify rule for ruff. But some of those rules will add more restrictions in terms of the kind of code that will be accepted. So, before I make changes for the rules, I want other contributors opinions on these rules. Please refer to the below doc which I have prepared and add your comments there about the mentioned rules. Implementing flake8-simplify(SIM) plugin rules
  - Riccardo: let’s merge current PRs before opening one
- [Jeff]https://opentelemetry.io/blog/2025/stability-proposal-announcement/#1-stable-by-default the repo (https://github.com/open-telemetry/opentelemetry-python-contrib) has no stable library, what’s the plan to mark libraries as stable? (e.g., HTTP library)
  - Aaron: we haven’t started the work yet
  - Leighton: we should find a subset of instrumentations that are stable
  - Liudmila: stable by default OTEP has not been merged yet
      - Java: the agent is stable, feature that may be breaking under feature flag, they cut a major release for breaking changes (including default semantic conventions)
  - Leighton: we are missing guidelines / framework for handling this
  - Aaron: two places to touch: bootstrap and opentelemetry-instrumentations (the one that install all instrumentations) package
  - Lukas: is this only about the instrumentations? We have in development sdk health metrics. We may need feature flags
  - Liudmila: should read the OTEP and comment from a Python POV https://github.com/open-telemetry/opentelemetry-specification/pull/4813
      - Leighton and Riccardo will take a look
  - Aaron: do we need stable semconv for having instrumentations marked stable?
      - Liudmila: for a purist approach: no, better put unstable stuff under a feature flag
- [Erden] Requesting review and merge PR related to AgentInvocation https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4274
- [Surya] Need some reviews on gen-ai prs from gen-ai folks:
- Lukas: let’s keep the instrumentations lean and evaluate the value brought by instrumentations dependencies
- [Liudmila]  https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4457
