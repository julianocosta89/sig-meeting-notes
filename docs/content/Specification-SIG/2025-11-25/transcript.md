SIG: Specification SIG
Date: 2025-11-25
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 01:22 Hello, Aaron.
**Austin Parker** 01:27 Good morning.
**Jack Berg** 01:28 Hello.
**Liudmila Molkova** 03:10 Hi, everyone.
**Austin Parker** 03:12 Reading.
**Pellared** 04:05 objects.
Don't know.
Thank you, sir.
**Tigran Najaryan** 04:15 Robert, your microphone is hot.
**Pellared** 04:18 Oh, sorry.
**Austin Parker** 04:49 We wanna get started?
**Josh Suereth** 04:55 Yeah, hold on, who's, who's on the TC list to run this meeting this week? I was just checking.
Is Armin here, or was he able to make it?
**Austin Parker** 05:09 I do not see Armin.
**Josh Suereth** 05:12 Alright, I'll… I'll run it on his behalf. He might be… he might be out. He… he was… He responded to the, we have a security duty, so he already responded to that today.
I just don't see him here, so yeah.
I can present.
All right, Austin, do you want to kick us off?
**Austin Parker** 05:33 Yeah, this is just a quick announcement. We'll publish a blog and put an announcement up, but for those that remember.
Last year, we are gonna do, like, a two-week, end-of-year sort of quiet period.
Same dates as last year.
I don't quite remember what those are, but basically the week the weeks of Christmas and New Year's, and the suggestion is that maintainers and everyone just go ahead and, you know, cancel meetings and da-da-da-da-da.
Just leave everyone a little holiday break.
And… I'm dressed up.
Relax.
**Trask Stalnaker** 06:17 Pablo already canceled all the meetings.
**Austin Parker** 06:20 Great!
**Trask Stalnaker** 06:21 Yeah…
**Austin Parker** 06:23 Boom.
We will put a banner up, too, on GitHub, I think. That's what we did last year, so…
**Tigran Najaryan** 06:32 What exactly are the dates? Sorry?
**Austin Parker** 06:36 The 20… The 18th through the 2nd, or is it the 26th?
Wait, is this the right… no, it's January. Good lord.
I think the 22nd through the 5th, right?
Does that sound right, Trask?
Oh, dude.
Yeah, so Monday, December 22nd through Friday, January 12th, so effectively the… The fifth.
And we'll have a GitHub announcement on December 15th. Great.
**Tigran Najaryan** 07:31 Thank you.
**Josh Suereth** 07:41 All right, next up is Luke Millen. You want to talk about Zipkin deprecation?
**Liudmila Molkova** 07:47 Yeah, this is just a quick ask last time we discussed, deprecation of Zipkin Exporter.
That PR is merged.
We've got some feedback from, Zipkin maintainers as well, and we discussed that we want a blog post. I drafted a blog post, and it's a very short one, announcement kind of thing. I would appreciate your reviews.
**Josh Suereth** 08:24 Alright, awesome.
Let's move on then. Next up is Evo. Evo? Did I say that right?
**Ivo Anjo** 08:31 Yep.
So I'm…
**Josh Suereth** 08:35 By the way.
**Ivo Anjo** 08:36 Yep.
So yes, hello again. So I, I attended the specification meeting a few weeks back, talking about this work, which is… From the, kind of, profiling SIG side, we're trying to solve this challenge of, since the, OpenTelemetry BPF profiler sits outside of the process, and so outside of Outside of the tracer, it lacks some of the context of, what's going on, and what's the configuration that was set on the tracing SDK libraries.
And so we came up with this proposal for, having this mechanism where the, SDKs can kind of publish, oh, here's some metadata, and the profiler can read it, and so the, we can do, like, better correlation of this profile matches up with this, things that were going on in the SDK, and I opened an OTEP with this, and I've gotten some feedback, but it's kind of gone quiet, and so I showed up to ask people for, to give it a stab, and to complain about it. I want… I won't complain.
**Josh Suereth** 09:50 One thing that would help, is, do you think there are contentious parts of the ZOTEP that need more attention than others?
I… for context, I did read through this, so I… I can… I can, seed some conversation here, but I just wanted to ask you first if there's anything you'd like to, Kind of raise here that you think people might disagree with, or that have had comments so far?
**Ivo Anjo** 10:14 Hmm. I think there's, there's kind of a section on, like, kind of problems that we, that I, that I, are identified already, and some of the why it's not such a problem, but, I think the, the main two things that may be a bit contentious for the discussion, is, one, the actual, format that we're, that we have right now. Like.
like, what's the name of the field? Is protobuf exactly the right thing, or should we do it, like, slightly different?
And the other thing is that right now this is, kind of Linux-focused, and, because also the, OpenTelemetry BPF Profiler also is, like, kind of focused on Linux, and while, we can it's possible to have, like, something like this on Windows or Mac OS. We're trying to scope it out.
of those OSes for now, but maybe that's kind of a point of contention, where people are saying, like, we shouldn't have something that's just for Linux.
So, that's the two things that I think have come up more in discussions so far.
**Tigran Najaryan** 11:25 Does this… couple questions, I guess. Does this, this is tied to a process, right? So, a process publishes this information.
Do we, what happens if there is a… an application with multiple processes, but a single Autel SDK.
Is there an expectation that All the process is published, one process publishes.
And I think we may have also the opposite situation, when there is a single process, but multiple applications.
Each having its own SDK. Is there a one-to-one mapping, is the question I'm asking here.
**Ivo Anjo** 12:02 Yes, right now, this kind of assumes a one-to-one mapping between the SDK and the process.
I'm not sure how it's possible to have an SDK and multiple processes.
But the reverse is possible, like, if you have, like, an application server kind of thing where you have multiple SDKs.
Right now, this kind of assumes there's only one. It's not impossible to expand this to have more, but right now, the specification is kind of assuming that there is at most one context, per process, and that we, and yeah, and if a process hosts multiple SDKs, then, it's not Kind of… it's handled by the fact that saying, like, there's all at most one.
**Josh Suereth** 12:51 Okay. So, multiple processes for an SDK is possible for, like, Python, if you fork.
the process, you will actually end up with multiple SDKs. It's actually a problem that the Python SIG ran into. Like, having… like, when you call fork, essentially, you can end up with multiple things that theoretically are from the same source. So just for context… Yeah.
But… but you're not the only thing that has… that that's problematic for, I would say, with an SDK that forks and SDK.
**Ivo Anjo** 13:26 For forking, it's actually, not… like, forking is already predicted there, and it's already handled by the… So, from what I get in the specific… in the, Tracer, in the SDK, sorry, let me go back.
There's a field there, which is, I think the deployment ID. Let me check up the field name again, I forgot about the field name.
there is, a field which is the service instance ID. So the service instance ID is expected to change, at least from the specification in the semantics, in the auto semantics repo, I see that it's supposed to change when the process works.
So, I think for the purposes of this spec, that is kind of identified as a different tracer, even if they were born from the same one.
And the way that this implementation works is that if a process publishes this context, and then forks, the child will not inherit the context. So the child will have the option of either publishing its own context, it will not inherit by default, or it never publishes and it's not… doesn't have a context.
Yes.
**Josh Suereth** 14:58 Go ahead, Rob.
**Pellared** 15:00 Have you considered, how it would work with OB? So, for instance, if you have an application instrumented with eBPF instrumentation, how it would work with the eBPF profiler?
**Ivo Anjo** 15:16 No, I think is the short answer. I haven't… I haven't looked into that.
**Pellared** 15:27 Would you add it to a to-do list?
Or something like that.
**Ivo Anjo** 15:33 Can you… Or just the null ?
**Pellared** 15:36 on just… You want the command?
**Ivo Anjo** 15:37 Yeah.
**Pellared** 15:39 Okay, sure.
**Ivo Anjo** 15:39 Yes, like, send me a… add a comment on it, and I will look it up and update the document. Yeah, that makes sense.
**Pellared** 15:46 Thanks.
**Josh Suereth** 15:49 So, one thing I want to call out, this mechanism… I understand the mechanism, I understand the need, I understand why it's Linux-only, because, like, doing these kind of shenanigans will have to figure out for different things. Totally get that. This is actually where I have most of my contention, is actually this… definition here. For context, I want to show you some work that has been done in our specification around what I'm calling, kind of, push-based identity.
So, inside of the entity spec, we're actually trying to make a way that we propagate these with environment variables, okay? Now, I know that you can't use environment variables, but if you look at this specification and what is passed.
I would expect that I should be able to do the same thing here with whatever I'm passing to eVPF Profiler, so that we get the same behavior.
And this is kind of the direction that we're going forward with, of, you know, we want to actually pass the entity type, we want to pass the schema URL, and we want to pass identifying descriptive attributes separately.
So I think for the purpose of what you need, you could, like, limit what you take in to say, okay, cool, I'm only going to take in identifying attributes.
I might need to pull in schema URL, because we, like, without schema URL, some of the transitioning we want to do of, like, the version of data.
becomes problematic, but we can have that discussion as well. And then the type is the other thing. So, like, am I proposing a service type? Right now, you're hard-coded to only accept, like, the service-related things.
And so, this actually opens up flexibility. So, if we're actually reporting about a process which is not a service.
Which is a thing we'll want.
This is a bit more flexible with what we could propose, and it's not just string-string resource attributes, right? It's a little bit more sophisticated. So.
I would… I would say that for your proposal here, I would… what I… what we want to see is this notion of passing resource identity.
in a composable way, and via different mechanisms. For entities, we've defined this new entity propagation thing, which we want to take over, OTEL resource attributes, specifically because this is more composable.
This format actually gives us the ability to do merge logic better, and understand conflicts better between different sources of identity.
So… so we can actually merge things between environment variable and process memory and that kind of crap, if we wanted to.
So that's why, like, the other, the other idea behind this is, A process might get its identity from the thing that runs the process, and then it would provide that in the memory map for you, right?
So, the environment variable is a way to get it to the process, not to get it out of the process. You're defining the other thing. I'd love to work with you on this to make sure that this lines up, but I do think that we want to go back to your protocol buffer and make it actually support, kind of, the use cases we're thinking about when we think about resources in OpenTelemetry going forward. So, it should align to at least, in my opinion, it should at least have type, ID, and schema URL.
That… that we can all propagate in some kind of fashion.
Let me go back to your thing. Were there any other comments? Sorry, I keep forgetting to raise my hand because I'm presenting.
**Jack Berg** 19:18 Josh, I think we have a bit of a chicken and egg problem with that, right? Because what you're talking about is still a proposal. Are there… are there concrete implementations in a plurality of languages?
**Josh Suereth** 19:34 Well, the implementation, we're starting to propose to SDKs now. So, like, the one for Java, I just rebooted it, so it's gonna land pretty soon.
You're right that, like, we have prototypes, and we have an OTEP, but this is the direction we're moving, and it's already supported in our protocol. So if you don't actually implement it now… again, this is… we're talking about an OTEP, so this is future work.
Right? So, I think we need to support where we're going.
And support where we are now, but there is no path where what you've proposed will actually support entities going forward.
So, but there is a path where if you use entities now, we can produce resources, no matter what. So, I would say since the OTEP around entities is already approved, since the specification's already written for these things, and since the implementations are going to start landing very shortly, I would align against that specification with an OTEP.
If this were, like, a specific implementation that we're not trying to standardize across a hotel, that's a different story.
**Jack Berg** 20:34 Yeah, yeah, I definitely agree with that, and, you know, I guess I'm just… I'm wondering if Ivo can get, you know, have his cake and eat it too by adjusting this representation from using a sort of bespoke protobuf type to just using the resource protobuf type as defined in the protorepository, right? So that's, like, what we have now and where we're going is represented in there, because the entity stuff is, as you said, it's already landed in the protorepository.
**Tigran Najaryan** 21:07 Exactly. I don't know why we just don't use the resource message as it's already defined. It has the attributes, it has the entities.
all the work of introducing entities in a backwards-compatible way is already being done by Entity 6, so why even invent a new protobuf format? I don't see the need for that.
And the whole, hardcoding of some attributes also looks weird to me. I don't know why we would do that, whether… Everywhere else, we just have key-value pairs and some conf for the common attributes, or commonly used attributes.
It's much simpler just to refer the resource message and you're done, right?
Since you're already taking the dependency on the protobuf, Format as a concept.
just say that the format of the payload is a resource in OTLP. You're done.
I'm maybe missing something, but…
**Josh Suereth** 22:10 Over the season.
Yeah, what's your size limitation on the amount of memory you can store here, or is it somewhat flexible?
**Ivo Anjo** 22:19 It's, it's flexible. Or at least, sorry, yeah.
**Jack Berg** 22:22 Are you gonna say, Josh, that, like, resources can get pretty big?
**Josh Suereth** 22:28 No, no, no, if they were using a technique where they were trying to pack this in a limited set of bytes, like, they're saying, cool, I have 256 bytes, and I have to pack everything into it, there's a… that means that we actually can't allow lots of extension, because we have a fixed size. You know, like, just taking our first strings is expensive. But if this thing can grow.
somewhat flexibly. I think resource is a reasonable size there, but if it were like, hey, I have to pack this into 64 bits, or pack this very, very tightly, we have to be very judicious about what strings we use, and using an integer dictionary is more efficient.
So that's all I wanted to understand. If you're trying to, like… there's a header that's size X, and I have to fit it into that header size, I get wanting an integer dictionary, but if it's not that, if this is flexible.
Then we should just use resource, because it's not… there's not a big difference between the two.
And we're not going to limit ourselves, right?
**Jack Berg** 23:19 Yeah, and what I was gonna say, if we're worried about size, is, you know, just because we're using the resource proto-definition doesn't mean we need to convey all the information that is in a resource, including all the descriptive attributes. We can use the proto-representation and pare down the information in it to only what is required.
**Tigran Najaryan** 23:42 Is size even the problem? You should be able to allocate as much as you need, right?
**Ivo Anjo** 23:51 Yes, in this situation, it should be, and this is not expect… this is kind of a fire and forget. You should… like, you'll publish this in the beginning of the process, and unless those things change, and I'm guessing those things won't change very often, you'll not do it again, so… I think a few megabytes is probably fine, and then forget about it, and then any outside reader can peek at it.
**Tigran Najaryan** 24:15 Yeah, and realistically, a resource is never megabytes, right? It's maybe kilobytes at most.
So…
**Ivo Anjo** 24:23 Yep.
**Josh Suereth** 24:29 Cool. So that was a… that was a bunch of feedback initially. Is there anything else you think might be contentious we want to talk through for this proposal?
**Ivo Anjo** 24:40 I think those are the main things, and as I… as kind of, like, we suspected, they got conversation and feedback out of it, so I think that's the main… things, and yeah, I'll… I thank you for the feedback, and I will iterate on it and come back, and annoy people again.
**Tigran Najaryan** 25:01 Is there… is there an expectation that this information is… republished periodically for when it changes, especially if we include entities there. And if that's the case.
How are the… How do you solve the concurrent access issues here?
Whoever makes… is there, like.
Do you atomically update the pointer to the payload? Is that discussed at all in the OTEP?
**Ivo Anjo** 25:31 It is, so the intention here is that this will contain things that don't update very often. In particular, there's something else that we're working on, which is, for instance, it would be… we would also like to have things like trace ID and span ID when there's a… ongoing traces, but this will not fit here, it would fit somewhere on a separate specification that will work in a different way, because that will kind of update very often. This is kind of the… things that are kind of fixed and don't update very often about the process. Any… the other… the things that change very often would go, elsewhere.
To answer the question of concurrency and updates, yes. So, the way, we do describe in Yotep what's the publishing protocol and how to read, and, it does describe and include, like, the protocol for reading and writing this does include.
How we handle this, like, update, and make them safe.
**Tigran Najaryan** 26:36 And is there an expectation that whoever reads this information should be polling for the changes?
**Ivo Anjo** 26:44 Not necessarily. So there's kind of two options, and we've validated that both work. So, you can either poll for the changes, if you choose so, or, it's actually possible to, hook on.
The… on the final step that we use to kind of publish this information at the kernel level, so you can use that as a kind of… Events are to tell you, oh, this application just published the… published an update.
So, and we've, we were able to get both working.
**Tigran Najaryan** 27:18 Okay, I should just go and read the OTAP.
Instead of asking questions here, I guess.
Thank you.
**Josh Suereth** 27:30 Well, this is, super exciting, so, glad to see this continue, and thanks for bringing it here.
I think it's time to move on.
Awesome.
Let's move on to Robert. Do you want to talk about stabilized Enabled API for Synchronous Instruments?
**Pellared** 27:49 Yes, can you share?
Thanks.
So, I think during the last specifications igniting call, I told that I would look into it, so I checked how implementations are implementing it.
So, basically, if we implement… languishers are implementing the enabled own instrument, like, on synchronous instrument, like counters, etc. I think for .NET, it's also for asynchronous instrument as well, if I remember correctly, but this is on basically as library, so it's basically in the .NET, kind of standard library itself.
And, I propose to sublease it, because it's being implemented for a long time. I don't think anything there is controversial, and I know that for sure, Collector would benefit for it.
Because right now, they are making, basically, type assertions in Go to… to make use of… to make use of it in their codebase. So, that's it, waiting for feedback, reviews, etc.
Any questions here?
**Carlos Alberto Cortez** 29:04 Yeah, I have a small question. Other than .NET, do Java and Google actually implement this? Because… I think they implement the API, and on the second point.
Previous times we made something stable, like, for metrics, we were wondering whether we should make the API and SDK parts compatible. The last one.
corporate excessive.
questions, number of questions.
like, how representative we think that Go and Java are.
So, to cover the rest of the…
**Jack Berg** 29:42 So, I was actually just looking up what the SDK behavior of this was, to refresh my memory, and I guess I'll share a link in the chat so other people can follow along.
**Pellared** 29:54 Maybe you can post it in the PR itself. What do you think, Jack?
**Jack Berg** 29:58 Well, I, I just… so I just want to say that, on the SDK side, enabled, it, it, it… responds according to two bits of information. Views, which are, you know, well accepted, well understood, and well implemented, and then this other concept, which is, like, the scope config. So, where, you know, you have this ability to turn off individual scopes, or enable or disable them, and that's, like, a language or a signal agnostic concept. So, you know, tracers, loggers, and meters all have the ability to turn them on I don't know.
And that scope config concept, while, you know, I like it a lot, I'm not sure it's widely implemented yet.
And so, and I know Go has expressed some reservations about implementing it at all. And so, like, you know, I have no problem with stabilizing this at the API level. I think it's, you know, at least the view part of the SDK is still a very useful thing to have, and I don't think there'll be much argument about that.
But that's a little bit of the context.
**Pellared** 31:04 So what I can say, if I remember correctly, because I was looking at it a few days ago.
I think in Go, we implement it also on the Vue side. Tyler can correct me if I'm wrong, and maybe Dave as well. And I remember also the no-op implementations returned by the no-op meter provider also. Returns always false.
And I think everything is even described in the SDK, in the SDK part of the specification, which you can double-check when reviewing this part, but I didn't want to make the SDK part stable, because I think implementation specifics, we can basically, you know, basically postpone.
So, basically, these are defined in the SDK specification, but I do not think we need to stabilize this part you know, together. Also, I think we can refine the metrics, enabled… the SDKs enabled specification a little bit before going stable, which is the other PR, which would be the next one.
**Jack Berg** 32:06 I don't think we need to make the SDK stable, but if we wanted to do that, one way to approach it would be to take this SDK-enabled section and to have it be mixed stability, where the view portion of it is stable, and then the scope config portion of it is in development.
Because I don't think we'll get much argument about the view part of it.
**Pellared** 32:28 Yep. Worse.
**Carlos Alberto Cortez** 32:32 Good.
**Pellared** 32:34 I'll work on that, on Disney as well.
**Carlos Alberto Cortez** 32:38 And sorry for asking again, but do you think that… I mean, I'm just asking, I'm not saying it's not just asking, like, Go and Java, I mean, and .NET for that matter, are that… are those representative enough?
Or I guess that the other way to, ask the question is whether the rest of the maintainers are fine with this, especially that only the API would be stable, which is, I think, safe.
**Jack Berg** 33:02 Yeah, let's see, I don't see, solid representation from other maintainers on this call here, so I think, you know, we're gonna get a biased answer.
**Carlos Alberto Cortez** 33:14 I haven't seen that, yeah, good point.
**Pellared** 33:16 So they agreed.
**Jack Berg** 33:18 Yeah, like, yeah, Java and Go are representative, this is good to go.
**Pellared** 33:23 Yes!
**Josh Suereth** 33:28 I'll say, I do think… I do think, if you add .NET in there, I know that those are the three that have the most divergent implementations.
So, I do think we need other maintainers here, but the ones that I would be worried about are actually more .NET and Java and Go. Specifically, these two are very different.
Go, I know, has… always has its own set of challenges, so I just… Go is always interesting on its own.
Versus every other SDK. But in this case, I think Java and .NET diverged significantly, how they implemented metrics. So I would say that, like.
It's not a bad set.
But we should get other maintainers to comment.
**Carlos Alberto Cortez** 34:25 Thank you.
**Josh Suereth** 34:27 Alright, should we, should we move on?
**Pellared** 34:31 maybe first go to the last one, Josh, because this is basically… Yeah, so… Exactly.
Allow instrument-enabled implementation.
So, this is already a follow-up after this enabled, so basically this is the part which describes the behavior of the SDK enabled. So, this is more… almost an editorial change, so it basically looks… because the enabled on, enabled on log… on logger.
is all… already has, I think, this mixed stability, which Jack called out, if I remember correctly. So basically, this, basically mimics, the structure and the way it is defined in Logger.
enabled.
It also allows, you know, basically also opt-in, additional features.
So, instead of having, you know, if none of this is defined, it needs to be true, then just say it should be true, because there may be other aspects, like, you know, I don't know, lazy.
lazy, I don't know, some lazy evaluation to get rid of some atomics, etc, which we were describing a few times ago, so I think this is just a safer language.
**Jack Berg** 36:04 Yeah, I'm on different… I'm indifferent on this. I think, you know, just saying it should return true, it leaves enough wiggle room for exceptional cases, but I don't know. I'm splitting hairs. Like you said, this is probably editorial, or close to editorial.
I'll leave a comment and approve.
**Pellared** 36:25 Hmm Also, if there's… you have a suggestion, Jack, we can, you know, we can change it in both specifications, logs and metrics at the same time, it's not a big deal.
**Jack Berg** 36:38 Oh, that, this is the same language from logs, that's what you were saying?
**Pellared** 36:42 Yeah, exactly.
**Jack Berg** 36:43 Okay, okay, I got it now, then, yeah, I… I… I prefer consistency, then.
**Pellared** 36:50 Also, you know, I'm a human. I may have made a mistake. The thing that I said doesn't.
**Jack Berg** 36:54 Alright, I'll double check before approving.
**Pellared** 36:57 Yeah, exactly.
And I think we can go to the last one, which is second from the bottom.
Yeah, so this is the… This is the second step, which, after, I think, the half-hour-long discussion from the last SEC meeting.
So, I tried to add clarifications both in the main README of the logs specification, as well as added, this a section for ergonomic API in Basic API. I'm not sure if it's… I think, in theory, it is not needed, but given we have so many conversations around it, I think it may be helpful for even us that we have some section, and I open to any suggestions. I tried to basically, we could remove it, we can keep it.
I don't think anyone will have a strong opinion to remove Kirsten, just thought, and really, I think that this is not needed, but if anyone feels that it will help them, other maintainers, then I'm fine keeping this, I don't know, you know, basically sections with 3, with 4 sentences, or something like that.
And, yeah, any comments on this? Anyone who had a chance to look at this so far?
**Tigran Najaryan** 38:29 I think it's fine to have a… Clarification or a recommendation about additional APIs that the languages may implement.
I haven't had a chance to read the actual wording there, but I think, The idea is, it's… It's totally fine Even if we don't prescribe exactly how that API is implemented.
I'm with you. We had… we had people asking about and being confused about how the API is supposed to work.
So, some guidance in the spec, not heard.
**Liudmila Molkova** 39:09 And so the point is to provide… by calling out that there could be an ergonomic API, to explain.
That the one that we have is not ergonomic.
And it just brings more clarity into the spec language.
**Tigran Najaryan** 39:27 Yeah, I'm not sure about calling it ergonomic versus non-ergonomic API.
kind of implies the existing one is sort of a wrong design, why would we have non-ergonomic?
**Liudmila Molkova** 39:43 Low level, let's call it the.
**Tigran Najaryan** 39:44 level.
**Jack Berg** 39:45 Yeah, that's what I would have said as well.
**Tigran Najaryan** 39:47 Yeah.
Yeah, but otherwise, I think, yes, it's good to have this sort of Clodification in the spec.
**Pellared** 39:57 Also, if you have proposals for better names, yeah, this is always hard.
**Liudmila Molkova** 40:08 Low level and convenience.
But ergonomic sounds fine to me, it's just… it sounds like non-ergonomic people don't like it, but ergonomic sounds fine.
**Tigran Najaryan** 40:18 Yeah.
Yeah, I like low level and convenience.
**Pellared** 40:25 Hey.
I think it's the first time I put more minutes than it actually needed… was actually needed, which I'm happy.
Thanks.
**Josh Suereth** 40:38 Awesome. Should we move on? Carlos, you want to talk about the stale period?
**Carlos Alberto Cortez** 40:44 Yeah, we don't have to discuss that here, but basically, if you could open the PR, just… For people to… in case you want to… discuss, have an opinion about this one, about keeping PRs open for longer.
Without marking them as stale. So, yeah, we can just… it's not super important, but I think it could be helpful. So please, if you have any opinion, just post your comments there. That's all.
**Tigran Najaryan** 41:14 Yeah, I think Carmen commented there that 3 months may be too much, and I agree with him, so maybe we… let's double what we have, and we'll see whether that's enough.
**Carlos Alberto Cortez** 41:26 Yeah, that's my personal preference as well.
**Josh Suereth** 41:37 Boop.
Oh, you know what? I forgot to click share this tab. Sorry, everybody. Yeah, this is the proposed change for reference, and yeah, I absolutely agree. The 14 plus 14 seems… Way better. And I also want to make a comment as someone who reviews spec PRs and makes a bunch of spec PRs that go stale and get closed, is I've actually appreciated when this thing tells me that I'm not paying attention to something, or that it's no longer a priority.
So… I think that we absolutely do not want to make it 3 months, because then the amount of croft we'll have in the repo will just increase.
So, if it's… if it's something that takes 3 months to get through, reopen it and mark it unsale. In fact, we just did that in the entity's sake for one of our OTEPs that we, we let stagnate a bit to work on some things, and then we're bringing it back. So, I think that's by design.
**Jack Berg** 42:32 Likewise, in the config sig, we have a long-standing PR to stabilize some stuff, and, you know, it got derailed by me going out on parental leave, and we're gonna reopen that soon. But, you know, for the time being, it would have been fine if it just had closed, or been marked still and closed, and then we reopen it when it's ready.
**Josh Suereth** 42:53 Alright, so I would recommend we all thumbs up Armin's comment here.
Well, it looks like it already started happening. Okay. But yeah, let's, like, 90 days, I think, is way too long.
And I really like the idea of one month, because that gives us a little bit of flexibility. If you miss one.
One week, and it goes an extra, not the end of the world, but, reopening these is not, in my opinion, not a big deal if it's something you're actively working on.
So… Cool.
Any other agenda items?
Has there been any status on the OTEPs around the stability proposals from the GC?
Is that something we need to start working on actually putting OTEPs together? And who's on that, is one thing I wanted to ask, because I kind of expected to have more discussion in this meeting here, but I didn't see anything.
I think you… I think Austin isn't here anymore.
Maybe Trashky could speak on their behalf?
**Trask Stalnaker** 44:12 Can you hear me now?
Yes. Sorry, yeah, I was looking for… I noticed Austin, isn't here. I think that Austin is on point for driving, the next steps there.
**Josh Suereth** 44:39 Alright, cool. I was just, I guess we'll call it here, but, Yeah, given… given the blog post went out, I'd love to start working on those OTEPs and kind of discussing through those. If you need more folks to kind of participate or split up the OTEPs and the… the work, let's, Let's do that.
Alright, anyway, thanks everybody.
We'll see you all next week.
**Liudmila Molkova** 45:09 Thank you.
**Jack Berg** 45:10 Thanks, bye.
**Armin (Dynatrace)** 45:11 Thanks, bye.
**Reiley** 45:12 Thanks.
