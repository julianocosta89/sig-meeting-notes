## Meeting Notes

### Attendees
- Albert Lockett (F5)
- Jake Dern (Microsoft)
- Utkarsh Umesan Pillai (Microsoft)
- Drew Relmas (Microsoft)
- David Dahl (F5)
- Josh MacDonald (Microsoft)

### Agenda
- [Utkarsh & Albert] View pattern talk
  - Albert follows-up on the topic of Visitor patterns following last week.
  - Laurent prototyped a “View” trait alternative, giving us a simpler, lower-overhead approach (Josh was impressed, didn’t realize Rust could do this!)
  - The View trait gives a more imperative interface for directly probing each visitable, making it possible to use ordinary for-loops.
  - Albert iterated, Utkarsh iterated, looking at lifetime.
  - Albert has experimented with using these Views to construct OTAP batches directly from OTLP bytes.
  - Utkarsh experimented with same, first approach was roughly equivalent to Prost, parsed objects and yielded views, and (naturally) slower than Prost; next approach was “lazy” which avoided a lot of overhead, yielding promising results
  - Laurent: many constraints, not obvious or easy how to solve this; thinks we are very close.
    - The ideal case is appealing: a set of conversion routines for each format “compatible with” OTLP, makes possible to re-use transformations
    - Josh tries to describe the “ideal” efficient view mechanism, it wants to not allocate but the order of field access is prescribed by the caller. The pros/cons of Visitors vs. Views comes out here.
    - Thinking about how to generate OTAP from a View or a Visitor; for a View the implementor has control over access, so (maybe) we memorize a set of offsets for what we skip. (This will make it hard for streaming data, but probably not an immediate problem.)
    - Josh asks about whether to memorize full random access or only what we’ve skipped.
    - We will anyway return to benchmarking the Prost encode/decode with translation to OTAP.
  - Utkarsh: also note that Prost uses unsafe and potentially we’re not making a fair comparison?
    - LQ: we should try to avoid unsafe, but if we can’t, we can’t: willing to accept unsafe if we have to just test carefully.
    - I.e., does Prost assume utf8 validity?
    - Is there a problem with not scanning all bytes for validity? Flip-side: it’s easy to deal with truncated protobuf objects.
    - Shall we have a recursion limit?
    - TIL in function programming the “View” traits are called Lenses
