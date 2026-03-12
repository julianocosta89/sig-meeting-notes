SIG: Arrow SIG
Date: 2026-02-24
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/4iUOs7jTW7zCEiSzffbH5eP3xV94tOtKsUSY1soHO1FBTSuGHztj_sbPCWlSWhIi.i3H1aQ29dQR_L64C
============================================================

## Zoom Recording Transcript

Albert Lockett 00:00:57 Hey, Kirsh.
Utkarsh 00:01:02 Hey, hi, Albert.
Albert Lockett 00:01:04 How's it going?
Utkarsh 00:01:05 Good.
Alright.
Albert Lockett 00:01:08 Yeah, pretty good.
Hey, Jake.
Jake Dern 00:01:16 Hey, how's it going?
Albert Lockett 00:01:19 Pretty good.
Laurent Querel 00:02:00 Hi, everyone.
Albert Lockett 00:02:03 Yes.
Laurent Querel 00:02:11 Hello!
jmacdonald 00:02:16 I will share our notes document.
Well, here we are again.
I'm back from a week of vacation and feeling still quite relaxed, so we can look at the issues, I suppose.
And then anyone on the call is free to put in an agenda item.
Albert has one.
Encouraging everyone who has a topic on their mind to write something down, Maybe I have something… let me think for a sec.
Alright.
Okay, for the kind of usual practice of issue triage, since I wasn't here last week, I'm just gonna, suggest that we go through the last week, or at least since last Thursday.
Of issues here.
And, if anything stands out, let's talk about it.
I can see, sort of a series of issues from Albert, looks like, on the columnar query engine. Anything worth saying?
Albert Lockett 00:05:18 No, I don't… I don't think we need to, like, spend too much time going too deeply into it. Basically, like, the goals for me for, like, the next… like, this week, and probably, like, the next 2 or 3 weeks is just gonna be, trying to get, like, expression evaluation working, and then, based off that, be able to implement, like, better ability to do assignment of fields, like assign, attributes, and assign, field values, and then integrate that into the filtering code, so, you know, don't want to spend too much time on it, but that's basically what those issues are that have that… that green called Requery Engine, label.
jmacdonald 00:05:56 Great.
Let's see, we have some triage deciding here on, one about this NMSC and histogram. I know the topic, but I wonder, Ukarsh, since you're here, if you… if there's anything that needs to be discussed.
Utkarsh 00:06:14 No, not really, I just… Firstly, we don't have full histogram support, so I thought I'll just create one issue for both MMSC and the full histogram.
Yep, that's nothing to discuss yet.
jmacdonald 00:06:28 Great. For the record, I am planning to work on an exponential histogram for Rust and for OpenTelemetry.
That I've been wanting to do for a while. So, I'll take… I'll take steps, for myself.
There's this one, well, let's see. Wow, it's out today, so I think we can… cover this one, metrics views for OTAP metrics and… sorry, views for OTAP metrics and OTAP traces. That's, a matter of… Having more efficient code paths in certain places.
And I think we know what needs to be done. This one here, generalized log macro, has led to a kind of interesting, and I'm not sure what to say, PR with Copilot taking the lead.
I'm In fact, without either CJO or, Blanche here, I'm not sure… what to think about this wild PR. Some of you have commented on it, It's nice to see that these agents are so capable. I'm not sure what to think yet.
I can ask CJ what he thinks. I have a one-on-one with him soon.
And Aaron offered some help. Aaron, do you have an opinion here?
Aaron Marten 00:08:02 I don't, I honestly have not taken a close look at this PR, I was just helping out with the…
jmacdonald 00:08:07 Emergencies.
Yeah, okay, no worries. I… I don't have any problems with letting Copilot do work, but I will have a high-quality bar for it if we do, and I'm not too familiar with this topic, but I know it's about something that CJO cares about involving whether log events can have variable severity or not, and whether the mapping between name and severity is distinct, and I don't want to talk about it here.
I hope that's fair.
And… Let's see, what else needs triaging? I mean, in theory, I should… we should make a issue that says what we decided, but we don't have to decide on that one. There's a flaky test, Drew is working on moving some nodes into different subfolders, that looks great to me. I'm trying to get us through this as quickly as we can. Albert has, Noted a shutdown deadline issue, good first issue, love those.
I said something about negative value histograms to help, Ukarsh, merge a PR.
My position from OpenTelemetry's perspective is you should not use and not a number. Like, don't… don't use NAND values in instrumentation, don't use INF values.
I'm subject to… I can be convinced. In fact, that would be a spec-level conversation, and we could have that.
And then Aaron is working on, metrics, as is Gokan, I understand, for each component we're working on.
Anything to discuss?
Alright.
Well, I would propose then to move on to the agenda items, starting with Albert.
Albert Lockett 00:10:12 Yeah, hi everyone. So, this is, hopefully a pretty quick discussion. Basically, we now have the OTLP HTTP exporter.
Which is in contrast to the current OTLP exporter. And the current OTLP exporter, exports OTLP over gRPC, and what the… what I'd like to propose to the group, for… feedback, if anyone thinks that this is a good idea or a bad idea, would be that we rename the current OTLP exporter OTLP GRPC exporter to, kind of make the distinction between the two.
Just by… by way of… evidence that… that maybe this is something worth doing. The… in the Go, collector, I think the OTLP gRPC exporter, when you give it, like, the exporter name when you're setting up your exporters, you do type OTLP underscore, GRPC, so… Not only does this help distinguish between the two components, but it also gives us, better, I guess, I don't want to say compatibility, but, the…
Laurent Querel 00:11:27 accumulated.
Albert Lockett 00:11:28 the Golang analog is, is… we're more aligned with that, if that makes sense. So, anyway, I'll open it up for discussion. Does anyone, feel strongly that we shouldn't do this, or does anyone agree that we should do it?
I see Josh nodding yes.
Andres, hand up.
Yeah, sleep.
Andres Borja 00:11:53 I… I'm not… I don't remember exactly how it's in the… in the co-collector, but is it not a single component with just a… parameter, if it's gRPC or HTTP, that's what I remember, no?
jmacdonald 00:12:07 the receiver is that way, as far as I know, and the exporter is not. And it's sort of a weird asymmetry. There was some discussion about this in the Slack as well.
Andres Borja 00:12:21 Okay.
jmacdonald 00:12:22 I… I like this idea, honestly.
it's just more clear, and I think it's confusing to users that OTLP means OTLP GRPC if you are the exporter, but it means OTLP or gRPC or HTTP if you're a receiver.
That's kind of confusing.
Albert Lockett 00:12:45 Okay.
Laurent Querel 00:12:46 But, so I'm not sure to… so in that case, I understand what you are saying, Josh, but… What is the conclusion?
Because, right now… We have a receiver, with this, intermediary protocol in the configuration, and then two branches.
gRPC and HTTP.
And I think what was, proposing, Albert, is an exporter where we have to distinguish exporter, which follows exactly the pattern followed by the GoCollector, both sides.
Which is fine for me.
Even if it's indeed not symmetric. We could discuss…
jmacdonald 00:13:36 It's just about the naming, whether there's a… this is really just about naming. There's a suffix underscore gRPC, that's clear about what it… and Albert, just to be clear, you are referring, I think, to the declarative configuration spec for an OTL SDK, which has OTLP underscore HTTP, or OTLP underscore gRPC, for configuring the SDK.
Whereas, I believe the OTLP exporter means OTLP GRPC implicitly in the… in the collector, and there's no… there's no OTLP underscore GRPC.
Albert Lockett 00:14:13 Oh, you're… according to the docs, it looks like it takes it both ways, weirdly.
jmacdonald 00:14:17 Probably.
Maybe there's an alias thing that I didn't realize. Maybe this is because they know the same computer.
Albert Lockett 00:14:26 Okay, yeah, I guess maybe they have an alias or something, so… Yeah, so this is really just about, like, naming of our OTLP gRPC exporter component, and my proposal is that we add the underscore gRPC suffix.
jmacdonald 00:14:45 Yep.
Albert Lockett 00:14:47 Okay, cool.
I'm gonna do it. Give it a thumbs up.
Thank you. Okay, I'll yield the floor.
jmacdonald 00:14:56 Alright, well, it's about topics, and Laurent.
Laurent Querel 00:15:00 Okay, so, I'd like just to make sure that I'm going in the right direction to support, the scenarios that matter for Microsoft, and we also have similar… we have… not necessarily purely similar scenarios for F5, but we have a need, definitely, for topics.
So… in order to avoid gigantic PR, like I'm used to do quite often, I tried to split things for this specific case. So, last week.
We had, a PR focusing on, topic configuration.
That has been merged.
And now I'm focusing on implementing a topic broker.
With, one backend that will be implemented, the in-memory backend, but I'm trying to make sure that this topic broker could be extended.
to, to plug Quiver, or to plug a Kafka topic mechanism, or something like that.
So this Round 2 will be focused On… the… the… let's say, the channel implementation by itself. It will not be integrated into the engine, and not connected or wired with the configuration yet.
It will be more, like, A dedicated component, that we can test individually.
Supporting a topic semantic.
Where you can… you can basically declare a topic by name with a set of policies.
Then we can get an access to a topical. This topical on the… on the exporter side, so there is also the concept of a topic exporter, so the topic exporter will take this topic handle, and will be able to publish on this topic.
NEP data message.
And on the consumer side, so the receiver side.
A topic receiver will be able to subscribe, To a name topic.
And the subscription will also contain a policy, which will define if the subscription is based on a consumer group, like in Kafka, so if you reuse the same consumer group.
across multiple instances of this receiver, then you get a load balance set of message, distributed by this topic. And if you don't precise… don't define any, consumer group You get, like, a broadcast semantic, so you will receive all the messages that this topic received by publication.
So I'm… my intent is to deliver by the end of this week, this, in-memory topic implementation with a set of traits.
that I hope will be good enough to plug Quiver or to plug Kefka in the future.
And then the third round will be… About connecting the… this, topic implementation with the rest of the engine. So, it means that when we When we get the full description of the pipeline group and pipelines, And if we have… Topic declaration, and if you… for people that followed what happened last week, topic declaration can… Can, occur in, in various levels, the top, the global level, group level, or, yeah, global level and, and group level only.
And, With this deployment, it's entirely possible to… or this configuration, it's entirely possible to have a topic name, that will basically, shadow A topic defined globally, because it's redefined into a group.
So, this, kind of semantic already exists with the previous PR, and then I will basically instantiate, the values topic based on this configuration, and and I will also create the topic receiver, topic exporter. And then we… once we, we should be able to To create configuration, where topics are involved.
And… I think, end of the one tree that should happen next week.
We should be able to… To, to deploy the following scenario. And I think that's the scenario you have in mind, Microsoft, Microsoft side.
So we have, we could imagine that we have a group XYZ.
Inside this group, there is a pipeline… ingest pipeline.
Which will define a set of receivers, and Just taking a shortcut, those receivers will go directly to a topic exporter.
The topic exporter will be configured with… A topic name?
And then, oh, sorry, my bad. For you, it's slightly different. You will have those receivers, then you will have the content processor, where you will define various outputs.
Each output will correspond to a specific tenant ID, And the content processor will just be there to root the values batch based on some, if I remember well, resource-oriented attributes.
And then you will define into this ingest pipeline a connection between, let's say, tenant A, output tenant A of this content router to a specific topic exporter, and you will do that for every tenant that you want to support for this specific deployment.
Then we will have… A dedicated pipeline per tenant.
And each of those tenant… each of those pipelines will be connected to the corresponding tenant based on the name of the… related to the tenant ID.
That's… I think will be supported by the end of the next week. And, in this case, the subscription model that we, in my opinion, need Knowing that we can decide that we allocate one or multiple CPU cores for a tenant corresponding… for a pipeline corresponding to a tenant. What we need in that case is, a consumer group-oriented subscription. So it will be basically exercising the load balancing mechanism that the topic will support.
And then we will have multiple of those, pipeline instances deployed on different core, to manage the… The processing and the, the export of a tunnel traffic.
So first, I'd like to make sure that that's what you have in mind.
Because if it's well aligned with that, I think that will be supported by this first implementation.
jmacdonald 00:22:58 I can speak… to my understanding, that's accurate. We're describing, essentially, a system where receivers are dispatched to content routers, dispatched to many… potentially many topic exporters, which will name their tenant, essentially. The tenant will then Have a receiver from that topic, which isolates that tenant's work to a particular thread or multiple threads on multiple cores.
as configured.
Laurent Querel 00:23:29 Yeah. So, just for information, on our side, we have a slightly different, Use case, still relying on a multi-pipeline deployment and a topic in between.
So the use case is the following. We have the same kind of ingest pipeline, except that we don't use a content router.
It's mostly there to have a stable, ingestion point.
Then we have a topic.
And we have another pipeline that is there to represent what processing we need to apply to this telemetry stream.
and one or several exporters, maybe one for metric, one for logs, or whatever. And what we like to achieve is the ability to reconfigure The second pipeline, the one that… where we have Data processing and, Export in various destinations, to reconfigure it on the fly, and… With the topic mechanism, we can do that much more easily, without interruption of The, the incoming traffic.
We will be able to start a new set of instances for this new configuration.
The load balancing will be done, specifically by the topic, and the underlying MPMC channel that will be used in this specific case. And then we can measure How well this new deployment is behaving.
And Grace will shut down the previous version when it's done. So it's a controlled blue-green deployment for pipeline that will be relying on a topic, topic semantic.
what that means for us. So it's a slightly different scenario, but what I want to highlight there is… The large number of, interesting constructs that we can build on top of isolated pipelines.
Topic, semantic.
And ability to redeploy, an existing pipeline.
I think we can combine those things in many ways, and for you, it's a multi-tenancy approach.
For us, we will also do that at some point, but we can also, manage properly, pipeline updates without any loss of data.
One thing I didn't mention is how the ACNAC mechanism will behave when we, we have a topic in between.
So… I think I will be able to deliver something by the end of this week supporting AC mechanism. So the way that that will work… Right now, we… we, for people that work, in… on… at the engine level, for example, Joshua, we have a relatively efficient way to declare interest, so a node can declare an interest to a… signal.
In that case, the engine will root ACT-NAC mechanism, ACT-NAC message, directly to this component, when a downstream component, so a node after this node into the DAG, will emit a such message. So, the engine is able to analyze the DAG, and let's say you have an exporter.
generating a NAC, the engine will look at the closest node into the DAG upstream that was interested by a NAC message, and will route the message. The way that it's done.
There is, an MPSC channel, Tokyo channel, that is used.
transparently, so the… the effect on LER has this, sender part of the MPSC channel that communicates from the node to the, to the controller, or to the engine.
jmacdonald 00:28:06 The idea is to use this same, sender.
Laurent Querel 00:28:11 but across pipeline. So when, when we, basically, when we, We are in a pipeline and into the topic exporter.
And we say, oh, I'd like to… to get access to topic name A, You can specify that you are also interested by ACT NAC message.
transparently, this, the effect handler will retrieve the sender for this control message, and will, provide it for the… on the subscription side, so the subscribe… the subscription side will be able to report that a local ACNAC message into the other pipeline has to be connected to this, other pipeline with the underlying AC infrastructure. So this same… so in terms of performance.
I think it will be a relatively equivalent So two pipelines connected with the topic, I think, will be relatively equivalent to a single pipeline where everything is combined together. That's the… the… I think the benefits of this approach.
jmacdonald 00:29:34 Sounds good to me, at least I understand now, and I tried to take notes.
I was going to say something about how there's the… I'm very much liking this design. I know there's a slight difference between topics and topic delivery to the same pipeline group on the same core as to, say, a pipeline, like, across course, and I know that you're thinking about that.
Yes.
Laurent Querel 00:30:08 Yeah, indeed. So the, that's something I… part of the discussion I had last week also with Riley. We were talking together about, Future optimization we could do at the controller level.
And there are many ways to, to, to optimize the performance of this overall system.
One of them is, for example, optimizing the placement of pipeline instances.
And that could be done by analyzing the topology. So, because we have the… A configuration describing the pipeline to deploy it.
And we know that they have an explicit connection between them through the topic mechanism.
So, effectively, the controller can analyze This configuration, and determine The set of pipelines that have some interaction together.
And take that into consideration to optimize the placement based on the, the, processor architecture.
So if we have, cores that share the same memory because they are part of the same humanoid, We could imagine, in the future, a version of the controller that will place Those two different pipelines, ingest and export.
In the same manner, in order to maximize the throughput between the… through the topic, so the communication channel that is between these two pipelines could be optimized this way. So that's an example of the optimization we can do.
Because we… we… We basically reify, at the configuration level.
Enough description to let the controller understand The relationship between those systems.
And then it can take the right decision to deploy things in the right place. As opposed to a blind configuration for the controller, if we imagine that you didn't, Specify the… this topic mechanism, and you have, internal, socket communication or Unix domain communication, in fact, Unix domain socket connection, and they are not necessarily visible at the… At the, controller level, then you will not be able to achieve this kind of optimization.
Another example that we discussed was, what I name a push-done predicate.
mechanism applied to DAG?
So, for people that are familiar with, databases.
Especially in distributed systems. For example, data fusion could do that, to some extent. So, if you have nodes that are That own a specific, storage.
And they are smart enough to apply filtering locally.
Then if you have… A distributed query engine that is aware of the capability of those nodes.
The push-done predicate mechanism consists to analyze the query, extract, Filters and potentially projection.
To the various nodes, so they can be done locally, and you… and when you have to join this information all together into a central node.
you basically do less job because a lot of filtering and projection have been done locally. That could be applied, so that's a mechanism that is well known in the database ecosystem.
that could be applied, to what we do. And an example of that is syslog.
If we know that there are some, Based on some criteria, there are some CSLOP messages that we know have to be filtered.
There is no reason to… materialize them into a PDATA message.
So, We could imagine that we invent some kind of, protocol to push down predicate.
For, receivers that are predicates, push-down compatible.
And then, based on… this predicate that will be pushed down to the receiver, they will be able to apply it locally, and that could be an optimization that is done transparently for the end user. So, I'm going a little bit farther, but that's the type of thing that, at some point, I think we will do in this, Engine to optimize, even more… the entire system by analyzing the topology, defining some, Clear protocol between those nodes, in order to do this kind of optimization.
jmacdonald 00:35:48 Gotcha. Yeah, I remember there was, early on a topic, an idea of a fused pipeline, or fused processor pair, or, you know, sequence. I think you're talking about the same thing, roughly speaking. Yeah. And definitely can imagine that.
Well, very good. Currently no hands are up. I, was offering to let anyone comment on anything we've just discussed. Utkarsh.
Utkarsh 00:36:14 Yeah, for that multi-tenant scenario, I was just wondering, like, yeah, like, core placement is one thing that we would Looking at, but also, like, From resource governance standpoint, like, if there's… multiple tenants sending to the same OTLP receiver, which is listening at just one port, and then through topics, we… Distribute that data to the pertinent Pipelines, Like, how difficult would it be to, like, enforce some kind of, constraints per tenant? Like, maybe… We don't want one tenant to be… Overloading the receiver, or the… Yeah, I think, like… Do you… how would that… Could that work?
Laurent Querel 00:37:05 Yeah, that's definitively, in my opinion, something we need to support.
And we can already support some element of that today.
But far from the global vision. So what we can do, for example, in the… If we take your example, we have a single ingest pipeline, multiple pipelines doing the processing and export one pertinent. Nothing prevalent today, to have some kind of, global controller into your infrastructure, deciding that tenant A we will allocate one CPU for him, and for tenant B, we will allocate two CPU. So, you already have a way to… to express… more or less power, or more or less, CPU usage available, pertinent.
It's not… it's far from good enough, but it's already some… some option to… To assign more, more or less, power, processing power to… to… pertinent.
What we could do, then, is… Leveraging the fact that Because we are a thread per core approach, and we have one thread per pipeline instance, That's perfect to… enforce, CPU, basically to use, Linux infrastructure to specify that, oh, this thread will only be able to consume X mini CPU.
So we can, we can put in place, this kind of, control, and then we will have something much more granular in terms of, Processing power that we will be able to allocate pertinent That could be, Also very nice, and because we have the back pressure mechanism in place, it means that You can back-propagate this pressure on the initial producer of this information.
jmacdonald 00:39:32 That sounds really good. You know, I've looked at rate limiting and memory limiting in the Go collector environment, and I understand we have, sort of, course level of… levels of memory control, and you can imagine having per-tenant memory control, but once you have a per-tenant pipeline configuration, now you just set its buffer sizes to get the memory control you want per tenant. Yes. And I would much rather see a CPU limit imposed by the kernel than an arbitrary rate limit trying to kind of meet the available resource. So, this is all sounding really, really good to me, actually.
Laurent Querel 00:40:07 Yes, yes. And what… and the next stage that we could, achieve is… The combination of, this, thread per pipeline instance combined with the ability of GEMalloc To, report memory usage per thread.
Is, first a way to measure the… The memory usage pertinent in your specific scenario.
And we could imagine, it will be a little bit harder than, controlling how much CPU a specific tenant will be able to use, but we could imagine that, We, we have, this local controller inside the… Our engine, monitoring regularly the memory usage.
And, acting with the, admitter controller.
In order to… Basically, prevent that we are going over a specific threshold for the memory usage.
I don't think it's feasible, to… Restrict, per thread, the amount of memory used.
Strictly by the kernel.
Or at least I'm not aware of that.
But we can do it, I think, indirectly, because we… We put ourselves in a position where we are able to measure effectively the memory used by a thread, so by a pipeline instance and a tenant. So, we should be able to go a little bit further and, And express, as a policy, in the policy mechanism that we put in place, this hierarchical representation where There is already a resource.
Where we have the core location. We could imagine that we have resource memory usage, we set, some constraint, and for a specific pipeline, we could set, okay, the constraint is much smaller than the default one, and because we know that this pipeline is assigned to a specific tenant, then we get the… Well, basically, you like to get a control on CPU and memory resource.
Utkarsh 00:42:50 Got it, thanks.
jmacdonald 00:42:51 Alright.
Go ahead, Ukush.
Utkarsh 00:42:56 Yes, we are saying, like, yeah, makes sense. Thank you.
jmacdonald 00:43:00 Cool.
great, that was, A great run-through from top… for topics and all the stuff we're doing.
I appreciate it.
So next on the agenda, I had something here, and it doesn't have to be a… this could be, like, a take-home assignment for us. it's the thought experiment that I wrote down, actually is sort of responding to, I wasn't here last week, and I didn't go back to hear the recording either, but I know, that we've discussed Elastiflow, and I've seen a little bit about it, and I'm projecting my own impressions or thoughts here more than anything else, but for a long time, we've, I guess, flirted with the idea that the code we write as a collector can also sometimes function as an SDK. We have now, for example, instrumented our own log events through Tokyo directly into our pipeline. That's the idea of being your own SDK.
And I believe that what we're building will make a good SDK in general, and I think that's a lot of the reason why many people focus on Rust, is it's so easy to embed through FFI into so many other places. Plus its memory safety makes it so appealing, and its performance as well, so… we have an opportunity, just like many in the Rust ecosystem do, to try and I will say, make a higher performance SDK from the pieces we're building, and just keep that in mind. That's… that's kind of what I wanted to say.
I think it's a key to bringing the community together. Like, there's other… like, lots of people want an embedded Rust SDK that's high performance, that's… that's open telemetry, that's more than an SDK.
Kind of the way OTEL makes it.
That's my statement, and I want to move on…
Laurent Querel 00:44:52 Can I just say something about that? Two things, in fact. So, CJO shared on, a private channel, I think it's an event in New York, basically a company talking about creating, highly efficient open telemetry client SDK. They are basically using exactly the same approach that we do, but just focus on the client SDK and not trying to recreate a collector, as far as I can understand from the summary. So that's definitively, for me, we… Doing that, I think would be great, and some people are already thinking about it.
So we, we should do, we should do that at some point. And the third thing is, when you, when you mention FFI, And now I remember something that is, one of… a requirement, I think, that someone in your team, you… you were looking at embedding the engine into some C++ system, maybe Geneva, I don't remember exactly in the context.
I think the, And how that could interact together. I think the topic mechanism, in my opinion, will be the way to interact. We could imagine that we… We have a topic exporter, a topic named.
And, I think if you want someone in your team, create an FFI around, a topic receiver.
Then, that will be a nice way for the C++ code to basically consume what the Rust engine is producing.
jmacdonald 00:46:52 I'm already there with you, great. Yes, I thought as much, and I will relay that information.
Cool. I don't think we need to say much more about that. Yes, anything we do to integrate with other languages through FFI and threads, likely to use almost the same exact thing, if not exactly the same exact thing as topics, to communicate.
So, Jake, I know you were working on some formalization. Let's hear it.
Jake Dern 00:47:23 Yeah, I just wanted to, you know, take a quick minute and just kind of update people on the progress there, and maybe solicit a little bit, of feedback, so… Give me till the end of today, but I'm going to push a really big overhaul of the first draft of the OTAP spec, which was really more of a tool-assisted brain dump, I think, as I mentioned in the PR description.
So I got some early feedback from Laurent and Albert, and I was able to refine it quite a bit, and I'm almost done, I'm getting to the end.
There's definitely still gonna be more to do. I'm gonna flag a whole bunch of stuff. Well, I already have flagged a bunch of stuff, kind of, for discussion. I'm gonna try to tag people, that I think will be interested, but please feel free to kind of hop in on anything. And then I guess my just kind of, like, general ask is, I think there's a lot of details in the spec, it's, like, quite long.
So if there are things as you're implementing where, you know, you're wondering, hey, like, what is this behavior, or what's the allowed, you know, column encodings here, or you have some question.
It would be really great if people could kind of check the draft of the spec, see if there's something defined there, see if they agree with what's defined there, see if they found it easy to find within the spec, if it is in there, and easy to understand, and then just kind of give me any feedback as I go along and work on that, so… Yeah, that's the update, and thanks.
jmacdonald 00:48:45 Alright, that's very exciting.
just in the sense of size of maturity. Like, you can't have, formal spec without, like, make this formal OpenTelemetry protocol without a much more rigorous data model and, like.
coding specification.
Very good.
Alright, and honestly, there's something that I feel like saying, like, this looks like a Microsoft Edge browser link somehow to me, and I don't know how I know that, anyway.
Here we are.
I looked at this myself today, I've approved it, Drew asked us to take a look at it.
Drew, since you're here… I am actually here, I was able… I joined about 5 minutes ago.
drewrelmas 00:49:36 So, right on time. But in general, this was a recommendation from, Trask, the last time we added some new variations in the matrix for our CI, we actually broke everything because the required jobs name changed it.
The required job names change, excuse me. Trask recommended, following a pattern done by the OpenTelemetry Java repos, where you calculate a single aggregated status check.
Based on job outcomes, and then you just have to make that one required. So, there was an external contributor that decided to take up this issue.
And basically.
I mean, you can look into the details, but long story short, it would, in effect, keep the same outcomes we have today, meaning a lot of OTAP data flow stuff is required, it just reorders the CI. So, we don't need to go deeper than that on this call, because it's rather, you know.
a side effect, not something critical to the project, but I just… wanted, if anyone else has an opinion or a better way to do this in, GitHub workflows, please feel free to comment.
jmacdonald 00:51:04 I take it that this will let us add and remove, targets that must be required without breaking the, like, chicken and egg problem I had last time. Right.
drewrelmas 00:51:17 So, these checks, the required checks are maintained in that OpenTelemetry admin repo, which only maintainers have access to.
So, it… this just gives us a better mechanism to do it in our repo instead of in that repo as well.
jmacdonald 00:51:35 Cool, and there's an issue that I'm sure Trask has also talked about. Anyway, this looks good to me. If anyone else wants to comment, I think you should merge this, Drew, when you're ready. And Laurent?
drewrelmas 00:51:47 But Ron, head up.
Laurent Querel 00:51:49 Yeah, that's… looks very cool and nice. The only question I have is, is there… I guess it's not the case, but is there any potential impact on… The speed or the slowness of the corresponding build.
jmacdonald 00:52:04 By reorganizing the…
Laurent Querel 00:52:07 This, this way.
drewrelmas 00:52:09 I don't think so, because we already run each matrix variation independently.
So, it's just changing… essentially.
like, for example, testing coverage will still run, but the non-required version, as you see, excludes OTEP data flow on Ubuntu and Windows latest, and then there's a second test and coverage underscore required, which runs the two variations that we want to require. So.
Honestly, there's a little bit of duplication here, and I don't love that, but I don't know enough about if GitHub does YAML templating like Azure DevOps does to solve that at the moment.
jmacdonald 00:52:49 Oh, man, this is killing me.
Oh, jeez.
Laurent Querel 00:52:53 two Microsoft products that are not doing the same thing, or…
jmacdonald 00:52:57 No, just… I don't know. All these, all these SHA, like, like, total opaque identifiers worry me, but I understand this is how it's supposed to be done. I don't know. How do I know?
drewrelmas 00:53:12 That's the recommended for security.
jmacdonald 00:53:16 That's why I asked you to purge it.
That was about… Everybody. Alright.
And the last one we have, I was hoping for, if you don't mind, we have a few minutes left. Rukarsh has previewed me for this one, and here it is. Would you like to ask or say what's going on?
Utkarsh 00:53:42 Yeah, so… sorry, I should have created the issue before the Sega thing, then it would have been… Been well-timed, but, like, our current URN naming convention, like, has a namespace followed by the actual component name, and then The last thing in that convention is the type.
So… Like, are you generally conventional thing, like, with I don't know, just… maybe, like, 5 systems, or even, like, less APIs, and everything is… like, the… the more you tend towards right, from left to right, you get more specific, so… Just flipping that order, like, having the component type mentioned before the actual component name. Feels, more, like, intuitive and… And more readable, but… Also, like, yeah, I mean, I know we want to finalize on config changes soon, so… the only thing is, if we do decide to make this change, we should change it soon, but yeah, I would like to hear.
The folks want to think of this.
jmacdonald 00:54:55 I see Drew's hand is up first. There it is.
drewrelmas 00:55:00 Okay. Well, I was gonna say, I don't have a problem with this. At the end of the day, this is a simple, like, string change.
And we should align on a convention, either the current or the new one. I only wanted to note that someone else, internally within Microsoft, who actually hasn't started contributing to Hotel Arrow yet, had noted this exact thing to me. So, if you want someone to take care of it, I have someone who should make their first contribution to Hotel Aero and do it.
Utkarsh 00:55:33 I have a feeling Akarsh is responding to the same person's feedback. Yes, yeah, I think I should just tag him if he already… if he doesn't have a GitHub account, I'll check.
But yeah.
jmacdonald 00:55:45 I would just…
drewrelmas 00:55:46 Of course, let's agree on it first.
jmacdonald 00:55:48 I sort of agree with it. I'm… to be honest, and I hadn't paid attention until I, you know, when you make it such a short, like, easy-to-look-at issue like this here, it kind of does remind me that in the Go Collector, the way I… the way you re… there's two conventions, and one is the name of the component, which is a file system directory, which will be OTLP receiver.
or, you know, Prometheus receiver, or OTAP exporter. And then there's a configuration model in YAML, where you see receivers, and then colon, and you get OTLP, because they dropped that receiver from the… the name… so that you have receiver OTLP.
Which is… what you're proposing. So, there is a way that this aligns with my… with the GoCollector.
In having the name receiver first, and the type name after that.
Laurent Querel 00:56:47 And yes…
jmacdonald 00:56:48 I can imagine… Counter-arguments, too.
Laurent Querel 00:56:53 No, for me, the only counter-arguments, and I'm not strongly, attached to eat, but A few weeks ago, we did the exact same exercise.
We, we, we, we, we started from a diff… Let's say the first version of the configuration, then we enter into a process of trying to get an approval, against, among us.
to finalize, so that's why I created multiple proposals. One of them, not much longer than this one.
was targeting UN, and, and we decided… And… maybe that was not the best, option. I do agree.
But I think I'm okay to change.
what I'd like to see next time is… we need to minimize this type of back-and-forth solution, or back-and-forth decision. So, Next time, it would be nice to have more people, looking at that, and, and then we can discuss, The right solution at the right time, instead of going back and forth.
Because the impact is on your side, on my side, because I already have someone converting the existing configuration. It's not a big deal, so that's why I'm… I will definitely not be against that, and I understand the rationale.
I don't even know why I didn't end up with this solution day one. But, yeah, what I know is next time that would be nice if we can raise this kind of issue.
jmacdonald 00:58:37 Yeah. As early as possible.
Yeah.
it hurt just to even hear it, like, oh, man, I don't even want to talk about that. I imagine there was a certain sort of saturation that was happening with everybody when this was discussed. Like, I didn't see it. So I'm sympathetic to both sides.
And I think, Drew, you might be the one with the greatest impact, if it happens, so… I would be… I would approve it, but… I'm not gonna do it, and someone needs to do it quickly.
drewrelmas 00:59:12 I, I have no issue with this. This is not a big problem.
jmacdonald 00:59:15 Okay.
Alright, I don't even want to talk about it, it hurts.
We'll do better in the future, is all.
Oh, man. Alright, I'm embarrassed. I don't know how. I was just like, that's weird. Okay, we did it. Again.
Laurent Querel 00:59:35 Okay, cool.
jmacdonald 00:59:37 Naming the party.
Laurent Querel 00:59:39 So much progress in this project, that's really cool to observe, to be honest.
But to observe and participate, but that's super cool to see this dynamic that we have in this project.
And, on our side, for March, we really like to see the… Clearly, a stabilization of the main… So not only the configuration, but also the… The availability of the men.
capability of this system, so Topic is one of them. We will have, someone that will work on the… the live reconfiguration at the pipeline level, not at the node level, but pipeline level.
I think once we have those two elements, at least on our side, we will be, In a good, position.
To… on which we can rely… on which we can… deploy some element internally, and I guess you, you are looking for such… for a similar, Type of stability on your side?
jmacdonald 01:00:48 Yeah, very much so. I'm even less aware of the exact requirements than others in the room, but I know that that's very, very accurate.
Well, okay, we did it. Another hour of, community talking. Thank you very much.
Laurent Querel 01:01:08 Thank you. Night.
Albert Lockett 01:01:10 Hi, everyone.
