SIG: Semantic Convention SIG
Date: 2025-09-22
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/78GnqjCxa2aZkjqzvhRclt2ZEcBSqSWrjJEIWRGWosKmHzqBi84ux65YrpNoEFzS.Mxbvk3XcsSCzNEZx
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:58 Oh, lol.
**Josh Suereth** 01:02 Hey!
How's it going?
**Liudmila Molkova** 01:05 Good morning.
**Josh Suereth** 01:06 Good morning.
**Liudmila Molkova** 01:07 It's good. It's good, I'm back. How are you?
**Josh Suereth** 01:11 Pretty good, pretty good.
I, I had an entire morning without meetings where I could actually think and do stuff. It's been… it's been quite a… some time since I had that.
**Liudmila Molkova** 01:22 Oh, wow.
That's nice.
**Josh Suereth** 01:29 Yeah But, to not get us distracted, we should talk, the,
Client-side SIG and entity stuff at some point.
But that'll be tomorrow.
**Liudmila Molkova** 01:45 I mean, during the spec call.
**Josh Suereth** 01:47 In the spec call, yeah, I was working on a proposal that I think we're gonna talk about in the spec call.
Anyway.
That was my morning. It was good.
Yeah, we should probably get started sometime soon. How many folks do we have here? Four of us?
We could do a little bit of triage, how's that sound?
While we wait for this to open.
I was looking at the triage board, there's two things on needs more approval.
Well, first of all, the triage document is listed as ready to be merged, and I really want to merge this. It has 3 approvals, all from core maintainers. I didn't see any…
Feedback that I thought was blocking.
So… I was just gonna check, do you think this is a blocking comment, Lyudmelon?
**Liudmila Molkova** 02:39 Absolutely not. We can resolve it and tackle it separately if we need to.
**Josh Suereth** 02:45 Alright, and then… There's some questions about Trask, about how to get things to render proper… appropriately.
Looks fine when I use Firefox. Okay.
Are those tweets…
**Trask** 03:02 I prefer to…
**Josh Suereth** 03:03 vote.
**Trask** 03:03 I don't know.
**Josh Suereth** 03:04 Yeah, okay, alright.
Cool. I think… I think I'm just gonna click Merge when ready on this one, and we can start moving forward with that.
That's on the merge queue, cool.
We don't have to resolve all comments in SEMConv? Is that just a spec thing?
**Liudmila Molkova** 03:24 I just resolved it.
**Josh Suereth** 03:25 Oh, it just hasn't updated my thing. Okay, got it. Weird. That it updates this, but not that. Alright.
Cool.
**Liudmila Molkova** 03:50 Is it just me?
We lost chat.
Okay.
So let's give him a sec to come back, and I'll prepare my screen in the meantime, in case he wouldn't
Okay, so I'm going to take over.
I hope Josh comes back.
So let's see what else we have on the project board. We just merged triage documents.
Oh, it's in the merge queue.
There are a couple of things that are… that needs more approval.
I think this, this one is pretty close.
Okay, so there are still some discussions, but otherwise, it seems to be ready to go.
**Josh Suereth** 05:19 Hey, sorry, my computer decided I had to update right now.
Okay.
I don't know if you have that…
you know, forceful, gonna kick you off of everything and reboot your computer, but it's fun. This one…
You already talked about this one? This is the one I really want to try to get through.
**Liudmila Molkova** 05:37 Yeah, there are some minor comments, it seems so.
Is there some particular question, this question you want to have?
**Josh Suereth** 05:46 No, I wanted to see if anyone has any, any concerns with the current state of things, just to do one last check, in case anyone wants to raise anything. And then, I did CC, I think… there was a comment with David Ashpole and the Cates group, just to make sure that we have
their blessing, but I think if you look at the approvals on this, it has,
one of the Kate SEMCOMF approvers, so I think we're covered.
But that is specifically a question about the current OpenTelemetry Prometheus, compatibility specification that, that's been David and,
Arthur have been kind of driving that lately, so I wanted one of the two of them to look at it. I think one of them did.
Anyway.
I also think that's something we can resolve later.
**Liudmila Molkova** 06:41 So you would rather resolve those discussions and merge it?
**Josh Suereth** 06:45 I think that discussion is specifically about a follow-on work for the Prometheus compatibility, yeah.
**Liudmila Molkova** 06:50 Okay.
So, yeah, I'm… let's do this. I'd like to check if this is necessary, because the moment we start merging Hugo stuff in that we don't understand, we will be lost. I'd like to check this one in, and I'll probably either leave a suggestion or resolve it.
And, maybe David or Arthur will chime in on your question, and then it should be ready to go.
**Josh Suereth** 07:18 Sounds good.
**Liudmila Molkova** 07:21 Christoph, you're here, do you feel comfortable resolving this discussion?
**Christophe Kamphaus** 07:25 Yeah, I resolved it just now.
**Liudmila Molkova** 07:28 Awesome, thank you.
And let's move it to… ready to merge, and once these questions are resolved, we should be good to go.
Then, I think then the last one is the upscreen name.
Let's take a quick look at it. I… it seems it has the code owner's approvals, but I've seen…
hansen to chime in with some additional comments, and…
Okay, they seem to be resolved now.
So it's now up to the general subconva provers to take a look.
Okay.
So, let's move on to the agenda.
We are out of our trash time box.
We don't have any topics.
So unless somebody wants to bring something.
Should we call it a day?
Okay.
**Josh Suereth** 08:56 I'm gonna ask one quick question. Maybe this is better for Wednesday.
Does anyone here interact with the attributes on instrumentation scope that…
may or may not be provided, and aren't well supported across different SDKs.
**Armin (Dynatrace)** 09:13 He attributes other than scope.
Name…
**Josh Suereth** 09:17 Yeah, there's name version, and then generic key-value pairs.
**Armin (Dynatrace)** 09:25 Not with the generic ones, no.
**Trask** 09:30 Yeah, I think Java SDK still doesn't support them.
**Josh Suereth** 09:35 Yeah. I know Java doesn't, for sure.
Which will tell you what I was doing this weekend, possibly.
**Liudmila Molkova** 09:47 Yeah, we had a discussion in, Jenna Isig.
Where we… been…
Okay, so the long story short, the typical layering situation. You have, GenAI spans, but they could be nested.
It could be GenAI span under Gen AI span. And this is where the span identity comes in, right? So we would have different identities for the spans.
And we've been thinking, Because we don't have a means to stamp it on the proto level, right?
We would want to stamp identity somewhere.
one of the things can be instrumentation scope name, and you have different tracers. This traces the…
Outer level, this traces the inner level.
But then… It's ugly. And then, where would we put this thing, that the span identity
But then there is no, Otlp property.
Instrumentation scope attributes was one of the candidates we've been discussing.
**Josh Suereth** 10:59 Yeah.
Yeah, we're looking at it in entity sake. There's, like, two things it does that I think are interesting, and we don't…
support in SEMCOM right now, right? So, span identification is something we need. I actually still think we need to add a field in OTLP for SPAN identity. And Ludmilla, maybe we just put
Maybe we end the call early, and then we just work on that proposal. What do you say? Let's just write it up. I think it's small, right?
**Liudmila Molkova** 11:28 Yeah, what… can you share your scenario for entities? I'm curious.
**Josh Suereth** 11:34 Alright, so, this… I'm gonna, I'm gonna briefly mention this in the spec sig next time, but if you look in the specification PRs, you'll see a draft that actually describes the problem.
I just posted it this morning, and we've been talking about this in entities for several months now.
But we were prototyping what would it mean to allow
to deal with session and browser, right? So, fundamentally.
people felt that Session belonged on resource, and that session doesn't last the same lifespan as the SDK itself.
Okay? So, we added entities into resource, which we think is independent of the session problem.
But then the browser SIG and the entity SIG decided we'd try to solve this problem together. And we put together a prototype of the SDK. There's one for Java that I was, toying around with.
that allows mutable resource, where you can actually provide entities throughout the lifetime of the SDK, and it needs to update signals. This works okay for logs and traces, because actually you attach entity kind of at the right moment.
And batching and all that kind of stuff isn't problematic, but it actually causes hell for metrics.
Because of how you need to aggregate and keep things separate.
And the other thing is, we were looking through OpenTelemetry, there's this notion that resource is the identity
of the SDK.
And there's a set of things that rely on identifying the SDK, like op-amps specifically.
There's a thing in OpAmp where it says you're gonna report resource attributes, but guess what it does? It divides them into identifying and descriptive, because you can't use all resource attributes to identify an SDK, there's way too many in there, and it gets ugly if you do so.
So what this OTEP is doing is saying, let's stop trying to put those two problems together.
of session and entity identifying attributes. So we have identifying attributes on entity and resource. That is already an OTEP that's been proposed. Let's continue with that as is. But let's solve session in a slightly different way. And so if you look at what this is proposing.
originally, if you look at… it's like OTEP 2-something, it's from TED, it's the very last spec BR. The top line is… is… sorry, the bottom line is what that would propose, which would be, you grab your meter.
You grab a histogram.
you discover your current session entity, and then push it into the entity provider, and when you do, all hell breaks loose in the SDK, because it has to shuffle data around and figure out where the new metrics are stored, and all that kind of stuff. Then you write your latency.
Right.
So, that was what the prototype had turned into, and it was getting very chaotic.
Right? Identity of SDK disappears.
Because you have mutable resource, so you don't know if you're talking to the same thing you were just talking to.
Alright, so instead, what this proposes is kind of a multi-tenancy scenario for OpenTelemetry, where when I grab a meter, I would say, cool, I want to grab a meter for this session.
And session entity would have a set of attributes that identify it, and I know it's about a session.
and then I can grab the histogram that records latency for a session and record. So I don't know if this solves your issue with,
what you were trying to do at Gen AI. I don't think it quite does.
But this, this is what we're kind of thinking about for that browser sig. Or for scenarios where I want to record data. I, you know, I have an identity, but I need to record data about sub-identities within that.
How do I do that?
**Christophe Kamphaus** 15:23 Yeah. For CRECD, that would also be very interesting.
**Josh Suereth** 15:28 Yeah, so right now it's still a strawman proposal, but we basically did a bunch of prototyping in
Well, I did a bunch of prototyping in Java, and
Maybe I'm arrogant about Java, but I feel like if my Java looks really terrible, it's a sign that I'm doing something terrible.
And that's what happened.
Although Trask can tell me how bad my Java code is, I don't know.
**Trask** 15:55 Your Java code is usually fine.
**Josh Suereth** 15:57 Okay, well, this was really bad.
So…
we're shifting how we think about entities, and I think it's going to impact semantic conventions, as you can see, right? Like.
understanding scope, understanding entity… like, entity association, I'm glad we defined it the way we did, because it could be that a metric requires an entity to be in scope, and that entity might be from instrumentation scope, and then we don't care.
Right?
So, I kinda… I think that we… actually, all of this fits well together, but I wanted to call out what we're thinking through.
**Liudmila Molkova** 16:36 So the proposal here would be to actually report session information on the instrumentation scope.
**Josh Suereth** 16:44 Yeah, so instrumentation scope will have zero or more entities attached to it.
The API would let you attach one. Maybe we allow more, but we want to prototype first and see what it looks like.
**Liudmila Molkova** 16:58 Okay.
That's interesting.
**Josh Suereth** 17:01 Yeah.
Yeah, there's a lot of, you can see other, like, future direction thoughts in there, and, like, questions to answer. It's a… it's a shift in direction, for sure.
Cool.
**Liudmila Molkova** 17:23 So then there are no more topics.
Okay, calling 1, calling 2, calling 3.
Have a great day, everybody.
**Christophe Kamphaus** 17:39 You too?
See ya.
**Trask** 17:40 Nails.
**Liudmila Molkova** 17:41 Thank you.
