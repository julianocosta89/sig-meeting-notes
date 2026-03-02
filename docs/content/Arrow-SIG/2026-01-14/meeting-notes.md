## Meeting Notes

### Attendees
- Mike Blanchard (Microsoft)
- Albert Lockett (F5)

### Agenda
- OPL will use its own parser
- Parser war stories & tips
  - LHS recursion & Pratt parser
  - [https://pest.rs/#editor](https://pest.rs/#editor) helpful tool
  - Schema validation - seed schema + output schema (mutations to seed) can be useful (it can be a hard retrofit)
- Columnar equivalent of RecordSet engine in progress - discussion about trait lifetime difficulties and using arrow’s internal Arc could help
