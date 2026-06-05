## Meeting Notes

### Attendees
- Diego Hurtado
- Tammy Baylis (SolarWinds)
- Mike Goldsmith (Honeycomb)
- Lukas Hering (Oracle)
- Aaron Abbott (Google)
- Gregory Loshkajian (Bloomberg)
- Keith Decker (Cisco/Splunk)
- Pablo Collins (Cisco)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Leighton Chen (Microsoft)
- Shuwen Pan (Cisco)
- [https://github.com/orgs/open-telemetry/projects/88/views/1](https://github.com/orgs/open-telemetry/projects/88/views/1)
- [Dylan] Extended Attributes
- [Lukas] JSON Exporters work
- [Mike] Declarative config – nearly there 🎉

### Agenda
- [Leighton] Deprecating http old semantic conventions and making new ones default - [Implement migration plan for selected instrumentations · Issue #2453 · open-telemetry/opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/2453)
- [Lukas] “[service.instance.id](http://service.instance.id)” Resource attribute [https://github.com/open-telemetry/opentelemetry-python/issues/5257](https://github.com/open-telemetry/opentelemetry-python/issues/5257)
  - [aaron] awesome thank you for sending this
  - [lukas] it’s stable already
  - Declarative config has its own impl. We can use this new PR’s impl to consolidate.
  - Config spec issue that describes where / how resource detectors, including resource ID - [https://github.com/open-telemetry/opentelemetry-configuration/issues/570](https://github.com/open-telemetry/opentelemetry-configuration/issues/570)
- [Lukas] Patch release for this PR? [https://github.com/open-telemetry/opentelemetry-python/pull/5250](https://github.com/open-telemetry/opentelemetry-python/pull/5250)
- [Mike] Are merge ques meant to accept changes without a maintainer?
  - This PR has 3 approvals from approvers, no maintainers
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5272](https://github.com/open-telemetry/opentelemetry-python/pull/5272)
- [Lukas] Reminder on Prometheus exporter stabilization PRs, importantly: [https://github.com/open-telemetry/opentelemetry-python/pull/5123](https://github.com/open-telemetry/opentelemetry-python/pull/5123)
- [Gregory] [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4635](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4635) new contributor, wanted to ask if I can work on this, anything I should be aware of?
  - Native instrumentation would be preferable. Is Pydantic open to that? Started discussion [here](https://github.com/pydantic/httpx2/discussions/1024).
  - If not, implementation as an extension to httpx-instrumentor would be preferred, prior art for aiobotocore.
- [Surya] Can we release the final version of gen-ai libraries to PYPI with a note to the new github repo?
  - [liudmila] can we remove the package code which were never released?
    - Anthropic, claude agents, langchain
    - We did release openai-v2 and <something else>. For these we need to first release the new version with new name, then we can deprecate it in the old repo
  - Riccardo’s feedback was to do all at once
  - Decision, once we release from new repo,
    - Release one more time contrib so the deprecation notices go to PyPI
    - Then Surya to send a PR to remove from contrib.
