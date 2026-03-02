## Meeting Notes

### Attendees
- Damien Mathieu (Elastic)
- Tyler Yahn (Splunk)
- David Ashpole (Google)
- Bryan Boreham (Grafana Labs)
- Robert Pająk (Splunk)

### Agenda
- [Damien] otelgin context reversal and data race
  - [https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8014](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/8014)
- [Flc: offline, due to time zone] A historical issue: otelgin: using middleware causes temporary MultipartForm files not to be destroyed
  - Information: Although it manifests in otelgin, virtually all HTTP-related middleware have this type of issue.
  - Some references (may include more):
    - [https://github.com/open-telemetry/opentelemetry-go-contrib/no issues/5946](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/5946)
    - [https://github.com/open-telemetry/opentelemetry-go-contrib/pull/6609](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/6609)
    - [https://github.com/golang/go/issues/71382](https://github.com/golang/go/issues/71382)
    - [https://github.com/golang/go/issues/74455](https://github.com/golang/go/issues/74455)
  - Due to repeated inquiries and the lack of a best practice officially provided by Go, I believe we need to establish a unified standard or solution to address such issues. Proposed solutions for reference:
    - Option 1: As mentioned in most references: c.Request.MultipartForm.RemoveAll()
    - Option 2: Leave it to the user to decide, with the principle of "whoever uses it is responsible for cleanup"
    - Option 3: Provide an option or switch for users to configure, but we need to determine a default configuration(I think the current situation can be set as the default configuration.)
  - Notes:
    - The options listed sound good
    - We likely want to start with default behavior of removal
    - Wait for user interest to add configuration
    - The component owners should be empowered to make this decision
- [Damien] checking in with long seen codeowners/triager
  - Reaching out to scorpionknifes about continuing on in the role
- [Robert] [sdk/log: Fix AddAttributes, SetAttributes, SetBody on Record to not mutate input #7403](https://github.com/open-telemetry/opentelemetry-go/pull/7403)
- [Tyler] Milestone v1.39.0 check-in:
  - [Otel](https://github.com/open-telemetry/opentelemetry-go/milestone/74)
  - [Contrib](https://github.com/open-telemetry/opentelemetry-go-contrib/milestone/33)
