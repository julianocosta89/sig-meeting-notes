SIG: Arrow SIG
Date: 2026-03-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Laurent Querel 00:01:22 Bye, guys?
Jake Dern 00:01:29 Hey, good morning.
Laurent Querel 00:01:31 Good morning, Jake.
And so, I'm updating them… Let's see…
Peace.
Can you update, the attendees' lists?
I could be past the wall from February 24th, so maybe there are people there that are…
Well, in these fields that are, in fact, not there, feel free to update it.
Mundendo.
jmacdonald 00:04:17 Hi, y'all.
Laurent Querel 00:04:19 Pero.
Jake Dern 00:04:20 Hey, Lauren.
jmacdonald 00:04:22 Let me bring up the notes.
drewrelmas 00:04:26 You're very quiet, Josh. Maybe try and put the mic…
jmacdonald 00:04:30 Oh, right. I was having microphone problems yesterday.
drewrelmas 00:04:33 You're better.
Laurent Querel 00:04:34 Yeah.
Much later.
jmacdonald 00:04:36 Well, that's just because I'm speaking loudly, it's the wrong microphone.
Hang on a sec.
Can you hear… can you hear me now?
Laurent Querel 00:04:48 Yes.
jmacdonald 00:04:49 Okay, that's better.
Maybe?
Jake Dern 00:04:52 I think it might be the same.
jmacdonald 00:04:54 No, this is the new microphone. Can you hear me?
Jake Dern 00:04:56 Yeah. Yeah, yeah.
jmacdonald 00:04:58 Okay, that's the correct microphone.
Alright, everybody.
Laurent Querel 00:05:01 I saw someone adding extension support in the wrong list, yeah. I just, okay, perfect.
Okay, so we have a lot to discuss today.
jmacdonald 00:05:23 Yeah, I would be glad to… it looks like we are, a couple of demos from you, Laurent, or discussions. Jake wants to get us to talk about his, OTAP spec. I've been reading Goten's PR, but it's a good time to talk about it.
Do you think we should go through the, kind of, issue triage that we usually do?
Laurent Querel 00:05:44 Yeah, we should, yeah, I think.
jmacdonald 00:05:47 Don't know what has happened to my…
Sometimes you press a button and things go wrong.
Okay, here we are.
No. Yes. Well, that was not the one. Alright.
Here we are.
Okay, let's do some triage, in the oldest first, I think.
So, a lot of stuff has been opened.
Going back as far as Tuesday of last week,
gosh, we could go even past the first page. But I do remember some of this stuff. So we're back far enough now.
We were… the…
And I was out of town 3 weeks ago, so that's why I'm kind of having a little trouble here.
So, we've added MMSC, min-max sum count instruments. I'm working on an exponential histogram, that's in good hands, I think.
Lallet has been proposing to move the, views into a crate of their own so that they can have zero dependencies. I think that's a good idea. I don't see anything controversial. Raise your hand if you want to, like, pin in, dig into any of these.
There was one about, a generalized macro that
Copilot opened a PR for it, it kind of… kind of didn't make sense to me, and it devolved into a… almost a joke. I'm not sure what… what was really needing to be done here, but this PR is…
didn't go very far. Lots and lots of trouble, and so I wasn't sure this was serious, or who created this.
Who assigned Copilot this, is basically what I'm saying. But it's closed, and I'm not sure what we're going to do.
CJ may have an opinion. This was… I felt like it was, re-litigating the question about whether we have variable levels or severity levels on a particular level of macro invocation.
CJ was against it for hotel spec reasons. And this looks like an effort to recreate it, so I'm not sure.
But without CJO, or… Or, Michael, I'm not sure we should do it.
But, you've heard it, at least.
There's a flaky test, I think we're working on that one.
Core nose got extracted by Drew. Is this… is this work?
Danger.
drewrelmas 00:08:19 This is a child of rearranged node folder structure. Okay. I have pushed the…
I separated this into two batches. One was the contribib nodes, which have been moved.
there's a lot more core ones, and there, you know, there's some coupling we have to figure out first, given how fast we're moving in the repo on a couple of different things. I haven't pushed this forward for the moment. I'm waiting for things to settle a little bit more. It's not hurting, but it's still something I'm planning to get to.
Laurent Querel 00:08:53 Makes sense.
jmacdonald 00:08:55 I was… I was just observing last night how we have a file… a crate named pdata with a file named otap.rs, and we have a crate named OTAP with a file named pdata.rs, and I wish we could fix that, but,
Very good, thank you. And now we're on to the first page again.
So, let's see, Albert reports that OTLP and OTAP are ignoring shutdown. Okay.
That's a good first issue, great. Are we also, yeah.
Let's see…
We have noticed that there is no enforcement for negative or infinity values, or not a number values in our histogram instrumentation.
I think the usual way to do that is to… is if you have an unsigned number, that's great, but if you have a floating point number, and you have a negative measurement, I don't know what to do, and it's… I don't want to make the data structure support negative values, and I'm not sure it's really going to happen, so that's what that's about.
Any top… any conversation, raise your hands.
Proposal to rename the OTLP exporter, totally makes sense, to me. That's because of the asymmetry and the naming in the Go Collector. So we've got exporter… OTLP exporter is gRPC, and OTLP HTP exporter is not gRPC, and that doesn't make a lot of sense.
I've seen all these, so I can talk through them quickly. The pass-through optimization Jake's talking about is to not force maximum size. It's more efficient if you don't force maximum size.
And it could be an option, or it could be a default. I'm not… I was gonna let that be Jake's decision. I've commented on the issue.
Strongly coupled batching operations. Okay, same topic, basically. Jake, I know you're here. Do you have anything you'd like to say?
Jake Dern 00:10:44 Oh, the only additional context I'll add there, is that I did actually take a swing at doing this, and I realized that some of those operations are, a little bit more tangled into,
the PDATIC rate than I thought. So, it's a little bit tricky, and I was thinking of maybe deferring this until, I realized, basically, I'd have to change a bunch of stuff to do this, and we also might have to change a bunch of stuff, for other reasons anyway, so I was just kind of holding off on this, but still want to track it as something that's probably worth doing.
jmacdonald 00:11:14 Got it.
Cool.
I'm familiar with the coupling you're referring to, it's… it's not great.
So, Parquet Exporter, we are interested in testing with cloud storage, I guess.
Naturally.
Laurent Querel 00:11:35 Don't you think, Joshua, we should,
At the minimum, I think we should change the label, deciding to accept it when we… That's right.
jmacdonald 00:11:46 Very right, very right, very right. So.
Laurent Querel 00:11:51 I can.
jmacdonald 00:11:52 Yeah, is someone you want to follow up on the ones I've just walked through, and…
We could also just bulk update them.
Laurent Querel 00:11:59 Yes.
jmacdonald 00:12:04 Can I take away labels?
Triage…
drewrelmas 00:12:09 I can do it on the side.
jmacdonald 00:12:11 Okay, let's not do what I was about to do. But thank you. Someone else can follow us.
So quasi-delta, that's a great word. I don't remember what it means in this context. Quasi-delta metadata encoding.
Jake Dern 00:12:28 Yeah, so… I think they just want to remove the name. Okay. Yeah, I have a whole bunch of these proposals. It may not be worth going through every single one of them.
jmacdonald 00:12:37 Okay.
Jake Dern 00:12:38 I did want to, as a topic, just talk about the OTAP spec, and maybe we can just.
jmacdonald 00:12:42 Okay, I see, four in a row. I will accept all of your naming questions.
This topology-aware placement abstraction came, I think, from a… in response to a Slack conversation that was about GPU isolation.
Laurent Querel 00:12:58 Yes.
jmacdonald 00:12:59 I accept.
There's a flaky test that Copilot's working on, never mind.
This is more of Jake's batch processing work.
I accept.
Jake Dern 00:13:12 Oh, that's not batch processing, that's, spec, sorry.
jmacdonald 00:13:16 Okay, okay.
Jake Dern 00:13:16 It has the word batch in it, so it's… You're gonna talk about OTEP spec, I'm excited for that.
jmacdonald 00:13:20 Okay.
Moving through them, okay, so Jake's talked about OTAP batching, increasing.
Process level metrics enabled to disable was a request from CJO, and it aligned very closely with one that I just merged last night. So we've got something we call node-level metrics now, and to get there, I added a type called metric level.
So we now have four levels for metrics. None, basic, normal, and detailed. That's maybe moving us in that direction, but being able to turn on and off metrics is essentially what we're looking for. And there's obviously more fine-grained control you might want, but this is a recourse setting.
So pipeline control message manager improvements was about, the cycle that was blocking and deadlocking the engine. I admit this was always something that made me nervous, so I'm glad to see it got
some attention.
I was, It was… so, does anyone want to talk about the outcome of this?
and the PR.
That, that led to it.
I don't see Okarsh, and I know we've all approved it, so maybe we shouldn't talk about it now, but the point is that there was some sort of memory allocation that was taken on to avoid a cycle.
Laurent Querel 00:14:46 Yes.
Introducing, some, some kind of unblocking,
Because the original problem was an inter-blocking, under… when the system is under load.
It was possible to have a situation where we… The control channel was full.
A node was trying to send this, some control message to this control channel, and still receiving also P data at the same time.
So, globally, basically,
the system was not able to process the control messages and the P data at the same time without blocking.
So we put some, some action, and I have suggested some, improvement.
And the improvements are mostly… Related to keeping, the…
The amount of memory used overall by the system always bonded.
Which was not the case in… which is not the case in the current PR, but, so I suggested some options for that.
jmacdonald 00:15:57 Okay.
skipping forward four issues, I found one that's closely related to that, which was a fix that we had for the Azure Monitor Exporter, but again, it was about how does an exporter stop reading the data channel when it needs to catch up with the control channel?
And, if you haven't seen this PR that we merged, you should. That's what I wanted to say.
Laurent Querel 00:16:22 I shouldn't slow.
jmacdonald 00:16:23 Yeah, this is important. Please, please take a close look. I'll DM you that, Laurent.
Laurent Querel 00:16:27 2188.
jmacdonald 00:16:29 2188, yeah.
Laurent Querel 00:16:31 Okay, thank you.
jmacdonald 00:16:32 Okay, so there's, there's, breaking news.
Laurent Querel 00:16:37 I just, I just have a request for the group.
for any… important PR, like this one, Could you,
Maybe copy the, announce them into the hotel dev channel.
For the big one like this one, where potentially we could have an impact, so I'm sure that I will review them.
jmacdonald 00:17:00 Yeah, I apologize, I DM'd you this, and it got lost in the message, messages, too many messages, a few times.
Laurent Querel 00:17:08 It's loose.
jmacdonald 00:17:08 We're assuming…
Laurent Querel 00:17:10 a PR,
jmacdonald 00:17:11 Yeah.
Laurent Querel 00:17:12 done that it's very hard to follow.
This…
jmacdonald 00:17:15 This one, I knew I needed to ask you about those, so thank you. And I'll follow up. So,
Something about durable buffer gauges,
this is a complete sentence, so we could just read it, but, Aaron, do you have any, is there anything we need to know about the metric instrumentation layer, or…
Aaron Marten 00:17:36 There are corner cases where this gauge can be inaccurate, and so this is a follow-up item from a PR comment to go handle that. I'm already working on a PR for this, so feel free to send it to me.
jmacdonald 00:17:50 Oops.
drewrelmas 00:17:52 Can I, say something real quick, Josh?
jmacdonald 00:17:55 Go ahead, Drew.
drewrelmas 00:17:57 For everyone in the call, I'm wondering if we could try to use the, issue type
When we create something like this, that's, like.
Not to call you out, Aaron, don't worry about this at all. I'm just saying, if we labeled this using, like, the bug type, it's clear that whoever opened it is tracking, like, an isolated issue in a specific component.
Rather than something that necessarily requires… so, not the label bug, but there's… there should be a type as well. We can get rid of the label bug.
jmacdonald 00:18:30 Okay. Type.
drewrelmas 00:18:31 Type, right there. So…
I'm just suggesting something that might help us in triage. If something is classified as a little bug, perhaps we don't need to go over it altogether.
Aaron Marten 00:18:43 Sure, yeah, happy to do that. My recollection was I may not have had permissions to set all those things.
jmacdonald 00:18:49 Hmm…
drewrelmas 00:18:49 I'll go double-check that, because I… Oh, okay.
Aaron Marten 00:18:52 Yeah, I'm not an approver or anything, so I have, like, you know, lowest level permissions.
jmacdonald 00:18:56 I want you to be an improver, Aaron.
Aaron Marten 00:18:58 We talk about that later, yeah.
jmacdonald 00:19:00 Yeah, thank you.
Tom Tan 00:19:02 And for… I have a… I have a quick, ask. And for the type, I think, for the issue type, could we create, like, issue template? Like, the user can choose, this is a bug, request, ask, then when users have the issue, you need to choose the category.
jmacdonald 00:19:19 Yeah, we're getting a blank issue, here.
Tom Tan 00:19:22 what you're suggesting, I… if you go to the collector repository, you see it. Like, there's 7 choices, and you have to… you have to declare what kind of issue you're filing. Yeah, that's right.
jmacdonald 00:19:31 I would support that.
Tom Tan 00:19:33 Yeah, I can help to create the template, yeah.
Laurent Querel 00:19:37 Good idea.
jmacdonald 00:19:38 I will not create a new issue for you about that, but you may.
Tom Tan 00:19:43 Okay.
jmacdonald 00:19:44 Sweet.
And then I think CJO's got a fix for this one about the batch processor, returning an error instead of a NAC.
It's in progress.
More flaky tests. Man, we have too many flaky tests, but I'm not gonna open it. More about Jake's topic. Let's just let Jake speak to us. Here we are, we've done.
Jake Dern 00:20:06 Yeah, these top two are kind of important, actually. Sorry, these are not related.
jmacdonald 00:20:11 Oh.
Jake Dern 00:20:11 fuck, yeah.
jmacdonald 00:20:12 Okay. Yeah, so I would be surprised if you haven't been hitting these on the Microsoft side, especially if you're taking the batch processor for a spin, but… We have, actually. I think I've seen this one.
Jake Dern 00:20:20 Okay, gotcha. Yeah, so basically we can end up picking a UA dictionary size for columns, like an attribute 16-like str column, but technically U16 is allowed by the spec, and certain parts of the code will return an error for that. So if you have a batch processor upstream of something that, like, does transport-optimized encoding, for example, it can fail.
And then, that takes me to my next, issue that's right above this one, which is that there's a lot of suppressed errors, in the OTAP exporter. So, if you hit that error in particular, you will not see anything. The only thing you can observe is metrics, where… and there's not even metrics where it says it fails to send, it just doesn't say anything, so…
jmacdonald 00:20:59 Yeah.
Very good, thank you for the warning.
This was also your… you sent some,
Places where we weren't awaiting a future inside of a macro that the linters weren't finding.
Jake Dern 00:21:14 Yes, I did, and I don't know that that fixes the metrics reporting in this case. I'd have to go back and double-check, but yeah, there was no, like, metric export failure, I think maybe because we were also just ignoring some of the returns.
jmacdonald 00:21:27 That's a little bit scary to me, and I don't know what is the appropriate response.
Because I'm used to the compiler telling me that I've done something wrong like that. That's, like, a huge mistake.
Jake Dern 00:21:40 Yeah, and I tried to turn on the… I was surprised it didn't either, and I tried to turn on, like, explicitly those warnings, and then that's when I discovered that if it's in the macro, it just doesn't show, which is too bad.
jmacdonald 00:21:51 Yeah.
This one right here. So.
I… I would never have expected that this could happen, but it did.
And because we weren't awaiting these futures, we were just ignoring whatever response was coming in.
Laurent Querel 00:22:06 Because there is the underscore I call also, no? That's…
jmacdonald 00:22:11 Because we're underscore… because we started to underscore…
Laurent Querel 00:22:13 Yeah, so…
Jake Dern 00:22:14 It was a…
Laurent Querel 00:22:15 Put explicitly, so…
Jake Dern 00:22:16 Yeah, hold on, wait, wait, wait, but that's not actually the problem. So if you underscore assign a future and don't await it, that is a lint that you will get, still. If you underscore.
Laurent Querel 00:22:26 Of course.
Jake Dern 00:22:26 assign a result. That, like, isn't… and, like, you won't get an error for that, because you're explicitly underscore assigning it. So the problem here is that, like, specifically, we didn't await the future, and that lint doesn't work inside a macro.
So the field, like, the sun's.
Laurent Querel 00:22:39 Inside the micro, okay.
jmacdonald 00:22:40 Yeah.
Sharp edges.
Laurent Querel 00:22:44 Why are you saying that we are inside a Mac model?
Jake Dern 00:22:49 Oh, if you expand the AR. Yeah, it's gotta be a select statement.
Yeah, it's one of the…
Laurent Querel 00:22:55 Oh…
Jake Dern 00:22:56 stream.
Laurent Querel 00:22:57 Okay, okay, okay.
jmacdonald 00:22:57 There it is.
Jake Dern 00:22:59 Yeah, so they don't actually let you underscore assign a feature by default.
Laurent Querel 00:23:05 Okay.
jmacdonald 00:23:07 All right, very good. That's, a good warning, and I'd like to know if there's something better, but, you know, that's…
Laurent Querel 00:23:15 There are ways to remove, basically, this micro.
Maybe that… that could be an option.
I understand.
jmacdonald 00:23:25 Well, we've now stepped through all the new issues. Thank you if you are someone who is following up with labeling work on them.
And, laurent, I think you have at least one demo, if not two.
Laurent Querel 00:23:38 Yes.
Yeah, that's… I think that will be one combined into… Thank you. Or two combined in one, so…
jmacdonald 00:23:44 a little bit of this, so I'm gonna say it's exciting. Let's… I'm gonna unshare so you can take over.
Laurent Querel 00:23:49 Okay.
Great, thank you.
So I will start with, before to go in the demo, I will start just
To remind people what we are trying to do with the topic, implementation.
Why it's not working.
Okay, anyway, I will, just… can you see the… This, this image.
jmacdonald 00:24:22 I can.
Laurent Querel 00:24:23 Thank you.
So, until now, we… we can basically, with the engine, we can group
We can basically organize and run multiple pipelines at the same time.
With this, logic of pipeline groups.
And, so we have multiple groups, multiple pipelines per group.
This idea of topic is a mechanism, a generic mechanism that will help us to
Connect, independent pipelines together through this, topic mechanism.
The first implementation will be purely in memory.
And by topic, I mean something relatively close to, to a Kafka topic.
So you publish to a topic, so Pipeline will have a new
Exporter type. It will be basically exporter column topic.
You can target a topic by your name.
And a topic has to be declared.
And, and you publish, PDATA messages on it. But you don't know how many and how the other pipelines, the consumer pipeline, are consuming this specific topic. So here, I put some, common, use cases of this topic approach.
For example, the first one, that I named De Copper Ingrace, is… is basically…
a way to load balance, to better load balance, if we are in a situation where
we observed that we don't have so many, TCP connections or gRPC connections.
Or, we are on a system, which does not support properly the SOU support, typically, macOS.
Then you can split your pipeline in two parts, ingress and the processing and export, and then, that will fix the problem, the load balancing problem. So that's the first
basic usage.
Another interesting aspect of that will be if you, if you have to…
Reconfigure the processing export, because that's where you have most of the processing and the configuration.
Decoupling the ingress from the processing and export, and once we support the library configuration, we give you a way to
Live reconfigure that without, closing the existing connection.
Because during this live reconfiguration, the topic will accumulate the incoming messages, and this ingress pipeline will stay in touch.
We will, integrate what I named the pneuma-aware co-location, so that that's a future version of the controller.
By analyzing the topology,
between the pipelines, so those pipelines are connected through topics, sometimes, and… and we can try to optimize their placement.
Based on their connection to topics. And obviously, it's better to have two pipelines.
Running on cores, the two pipelines that are interconnected together, running on cores.
located in the same method. That's basically what is summarized there.
This other,
scenario is the one, I think, you want to leverage inside Microsoft. We also have the same type of scenario for Wi-Fi.
So in that case, we, again, we decouple the ingress pipeline, we have a router, a content putter.
that will, extract whatever attribute or headers. Right now, we support extraction of attributes, resource attributes in that case.
And, and we, we, we declare, as many as topics that… corresponding to the number of tenants that we want to support.
So you declare tenant A, B, C, and so on. And, and you, basically route, based on the… some service attribute, sorry, some resource attribute, batches that will go to a specific, topic. And then, behind this,
tenant-oriented topics. You, you have, corresponding pipeline configuration.
That could be the… always the same, or that could be different if you… if you want, and the number of CPU cores allocated for
each of those pipelines could be different. So, you could imagine that you have
Small tenant and big tenant, and they don't have necessarily the same number of cork.
So that gives us a lot of flexibility, and that also gives us isolation, resource consumption, the budget, resource budget, and, and also monitoring that are pertinent.
And finally, again, this list is…
Apart from complete, but another example…
Something that I didn't mention, I mean, I mention it because it's close to Kafka Topic. So, Kafka Topic has this concept of consumable.
Which is optional.
So when you specify it, you say, oh, I want to subscribe to this topic, Consumer Group A.
or Consumer Group B. Every, Consumers, or subscriber, Using the same consumer group.
We'll receive the message from the topic in a load-balanced manner.
If you subscribe to a different consumer group.
you will receive a copy of those messages. And again, if you have multiple consumers in a different consumer group, they will also be served in a load balanced manner.
That is supported by this PR. And, if you don't specify, a consumer group.
Then, we… we have a broadcast approach with, a policy that specifies what happens if there is
A consumer of this ring, when I say ring, it's the underlying mechanism used to broadcast.
What happens if there is one of those consumers that is lagging?
And, because the idea is to,
not, let's say, defining the speed of this ring based on the slowest consumer. The idea is to have a policy that helps us to define what to do when someone is lagging.
And we can, with this approach, for example, decide that a consumer will receive,
We'll drop the oldest message because it is too slow, it is too slow, and then we'll receive,
How many messages, the consumer, basically a representation of this lag.
So, a scenario, that is meaningful in using those concepts, you can imagine that you have, again, an ingress pipeline, a primary observability pipeline where you don't want to lose anything.
And then you have, as many as…
Pipelines you want that will consume this broadcast ring channel.
And, if they lag, it's not a big deal. That will not impact the primary observability pipeline. So that gives you
an overview, of what this PR is doing.
Obviously, we want to extend that with persistent topics, especially the Quiver integration.
That will come later, and need to discuss that with, with Aaron.
And in terms of RACNAC,
It's still a part where I need to work a bit. It's already in place, but I'm not fully confident, so I'm still working on that. So when we are talking about ephemeral topics, so the in-memory version.
The ACNAC will… will… you can enable it on the publisher side.
And it will be an end-to-end ACNAC across pipelines.
So, I think that is really nice. It's…
I think working, more or less, and just need to test that a little bit more.
And when we have a persistent topic, the spam, basically, of this ACNAC will be reduced, because we consider that the messages are now persistent, so we can act
much earlier. So the benefits of having a persistent topic will be basically to reduce the latency to return the AC or NAC to the producer of those messages.
But at the same time, you add latency for the processing itself.
But, so it's a trade-off.
Okay, so now, Demo. So, the demo is using…
Some of you already saw this, this UI.
And I saw recently a conversation, especially from CGO, some attempt to create a web UI.
In fact, we have already a web UI that we implemented inside A5, and I was questioning myself, do we want to contribute this UI? And I think we will. So, I'm showing you this UI now, and I will run
So… Give me a few seconds to, start
So, I have a server on a different,
An engine running on a different machine.
Okay… Why it's not working…
We're tipping.
jmacdonald 00:34:59 Live demo situations.
Laurent Querel 00:35:01 Yeah, I didn't check this before. What is this problem?
jmacdonald 00:35:14 I'm waiting for some SVG to show.
Laurent Querel 00:35:15 Oh, okay.
jmacdonald 00:35:16 There it is.
Laurent Querel 00:35:16 Okay.
Okay, so, this UI is consuming the primitives endpoint that we already have.
And, and we can basically navigate across the pipeline. The pipeline group dimension is not yet integrated into this UI.
But, so let's start with,
I need to show you what we…
what we see here. So,
Let me go to the files…
And, we… currently, I'm running this, this scenario, or this, configuration.
So this configuration…
is equivalent to the continuous benchmark, except that, so, for people that don't know, the continuous benchmark,
we have a Python program orchestrating the…
multiple engines, one engine to generate traffic, one engine that we name System Under Test.
which is basically a few pipelines, or one pipeline, receiving the traffic generated by the first engine. And we have another, a third engine that is simulating a backend, and basically measuring the overall performance in terms of
Message throughput and this kind of thing.
This, configuration is mimicking that, except that, the communication between the traffic generator,
pipeline, the system under test pipeline, is using, topics.
So… If you look at the configuration, you will see that we have a group
continuous benchmark topics. I'm declaring,
two topics in this case. What I, the ingress topic, which is between the traffic gen and the system under test pipeline.
And… and we have, a backend log, topic, which is between the system under test pipeline and the simulated backend.
And then we have the definition of the pipelines. So, if I'm going back here.
What we see, the two traffic gen pipelines.
Sending, so that this thing is misnamed, and we… to change, basically, the…
the configuration, but here we have the name of the node, so if the name of the node was TrafficGen, we will see TrafficGen here.
You know, we have the… if we look at the configuration, traffic gen… yeah, TrafficGen.
it's an exporter topic, targeting the ingress topic.
And this one, the first one was… this receiver was a receiver traffic generator. So, ideally, I should rename that to me… to make the demo a little bit better, I forget.
So, when we run that, we can,
we know on how many calls this, pipeline is running. Right now, we are looking into this call, the core two, but we can have a view that, show us overall, so combining all the
pipeline instances for this configuration. And right now, this traffic gen pipeline is generating 9 million signals per second.
If we go to the Pacific Gen 2,
Which is slightly different, but it's more or less the same thing.
So 9 million also.
Now, I can move to the system under test pipeline, and this one is… Running only on 2-core.
Receiving the traffic Generated by the traffic gen pipelines.
Here, we have a receiver topic.
then we split the traffic per type, because I'm generating only logs, that's why we see,
Only the… this link that is green.
Green represents activity, so in the configuration, we have this metric and traces, but both links are not used, there is no signal traversing it.
And, and then we have a retry, and then we have, again, an exporter topic.
And finally, there is the backend, and the backend is…
receiving this traffic that has been routed. So, it's a very basic scenario, not super useful, but just to demonstrate,
The ability to communicate across topic, across pipeline, via topic, sorry.
And, also showing How far we can go, in terms of performance.
With this approach.
So now, I will, run…
So, I will run a different scenario
One single.
Oh.
Yeah, maybe this one will be interesting.
So the, the, this UI is, in fact, a single HTML file.
So, could be served by, exactly like CJ started to do recently, I think yesterday.
And, and instead of developing, this kind of UI,
And, and duplicating effort, proposing to basically,
donate this UI to the project, following exactly the path that CJO is doing, except that we… we implemented this UI, you know, for some time, so obviously we… it's a little bit more advanced.
But,
But does not integrate yet the engine, matrix-level matrix… sorry, the engine level matrix that have been, created recently.
So that should be done, not necessarily by me, but,
I think once we have that, we will be a superset of what, is currently under review.
So, in this, example, I'm mimicking, basically…
What was, described, here.
this configuration.
And, in this configuration, we, again, we have, In that case, I'm…
We have 3, traffic jams.
I'm using an attribute processor to add, specifically, a resource attribute, tenant A, for this traffic gen, and sending to a topic, which is common across
across all the traffic gen pipelines. You have a question, Joshua?
jmacdonald 00:43:02 Yeah, I, I just wanted to remind us about time, mostly because I know there are two important topics left, and…
Laurent Querel 00:43:09 Yes, sir.
jmacdonald 00:43:09 Demo is great, basically.
Laurent Querel 00:43:13 Okay, yeah, so, I think I'm done, because…
Thank you, you saw mostly the… what,
Alright, I wanted to show you guys… It's very cool. And I will let you discover what we… because it's… it's much more complete in terms of interface, that's what I demonstrated. Okay, I'm done.
jmacdonald 00:43:33 Very good. I will mention this to CJ, since he's the one who opened a PR, and yours is much, much more developed at this point, so I think we'll be able to figure out how to take that forward.
Laurent Querel 00:43:48 Yup.
jmacdonald 00:43:49 The two more, items, I've been taking notes, the two more items on the agenda are from Jake, and then one about extensions from Goken. Jake, would you please, start us off?
Jake Dern 00:44:00 Yeah, I'll be pretty quick. So basically, as you saw, I opened a whole bunch of proposals, for the spec. Some are small, some are, a little bit less small.
I'm opening these proposals partially because I think we should do some of them, partially because I think it's not obvious why we didn't do them. I'll let you try to figure out which is which.
But basically, I have,
The PR published for the first draft of the spec.
And I think what would be a good idea would be to merge that in in a draft status, assuming everything inside looks good.
And then sort of, you know, that opens up the door for, other people to kind of also work on the spec, and also for us to have kind of a nice, clean way to close the proposals, with a PR, just kind of like we do anything else.
jmacdonald 00:44:52 Okay, I, any comments?
Laurent Querel 00:44:58 No, I think it's, it's really cool to have this.
jmacdonald 00:45:02 Yeah.
Laurent Querel 00:45:03 I already read it. I probably need to read the delta between my, obviously, you and now, but it was already very good, so I'm super happy with that.
jmacdonald 00:45:14 Yeah, it looks really good.
I can say that, from my bird's eye view of the protocol, and knowing
This kind of detail has been buried in code for so long that now we're seeing it in Texas, right?
Jake Dern 00:45:29 Thank you. Exactly. It's, and I hope, folks, you know, I think I advertised this a week ago, but if you're trying to figure out information about the spec when you're implementing, it would be really, really nice if you could, instead of looking wherever you usually do, in the draft spec, and let me know if there's anything missing.
jmacdonald 00:45:45 Tell your co-pilot to read it here first.
Jake Dern 00:45:48 I actually do, and it helps a lot. Nice.
jmacdonald 00:45:51 Very good. Okay, well, I will, I know I've been ignoring this PR for at least a couple weeks, while other things bubbled up, but, it looks really important, and I will review it.
Jake Dern 00:46:03 Thank you, Jake.
jmacdonald 00:46:09 I'm glad we have time now, there's 15 minutes left. Jake, your document looks really good. So Gokan, has, a PR here, and before I, before I open the floor to Gokan, I want to say we also are aware of
two other PRs, one by Gokan, the first draft, and one by Ukarsh, who was exploring this to help us. But I think this is… our aim is to have this PR, the one that is
in front of us become the thing, at least that's what we're discussing now. Goken, I apologize, I've read part of it, and I wasn't all the way through it. I was working on it yesterday night, and I'm gonna keep working on it today.
But here we are, and I'd like to discuss it.
Gokhan Uslu 00:46:53 Okay, thank you.
So… so, the, just to recap, there was this first,
pull request that I created, which got a pushback for good reasons that I didn't fully understand back then, now I understand better, you know, live and learn, I'm learning Rust still. So, and sync is not a good thing, so we don't want to have sync. That creates a problem for me when we cannot also have NOS and no sync, because I cannot clone instances, etc, and when I want the extensions to be
some kind of a service discovery model, where there's, like, an instance that has one background, like, not background, real background in this case, but one task running, like an event loop, and then can provide instances, of, its own traits.
You know, based on what you request. But I figured then, Okay,
I cannot use either ARC or RC, because we also want send in at least shared components.
So, I just iterated over my initial design by accepting this trade-off of
if anyone remembers my initial design, I can just get into that detail, but the bottom line is that I'm just using box instances, I'm cloning them, I'm cloning the extension registry as well.
And leaving the shared state management to the extension author. And that way, you can, you know, get an instance that you own in your extension, and, sorry, in your exporter, for example. And there is a send-only trait.
And you can, you know, use it for whatever you want. One thing that I also… that I added, though, I made extensions still possible to write either local or shared.
Because it still has a start method where there's a lifecycle management there, so if there's any optimizations that you can do in that.
Background task, maybe, you have the option to do.
Based, based on whether it be local or shared.
The, and,
But, whatever you implement and use in the centrates, that would require you to be,
SAN compatible, and an example of it could be seen in Azure Identity Author Extension over there, a little above on the left side in the files, extension RS.
In that folder should show.
How it would be implemented.
jmacdonald 00:49:38 So, okay, so here's an Azure Auth Identity Extension.
It has a create function, which parses configuration, validates configuration, constructs itself, and then… And then…
And then what?
Gokhan Uslu 00:49:58 That's the mod RS, that's the… not the extension RS. Extension RS, probably you need to collect load diff on that.
Laurent Querel 00:50:08 I, I love.
Gokhan Uslu 00:50:10 toothache.
Laurent Querel 00:50:11 this.
jmacdonald 00:50:12 Yeah, this…
Gokhan Uslu 00:50:12 Let me share my screen if it's okay.
jmacdonald 00:50:16 While you do, maybe Laurent could speak.
Laurent Querel 00:50:20 Yes, so… I didn't read yet, the, this PR. I need to.
What I will suggest, and not only for Gokan, but for everyone doing such big, important PR.
We really need, A document describing the architecture.
the constraint, the trade-offs that have been put into this design. Instead of
Letting the reviewer digging into the code, very deeply in order to extract those information.
I'm trying myself to do that each time.
It's super important to do it systematically when we have such a big, big scene.
jmacdonald 00:51:12 Yeah, a lot of this, like, is in the PR description, but I kind of agree that this, this… I mean…
Laurent Querel 00:51:19 is not enough, in my opinion, in the PR description.
jmacdonald 00:51:22 Correct. I think, this… this could be a document in the docs folder, like a design document.
Gokhan Uslu 00:51:28 We added it to all of your surprise, missing the PR.
Laurent Querel 00:51:33 Okay, okay.
Gokhan Uslu 00:51:33 But I don't know if there's enough details there, and I used a little bit of AI generation to help with that, because a long document. I reviewed it, it's a bit interesting.
jmacdonald 00:51:43 And I was reading this yesterday night. This is where I left off, so I was reading through this document,
Okay.
Gokhan Uslu 00:51:51 I cannot share my screen, it requires me to restart my client, but if you can open the expansion RS file in that PR, there's an example of how it is implemented and how self-registration is done.
jmacdonald 00:52:05 For the record, this is the, the design document. Here we have it. And I,
I agree with Laurent. I will add that this is, like, the third or fourth draft, and we've been working on this for a while, so we could go back through the old proposals as well. But this… I think this is the right level of detail, although I haven't read it yet.
But you were saying you wanted to show us an example.
Gokhan Uslu 00:52:32 Yeah, in Extension RS,
Yeah, yeah, there. So, there you would be seeing, like, how the self-registration is done, and how the trade implementation is done. Okay. If you look at an implement.
jmacdonald 00:52:48 The implementation block, somewhere.
Gokhan Uslu 00:52:51 Yeah, there. Yeah, it implements bearer token provider.
So you implement whatever it does, you know, just some simple method there, and then you, write implement extension for, extension for Azure Ident extension below, and you need… you can use this line macro to self-register whatever,
at the top of that block. Whatever, trades that it registers.
jmacdonald 00:53:22 Which is the macro?
Gokhan Uslu 00:53:23 Yeah, it's the setup of that implement block for, yeah, the…
jmacdonald 00:53:26 Oh, here it is. Okay, great.
Gokhan Uslu 00:53:28 So, I, yeah, I, I chose this, self-register.
Method as part of the extension trade, and it generates the method for, which… the trades that it needs to register.
Because it seemed to enable simply about what I'm trying to do with these box instances, basically. Yeah.
jmacdonald 00:53:57 I believe a macro is going to be required, so that doesn't bother me.
Gokhan Uslu 00:54:04 And the other option which this gives is,
How, like, you don't have to implement any?
traits at all. It can be a background extension, then at that point, it gives you
Full flexibility of, you know, you can use, no sand, no whatever, or, you know, just, it's completely up to you, don't… you're not bound by the…
jmacdonald 00:54:30 here's the wrapper. We've done… we've followed the pattern in the engine codebase. You have a wrapper that does shared and local. I'm trying to find the macro definition.
Gokhan Uslu 00:54:39 Yeah, it's probably in the registry, if I remember correctly. It's in the extension for… if you go up, in the extension folder.
jmacdonald 00:54:47 Oh, there.
And then… .
Gokhan Uslu 00:54:52 Look for macro rules.
Laurent Querel 00:54:54 Okay, I will do my best, so…
Here at F5, we… today and tomorrow, we are in Wellness Day, but anyway, I tend to…
So, my opinion… So, I will look at this PR, and.
jmacdonald 00:55:10 I want you to take a wellness day. I don't think this is our, so urgent that it can't… that we can't spend 4 or 5 days reviewing this, and… and I'm gonna be out of town until… through Tuesday, so…
I… unless… unless everyone in this room speaks up right now, I don't think we expect this type of work to merge in a hurry, and we've got time to review it. And I hope that I'm not upsetting anybody yet.
Gokhan Uslu 00:55:34 No hurry. By the way, I wanted to also highlight, over my initial design, Utkarsh had his own take, and what I did was I incorporated some of Utkarsh's code here in my pull request, which is to…
make the extension, the channels, etc, like, P data free, basically, that's the part of it that I incorporated there. So thanks, Utkarsh, on that as well. But I wanted to do this because, in Utkarsh implementation, it seemed like there was two different instances, you know, there's a handle and there's an extension.
That seemed a little bit complicated for extension implementers, and there was also some matrix used that I wanted to avoid there.
But in general, I just want to say, if the trades need to support sync, or trade needs to have no sync, no sand, etc, all of these are possible here. That just increases…
the variety and the complexity here in this system that I wrote. And, just having sand-only trades, if possible, in general. I think that's what I also want to look into, like, is this…
an acceptable, thing moving forward, because if you would say that I want sync and no sync, no send versions of these trades, the same trade, etc, then it's going to create lots of.
Laurent Querel 00:56:52 complexity for the, again, extension implementers. Now, what I… I think what I will do, is just reading this extension system in the.
Gokhan Uslu 00:57:03 Nothing else.
Laurent Querel 00:57:04 And all the questions I will have, I will add, maybe, or maybe not, some comment on this document. My intent is to reach
a version of this document where all my questions are answered, in terms of architecture and guarantees and design. That will be my only focus to begin with. And then, next week, focusing more on the topic. Oh, sorry.
My brain is mixing multiple things.
jmacdonald 00:57:38 That's.
Laurent Querel 00:57:38 Focusing on the code, next week.
jmacdonald 00:57:42 Yeah, okay, I'll, give me a day to re-review so that if, you know, that's… I can polish this document a little bit. I like, I like… here's my proposal. Laurent, you have wellness days, I really want you to take them. I'm also leaving town. Goken, if you would, I think the right thing to do here is to
Either reopen a new PR with just the document.
Actually, that's what we should do. I think we should do. Your PR… I mean, the code, it's too much to review. The document first is what we'll do, and I will also review your document today, and I will be aware that you are still working on it, so don't worry about that. I will review it before I leave today.
Gokhan Uslu 00:58:22 Okay.
Laurent Querel 00:58:23 Yeah. By the way, regarding Doc. Nothing to change for now, but we have a mix of location for documentation that we need to fix at some point. We have Doc in the
the shared directory between Go and REST, which is.
jmacdonald 00:58:44 Yep.
Laurent Querel 00:58:45 the location where Go can put the extension system, and we have a lot of doc into the, the pure Rust or Tap Engine, directory.
Anyway, we have a lot of work to do to…
update this entire repo for future users. That was not the focus until now, but that will be definitively something probably by end of March or beginning of April.
jmacdonald 00:59:13 Yeah, I also have dedicated some time after I get back to documenting and websiting this project.
Very good. Thank you, Goken. I know this is hard. I know Rust is hard, and you're doing great. And thank you, Akarsh, for helping, as well, if you're here on the call.
Gokhan Uslu 00:59:34 Yeah, he was very helpful.
jmacdonald 00:59:35 Yeah, I agree. So I can't… I'm so disoriented when I'm sharing, I can't see anybody. Hi, everybody. We reached the end, and, it was a good one. Thank you, all for speaking.
I think we're done. Thank you. I'm gonna be back, but I won't make the Tuesday meeting next week. I'll be in a car or something like that, so enjoy yourselves next time. I'll be on Slack.
Laurent Querel 00:59:58 Okay, thank you.
jmacdonald 01:00:00 Thanks, all. Bye.
Laurent Querel 01:00:01 Bye.
Gokhan Uslu 01:00:01 Bye.
