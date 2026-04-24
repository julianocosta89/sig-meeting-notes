## Meeting Notes

### Attendees
- Tyler Yahn (Splunk)
- Robert Pająk (Splunk)
- David Ashpole (Google)
- Bryan Boreham (Grafana Labs)

### Agenda
- [Bryan] Feedback on Go runtime metric proposals
  - Heap memory usage falls into “other”.  Won’t most of users’ memory usage be “other”?  That seems not very helpful.
- [dashpole] Open Question for exemplar reservoirs:
  - [https://github.com/open-telemetry/opentelemetry-go/pull/8257](https://github.com/open-telemetry/opentelemetry-go/pull/8257)
  - Is round-robin to multiple algorithm L implementations acceptable?
    - It prevents Offer 1 and k+1 from ever being both sampled.
  - We should keep the randomness after round robining.
