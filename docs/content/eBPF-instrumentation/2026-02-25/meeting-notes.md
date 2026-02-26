## Meeting Notes

### Attendees
- Mike Dame (Odigos)
- Stephen Lang (Grafana)
- [Florian Lehner](mailto:florian.lehner@elastic.co)(Elastic)
- Rafael Roquetto (Grafana)
- Mario Macias (Grafana)
- Nimrod Avni (Coralogix)
- Tyler Yahn (Splunk)
- Mattia Meleleo (Coralogix)
- Giuseppe Ognibene (Coralogix)
- Antonio Jimenez (Cisco ThousandEyes)
- Marc Tuduri (Grafana)
- Nikola Grcevski (Grafana)
- Robert Pająk (Splunk)

### Agenda
- [Mattia] CI release job is broken – v0.5.0 image was not published
  - Image was pushed, just not correctly tagged
  - [Tyler] AI: ask for the image to manually tagged
    - [https://github.com/open-telemetry/community/issues/3294](https://github.com/open-telemetry/community/issues/3294)
- [Stephen] Image signature verification is also [broken](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1359) (cache image only)
- [Tyler] [v2.0 Configuration](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1351)
- [Tyler] [Adding OBI to the collector-contrib distribution](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/46192)
- [Rafael] Quick update on .NET/tpinjector work
  - Upstreaming or partial changes
- [Nikola] I started adding [GenAI spec protocols](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation/pull/1353)
- [Mike] please join llm-d sig observability: [https://github.com/llm-d/llm-d/blob/main/SIGS.md#sig-observability](https://github.com/llm-d/llm-d/blob/main/SIGS.md#sig-observability)
  - meeting calendar: [https://llm-d.ai/docs/community#public-meeting-calendar](https://llm-d.ai/docs/community#public-meeting-calendar)
  - sig notes: [https://docs.google.com/document/d/12cvQ5eCktoZwlvgmdnip5135HMrGauq-WCqjgvHTDvw/edit?tab=t.0#heading=h.2i2twlagmg0z](https://docs.google.com/document/d/12cvQ5eCktoZwlvgmdnip5135HMrGauq-WCqjgvHTDvw/edit?tab=t.0#heading=h.2i2twlagmg0z)
