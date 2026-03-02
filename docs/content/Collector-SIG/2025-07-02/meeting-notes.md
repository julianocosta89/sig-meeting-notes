## Meeting Notes

### Attendees
- [Evan Bradley](mailto:google@evanbradley.org) (Dynatrace)
- Israel Blancas (Coralogix)
- Josh MacDonald (Microsoft)
- Mikołaj Świątek (Elastic)
- [David Ashpole](mailto:dashpole@google.com)(Google)
- Christos Markou (Elastic)
- [Yang Song](mailto:yang.song@datadoghq.com) (Datadog)
- [Jade Guiton](mailto:jade.guiton@datadoghq.com) (Datadog)
- Dakota Paasman (Bindplane)
- [Sam DeHaan](mailto:sam.dehaan@grafana.com)(Grafana Labs)
- David Boney  (University of Houston)
- [Jordi Vilaseca Corderroure](mailto:jvilaseca@tinybird.co) (Tinybird)
- [Srinivas Venkata Bevara](mailto:venkata-srinivas.bevara@broadcom.com) (DX O2 - Broadcom)
- Raj Nishtala (SumoLogic)
- Dmitry Anoshin (Splunk)
- [Paulin Todev](mailto:paulin.todev@grafana.com)(Grafana Labs)
- Ron Korland (Sawmills.ai)

### Agenda
- [Jade] RFC amendment announcement: [https://github.com/open-telemetry/opentelemetry-collector/pull/13260](https://github.com/open-telemetry/opentelemetry-collector/pull/13260)
- [Vihas] (will not be able to attend) RFC announcement: [https://github.com/open-telemetry/opentelemetry-collector/pull/13256](https://github.com/open-telemetry/opentelemetry-collector/pull/13256). Here’s a summary of my RFC:
- [Josh M] Briefly mentioned:
- [Mikołaj] Subcomponents status support: [https://github.com/open-telemetry/opentelemetry-collector/issues/13210](https://github.com/open-telemetry/opentelemetry-collector/issues/13210)
- [David Boney]
- [Paulin] I’ve been working on [a feature](https://github.com/open-telemetry/opentelemetry-collector/pull/13155) which generates config.go files for components from schema located in each component's metadata.yaml file. I wonder if the broader group of collector maintainers would find such a feature useful and if you'd like me to work on it in a particular way?
- [Evan] k8s semconv migration – question on how to proceed
- [Ron] Keda Scaler Exporter - I need help with find a sponsor for my PR
- [Sam] scraperhelper [parallel scraping](https://github.com/open-telemetry/opentelemetry-collector/pull/13167)
