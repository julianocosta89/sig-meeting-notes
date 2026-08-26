SIG: Arrow SIG
Date: 2026-08-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Laurent Quérel** 00:14 Bye, guys.
**Jake Dern** 00:16 Blue.
**Josh MacDonald** 00:22 Hello.
**Laurent Quérel** 00:25 Yeah, it was fun.
**Josh MacDonald** 00:29 is say that these afternoon SIG meetings Tax me, somehow.
4 o'clock.
**Laurent Quérel** 00:40 Yeah, I don't know what I prefer.
**Jake Dern** 00:46 I think I'm on the same page as Josh. I think about 4PM I'm due for a crash.
**Josh MacDonald** 00:51 Yeah.
**Laurent Quérel** 00:54 Dr.
**Josh MacDonald** 00:54 dinner, I'd be better, yeah.
**Laurent Quérel** 00:59 No, the one that is the most problematic for me is the one that I have tomorrow at 7am.
For, Hotel Wheeler. That's the… the worst. Cebenheim, I'm definitely not on board.
**Jake Dern** 01:16 I think.
**Laurent Quérel** 01:17 Except…
**Jake Dern** 01:17 7AM is my most productive hour.
**Laurent Quérel** 01:20 Oh, okay, good for you.
**Josh MacDonald** 01:24 I have, entered one item on the agenda with a sort of future… forward-looking, set of issues for myself, but it's, sort of minor, so I hope that others will put their Items on the agenda.
**Laurent Quérel** 01:42 Yeah, but I think there is a… we have… I think two important, in the triage part. I think we have two additional issues.
That could be discussed, the one that is related to… Some improvement regarding the configuration framework we have.
And, the other one related to the… the pregable PDATA codec stuff, and what you also added around it.
Like, it might be related to what you also.
**Josh MacDonald** 02:19 Yeah.
**Laurent Quérel** 02:19 Yeah.
**Josh MacDonald** 02:20 It is. So, while I have this, screen shared, we may as well start. These are the needs discussion There are many of them.
I guess we start at the… Bottom?
We've skipped this one from CJO a couple times. We skip over this Phase 3, which is, I think, okay to leave.
And then we're back to this one that just right into it, the system decay support for Kafka receiver logs path, that's one about where we have discussed, pluggable representation.
for OTLP Bytes, which… oh, I'm not logged in. Well, anyway… That… is here.
Would we like to discuss this now? We do have Brian here on the line, and I.
**Laurent Quérel** 03:19 Yo.
**Josh MacDonald** 03:20 A bit with him as well.
**Laurent Quérel** 03:22 I think that.
**Brian Sapozhnikov** 03:22 Hello.
**Laurent Quérel** 03:23 I don't know.
**Josh MacDonald** 03:24 Hey, Brian.
Yeah, so this was basically, I think, a long-term vision that we try and factor apart the code so that syslog parsing is available as a module that we could use. And then the second idea, the one introduced in this, And this issue here is that we would carry some sort of extension marker and allow other payload bytes to pass through our pipeline so that we could lazily or lazily decode other content types into OTLP or OTAP.
**Laurent Quérel** 03:58 yeah, if I can add to that, I think the… the problem is the following. So, first, we are trying to… to favor into this project, composability. So that means that… We try to… We move as much as possible specific, implementation from components, and in order to externalize them into one place, and they can be composed with various other, systems. So, concretely.
For example, the retry processor is a good example.
The required processor is dealing only with, retry strategy.
**Brian Sapozhnikov** 04:42 And twice about history.
**Laurent Quérel** 04:43 And… and we can combine AI There is someone that needs to…
**Brian Sapozhnikov** 04:47 somewhat addiction.
**Drew Relmas** 04:49 Brian.
**Josh MacDonald** 04:49 Brian, you're, you're feedbacking.
**Laurent Quérel** 04:52 Yes.
**Brian Sapozhnikov** 04:52 Oh, sorry.
**Laurent Quérel** 04:55 Yeah, so I was using the example of the retry processor, because I think it's something similar.
There is multiple ways to, to imagine, A retry mechanic, or a retry, system.
It could be embedded into every exporter's.
Or it could be a dedicated processor, and we compose this processor with any Exporter, and then we get for free a retry mechanism.
For any current and future exporters.
And there is a clear contract.
to, On which every exporter needs to comply to, and then they will be a part of this, retryable mechanism.
So for… for this syslog decoding support for the Kafka receiver, I think we are in a similar situation.
we could imagine, for example, an MQTT receiver, a Kafka receiver.
PubSub, a GCP PubSub receiver.
So that's the kind of, persistent cue.
We're dealing with messages that we can consume from the receiver, and, the message, part of those persistent queues could be OTLP, protobuf representation, could be JSON messages, could be OTAP message, could be… a batch of syslog messages. So what I mean is… There is, in my opinion, no point to make a specific decoder into the Kafka.
A receiver, because most likely we will have to Do that again and again in different receivers in the future.
So… That being said, the idea was to create this, pregable pilot, Codec extension.
That could be… A new type of extension.
And reused again and again in different receivers.
And that's the 3452.
And it's basically an extension that will define The encoding, decoding, the decoding from whatever format to a tap.
And the, the encoding or tap to any kind of format. And this codec could be… Heather, or just the decoding part?
the encoding part, or both directions, or together. There is nothing preventing to force anyone to necessarily implement both directions.
So… With that, we could change the existing way that we… So, right now, the OTLP and OTAP are deeply… Let's say, embedded into the engine.
And, so we have a special treatment for them.
But we could make that generic.
And, and we… we could rely on… default P data extensions, OTLP and OTAP, and progressively add additional extensions, so this, syslog codec could be added.
And then, magically, it will be available for… I mean, we can find a way to make it available for the Kafka receiver, and in the future, for the GCP PubSub receiver, and so on.
So I really think it's, It will be a nice addition, and will make the entire system much more, I mean, easier to, to, To, to have new, new formats, that will be beneficial for… A large category of receivers, exporters.
**Josh MacDonald** 09:04 True.
**Drew Relmas** 09:06 I just want to ask, because I feel like there's two slightly different angles here. The first is a reusable piece that, for example, receivers can use to, take the same raw data format and put it into internal representation.
totally down with that. I think it's… doing a receiver extension is almost equivalent to, like, reusing the parser library.
But I agree with you that it'd be nice to have it abstracted in a way where it's just plugged in to the syslog receiver and the Kafka receiver, and that's just good.
The other kind of angle to look at this is keeping data in that representation as long as possible in the pipeline, basically delayed decoding.
**Laurent Quérel** 09:57 Yes.
**Drew Relmas** 09:58 So… I think there's, like, the reusable component, or the reusable extension to let multiple receivers decode the same kind of data, that's definitely, like, a shorter-term achievable goal. I think keeping you know, once we have that proven, once… let's say we have the decoder extension on receivers, we could potentially… Hear me out on this, Laurent, what if we were able to attach the decoder extension to a pipeline as a whole?
And every node, if it needs to run decoding, it has access to that extension to decode. Yeah.
**Laurent Quérel** 10:42 Well, that's true.
**Drew Relmas** 10:43 We see it as a tiered approach here. First, we make it available for receivers, and then we think about making it available anywhere in the pipeline.
**Laurent Quérel** 10:51 We could… so what you just described is… Indeed, I did not mention it, but it's described into this, issue.
The… the pass-through mode.
So, but basically, what… mimicking what we are able already to achieve with OTLP bytes, And, And decoding this, OTLP bites, in a lazy… fashion or lazy mode only when it's needed. So we… when we don't need it, it's just… the system behaves as a pass-through… in a pass-through mode, so we don't basically decode the OTIP bytes, and we… we can route them to… a destination, because in the middle, we didn't have to interpret the OTLP byte. That happened. We could imagine that applied to any format. The Parquet format was the… The, the initial, reason why we created this new, GitHub issue, but that could be applied equally to, to the syslog example, and then we have a pass-through mode for Parquet, or for syslog, or for OTAP, which is super nice.
Is it much harder to implement? I don't think so. I think it's just a matter of defining properly the… The interface of this, a pluggable, PDATA codec.
We could imagine that we split that into, maybe it's, it's the right approach.
I'm not sure that it's so… so different.
**Josh MacDonald** 12:40 It sounds good to me.
It is one of the great shames of Zoom that I can't give a thumbs up when I'm presenting. Ukarsh.
**Utkarsh** 12:52 Yeah, hi.
So, I did go through the issue a little bit over, like, I took a high-level look at it. So, I have a few questions, like, I… I see the value of PData codec trade, But I think the scenarios that we're considering, like, where we want this common parsing logic extracted out so that syslog receiver and Kafka receiver can both use it.
I'm… don't see us doing any kind of lazy decoding at all. In fact, we would… We want to decode it as soon as… at the receiver end itself.
Because we want to emit metrics about invalid logs being sent.
And those things. So we… we don't really want… The same byte representation that we are receiving To be passed through.
In the pipeline.
I mean, I… I… I think we… what we need is something similar to what stanza offers in the Go Collector world, where, You have an abstraction over how to decode bytes.
into an internal representation. That could be… in our case, it could just be that we… Provide a mutable log… log records builder, and we also provide the input bytes, and then the custom logic can decode it the way it wants, and append to that builder, and the receiver can decide when to call… build on it to make an Arrow batch out of it.
So that can, again, be like a public abstraction to look kind of similar to the first half of the PDataCodecTrate method, but But I think that's what we need here.
**Laurent Quérel** 14:37 Don't you think, Utkarsh that… if we take the example of the Parquette and the motivation So first, I agree with you that most of the time, for C-slug, that will not be necessarily the pattern that we want to follow.
But we could… we could sell the same thing for Parquette, and it looks like… internally.
you have this requirement, for… for the packet, so I'm just trying to Maybe, thinking that that's something that could also be useful for CSLogo, for any kind of format. Imagine that you have We use this engine to… "… To import, or to… to consume, syslog batches present into a Kafka topic, and… and based on… on a configuration, you want to root those, Message to a different destination without necessarily decoding it.
That's… I think that's a scenario that is… pollute for the Parquette, representation.
If I remember well. So I'm just trying to think, okay, why it would not be necessarily also useful for syslog.
For me, it's… It's an option. Obviously, it's, It could be, a configuration decision.
**Utkarsh** 16:07 So you're saying, if you're operating in a mode where we are purely forwarders, just, we don't do any decoding or processing at all, we receive something and we just forward it?
**Laurent Quérel** 16:18 Yeah, forward it to a different destinations that could be based on, let's say, for example, a Kafka header.
Sure, yeah.
**Utkarsh** 16:28 So, in, like, a pure forwarder mode, I think the straight definitely helps, because there, like, we are able to utilize the… the lazy decoding part. In fact, we will never decode.
**Laurent Quérel** 16:41 Yes.
**Utkarsh** 16:41 with your folder. Yeah. But… I think the… at least for syslog receiver scenario, most likely, it'll always go through some kind of filtering or transformation and final.
**Laurent Quérel** 16:52 Yeah.
**Utkarsh** 16:54 So, I see some value in having a smaller subset of abstractions which are mainly Either only at the receiver side of things, where Also, like, syslog receiver at least doesn't get a batch of messages usually, so we operate on a single record, and we keep appending it to the builder. I'm not sure how the Kafka receiver is gonna work, if it's gonna operate on a single syslog message, or, like, would it get a batch of messages? So based on that, again, the, Abstraction might have to be different, like… Do the bytes represent a single syslog message, or do they represent a batch of messages?
Because converting or forcing someone to convert a single syslog message into an OTAP record is going to be wasteful.
**Laurent Quérel** 17:39 Oh, yes, yes, yes. But I don't think fully, because the overhead of the Kafka message is not negligible.
So, I would be very surprised if someone is using mapping one syslog event, one Kafka message. That will be particularly inefficient.
So, my guess is… and Brian can probably answer this question. My guess is, most likely, the Kafka message will present a collection of these slugan trees.
**Brian Sapozhnikov** 18:15 Yeah, I think we definitely want to at least, support that.
Right? It's… it's easy to go the other way.
**Josh MacDonald** 18:26 And is there, like, a natural separator? Like, I imagine a new line, just like, here's your syslog line, here's another syslog line, or do we have to frame those lines, is, I guess, the question.
**Brian Sapozhnikov** 18:40 Yeah, honestly, I'm not sure, but I imagine that would be part of the responsibility of… that's specific to Kafka to define, because maybe it's in, like, the metadata that we get back from Kafka to indicate things like that. I'm not really sure.
**Jitender Bisht** 18:55 if I may, so generally it depends on if the, if the syslog, plugin where you're pushing the logs to, if it's consolidating into a multiple… single events have multiple records, then you need to have a delimiter. And the delimiter, I'm not sure if it can be defined by anybody else. I think it should be defined… As a part of the record itself, right? So, I think it should be part… it should not be part of the Kafka, but it's… it's definitely part of how you're pushing those events as the raw events.
**Josh MacDonald** 19:28 Right, so in the case of JSON logs, which we have a lot of experience with, a new line would be appropriate. Maybe you would have to invent a sort of bespoke protocol to be a collection of syslog messages, which would be a repeated bytes protobuf or something like that.
**Jitender Bisht** 19:44 That's right.
**Josh MacDonald** 19:45 That, that all sounds okay to me.
I pulled up, sort of slightly related, somewhat tangential, somewhat trying to move us along. This is an issue that I filed yesterday, essentially asking for the same type of pluggable representation, but applied to Arrow records. So I was going to also interject that if you have a situation where it doesn't make sense to turn one record into one byte array, you might instead figure out a way to turn it into a batch of Arrow records. This is going to take too long if we talk about everything in this meeting, but you can also follow up on this item.
As a sort of alternative intermediate representation, if it appeals to you.
**Laurent Quérel** 20:28 Yeah, so I think there is a big potential Behind this pluggable, P-data extension mechanism.
I think we could… in my opinion, the first thing to do will be… Not even to, to, create an extension for C-slot, but just… converting what we have today, for OTLP and OTAP.
And just, transforming what we have today based on this pluggable Pdata extension.
And supporting the same kind of behavior that we support today.
Meaning the, the password for RTLP, and obviously, the native OTAP representation.
Once we have that, we basically all produce what we have today with this pluggable extension, and then we can start to extend it to support syslog?
And later on, Parquette, and whatever format people, would be interested in.
I really think that's the right path to go, because first, I don't think it's super complicated.
And, and second, that will be… A nice way for us to… To check that this transformation and additional extension mechanism does not change anything in terms of performance.
Because we will basically be able to compare the before and after with exactly the same parameter.
And then once we have the validation of that, then we can extend the mechanism.
And, and starting with, with CSMUG.
**Utkarsh** 22:30 Okay, but I had a question, so… is the goal also to have the receiver, such as syslog receiver, adopt some kind of abstraction? Or, like, because right now it's very… it's hardwired in the receiver logic that… The bytes that it receives, it Tries to make a log record out of it.
And append it to the builder.
But do we want to change that to use some abstraction?
**Laurent Quérel** 22:54 I think we will not force the syslog receiver to do it, but it could be nice, progressively, to… to let the syslog receiver adopt this syslog version of the pluggable pdata extension.
And I think we need to design the corresponding CADEC threat.
To make sure that, the… the integration with a receiver like syslog will be straightforward.
Yeah. And I think it's… this conversation on, notifying the limiter for a line, I mean, exists, obviously, also in your implementation with Utkarch. The C-Strike receiver, I mean, obviously, has, line separators, and, I don't think that will be… necessarily different for the KFCL.
Scenario. Could be exactly the same, in fact.
It could be configurable, if really it's required.
But we are already dealing with that in the sysmog receiver.
Brianne, you, you had a… No question?
**Brian Sapozhnikov** 24:09 Oh yeah, just a comment, I guess, and I'm new here, so I will probably say something dumb, sorry. But just to follow up on something that Utkarsh said a little while ago, it sounds like all of the options we're considering involve some concept of a codec, right?
Whether we use it as an extension, or as a separate node, or as something under the hood, inside of PData, does it make sense to start by first factoring out that, like, defining that trade, and then we can start by… Whatever receiver needs it, or whatever node needs it, can use it.
And then we can also use it in the codec, or the extension, or whatever.
**Laurent Quérel** 24:53 Yeah, that's what I was suggesting. Defining the trait, applying it to what we already have today, So, today we could apply it to a TLP and OTAP.
measure the performance. If we have any performance migration or not, we should not, but… And then extend this trait, or at least adding a new implementation for syslog, and progressively add other formats when it's required.
So, yes, I totally agree. That's what we should do.
Okay.
**Utkarsh** 25:37 One question I have is, then when that happens, when we have such a trade and we can allow any byte representation.
To even pass through, like… Do we still call ourselves Hotel Arrow at that point?
**Laurent Quérel** 25:51 Yes.
**Utkarsh** 25:51 situations where we're not even doing any Arrow.
**Laurent Quérel** 25:54 I think there is a rational behind it.
Because, fundamentally, Fundamentally, the engine, the pipeline, and all the components.
all the processor, I should say, are, working on OTAP.
So when you have a processor that's required to understand the the data itself.
That's why this codec will be used.
on the fly.
But when the processor or the exporters don't really need to look inside the data, they can just behave in a pass-through mode.
and, and, route or, or export the corresponding data. So, this password mod is, like, an optimization Mechanism that we can get for free with this password mode that will be generalized.
it's still an OTAP, or an OTL, engine, because fundamentally.
Any transformation processing you need to do, like filtering, transform, sampling, and so on.
We require to… to work with OTAP data, or OTel Arrow data.
**Drew Relmas** 27:14 I'm laughing at what Albert said in the chat, but in the interest of time, we probably want to move on.
**Laurent Quérel** 27:22 release.
**Drew Relmas** 27:22 for today.
**Laurent Quérel** 27:35 Okay, so, let's move on. That case.
Joshua, you want to, okay.
**Drew Relmas** 27:41 Yeah, I have two, kind of semi-related issues here. I think we don't need to spend a whole lot of time on it today, but as part of the metrics work, reviewing one of our PRs, Josh mentioned, it's a little weird how we have runtime metrics as a level, and then two bools for pipeline metrics and Tokyo metrics. This issue is just meant to track, is there a way we can put everything into runtime metrics? Should we use… a level enum as well for Pipeline Tokyo, instead of just Bulls, but, really.
don't need to verbally discuss this, I think. People can… Valentine as they wish.
**Laurent Quérel** 28:22 Yep.
**Drew Relmas** 28:30 And then the next one was also something very… short, which is, Laurent and Josh, as you know, I was refactoring the node and flow metrics. Flow has flow.compute.duration, which tracks the compute time across a set of processors.
I found that the node… Duration is a little less clear, because it tracks from the time it reached this component to… the finalization of ACNAC.
it's not actually, like, what duration was spent in the node, so I think I want to come back here and propose a different way. One, to show time spent in the node, clearly, and two, to Make it clear that this metric is, like, from this node looking forward, on the forward.
**Laurent Quérel** 29:27 Like, a completion duration or something?
**Drew Relmas** 29:30 Yes, exactly.
**Laurent Quérel** 29:32 Yeah. Yeah, I think in general, we need to be more, precise.
in the… Or less ambiguous in the semantic of the metric.
And I think this one is a good example, duration alone.
It's probably not… semantically, precise enough to…
**Drew Relmas** 29:55 Flow, it's compute duration, because it's.
**Laurent Quérel** 29:58 Yeah.
**Drew Relmas** 29:58 Spent actively working in each processor.
**Laurent Quérel** 30:01 Yeah, yeah.
**Josh MacDonald** 30:03 I would maybe call this request duration, and when I first put this code in there, it was like trying to copy what the Go collector does, which, because it is synchronous in Go, you're just waiting for the call to complete, and that's your duration.
But I agree that completion duration maybe works, so it's, like, a little bit of a mouthful.
**Laurent Quérel** 30:26 Yeah, the problem with requests is everything is not a request.
Look at, what we just discussed.
Regarding the Kafka and the CSLOG receivers.
Is it…
**Josh MacDonald** 30:40 So what do you call it when Ack and neck is returned? Like.
I guess I still informally think of that as the AC or NAC to my request, but okay, I agree.
**Laurent Quérel** 30:53 Yeah, but it's not always a request, because sometimes you are not receiving a request, you are reading a message into a Kafka topic, or you are reading, In the case of syslug, it's not necessarily the best example, because usually we don't have a knack for syslug. But for Kafka, it's definitely not a request.
So I think it's… that should be something that is more aligned with what… This act, like, represents, and not really what was the incoming message or request.
**Josh MacDonald** 31:34 Yeah, I was thinking of the word round trip, but I don't have any.
**Drew Relmas** 31:38 I was thinking maybe forward path duration, but… Anyway,
**Josh MacDonald** 31:46 I actually don't…
**Drew Relmas** 31:47 Spend time here.
**Josh MacDonald** 31:48 When I first wrote this stuff just at the very beginning, I didn't think anyone cared about forward path duration, except for processors, which already have a compute, which is equivalent, as far as I know.
**Drew Relmas** 32:00 Right, I mean, there's the chance that Actually, this is… we're deprecating this forward path duration, and we should only emit in node duration.
Because Flow takes care of cross-processor.
So that's another option, is…
**Josh MacDonald** 32:19 See, that's a really good point. So you could take away compute duration and rely integration.
**Drew Relmas** 32:27 I'm saying, we take away this… from when a message reaches a node to ACNAC, I think that duration isn't… really helpful. I care more about… I expect to get just node.duration, which is the time spent in this node, and that's it.
**Josh MacDonald** 32:52 Okay, that's a… strangely, I feel the opposite way, like… what I care about is end-to-end latency more, but I'm okay with a.
**Drew Relmas** 33:01 Okay, well, Josh, we can talk about this offline.
**Josh MacDonald** 33:05 Sure.
**Laurent Quérel** 33:05 Yeah, I think, yeah, we have to clarify that definitively.
I was okay with note duration.
**Josh MacDonald** 33:13 Sorry, I was…
**Laurent Quérel** 33:14 Good.
**Josh MacDonald** 33:17 I was just saying I was okay with node duration, as Drew just… suggested.
**Laurent Quérel** 33:27 not duration being what? Because then they start to be confused. Is it, taking into account the ACNAC, or is it just the process.
**Drew Relmas** 33:36 so local.
**Laurent Quérel** 33:38 Okay.
**Josh MacDonald** 33:39 Okay, so we're totally disagreeing. I was, again, still thinking that that was time spent in the node, meaning full… full round trip, like, this… if you're waiting for completion, then that's the time spent in the node.
Interesting disagreement. I, I, I welcome that.
**Laurent Quérel** 33:56 We need to think about that maybe offline, but…
**Drew Relmas** 33:59 I'll post a little bit.
**Laurent Quérel** 34:00 Yeah.
**Drew Relmas** 34:02 I'll post a longer comment on the issue, explaining what I'm thinking.
**Josh MacDonald** 34:06 Thanks, Drew.
Mtls.
For op-amp.
Whoa.
**Albert Lockett** 34:13 Yeah, this is, Pretty, short one. We added a controller extension that can receive config and update it, using, OpAMP, protocol, and, currently it doesn't, do any TLS, so this is, the issue to basically track that work.
**Josh MacDonald** 34:37 Alright.
I have to be honest and admit that I did not realize we had actually merged any op-amp. This is awesome.
**Laurent Quérel** 34:45 Oh, yes, we did that, I think, in… And dry.
**Josh MacDonald** 34:49 Maybe it was the week I went away. Very good.
Well, yes, let's have TLS for that.
**Albert Lockett** 34:58 Yeah, I'm probably gonna… I'm gonna plan on starting working on that, this week, basically.
Right. Which is why I filed the issue.
**Josh MacDonald** 35:07 Cool. Alright, so we have one from Laurent about…
**Laurent Quérel** 35:11 Oh, yes.
Yeah, so this one is following, an observation, so I was reviewing… I think it's, the PR…
**Josh MacDonald** 35:22 Wow, this is the one from Tim.
**Laurent Quérel** 35:25 Yes, I was reviewing the PR, so T3 for, no, no, I don't remember… One of the… one of the recent PRs from Tim.
Which was basically about introducing Secret string.
And making sure that the secrets or the passwords kind of stuff We'll never be visible when we interact with the API or OP, for example.
let's say that you have a configuration that has been provided with some secret, and there is an API to get the current Configuration, we just want to make sure that we have a way to redact… Sensitive information.
And the corresponding PR was huge.
So, initially, I found that relatively strange, and then I discovered that, in fact, it was Not, a bad way to do it. It was more a design flow that we had initially into the system that make this kind of A redacted string or secret string more complicated than we should.
And then, the GitHub issue that, I created, that we saw just before, is about, Proposing some changes in the way that we, We, interpret configuration, so… The recommendation is to split two things. So we see submitting YAML or GZAN, so that's the configuration coming from different sources.
And, and splitting the 1.config from the reserve.config is the solution I'm proposing. Today, they are together the same thing, which complexifies significantly the introduction of a search Mechanism to… to deal with sensitive information.
So, yeah, I don't necessarily need to enter into a lot of detail, but that's about solving a design flow that we have in the system.
**Josh MacDonald** 37:44 Very good.
I agree, I've said this before, the Go Collector is basically a half configuration, and it's very complex, so my fear is that we end up there, where no one understands the configuration logic. But I agree, we have some, Work to do.
**Laurent Quérel** 38:05 Yeah, and my proposal is basically to make that simpler.
We should not have a PR with, I don't remember, 2009 of God, just to…
**Josh MacDonald** 38:17 That was 2,000 lines.
**Laurent Quérel** 38:18 Yeah, so it's a sign that we have something wrong in the design of the configuration model. Yeah.
**Josh MacDonald** 38:27 Yes.
All right, well, we're gonna run out of time if we're not careful, so I know I filed one, it's very brief. As far as I could tell, the OTLP HTTP exporter does not use transport header propagation. Don't think we need to discuss it.
And now we're getting into those issues that I put on the agenda. I would… I would like to run through it quickly.
the… the… previous discussion that we had about pluggable representations kind of leads into this. We've got pluggable representation ideas. One of the ones that I'm interested in is the Net Trace V6 format. This is a diagnostics format that includes a mixture of traces and logs and metrics and profiles, and it would be a nice protocol to be able to pass through the OpenTelemetry data plane, and also this payload does convert into each one of those signals. So, In addition to wanting pluggable representations, which we just discussed, for both bytes as well as for Arrow records, this makes me think that we may want to eventually support mixed signals.
And I know this has come up in the past, I think that this is something we even considered during OTel Arrow Phase 1, the idea that our Arrow payloads, our OTAP payloads, could theoretically mix all of the tables for all the signals, because they don't overlap, assuming that the resource and scope areas are shared, and this is just a point that once we have these pluggable extensions, we might also want mixed formats. Drew?
**Drew Relmas** 40:02 Just one minor note, a lot of the new metrics, Implementations depend on one signal type per, record batch.
So, we would have to be careful about item counting and stuff like that, if we supported mixed messages.
**Josh MacDonald** 40:20 Good point.
**Laurent Quérel** 40:20 Yo.
**Josh MacDonald** 40:21 Got it. Yeah.
**Laurent Quérel** 40:23 I mean, there are multi… I think it's a long-term project. We discussed that this morning with,
**Josh MacDonald** 40:28 Yeah.
**Laurent Quérel** 40:28 with Joshua. I think it's an interesting challenge, but it's a long-term project, and there are many many, ramifications or complex things to deal with, with that. For example, the batch processor is an example.
Which also currently rely on one single type… a signal type.
Real batch, and they are… the, the… The… the signal type putter is another one.
So we, we have to deal with this kind of, existing, Components that, deal with this, fundamental property, and see how we could make them supporting multiple… a mixture of, signals.
**Josh MacDonald** 41:23 Great. Yes, I totally agree, both of those points. I think we could probably find reasonable solutions, maybe add codec support and so on. But, yeah, that's a long-term one.
**Laurent Quérel** 41:35 Yeah.
**Josh MacDonald** 41:40 So we've spoken enough about my issue, I just want to, like, show these two more links that I put. There are two draft PRs, one where I sketched out how NetTracev6 could be passed through the pipeline, by turning it into 14 Arrow tables.
And that includes all the metrics, all the logs, all the spans, and all the profiles, and a couple more tables. And then I also kind of following the same design, but much, much simpler. I sketched out a prototype that takes this one collect library that we're using for our ETW receivers and user events, and instead just uses it directly to get stack trace information, and then layers it on top of OTLP logs with an extension using this pluggable extension concept that we've just talked about, but for Arrow records. So you get Arrow records that have tables with stack traces in them, which is a dream of mine coming true. So I just wanted to share that.
Nothing more to see there. I also have the next issue here, but, this is just an epic to cover a bunch of work that we've seen. My RFC number 0004.
So, I will begin writing sub-issues. I put about 8, roughly speaking, that need more detail here as I begin to work on the RFC. And I should have one coming very soon.
I don't think we need to discuss that.
Here we are at,
**Laurent Quérel** 43:11 Oh, yes.
So the next two ones, are… Resulting from the same… work I'm doing these days on the ClickIOUS Exporter.
So, in this PKIOS Exporter, we… I was mostly working on performance, improvement.
But I, along the way, I also discovered some missing, important missing aspects, like the… the lack of act-like management.
Into the existing ClickIO exporter, so, That… Also, convinced me that we have some, design… not design issue, we have, implementation issues, I should say, here and there regarding the way that we, we deal with ACNAC. One in the OTAP Exporter.
Mostly related to, corner cases, related to that live reconfiguration.
So that I just, Tracked those discoveries, and that's what we see.
The Dern OTAP exporter stream before the Chad Dern Line is an example.
And, the other one was, if you go back to the, to the list.
The other one, is, Yeah, keep drain receivers alive for late-act NAC completion. Same kind of, Situation, where we… right now, we don't behave exactly like we should.
**Josh MacDonald** 44:53 Alright.
I think we can accept those. I haven't updated all of these, but let's come back to that. Here we have one, again, with, submitted by Brian, and I read through it earlier today. I'd like to discuss.
Brian, would you like me to introduce this?
**Brian Sapozhnikov** 45:15 I can probably go quickly, the Kafka receiver currently emits metrics for, consumer lag per partition meaned, so, a single metric, that's the average of the lag in each partition.
Just from an observability point of view, it seems like it would be nice if we could support, having that metric emitted per partition.
that brings in a cardinality concern, which is why in this issue I was proposing maybe some kind of limit, that would be applied to it. My goal is not to have the limit, my goal is to have the per partition, but I don't know what the best way to do that, would be.
Given the cardinality constraints, so that's why I have the proposal here.
**Laurent Quérel** 46:02 That's an interesting, problem. I mean, not saying that it's, I definitively see the… The need for it.
It's just, that's something that we can easily represent with the existing instrumentation mechanism.
**Josh MacDonald** 46:25 I have a proposal on this topic.
I feel… I'm thankful to Brian for, like, raising one of my most nerdy interests here. So… So I… this… I wrote this fairly long comment, and I know we're almost gonna run out of time here, so I'll try and briefly summarize it. But, so… so the idea here is that you have this… this count that is representing the current number of un… unprocessed items in your receiver. So it's a difference that was summarized. There's this max function in there, but it's basically one number minus another. So it can be represented by a gauge, and I'm going to go with that for now. So the gauge says this is the current number of outstanding requests per partition and topic.
And if it weren't for this limit on cardinality, there would be a fairly straightforward answer here, which is to say, it's a gauge, you have one of them per partition topic, we're going to output one time series per partition topic, and that's just fine, it's a simple number.
And the problem is, when you get to that limit.
And so, many of you may know that I spend a little bit of time, leading the sampling SIG in OpenTelemetry. I've always been interested in this topic, so now I'm going to try and sell you a sampling algorithm.
And this is, So, the lengthy explanation is that since each of these numbers that we are recording through these metrics are ratios, that we can use weighted sampling. So, the concept of using weighted sampling allows us to replace the number Which is that lag metric with a weighted number, which represents the population expected value, and that would be a way that we could, inside of the SDK, re-aggregate metric sets to a limited number. I also proposed that the metric set values would be placed literally inside some data structure that's owned by the receiver. So if you have physically a certain number of partitions, you're going to have physically a certain number of metric sets, you would report them all, and then the SDK would say, I'm over my limit, I'm going to downsample them, and it would output a fixed number of metrics. That's the story I wanted to sell you, and now I'll let someone else speak, Laurent?
**Laurent Quérel** 48:57 Yeah, Yeah, my problem was not necessarily related to… I mean, I understand what you want to do there.
It's nice.
I don't think it's solving my problem.
My problem is more about… How do we… represent partition ID.
And, and, my understanding from what Brian was mentioning, this partition ID will be some kind of attribute.
But unfortunately, right now, the framework that we have, I mean, unfortunately or fortunately.
The framework that we have is relatively strict.
When we do the measurement, we have to provide measurement-oriented attributes, and those attributes need to be bounded alums.
Where all the… the possible values are… Known a priori.
And that's not the case for the partition.
I mean, it could be a huge number.
It's not something that you will know during the… when you compile your system.
So, how do we represent today?
this concept of partition ID that is… will be… Configured totally differently from one system to another. Could be a huge number.
So that's why I'm… I'm skeptical on… How your approach will solve this issue.
**Josh MacDonald** 50:33 Got it. Yeah, something I had considered, I want to hear what Brian has to say.
**Brian Sapozhnikov** 50:41 Oh, I might be totally wrong here, but my vague understanding was, that bounded limitation is when you're adding the attribute, per item, like, when you're actually emitting the metric. There's a separate way of adding attributes declared, earlier?
**Laurent Quérel** 50:59 That's great.
**Brian Sapozhnikov** 50:59 registration time.
So my thinking here was, we would declare the attributes when we have the reg… when we set up the consumer, and then if there's rebalancing, then we can.
**Laurent Quérel** 51:12 Oh, that's a nice… yeah, I agree with that. Yeah, that could be a nice way to… to serve this, this issue, I agree.
So, not reporting it during the measurements, but reporting it during the registration.
**Josh MacDonald** 51:28 Yeah, and I was thinking about an entity key, and I think there's probably a few unresolved issues here, but I was imagining that for each topic, or partition topic, that you physically hold in memory, there's some registered thing, which I was thinking of as an entity key that would name the topic and the partition, so that… so that then, when you're emitting your lag metric, you're just filling in one integer. But I realized that all of the pieces of my story didn't add up, because I was… pretending that I would be aggregating metric sets.
And really what we're doing is aggregating metric sets across different scopes defined by different entity keys, and the thing that you're sampling over is actually the entity keys, which are the partition topic identifiers.
That's to say there's some work to do, I understand your concern, and registration was the answer I was thinking of as well.
**Laurent Quérel** 52:28 Yeah, so that's the good news. I think we have a solution.
**Josh MacDonald** 52:32 It's a little complicated, but I'd be happy to work on this, at least the mechanics of the metrics we're all going to have to review, but the sampling part is something that I'm fairly glad to help with.
I hope that.
**Brian Sapozhnikov** 52:50 So, if I understood you right, Josh, you're saying, essentially, each individual processor no longer needs to deal with the cardinality concern, and the infrastructure aggregates… re-aggregates where needed to take away that concern?
**Josh MacDonald** 53:04 Yeah, and the key, the property that I'm relying on is that, like, in a standard, like, open telemetry metrics SDK scenario, you might have to just face, like, arbitrary cardinality coming from, like, the user, but this is the case where we're modeling as asynchronous instruments, and so for every… metric that you intend to report, you also have a big piece of memory being used somewhere, so that there's no, like, extra memory being used just by the metric SDK to keep track of the cardinality in all the metric sets, because you have some real object that's keeping track of those partition topics. And so, for each of your real partition topic objects in memory, you're going to store one little metric set.
you'll report all the metric sets, and then the metric SDK takes care of When it needs to, reducing that down to a reasonable number.
**Laurent Quérel** 53:57 Yeah, and this kind of thing will happen in the ITS system, right? Right, right.
this.
**Josh MacDonald** 54:05 Alright, I would be glad to help work through that. I love this problem.
Great.
**Laurent Quérel** 54:11 Yeah, and do you think that, That's, that would be a good exercise, and the reason why we have ITS that is, in fact.
our own engine is… one of the reasons is, if we do something for ITS, can we apply it to regular pipelines? So, what you just exposed, cardiology reduction.
Let's say that you are implementing a processor to do that.
Joshua, will you be able to do that at scale for a regular metric-oriented pipeline.
**Josh MacDonald** 54:49 I think the answer is yes. If you put them in one message, we should be able to do that, and I would accept that as a challenge.
**Laurent Quérel** 54:58 Okay.
I mean, it's nice, because it's a good example of why I think it's great to have the This pipeline engine everywhere, including for internal, because what we… sometimes we do for the internal, if we can apply it For the regular pipelines, it's a win, and the opposite is also true.
**Josh MacDonald** 55:24 Yeah, I like the idea. So, so the only trick is that then you're talking about doing some algorithm instead of on these objects, which we have bespoke built for ourselves for logging with, or for metricing with. Now we're handling OTAP, which makes it a little bit more difficult, but as you say, like, magnifies the benefit as well. So yeah, putting this… we're gonna call it the asynchronous sum downsampling logic into a processor. I could see that working out, yes.
**Laurent Quérel** 55:54 Yeah, we could do that in two steps. We could do the… the E-ZPass first, that could be integrated into the internal telemetry receiver.
That will simplify the… that means that you will not have to deal with, with OTAP.
And, you could just reason about the internal representation, and then… If that helps, and then a single step could be remove this logic, make the required adaptation.
And create a processor that will do this, Sampling mechanism.
**Josh MacDonald** 56:32 Yeah.
**Laurent Quérel** 56:32 This is all.
**Josh MacDonald** 56:33 when we actually reach that point, it will become clear that we could also use a gauge histogram in OpenTelemetry, because the other aggregation you could use over all these lag values is not to sample out and keep the top most heavy values, for example, but just simply to produce a distribution of lag values, which would be called a gauge histogram, and that's an obstacle in open telemetry.
**Laurent Quérel** 57:00 You want to introduce all the ideas that you.
**Josh MacDonald** 57:03 This one issue triggered them all, that's why I love it so much. Thank you.
**Laurent Quérel** 57:09 Okay.
**Josh MacDonald** 57:11 clear.
Yeah, okay, moving on, We have a couple more minutes and a couple… and it looks like we actually covered all the issues. That was an entire meeting spent on needs discovery.
**Laurent Quérel** 57:25 We have the stale list. Can you just maybe open this one? Yeah, I think we have only one.
Otab, gRPC, it's for you!
**Josh MacDonald** 57:35 And there's also an open PR for it.
No.
**Laurent Quérel** 57:39 Okay.
**Josh MacDonald** 57:40 Oh, there's… Utkarsh has one open about something else. Let's, talk to Jitender. I see your hand up.
**Jitender Bisht** 57:48 Hey, hi, everybody, thanks a lot. I have a question regarding, I… should we raise up an issue regarding the database receiver we've been discussing internally, right here, so that at least we can discuss in this forum?
**Josh MacDonald** 58:05 Yeah, let's see. So, Drew, I think you had advised on this already. The idea would be to file an issue along the lines of the ones we just looked at.
With similar content to the design document that you shared internally.
**Jitender Bisht** 58:22 Okay, okay. So, we can do the follow-up, in the next meeting, like, is this something we've scheduled for weekly, or we have some…
**Josh MacDonald** 58:32 every other week in this time slot, and then we do a Thursday morning on the opposite weeks. In this case, since we have a few minutes, a couple minutes, maybe, I would say that last week we discussed how connected this is with the file log receiver and the need to maintain state, so that when you're pulling from an append-only source, you don't replay a bunch of old data. So there's definitely a common interest here between The database and the file log, so when you record your issue, we can Bring that discussion back and see what else people had to say.
**Jitender Bisht** 59:03 Okay, okay, that sounds… makes sense. Sure. We'll… we can follow up in the next meeting.
**Josh MacDonald** 59:12 Alright…
**Laurent Quérel** 59:13 Right?
**Josh MacDonald** 59:15 Well, we made it to the end of another hour.
I think, I thank you all for coming.
And… last words.
**Laurent Quérel** 59:31 They surely wouldn't.
**Josh MacDonald** 59:32 Alright, thanks very much, see you next time.
**Jitender Bisht** 59:34 Thanks for meeting everyone.
**Albert Lockett** 59:35 Bye, everybody.
**Brian Sapozhnikov** 59:38 Thanks so much, everyone.
