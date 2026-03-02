SIG: Entities SIG
Date: 2025-10-20
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:01:08 Hey.
Dmitrii Anoshin 00:01:11 Toter on.
Josh Suereth 00:01:16 How are we all doing?
Dmitrii Anoshin 00:01:18 Doing well.
How are you, Josh?
Josh Suereth 00:01:21 Pretty good, pretty good. Better than last week. Last week, I was…
I got some sort of head cold that had me out all week, basically.
Dmitrii Anoshin 00:01:29 Wow.
Josh Suereth 00:01:30 Yeah.
Seems to be the way of it these days, right?
Out for a little bit, out for all.
Right.
I need to finish typing up one thing from the last meeting, and then I'm ready to get started. In the meantime, if you want to take it away, Dimitri, feel free.
Dmitrii Anoshin 00:01:53 Boom.
So, yeah, my… I've been working on the collective support, and in collector, it's… we, like, have to…
Different companies and processes as well would need to… instead of changing the resource attributes, they would need to change entities.
And I found it very complicated if we don't establish any, like, data integrity, restrictions.
Because if we allow several entities to share the same resource attribute.
Even if it's not identifying, if it's descriptive, it's gonna be super complicated. You would need to put, like.
I don't know, we need to maintain reference counter on each of the resource attribute, then, like, decrease, increase it based on… and also we need to, like, disallow, change, and so it's, like, it's insane. And I don't think it actually makes a lot of sense. So, given that we have another rule, that if you have
two entities, using the same attribute, which can potentially conflict, that's what's already written in the spec. You should use…
only one entity should reference that, so I'm, like, I'm making it a bit more stronger.
And, that's what I'm suggesting. And for the entity type uniqueness, I believe you already have it, it's just not explicitly written.
Josh Suereth 00:03:21 Oh, we didn't write this down yet.
Dmitrii Anoshin 00:03:22 Right, yes.
Josh Suereth 00:03:25 Yeah.
This, this second one, I…
I'm on board with it, like…
Things are getting awkward with this.
in some fashion, like the availability zone discussion we had before.
Dmitrii Anoshin 00:03:40 Yeah. Where…
Josh Suereth 00:03:41 Yeah, so I do think that we'll lead to some semantic convention changes.
But, yeah, yeah.
This all makes sense to me.
Dmitrii Anoshin 00:03:51 Okay, cool.
Josh Suereth 00:03:53 Anyone, anyone else have thoughts here? This is in the data model, yeah.
Daniel Dyla (Dynatrace) 00:04:00 I guess we need to define what happens if two…
Entity detectors attempt to detect the same attribute.
Dmitrii Anoshin 00:04:09 And that's what we already have in place. If you have placement of shared descriptive attribute, the next section.
That section talks about it.
Josh Suereth 00:04:18 Yeah.
If multiple entities share the same script address key, the attribute must logically belong to only one of them.
Others should not reference it. The attribute must be referenced by the most specific entity.
Those topology graph? Okay, interesting.
Daniel Dyla (Dynatrace) 00:04:34 But I don't know how that's possible… With the current… API…
That we have, like, there's… each detector.
doesn't know… like, the SDK doesn't know which detectors are more specific.
Josh Suereth 00:04:51 That's… we… yeah, what we talked about previously was this is where config comes in, where there's an order that a user specifies, and we just tell them to put most specific either at the top or at the bottom, doesn't matter. I don't care which one's most specific, top or bottom.
But there's one that we would… there's an order, you can configure that order, that order is your specificity.
Daniel Dyla (Dynatrace) 00:05:11 Yeah, so to me, that's two different concerns then. So this would say, like, the last one wins, or the first one wins, however we define that, and then in the config spec, we would recommend that you do your most specific last, or something like that, or first, or whatever you want to do.
Josh Suereth 00:05:30 So in… this is the data model spec, so here we would say that it should be, like, it should be the most specific.
That… that gets it. And then in the actual spec, we would say it's… this is the conflict resolution algorithm and the order.
And that's where we say you order it in terms of most specific, or whatever. So I kind of agree with you, but kind of disagree, because of the purpose of the data model spec.
Like, the data model's how to interpret the data that's coming in.
Daniel Dyla (Dynatrace) 00:06:03 Okay.
Josh Suereth 00:06:04 I think that this… like, to agree with you, though, I don't think this can be a must.
Dmitrii Anoshin 00:06:11 It's actually already been a must, if you look at it.
Josh Suereth 00:06:14 No.
Dmitrii Anoshin 00:06:14 And we're providing that, yeah.
Daniel Dyla (Dynatrace) 00:06:16 It's true.
Dmitrii Anoshin 00:06:17 is that I removed the wording saying, descriptive attribute with potentially conflicting values. I removed with potentially conflicting values, saying that we do not allow two entities to reference the same attribute at all.
Yeah, whether it's potentially or not potentially conflicting.
Josh Suereth 00:06:40 Okay.
Dmitrii Anoshin 00:06:41 That's the only change in this paragraph.
Josh Suereth 00:06:46 Okay.
Yeah, I think the… this… this bit we'll have to talk through more, but, yeah. I… in terms of this limitation, I… I think we kind of have to go forward with this practically.
I don't know… I don't know if anyone else sees an option here to…
with how we've defined things in OTLP, I don't think we have a choice.
Daniel Dyla (Dynatrace) 00:07:10 I mean, I think for the unique type thing, our merge rules already imply that anyways on the SDK, so this is just making it explicit for the processing pipeline.
Josh Suereth 00:07:22 Yeah, yeah, no, the attribute ownership one is the one I'm specifically…
this is one I think we… oh man, we walked into, basically, and this… just in terms of making sure our implementation's reasonable, I think we have to put that…
restriction in place.
Ted Young 00:07:42 Are there reasons why users would have to define this, or can we…
make a canonical listing. I mean, obviously, stuff can show up that isn't in semantic conventions, right?
Josh Suereth 00:07:54 Yes.
Ted Young 00:07:57 Yeah, for everything else, do we have hope that there can just be one canonical ordering?
Josh Suereth 00:08:03 That's my… my hope is if we get Kate's major cloud providers, VMware, like, we're gonna do 80% of the work for you.
90%, 99%, you know? It's… it's… we do processes, we do hosts, right? Like, we should be able to cover 99% of these, and then the open extension is needed, because you don't know what people are gonna have.
Yeah, mate.
Ted Young 00:08:27 Okay.
Josh Suereth 00:08:28 So…
Okay, yeah, this looks good to me. I'll make comments on that.
Later, but that was our discussion.
Thank you for taking notes here.
Alright, Florian.
Florian Lehner 00:08:46 Yeah, hi everyone. I'm from the profiling sick.
And, we wanted to get some feedback on process context labels.
It was… so there are multiple options how labels can be set to a process, and, there are multiple options how to express or could be expressed them in semantic conventions, and…
We wanted to ask if you have an opinion or a suggestion to Go forward.
Josh Suereth 00:09:23 Why aren't these just… raw labels in the resource, as, like, that the process exists on. Why are they…
underneath the process.
Florian Lehner 00:09:33 Because they could change…
Labels can be attached to a friend level, and so not be globe… process global labels.
And if you have a profiling view on a process, you can see every…
A thread of the process, and, so these can change.
Josh Suereth 00:09:55 They change for the lifetime of the process itself?
Florian Lehner 00:09:58 Not necessarily, they can change during the lifetime of the process, but most of the time it's just like, hey, if you think of threads, thread A does have label ABC, with keys, D, E, F.
And, thread, 2 does not have any, labels attached at all. It helps, to identify.
congestions, be it in terms of logs, congestions, memory log congestions, but also, if you, if you take the data and say, hey,
my process, or this particular thread, is moved by the operating system from one core to another, and now I have higher latencies, because maybe the CPU bus is connected to a different memory lane.
And it's causing you higher latency, so this is the use case that would enable this.
Josh Suereth 00:11:00 Right, I guess… Yeah, but you're doing generic key-value pairs for that?
Florian Lehner 00:11:06 Yes, yes, yeah.
So, similar, to, environment variables, but environment variables are, on the, process, globally to the, process, so you don't differentiate,
And environment variables on the, on the fret level. But this, labels can be,
Can be specific to a, to a friend.
And so we don't, at,
on the… thinking about the OTLP protocol, from the profiling part, we don't, attach these, or would not attach these, process context labels on the resource level.
But on the sub-message, sample labels, where we can say, hey, this is a specific, thread that was on the CPU at time XYZ.
Josh Suereth 00:12:06 Okay.
Who owns making these labels? Like, who defines them, who writes them, where are they stored?
Florian Lehner 00:12:14 Usually they are, created by a process.
Pprof, PProf is an extension for most, processes that can handle such, labels.
They are stored depending on… Language. So…
If you look at native languages, so C, C++, Go, and Rust, they are usually stored in the thread local storage.
Of the process. For interpreted languages, this can be different. So, we are currently working on getting support for labors.
for JavaScript and Python. Theirs is a little bit different, but the, the idea is generally the same, that, labels are on, on, on the thread, on the, on, on, on the context, not on the global process.
Josh Suereth 00:13:14 Yeah, okay, and… but the way I would fill one out, right? Like, how do I actually provide one of these labels? Is PProf doing that on my behalf? Or am I setting that as, like, a process myself?
Florian Lehner 00:13:29 As a process, by yourself is doing this, usually?
Pre-prof is just a helper that, can, can this… can do this, or perform this task.
Josh Suereth 00:13:38 Right, so I would have code somewhere that says, add this label.
Florian Lehner 00:13:41 Yes.
Josh Suereth 00:13:42 In this thread, in this context. How is this different than OpenTelemetry context?
Florian Lehner 00:13:49 What do you mean by open telemetry in context?
Josh Suereth 00:13:53 So, there's an OpenTelemetry Context API that's supposed to be kind of a thread local of sorts.
that will trace through a transaction or a request or whatever, right? And you can put key-value pairs on it. It's where we store span IDs. That's how we thread span IDs through. You can also put baggage on it, which is like generic key-value pairs.
And there's supposed to be ways for this to interact with other things.
But ways to, like, get data out of that context and into, like, metrics, or into logs, or into traces. It's a thing that I think is somewhat…
We use it in our specification for trace ID, but we're kind of weak when it comes to generic key-value pairs. But I'm kind of curious…
it sounds like you might be doing similar things with thread locals for that, where you have a thread local place where you can store labels, users will throw labels into this thread local, and then you want those thread local labels to show up in data that is generated. To me, that sounds like a…
Contextual-based interaction between a signal and the SDK, right? That…
OpenTelemetry had other things that wanted to do stuff similarly, but
I don't think you need a namespace and semantic conventions for this. These are, like, user-defined attributes.
These are just, like, the user says I want to attach attribute X to something, and so I…
Take that label and put it where I need it to be.
And it doesn't need a namespace and SEMCOM for that to exist. Like, what I fear is happening here is that
you might be using SemConv where I think your data model needs to account for this. Or in OpenTelemetry, we might use a data model for it.
And I'm trying to tease that out and understand better, because I… I honestly am not sure.
Right? But, you… I would recommend, to take a look at context, how it's used in OpenTelemetry to thread trace IDs through, how generally, like in Java, it's a thread local.
And when I pass a request from thread A to thread B, I will actually pass my context along.
Florian Lehner 00:16:02 This, this is different, because,
for example, a span and trace IDs.
get along a processing path, I would say. But the process context, as in the labels that we are speaking in on this topic, they are stuck with the, with the process.
So they are not passed along. So if… just if the thread of the process moves from CPU ID 1 to 2, the labels will move on with it, but not with, but not if something like a span ID passes, passes through it.
Josh Suereth 00:16:44 That's true. That makes sense. Okay.
Ted Young 00:16:46 Yeah.
Josh Suereth 00:16:47 So it literally is your annotating process with just additional random labels.
Florian Lehner 00:16:51 Yep.
Josh Suereth 00:16:52 Okay.
Ted Young 00:16:54 Yeah. If it's at the process level, it's definitely a resource. Though, one thing I'll note, you know, we have context propagation, but we don't…
we don't have anywhere in our data model to put baggage and other things, so this is a thing that's coming up. I know we've proposed
Various ideas for, like, how to do that?
Josh Suereth 00:17:14 Beautiful.
Ted Young 00:17:15 If someone did want to use context for this, they'd still have the question of where in the data model visits.
Josh Suereth 00:17:20 I know. I've wanted to sell that for so long, Ted. Wait till you see the future work in the OTEP that I have.
Ted Young 00:17:26 Because I literally called it out. Yeah.
Josh Suereth 00:17:31 Yeah, no, no, this makes sense. There's a piece of me, Florian, that is like, I don't know if you need semantic inventions, you should just be able to provide these attributes.
But if you need to know, like, what they were attached to, it makes sense to put it under process as a descriptive thing.
It's just… it's interesting. These are descriptive attributes for process that we want to record and remember.
Florian Lehner 00:17:54 Yep.
I would say so, yeah.
Josh Suereth 00:17:58 Yeah, it's just, to me, it feels similar to just attaching attributes to a span, but instead of attaching to a span, you're attaching it to a process of interest, right?
Florian Lehner 00:18:06 Right.
Josh Suereth 00:18:14 And this PPROF label, what… This is an alternative, this isn't like.
Florian Lehner 00:18:19 Yeah, I just named here four, three different, alternatives.
Process context label might be the most promising.
Yeah.
These are just alternatives, I don't have a heart feeling for one of them.
At the moment, we are just making, or just want to achieve something that, weed it.
the people that speak OTEL profiles can… can share data with each other. Cool.
Josh Suereth 00:18:53 Where are you putting this data, then, in the data model? You said that you don't want this in the resource, is that true?
Florian Lehner 00:18:59 This is correct. In the hotel profiles data model, we have resources, then profiles, and then, samples, and we attach it to the samples. So, it's, I would say, a second sublevel.
attribute, not on the top level of resources. So, as a direct consequence, you will… there will not be a filter for it.
Josh Suereth 00:19:25 Yeah, that's… see, that… this is… this is why… this feels weird to me in our semantic convention data model.
So you're saying that it would be in sample?
Florian Lehner 00:19:34 Sample, right? Sampler.
Josh Suereth 00:19:38 Because the… generally, the entity and the process will be up here, right?
Florian Lehner 00:19:43 Nope.
Josh Suereth 00:19:45 No? Where are you putting process?
Florian Lehner 00:19:48 Profit process is also on the sample level.
On the resource level, we only have an indicator for a container ID, or not a container ID, but everything else is really in the sample level.
Because, if we push everything into resource profiles at the very top, 10…
We have an interest problem.
Josh Suereth 00:20:12 You have an ingest problem.
Florian Lehner 00:20:14 Yeah, because we have too much data.
Josh Suereth 00:20:17 Because of the dictionaries?
Florian Lehner 00:20:19 No, the dictionaries are not, they're up here, right?
Yeah, our dictionaries are there, but the resource profiles does not have access to dictionaries.
they don't benefit from it. Everything in resource profiles is a general hotel resource attribute.
Josh Suereth 00:20:37 Oh, God, yeah, we need.
Florian Lehner 00:20:38 Yeah. Right.
Josh Suereth 00:20:40 Okay, that's… yeah.
Dmitrii Anoshin 00:20:42 What's the entity, like, the entity that would be at the top in that case? Like, a container, you said, but what's the… the… let's say…
Is it… I mean… the…
What other entities would be? Is there any, like, let's say, more specific entity? The container?
Florian Lehner 00:21:08 On the resource profiles level, so that is marked at the screen at the moment, we only put, the container ID, or nothing. So, if we say, hey, you are running on a bare metal host, and there are no containers, then, resource profiles will, likely be empty.
Josh Suereth 00:21:27 Yeah.
This one sounds wrong to me, like…
Dmitrii Anoshin 00:21:30 Right, right. For the entity, we would need some kind of entity at the resource. In that, if bare metal, it means it has to be host, at least.
Josh Suereth 00:21:38 Yeah.
Florian Lehner 00:21:39 We never, read out the host name information.
Dmitrii Anoshin 00:21:43 You don't read, but, like, if you send it further through the collector, for example.
Florian Lehner 00:21:48 Yeah, if a subsequent processor enriches the resource profiles with hostname, totally fine.
But the reference implementation that, in the initial level does not populate it.
Josh Suereth 00:22:02 But let's talk about what's important here, is… Contextual correlation.
Right? So resource exists for contextual correlation, but resource-based contextual correlation of, I know that I was running Process X, and process X saw a latency metric, and I go look at my profiles for the same process. The way we do that today is resource in OpenTelemetry. The resource would say.
would be how we line things up. I am service X of instance ID X, right? So I need to line that up.
So, the fact that process is somehow way down here, because of performance reasons, tells me we need to fix OTLP, not model it that way. Right? Like, I feel like this is something we need to go chase down in OTLP. You should, like, let's focus on what the right mental model is for how to get this data joined, contextually, appropriately. And foundationally.
you know, if I have process X, and I'm reporting host metrics on process X, and I'm reporting, you know, spans on process X, and I'm reporting latency on process X,
I want all of that data to somehow… I know that it's all process X, and that that's the most important thing around correlation here. What you're doing today, though, with putting stuff down here in profile, or sorry, in sample.
We rehearsed that story in Hotel.
Florian Lehner 00:23:25 Yep.
Josh Suereth 00:23:26 Okay, sorry, Ted.
Florian Lehner 00:23:27 trust me.
That's… that's why, filtering in the, in the OTA collector does not work on profiles, because the…
I would say interesting, attributes, or, attributes like a process or process name, or something like this, is attached to a sample, not on the profile, the resource profile at the top.
Ted Young 00:23:48 Yeah, I was just… just, trying to get clarity on whether or not you're putting things down there for… for pragmatic reasons, or because you… the profiling SIG thinks it's the right place to put it. It's sounding like…
practical reasons, right? You're saying you're struggling to put it in the… the resources might be the right place, but you're struggling to put it there.
And that's why you've put it down in sampling. But I'm just…
Florian Lehner 00:24:16 Yeah, yeah,
there are multiple reasons to put it into samples rather than resource profiles. One is the amount of data that is generated.
One of them is,
I think we had some benchmarks at some point before we went…
With the design of the current state of the protocol, and…
It is highly inspired by, Google PProf.
And, yeah, rewriting…
Yeah, at the profiling level, you have a very different view on everything compared to how…
So, from a profiling perspective, we have a very different view on resources compared to logs, metrics, and traces.
And, yeah, I would say that's the origin why… why this… That's the current state.
Ted Young 00:25:19 Right.
Yeah, I mean, it sounds like we need to learn more about
profiling's motivations for putting it down there. Because it sounds like you have some good ones.
Florian Lehner 00:25:31 Yeah, a ton of them is Profiles Dictionary.
Ted Young 00:25:35 Yep.
Josh Suereth 00:25:36 So, the dictionary thing, man, I… I'll push on this with the TC. I think we just need to add a dictionary to OTLP.
Like, like, profiling has convinced me, for sure. I've also been doing a lot of prototyping, on, like, various high-performance, get-out-of-process things for spans and for trace… for, metrics. And in all cases.
it just makes sense to have a dictionary, at least for keys. Even for attribute keys, right? Just generally. So, I…
I think we should actually consider that as a general OTLP enhancement. And specifically, since the profile part of OTLP is not something people have engaged with.
We still have an opportunity, even though you want it to use common resource, we can put a dictionary for you in that common area.
That only the profiling signal would use, and it won't break other people.
So, I think there's a way we can do this, and we should move that forward. Because I, like, we had this discussion several times with, I think the client SIG was the one where they were trying to optimize everything before we really understood the… You understand the problem significantly, you have tons of benchmarking, you've proven to me that we need dictionaries and LTLP if we're going to use OTLP as a…
a way to communicate this data. So, I… I think let's figure out a path forward there. I'll… I'll break…
I now have four topics for a TC meeting this week, but I'll raise that in the TC meeting, and we'll talk through it there. I think, it'll take some time, but let's… let's push on that, if we can. I think that that would be,
You shouldn't have to jump through the hoops you're jumping through.
Florian Lehner 00:27:19 Thanks, I appreciate it. Yeah, profile dictionary approach does come for free, for example. You increase complexity in the OTEC collector quite significantly if you want to filter on something, or if you want to merge two profiles, or
two things that, use a dictionary. Yeah, I'm…
they're… they're both up and downside. For us, we said, hey,
Profiles dictionaries or dictionaries are the best way for us to go, and we accept the downsides.
Dmitrii Anoshin 00:27:57 And can I ask something? But that thing is needed only for the… like, for…
Nathan Smith @ Elastic Observability 00:28:05 network,
Dmitrii Anoshin 00:28:07 compression, mostly, right? It doesn't really make a lot of sense to send that data in this format through the collector, right?
So, why it has to be data model concern if it can be, like, compression or GLP concern only?
Florian Lehner 00:28:23 I think it's not only about the, about the storage on the network path, but also if you expand the protocol then on the collector. We, in, for example, in sample, we just…
have references to all the attributes, all the elements in Profess Dictionary. So, there can be thousands of samples that just reference a single attribute in Profiles Dictionary.
And, if we expand this on the collector, then collector does have a problem, depending on the resources of the.
Dmitrii Anoshin 00:28:59 Collector can introduce something like that internally as well, so it can be collector, like, internal optimization.
optimization for the internal data model, and we actually have, like, significantly improved that recently. But I'm still not convinced that it has to be, like, data modeling problems.
Josh Suereth 00:29:21 The other thing I'm curious about, Florian, is how much duplication you actually have across pro- like, so we're talking about processes and labels on process, right?
Florian Lehner 00:29:30 Sorry.
Josh Suereth 00:29:31 How many processes are we actually talking about in one message?
Florian Lehner 00:29:35 So for the eBPF profiler.
For example, it has a sampling frequency of 20 Hz, and, reports every…
5 seconds, and then profiles are sent out, I think every 1 minute, then we can just take them off, so 20Hz, times number of CPU cores, and then you have, have roughly the idea. So, with
it was, at some point, an Elastic product. We generated…
It was a different protocol, sorry.
Do I have a number at hand? I don't have a number at hand, but…
generally speaking, if you open top at your current device and count the numbers of processors, times 20 Hz, times reporting cycle, times, CPU… number of CPUs you have available. So this, scales quite fast.
Josh Suereth 00:30:43 Yeah, I can see that when you're trying to record everything at every 20Hz. I don't think our protocol's designed around a 20Hz cycle for, like, every process on a host.
Okay, it sounds like we need… we need more information here to guide and help, see ya.
it does sound like having a dictionary, even a shared dictionary for a resource, would be valuable for profiles, if you're gonna report that frequently. Like, but that level of reporting is… is…
Like, would it make sense to store data longer in OpenTelemetry and report less frequently? Like, report at a 1Hz level?
The process of innovation, or is that impossible?
Florian Lehner 00:31:24 And the other way around, so more like… 250Hz.
So…
Josh Suereth 00:31:30 It's numbered per second, right?
Florian Lehner 00:31:33 Yep.
Josh Suereth 00:31:34 So 20Hz is 20 times a second?
Florian Lehner 00:31:36 Yeah, and people are… or customers are asking more about 250 times a second.
For… yeah.
Yeah, that's not that often for a 4GHz machine.
So…
Josh Suereth 00:31:50 I see.
Yeah, are you able to, like, batch it more, though? So, like, even though you would sample at 150 GHz, you'd only report OTLP?
like, one.
Florian Lehner 00:32:00 It can be, yeah, a processor can do this, yeah.
Josh Suereth 00:32:03 Yeah.
Florian Lehner 00:32:04 Processor can do this, but, merging these, profiles.
Josh Suereth 00:32:07 Becomes memory intensive.
Florian Lehner 00:32:10 Because you have to walk the profiles dictionary and the samples, and have to check, hey, where are these referenced? So merging these profiles is a heavy task.
Josh Suereth 00:32:22 Okay.
Interesting. Alright, I think we probably need a bit more information about that, maybe.
I don't know if you have, like, an architecture write-up. Is the… the ePPF profile on OpenTelemetry works that way as well? Where you're going to be sampling very quickly and firing things out quickly?
Florian Lehner 00:32:39 Yeah, sampling frequency by default is 19 Hz.
So, quite low.
But, yeah.
That's how it works at the moment.
Josh Suereth 00:32:50 Okay.
Interesting.
Florian Lehner 00:32:52 No.
the protocol is also now used in async Profiler, so from Java. So, Java Async Profiler can also generate OTLP profiles data, and, often.
the sampling profiler, RSync, RSync sampling profiler, so that usually generates, Sharp for flight recorder data,
they usually have a very higher, sampling rate, or much more than we have with ePPF Profiler. So 19Hz is really low, and just a bare minimum, I would say.
Josh Suereth 00:33:29 Yeah.
Yeah, I, I'm, I'm… I think the,
Generally, we just have an issue where OpenTelemetry has this assumption that you have lots of little pieces of data that you can batch up and send in a big bunch.
What you're trying to do is send a… like, you have a big bit of data, you're trying to send little bits at a time.
Florian Lehner 00:33:54 Yeah, yeah, try.
Josh Suereth 00:33:56 And, and we don't… Yeah. Okay.
I still want to play around with what we're doing in the profile. I think, I think, let's continue that discussion. If you can write down more, like, the use case, what you see.
what kind of overhead we have with various options, we should take a look at that, because, yeah, even with dictionaries, the frequency at which you're sending things is interesting.
Like, we almost want a stateful protocol to something local for what you're doing.
Or where we can, what, what is it called? Content,
content addressable hashing, or whatever. Some way to erase the resource completely, so that you don't have to reference it.
Dmitrii Anoshin 00:34:41 And, Josh, sorry, and that stateful protocol can eventually be introduced for OpenTelemetry in general, for TLP in general, right? In that case, we might be able to avoid all of this complexity.
Josh Suereth 00:34:56 Yeah, we're looking at that. I think… I guess…
to what you're saying, Dimitri, the way I'm thinking about it is…
OTLP right now is large batches, infrequently, like, every minute.
Dmitrii Anoshin 00:35:10 Here.
Josh Suereth 00:35:11 If we have OTLP profiling, we should think about it in that context. If you need very, very fast sampling.
And, like, small batches?
We probably need to think about a different protocol.
Dmitrii Anoshin 00:35:24 Yeah, like, that kind of dictionary can be…
Established once, right? And they don't even have to be sent with every batch.
Josh Suereth 00:35:33 Yeah.
Anyway, for context, there's a couple protocol experiments going on.
One is based on Apache Arrow.
And then Tigrin has one called Simple Tabular Exchange Format.
Both of them are incredibly stateful, so they only work, well, Apache Arrow, I think, can work not with state, but, they, they're, like, WebSocket-based.
And so you can exchange a dictionary, then reuse it.
Florian Lehner 00:36:06 Anyway, I think… I haven't been able to attend the Profiling SIG in, like, 2 weeks or so, or, like, a month, but I'll see if I can attend. Are you… is this the Profiling SIG week, or is it next week? Next week.
Josh Suereth 00:36:17 Next week, okay. I'll see if I can attend, because I think we need to have some discussion there.
So… Yep.
Florian Lehner 00:36:23 Cool, cool, thank you, and sorry for iChick.
Josh Suereth 00:36:26 No, this was a great… this is, again, a really good discussion. I think the thing I want to just confirm with you, though, from a data model perspective, if we look at that hierarchy you had, right, nominally, do you think that if we could solve the performance problems, resource and process
Should be the same for a profile.
Like, the resource is the process, and then the samples are against that resource.
Just conceptually.
Florian Lehner 00:36:55 In theory.
Josh Suereth 00:36:59 Possible?
Florian Lehner 00:37:07 I think the challenges come also from the side that profiles, or eBPF profiles.
Josh Suereth 00:37:11 often.
Florian Lehner 00:37:11 Deployed as a daemon set, rather than, sidecar, like, other solutions.
And that we have… All these levels of… and direction, different to… to,
to other, signals. I think, Serial instrumentation, approach with eBPF.
Josh Suereth 00:37:36 That was, donated by Grafana, maybe, Tyler Jan, can tell about more. I think they are facing the very same issue, that, they have a system view and have to, need to have way more data than just, a single entity that sends out from time to time.
Yeah, I mean, it's, it's multi-tenant, right?
You're about to see a proposal where we're actually going to change the SDK to be able to have multi-tenancy, and be able to report about multiple things at the same time, but I don't think, like, in that auto-instrumentation, we're still recommending the same resource bundle.
And yes.
Florian Lehner 00:38:17 That's a slow disparate.
Josh Suereth 00:38:18 that you have to sort out, but we are recommending that. That's what we'd like to see, right?
Again, let's… Let's start with, conceptually, what do we need?
Make sure we understand that. What's our ideal world? Practically, what do we want? And what are practical limitations? And then let's sort out something in the middle there. But,
Yeah, I feel like we need to address more protocol things, because conceptually, I feel like we're going down a rabbit hole, conceptually, that will make profiles not as good as they could be.
Florian Lehner 00:38:52 Nope.
Josh Suereth 00:38:54 Okay.
Alright, cool.
Florian Lehner 00:38:57 Take care.
Josh Suereth 00:38:58 Let me move on to the next topic.
Florian Lehner 00:39:00 Totally fine.
Josh Suereth 00:39:01 Okay.
Yeah, again, super interesting. Alright, so real quick.
since we only have, 20 minutes, I started updating the OTEP based on the discussions we had 2 weeks ago.
So the idea here is this is an alternative to having mutable resource on the SDK,
We got some feedback that adding entity into instrumentation scope would actually
be even more difficult than just adding it to resource. So this proposal is, you now will have… and I call it for entity, but you can call it whatever the heck you want. I'm bad at naming.
You have a thing where you can take a provider and create an instance of that provider for a specific entity.
Or set of entities.
And so, I can actually say, cool, I created my, my SDK, there's a single resource for that SDK.
But then I can actually start communicating information about other resources.
Using the same SDK's configuration and export parameters. So I will have multiple tenants, if you will, multiple resources that I'm reporting against.
I haven't had a chance to flesh out the SDK implementation. I'm actually still working on that prototype, but I updated the API to what I think will work from that. So the TLDR here, let's do…
So we have a few fundamental new concepts. Basically, resource remains immutable.
We continue to use the entity part of resource that we had in our previous OTEP, and the SDK should get that explicit initialization stage we were talking about.
That's to do to figure out what we want that to look like. Second, SDK will be identified by a single resource. So the SDK… there's a resource attached to the SDK, which identifies the SDK itself, but the SDK can report against multiple resources, all of which will go out in a batch together.
Resource detection, we want to expand as described in OTEP264 to include entities and the environment variable propagation, and we want an explicit section about SDK initialization.
Signal providers in the SDK would allow specialization.
Right? Where basically, you call that four entity, or four entities, or whatever the heck we want to call it, and I'll construct a new resource
for which things in that new provider will get reported against. And so SDKs actually have to be able to have multiple resources attached when they export data.
internal details, I still have some to-dos, but we have API. Effectively, there's four entities, it takes in a set of entities, and then we define what entity it is. This is all the same as before. SDK details are to-do, I'm working on some prototypes, to… or, sorry, the Java prototype.
And I'm reading through the spec to figure out how we have to change things, but effectively, what we're doing is, almost everything in the SDK remains the same.
But there's a new tracking mechanism where I create one of these new meter providers, there is a new resource that things will get attached to. And since I'm doing it at the initialization of the provider, not a lot of the spec actually needs to change. Just the fact that you'll have more than one resource remembered.
It's just, when I call that for entity, I will construct a new resource for the sub.
Set of things.
Okay, trade-offs and mitigations.
We've talked about these before, we want to avoid breaking changes. So, we think that this actually has less breaking change, because you can interact with resource the exact same way you did before, and from a collector standpoint, if an SDK reports multiple resources of information, that's the same as if two SDKs are reporting data.
And today, when people do multi-tenancy crap, they just instrument two SDKs.
So, this has the benefit of there to be one SDK instead of two, so there's less overhead in code, but the collector won't see a difference.
In that sense.
prior art and alternative, we already talked about… I can talk about how OpenCensus works and context things. Open questions. How do we protect against high cardinality entities? I think we… we talked about this before, we need a way to, like, open and close these things to say I'm done reporting against this entity.
So there has to be some kind of lifecycle around this additional context. So the SDK resource is forever for the process.
But we need the ability to say, okay, I'm gonna start reporting about this, okay, I'm done.
We see that in, this issue.
What happens if an entity already exists within resource? The proposal here is that
The new entity is the thing that takes over.
So, I can report about, like, I'm process X, but I'm talking about process Y. I can report my resources process X. If I say, give me a new entity for process Y, that entity type gets replaced.
And I'm now talking about process Y.
Descriptive attributes allowed and changes in resources, for now, basically, no.
We don't allow descriptive attributes to change. All identified attributes are locked, descriptive attributes are locked. When we have entity as a signal, we can figure out what we want to do with descriptive attributes. But I'm suggesting for the purpose of resource, it's immutable and static. If you include a descriptive attribute.
in a resource, you are not allowed to change it for the lifetime of that SDK. So we're probably going to recommend people not do that.
Okay.
what's expected for collector components? I think this means we don't need anything new outside of what we were already working on.
So, I updated that for this.
How do we guide developers on when to use Entity?
We'll have clear guidance for it.
I don't know what else to say besides we'll have to provide guidance. I could put the guidance here in the OTEP, let me know if you need to see it. Last thing, future possibilities. Right now, I think the biggest concern I have a little bit is that this is lexical scope, so I literally have to, like, this is a JavaScript example, and
Tell me if I'm terrible at JavaScript, Daniel, I was hacking this, but, you know, I would have to grab my global meter provider, call 4 entity, pass in the current session, and then I'd have to say, okay, now do something, and here's the meter provider to use. So, I have to explicitly pass context.
And it matches my lexical scope.
We could think about…
Putting an entity in context, and then having context interaction, where if you discover an entity in context, you need to report against that other resource.
And bifurcate that way.
That is an alternative, which is now… that is runtime context, instead of lexical context, because this would be the thread local. So this would be, okay, I attach an entity to my thread local.
So, Florian, this is what you're talking about with labeling processes. Anyway, I'd attach…
Daniel Dyla (Dynatrace) 00:46:30 We can't do this with the current, JS context. In order to do this, like, context with, it takes a callback, and you would have to do something inside the callback, and as soon as the callback ends, that context is popped.
You can't modify the current active context.
Josh Suereth 00:46:51 Okay, it's still lexical, is what you're saying.
Daniel Dyla (Dynatrace) 00:46:53 Yeah, it's still excellent.
Josh Suereth 00:46:54 with, and… okay. Alright.
That's… a lot of context is like that, to be fair.
Click and go, you still have to pass it all the way down.
Daniel Dyla (Dynatrace) 00:47:05 Yeah, I probably wouldn't have done it if I… wouldn't do it that way if I was doing it again today, but it's…
Much, much too late for that particular decision.
Josh Suereth 00:47:15 It… Java also does it that way, even though it's a thread local?
So you have to put a try-catch around it, and it pushes it into a thread local.
For, like, in the try, and then in the finally, it, like, pops the thread local?
Which is a good way to not leak memory, by the way, because thread locals are a great source of, memory leaks.
Daniel Dyla (Dynatrace) 00:47:37 Yeah, I… I'm sure, yeah, that for us.
It doesn't matter that much for this, I guess, but the reason we did it had to do with the wording and the specification made us think it was required, the wording around the immutability and such.
and then by the time…
Anybody said, no, that's not what we meant. It was too late.
Josh Suereth 00:48:01 Yeah, that's fair, that's fair.
Well, I can update that. So basically what you're saying is, even if we use context, it would still be lexical scope?
Daniel Dyla (Dynatrace) 00:48:14 It's still lexical, yeah.
Josh Suereth 00:48:16 Yeah, okay.
Daniel Dyla (Dynatrace) 00:48:20 I mean, you could always instruct your meter provider and pass it wherever you want to, but yeah, it's flexible scope.
Josh Suereth 00:48:28 Well, I think the difference, though, is you're not explicitly passing it, so it's still…
it's still slightly better. So, this is… I have… I have something called Do Something, right? The difference would be, I would still… I would just put, maybe I should edit this somewhere, but I would call do something within the callback.
But I'm not calling do something with this meter provider. I'm just saying do something.
Daniel Dyla (Dynatrace) 00:48:52 Right, yeah, no, I see what you're saying.
Josh Suereth 00:48:54 Yeah, because I don't.
Daniel Dyla (Dynatrace) 00:48:55 It would use the global meter provider, and if that happened to have an entity bound to it, then great.
Josh Suereth 00:49:02 Yeah, and so we could have… we'd have to update the spec to basically say, if, if you…
If you get a measurement, right, someone tries to, like, record something.
and you detect an entity, then go grab the meter provider for that entity and record it against that, instead of the one you're using now, right? So we'd have to have
That would look up map at measurement time for this, which would slow down all measurements.
Daniel Dyla (Dynatrace) 00:49:28 So we… we have a different mechanism for this. We have a, like, a helper library for writing instrumentations, and there's an instrumentation…
class, that's, like, the main orchestrator.
Josh Suereth 00:49:41 Yeah. And…
Daniel Dyla (Dynatrace) 00:49:42 it takes a meter provider and a logger provider and a tracer provider at the creation time, and you could just give it a different one for the instrumentation. So the instrumentations are all using their…
they don't call the API directly, they call it through the instrumentation class, and we can just give them a different one.
Josh Suereth 00:50:04 Well, I…
Daniel Dyla (Dynatrace) 00:50:04 So that's the way that…
Josh Suereth 00:50:06 The question would be, then, if I need session, this wouldn't be Node.js, this would be your browser instrumentation, will this work with that?
like, will I be able to basically.
Daniel Dyla (Dynatrace) 00:50:18 Yeah.
Josh Suereth 00:50:18 With a different session.
Daniel Dyla (Dynatrace) 00:50:21 Yeah, because the instrumentation would be able to just swap out the meter provider in its instrumentation implementation.
Josh Suereth 00:50:29 Instance, whatever you want to call it.
Okay.
Daniel Dyla (Dynatrace) 00:50:37 Yeah, I don't think that that's a problem. Obviously, we have to prototype to make sure, but…
On first glance, I don't think it's a problem.
Josh Suereth 00:50:44 Let's look at it. I do want us to consider junk like this in the future, including, like, attaching labels via context, attaching entities, like, there's a bit of context we're not taking advantage of in OTEL.
that, I think could have some value.
But we also need to be careful, because anytime you add something to context, you can explode the runtime complexity of a process.
Daniel Dyla (Dynatrace) 00:51:11 Yeah, part of the problem in JS is that the context implementation is actually not in the API, because there was no…
built-in context at the time that was stable in Node.js, so we needed to be able to swap them out with the SDK. That's no longer true anymore, so now our minimum version has a built-in, context. Like, the async local storage is accessible and it's stable.
So we've been discussing the possibility of moving the context implementation entirely into the API.
Then, essentially, the…
the operations that register a context manager from the SDK, I mean, they might continue to work, or they might just no-op, but then that would allow us to make changes to the way that the API works a little bit more easily without requiring new context manager implementations.
Josh Suereth 00:52:03 That… that's cool.
Daniel Dyla (Dynatrace) 00:52:05 So we could potentially evolve to this in the future if there's a need for it, I guess is what I'm saying. But right now, we can't do it.
Josh Suereth 00:52:11 Well, this is where I think we have to prototype the browser-based work.
Daniel Dyla (Dynatrace) 00:52:15 to figure out… Well, the browser is even worse, because there is no context in browser. There's no, like…
Josh Suereth 00:52:21 Yeah, no.
Daniel Dyla (Dynatrace) 00:52:21 There isn't even a concept for it. There's nothing that exists. It's the number one, complaint that we get, and we can't do anything about it.
Like, you have to use either,
Zone.js, which is, like, a massive dependency.
Or nothing. That's essentially your only two choices.
Josh Suereth 00:52:42 I see, so you basically don't have context. So this isn't even a possibility in the browser.
Daniel Dyla (Dynatrace) 00:52:47 No, it's… that's never gonna happen.
Josh Suereth 00:52:49 Alright, then we have to check.
Daniel Dyla (Dynatrace) 00:52:53 There is a, a TC proposal for context, built into the language.
But it's, I mean… best case scenario, 2027 or something like that, and… The absolute best case scenario.
Josh Suereth 00:53:12 Yeah, you know, I don't mind waiting.
Okay, interesting. So, if we go back to this, you know, I… obviously we need some SDK details and some more prototyping. How do folks feel about this directional shift? Any thoughts, concerns, complaints?
Dmitrii Anoshin 00:53:31 Sounds, sounds great to me.
I don't have any concerns.
Josh Suereth 00:53:36 Okay.
I think this definitely, cleans up our prototypes a good bit. I am a bit nervous about, getting enough of the SDK implementations out here.
So, I'll start working… sorry, specifically.
Where is it? The issue that we have around cardinality.
I'm thinking about
Having… instead of it returning a meter provider, having it return a thing that's like a meter provider that also has a close method.
Because the API doesn't have a close method.
Daniel Dyla (Dynatrace) 00:54:15 The meter provider has a shutdown method, though.
Josh Suereth 00:54:18 in the SDK.
Not in the API. This is an API-level access.
So there's an API meter provider and an SDK meter provider.
They're different.
So…
since I think… I think this needs to be an API-level thing, because I think you have to be able to do it from the API,
Also, so that's part one, is I want to add that close, and I think I'll probably do that in my prototype and then add it to the spec, unless folks have concerns.
Nathan Smith @ Elastic Observability 00:54:51 No!
Josh Suereth 00:54:56 Okay.
Daniel Dyla (Dynatrace) 00:54:57 Nathan?
Josh Suereth 00:54:58 be.
Did you want to say that out loud, Nathan?
Nathan Smith @ Elastic Observability 00:55:03 No, I did not, sorry.
Josh Suereth 00:55:05 Okay.
or is… It was kind of perfectly timed.
Daniel Dyla (Dynatrace) 00:55:10 Yeah.
Nathan Smith @ Elastic Observability 00:55:11 If you want to know the context, I'm actually…
building a door, like a root cellar door in my house, and listening to this, and I just put the second door on upside down.
Josh Suereth 00:55:24 owed.
Nathan Smith @ Elastic Observability 00:55:24 So I gotta take it all apart again. I just figured that out now, and I didn't know I was…
Not muted, so sorry.
Josh Suereth 00:55:31 Oh, wow.
It'll, it'll, it'll all be good.
Yeah.
Ugh, that's the true kind of prototyping.
Oh yeah, from… if you were in the meeting last, like, the semantic convention, Ludmila was upside down for some reason, in her camera. We have no idea why.
I made a Stranger Things reference, but I think I got cut out. Anyway,
Okay, so the second thing, for this…
It was high cardinality metrics and close… oh, right, right. Do we want to make an OpenTelemetry thing that is, like, a container that gives you access to all of meter provider, Tracer provider, and logger provider?
Or…
Daniel Dyla (Dynatrace) 00:56:16 You're talking about an instrumentation API, which I think a lot of people have, brought up as a possibility many times over the course of many years.
Josh Suereth 00:56:25 Yeah.
Daniel Dyla (Dynatrace) 00:56:26 I think every implementation essentially has one already, they're just not specified in any meaningful way.
Josh Suereth 00:56:34 Well, and I think they conflict with each other.
If we tried to specify it, I think we'd break all of them.
Daniel Dyla (Dynatrace) 00:56:40 I think it would have to be, like, a new… a new, like…
Yes, you'd break all of them, they would have to all… all of them would probably have to deprecate what they have, and…
I guess there's two ways to go. One would be to look at the state of the world and try to come up with a loose enough specification that all the implementations would be okay. The second would be to say, we don't want to do that, we're going to make a new specification.
And you have to deprecate what you have.
And maybe it continues to work, but, you have to build this new thing as well.
Josh Suereth 00:57:15 I'm leaning towards the second, but with a different message of, make the thing you have now work on the thing.
And eventually, people will migrate, but just keep both.
The only, the only thing that has me hesitant on this, and one of the things that I think we've pushed back on previously.
We want OpenTelemetry to be loosely coupled signal-based things, so if I use metrics, I don't have to use logs.
The only caveat here that we are doing with entities is because resource is foundational to all of them, we're forcing resource to exist somewhere, right?
And we're formalizing what that looks like, we're formalizing the SDK around it.
So, I… I… I'm…
kind of getting conflicting ideas in my own head about where to go here, right? Should we just basically say, you know what?
We're at a point now when you engage with OpenTelemetry, you get everything.
And if you don't use the API, then it's not used. Or do we want to keep them completely as disjoint, so I can say, I only use tracing, I only use metrics, I only use logs, and everything's still healthy?
Daniel Dyla (Dynatrace) 00:58:23 They have to be disjointed for the browser.
Josh Suereth 00:58:27 Okay.
Well, there's an answer.
Daniel Dyla (Dynatrace) 00:58:33 I mean, yeah, some of the browser folks are very sensitive to the idea of, you know, one possible answer is tree shaking solves this, but it doesn't solve it as well as just not bringing it in to begin with. And we have some people who are very sensitive to that.
Josh Suereth 00:58:52 That I can see. Okay. Alright, well then…
Tyler Yahn 00:58:54 Daniel, just got a question for you there. How do you do, observability of the SDK without bringing in other dependencies, then?
Daniel Dyla (Dynatrace) 00:59:03 We log everything to a global logger that is no-op, that you have to.
Josh Suereth 00:59:11 you know, it's…
Daniel Dyla (Dynatrace) 00:59:11 It's essentially a function that we call that does nothing unless you register something to it.
Tyler Yahn 00:59:18 So do these log messages to get translated into, like, traces and metrics?
Daniel Dyla (Dynatrace) 00:59:23 No.
I mean, you could do that if you wanted to, but right now, they just log out to the console.
Actually, right now they do nothing. The most common thing to do with them is to log them to the console.
Tyler Yahn 00:59:35 Oh, I meant, but, like, the semantic conventions are defined for the OpenTelemetry SDK for, like, metrics and that kind of thing.
Daniel Dyla (Dynatrace) 00:59:41 Yeah.
Tyler Yahn 00:59:41 that?
Daniel Dyla (Dynatrace) 00:59:42 We just don't do that.
Tyler Yahn 00:59:45 Okay, thanks.
Daniel Dyla (Dynatrace) 00:59:46 I mean, we… one possible thing we could do is just call the API methods, and if they're registered, then they go somewhere, and if they're not, then they don't. But as far as I know.
Nothing like that's implemented.
Tyler Yahn 01:00:00 Yeah, that's… that's what we do in Goeswell. I just, I didn't know if that's what you meant by bringing into the dependency, though.
Daniel Dyla (Dynatrace) 01:00:06 Yeah, so the API has all of the… Signals in it.
But each signal has its own SDK implementation that has to be separately registered, because that's where the bulk of the code is.
Tyler Yahn 01:00:21 Okay, I gotcha. I think I misunderstood. So yeah, like, bringing in the whole API is not the problem, it's just the SDKs.
Daniel Dyla (Dynatrace) 01:00:28 Yes.
Tyler Yahn 01:00:28 Yeah.
Josh Suereth 01:00:36 Alright, well, I think, to end that and end this meeting, if anyone has time, I know, Daniel, you're working on a prototype as well. If you wanna…
start migrating your prototype to match the OTEP. We need to flesh out the SDK section and get the prototypes done, but I feel like we're making good progress, so let's,
Let's get that working.
Daniel Dyla (Dynatrace) 01:00:57 I actually already started on that before you made this, OTEP change, because I…
Saw that that was the way the wind was going to be blowing.
Josh Suereth 01:01:08 Nice. Maybe next time you could show us what you did.
Daniel Dyla (Dynatrace) 01:01:11 Okay.
Josh Suereth 01:01:11 Cool.
Alright, thanks everybody. See y'all next week.
