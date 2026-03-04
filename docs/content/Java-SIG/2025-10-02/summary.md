## Key Topics
- Discussion on profiling use cases and the role of the OpenTelemetry SDK in supporting profiling tools like eBPF, async Profiler, and JFR.
- The need for a library to build data for export rather than just an exporter, focusing on data capture and translation.
- Challenges related to the JFR file format and the potential need for filtering events to manage data size.
- The current state of profiling SDKs and the absence of a standardized API for profiling in OpenTelemetry.
- Consideration of an internal API or SPI for profiling to facilitate data handling without being a full user-level API.

## Action Items
- Define the scope of support for profiling use cases and determine which functionalities to include in the SDK.
- Explore the feasibility of creating a library for data capture and translation for profiling.
- Investigate the implementation of an internal API to assist in building profiling data for export.

## Participants
Trask Stalnaker, Jay DeLuca, Jason Plumb, Jonathan Halliday, Lauri Tulmin
