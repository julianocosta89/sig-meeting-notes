## Meeting Notes

### Attendees
- Mike Blanchard (Microsoft)
- Laurent Querel (F5)
- Albert Lockett (F5)
- Andres Borja (Microsoft)
- Luke Steensen (DataDog)

### Agenda
- Introductions
- Status updates
- OPL Overview from Laurent
  - KQL inspired stream processing language, strongly typed, and guarantees valid OTel signals is the output.
- Brief description of learnings from Columnar Query Engine POC from Albert
  - Challenges with single DataFusion ExecutionPlan: Operating on multiple batches and confusing join order for filtering attributes
  - To address challenges - pipelines are multi-stage, not a single ExecutionPlan
- Discussion about OPL & pushing the pipeline stages to multiple pipeline components
  - Initial plan: start with processor, but keep in mind distributing certain pipeline stages. The motivating example is predicate pushdown (filtering in the processor).
- Alignment on our own Abstract Syntax Tree
  - We agree this is the right approach for multiple reasons: easier support for various languages, and b/c we’d like to have another layer on top of the DF logical plan (considering our query plans will be made up for multiple stages that are not necessarily a single ExecutionPlan).
- Datadog interest:
  - Improved bandwidth & filtering/processing exploration
- Discussion of OTel-Arrow vs other formats - tradeoffs
