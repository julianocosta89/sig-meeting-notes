## Meeting Notes

### Attendees
- Utkarsh (Microsoft)
- Laurent (F5)
- Josh M (Microsoft)
- Jake Dern (Microsoft)
- Mike Blanchard (Microsoft)
- Albert Lockett (F5)
- Danny Chin (CMU)

### Agenda
- Issue triage
  - Talk about OTLP metric export
    - About the diagram NUMA-node level metrics aggregator -> Rust OTel client SDK
    - This is the plan of action. However, we also can imagine a direct SDK for metrics to OTAP; **we will not prioritize**.
  - About multivariate metrics dreaming
    - For SDKs
    - For storage
    - For Analysis
  - About concurrent, backpressure, wait_for_result
    - These do have equivalent settings in the Collector, but its default is wait_for_result=false; we need a Collector issue to track
    - (we don’t all always agree here!)
- Benchmark plan
  - Continuous benchmarks (per commit) - “core” protocol matrix (otap, otlp)
  - Nightly - Additional protocols, configuration parameters of interest
  - Periodically (TBD) - Comparison against other solutions
- Laurent: define a list of engine-related tasks that require prioritization
- Demo: @c11y shows us logs filter processor
  - E.g., by severity, by attributes
- Parking lot:
  - About instrumentation of num_items()
  - About fanout-connector and how to handle backpressure when there are multiple exporters
