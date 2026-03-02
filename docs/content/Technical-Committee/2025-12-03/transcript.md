SIG: Technical Committee
Date: 2025-12-03
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/jkaxurC03u6S-GmGOAFqm-U2cFIFQTTAkGcoYCo7-CJ8U5-5hLYO1EH8a68U0ehY.PXUXnktiR8K5F_I_
============================================================

## Zoom Recording Transcript

**Josh Suereth** 02:50 Hey! Sorry, the semantics Convention meeting ran long.
**Tigran Najaryan** 02:55 Hey, morning. Good morning.
**Josh Suereth** 02:57 Not bad, how are you doing, man?
We haven't had a chance to…
**Tigran Najaryan** 03:04 talk about the… Dictionaries and stuff.
**David Ashpole (dashpole)** 03:10 Probably time we, maybe.
**Tigran Najaryan** 03:12 Do a live session or something like that.
**Josh Suereth** 03:14 I… I think we need to, yeah. I… it's funny, because the… my main thing is I want the dictionary at the top level.
not… I don't necessarily think it's needed for resource, but I think it has to be at the top level, from what I was seeing with the benchmarks.
**Tigran Najaryan** 03:30 Yeah.
The benchmarks…
I'm not sure I understand them, to be honest. I probably need to go look at the actual source code of it, too.
To get a sense of the numbers, because they… they look a bit surprising to me.
Could be that I'm just not…
I'm just not understanding what exactly is it that they are measuring.
So, probably need to spend a bit more time on that.
**Josh Suereth** 03:57 I do think it's true that, like, the way that profilers are captured is not… would be surprising if you're used to spans and logs and metrics. Like, it's… it's subtly different in fun ways. Yeah.
**Tigran Najaryan** 04:10 Yeah.
**Reiley** 04:15 Hey, hey, son.
Sorry for being late, I have to reboot my computer, so, shall we start, or we already started?
**Tigran Najaryan** 04:26 We haven't, we were just chatting.
I looked at the inboxes, they are empty, so…
I don't see anything in the agenda, to be honest, so I don't know. Do we have anything?
**Josh Suereth** 04:42 I do want to talk about the profiler and the.
**Tigran Najaryan** 04:45 We can do that, I guess, if there's nothing else, yeah.
Could spend a bit of time on that.
**Reiley** 04:54 Yeah, then… go ahead.
Yeah, so mostly, I think…
**Josh Suereth** 05:02 there's two things I want to address. There's, like, the… what's reasonable for us to ask of the profiling SIG, and then there's, like…
How do I want to phrase this?
I think it's fair for us to ask them for benchmarks.
I think it's fair for us to ask them to justify their needs. I think it is not fair for us not to read those benchmarks before we start blocking things, or, like, continually ask them for benchmarks repeatedly.
Because they've spent about a year doing benchmarking and proving their needs. And so, at this point, we need to go read those benchmarks, understand what it is they're telling us, and respond to that.
So that is the main thing I wanted to talk about, actually, because, like, the SIG has been spending a significant amount of time on benchmarking. If we're not happy with what that is, we should ask them to improve those benchmarks.
But I do feel like every time they've asked for, hey, we need this thing in OTLP because profiling's weird, we say, cool, go benchmark it. They benchmark it and say, we did benchmarks, we looked at what you proposed, we looked at what we proposed, here's what it looks like, we'd like to do this weird thing, and then we say.
oh, we don't want to do the weird thing, go do more benchmarking, right? That's… that's what it looks like if you look at the history.
Over the past, like, 2 years.
So…
I think it's fair for us to ask for benchmark, I think it's fair for us to, question what they're doing.
**Reiley** 06:31 But I…
**Josh Suereth** 06:32 I think we need to spend some time understanding profiling, so that that SIG can be successful.
**Tigran Najaryan** 06:39 I mean, I generally agree with you. I may be guilty of some of the lack of the understanding myself.
The… I think that the very last change they made with the dictionary attributes in the resource, that's new, right? We haven't seen benchmarks for that yet. This is the first time we're seeing that.
**Josh Suereth** 07:00 Yes, that is, that is new, yes.
**Tigran Najaryan** 07:03 Yeah, so it's not like… were… kind of…
running in a loop, asking for the same thing over and over in the same situation. The situation is different. I mean, but the proposed change is different compared to what they were doing in the past.
**Josh Suereth** 07:19 I think the main thing that we ran into there was, they had asked for the dictionary to be at the highest level, and we asked them not to put it there.
And then when they actually implemented everything, this was what we discovered, was they weren't filling out resource accurately.
So because they weren't putting any attributes in resource that were relevant to doing correlation, you actually couldn't correlate a specific profile to something else at a resource level.
**Tigran Najaryan** 07:46 It wasn't a proper resource anyway, right? So it was sort of a surrogate of a resource.
**Josh Suereth** 07:51 Yeah, exactly. So, like, to me, there's a set of things that we need to hold to and say is important. And we did have a discussion in the TC about that resource decision. I don't think you were there for that one, Tigran.
But,
To me, we have to figure out what's important to us. I think the data model in OTLP is the important part. You have a resource, you have a scope, you have a signal.
You can group by resource, and that makes sense. That's the thing I want to make sure that they provide.
The fact that they need a dictionary, I think they've proven through benchmarking that this is necessary for profiling.
At least for the signal itself.
And so, the other thing that we're seeing is when you need to profile a host that has multiple containers within it, which is what our eBPF profiler is doing, if that dictionary is not shared across all the processes, it actually becomes very unwieldy.
**Tigran Najaryan** 08:51 Can you clarify something, Josh, if you had a chance to look into the details of that?
how many resources are in the dataset that they would use for the benchmarking? Because it looks…
very weird to me that you would incur 30 megabytes of penalty just because you're not sharing resource attributes. Like, how many attributes can there be?
**Josh Suereth** 09:14 It's not that they're not sharing resource attributes, it's they're not sharing the dictionary between the resources.
**Tigran Najaryan** 09:20 I get it, but how many resources are there? Like, is it…
Millions of resources.
I think it's, like, empty the case.
How many?
**Josh Suereth** 09:29 I think it's, like, 10 to 20. I need to take a look again.
**Tigran Najaryan** 09:32 how can you… if you have 10 to 20 resources, and they don't share dictionaries, it's still a couple hundred attributes? How can that be 30 megabytes of extra payload?
**Josh Suereth** 09:44 It's not… it's not a couple hundred attributes, because you're still thinking it's just resources. They're trying to share the symbol table of the processes.
**Tigran Najaryan** 09:54 So, it's not about the resource attributes, it's about all… everything that has a dictionary in AI.
**Josh Suereth** 09:59 That's the message I've been trying to send. That dictionary has to go across the resources.
**Tigran Najaryan** 10:04 So the change they made there wasn't just about resource attributes, it's about splitting the dictionaries for everything, is that what… but that's not what we asked for, right? Did we ask for that?
**Josh Suereth** 10:16 So… We… we… okay.
We have to decide where to have consistency, but the important thing they need, the dictionary should be shared across all the resources in that batch for a particular host.
**Tigran Najaryan** 10:30 I'm with you on that. I think that Boddam was asking for the opposite of that, because that complicates batching.
But I… I… it is… it has to be like that, otherwise that's what you end up with, right?
**Josh Suereth** 10:44 Right.
**Tigran Najaryan** 10:44 10 times… not 10 times, twice the payload, because of the not sharing of the dictionaries.
**Josh Suereth** 10:49 To me, that's the important point here.
re… like, resending the same resource attribute a couple times, I don't think is as… as big a deal. We can ask them what they're putting on resource. I think you're right, it's only, like, 10 to 12 attributes. They do have some weird shenanigans they're doing with resource, where they're, like, attaching crap.
to remember a resource and understand, like, whether something forked or not. I… I need to go recall the details of that. But the important bit here is when… when we told them before that this, the, the signal, sorry, the,
Dictionary should actually be at the profile level, not at the message level.
**Tigran Najaryan** 11:28 Yeah.
**Josh Suereth** 11:28 That's what led to all the problems they had before.
**Tigran Najaryan** 11:31 Yeah, I don't think that's the right requirement. I disagree with that requirement. Bogan pushes for that.
For the reasons I understand, because it complicates batching in the collector.
**Josh Suereth** 11:43 Yup.
**Tigran Najaryan** 11:44 that batching still can be done, you just have to rewrite the dictionaries and references to dictionaries. It's not impossible. It adds compute, but it's doable, and I think it makes a huge difference in terms of the payload size. If that's what the debate is about.
I am on the side of having a single dictionary per message. I think that's… that's the right approach. But.
**Josh Suereth** 12:07 Nope.
**Tigran Najaryan** 12:07 That's not where it started. The PR was about adding reference-based attributes to resources, right?
**Josh Suereth** 12:14 Yeah, this is where it gets into consistency. So, because they're using a dictionary for all string-based things, then they were like, okay, well, can we use the dictionary for resource as well?
**Tigran Najaryan** 12:24 Why? Why do you need that? If you only have 20 resources, just don't use reference-based attributes for resources, what's the point?
**Josh Suereth** 12:32 I think it's fair for us to go back to them with that. As long as, like, like, and to have.
**Tigran Najaryan** 12:37 Yeah, I'm happy if the dictionaries, the general dictionaries, are at the message level, and you don't need dictionary attributes for resources if you only have 20 resources in your 30MB payload. What are you going to save there? Nothing, really.
So that's what… I kind of… I was confused what's going on there, like, how can it possibly result in so much savings? So, essentially, that's the change they made, the change that Bogdan was asking for.
**Josh Suereth** 13:06 The old comparison.
**Tigran Najaryan** 13:07 parrying The implementation with resource dictionary attributes.
with an implementation that doesn't use dictionary attributes for resources. This is a different comparison.
**Josh Suereth** 13:19 Yes, the comparison is not solely Using a dictionary for resources.
**Tigran Najaryan** 13:23 Okay.
**Josh Suereth** 13:24 everything is.
**Tigran Najaryan** 13:24 Absolutely, yeah.
**Josh Suereth** 13:25 The dictionary up above the resource level, yes.
**Tigran Najaryan** 13:28 Okay.
**Josh Suereth** 13:29 Yep.
**Tigran Najaryan** 13:30 Okay, I think you understood my position here in this.
**Josh Suereth** 13:34 Oh, yeah, yeah, absolutely, which is why I wanted to clarify, like, what I think is important for us to focus on. And the other thing is we need to pick what… what…
principles we want around profiling. One thing I want to call out, too, the fact that batching doesn't work well in profiling, I kind of don't care about, because in practice, you can't.
**Tigran Najaryan** 13:54 They're a huge body.
**Josh Suereth** 13:55 anyway.
**Tigran Najaryan** 13:56 You don't need to do boxing there, really.
**Josh Suereth** 13:58 It's pre-trash.
**Tigran Najaryan** 13:59 I agree. We don't…
Batching, if it's too complicated, I don't care. There isn't… there's no need to do batching there, really. It's doable, you don't want to do it, don't do it.
**Josh Suereth** 14:10 Exactly. Our endpoint that accepts profiles.
We need to actually have a different, like, quota system for it, because they're so freaking huge.
Yeah. So, so we almost want, like, a different implementation for sucking it in. Like, like, there's a whole bunch of things with profiling that I, you know, what I'm trying to get at for us to understand a bit is our intuition
on how we deal with signals and open telemetry is different for profiling. You need to start from the premise that this is… starts as a huge batch of data.
And the things that we're used to with, like, small, small signals, little metrics, little spans, little events that I batched together.
is very different of profiling. We're starting big, and we need to deal with the fact that it's large.
**Tigran Najaryan** 14:54 Yeah. So, I mean, I agree with you, but it has never been my intuition like that, right? So…
what… in my case in particular, I just misunderstood what exactly they were… they were comparing in the benchmarks.
**Josh Suereth** 15:08 Good.
Yeah, that's fair. Okay, so in terms of making progress there, we can ask them to make a benchmark where
resource…
uses the same structure as the rest of OTLP, but they're allowed to share the dictionary at the highest level between all the signals.
**Tigran Najaryan** 15:24 That's what I was expecting, to be honest, yeah.
**Josh Suereth** 15:27 Yep. Okay.
**Reiley** 15:31 I have a question. So…
Josh, when you mentioned start big, does that mean if the connection
is reset, you have to send the big thing over again. And that means if you have a load balancer that's trying to distribute the workload across, like, hundreds of servers.
you wouldn't be able to do that. You have to keep
Like, you have to send the entire thing through the connection to a single server, because otherwise you wouldn't have the contact, the server wouldn't be able to know what's the big thing from the beginning.
**Josh Suereth** 16:08 Yes. Yep. That's… that's a problem with, like, if you try to batch too long. What, what our eBPF profiler does in OTEL, what they're working on, I think they report every 15 seconds, and they actually want to make it even quicker.
And the reason they're reporting so quickly is to avoid that kind of a problem. Like, to basically limit the size of the badge.
**Tigran Najaryan** 16:30 You can also place limits on the size, the actual size, right? Not just limit, I guess, the frequency, right?
Could be that as long as you have X amount of data, you just send it.
**Josh Suereth** 16:42 I don't know if you can efficiently do that in profiling, because you don't know what data you're collecting. Like, like, again, your ability to limit by size is harder with that system.
**Tigran Najaryan** 16:51 I guess, but you can make some estimates, right? Rough estimates of what you have collected in memory. I'm with you. Until you do the actual encoding, it's different to… it's difficult to say how much the payload size is going to be. But maybe some approximation is possible there.
**Reiley** 17:07 is that by self-content? That means, like, when you handle that, you don't have to…
Like, remember what was sent.
**Tigran Najaryan** 17:16 Yeah, it's stateless. It is stateless. The entire payload is self…
decodable. It contains the dictionary that is used in the payload.
**Reiley** 17:26 Let's see, so if you use some, like, symbol, that symbol table would have to be reason.
**Tigran Najaryan** 17:30 Is in the same message, yes.
**Josh Suereth** 17:32 Yeah, they… I think they actually…
**Tigran Najaryan** 17:34 It's not a straightforward protocol, yeah.
**Josh Suereth** 17:36 and resend the same dictionary often. So, yeah, it's not stateful.
Go ahead, John.
**Tigran Najaryan** 17:42 We had that debate a long time ago, so they gave up on the idea of making it stateful.
For the reasons of
having it… making it difficult to support in the collector, because the collector's design was stateless. It was based on the idea that you pass individual messages through the collector, and there's no state inside the collector between the messages.
**Reiley** 18:07 Yeah, but when folks are adding more and more stuff, at some point you might realize, hey, like, a stateless protocol won't really work well there. You have to change it to a.
**Tigran Najaryan** 18:16 I'm with you. I'm working on a stateful protocol, have been working for many months now, and there is huge gains possible there, payload size and compute size, but
the idea that the collector… it has to be terminated at the collector anyway, right? I think it's still… it has its place.
But for a general purpose profiling protocol, I think we made the right call here, so that
So that it works with the… with the concepts that we had previously everywhere in audio.
**Reiley** 18:49 Yeah. Go ahead, Jack.
**Jack Berg** 18:52 I want to go back to something Josh was picking at earlier about, you know, coming up with sort of principles or philosophy about where we want to be consistent and where we're okay with being inconsistent with profiles and, you know, signals in general. And, you know, I'm sort of an outsider to the collector, but I know a few things about it. And, you know, there's this principle where processors process data.
And there's a bunch of processors that are built on top of things like OTGL and count on the data being represented similarly, so you can do similar things across logs, metrics, and traces.
And so, you know, in my head, the question is, like, as a user of the collector, what do I expect to be… to do… to be able to do to profiles similarly to metrics, logs, and traces, and what do I, not be able to… be able to do consistently? And so, like.
like, you're saying that profiles are big. Profiles have dictionaries. You know, profiles might be sort of, like, the message of the profile itself might be a big black box.
from the collector's standpoint, where you can't operate it on it the same with, like, OTTL. You can't modify its attributes and things like that. But, like, maybe, maybe we could take a premise where it's like, profiles are a black box.
when you get down to the profile message itself, but, you know, from a resource and scope perspective, we expect to be able to operate on it similarly to logs, metrics, and traces. And then anything lower level than that, we just throw up our hands and say, like, you know, don't manipulate this.
**Tigran Najaryan** 20:24 You don't have to… I agree with you, you don't have to throw up your hands, because you can have specialized processes which do understand the profiling, payloads, which…
which are not universal, they don't operate on all signals, but they know how to do things with profiles, rewrite samples, I don't know, do extrapolations, aggregate samples, stuff like that is possible.
I don't know if you want to do that in the collector, but it's not like we treat it as a black box. I do agree with what you were saying, though, that the resource… the common concepts, which is the resource and the scope, have to be…
Universally processable by the user, regardless of which signal it is.
**Liudmila Molkova** 21:05 And attributes.
**Tigran Najaryan** 21:07 And… and attributes of whatever is…
the… the data element of that signal, which, in case of profiles, I'm not sure I quite understand what it is. Is it the sample?
the attributes of… like, what is the… what is the entry that… the natural entry that you can think of? Like, in case of tracing, it's the span. In case of logs, it's the log record, right? For the metrics, it's the data point.
Which one of the profiling messages is that natural?
beta element on which you would like to do attribute processing, right? So we have an attribute processor. Attributes of what?
should be modified by the attribute processor when you use the profiling signal with it. It's not… I don't have an obvious answer to that, to be honest. Perhaps sample, I'm guessing? But sample is a big thing, really, if you compare to the other things we use attributes processors on.
**Josh Suereth** 22:07 I don't remember… does sample have… it does have attributes, but it does an index into the table. The profile also has attributes.
And I think everything has attributes here. Does memory have attributes? Yes, it does.
Well, they're.
**Jack Berg** 22:24 attributes, but they're not attributes in the same sense as we think about them with the metric data point, the log record, or the span.
Because they're.
**Tigran Najaryan** 22:33 And that's the thing, yes, yeah, yeah. I don't know in what way you would use those attributes in the same manner as you would use them for log records or spams.
**Josh Suereth** 22:48 or data points.
**Jack Berg** 22:49 Is it important to me?
**Tigran Najaryan** 22:50 And you require that universality of processing, right?
**Josh Suereth** 22:55 To Jack's question, is it important to manipulate them? This is the first thing we asked the profiling sake, two years ago. Yeah. Or, what, two and a half years ago. Oh, yeah.
**Tigran Najaryan** 23:05 What do you want to be processable in the clip?
**Josh Suereth** 23:08 There was no known use case.
**Tigran Najaryan** 23:11 Yeah.
**Josh Suereth** 23:12 from the profiling SIG of how to manipulate these things right now, prior to entering storage, for, like, what's in the profile. So, like, it's not a thing the profiling folks kind of ask for today. So, my opinion here is, yeah, if there's things that we think are useful around resource, great, that makes sense, or scope.
Those attributes themselves, it might be that we need to do things like redaction, where we can look through that string table, look for PII, and redact the string.
That's actually easier on the string table, possibly, because, you know, you have a dictionary to look through, you don't have to, like, look through the whole message.
there might be a set of things we want to do there, right? And the reality of the collector today, though, is even with OTTL, there is a custom context for every signal type, because of the way OTLP is structured.
So there will have to be a custom context for profiling, and we can make that look like a general OTLP data model, even if it's backed by a dictionary, if we want. Like, that's actually technically feasible to do.
**Jack Berg** 24:17 That's just… I think that's going to cause, sort of, maybe not endless, but a lot of frustration and arguments in the collector SIG as they try to grapple with how to manipulate P data and, you know, these in-memory representations of this when the underlying thing is so different with the dictionary versus concrete data. So can we just avoid this problem by socializing the idea?
**Tigran Najaryan** 24:39 I'm not convinced it's even necessary.
**Jack Berg** 24:41 Right.
**Tigran Najaryan** 24:42 Right? I don't know if we need it at all. Because if you're not touching the internals of the profile of the sample, if there's nothing to do with that, no processing is necessary, if the only thing you need to do is work on the resource attributes and scope attributes, I am not convinced that needs dictionary encoding at all.
I'm not. And if it's not dictionary encoded, the existing processors will work just fine with that, right? You don't need to do anything.
**Josh Suereth** 25:08 And honestly, like, resource enrichment is the thing that we probably want here, because we have an ePPF thing that won't have enough resource data, so if we get…
**Tigran Najaryan** 25:17 And if it's regular attributes, that enrichment just works, right? Nothing else is needed.
**Josh Suereth** 25:23 Yeah, and so these are all great questions, yeah. These are all things that we did run with the profile SIG, asked them for answers, and these are the answers we got. So,
Yeah, I think… I think if anyone… if no one complains, let's say, hey.
move your dictionary up to the top, keep resource as is, run some benchmarks, let's see what that looks like in the current ePPF Profiler. That sounds like a good path forward.
**Tigran Najaryan** 25:49 Yeah.
I agree.
**Jack Berg** 25:56 Yeah.
I think this idea that it's so…
**Tigran Najaryan** 25:59 as long as the resource is there, and then… I don't know if scope even is going to be used extensively, but scope as well, just for consistency, maybe?
then we should be good, right? And the processing that we can imagine
Will work just fine in the collector.
Sorry, Jack, I cut you off.
**Jack Berg** 26:21 I was just gonna say that, I think this needs socialization.
Right? So, like…
It's a great simplifying assumption to say that, like, we're going to try to have consistency amongst resource and scope, and then treat everything lower level than that as something that's unique to profiling that the collector doesn't have to try to cope with.
from a P data standpoint, and OTTL standpoint, and processors, etc. And I think they would probably get on board with that. I'm not in the collector community, but, like, you know, if I put myself in their shoes, I'm frustrated with how I represented P data, and I'm frustrated with profiles being so different from that. And all of my frustrations go away if I don't have to try to provide OTTL-style manipulations on top
of these dictionaries. So, like.
you know, I think we could smooth things over if we could articulate a clear vision of, kind of, where we see consistency and no consistency, and then socialize it with the profiling folks and the collector folks.
**Josh Suereth** 27:22 So, one other thing, the profiling folks are the ones owning PData Profiler in the collector. Like, they're the ones building that out, they're the ones driving that. So, it's technically, the people who have to deal with it are the same people that own Profiler.
**Jack Berg** 27:37 They're merging it to the collector repo itself, and there's maintainers in there that are trying to strive for consistency across all P data representations, not just profiles.
**Josh Suereth** 27:46 Fair.
Agreed.
**Tigran Najaryan** 27:54 Okay.
Josh, do you wanna maybe…
When is the profiling sync? Is it tomorrow?
**Josh Suereth** 28:03 No, it would be next Thursday.
Tomorrow's the off week.
**Tigran Najaryan** 28:08 It's bi-weekly? Okay.
**Josh Suereth** 28:10 It is bi-weekly, yes.
**Tigran Najaryan** 28:11 Okay, I don't want to wait that long, maybe, maybe, maybe let's…
Maybe let's have a, like, a very short
Write-up of what we discussed, what we think is the right approach.
And then… then… and have that, that discussion in Slug.
I think this is closer to what they want to do with slight modifications for the resource attributes, which I think they should be okay with, because it shouldn't impact the payload size much.
**Josh Suereth** 28:40 Yeah, yeah, do you want me to write that up and send it to you first, or do you want to just chat with them on Slack? Like, I was just gonna chat with them on Slack.
**Tigran Najaryan** 28:48 No, we can just talk. I'm fine.
**Josh Suereth** 28:51 Cool.
**Tigran Najaryan** 28:51 Oh, let's… Well, the, we have that private channel where we were discussing the thing, we can…
either use that, but then I would want to invite ProfilingSeek to that, or we just use the public profiling channel for the discussions from now on, because I don't want to restrict it to just people who are in that private channel.
**Josh Suereth** 29:13 Yeah, yeah, I think that's fair.
**Tigran Najaryan** 29:15 So let's go with the public, okay?
**Josh Suereth** 29:17 Right, and I will update the private channel to say, hey, we're moving this conversation public, and we have some responses. Okay, let's do that.
Cool.
**Reiley** 29:30 I have a potential topic.
Aye.
I want to check on the PR that mentioned yesterday along multiple resources in the SDK.
I remember there were some debates, so let me put the link in the… Nothing knows.
So my… my main question is, is there…
There are, like, instrumentation libraries that are Assuming there's a global provider.
Like, they will… they will go and fetch the global provider, and then add their instrument. So with this change.
How… how do you imagine that to work?
Like, the example shown here
it's like the piece of code that you have control of both the creation of the provider and the creation of the instrument. But the problem is normally the application is the owner of the provider creation, and the instrumentation library
They don't create any provider, they just go and assume there's a provider. They go and guide a provider.
And then they create the instrument here, so…
**Jack Berg** 30:55 I would… I would…
**Reiley** 30:55 Cool.
**Jack Berg** 30:57 I would just jump in and say one thing, just one distinction from what you're saying, Riley. So typically, the instrumentation is provided
you know, upon initialization, a provider. So, a meter provider, tracer provider, logger provider. And I think what this is saying is that the instrumentation would have to be responsible for resolving the entity, and then calling that existing provider, and instantiating a new instance from that.
So it's like you have a tracer provider that's provided on initialization, you get a session entity, and then you say, tracer provider, give me a new tracer provider in the context of this entity.
And so… and then you, like, you know, proceed to initialize accordingly. And so it's kind of awkward, because you're doing your initialization steps of, like, getting meters, loggers, and tracers lots of times, rather than just, like, one time at start.
And so, like, arguably those processes… those operations need to be a lot more performant than maybe they have to be now when they're considered low throughput, but
That's at least how I read this.
**Josh Suereth** 32:01 So, yeah, but in practice, Jack, you're not doing the full initialization that you would do in other cases, because you're reusing the pipelines.
So, technically, all you're really doing is replacing,
You're replacing what resource will get pooled, when you feed data into the pipeline.
So, creating the sub thing is not, not as expensive as you might think. The most expensive part is constructing the resource.
Since all the other stuff is reused and has been instantiated.
**Reiley** 32:35 So, for example, if… if…
I'm an instrumentation library. I got a provider, and then I use a provider and identity, which gives me another provider.
And… And at some point, I just decided I'm going to call the provider destroy or something.
Does that mean I have… I tear down all the underlying… so now the problem is the provider has all the processors, exporters. Oh, let's share
all the…
**Josh Suereth** 33:03 This is in the OTAB, so please read the OTAB. But, yeah, effectively, when you close down, you don't…
If you close down the outer provider, all providers underneath it… like, if you close down the master provider, everything's shut down. All providers are shut down. They're all considered closed. If you close down a sub-provider, all that happens is you flush
Any information that that provider had to store, and you allow it to get garbage collected, but you do not kill the pipeline, because the pipeline is shared.
That is what the prototypes do, and that is how that thing was designed and implemented.
**Reiley** 33:37 Okay, so that sounds to me like we're creating another, like, a sub-provider, as you mentioned, and this is different from a provider. We're introducing a new type.
**Josh Suereth** 33:48 If we could have introduced a new type, we would have.
We wanted it because of the way instrumentation gets instantiated, where you pass a provider to it, we… we… this was… this, David, I don't know if you want to speak to that, that was actually one of your…
**David Ashpole (dashpole)** 34:03 Comments on it?
**Josh Suereth** 34:04 But because a lot of instrumentation takes a provider, we need to have it be the same type, otherwise this doesn't work in practice. But yeah, conceptually, it's like a sub-thing.
**David Ashpole (dashpole)** 34:16 I think one of the things that…
I thought would be useful is if you could bind
a provider before passing it to instrumentation. So if there's an instrumentation library that, say, isn't multi-tenant in the way that it's written, and doesn't support this, like, late binding of
additional resource attributes. You could still use it, you would just…
like, let's say you're creating a client to go talk to something. You could bind it to…
a certain set of resource attributes, and then pass the meter provider into the existing instrumentation library. So you…
The current design allows you to do it either within the instrumentation library, if it's aware of, like, say, multiple tenants, or you can, like, impose it from the outside.
**Jack Berg** 35:07 So…
A quick comment on this close method that you would have to add to the providers. So, if you take a provider, tracer provider, and you create a new tracer provider in the context of an entity, you can close that new tracer provider.
maybe this is in the OTEP already, but you shouldn't be able to close the root tracer provider. We can't give that power to instrumentations.
**Josh Suereth** 35:31 So, this is in the OTEP, yeah, and this is in the prototype. So basically, shutdown… Daniel Dyla actually wrote this spec, and I really like how he phrased it, but basically, we don't make a close method, we just reuse shutdown. If you call shutdown on the newly created thing.
It… it force-flushes your data, or makes sure that it's exported, and marks all of that, you know, infrastructure you set up for cleanup if you need it to.
But it does not close the main provider at all. And it doesn't close down the pipe… the export pipeline. All it does is mark what you've created as a sub-thing ready to get cleaned up and flushed and gone.
**Jack Berg** 36:12 When you say you reuse shutdown, you're… what you mean is shutdown in the SDK is getting promoted to the API.
**Josh Suereth** 36:19 Shut down all the.
**Jack Berg** 36:20 they exist in the SDK.
**Josh Suereth** 36:22 Yeah, so you can only shut down one of these if you interact with the SDK.
Right now. We have not promoted a API-level close method. That is probably something we would have to do or account for in the OTEM, so you should comment about that, yeah.
**Jack Berg** 36:36 Yeah, you definitely have to do that if instrumentation is gonna call it.
**Josh Suereth** 36:40 Yeah, I mean, in the prototype, you had to interact with this thing on the SDK level for 90% of everything anyway, because you're dealing with resources, and it's…
it's awkward, but yeah, I agree. We,
There's a few things this does not solve, by the way, that are still systemic problems in OTEL. One is, you have no resource level
access to resource. Or, sorry, no API-level access to resource at all.
And so, any instrumentation that's interactive resource still cannot.
what this proposes is that we would expose an entity API where you can at least define an entity in instrumentation and interact with resource implicitly, but you can't interact with resource in the API. And that is something I still think we need to address, but it's not in this OTEP.
**Jack Berg** 37:30 You know, as you mentioned this, like, that thing… that question comes up over and over again in Java, and my answer is… my answer when people request it is, like, what are you trying to do with the resource at the API level? Like, why do you actually need this? And I always get crickets. I never get good answers.
**Josh Suereth** 37:45 Oh, there's one… there's one specific answer that I know people want to do, and java, you actually
do this in a way that I think could be better. When, when you,
if you want to attach your service name and baggage, so when you communicate to something else, they know what service they're communicating, like, what service it came from. That's, that's, like…
Yeah, context propagation. I want to take some of my resource information, throw it into baggage to con… to do context propagation of who I am.
We can't do that today without talking to an SDK.
So…
**Jack Berg** 38:21 Actually, yeah, there's probably some clever solutions in there with entity. It's like, you know, so entity is trying to solve this problem of which resource attributes are identifying versus descriptive, and so, like, you know, maybe we sort of…
we can look towards exposing entity in the API instead of resource, because if you want to solve that context propagation problem, you want to communicate your identity. You don't want to communicate your entire resource. So it's like, the entity solutions lend themselves better to this context propagation problem.
**Josh Suereth** 38:50 Yeah, yeah, I do think that, entity will be in the API, for sure, and that's the path we need to take. The question is, how do we get there? For this particular OTEP, by the way, I am not…
I just want us to agree on whether or not this is a viable solution for the multi-resource problem with SDKs. I'm not planning to push this quickly, at all. If browser needs it, then we need to push it faster, but I'm gonna let them
run with the timeline. This is just how we think the needs of browser and the needs of entity meet together.
**Jack Berg** 39:25 Yeah.
**Josh Suereth** 39:26 we're still more focused on, let's get a non-breaking mechanism of entities in the SDK, so that resource detection, resource construction, resource reporting uses entities, and then we can continue to explore, like, how to expose in the API effectively.
**Jack Berg** 39:44 You know, this question about
should resource or entity be exposed in the API? I was thinking about what Ivo was presenting the last couple of weeks with, this OTEP to, allow resource to be communicated out of process to eBPF, and it's like, if we're gonna let resource escape the process so that eBPF can observe it, like, why do we care if instrumentation can access it? Like, come on!
**Liudmila Molkova** 40:12 Oh, because the instrumentations would abuse it, because people really want to abuse it, and all of the scenarios people come with, they would not be possible, and we don't want them to.
**Jack Berg** 40:22 Will one of the instrumentation be able to access the resource information from shared memory the same way EBPF can?
**Josh Suereth** 40:28 Yeah, yeah, absolutely.
**Liudmila Molkova** 40:30 None. No.
Very few people would go without this route.
**Jack Berg** 40:34 Okay, so we're adding friction.
**Reiley** 40:36 Great. Yeah.
**Josh Suereth** 40:37 You know there's gonna be a library that does it, just wait. Yeah.
**Reiley** 40:42 But…
**Josh Suereth** 40:42 Yeah, I think, I think the,
The only thing I want to say is that we had this notion before of being able to mutate resource and SDKs, and we were working on prototypes for that for a while, and they were disastrous. Like, that is,
if we were going to do anything like that, we would have to V2 the SDK spec, in my opinion. It just… it was some of the worst… like, Jack, I send you a lot of bad code and you clean it up. This was not something I could send you.
That's how bad it was. So, like, the notion that we would mutate resource and handle that and figure out what it looks like, for spans and logs, not as bad. For metrics, it was godawful.
What we have now in this prototype for metrics is… the code that you're looking at is not the code that I would submit to Java. There's a lot of cleanups I can do to it, this is just getting it working, but it's reasonable, right? And I think it's practical, I think we can do it efficient, and I think we can keep it clean.
mutating the way we were doing before, I don't think we have a viable solution for that in our current SDK that is practical.
So… Yeah.
Anyway, any other questions, Raleigh?
**Reiley** 42:09 Yeah, so, two things. One is, if we really want to introduce this concept of, like, a provider version 2 or something, or sub-provider.
I think there might be other opportunities, like.
Maybe we can allow people to add an additional processor.
So, like, if we introduce that type, I want to make sure we don't just introduce that as a workaround for entity.
We really demand this time.
**Josh Suereth** 42:41 We explicitly do not want that. Like, that is… that is… that is actually… we had a whole discussion about why we don't want to do that. The primary reason is, if you think about the declarative configuration.
and possibly, like, op-amp-related controls. We don't want the notion that there are sub-providers to… and that they're dynamic.
to be exposed to, like, the configuration and op-amp-related controls. We want that to… like, there is a core SDK processing pipeline that you can manage and control, and if you want to do any sort of processing on one of these sub-providers, what we would do instead is expose resource
In some fashion on, like, sampler, on processor, on that sort of thing.
**Reiley** 43:26 not upside.
**Josh Suereth** 43:26 Yeah, you can understand.
**Reiley** 43:27 Oh, boy.
**Josh Suereth** 43:28 What?
**Reiley** 43:28 That is very slow. If you already have, like, different entities attached, you won't have a filter plug-in listening on the noisy path. Instead, like, for efficiency, you should just do it on the source.
Right. If you have an entity attached to a specific sub-provider, you know all the data coming from there, you want to drop that data, you should just drop it there instead of listening on a noisy stream.
**Josh Suereth** 43:55 So… Okay.
**Reiley** 44:00 We, we…
**Josh Suereth** 44:01 Why don't you comment on the OTEP, and we can talk through that. I… I disagree, because I think we…
We already have kind of a noisy Yeah.
if you start adding those, like, sub-things, it gets really awkward. Now, what does sharing the pipeline mean? If you look at what, like, a span processor is, it is a wholesale, complete thing.
It is not like a pipeline, in practice. So actually sharing a span processor makes the most amount of sense. Allowing a separate span processor means I could define my own pipeline completely. There's no such thing as, like, a span delegate. You would have to invent a new.
**Reiley** 44:40 I hear you. Then we shouldn't call it a provider, we should call it something else, because the spec allows you to add processors, even the, like, the provider is created.
**Josh Suereth** 44:51 It doesn't, it's a… that's a May, it's not a…
**Reiley** 44:54 They may, but their languages implemented that.
what do they do? If they call that something that is a sub-provider, it's a provider, then people try to add a process of what's a semantic there. It's a breaking change, right?
**Josh Suereth** 45:08 Well, no, no, because we could say the subprocessor doesn't support that. It, like, again, it's a new thing. There is no breaking change for the new sub-provider.
**Reiley** 45:16 Okay, I understand. Then don't call that a provider, call that something else.
**Josh Suereth** 45:21 If we don't
call it a provider, then we can't reuse instrumentation as it exists today. So, like, I agree with you, things are not ideal, but the question is.
What can we do in a backwards compatible way?
**Jack Berg** 45:34 So it needs… it needs… we need a polymorphism aspect to this. We need whatever subprovider is, as, like, a concept that is not allowed to add spam processors to it to implement the exact same interface as the existing tracer provider does, because we want instrumentations to exist as is.
**Liudmila Molkova** 45:52 It's already the case. There is an API tracer provider that you get from the OpenTelemetry instance, the global, or you get it through the API.
Yeah. And there is an SDK version of it. An API version obviously doesn't have ability to add processors.
**Josh Suereth** 46:08 Yeah, in practice, so we can make the specification look and feel polymorphic, that's fine. We have to be careful with how we do that. In practice, it can't actually be polymorphic because of how our implementations were defined. There was no expectation that there would be any polymorphism at the SDK level, and so a lot of those things are final, and we had to actually modify them directly.
in the prototypes, and I don't see a way around that without breaking or an SDK V2.
**Reiley** 46:39 Yeah, or maybe I explicitly call that, like, all the subproviders, if you call that processor, they'll just, like, give you error, or throw exceptions.
**Liudmila Molkova** 46:46 There should never be…
**Josh Suereth** 46:49 Anyway.
Go ahead.
**Liudmila Molkova** 46:51 that there should never be a way to add a processor. I don't really understand where the possibility even comes out of.
**Reiley** 46:58 It was in the original spec.
**Jack Berg** 47:02 So, if you have an S… so, you know how there's, like, a distinction between SDK tracer provider and API tracer Provider?
let's say, for whatever reason, you're interacting with the SDK tracer provider, and the SDK tracer provider implements the same interface as the API one, and you say, hey, get me a new sub-provider for this entity. You now have a new, like, SDK tracer provider.
With the same methods exposed to be able to add a processor to it.
But, like, that doesn't make sense to do at the sub-tracer provider level. That's the problem we're dealing with. So we need to find a way, like, if for some reason you're interacting with the SDK version of the tracer provider.
If you ask for a subprovider, you can't… you can't mutate it anymore.
I don't think that's a… it's not a real problem in Java, but, like, I can see it being a problem in certain languages. I don't know which languages it would be, but if you designed it in a particular way, maybe this is a problem for you.
But I guess, like, we can just make clear that, like, you know, the part of the specification that says that
SDKs should be mutable, that you can update, or you may… may be mutable. You may be able to, like, update their configuration. We can just make it clear that, like, that is not applicable to sub-providers.
Right? If and when you implement this, make sure you implement it in a way where only the top-level provider is mutable.
**Josh Suereth** 48:35 Yes,
Agreed. I feel like this will be some dance in the spec, where we can probably do what everyone's suggesting here, where we write the spec in a way that there's a thing called a subprovider in the spec.
But we need to call out subprovider doesn't have to be a physical type in your system. And subprovider has these behaviors and limitations. And then, because we have to reuse the same implementation, we just make it so when you're the sub-provider instance, here's the things that are true. When you're a regular instance, here's the things that are true.
And we can make it so the spec is easier to read, even if the implementation has to be a little weird.
Does that sound reasonable?
**Jack Berg** 49:16 Yeah, exactly. Like, here we started using the term subprovider to distinguish between, you know, the global provider, the top-level provider. It would have been really hard to have this conversation without a word that you use to refer to a child provider.
**Josh Suereth** 49:34 Yeah, so I think the spec can do that, and have those limitations, Riley, and then when you implement it, we'll have to see what is backwards compatible.
**Reiley** 49:42 Yeah, and the second thing is, from my memory, like, in OpenTelemetry.net, I think folks assume that entity…
is, initialized
as part of the provider initialization, and it'll never change. So the processor kind of took advantage of this.
And they won't… they won't check if the entity is changing or not, because that's just attached at a upper level.
And now, we're essentially telling the processors, you cannot make that assumption anymore, since it could be dynamic. You might be receiving something else.
And I'm not sure, like, how much of the braking change.
from the processor, or the exporter developer perspective. You can imagine, like, a lot of people, they try to tune the performance for the exporter. They will say, if I need to export this
this entity, I know it's not going to change. Let me just do all the serialization ahead of time, then I can reuse the byte array and send that over again. And now the situation changed, so…
**Josh Suereth** 50:45 So, that's actually done in Java, and we were… we'll have to see what the implementation in .NET is, but in Java, the entities are pre-serialized and cached.
Sorry, resources are pre-serialized and cached. Or, they're serialized… they're serialized in a cache.
and you reuse the cache every time you write, and that actually worked with multiple resources. But that's because of how it's implemented, right? So the way Java actually attaches things, the processor actually has access to a resource per span.
where they have a get resource method, and it's this one object that contains everything. And if we have different resources, the way the code was written, everything actually aggregates appropriately, and the resource does get cached between exports.
**Reiley** 51:30 Yeah, I understand.
**Josh Suereth** 51:31 that it's, like, 10 or so, so, like, you can only catch 10 things. But it worked out pretty well, because we're not expecting, like, a ton of, we're not expecting a ton of resources here.
**Reiley** 51:42 Yeah, I understand. And that's because you added some additional code, so you're, you're using, like, maybe a couple, like, security protocols.
**Josh Suereth** 51:52 Added no new code, no new code to the export pipeline. I understand.
**Reiley** 51:58 what I'm saying is.
you're… you're saying, in the Java SDK, people are doing this indirect thing, like… like a virtual, like, function or something, and… and this allows you to… to have this dynamic support. But for people that want, like, even better optimization.
They don't have this additional, like, low-carbon resource. They just assume that thing will always be the same.
**Josh Suereth** 52:24 They have to, like, if you expose a custom exporter, that custom exporter needs access to the resource, so at some point, I need to be able to go from a batch of span data to the resource that's attached to it in some way.
So, like, I think in the spec, even, we call out that, like, the…
readable span thing has to have get resource on it. So you need to have that level of attachment in some way. You can cache it successfully and do all the things you're suggesting, which Java does, but it still has, per piece of information, a resource attached.
**Jack Berg** 52:59 So what Radley's saying is, like, maybe the exporter takes a big shortcut on this, and it says the first time you ever call export, you take the first resource of the first span and cache that.
And you don't even do a lookup. You're not saying, like, hey, give me the serialization of this resource. You're just saying, like, I'm going to assume that the first resource I ever saw, I'm going to use that serialized representation.
for here on out. So, you know, I would argue they're, like, that's a big shortcut they're taking, and they should update their code, but, like, you know.
**Josh Suereth** 53:30 Yo.
**Jack Berg** 53:31 Exist somewhere.
**Josh Suereth** 53:33 Yeah, that I can believe. We did talk about this as well. Okay, I see what you're saying. That is something we think we can fix and still keep efficient, right? Like, there's still a set of things that you have to have true about resource generally that,
I think that's a fixable problem.
**Jack Berg** 53:48 I mean, no, it's gonna break code that depended on that. There's no way it doesn't break code.
**Josh Suereth** 53:52 Yep.
**Reiley** 53:53 Not, not break…
**Jack Berg** 53:54 It's just gonna break the export.
**Reiley** 53:56 For code that we control, for sure, like, go and add additional 3 CPU cycles to do the lookup, fine. But for the code that you don't have control, people already have the assumption, they optimize that to the hell, and now you're asking them, I'm going to break you, and you've got to add this indirect lookup.
that's also fine if we're not asking a lot of folks. My question is, do we… do we have a…
At least I know from .NET their two weeks powder set will break.
**Jack Berg** 54:25 Riley, as you're saying this, I'm thinking about the shift that we made to support complex attributes.
Like, that's a much bigger ask of exporters, to adapt to a world where the attributes are not just, you know, primitives and arrays of primitives. So, if we can say that exporters have to adapt to that new reality, then I think we can say that, similarly, they can adapt to a new reality where resource isn't completely static.
They're similar asks. Both break the exporters. They don't break them, they just, like, they're not going to… they're no longer going to export, like, you know, what the SDK is telling them to export.
**Liudmila Molkova** 55:03 C, cuz.
**Reiley** 55:03 Right.
**Liudmila Molkova** 55:04 tied to entities, because entity does not exist. Anything you do with entities cannot have breaking changes. So, if we are moving to entities on the SDK side as well, if there will be an entity SDK.
Then, could this all be,
exposed surro entities and exporters that deal with resources.
Would not be broken.
**Josh Suereth** 55:34 I'm… I'm not sure how.
I'm trying to understand the suggestion.
Like, the, the, the problem is, like.
if we change the resources on the span, and we're trying to reuse that export pipeline, are you suggesting that we would have, like, an entity-specific OTLP exporter, an entity-specific, you know, XYZ exporter?
like…
**Liudmila Molkova** 55:56 It's more of a, trying to understand if, let's say, like, how the transition to entities would happen on the SDK side, and if… it should not be completely transparent. I mean, it's, like, you can assume there are no entities, but at some point, you should be… you should start
We're using that.
**Josh Suereth** 56:18 Yeah, well, yeah, so an SDK can actually engage with entities in its own resource data model and resource detection.
independently of exporters. If exporters drop entities.
Entities are still valuable, because they will help with the merge algorithm between detection, and they'll help with, we can actually tie, like, an entity namespace, or, like, an entity set to, the configuration names that we have now in the spec.
We can tie that to Weaver, semantic conventions, like, there's a lot of value we can get, even if we drop all that information on export. That's fine. And that's why we went with the OTLP data model we did.
Because we don't want that to be a breaking change. Eventually, the OTLP exporter needs to also expand to send these entities, but you can actually make those changes independently.
**Liudmila Molkova** 57:10 And when you update entities, you would have to update resource as well. You cannot keep them, like, two versions, two views on… it's two views on the same data, not two different sets of data.
**Jack Berg** 57:22 Yeah, because the entities reach into the resource attributes.
**Liudmila Molkova** 57:26 Yep.
**Josh Suereth** 57:27 Exactly. That's why we did that encoding, is so resource remains exactly as is, and entities are a view on top of it.
This doesn't fix the problem of multiple resources in an exporter when we add that, right? Because at that point, we just look at resource and make sure that the entity information also gets into OTLP.
And that one, we only have to change OTLP. If, if you have a custom exporter for your own language, you want to look at entities, great, you do. If you want to use resources as it exists, we don't care.
That's fine, there's no breakage there. So, it's, this multi-resource thing that Riley's bringing up, that one we have to address in some fashion or call out.
And that's independent of entities in SDK.
**Jack Berg** 58:19 Any parting thoughts?
**Josh Suereth** 58:23 Some good discussion in this today, man. Fiery. It's good.
**Jack Berg** 58:29 Yeah, I'm glad these aren't public.
**Josh Suereth** 58:33 Oh, but they are.
**Jack Berg** 58:34 No, I'm glad they're public, because, you know, at least there's some sort of paper trail, and, you know, these discussions, which we're always bad about taking notes on, aren't just, like, lost to the abyss.
**Josh Suereth** 58:45 Yeah.
Now we just need to get,
AI to take our notes for us and make it clean, the public notes, and then we can be super lazy and just have fiery discussions all the time.
**Jack Berg** 58:58 That would be… That would be great, if we didn't have to worry about trying to take notes.
**Josh Suereth** 59:06 Alright.
**Jack Berg** 59:07 Alright, see you all.
**Josh Suereth** 59:08 Thanks, see you, everybody.
**Armin (Dynatrace)** 59:11 Bye-bye.
