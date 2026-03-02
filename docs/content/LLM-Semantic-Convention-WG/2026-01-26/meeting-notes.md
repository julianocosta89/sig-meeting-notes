## Meeting Notes

### Attendees
- Minghui Zhang (Alibaba)
- Haotong Zhang (Ant Group)
- Xiang Wu (Ant Group)
- Chris Yang (Ant Group)
- Neil Yashinsky (ContextCore)
- Liudmila
- Huxing Zhang (Alibaba)

### Agenda
- Python contrib PR for events - [https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3994](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3994)
  - Liudmila to review
  - Need more eyes
- [Haotong, 15min] Semantic Conventions for Token-level Attributes and Events：
  - [https://github.com/open-telemetry/semantic-conventions/issues/3335](https://github.com/open-telemetry/semantic-conventions/issues/3335)
- General approach on recording time-per-token
  - Token relative timestamps
  - Alternative: distribution only
- How to record
  - Attribute
  - Span events - on deprecation path
  - Logs - one log as a child of inference span with more details
- **How to make progress**
  - **This is mostly about engines**
  - **Let's try to find community that can collaborate**
  - **Let's try to document conventions in vLLM and see if that's common enough for others to adopt**
    - **We can link from otel conventions**
- What to record
  - Arrays with schedule time, generation time, batch size, total token number
    - Better perf
  - {st: 1, gt: 1, bs: 2, ttn: 3 }
    - Better readability, not performant
- E2e
  - Workflow
    - Agent1
      - Inference (client)
        - Http client
          - Vllm server span
            - Here're the per-token latencies
