## Meeting Notes

### Attendees
- Trask
- Steve
- Liudmila
- Madhav
- Matthew

### Agenda
- gRPC feedback
  - Liudmila will respond on [https://github.com/open-telemetry/semantic-conventions/issues/3873](https://github.com/open-telemetry/semantic-conventions/issues/3873)
- Error.type
  - From grpc perspective all status codes except OK are errors
  - Madhav will create an issue
    - Would be great to collect feedback on whether users asked for different mapping
    - OTel / prior APM systems receive feedback to not mark client errors on server
- Metadata -> headers + trailers
  - Disambiguates
  - Madhav will file an issue
  - Not on the core span, opt in for others
  - Most rpc protocols follow / compatible with gRPC and header / trailer could be common terminology
  - Dubbo uses attachment [https://cn.dubbo.apache.org/en/overview/mannual/java-sdk/tasks/framework/attachment/](https://cn.dubbo.apache.org/en/overview/mannual/java-sdk/tasks/framework/attachment/),
    - Steve will check out  trailers
- Histogram buckets
  - gRPC  0, 0.00001, 0.00005, 0.0001, 0.0003, 0.0006, 0.0008, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.008, 0.01, 0.013, 0.016, 0.02, 0.025, 0.03, 0.04, 0.05, 0.065, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25, 0.3, 0.4, 0.5, 0.65, 0.8, 1, 2, 5, 10, 20, 50, 100
  - Let's entertain idea of
    - Adding smaller buckets
    - Having fewer buckets by default
    - For RPC in general
