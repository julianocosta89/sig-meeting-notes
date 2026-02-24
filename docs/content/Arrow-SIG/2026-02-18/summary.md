## Key Topics
- Discussion on recent OPL PRs, particularly adding datetime support to the parser.
- Issues with date parsing in the current implementation, specifically regarding timezone support.
- Clarification on the date formats supported by KQL and their implications for OPL.
- Plans for future work on expression evaluation within the columnar query engine.
- Challenges related to joining datasets in expression evaluation.

## Action Items
- Albert to document the identified issue with date parsing (GitHub issue 2047).
- Albert to explore the implementation of expression evaluation using DataFusion.
- Mike to continue work on achieving parity between the Go Collector and Aero Rust Collector.

## Participants
Albert Lockett, Mike "Blanch" Blanchard
