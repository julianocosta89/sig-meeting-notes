## Meeting Notes

### Attendees
- **Brett McBride**
- **Chris Lightfoot-Wild**
- **Nick Schuch**
- **Pawel Filipczak**
- **Sergey Kleyman**

### Agenda
- [all] - discussed [https://github.com/open-telemetry/opentelemetry-php/issues/1701](https://github.com/open-telemetry/opentelemetry-php/issues/1701) and whether “auto root span” + “local root span” could be used as a pattern to better capture the full request lifecycle. Eg, always start a root span from RINIT, and in framework instrumentations modify the root span instead of creating it.
