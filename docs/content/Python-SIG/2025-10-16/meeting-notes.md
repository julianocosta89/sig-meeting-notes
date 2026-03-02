## Meeting Notes

### Attendees
      - Dylan russell (google)
      - Nagkumar Arkalgud (Microsoft)
      - Radhika Gupta (Microsoft)
      - Luke Zhang (AWS)
      - Aaron Abbott (Google)
      - Keith Decker (Cisco/Splunk)
      - Riccardo Magliocchetti (Elastic)
      - Hector Hernandez (Microsoft)

### Agenda
      - Riccardo: 1.38.0 / 0.59b0 is out!
      - The release was smooth at last!
      - ♥️
      - PR to not report version changes as breakages will remove last annoyance https://github.com/open-telemetry/opentelemetry-python/pull/4778
      - Riccardo: Log stabilization: https://github.com/open-telemetry/opentelemetry-python/issues/4750
      - @Hector what do we want to merge first? https://github.com/open-telemetry/opentelemetry-python/pull/4676 or https://github.com/open-telemetry/opentelemetry-python/pull/4647
      - Let’s start with 4676
      - Nagkumar: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3813 as opentelemetry-instrumentation-langchain-v2
      - Aaron: try to get in touch with galklm https://pypi.org/project/opentelemetry-instrumentation-langchain/#history
      - Riccardo: for the next instrumentation maybe try to sort it out ownership before merging the code in -contrib
      - Weaviate would be next
      - Implement filtering logic for min_severity and trace_based parameters by rads-1996 · Pull Request #4765 · open-telemetry/opentelemetry-python
      - Leighton: we should probably implement LoggerConfigurator
      - Also this not priority for log stabilization
      - Riccardo: I was looking at implementing TracerConfigurator
      - [Aditya] - Update opentelemetry-api and sem conv dependency versions in opentelemetry-instrumentation-langchain - https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation-genai/opentelemetry-instrumentation-langchain/pyproject.toml#L27
      - https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation-genai/opentelemetry-instrumentation-langchain/src/opentelemetry/instrumentation/langchain/__init__.py#L79
      - Can you add oldest and latest tests, as an example https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation-genai/opentelemetry-instrumentation-vertexai/tests/requirements.oldest.txt
      - https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation-genai/opentelemetry-instrumentation-vertexai/tests/requirements.latest.txt
      - [Keith] - PR for additional SemConv Attributes in GenAI Utils: https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3862
      - Aaron: is there any plan for any instrumentation to use them?
      - Keith: Langchain
      - [Luke] PR for Add OpenTelemetry instrumentation for Model Context Protocol (MCP) PR-3822
      - We have the same issue with Traceloop already owning this package name https://pypi.org/project/opentelemetry-instrumentation-mcp/
      - Aaron:
      - Please join GenAI WG
      - Could you please split the PR in smaller chunks?
      - [Aaron] Contrib package independent releases, could use some improvements
      - What approvals do we need for release PRs?
      - Everyone is OK with this, aaron to send a PR updating the releasing docs
      - [Luke] How to become approver etc.
      - https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md
      - Riccardo: more python excluded urls support for missing http instrumentations https://github.com/open-telemetry/opentelemetry-python-contrib/pulls?q=is%3Apr+is%3Aopen+urls+excluded+author%3Axrmx+
