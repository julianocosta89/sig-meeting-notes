## Meeting Notes

### Attendees
- Trask
- Liudmila
- Steve
- Albumen

### Agenda
- Move meeting an hour earlier during Standard Time
  - moved
- Which protocols / frameworks ? [https://github.com/open-telemetry/semantic-conventions/issues/2921](https://github.com/open-telemetry/semantic-conventions/issues/2921)
  - Frameworks:
    - **Grpc**
    - Connect-rpc
    - **Dubbo**
    - There are some JSON RPC libs, but it's used more as a convention than lib - let's not stabilize?
- Review open PRs
  - Status code: [https://github.com/open-telemetry/semantic-conventions/pull/2920](https://github.com/open-telemetry/semantic-conventions/pull/2920/files)
    - rpc.**response**.status_code
    - “Response” is logical response
    - Also consistent with db.**response**.status_code
      - Where possibly could be timeout etc
  - Duration: [https://github.com/open-telemetry/semantic-conventions/pull/2961](https://github.com/open-telemetry/semantic-conventions/pull/2961)
    - Should we have streaming and non-streaming mixed in the same metric or have two different metrics?
      - We have to differentiate somehow
        - We can have a dimension?
        - Do we even know on the instrumentation level?
      - rpc.client.call.duration
        - Dimension for streaming or not
        - Cover both Unary and Streaming (duration from start of stream to end of stream)
      - rpc span
        - Same definition
- Next steps:
- Next week: KubeCon - let's cancel?
