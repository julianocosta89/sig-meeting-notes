## Meeting Notes

### Attendees
- Tyler Benson (ServiceNow)
- ~~Lukas Hering (Capital One)~~
- Bhaskar Banerjee (Capital One)
- Stephen Hong (Capital One)
- Warre Pessers (DPG Media)

### Agenda
- Bhaskar: Seeing added cold start delays from using the OTel Lambda layers.
  - Majority of the delay is from the language sdk layer
  - Evaluated and saw significant degradation in Java, Python, and Javascript
- Lukas: Adding [FaaS metrics](https://opentelemetry.io/docs/specs/semconv/faas/faas-metrics/#metric-instruments) to Lambda Layer
- Lukas: (related to above) explore ways to propagate application exception info to the layer
- Lukas: Develop automated test suite for supported Lambda runtimes
