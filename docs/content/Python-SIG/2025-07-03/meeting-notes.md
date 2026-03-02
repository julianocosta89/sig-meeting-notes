## Meeting Notes

### Attendees
              - Ridhima Satam(Cisco/Splunk)
              - Tammy Baylis (SolarWinds)
              - Jeremy Voss (Microsoft)
              - Pablo Collins (Cisco/Splunk)
              - Emídio
              - Hector Hernandez (Microsoft)

### Agenda
              - [riccardo] what should we merge regarding logs deprecations?
              - https://github.com/open-telemetry/opentelemetry-python/pull/4647
              - The PR is fine
              - Revise GC/TC feedback from last week
              - [Ridhima] - new genAI instrumentation langchain support, PR - https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3600
              - We need to look at the package name if it’s possible to reuse openllmetry namespace with a new version or release the package with a different name
              - [Jeremy] Draft PR to fix dependency conflict breakage almost done. See Issue for details
              - Hope to get approval from kafka, fastapi, and psycopg2 stakeholders
