## Meeting Notes

### Attendees
- **Pawel Filipczak**
- **Chris Lightfoot-Wild**
- **Shawn Maddock**
- **Brett McBride**
- **Sergey Kleyman**
- **Ago Allikmaa**

### Agenda
- [BM] - discuss [https://github.com/open-telemetry/opentelemetry-php/pull/1659](https://github.com/open-telemetry/opentelemetry-php/pull/1659)
- [BM] - Shawn noticed that our “build php base image” job has been failing for a while. Was taking >5 hours 12 months ago, then consistently >6 hours (github max)
- [SM] - Clock component in the API - react developers.
  - Can we add some sort of sleep / delay to our Clock component
  - PSR transport
    - For react we could make an applicable clock interface instead of the system sleep
  - [https://github.com/open-telemetry/opentelemetry-php/blob/main/src/SDK/Common/Export/Http/PsrTransport.php#L105](https://github.com/open-telemetry/opentelemetry-php/blob/main/src/SDK/Common/Export/Http/PsrTransport.php#L105)
- [SK] - Sdk Autoloader
  - Configuration being passed to instrumentation
    - Environment variables (original implementation)
    - File based configuration -> Declarative configuration
    - [https://github.com/open-telemetry/opentelemetry-php/pull/1523](https://github.com/open-telemetry/opentelemetry-php/pull/1523)
