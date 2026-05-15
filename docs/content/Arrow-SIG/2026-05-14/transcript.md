SIG: Arrow SIG
Date: 2026-05-14
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Laurent Querel** 01:50 Are you a win?
**Aaron Marten** 01:54 Hello, morning.
**Jake Dern** 01:56 What? Hey, morning.
Bye.
**Laurent Querel** 02:09 Okay, it's Peter with my airport connected.
I even win.
Do you know what I mean?
**Aaron Marten** 02:16 Yes, good morning.
**Jake Dern** 02:18 Yep.
Morning.
**Laurent Querel** 03:19 Okay.
Aaron, we… are you there, today, for this afternoon, at the, the, Raid Monde Compass, Microsoft Compass.
**Aaron Marten** 03:34 Yes, yeah, I'm here at the Redman campus right now.
**Laurent Querel** 03:37 Okay, quick.
Okay, let's put Barrel down.
Okay, so right now… Cool.
Jeez.
Always.
Okay, let's start.
I don't know if we will, be, much more today.
So we can start with the triage.
quickly… And please add, any topic in the agenda.
Opening kids… Accepting, accepting, accepting, okay, deciding.
Okay, so I guess I can start.
So this one, implement staff protocol for Whatap Engine.
So the… that's following a discussion I had with, et Joshua.
So the idea is basically to… to support in addition to the TLP and OTAP staff, which is, A protocol optimized for transport.
will comprise even more than OTAP, probably for some, some workload.
It's optimized for transport, not really for, Processing, so there is a desertization, salination phase.
easier than… of what Autobuff is doing.
But there are ways to optimize it. So they started the implementation of this protocol, Because to… we know that we will have to, we will have this kind of question in the future, how Steph is behaving, against, OTAP.
And, because we were working on benchmark, I think it's important to work on that.
Any question on that?
Okay, create dashboard comparing. So, Jake, maybe you can talk about this one?
**Jake Dern** 07:05 Yeah, I mean, I can kind of give a little update where things are at. So we have all of the, you know, sort of, like, very minimal framework code checked in. We have a lot of testing suites to find, mostly just for baselines, so covering OTAP, OTLP, OTLP, HTTP, and all of the above with, you know, no compression, GZIP, or ZSTD.
And we have that for the data flow engine and for the hotel collector. We also have the site publishing alongside the existing site, so this is at that slash compare endpoint.
And we kind of have all the machinery in place, you know, for all of this to be automatic. So the gist of it is that, all of the site code and the comparisons and the suites and the definitions of all the stuff that's, like, important, that's not data, lives on the main branch.
And then, anytime we check in data to the benchmarks branch in a particular directory, then automatically a build fires and generates a static site, and automatically commits that to the same branch, so… Basically all the generated stuff and data lives on the benchmarks branch, all of the definitions of everything and the site code lives on the main branch, and all that machinery is kind of up and running. So, there was one kind of hiccup with getting final data, at least for the data flow engine, which was there's this, like, small, small latent bug that we had with, the Prometheus metrics that, I believe the fix for was just merged last night, so… I'm gonna start running, all of these baseline suites again, try to get final data.
And yeah, we'll start publishing stuff soon, starting with the Dataflow engine.
**Laurent Querel** 08:49 That's great, thank you. Yes, I guess it's… That has been merged yesterday.
**Jake Dern** 08:59 Yeah, I think last night sometime, it got in.
**Laurent Querel** 09:03 Okay.
Great.
Back to the… So, yes, okay, log receiver for SystemD, journal logs… I don't know about this one. Do we have with us, Joshua?
No. On the experience, we are interested in internal D-log receiver.
Cute.
I don't think there is any.
**kennedybushnell** 09:40 Yeah, this probably came from… Kind of indirectly from someone on my team.
Again, we collect a lot of logs from Syslog. We have some good coverage there in OTAP Dataflow. We've got JournalD and files, or kind of… The main thing on one of our platforms.
This is probably just to kind of get that ball rolling.
**Laurent Querel** 10:04 Yup.
And, Because the… We can imagine that there are a lot of commonalities between, This specific receiver and the file log receiver we discussed last week.
Did you think about it, to see how, That could be combined, or even if it's interesting, it could combine them.
**kennedybushnell** 10:30 The file log receiver and…
**Laurent Querel** 10:32 and the… Yeah, and the system digital debugs.
Receiver that is defined there.
**kennedybushnell** 10:42 I haven't thought about that.
**Laurent Querel** 10:48 Yeah, I think that's… Something we need to… I don't even know what the GoCollector is doing regarding that.
Do you know if they have a dedicated receiver, or if it's part of the 5-log receiver?
**kennedybushnell** 11:04 I… am not sure.
I no longer really think about the Go Collector, to be honest. I'm not trying to, like, mirror those, so…
**Laurent Querel** 11:15 Yeah, okay. Yeah, okay, so I will, talk to Vijosh and, try to figure that out.
So then we have the flow matrix, so do we have Joe with us?
Otherwise, I can talk about that.
**kennedybushnell** 11:34 today.
**Andres Borja** 11:36 Yeah, he's out of the office today.
**Laurent Querel** 11:38 Wicked.
So, that's something interesting, so we… we basically introduced, this concept to measure Subraf into a pipeline.
So basically, we can specify the beginning and the end of, part of the graph, notified by NodeID, and then we have a way to measure this specific flow And, we measure the… The average, duration, For the transit of batches that traverse this flow, or to measure the, The number of batch and signal entering into the flow, or… Exiting the flow.
So that's relatively cool, especially when you… you want to represent, Combination of nodes, and… It's much easier to do this way, because the aggregation is already done directly.
And there is no need to find some ID into the different metrics.
To combine them, it's not necessarily super easy, so that's a very cool, I think, solution.
Dude, it's… Okay, what's up? Mini 10 is expensive, we're using PACT.
implement single-pass allocation for review for calculating new attempts.
I think it's related to you.
I don't know the detail for this one. Is there anyone, today that, know about that?
Okay, opting items and bike screens, I think it's related also. Yeah, so this one… I encourage everyone to… to read, so there is an open PR right now.
Which is, here.
not necessarily to spend too much time on that today, but, basically, I tried to… To write a set of documents on… Describing values.
AI workflow I'm using regularly.
And I think where we need to… Oh… progressively improved, for example, for the… the review process, I established a list of, design principle to follow.
That we can easily use as a prompt for cloud or for… critics.
In order to identify much more quickly, issues, that are not aligned with the design principle for this project.
So that's this document. And I'm sure that we will, Make a lot of modification on this document progressively.
And because we have so much, much more activity, week after week. I think that that will be super helpful to, To improve this process.
Then, two additional, what I name, AI-assistive component development.
So that, that will be the topic of, I guess, a long discussion this afternoon, in the… Microsoft Corpus, so I will not go too much into detail, but… It's about, I will take two examples, the 5-g receiver and the osmetric.
We know that they are super important in the ecosystem.
They already exist.
We don't necessarily want to reproduce exactly the same configuration, exactly the same, type of behavior.
But we… we want to deliver, basically, the same, The same type of component, but we also want to learn from the feedback from the community.
So this process, this one, Describe, basically, the workflow I use to Collect all the feedback.
from various sources, like GitHub, GitHub issues or PR commands.
On the corresponding component that you want to re-implement.
Plus, they use other sources. And based on those, feedback, Enter into a design, a specific design.
Session, taking into account the… specific, Architecture that we have, which is… Sometimes, not negligible, so the thread blocker, for example, in the context of the file log receiver, Impact a lot the design.
So it's about that.
And how we can use AI to accelerate this process.
And the other one is the one that I use for, staff.
That's what is commonly called, a spec constraint, or right?
Oracle, re-implementation.
So, when we have something like a protocol, relatively well specified, Where competitive material.
It's a perfect match for this kind of approach.
where we can effectively run a Go implementation And automate the implementation of the corresponding In that case, a staff protocol.
the European roast.
And, and test again, so, for example, we can have the Rust stuff Exporter, communicating with the… the Ghost F, receiver, and do the same thing on the other side.
And that's… Accelerate a lot the reimplementation.
Of something like stiff.
So that's the seven documents.
I guess we will, go much more in the detail later today.
Good news.
Yeah, that is something that is, Oh, Jake, I think we, it's still not, do we have any issue to merge this, the corresponding PR to be central.
**Jake Dern** 19:01 Yeah, the only blocker to this… But… and I'm not sure exactly what the issue is, but it looks to me like when we run Cargo Next Test Archive, for some reason, the runner's, like, running out of memory or something. It's getting 143, so I think it's getting killed.
I don't know why the changes in this PR would cause that. If anybody has ideas, let me know, but that's… that's the blocker right now, is, yeah, the runner seems to be running out of memory or something during cargo next test archive, on Ubuntu Latest only, which doesn't make sense to me, but… alas.
**Laurent Querel** 19:38 Okay.
You know, we need to fill that out.
Yeah, like I told you, I think, when we had, discussion on that. I'm not sure explanated, but, something I'm sure is… when we… we are using Next Test.
for all the tests in the CIA.
I really think that we need to move from this system. It's not very… it's not working well for our project. I don't have any good explanation of… on the why.
But definitively, when I'm using NextText on my laptop, it's… Two times, three times slower than just the basic cargo test.
So we are already doing something wrong, but in the meantime.
When we have build, and maybe when they are, done into a container, that could be, That could help a lot if we, migrate to cargo test, and then figure out why next test is not working well in a certain time.
**Jake Dern** 20:50 Yeah, yeah, if anybody has ideas on this one, please let me know. It'd be great to merge it. I did include some benchmark results in the attached issue for that, and yeah, I mean, for cases, with compression especially, are the most affected, and I saw, like, an over 50% perf bump, so definitely want to get this in.
**Laurent Querel** 21:10 Nope.
Support live… Okay, so that is something that Chris, added. So we already have label configuration, but there are some operations that are not yet fully supported.
So that's about that. Making the distinction between shutdown and deletion.
That's one aspect, and Right now, we have, I think we are covering relatively well the lifecycle for starting, stopping pipelines?
We don't really have a similar, Coverage for groups in general, so we can shut down a group.
But we can't start from scratch a group.
So… Follow me.
in the context of a controller, I know that Microsoft has exactly the same requirements on their side that we have for 5.
So, for example, we could imagine that we start the engine with, an empty configuration, And, So we provision, basically, the engine, but then we… we want to add or remove, groups.
Right now, we can only update an existing group, we can't really create new groups, so that's about that.
Status condition sent for intentionally stop pipeline, I guess it's related.
Oh, Chris is not there today, so… okay… A metric to track number of dropped events, or log sampling.
Okay, that's from Ken.
Oh… On this one, Jake, that's not something that we already have, the ability to understand how Much, signal has been dropped during the sampling.
**Jake Dern** 23:07 I need to go back and check. I don't recall exactly what the gap was, but, yeah, it's possible.
**Laurent Querel** 23:16 Okay.
add counter matrix to track number of pass-through matrix for the temple. Okay, I guess that will be the same answer.
**Jake Dern** 23:26 Yep.
**Laurent Querel** 23:27 This one… I think it was, way too… too sexy.
Okay, that's a SQL report, I guess. Nothing specific on this one, in addition to what you already explained?
**Jake Dern** 23:47 No, there's something pending merge for this, it's a different issue, but, just a small… just have to add, like, a string for the hotel collector, to the SQL reports to get them to report CPU metrics, yep.
**Laurent Querel** 24:01 This one looks interesting.
Aaron, do you want to talk about this one?
**Aaron Marten** 24:05 Sure, yeah, and I put this one on the agenda, but it looks like we're through the end of the issue, so, So, I mostly wanted to get this one, filed, because… just to get some community feedback and start the conversation about it.
This is a… kind of a high-level proposal at this point. I intend to create some sub-issues underneath it that go into a bit more design detail, but I wanted to make sure that, like.
Everyone is aligned on general direction before we dig too much deeper.
The basic idea is that we should have some support for some kind of binary plugins. I'm avoiding the word extensions, because we're already using that to mean something else, so… And, the basic idea with what's proposed here is that we… we do… we use WASM, as a kind of our main you know, Binary method to actually host Host these binary plugins?
And that we use a… what I'm calling a host kernel.
API design for that. So, the idea is that if we're hosting WASM plugins, one of the big, Issues you'll notice.
if you try to do anything with WASM, is that, you know, WASM needs its own memory space. And so, typically, when you're… you're talking about, you know, a plugin system, you're… you're copying data back and forth To that plugin, which is, in its memory space, which is gonna, kind of kill your performance.
So the idea is that we would implement, a series of APIs that the WASM runtime would call back into to be able to operate on the data, and that, ideally, plugins would be able to use those kernel APIs to operate on the data without actually having the data copied into it. Of course, there would be ways if you really did need the data, to get it into the plugin, but you're going to take a perk penalty for that.
**Laurent Querel** 26:11 Yo.
**Aaron Marten** 26:12 that's kind of the idea in a nutshell. This talk goes into a little bit more detail underneath that, and describing kind of some of the some of the kernel APIs we could offer.
**Laurent Querel** 26:25 Yeah, I totally, agree with the approach. So the two comments, so the… we started a work around the PData object to improve the interface, to make it exposing action command, instead of exposing directly the low-level operation for Aperture.
I think that that will help a lot for this, WASM interface that you are, you know, you are mentioning.
And the second thing, It happened that we are lucky here at F5 to have, a lot of wasn't time not sooner.
In fact, also for Quanlift.
So I talked with them a few months ago about this idea of integrating WASM into the Dataflow engine.
And, the conclusion was… so, obviously, the discussion was around, avoiding the override of copying the… the batch, from the rest, to the… to the wizard runtime.
So the… it looks like… The best method.
Based on their feedback, is to use the concept of resource.
That's maybe what you have in mind also.
So, resource is basically a handle that you can use from your WASM plugin.
to interact with something that is, in fact, a resource into your Rust program, which is Rust in that case.
**Aaron Marten** 28:14 Yep, yeah, that sounds very similar to what I'm proposing here. If you look at that diagram there, you can see that that's pretty much it, right? Like, the aerody into WASM as an opaque handle.
Yeah.
**Laurent Querel** 28:27 Yeah, yeah, yeah.
The… no, the… I think the WASM integration, will be… Because in this specific case.
It's a WASM plugin that looks like a processor.
But the question will be… obviously, we… we could imagine a WASM plugin for a receiver, a WASM plugin for an exporter, and same thing for the… for the… for the processor. They will not necessarily have the same Integration mode.
Another discussion I had with, those people, specialized in Western time, was… calling, from your ROS culling a WASM plugin.
That's some overhead. You don't avoid… So they, they were suggesting to… To have a long, a long, long-running plugin.
So, for example, that's very similar to the concept that we have with the receiver and the exporter.
Where we start them, and then they're… they basically… it's like an invert loop inside the receiver, inside the exporter.
So that, is probably a good match for a WASM plugin, and we could imagine that we could do the same thing for a processor.
Even if today.
processors for a different reason. They expose a method, process, and the engine called this process method for each Incoming batch.
The reason why we designed the engine this way was to be able to combine multiple processors together.
In order to eliminate intermediary channels.
When the topology of succession of, a chain of processor allow just something sequential. In fact, we can… Fuse them into a chain and avoiding a lot of override.
So that's why we had this, difference between processor, receiver, exporter.
But we could, easily imagine that, We extract the event loop that is part of the engine into we could have a new kind of processor that is maybe better for a WASM plugin integration.
That will be a long, Similar to the receiver, basically implementing the event loop.
Directly inside the plugin, so that there is no… overweight.
To start, stop, to call, basically, the processed metal.
That's maybe something we need to think during the design of this thing.
**Aaron Marten** 31:35 Sure.
**Laurent Querel** 31:38 Okay, great. So… Regarding the, Okay, so that's basically what we just discussed about the… So is there, maybe, additional, Explanation you want to provide, or question from the… From the people that participate to the meeting.
That one needs to peak.
**Aaron Marten** 32:10 There are some open questions, if you pull the proposal back up, if you scroll to the bottom, maybe we could, go through.
**Laurent Querel** 32:20 You?
**Aaron Marten** 32:22 No, all the way at the bottom.
Yep.
**Laurent Querel** 32:28 Okay.
**Aaron Marten** 32:33 Yeah, so career vocabulary scope, that's just… that's just asking for feedback on the, you know, on the proposed API.
**Laurent Querel** 32:49 Oh, that's…
**Aaron Marten** 32:52 Yeah, I think, I think I gotta fix that.
The anchor leak, it's to a previous, previous section in this.
**Laurent Querel** 32:59 Okay… okay, that's lovely.
So that's deepfilms… Yo.
Category of operation.
Record Builder.
a servicing… Looking okay.
alchemos… True.
the jet.
I think that the… Something to consider, also, around, Basically manipulating your… Processing records, with operation.
An alternative could be to give access to OPL, Because we could imagine that the plugin create an OPL program.
And we have a way just to apply this OPL program on the batch.
And then we will inherit all the… the opioids are supported by OPA.
Which… Aggressively will cover all the… the need that we could imagine on… processing signal.
Maybe that's, another way to think about it.
Do you have any opinion, Aaron, about that?
**Aaron Marten** 34:45 So… I guess I have more of a question than an opinion. So with OPL, Is that something that would necessitate a plugin, or can we just do OPL through, you know, just through a transform Specified in… in configuration.
**Laurent Querel** 35:08 No, I was thinking, offering the ability to… to execute an OPL program on… From the… the WASM plugin.
On a specific batch.
**Aaron Marten** 35:28 Okay.
**Laurent Querel** 35:29 So what you, what you name, basically, are OKR names?
It could be, in fact, an OPL program that will apply All the transformation and filtering function and other things like that.
But much more… covering much more operation, because in OPL, we will cover more than just filtering, replacing, and so on and so on.
Well, that could be, A nice way, basically, to support the… All the, the possible operations that we can imagine on, stream of signal directly from a WASM program, and the WASN program will be there just to Build on the fly.
the, the OPL program that, this wasn't plugin going to, So, sometimes you can just use the… the transform processor, that will be enough, but when you have something more dynamic, and you want to apply transformation that, Will change over the time.
Then you could imagine that you have a WASM plugin.
generating on the fly the OPL and applying this OPL program directly on incoming… But she's… I didn't think about it too much, but maybe that's, interesting option.
**Aaron Marten** 36:58 Yeah, no, I think that makes a lot of sense.
Good suggestion.
**kennedybushnell** 37:02 I hate… I don't know that I do. So I'm, like, it feels like transform should be kind of a separate concern, kind of is, like, single responsibility principle, right? So, like, I do see a path where there's value for the plugin to be able to say, like, hey, I always want, like.
like, basically, I need you to generate a piece of the DAG for me, so the DAG gets generated really at config time, ultimately, but there's, like, almost a post stage. So you could say, hey, I always need this thing that drops this column after my output. So put the transform processor, maybe it's an OPL processor, with a drop column.
thing. But ultimately, the DAG is a config time piece of execution. I don't know if… maybe I'm wrong in that OPL, like, is also considered just a general function that you call, but, like, I've always kind of bundled that with, really a transform processor specifically.
if that's not the case, then maybe it does make sense, but, like, arrow kernels is really, like, a function that you call as part of your general processing and everything, so those types of things make sense to me.
But if you're wanting to be able to use OPL, or even KQL, you know, whatever your, like, kind of favorite language is.
I could see value in being able to kind of control your DAG a bit.
**Laurent Querel** 38:37 I'm not sure to follow with the bag, R&L, but.
**kennedybushnell** 38:43 maybe you call it something else, so, like, the wind…
**Laurent Querel** 38:47 I don't understand that, but I don't see how the DAI could be transformed either with… the… the WASM plugin or the transformer.
For me, the DAG is basically, a definition of receiver, processor, exporter interconnected together.
In some way, so the engine take the configuration, create the corresponding DAG, and run the… And the data flow engine is basically, implemented on top of a DAG where data flow, the Apache oral records flow across this DAG. I don't think that's… Either the plugin or the transform changes the… on the fly, the configuration of this deck.
Stu Lucidon.
Or maybe I misunderstood what you mean by DAG.
**kennedybushnell** 39:37 Yeah, so I'm kind of saying that, like, Maybe, maybe… Maybe we're misunderstanding each other in both ways, so that might be part of the problem, but like… I can't think of a… a real example, so I'll just make one up, but let's say syslog, our Syslog receiver.
Always needs to run a transform after it that goes and changes, like, some field.
to split, like, the name and IP out into two different columns or something. And we've determined that we want to do that with OPL for some reason. So, you could have Syslog, like, natively call into, like, an OPL runtime and do that.
Or, you could… we could teach the system how when you instantiate a syslog receiver, it always puts a… I don't know, syslog, like, an OPL transform… right after the syslog receiver with the OPL for that split function, and then, when it goes and builds out the rest of the DAG, it just keeps doing the thing it always does. So you can have another transform that's user-defined that goes and drops IP column, because that's what I want. But syslog is able to, like.
Instead of just instantiating one node in the DAG, it can say, here's, like, my little DAG section that gets inserted.
**Laurent Querel** 41:00 Yeah, so we, we, I understand.
In my opinion, the… this combination… of nerds.
It's more a concern of having higher level In my opinion, higher level configuration option.
That, for example, a controller for a specific situation, we'll decide, okay, we need to implement the… an extended syslog, ingestion, processing stuff, and and automatically we… this controller will generate a configuration with exactly what you said, a C-slug receiver, just after that, a transform processor with an API program that do something on the, specifically.
At the data plane level, for me, it's just, a system that doesn't try to be super smart, so just executing a DAG, I don't know if we really need this option of, A receiver that, Explain to the engine, or by the way, put, A processor just after me, Maybe it's a good idea, but for me, it's more… Something higher level to the data plan that will, in fact.
Do that, and just provide the configuration to the data plane.
**kennedybushnell** 42:41 Yeah, that's probably fair. I guess I… Let me ask this. Do you view arrow kernel calls and OPL Function calls as equivalent.
**Laurent Querel** 42:57 No, the arrow kernels are, like, the primitive used by OPL.
So it's not strictly equivalent. OPL add more on top of that.
Our kernels does not necessarily understand the semantic of open telemetry signal, so that's basic operation, operating on A generic record with columns.
OPL will prevent to… To build, invalid signals, for example.
So there, for me, there is, an additional semantic layer, or… Multiple layer of… in a PL, as opposed to KQL, that's all the discussion we have regularly, With, Mike Blanchard, the… And that was my initial concern with EQLs.
AQL is a general stream-oriented processing language.
OPL is… Dr. Jean-old is, tailored, stream-oriented processing language for open telemetry.
There is a strong guarantee that Everything that you can do in a PL will necessarily generate a valid stream of signals compatible with the OpenTelemetry model.
Yeah.
**kennedybushnell** 44:25 I'm more specifically asking in context of, like, exposed APIs that we would need to plug into these, right? Because, like, OPL has a lot of functions, and then that contract, like, probably grows over time in some cases. I don't know how… So, like, changing that contract between something like this, it ends up being pretty complex.
And… and full of thorns, right?
So, is that something that these… like… Arrow kernel calls is something that I… I've seen many receivers, processors, and exporters used directly.
it's, like, pretty natural in the flow of… of messing with these arrow batches. Opl… I haven't seen, but, like, directionally, is that something that we… we think… Could or should be done.
**Laurent Querel** 45:19 Yeah, that's my opinion, but just to…
**kennedybushnell** 45:23 Okay.
**Laurent Querel** 45:23 trying to, I think it's okay if we… we could imagine that we have different, level of abstraction that we expose.
A whole kernel could be one.
Opl could be a higher level… abstraction that we are also exposed to Wazan plugin.
Exactly the same way that we could imagine that we have, Not knowing the stream processing, system that operates over, tabular information.
could expose a SQL, query layer.
That let this plugin Do whatever they want on a specific table.
We could also imagine that this plugin access to lower-level operation.
Like, the… Operation that we can imagine to have in, a query plan, it's… the parallel is relatively close. Let's say our kernels are, like operation in a query plan, and SQL versus OPL are the same level of abstraction.
Do you imagine that into a plugin that is processing tabular information?
People will prefer to have access to the the low-level operator versus SQL.
Maybe, in some situation.
You were talking about, about, exposing, sorry, exposing the… Interface that could change, and so on.
In my opinion, the experience, based on what we see in the SQL now for many years.
The query plan can change a lot.
The basic operation can change alerts.
the SQL program is still the same.
So I'm not that sure that it's… Better in terms of, interface.
To provide the low level, instead of providing something that is more… A declarative language, always high level.
Yeah, I mean, it's a long discussion, I don't know, we need to think about that definitively, that's two possible options.
**kennedybushnell** 47:57 Yeah, yeah, I haven't thought about… exposing more than, like, the arrow stuff, so it's an interesting thought. I need to think more about that.
I worry about, like, If we expose too many, like, domain-specific things.
Then that can be problematic, but allowing for plugins to hook through something more like the extension model.
Could be an interesting route to… to go. So, yeah, definitely, I… I don't have a strong opinion yet, because I haven't had a lot of time to think about it, but yeah, good, good thought.
**Laurent Querel** 48:31 Yeah, and I think, one aspect that, Aaron, you could add into this specification And, I'm sure that we will iterate on that a lot, because it's so important.
I think we should define a set of, Not only design principle, but guarantees that we… or properties that we want to, to ensure, to, that we… we can't, that we have to… to comply with. One of them is… Owned.
like OPL, I think it's fundamental that a plugin, a Western plugin, counts.
create something that is not compatible with the OpenTelemetry model.
Because if we… if we, if we don't have this property.
And that's why the Arrow kernel could not be just a basic Arrow kernel. It has to be something that… Guaranteed that whatever operation you will apply on a batch.
It's still valid at the end.
for, for the OTAP, model.
Because otherwise, you put your, your WASM playin, basically destroying the, the OTAP representation, and then the next processor in the DAG.
We'll basically not be able to, to interpret this, this batch.
So it's a fundamental guarantee that we… and we have to provide an interface that guarantees this kind of behavior.
**Aaron Marten** 50:22 Makes sense.
**Laurent Querel** 50:26 maybe a way to do it is, and we need to talk with Alberta about that.
Is to… have two layers in the OPL, library, so we have this, Declarative language layer, and we have the… The… the low-level operation.
we have this AST where we basically translate this OPL program into a collection of operations. Maybe that's the collection of operations we could expose That we could… it's similar to the Arrow kernel, but at least those low-level operation used by UPL, have this kind of guarantee. They are… they understand the semantic of a tap, And… basically, you can't misuse them at the end of the processing, it's still a valid batch. Maybe that's what we could expose if we want something lower level than just an OPL expression.
**Aaron Marten** 51:41 Okay.
Sounds good, I'll look into that.
**Laurent Querel** 51:45 Okay, yeah, and and regarding the… The receiver and exporter, it's, I don't know, did you think about, what that means to build, a WASM plugin for… For a receiver or for an exporter.
The interaction with the network, or with the interaction with… or you put some… Oh, that's what the us service and the YZ, HTTP… Okay.
**Aaron Marten** 52:21 Yeah, yeah, so WASI provides some of that functionality, provides, you know, an HTTP client.
And some ability to… to interact with Sockets, but, there likely are gonna be.
**Laurent Querel** 52:34 Awesome, that's…
**Aaron Marten** 52:36 I imagine we're going to hit, certain cases where we're going to want the hosts to kind of handle that and provide it as just, you know, services to the Through the plugin APIs.
Certain, like, low-level things with sockets that you just can't do with WASI, but would make sense to want to do from a plugin, for example.
**Laurent Querel** 52:55 Some of you.
Yup.
Another, question where I'm not fully clear, a topic where I'm not fully clear is the… the, async, model of this, WASM plugin, how… how is it compatible with a single threaded approach that we have?
is the await cones that are part of the WASM program.
Will, will be, we'll give back control to the… to the… Local runtime that we are using.
So, yeah, that's the type of question that, is where we need some answer now.
By any chance, did you, explore this part?
**Aaron Marten** 53:56 I have not explored async await in great detail yet. I do know that, like, the, WASI 2, which is kind of the latest one that's been implemented in Wasmtine.
does have some support for async await, but I need to explore more how that's gonna interact with, Tokyo.
**Laurent Querel** 54:19 Yeah, I think the question is, is the… the runtime that we use at the REST level.
could interact with the acid function part of your own WASM plugin, or do we have to create an independent thread?
Whiz… Communication, channel-based communication.
So we… we don't block the… Basically, the pipeline running on top of a single 3D runtime.
Yeah, this part is fundamental, and I don't have any answer.
I don't think we discussed that with the guy from Wasentine. Maybe I can ask the question also.
Okay, is there any, last-minute question? It's, 8.55.
But super interesting topic, definitively.
Thanks to Welcome Meet.
Okay, so, I think we can, get back the last, 4 minutes.
And you weigh, we will meet together, most of us, later this afternoon in the Microsoft office.
Thank you.
**kennedybushnell** 55:57 Look forward to it. Thanks all.
**Andres Borja** 55:58 Right.
**kennedybushnell** 55:59 Bye.
