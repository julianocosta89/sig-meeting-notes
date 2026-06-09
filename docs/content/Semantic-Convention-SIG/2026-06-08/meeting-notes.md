## Meeting Notes

### Attendees
- Josh Suereth (Google)
- Sven Cowart (ElastiFlow)
- Liudmila Molkova (Google)
- Armin Ruech (Dynatrace) [first 40mins]
- Russ Trow (Green Software Foundation)
- Jamie Cowan (Green Software Foundation)
- Sarah Hsu (Goldman Sachs)
- Christophe Kamphaus

### Agenda
- (timebox 7 min) Project Status + Triage + Blockers
  - Stability Blockers
  - PR Triage Board: [https://github.com/orgs/open-telemetry/proje](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - [cts/67/views/1](https://github.com/orgs/open-telemetry/projects/67/views/1)
  - Issue Triage Board: [https://github.com/orgs/open-telemetry/projects/131/views/1](https://github.com/orgs/open-telemetry/projects/131/views/1)
- (timebox 50 min) General topics
  - [Sylvain Juge], not sure I can attend, could be postponed if I’m not here
    - Http request/response body capture attributes: [https://github.com/open-telemetry/semantic-conventions/pull/3521](https://github.com/open-telemetry/semantic-conventions/pull/3521)
  - [christos] Suggesting a new release: [https://cloud-native.slack.com/archives/C041APFBYQP/p1780398977228919?thread_ts=1777283393.988019&cid=C041APFBYQP](https://cloud-native.slack.com/archives/C041APFBYQP/p1780398977228919?thread_ts=1777283393.988019&cid=C041APFBYQP)
    - "Fun" for people who generate semconv
    - Deprecated GenAI attributes and they are now in separate repository
    - Code generation will not be broken BUT if you want to use GenAI semconv you need to create *new* code-generation.  Guidance is TBD.
      - AI: Make sure release notes call this out.
- New working group: [https://github.com/open-telemetry/semantic-conventions/issues/3769](https://github.com/open-telemetry/semantic-conventions/issues/3769)
  - what else needs to happen?  Does system.network + network need to exist separately?
  - Need to sort out scope / phases + proposal
  - Now recommending a SIG
- Semantic Conventions for [Software Carbon Intensity](https://greensoftware.foundation/standards/sci/)
  - Part of Green Software Foundation (also under LF)
  - Looking to find ways to calculate scores (SCI rate) from OTEL instrumentation / semantic conventions
  - Calculate environmental impact from software
  - Previous attempt - [https://github.com/open-telemetry/community/issues/2020](https://github.com/open-telemetry/community/issues/2020)
  - Now want to develop / complete semantic conventions
  - This is an opportunity to create federated registry - A specific registry for instrumentation if it's not re-using existing OTEL instrumentation.
    - The standard can evolve quickly without blocking on OTEL semconv initially.
    - Federation proposal - [https://github.com/open-telemetry/opentelemetry-specification/pull/4906](https://github.com/open-telemetry/opentelemetry-specification/pull/4906)
    - [https://github.com/open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)
      - [https://github.com/open-telemetry/opentelemetry-python-genai](https://github.com/open-telemetry/opentelemetry-python-genai)
    - Two options for federating
      - 1 - Living in OpenTelemetry org
      - 2 - Living outside of OpenTelemetry org
      - We support both.
      - Example OCSF is planning to host their own.
  - If you're interested in green software - please reach out!
