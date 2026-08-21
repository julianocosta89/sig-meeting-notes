## Meeting Notes

### Attendees
- Laurent Querel (F5)
- Albert Lockett (F5)
- Gokhan Uslu (Microsoft)
- Aaron Marten (Microsoft)
- Drew Relmas (Microsoft)
- Kennedy Bushnell (Microsoft)
- Jake Dern (F5)
- Matt Wear (Dash0)
- Josh MacDonald (Microsoft)
- Maksat Maratov (Microsoft)
- Brian Sapozhnikov (Microsoft)
- Swapnil Ashtekar (Microsoft)

### Agenda
- [Triage]
  - Issues that need to be discussed: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Atriage%3Aneeds-discussion)
  - Issues that have just been marked as stale: [https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale](https://github.com/open-telemetry/otel-arrow/issues?q=is%3Aissue%20state%3Aopen%20sort%3Aupdated-desc%20label%3Astale)
- [Group]
  - Keep in mind the continuous benchmarks and look at them: they are showing some irregularities recently; would be nice to annotate the performance graphs when they change.
- [Laurent]
  - New file exporter (phase 1), future phase 2
- [jmacd] Briefly discuss [chore(sql): prototype Oracle receiver with base scraper by athomas9195 · Pull Request #3821 · open-telemetry/otel-arrow](https://github.com/open-telemetry/otel-arrow/pull/3821)
  - Idea of a “cursor service” extension might be possible, could be refactored out of Quiver or could be an external service like Redis etc.
