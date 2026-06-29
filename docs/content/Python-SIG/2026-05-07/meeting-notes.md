## Meeting Notes

### Attendees
- Lukas Hering (Oracle)
- Aaron Abbott (Google)
- Riccardo Magliocchetti (Elastic)
- David Perez (Feather)
- Keith Decker (Cisco/Splunk)
- Jeff Luo (Google)
- Liudmila Molkova (Grafana Labs)
- Emídio Neto
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Ridhima Satam (Cisco/Splunk)
- Shuwen Pan (Cisco)
- Mike Goldsmith (Honeycomb)
- Leighton Chen (Microsoft)
- Josh Winerman (Cisco/Splunk)
- Surya Teja
- [https://github.com/orgs/open-telemetry/projects/88/views/1](https://github.com/orgs/open-telemetry/projects/88/views/1)
- Lukas - JSON Exporters + Prometheus Stabilization

### Agenda
- Riccardo: dependabot requirements broken after [https://github.com/open-telemetry/opentelemetry-python/pull/5142](https://github.com/open-telemetry/opentelemetry-python/pull/5142) , pip / uv is fine with that though. [Logs](https://github.com/open-telemetry/opentelemetry-python/actions/runs/25368454713/job/74385376366), tried to workaround but no joy [https://github.com/open-telemetry/opentelemetry-python/pull/5178](https://github.com/open-telemetry/opentelemetry-python/pull/5178)
  - Emidio: I can take a look
  - Aaron: does renovate handles it better?
    - Emidio: I think so, we have an issue, hadn’t time to look into that
- Riccardo: Emidio UP ruff rule bump for 3.10 baseline [https://github.com/open-telemetry/opentelemetry-python/pull/5133](https://github.com/open-telemetry/opentelemetry-python/pull/5133) , is it safe for downstream typecheckers? E.g. Typing -> collections.abc
  - Emidio: can write a POC
- Riccardo: use docker from the system in docker-tests, any drawback? This will unblock to upgrade some requirements like requests and drop a bunch of dependencies [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4477](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/4477)
  - [https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3187](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/3187)
  - Emidio: install everything using a Dockerfile and run tests from there
- Lukas: Questions around exporter <-> SDK dependencies [https://github.com/open-telemetry/opentelemetry-python/pull/5151](https://github.com/open-telemetry/opentelemetry-python/pull/5151)
  - Leighton: we would like to let users use the version of the sdk they prefer
  - Aaron: rely on semantic versioning and consider stable what is de-facto stable
- Ridhima: asking for reviews on langchain workflow and invoke agent support [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4449](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4449)
- Aaron: [https://github.com/open-telemetry/opentelemetry-python/pull/4917](https://github.com/open-telemetry/opentelemetry-python/pull/4917)
  - [https://github.com/open-telemetry/opentelemetry-python/issues/4904#issuecomment-4398690384](https://github.com/open-telemetry/opentelemetry-python/issues/4904#issuecomment-4398690384)
- Aaron: [https://github.com/open-telemetry/opentelemetry-python/pull/4854](https://github.com/open-telemetry/opentelemetry-python/pull/4854)
  - [https://github.com/w3c/trace-context/issues/579](https://github.com/w3c/trace-context/issues/579)
- [Liudmila] genai repo
  - Should we move on [https://github.com/lmolkova/opentelemetry-python-genai/](https://github.com/lmolkova/opentelemetry-python-genai/) and iterate?
  - What do we do with PRs open now
    - Merge what's almost ready
    - Once new repo is out (synced with python-contrib), ask pr authors to come to the new repo
- [Tammy] Ptal at this Labeler PR with some approvals already [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4288/](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4288/)
  - [https://github.com/open-telemetry/opentelemetry-specification/pull/4931](https://github.com/open-telemetry/opentelemetry-specification/pull/4931)
