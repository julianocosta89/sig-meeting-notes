## Key Topics
- **SQL Client Instrumentation**: Discussion on changes for context propagation using context info and the need for review before merging.
- **Testing on Mac OS**: Challenges faced with running tests on Mac OS and the need for assistance in executing integration tests.
- **Security Updates**: Update on addressing insecure package versions and compliance with existing policies.
- **Frequent Sampling Plugin**: Overview of a new plugin for frequent sampling, including design considerations and demo results.
- **Propagator Configuration**: Discussion on the implications of baggage propagation and how it affects downstream services.

## Action Items
- **Review SQL Client Changes**: Zach Montoya to review the SQL client instrumentation changes.
- **Create Issue for Policy Discussion**: Mateusz Łach to create an issue regarding the testing policy for package versions.
- **Investigate Propagator Behavior**: Consider creating an issue to discuss handling propagators and baggage propagation.
- **Submit Follow-Up Issues**: Mateusz Łach to submit issues for improving test coverage and moving symbol resolution outside runtime suspension.

## Participants
Piotr Kiełkowicz, Rasmus Kuusmann, Zach Montoya, Chris Ventura, Mateusz Łach
