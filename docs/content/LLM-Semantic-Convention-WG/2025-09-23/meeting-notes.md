## Meeting Notes

### Attendees
- Liudmila Molkova (Grafana Labs)
- Xander Song (Arize AI)
- Aaron Abbott (Google)
- Keith Decker (Cisco/Splunk)
- Ridhima Satam (Cisco/Splunk)
- Pranay Prateek (SigNoz)
- Guangya Liu (IBM)
- Shuwen Pan (Cisco)
- Susan Chang (Elastic)
- Tao Chen (Microsoft)
- Bruno Baptista (IBM)
- Joshua Winerman (Cisco/Splunk)
- Tristan Sloughter (Groq)

### Agenda
- Triage
  - WG Project board: [https://github.com/orgs/open-telemetry/projects/82](https://github.com/orgs/open-telemetry/projects/82)
    - Please review embedding instr - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3461](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3461)
    - MCP
      - Let’s check if there is any update upstream
      - Liudmila to update PR and address new feedback
  - [everyone, 5 min]  Intro for new members
- Open PRs to review
  - [https://github.com/open-telemetry/semantic-conventions/pulls?q=is%3Apr+is%3Aopen+genai+label%3Aarea%3Agen-ai](https://github.com/open-telemetry/semantic-conventions/pulls?q=is%3Apr+is%3Aopen+genai+label%3Aarea%3Agen-ai)
  - [aaron] MultiModal types [https://github.com/open-telemetry/semantic-conventions/pull/2754](https://github.com/open-telemetry/semantic-conventions/pull/2754)
    - Let’s start with generic file and blob
    - Liudmila will check OpenAI instr and prototype images
    - We’ll see if this works for images based on prototyping
  - [keith] - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3768)
    - Do we need generators? Generators are expected to customize telemetry to backend needs
      - If the need is to convert to different conventions, let’s discuss why
    - Let’s discuss offline
- [5 min] Current state
- [aaron] can quickly show the uploader hooks
  - Upload hook using fsspec [https://github.com/open-telemetry/opentelemetry-python-contrib/blob/b232b9a298a31fa944beeef5232b64d473ea61c4/util/opentelemetry-util-genai/src/opentelemetry/util/genai/_fsspec_upload/fsspec_hook.py#L164-L173](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/b232b9a298a31fa944beeef5232b64d473ea61c4/util/opentelemetry-util-genai/src/opentelemetry/util/genai/_fsspec_upload/fsspec_hook.py#L164-L173)
  - What is the name [https://github.com/open-telemetry/opentelemetry-python-contrib/blob/b232b9a298a31fa944beeef5232b64d473ea61c4/util/opentelemetry-util-genai/src/opentelemetry/util/genai/upload_hook.py#L97C44-L97C75](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/b232b9a298a31fa944beeef5232b64d473ea61c4/util/opentelemetry-util-genai/src/opentelemetry/util/genai/upload_hook.py#L97C44-L97C75)
    - Can we do “enrichment hook”?
    - For HTTP it’s called “request_hook” and “response_hook” [link](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/b232b9a298a31fa944beeef5232b64d473ea61c4/instrumentation/opentelemetry-instrumentation-requests/src/opentelemetry/instrumentation/requests/__init__.py#L193-L194)
