## Meeting Notes

### Attendees
- [Scott Gerring](mailto:scott@datadoghq.com)(Datadog)
- [Björn Antonsson](mailto:bjorn@datadoghq.com)(Datadog)
- Warren Snipes
- Partha Sharma

### Agenda
- Warren had an issue setting up mixed logs+traces export where logs go out stdout via tracing, and correlation is difficult. This seems like a common issue and perhaps we can either point out a better solution, or at least document best-practices in our examples repo
- Warren is also trying to do context propagation from Rust into a Python app via an FFI (for data science-y stuff on the inside) - interested in either 1/ returning nested telem back to parent rust, or 2/ exporting spans from python. We have difficulty thinking of a clean way of doing this; if anyone reading this has a good idea, plus write ;)
