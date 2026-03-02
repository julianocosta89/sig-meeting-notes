## Meeting Notes

### Attendees
- Christos Markou (Elastic)
- Edmo Vamerlatti (Elastic)
- Ondrej Dubaj (Dynatrace)
- Moritz Wiesinger (Dynatrace)
- Evan Bradley (Dynatrace)
- Constanca Manteigas (Elastic)
- Damien Mathieu (Elastic)
- Paulo Dias (Five9)
- Israel Blancas (Coralogix)
- [Andrzej Stencel](mailto:andrzej.stencel@elastic.co) (Elastic)

### Agenda
- [Christos] Call for feedback:
  - on the work about linking components' metrics to semconv definitions
  - on defining rules about metrics' stability levels
  - Tracking issue: [https://github.com/open-telemetry/opentelemetry-collector/issues/13297#issuecomment-3355285318](https://github.com/open-telemetry/opentelemetry-collector/issues/13297#issuecomment-3355285318)
- [Moritz] Introduce standardized list of components for chloggen to validate against?
  - Looking for feedback/discussion
  - Start implementing this in collector-core
  - Also make chloggen produce changelogs that are in alphabetical order (maybe using a special flag to make it non-breaking?)
  - EDIT: issue created: [https://github.com/open-telemetry/opentelemetry-collector/issues/13923](https://github.com/open-telemetry/opentelemetry-collector/issues/13923)
