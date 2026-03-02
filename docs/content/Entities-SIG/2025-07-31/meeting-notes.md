## Meeting Notes

### Attendees
- [Daniel Dyla](mailto:dyladan@gmail.com) (30m)
- Josh Suereth
- [Nathan Smith](mailto:nathan.smith@elastic.co)
- [Antoine Toulme](mailto:atoulme@splunk.com)(30m)
- Dmitry Anoshin

### Agenda
- [josh] Entity ENV variable
  - Clearly disambiguate from Config
  - Clearly denote use case for passing ID via ENV from system of ownership.
- [josh] [https://github.com/open-telemetry/community/pull/2837](https://github.com/open-telemetry/community/pull/2837) - Service/Resource tags
- [josh] API/SDK proposal discussions
  - How to do startup
  - Strawman
    - SDK EntityProvider will have a registration of "startup entity detectors"
    - When these complete, we'll fire initialization event
    - Defer sending data until this completes
    - give it a hard time limit on completing and force initialization after that limit.
- Triage
- New Times?
  - Moving back to weekly, but with 30 min meeting.
