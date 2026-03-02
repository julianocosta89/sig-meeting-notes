## Meeting Notes

### Attendees
- Ted Young [Grafana Labs]
- Jared Freeze (Embrace)
- Joaquin Diaz (Embrace)
- Martin Kuba (Grafana Labs)
- Abinet Debele (Cisco)
- Wolfgang Therrien (Honeycomb)
- Benoit Zugmeyer (Datadog)
- Daniel Dyla
- Hector Hernandez (Microsoft)

### Agenda
- [martin] Page view semantic conventions
  - Discussion about separating soft navigation into a different events
  - [slack thread](https://cloud-native.slack.com/archives/C093P0AMP0T/p1757540365873069)
  - arguments for separating
    - instrumentation for soft navigation will be complex
    - soft navigation concept is not standardized - the instrumentation will likely be experimental longer
    - soft navigation will probably have more attributes than just the URL (do we want an event where some attributes are applicable based on type?)
    - “[soft navigation](https://wicg.github.io/soft-navigations)” is a more precise (technical) term, while page view is a user-centric term
  - arguments against
    - users would have to look at two different events when analyzing number of page views
- [Joaquin] [Only if we have time – if not we can discuss on PR] Page load event
  - Definition: The event represents the page load phase, from navigation start until Largest Contentful Paint (LCP).
  - Possible attributes (draft):
    - browser.page_load.navigation_start_time: Unix timestamp in milliseconds when navigation started
    - browser.page_load.duration: Total page load duration from navigation start until Largest Contentful Paint (LCP) in milliseconds
    - browser.page_load.first_paint_time: Time in milliseconds relative to browser.page_load.navigation_start_time when first paint event occurs
    - browser.page_load.first_contentful_paint_time: Time in milliseconds relative to browser.page_load.navigation_start_time when First Contentful Paint (FCP) event occurs
    - browser.page_load.resource_count: Total number of resource requests initiated during the page load.
    - browser.page_load.blocking_resource_count: number of resources that blocked rendering before LCP
    - browser.page_load.cached_resource_count: number of resources served from browser cache
    - browser.page_load.transfer_size: total number of bytes transferred over the network for all resources requested during the page load
- [ted] Using resources/entities to store page info?
