## Meeting Notes

### Attendees
- Diego Hurtado
- Dylan Russell
- Riccardo Magliocchetti (Elastic)
- Aaron Abbott (Google)
- Keith Decker (Cisco/Splunk)
- Shuwen Pan (Cisco)
- Erdenesaikhan Tserendavga (Cisco/Splunk)
- Emídio (Independent)
- Pablo Collins (Cisco/Splunk)

### Agenda
- [Riccardo] 1.42.0 release issues:
  - [https://github.com/open-telemetry/opentelemetry-python/issues/5227](https://github.com/open-telemetry/opentelemetry-python/issues/5227)
  - With merge queues bump version in main PR ignores labels pointing to the right branch to test against
    - [aaron] should be fixed [https://github.com/open-telemetry/opentelemetry-python/blob/05ee71b223014c9a40acbacabb60328fd665b770/.github/workflows/ci.yml#L49-L50](https://github.com/open-telemetry/opentelemetry-python/blob/05ee71b223014c9a40acbacabb60328fd665b770/.github/workflows/ci.yml#L49-L50)
  - [RELEASING.md](http://RELEASING.md) needs to be updated wrt [CHANGELOG.md](http://CHANGELOG.md) changes, backports PR will require “Approve Public API check
    - [aaron] will update the docs
- [Riccardo] quick 1.42.x candidates:
  - 1.42.1 on its way with:
    - [https://github.com/open-telemetry/opentelemetry-python/issues/5240](https://github.com/open-telemetry/opentelemetry-python/issues/5240)
  - [https://github.com/open-telemetry/opentelemetry-python/issues/5231](https://github.com/open-telemetry/opentelemetry-python/issues/5231)
  - [https://github.com/open-telemetry/opentelemetry-python/issues/5235](https://github.com/open-telemetry/opentelemetry-python/issues/5235)
- [Diego] JSON HTTP exporter
  - [https://github.com/open-telemetry/opentelemetry-python/pull/5224](https://github.com/open-telemetry/opentelemetry-python/pull/5224)
  - Lukas is working on it
    - [https://github.com/open-telemetry/opentelemetry-python/pull/5051/](https://github.com/open-telemetry/opentelemetry-python/pull/5051/) (closed PR)
  - We need to improve the issue tracking for this:
    - [reopened] [Support JSON over HTTP in OTLP exporter · Issue #1003 · open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python/issues/1003)
- [Aaron] [https://github.com/open-telemetry/opentelemetry-python/issues/5240](https://github.com/open-telemetry/opentelemetry-python/issues/5240)
- [aaron] [https://github.com/open-telemetry/opentelemetry-python/pull/4863](https://github.com/open-telemetry/opentelemetry-python/pull/4863)
  - Should be ready to go
- [Leighton/Aaron] Add label for issues that are agreed upon
  - Seeing users sending PRs before there’s any feedback on the issues.
  - E.g. [Retry 413 / payload too large errors in OTLP batch exporter · Issue #4533 · open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python/issues/4533)
  - [riccardo] [contributing.md](http://contributing.md) file could use some updates.
    - It has too much stuff and contributors might skip it
    - Liudmila +1
      - AGENTS.md too
      - Copilot instructions can be updated for automated review feedback
      - Faster feedback
  - [aaron] semconv repo has a lot of automation for this [https://github.com/open-telemetry/semantic-conventions/blob/main/issue-management.md](https://github.com/open-telemetry/semantic-conventions/blob/main/issue-management.md)
    - We can reuse the labels maybe
- [Keith] Additional reviews on adding RetrievalInvocation to genai-utils [https://github.com/open-telemetry/opentelemetry-python-genai/pull/36](https://github.com/open-telemetry/opentelemetry-python-genai/pull/36)
