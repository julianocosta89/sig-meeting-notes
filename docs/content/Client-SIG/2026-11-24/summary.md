## Key Topics
- Jared Freeze reported from the Performance.now conference that Firefox, Chromium, and Chrome teams are interested in moving OTel into the browser, possibly using the Reporting API to send performance timeline data.
- Discussion of web vs. mobile session modeling: web sessions are split into short-lived spans and stitched later, while mobile often uses a long-running session span with crash recovery and disk buffering.
- Jason Plumb noted an open spec proposal to emit span start events so long-running operations are visible before they end, and said a session SIG is needed to formally define session data models and lifecycle.
- Browser payload size and delivery constraints (single-frame sends, compression, abandonment signals) were raised, with a note that OTLP JSON and protobuf may be too large for the web.
- Schema stability concerns: browser vendors need strict forward-only compatibility for published telemetry schemas (such as `span.type`), with no room for breaking changes.

## Action Items
- Jason Plumb: help bootstrap a session SIG when time allows (no firm date).
- Jared Freeze: continue exploring what "good enough" session export looks like on the web (e.g., idle-based flushing or passing a session ID instead of a full span).

## Participants
Jared Freeze, Jason Plumb, João Oliveira
