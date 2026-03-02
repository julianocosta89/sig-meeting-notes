## Meeting Notes

### Attendees
              - Dylan russell (google)
              - Aaron Abbott (Google)
              - Ezzio Moreira
              - Riccardo Magliocchetti (Elastic)
              - Pablo Collins (Splunk/Cisco)
              - Hector Hernandez (Microsoft)

### Agenda
              - [Jeremy] “instruments_any” feature PR to solve longstanding conflict between instrumentations that need and dependency lists vs or.
              - Issue, PR 1, PR 2, file
              - Relevant instrumentations: fastapi, kafka-python, psycopg2, cassandra, tortoiseorm
              - Investigation uncovered potential conflict between how bootstrap and dependency conflicts interpret “instruments” list. Bootstrap seems to interpret as “or”. Each entra is considered a reason to install the instrumentation on its own. Sdk interprets as “and”
              - [Riccardo] Will cut a release tomorrow
              - Merge this https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3624 or wait?
              - More log breakage in the next release https://github.com/open-telemetry/opentelemetry-python/pull/4676 , any idea for backward compat?
              - [Aaron] let’s try to not spread breaking changes in too many releases
              - [Aaron] create a milestone / add labels to group stuff deprecating / breaking
              - [Ezzio] I have been working on an issue, the refactor to deprecated SpanAttributes PR. We need to define which version I should return to the _get_schema_url_ in opentelemetry-instrumentations functions: 1.21 or 1.23.
              - [Riccardo] I would stick with current value and update once we have checked the actual semconv we are exporting
              - [Aaron] any update on previous topic The GC and TC are collecting feedback from all SIGs in order to put together a roadmap (past and future) to share with the community
              - AI: let’s do a capacity plan similar to what we did in GenAI SIG next time. See GenAI prioritization/capacity plan as a template [External] GenAI project priorities
              - [Sergey] GenAI Instrumentation SDK - common library for boilerplate code to support different GenAI Telemetry and types
              - [Aaron] take a look at vertex-ai implementation for sync/async handling
              - [Aaron] Also please add this sdk to the typechecked dirs
