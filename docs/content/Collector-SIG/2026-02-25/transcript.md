SIG: Collector SIG
Date: 2026-02-25
Duration: 7 minutes
Zoom Recording URL: https://zoom.us/rec/share/PNMDOryDyTdpbVVZqkPb3qvS5ZUGhQeqBYhWFJNRVkKBAPPCU3OjdJwnbwQ0ToU9.VbcDGOIKKA2fjiMX
============================================================

## Zoom Recording Transcript

**Andrzej Stencel** 02:23 Hello.
**Perk (Marcin Stożek) | Elastic Ingest** 02:24 Hello, everyone.
**Andrzej Stencel** 03:19 We have only one item on the agenda, regular stability.
Something, something. Anyone wants to say something about it?
**Christos Markou** 03:52 For the K attributes processor, we have had some significant progress, I think.
I think what is missing is… To link… to figure out how benchmarks Should be linked to the documentation.
the README file.
Yeah, we haven't had the chance to look into this yet.
And, yeah, and other than this, we are… expecting the new Samanth conventions to… So I filed the PR in OpenTelemetry Go to generate the new semant conventions.
And after this is merged, I will, update the dependency of the component to this commit.
And after this, the component will be pointing to beta semantic conventions, or Kubernetes attributes.
So, yeah, next step is to promote semantic conventions to release candidates.
That is the plan, and after this, we should wait.
For a significant period of time, I would say.
And, wait for feedback until we are confident to… Start switching, the feature gates.
And everything.
**Jade Guiton** 05:12 Sounds… Considering the… The benchmark thing seems like it's going to be a problem for all components.
Has there been a… an issue, like, a repo-wide issue opened about it that would probably help?
Track, implementation of whatever we need for that.
Which I guess is probably just… CI.
**Christos Markou** 05:35 I don't think we have an issue for this. We discussed this in the respective issue for the cage processor.
And in the Prometheus receiver, with Arthur as well, because these two components have faced that already.
And we slightly discussed this last week in the Collector SIG.
And Dmitry pointed out to some… to a page that we have.
Where the benchmarks of the collector are published.
So… yeah. But I haven't… I didn't have the chance so far to… like, look into this, and no one else had the chance as well.
**Jade Guiton** 06:16 Yeah, no problem. It's just that it might be better for visibility for other components that might be trying to aim for stability, to have a… A general issue about it.
**Christos Markou** 06:27 Yeah, yeah, sounds good. I can, create one right after this meeting, then. That helps.
**Jade Guiton** 06:34 Okay, thank you.
**Christos Markou** 06:36 And I guess I will link it back to the stability issue, the main one that we have.
For all the components.
**Jade Guiton** 06:44 Yeah, that makes sense.
Any other updates regarding component stability?
Sounds like a no?
Any other topics somebody would want to bring up?
That was, like, also a no. So… I guess we can end it here?
**Evan Bradley** 07:33 one today.
**Christos Markou** 07:34 Thank you.
**Andrzej Stencel** 07:36 See, everyone.
**Jade Guiton** 07:37 Thank you, everyone.
