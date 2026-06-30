## Meeting Notes

### Attendees
- Keith Decker (Cisco/Splunk)
- Radhika Gupta (Microsoft)
- Dylan Russell (google)
- Leighton Chen (Microsoft)
- Riccardo Magliocchetti (Elastic)
- Nagkumar Arkalgud (Microsoft)
- John Scancella
- Aaron Abbott (Google)
- Shuwen Pan (Cisco)

### Agenda
- Nagkumar Arkalgud - Opentelemetry-instrumentation-openai-agents - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3762](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3762)
  - Should this be a separate package?
    - Leighton: looks good
  - Still using the Events API:
    - Please use logs
- [Fixup LogRecord.emit signature by xrmx · Pull Request #4737 · open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python/pull/4737)
- Riccardo: LogRecord warnings on not using context are too annoying [https://github.com/open-telemetry/opentelemetry-python/pull/4762](https://github.com/open-telemetry/opentelemetry-python/pull/4762)
- Keith - GenAI Utils PR Review: [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768)
- Dylan: [https://github.com/open-telemetry/opentelemetry-python/pull/4760](https://github.com/open-telemetry/opentelemetry-python/pull/4760) - small PR for otlp auth
- Sergey: overview of [https://github.com/zhirafovod/opentelemetry-python-contrib/tree/genai-utils-e2e-dev/util/opentelemetry-util-genai-dev](https://github.com/zhirafovod/opentelemetry-python-contrib/tree/genai-utils-e2e-dev/util/opentelemetry-util-genai-dev)
  - What do you think of the approach of converting the emitted traceloop instrumentation?
- Dylan: FYI plan to move the GCP resource detector into -contrib
