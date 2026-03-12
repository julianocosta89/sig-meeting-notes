SIG: Technical Committee
Date: 2026-01-21
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/ng6dHjS2JIiF1sCAnja-hfkZNHM27GxRW13cKfS2KyyMbvIGe_jwHEkyyXyO5nad.Mqj5L8DbZoh5XAVY
============================================================

## Zoom Recording Transcript

**Reiley** 00:49 Hello, how are we?
**Armin (Dynatrace)** 00:53 What's up?
**Reiley** 00:56 Hey.
How are you doing?
**Armin (Dynatrace)** 01:02 All good. What about you?
**Reiley** 01:04 Yeah, doing well.
It's just, looking at the… the inbox, there's one… issue in the spec inbox, and community has nothing.
It looks like Carlos created that, the deprecation of the… Open tracing propagator.
**Armin (Dynatrace)** 01:26 in line with the Diego one, I guess?
**Reiley** 01:30 Yeah.
**Tigran Najaryan** 01:34 Hey, guys.
**Reiley** 01:36 Hey, Tigran.
Let's give folks one minute, and I just checked the inbox. We have one deprecation about the OpenTracing propagator.
**Armin (Dynatrace)** 02:43 I just checked with Carlos, he will be joining later, he said, But that's all that we have on the agenda before we will jump on the private car.
So I guess we can just jump on that one right away, and then… Come back to this one for the, trace propagator discussion.
Or is there any other… other topic for the main agenda?
**Josh Suereth** 03:08 I did want to check if we need to do any follow-up on the topic with the GC public call, and the TC public call last week on, the stable by default OTEP, or if we're… Okay, just following up on the OTEP itself with comments and things. I don't… I didn't have a chance to check to see if it got updates to it. I was gonna take a look now.
**Tigran Najaryan** 03:30 I think Austin said he has enough feedback from us to do another round. I think that was last I heard in the GCTC meeting, so… I'm expecting him to update the OTEP, and we can take it from there.
**Josh Suereth** 03:43 Okay, but that update…
**Tigran Najaryan** 03:44 I don't know if he did, though, I…
**Reiley** 03:47 So, I checked, I blocked the PR, so if any update, I'll get notified.
**Josh Suereth** 03:55 Okay.
**Tigran Najaryan** 03:56 And on the deprecation of the, trust Propagator.
I think it should be fine, right? I also don't see why that would be a problem.
**Josh Suereth** 04:09 I think we just need someone to sponsor it.
So, I… like, let's check with Carlos and see if he'd like to push that.
But yeah, like, there's no… I think we accept it, for sure, it's just, do we accept, like, is someone gonna sponsor and drive it through?
That would be the only thing.
**Reiley** 04:29 So the first thing is for the TC to triage whether we agree or not, and currently it has a triage tag.
I think we should remove that and say it's accepted, right?
**Tigran Najaryan** 04:42 I think so.
Go ahead, Jack, you have your hand up.
**Jack Berg** 04:47 Yeah, so, I just wanted to share with this group what we're doing in declarative config around these concepts, these types, these components that were defined in the specification, but that we later deprecate. We don't necessarily remove. I think in some cases we do remove, actually, but these are the Jaeger span exporter, Zipkin span exporter.
the Jaeger propagator, and now the OT trace propagator. So, in all these cases, we have, like, a decision to make in declarative config, around these types and stability. Like, we're stabilizing the data model, and we, we have a decision to make, like, hey, are we going to permanently have an artifact in the data model for concepts that are deprecated or deleted?
And so, what we've been doing for now, because declarative config is new.
And, is we've adopted a stance of, we are going to delete these concepts from the data model and restore them in a deprecated status if we get user feedback that requests them.
Right? So, like, delete by default, but if anybody at all is using these things, we're open to re-adding them.
So that seemed like a reasonable position that doesn't, like, keep these dated concepts in our data model, like, forever, while also, you know, meeting users where they are. Just wanted to share that.
**Tigran Najaryan** 06:24 Okay.
Do we want to move to the… did you want to discuss more about OTEP stable by default more?
Josh, to the private topic, then?
**Josh Suereth** 06:35 Yeah, there's no… there's no… there's no changes of note to it, so I think we want to wait until that happens, and then… and then have that discussion. I just want to, like… I don't want to phrase this. That's the most urgent thing on my mind, is making sure we make progress on that, so that's why I just wanted to do a check. But let's move to private.
**Jack Berg** 06:53 Real quick, I'm taking the action item to adjust the labeling on this OT trace propagator issue, and I'll adjust it to accepted needs sponsor, and we can see if Carlos is interested in driving this.
Alright, I'll see you all on the private call.
**Josh Suereth** 07:09 Okay, see you there.
