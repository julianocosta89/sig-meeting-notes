## Meeting Notes

### Attendees
- Aaron Abbott (Google)
- Sergey Sergeev (Cisco/Splunk)
- Dylan russell (google)
- Keith Decker (Cisco/Splunk)
- Michael He (AWS)
- Xander Song (Arize)
- Pavan (Cisco)
- Dat Ngo (Arize)
- Marcelo Trylesinski (Pydantic)
- Bruno Baptista (IBM)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
  - [everyone, 5 min]  Intro for new members
- Open PRs to review
  - Please review embedding instr - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3461](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3461)
  - Blob / file parts [https://github.com/open-telemetry/semantic-conventions/pull/2754](https://github.com/open-telemetry/semantic-conventions/pull/2754)
  - GenAI Utils Inference PR: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768)
- [Sergey, 5m] Instrumentation roadmap
  - Sergey to submit some issues to github tracker
- [Sergey, 5m] Util GenAI evolution
  - review use-cases [README.refactoring.emitters.demo-scenarios.md](https://github.com/zhirafovod/opentelemetry-python-contrib/blob/genai-utils-e2e-dev/util/opentelemetry-util-genai-dev/README.refactoring.emitters.demo-scenarios.md)
  - review another iteration of the architecture [README.architecture.packages.md](https://github.com/zhirafovod/opentelemetry-python-contrib/blob/genai-utils-e2e-dev/util/README.architecture.packages.md)
  - Action items - put the new to a doc
    - Requirements section
    - high-level structure/design
- [Michael, 5m] PR for loosening invoke agent spec to support internal/server span kind:
  - [https://github.com/open-telemetry/semantic-conventions/pull/2881](https://github.com/open-telemetry/semantic-conventions/pull/2881)
  - Please review!
