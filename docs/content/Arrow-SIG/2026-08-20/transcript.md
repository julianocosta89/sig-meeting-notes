SIG: Arrow SIG
Date: 2026-08-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Laurent Quérel 00:01:31 Do you want to end?
Drew Relmas 00:01:34 Hello.
Laurent Quérel 00:01:49 Okay, so…
Sophy Chen 00:01:52 So…
Laurent Quérel 00:01:55 Oh, there is an eco.
Sophy Chen 00:01:56 Sounds really cool. Can you…
Drew Relmas 00:02:01 I think.
Sophy Chen 00:02:02 I think if everyone in the chat can make sure that you…
Drew Relmas 00:02:05 your,
Sophy Chen 00:02:06 Mic is off. Mic is off.
Laurent Quérel 00:02:12 Let me, excuse me.
Sophy Chen 00:02:14 Let me,
Laurent Quérel 00:02:15 Or connect, because I saw…
Sophy Chen 00:02:17 Connect, because I have some issue.
Drew Relmas 00:02:20 Sophie, I think it…
Sophy Chen 00:02:21 Sophie, I think it might be…
Albert Lockett 00:02:23 Yes.
Drew Relmas 00:02:24 Coming from your space.
Sophy Chen 00:02:25 and from yours.
Drew Relmas 00:02:27 There we go.
Laurent Quérel 00:02:28 Okay.
Drew Relmas 00:02:28 I think part of it.
Laurent Quérel 00:02:29 Okay, great.
Thank you.
Okay, so I encourage everyone to add their name to this, attendee list.
And, and add also some, some topic in the agenda.
In the meantime, we can start to look at the… new issues.
So, this one, define consistent malfun photobuff and length for raw OTLP bytes.
So, Right now, the views, the view mechanism that we have to convert, something into, OTAP message, for example. So the same thing could be a TLP, could be, a text message, like, you know, a C-slug message.
Or different other things. And, when it's OTLP, the, specific implementation of those use, or, try, try to be, How to say that?
To ignore, basically, when there is a malformed section into the photograph.
I think it's okay, for most of the time, but, We, what I'd like to add is a strict validation mode.
So it's really an additional mod that we can put into the view, so, instead of, Returning something like an empty vector or an option, because something is not there, has been ignored.
We should have a way to return a result.
In order to optionally return, An error when there is something malformed.
No senior John there, but, That's something I think we should support.
I don't think it's controversial.
Any, feedback on that?
Albert Lockett 00:04:42 Yeah, I agree. I think the current behavior where we're just, like, ignoring, like, bad wire types and things like that was more just because when it was originally implemented, the view, traits didn't return errors for a lot of the methods where we would detect those, invalid situations.
We could probably adapt the trades to return errors, or something if we had to, but yeah, it wasn't like that we didn't want to do validation, it was more just for, like, expedience when we originally implemented that.
Laurent Quérel 00:05:13 Yeah, yeah, completely agree.
Okay, next, quiver, or do we have, arrow and Drew with us.
Drew Relmas 00:05:26 I think you have both.
Laurent Quérel 00:05:28 Bloom.
Okay.
Drew Relmas 00:05:32 Oh, yeah. Oh, I don't remember if I marked this with needs discussion or not, but, could you scroll down to the bottom? Maybe Tom did.
So, I… yeah, I discussed this with Aaron offline. I recently added the, some lost bytes accounting to Quiver, meaning When we expired… when we get rid of data, persistently stored, either due to a size cap or a time period expiration.
There's… some… additional reading of the metadata, that we can probably optimize away. Aaron, I don't think this is controversial. I think we can just mark this as accepted, right?
Aaron Marten 00:06:22 Yeah, I didn't have any additional comments on this we discussed offline. If others have comments, feel free to…
Drew Relmas 00:06:28 Oh, that's what this is. Okay, I recall now, sorry, it's early in the morning. This specific issue is related to if Quiver starts up again, with persisted data locally, like.
when it starts up, we shouldn't have to read a whole bunch of extra metadata just to determine the amount of bytes that we lost. There should be, like, a shortcut way to read this information. But anyway, we can move on. I don't think we have to talk about this.
Laurent Quérel 00:06:59 I'll get… Kafka Exporter, fixed library configuration, so I don't know… I can talk about that, but I would prefer to have Shenly, if Shen Li is with us. No, I don't think he is.
So, so… Shelly is, obstifying or consolidating the Kafka receiver exporter, in that case, the Kafka exporter.
I was not supporting properly library configuration.
So that's the, corresponding effort, describing the approach.
I will not enter into the detail.
But, so expect to see a few additional Kafka receiver exporter.
Issue, during the next two weeks, I guess, because there is a definitively a focus We had a produced focus on performance with very good results.
So the, especially on the Kafka exporter has been introduced.
a maximum flight, we basically apply the maximum flight pattern that we are already using for DAP and OTAP exporters.
And, so… It was definitively missing for the Kafka exporter.
We measure something like 1 million… message per second store into a CFCA store.
So… that's good, that's the level that we were expecting.
And, and we will continue more now on the… Debugging thing, and… and… Testing corner cases.
Eli, question or feedback on this one?
Drew Relmas 00:08:51 Is there a way we can… maybe this is part of the component inventory discussion, I don't know. How can we inventory the full list of components that technically support live reconfiguration in this way?
Laurent Quérel 00:09:06 I think it's a great, not only a great question, but I think it's something we're missing in the components inventory.
Yeah, I really like to see this kind of properties exposed By the component themselves.
For multiple reasons, for documentation, obviously, but also for… For the engine to determine what is acceptable and what is not.
So if we receive, A level configuration of, Of an entire pipeline, and we detect that there is, One component, or one or multiple components that are not compatible with that, we can just return a… an error and keep the system LC.
That's a very good idea, I think we need to add, a Gitav issue for that?
Drew Relmas 00:10:04 Okay, yeah, I'll… I'll take a note and try and write one up.
Laurent Quérel 00:10:13 Define shared voice capabilities. I think that's for Gokhan.
Gokhan Uslu 00:10:19 Yes, I, I wrote up… the issue there, but should I talk about it?
Laurent Quérel 00:10:28 Briefly, I think, yeah, if you can do that in one or two max.
Gokhan Uslu 00:10:33 Okay, so just, A quick recap of what happened. I've been trying to add the authorization, capability to OTLP receivers, but tonic requires sync and being able to call authorize, in there.
requires the capability to de-sync as well, and I was thinking about how we can get sync.
Should it be, like, a return type, or etc, but… those things seem like workarounds, and I realized that None of the shared implementations right now have, complaints about if I had the SYNC capability, so sync to the shared capabilities, and I was basically proposing, could we make shared, capability definitions sentencing instead of just send?
And the optimized path still would be the local one.
Laurent Quérel 00:11:30 Okay, okay, I think that makes sense for me.
Gokhan Uslu 00:11:37 That's, like, a very minor change, but yeah.
Laurent Quérel 00:11:40 Yeah.
Okay… Everyone is fine with that.
Okay, that's… this one is for me… Oh, yeah, okay, I remember now.
So, I think that that's, an important… I mean, it's not, It's more a potential performance issue at some points, in some… for some situations, some workload.
That I think… well, I think we could do a better job.
So, let's imagine that you have… right now, you all know that we have, A thread per core approach, and a single thread, async runtime.
So it means that this event cloop that we have, is shared… is used to basically process I.O.
Input, output, and any kind of processing we do in the middle.
This model is… is… is very nice, because we can… Avoid… synchronization mechanism, and we can also pin a thread to a core, and we can get memory, locality… Optimization.
The difficulty is to make sure that you don't have into this model a synchronous work that is taking too much, because if you have… because the asynchron time has no way to interrupt it.
It's like a collaborative effort.
So, we… we… we have to, we have to do two things. First, I think what is missing today into the, The test or validation framework that we have.
and the values benchmark system… the values benchmark system that we have. We don't really measure, If we have a such situation where we have a computation that is SYNC, It's, it's an improper word, that is not, suspendable via an async min.
And, and when this computation is too long, we should be able to detect it.
Because we know that that will impact the throughput and directiveness of the system.
Basically, the I.O. will not be able to be processed for this period of time.
Which, mechanically will, increase the buffer of the socket.
And, and… and, also we'll, basically, put… create some kind of back pressure on the, The process sending us data.
So, if we were able to split this, piece of computation in smaller parts. Not too small, but just smaller parts.
Then we will be able to process I.Os between each of those parts.
And, and we need to do that specifically in the exporter side, when we convert something, so it could be an OTLP representation, an tab batch, into something for the external world.
Depending on the size of the batch.
This conversion is, is, is not a sync right now.
I think we need to… To revisit that.
I was thinking about that when the console exporter has been recently improved.
To… to display metrics.
And, and in this specific situation, we… we display batch of metrics, and in… and some of those metrics are histogram.
They can generate a huge amount of text.
So this entire conversion of, for example, another batch to A gigantic buffer of text.
As it is implemented today is, not a sync.
So that's an example of where this kind of thing can be problematic.
Any question or feedback on that?
Joshua MacDonald (Microsoft) 00:16:15 So, I'd also noticed this with the second bullet that you explained, the OTAP to OTLP conversion happening, and blocking the main single thread runtime. And I remember at one point realizing that this could be, like.
since the gRPC exporter is shared, we can actually… we have other threads in it. Wouldn't it be better to just move that encoding translation off the main thread into the.
Laurent Quérel 00:16:40 BC.
Joshua MacDonald (Microsoft) 00:16:41 thread, but that, I guess, seems like a sort of… like a patch rather than a correct fix. Does it… it sounds like you're proposing.
Laurent Quérel 00:16:49 Yeah, yeah. We could already simulate what you are saying by having two pipelines separated by a topic, and focusing the second pipeline for the export part only.
That will do more or less what you are saying.
Joshua MacDonald (Microsoft) 00:17:05 But you're basically proposing that we begin,
Laurent Quérel 00:17:08 Yeah, I think we… async.
Joshua MacDonald (Microsoft) 00:17:09 out of our CPU-intensive work.
Laurent Quérel 00:17:12 Yeah, and be careful about it, but I think that's something we could address.
Albert Lockett 00:17:16 I think for the OTAP conversion specifically, like, we… we probably need to, like, like Laurent suggested, make it async rather than doing something fancy in the exporter, just because we convert to OTAP lazily when we have to, and so if the first time we need OTAP is in the exporter, great, it happens in the exporter, but, like, as soon as you add, like, a transform processor or something else in the middle, that… conversion now happens in the processor, and then you lose the opportunity to put that on, like, the gRPC thread, for example, so…
Laurent Quérel 00:17:46 Yeah, that's a good point. Yeah, definitively.
Yeah.
Kennedy, you want to say something?
Kennedy Bushnell 00:17:54 Yeah, so this is not about, any type of batching work that exporters may do themselves, right? Like, if you're sending to a backend that imposes additional let's say you've got a batch that comes in at 4 megs, and you're sending to a backend that requires them to be in 1. This isn't about any of that type of thing?
Laurent Quérel 00:18:16 No. Yeah, no, no, no, it's not really that… It's more on the… Taking into account the, the fact that we have a single SWAN managing this event loop.
And where we have a competition between task… that run into this thread, dedicated for I.O, some others are dedicated for processing.
And, and we… We count on the fact that each of those tasks will, We'll just use a fraction of the thread responsibly.
Without, yeah, having the monopoly of the thread for too much time.
Because otherwise, that will not… I mean, the system is still working, obviously, but, I.O. will be less processed, and we have no control of it, so it means that, like I said, the socket buffers will be, food at some point. And… and we are basically not… we are not processing the… The incoming data as the efficiency that we could.
Kennedy Bushnell 00:19:31 Yeah, yeah, so this is purely about splitting, like, the CPU-bound and IPO-bound work.
Laurent Quérel 00:19:36 Yeah. Yep.
Kennedy Bushnell 00:19:37 Okay, cool.
Laurent Quérel 00:19:39 Something I, now I remind also about the exporter side, I think I need to create an entry for that. Just one minute on it. The, I was mentioning the max in-flight pattern, in the previous, In one of the previous issues.
So we, for example, for OTLP, OTAP, and now for Kafka, when we have… what… in order to improve the… The global output throughput.
We… we basically… We'll basically send, in parallel, multiple exports.
request, or multiple message in the case of Kafka. And, and, so, it's, it's, it's something recurrent. I think we should support that at the engine level, ideally.
and get rid of the specific logic inside the exporters. I think there is a way to do it at the engine level.
Transform that as a policy.
So every exporter node could basically iterate that from the engine. I need to think about that a little bit more, but I'm pretty sure that That's something we could imagine.
Okay, map permanent snack, oh yeah, this one is a good one, Utcharch?
Drew Relmas 00:21:09 Ukarshan shared that he won't be able to attend this morning.
Laurent Quérel 00:21:13 Okay.
I think I can talk about it.
So we… imagine that you are at the exporter side again, we have some issue with the backend. Obviously, there are different types of errors, some are permanent, some are not permanent.
we already have a way to report that, into the engine, so the NAC can, report, I think there is a… a property, is it permanent or not? And, and there is a cause.
I think that's the… this engine right now. We can probably extend that a little bit. But what was not properly addressed, so this snack will, back probate… Back to the… to the receiver.
at least through every node that, subscribes to the ACMAC mechanism.
And, for the receivers, at least for the TLP receiver, looks like, it was not mapping correctly the NAC that are permanent with the proper client error statistical. And then, a well-behaving OTLP client.
Could, and the way that it was done, it was for a permanent, an internal permanent.
NAC was translated into something not permanent, so the OTLP Client could send again and again the same message, and obviously with the same response.
So, that's definitely a bug that needs to be addressed.
That's the kind of thing that we, I think we… at some point, we need, A validation framework.
For… to detect behavior of this kind, to validate behavior.
Joshua MacDonald (Microsoft) 00:23:19 the Go Collector doesn't quite have this detail right either, so we're in good company.
Laurent Quérel 00:23:25 Yeah, but we need to do later. I agree. Yeah.
Receiver, exporter, share metric set, oh, this one.
Ruh.
I'll let you,
Drew Relmas 00:23:40 Oh, beautiful.
So this was, as I'm sure most people on the call know, we've been doing a whole overhaul of a lot of the common metrics instrumentation of the engine itself.
And… Laurent recently did some work on a couple of the exporters, looking at what the shared exporter metric set looks like for a few of our different nodes. And that kind of got me thinking, and I was also taking a look at the Go collector RFC on universal component telemetry as another reference. But basically what I want to propose is, a shared receiver and a shared exporter metric set, that I do… I'm not quite sure how it would work mechanically, but it hopefully wouldn't be something that each component author needs to take care of themselves. I'm not sure about that, because everyone… has slightly different semantics in the kind of request lifecycle they deal with, so it could be that there is just a shared metric set, and each component author is responsible for just plugging in values where it makes sense. But in general, I want to be able to describe both the boundary, behavior of the pipeline, you know.
Similar… at a high degree of parity with the internal, work, which we've mainly been focused on, in terms of the node-produced, consumed, channel metrics, etc.
So… Yeah, that's… and then Laurent took this space issue and drafted this fancy diagram that you can see in front of you. Basically, when we talk about receiver, I want to be… Typically, in between nodes in the pipeline, we use a terminology message to denote, like, a message traveling along a channel.
I'm thinking for receiver, we commonly use the word requests, because that's, like, an incoming network request, you know, typically over the wire. I know, there's been some thinking as well floating around about pull-based receivers, so… I'm setting that aside for now, I'm only looking at our current, component inventory.
I think requests is a good word to use here, and then for exporter side, I think exports, something simple. I'm thinking about what you would want, what kind of info you would want to get from every receiver and exporter.
Receiver that we started processing a request, we completed it, how long it took us to process that That, request over the wire, as well as the amount of bytes that we brought in.
And then exporter, you would want to know how many… Laurent, actually, I see messages here. I'm questioning if messages is the right terminology.
Laurent Quérel 00:26:42 Yeah, that's true, that should be export.
Right?
Drew Relmas 00:26:48 Right.
Laurent Quérel 00:26:49 Yeah, we, we, yeah, I need to… To revisit that.
Drew Relmas 00:26:54 And in addition, Laurent, I wanted to… double-click on Bites Success Only. That's a little weird to me, to have metric… a metric that…
Laurent Quérel 00:27:06 That's not… the second line is attribute. Signal, outcome.
Bites. Yeah, but it's… Try to remember, bytes, yes, it's only… I think the, the, the, the…
Drew Relmas 00:27:24 In this case, it's more about, like, over the wire, how many bytes did we have?
Laurent Quérel 00:27:28 Yes, yes, yes, yeah, yeah. And we account for that only in some specific situations, I think that's what.
Drew Relmas 00:27:36 So, if you get… if you get a 400, for example, like, we wouldn't accumulate? That's what you're thinking?
Laurent Quérel 00:27:45 Because…
Drew Relmas 00:27:47 to actually…
Laurent Quérel 00:27:48 Yeah, I think we need to revisit that, because we could accumulate, with the… for each specific outcome variant.
Drew Relmas 00:27:56 Right, right, right. I think that makes sense, because it's not true to say that you didn't send bytes even if you got a 400, right?
Laurent Quérel 00:28:04 Yes, yes, I agree. So that should be aggregated per outcome.
Yes. So, an operator can see what is the effective Export done by this exporter, and what is the one… the bytes that failed? And basically, it's, it's, We are losing some efficiency because there is a lot of… Not, not, saved or properly backed, information.
Drew Relmas 00:28:33 And in terms of outcome, like, I… we would… we should stay away from just HTTP status code, because that won't represent all… possible types of exports, right? Yes. So, we need a different enum-bounded set to talk about.
But anyway, I don't want to take too much time, I know we have a few more issues to get to, but this was just something that came to my mind, and I think as we're doing this huge metrics revamp, we should consider.
Laurent Quérel 00:29:06 Yeah, and Once we have those, and we are very close, because on the exporter side, we already have this pattern.
On the receiver side, not yet. We are closed, but there are variations between receivers.
So not only that will be… Better for the operator of this system.
Because, they will retrieve, some systematic pattern in how the metrics are Arl… Associated to each, common components.
But, it's also very nice, in my opinion. I think, Jake was mentioning that also at some point.
The validation process, that I was mentioning before for a different, domain.
Could basically rely on… on this kind of pattern, and, expect any receiver, expect any exporter.
To expose those metrics.
And and see how those metrics behave, and validate automatically, that the instrumentation is correct.
And, yeah, it's not only the instrumentation is correct, but the behavior of the component is correct for a subset of behavior that we know should be observed every time.
Andres?
Andres Borja 00:30:37 Yeah, I was thinking a little bit before that, is the messages the common name that we are using for those packages that are flowing through the line, or we have multiple of those?
I think…
Laurent Quérel 00:30:52 So message between, between nodes in the DAG? Yes, we name it, message.
Andres Borja 00:30:58 So if that's the language we are using, I think it's important to… to… to share it across all of them, right? So… the… the problem that Drew mentioned about Having something called requests, it implies, like, like,
Laurent Quérel 00:31:15 The requests are only for the… what is coming from outside.
Andres Borja 00:31:20 Right, what I'm saying is that if it's messages, it should be called messages everywhere, because.
Laurent Quérel 00:31:26 But that's the case. Everything here is message.
Drew Relmas 00:31:31 No, I think, Andres, I think you're saying even the receiver ones should be called messages, that's what you're proposing, correct?
Andres Borja 00:31:36 Correct.
Laurent Quérel 00:31:37 Oh, oh.
Andres Borja 00:31:38 Because that will get into the conflict of… Of if it's pull or push, for example.
Which I think we should think of it from scratch, you know, from the beginning.
Yeah, that's a good point.
Drew Relmas 00:31:51 We shouldn't just discount that, because we'll get ourselves into an issue there. That's a very valid point, Andres.
Laurent Quérel 00:31:58 Yeah, I agree.
Andres Borja 00:32:00 So, it's more about, you know, the semantics. That's why I'm asking if we agree that it's messages, so that's great. Let's call it messages everywhere. I don't think we have the same level of consistency in the goal collector, so I think it's a good thing to improve, you know?
Laurent Quérel 00:32:18 Yeah, I think we… I agree. I think we need just to think about it a little bit more, but That will definitely simplify, things.
Is there any concern with that?
Okay, looks good.
Yeah, great.
Drew Relmas 00:32:41 Right, absolutely.
Joshua MacDonald (Microsoft) 00:32:42 I've shifted to using messages in my thinking as well. Requests is maybe the wrong word.
Drew Relmas 00:32:48 Yeah, thank you, Andres.
Laurent Quérel 00:32:50 Yeah, thank you.
Okay… a logical arroyte measurement for a tap. Drew, again…
Drew Relmas 00:33:01 But I don't know if we need to spend a lot of time on it, because I see both yourself and Albert have approved my PR, so I think this is good.
Laurent Quérel 00:33:10 Yes, sir, we approved, we approved not for the Arrow byte, I guess.
Sorry. Cause I had some… Maybe I'm… I'm… maybe I made a mistake, but, for me… I remember a discussion and a PR where we were basically converting OTAP to OTLP message, serialization version.
Drew Relmas 00:33:32 It's just…
Laurent Quérel 00:33:33 To get the…
Drew Relmas 00:33:33 Find the bite size, yeah. So this is… this is the replacement for that. I… I took that out of my previous PR, because Josh rightly had some concerns about it.
Laurent Quérel 00:33:44 and Meetings?
Drew Relmas 00:33:45 talked with Albert, and there's an… there's a native Arrow… function we can use that gets us… Oh, okay.
Laurent Quérel 00:33:53 Perfect, perfect. Okay, great.
Drew Relmas 00:33:55 So, I'm merging… essentially, we can call numbytes now, instead of… I think Lalit had done some work to get retained bytes, which is the full buffer array, which is kind of an overestimation.
But… and he was returning none from numBytes, but now we will return from numbytes. The follow-up PR is going to be caching this value the same way we just added caching of item count.
Laurent Quérel 00:34:23 Great.
Accidents.
Okay, so… Abolo?
Aaron Marten 00:34:35 So this issue right up is an attempt to… define kind of a V1 For exporter plugins.
We have the, kind of, beginnings of WASM hosting.
And at this point, in a kind of, very simple processor plugin, I was anticipating we might have some additional, desires to have exporters as kind of a next Next major area to tackle.
And then I think I'm gonna probably go for a similar write-up for receivers, after this.
Laurent Quérel 00:35:09 Yeah.
Aaron Marten 00:35:10 the… I don't know if we want to go through all of it, it's a pretty.
Laurent Quérel 00:35:15 No, that will take too much time, I guess, except if someone in the… the attendees, wants to ask some questions. I think I know exactly what you are doing there.
Aaron Marten 00:35:30 Good news.
Laurent Quérel 00:35:30 I have both.
Aaron Marten 00:35:30 I mean… oh, sorry, go ahead.
Laurent Quérel 00:35:32 I have only one question for you, Aaron. It's more, A logistic thing more than a technical question.
So, we initiated, a meeting with a few folks from F5, expert from Western Time.
And unfortunately, I didn't reschedule any meetings since. Do you want me to schedule something every week, every two weeks?
It's more for you, so let me know, what would be the best In your opinion.
Aaron Marten 00:36:08 I mean, yeah, maybe every… maybe every two weeks, just to kind of check in. I don't have the, like… like, I haven't had a ton of questions working with it. I did have one very specific question related to some of the async behavior that I asked.
in that, kind of, like, Slack chat that we had set up between a few of those folks. I didn't see a response, so I ended up answering my own question and getting unblocked, but, There may be…
Laurent Quérel 00:36:34 for that, and I think, having this recurrent meeting will, We'll make this channel a little bit more effective.
Aaron Marten 00:36:43 Do they?
Laurent Quérel 00:36:44 Okay great. Excellent to see progress there.
Joshua MacDonald (Microsoft) 00:36:49 Very cool. Yeah.
Laurent Quérel 00:36:52 That will be a big differentiator.
Okay… Define consistent policy resolution, I think, yeah, Lalit, I don't know if Lalit is with us.
Drew Relmas 00:37:06 Is also not here today.
Laurent Quérel 00:37:08 Okay, so, I think we can just accept. I think we… it's… it's a… It's a topic that come… that came many times, in various occasions, so I don't think it's, It's a problem to just accept it.
Joshua MacDonald (Microsoft) 00:37:28 So this is just sort of, like, highlighting that we have this confusing topic, which is this multi-level policies. I say confusing, that's, like, my mental model. We have multi-levels of policies, and when you get to a real configuration, there will be a composition of multiple levels, and the question here is, how do you take multiple levels of thing.
Turn it into one resolved.
specification of the policy consistently across the domains that are in the policies, is what I… what I'm hearing this as.
Laurent Quérel 00:37:57 Yeah, knowing that this AIO cone policy stuff, it's… the rules are simple. The closest level to you win.
If it's you, you win. If it's the group level, the group level win, and so on.
But, I think it was also the… The observation that sometimes we need to name a specific policy.
And attach this specific policy to… To, to a node by name, because there are some situations where that makes sense.
And I think that, It's about having these two models together and how we can make them… we can make this thing consistent and understandable.
Joshua MacDonald (Microsoft) 00:38:46 I see, because sometimes the policies contain maps by name to policy fragment, and then I think you're not just saying, take the closest one, you're saying, look at every namespace to which I have access, find me a named policy.
Laurent Quérel 00:39:04 Yeah.
Joshua MacDonald (Microsoft) 00:39:06 Okay.
Laurent Quérel 00:39:09 Okay. So we'll continue being open.
Joshua MacDonald (Microsoft) 00:39:10 And we'll keep working on it.
Laurent Quérel 00:39:12 Exactly.
Okay, I think we are good, this one. I don't think we have the time. Structured security report nest for the FNG.
It's, Old Juan, I don't know if we have Sijo with us today.
Drew Relmas 00:39:29 No.
Laurent Quérel 00:39:30 Okay, so let's keep it this way.
What about the topics? We don't really have too much topics, so we can continue on the still… Columnar query and gene filtering, additional feature support… I think we have to keep this one open, Albert.
We still have the… those things, right?
Albert Lockett 00:39:55 I'm pretty sure this actually works now.
Laurent Quérel 00:39:57 Oh, okay, so let's do,
Albert Lockett 00:40:00 Yeah, we can close this. That's, I'm pretty sure that's all working.
Laurent Quérel 00:40:06 Okay… And, filter by static literal.
Albert Lockett 00:40:13 Yep, that's, that's implemented.
Laurent Quérel 00:40:16 Okay, ongoing.
Arithmetic that's supported also.
Albert Lockett 00:40:22 Yep, and function calls is supported. Yeah, we can close this.
Laurent Quérel 00:40:26 Okay, perfect. So we can close it, close issue.
Okay, declared, sorted column. I think this one, we already, installed it one time, so I think we… We are still in the same situation.
Do you agree on that?
That's about the ability to have some metadata attached to the column to define.
Albert Lockett 00:41:05 Yeah, I think, I think it'd be nice if we did this, but it's… it's still not done.
Laurent Quérel 00:41:11 Yeah.
Joshua MacDonald (Microsoft) 00:41:12 And does that belong in the Arrow?
Part of the payload, or is that context?
Laurent Quérel 00:41:18 It's, in the metadata of the… oh, sorry, you want to respond?
Albert Lockett 00:41:23 I was gonna say what you were gonna say. I think it belongs on the Arrow Record batches, not on, like, the OTAP badge context.
Laurent Quérel 00:41:30 Yeah.
Joshua MacDonald (Microsoft) 00:41:31 I accept.
Laurent Quérel 00:41:33 Okay, and, OTAP gRPC propagate error status code.
Joshua MacDonald (Microsoft) 00:41:40 This one feels like the one we were talking about earlier. Yeah.
Laurent Quérel 00:41:43 Yeah, I agree.
Joshua MacDonald (Microsoft) 00:41:43 It was a known issue, like, you can see the history of how we added the permanent status, and then we, you know…
Laurent Quérel 00:41:50 Yeah.
Drew Relmas 00:41:51 Lukarsh found it, he referenced it.
Laurent Quérel 00:41:54 Oh, nice.
System is working.
Joshua MacDonald (Microsoft) 00:41:57 Okay.
Laurent Quérel 00:41:58 That's great. So, okay, we can keep, that this way, right? Or do you want to act, differently?
Joshua MacDonald (Microsoft) 00:42:06 It's okay, let's keep this one, it's a… it'll…
Laurent Quérel 00:42:08 Okay.
Joshua MacDonald (Microsoft) 00:42:08 Possibly fall out of the other.
Laurent Quérel 00:42:10 Okay, great. I have something to… to mention before to go to the file exporter.
So we have this, we have a benchmark suite.
We have basically two categories of benchmark, the continuous benchmark, And, the comparison benchmark.
Which is not updated, I think it's an update that is done manually.
And we didn't, updated it, recently, but that's not my concern. My concern is more about the… The continuous benchmark, and making sure that everyone is looking at it regularly.
Or at least every month in a row.
I… I didn't see on the… on the main one.
Strange behavior, or something that should require our attention, but… When we look at, scenarios… So for example, this one is about C-slot TCP benchmark.
There are… there are some situations like that.
or like that, that I think at least we should discuss and be aware of what is missing, unfortunately, into the continuous benchmark solution that we have.
We don't really have a way to add labors… to… to basically mark a situation and say, oh, yes, we know, we are aware of that, and the explanation is XYZ. I think we will be ideal if we end up into the situation at some point. But, I think we… we should regularly look at the… Those benchmarks and detect when there is something like that that is strange.
and permanent, and try to think about it and see if it's normal or not. We have, other situations like that. So this one was about, Where's about what… Oh, batch… batch… batch style variation. I don't know if it's, Normal or not, or not, maybe we change the… some configuration of the traffic generator, I don't know, but again.
Maybe there is an issue beyond that, maybe not… And, and this one, again, syslog, egress bites. I think it's got… it's, at the same time than the other one we saw on… on syslog, so maybe there is a… Something normal there, but again, and
Drew Relmas 00:44:58 I think the commit that's flagged there seemed like CJ was re-enabling the workflows. So… I'm curious if this is actually steady state?
And the procedure…
Laurent Quérel 00:45:14 Yeah.
Drew Relmas 00:45:15 Content was misleading.
Laurent Quérel 00:45:17 Yeah, maybe, maybe.
Kennedy Bushnell 00:45:19 Yeah, we've talked about this before. That was the case. He fixed it.
Laurent Quérel 00:45:22 I don't care.
Kennedy Bushnell 00:45:23 Broken tests, and this should be our new normal.
Laurent Quérel 00:45:27 Okay.
But that explains this, this, specific issue, right? Not necessarily all the other ones that we, we saw, for example, yeah, we had multiple situations.
Right.
Kennedy Bushnell 00:45:39 Yeah, those probably are different.
Laurent Quérel 00:45:41 Yeah. Yeah, I think we, we, at some point, we need… At the minimum, a label that could help us interpret those bumps.
When they… when they are already identified, And, And also making sure that all maintenance are looking at those charts and making sure that we… We don't, blindly continue to work on something that… where we introduce a regression.
And this one, I don't know, it looks very strange for me also.
It's about the trace.
We don't exercise so much stress, so maybe there is an issue, maybe not… But again, we have a strange thing there. Looks like something that was not done properly that becomes It was, yeah, CPU percentage zero. Looks like there is no trace before.
Oh, there is a trace there.
Yeah, I don't know, something strange.
Again, to… probably to investigate at some point.
Okay…
Joshua MacDonald (Microsoft) 00:46:55 I added a note that we should all be keeping an eye on those, mysteries.
Laurent Quérel 00:46:59 Thank you.
Joshua MacDonald (Microsoft) 00:46:59 As you point out.
Laurent Quérel 00:47:00 Yeah.
Excellent.
Pet exporter, so the…
Joshua MacDonald (Microsoft) 00:47:08 Please, please carry forward with your topic about the file exporter, and maybe in a minute I'll connect it with the.
Laurent Quérel 00:47:14 Okay.
Joshua MacDonald (Microsoft) 00:47:15 order that I linked there.
Laurent Quérel 00:47:16 Oh, yes, interesting, yeah, yeah, yeah, yeah. Let's see… Tweez… So we must do…
Joshua MacDonald (Microsoft) 00:47:34 There's so many PRs, it's hard to find them.
Laurent Quérel 00:47:37 Oh, yeah, that's the second entry. Okay, sorry, my bad. So file exporter, so that was, I had to urgently Create, a new exporter.
Basically mimicking the… what we have with the… the file exporter in the… in the Go, collector, with… with some adjustments, but, One of the adjustments is taking into account that we have, a straight parkour, share nothing.
Architecture and, every core… We'll have… we'll generate a different file, and… and those files will be… There is, I think, yes. There is, in the configuration of this, exporter file. We have this pass.
where the signal, the core ID, and the generation are required, but you can put them where? Where you want into the pass, but they need to be there.
And, and this way, we have unique files.
One per call.
That's one of the major differences between this file exporter and the other one.
Right now, the… let's say the features, capabilities supported by the file exporter are relatively limited. We don't support rotation right now, we don't support compression.
And we don't have any retention mechanism that is defined. That will come soon, but I had to do that quickly and get a first version, so phase one is relatively basic.
But we already have things like the ability to To specify if we want to sync every, right, or if we can let the OS buffering, the… the data. There is, an open mode.
There is also something that was missing into… I think it's, let's see… Yeah, the repair on an incomplete, happen node.
So, and this one, We, we check that, let's say you restart the, the… The engine, and we basically crashed So there may be some entry at the end of the… Some of those files will be incomplete, so we have a way to check that, remove an incomplete entry, and And just, generate, making this file valid for future, for future, import.
So, as I mentioned, we'll come later, support for OTLP proto message format. Right now, it's only OTLP GZON.
A retention plus, completion plus… audition.
And ye… Feedback, question on that?
If you are interested by how it's designed, there is, an architecture.md file describing that.
So, you were mentioning…
Joshua MacDonald (Microsoft) 00:51:11 I was making a mistake earlier. I wanted to discuss this issue about database receivers, and I would connect.
Laurent Quérel 00:51:18 Yep.
Joshua MacDonald (Microsoft) 00:51:18 receiver.
Laurent Quérel 00:51:20 I don't remember.
Joshua MacDonald (Microsoft) 00:51:20 the status of our file receiver work. I know we've talked about it a little bit. I started to review this yesterday, and I came across, effectively a need to checkpoint, what data has been received Already by a receiver, and that this receiver, as well as the file receiver that we are kind of hoping for.
both have a common, essentially, need to keep track of what they've already ingested in a durable way, so that we can restart or crash and come back and not replay a bunch of data that is available in a log file or in a database. And I was wondering if we have Any emerging designs or plans around, this sort of management of durability for receivers, and whether we expect to see something common emerge, or whether it's sort of, like, on your… on each receiver on its own to handle this issue. So yeah, again, not connected with file export, connected with file receiver.
Laurent Quérel 00:52:27 Yeah, the file receiver, I think we have… try to remember, I, I, I, work on… a proposal… where I think some patterns are in common with what you described.
Joshua MacDonald (Microsoft) 00:52:46 Yeah, I guess that maybe the kind of, like, wish that I have kind of corner… in the corner of my head is that we have… we have mechanisms for storing durable things. We have a… we have Quiver, we have the ability to put pipeline data into… onto the disk, and when we find ourselves in the need of essentially needing durability as a receiver. We could invent it ourselves, like, from scratch.
And whether it's shared or not, we could do that. Or we could try to imagine, essentially, an internal pipeline where you record things through Quiver, and then export them to yourself, or something along those lines, to reuse the durability mechanisms that we have for receivers.
That was just kind of what's… what's.
Laurent Quérel 00:53:31 I think we could… I think it's a perfect example of an extension.
Exposing your capability, To store or state.
For the… For this kind of situation.
And we could imagine that we provide a basic file-based state mechanism.
That persists across, crash or restart, but we could also imagine that some people come with a radius-based or… Whatever, a Dinamu, DB, or, the equivalent for, for Microsoft.
Joshua MacDonald (Microsoft) 00:54:17 See Aaron's hand up.
Aaron Marten 00:54:20 Yeah, I was just gonna chime in and say something very similar. I think, at the very least, maybe we designed some kind of a cursor service that multiple different receivers could opt into.
Quiver has its own kind of, a couple different places where it persists cursor files and manages them, so maybe we refactor that functionality out into something common.
Laurent Quérel 00:54:41 Yeah.
Seems great.
Yeah, I like…
Joshua MacDonald (Microsoft) 00:54:44 Good idea. Sounds like a good extension.
Laurent Quérel 00:54:47 I, I don't know if for this, specific, what it is… Also, I'm not managing my tab properly today.
Yeah, when I read this, very quickly, so I didn't, enter in much detail in this, in this issue, and But I was thinking that maybe there are some other patterns that will be required here that will be shared with the file receiver.
So, in the file receiver, we are in front of the following problem.
We… we have a multi… a multi-core… Chernosigne architecture.
So, I mean, straightforcourt, Chanelessie Architecture, and… And we want to avoid to have each instance of the file receiver Doing the same work than, the other friends.
So there is a need for some kind of orchestration.
That will say, oh, you do this job, do this one, and do this one. So, basically, an extension that will look at the amount of work to do, so all the 5 that need to be observed.
into a bunch of directories, and those files can arrive periodically. So there is a monitoring aspect of it. Look at the things that we need to do, and then there is an orchestration aspect. Basically, a message that will be sent to A receiver saying, oh, take, take care of this file, it's for you, and the same thing for the others.
I was thinking, do we need such mechanism also for this kind of, scrap-oriented receiver that will query a database, like Oracle.
Joshua MacDonald (Microsoft) 00:56:55 Yeah, this, I think we're on the same page. This notion of a scraper, the title includes base scraper, and that's, borrowed, essentially, from the Go Collector, has an apparatus, a common framework for receivers that pull data from lots of sources.
And so, there will be a common configuration that says, I'm a scraper, this is my interval, this is my policy, like, for repetition, for retry, for back-off, for all the sort of things that we need policy around scrapers for.
Because they're… many of them, they're individually enabled and disabled.
what you just described would… in this architecture, you're going to want to run each scrape event on one receiver. So you could imagine having a multi-node, multi-CPU receiver that gets distributed work Through some sort of basic scraper apparatus.
Laurent Quérel 00:57:52 Okay, I was not aware of that, because I look at the GoCollector when I was designing the spec for the file receiver, I don't remember… Really?
Joshua MacDonald (Microsoft) 00:58:02 It's not using the scraper mechanism that exists, but there is such a thing, it's not well documented, it's part of a bunch of… Like, metric… it's many, many metrics plugins are very specific to a specific metric that only exists on some platforms, and the receiver will be organized as a… essentially an adapter for the standard scraper support. And so the adapter knows how to get the individual metric, the scraper tells it, schedules it, essentially.
Laurent Quérel 00:58:29 Okay.
Okay, so… and do you think that there is a connection with the Oracle receiver?
For example, can we swap Range of froze.
That does not overlap.
And this orchestration mechanism that we just described could be used for.
Joshua MacDonald (Microsoft) 00:58:49 Yeah, I think so. That's also the cursor state that you would want to persist as well.
Laurent Quérel 00:58:55 Which is a different, in my opinion, pattern, and maybe the orchestra.
Joshua MacDonald (Microsoft) 00:59:00 Administration is the one that's doing durability of.
Laurent Quérel 00:59:03 Yeah, that could be that, yes.
Joshua MacDonald (Microsoft) 00:59:09 In any case, the concept of this using the word scraper as the sort of general purpose Schedulable telemetry source retriever, is at least the concept we're aiming for here.
Laurent Quérel 00:59:26 I'm not sure if we need to name it Scraper, because I can totally imagine…
Joshua MacDonald (Microsoft) 00:59:31 That's not a very good name, how's that?
Laurent Quérel 00:59:32 Yeah, I think something that will orchestrate job, I think that's what we want.
A job orchestrator across multiple instances running in different core.
In order.
Joshua MacDonald (Microsoft) 00:59:46 Interesting.
Laurent Quérel 00:59:47 Avoid duplication of, effort.
I think that's what we want, and that could be used for the scraping situation.
Where we have such need of coordination.
But I can totally imagine other situations that are not Skype-oriented, that will require this orchestration.
Joshua MacDonald (Microsoft) 01:00:09 Just another example, it would be a Prometheus receiver. It's going to have a list of 100 targets, let's say, and then you could just distribute those through an orchestration.
Laurent Quérel 01:00:19 But in that case, it's close to the scrapping, but but, Yeah, okay. I think we can definitely work… I think that's something on which we need to work. It's a fundamental, requirement, for… for the engine, partially related to the fact that we have a specific architecture.
And we need to provide that for future receivers that will otherwise be very complicated to implement without this capability.
Joshua MacDonald (Microsoft) 01:00:54 Sounds good.
Laurent Quérel 01:00:56 Great! End of the hour. Any, last-minute, comment?
Okay, thank you, everyone, and have a good, end of week.
Drew Relmas 01:01:12 Thanks. Bye-bye.
Joshua MacDonald (Microsoft) 01:01:12 Cheers.
