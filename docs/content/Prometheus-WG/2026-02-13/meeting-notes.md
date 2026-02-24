## Meeting Notes

### Agenda
- [arthur] Stabilizing Prometheus exporter spec
- [arthur] Prometheus Receiver stabilization progress review
  - assigned documentation task, first step is to go through the list and see what we are missing anything.
- [arthur] prometheusreceiver needs to migrate to appender v2. Big chunk of work that needs an owner.
- Sdk exporter spec is not compliant with OpenMetrics 1.0.
  - 1. Client ignores OM spec.  It is the server’s responsibility to enforce or not.
  - 2. Fail when TranslationStrategy is NoTranslation on OM 1.0.
  - Needs an issue to discuss.
  - Consensus: NoTranslation should do what it says and not translate.
