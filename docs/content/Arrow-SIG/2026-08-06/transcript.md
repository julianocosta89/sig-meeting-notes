SIG: Arrow SIG
Date: 2026-08-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Laurent Quérel 00:00:55 Anyone?
Drew Relmas 00:01:00 Hello, good morning.
Laurent Quérel 00:01:03 annoying, no.
Okay, so…
Albert Lockett 00:01:12 Yes.
Laurent Quérel 00:01:20 Did you see my screen?
Albert Lockett 00:01:23 Yep.
Laurent Quérel 00:01:26 Great.
So, I invite you to add, Your name into the attendees list.
And add also a topic to the agenda, if you have any.
On my side, I don't have a specific topic today.
Okay, so let's see… So this is the list of, new… Issue.
Let me check what we have today in the… In the meeting, yeah.
Okay.
Okay, let's start with this one. Add optional live EAP profiling in PPROF format. Lalit, I think Lalit is not with us right now.
I'm cheating because we… we have, oh, Albert with us.
Albert Lockett 00:03:05 Yeah, I'm here, what I was gonna say is, I am pretty sure we have a… PR, open for this, so I think Mia, Lala might have had the same idea, Let me find a PR number.
Laurent Quérel 00:03:23 Yeah, that's exactly the one that you…
Albert Lockett 00:03:25 Yeah, the reason I haven't marked the PR, ready for review is because I was going to try to do some, It's PR number 3497.
I was gonna try and do some performance testing to try to figure out, okay, so if we, If we, have this, or 3497.
3, 3297.
Laurent Quérel 00:03:57 Sorry, I don't understand. 3…
Albert Lockett 00:04:02 Lockett nous cette.
Laurent Quérel 00:04:06 Okay, no, I'm a little bit slow.
Albert Lockett 00:04:08 I don't know.
Laurent Quérel 00:04:11 Yes.
Albert Lockett 00:04:12 So, the reason I haven't marked this one ready for review is because it, like, I just want to do some performance testing to figure out, like, okay, if we have this, like, profiling enabled, like, is there any overhead? So, I'm actually working on doing that performance testing this morning, but… Yeah, so I think, I don't…
Laurent Quérel 00:04:30 Let's say that, this one is, Yeah, covered by this PR.
Okay.
And obviously, We cannot do that.
Great.
COVID use native exponential histogram Support. I think, Josh is with us.
Joshua MacDonald (Microsoft) 00:05:08 Hi, yeah, so I've merged a large PR with, like, the very beginnings of exponential histogram support, and it has just, like, a bunch of leftovers that I didn't want to do in the same PR, and are available. They're not all urgent. Actually, none of them are. So they're there, and we can run through them.
Prometheus has a slightly different encoding for the same type of data. They're fully compatible, it just requires a conversion.
One uses sparse, one uses dense, and there's an off-by-one. It's a terrible situation. Long story.
I won't say more.
Laurent Quérel 00:05:44 Okay, okay, okay, and… Do you have, an issue to track the fact that we need now to use histogram into the existing codebase?
Because I'm too low…
Joshua MacDonald (Microsoft) 00:06:00 There are five issues, one of them covered.
Laurent Quérel 00:06:02 Oh, okay, so there is one for that. Okay, perfect.
Joshua MacDonald (Microsoft) 00:06:05 Yeah.
Laurent Quérel 00:06:06 Great.
Yeah, so, so, that was the, the, the last important, missing piece.
In the internal implementation for the project. That's super cool to have this along. Thank you.
Joshua MacDonald (Microsoft) 00:06:25 So let me run through the others there, then, since we're here. The new implementation uses a table lookup, it's exact, there's a related specification PR that I wanted to put together for a long time, so I did that. So this… the ability to generate a table at compile time is there, but it's not implemented. I've seen the… I've written the generator, it's in another repo, it's prototyped, just needs to build mechanics.
And I don't know that's that important. So right now, the default is a table scale of 8, so… It gives you less than 1% relative error, and then if you want to get even finer, we could set it to 10 or 12, you know, just add space and, tiny little bit of extra compute.
So the two that, the next two are… tuning considerations, and this is the fact… the data structure is variable size, but it needs to be fixed, like, when you actually use it. So, right now, I've encoded a 10-word and a 26-word variant, but they're not being used anywhere. Moreover, there's, like, fine settings that you can make, and I wrote a little bit about why you might do that here.
There's no control there, so right now, it's… it's, There's no configuration yet.
So control over size, and then limiting si… limiting scale and width are secondary considerations.
So, nothing too important there. The last one is the one that I think you asked me about just now, which is… Right now, we have, these data types. One is called MMSC, one is called exponential Histogram NN, meaning non-negative.
And… and the choice of MMSC versus non-negative histogram is not made right now. It's… it's… you would have to choose in code which one you want.
And I think a nice… a nicer arrangement would be to have a choice that the user gets. Like, I want to pay more, so I'll get histograms, I want to pay less, so I'll get NMSC, meaning it should be, like, a configuration choice somehow.
And we've talked about, like, how views could be done statically, so that you could just, like.
build the code saying, I want to have NMSC and a choice of histograms, and then at runtime, you could choose them, you could vary the sizes at compile time, like, so there's lots of options there, but having control over the instruments is not yet there.
And so if you're looking.
Laurent Quérel 00:08:46 You'll.
Joshua MacDonald (Microsoft) 00:08:47 find two instances, it's the traffic generator has these histograms installed, that's it.
Laurent Quérel 00:08:53 Luke it.
Yeah, the good candidates could be the… For example, in the processor, the duration.
Joshua MacDonald (Microsoft) 00:09:05 Yeah.
Laurent Quérel 00:09:05 For the situation, we could imagine, Also, the… Don't let them see introduced, so the time passed into the channel.
This kind of stuff.
Okay, is it considered compatible? So, you were saying we could move from MMSC to… Non-negative histogram.
with a symmetric name. Is it something that, we… We stay, in line with the… OpenTelemetry recommendation with that.
Joshua MacDonald (Microsoft) 00:09:46 That is a gray area, I think, at best.
I would say we're not crossing the line. Switching between histograms is not necessarily ruled out.
when you choose the instrument in histogram… like, the OpenTelemetry wants to talk about semantic conventions for what instrument choice you make, and histograms and MMC are the same type of instrument, they're just different resolutions and expressions, different aggregations, so… Yeah.
But… but real metric systems would probably not like it if you began switching between MMSC and exponential histogram. Now, there was a fine point there. The MMSC doesn't have a native type in OPTEL metrics, so what we usually do is express it as a histogram with no buckets.
And in the review, someone flagged that, and I felt like accommodating it a little bit. So, right now, if you use MMSC, you get an explicit bucket histogram, so it will say, I'm an explicit bucket histogram with no boundaries.
just min, max, sum, and count. And then when you switch to the exponential or the non-negative histogram, you'll switch to the exponential histogram point. So you'll see two different types of histogram, one for MMSC and one for exponential histogram. And whether you support that or not, at least semantically, they're compatible.
Laurent Quérel 00:11:17 Okay.
Okay, yeah.
Joshua MacDonald (Microsoft) 00:11:21 similar to…
Laurent Quérel 00:11:21 Commission, for example.
Joshua MacDonald (Microsoft) 00:11:23 I don't know that we should go too in-depth, but, like, if you're using delta temporality, or if you're using cumulative temporality, differences emerge.
Because of the use of resolution. So if you have a delta temporality, and for one period, something blows out your distribution, like you have a very, very long latency, it's going to reduce the scale of the measurement. Now, if you're aggregating reduced-scale measurements over long periods of time, the only correct solution is to reduce the scale of the entire timeline.
Which means that if you're doing cumulative, eventually your histogram is going to fall in resolution. Now, if you choose delta temporality, what you can do is just let it blow it out, or you can… make a gap. Like, here… here, my histogram was blown out. I'm not gonna tell you anything. I'd rather… I'd rather make a gap than reduce resolution, for example. Those are variables.
We can talk about that.
Laurent Quérel 00:12:14 Okay.
Great, thank you.
Okay, back to this one. Add authentication and TLS to the admin HTTP server. Yeah, this one is definitively, almost too well.
Ideally, if we can reuse… Yeah, that's not necessary… at least at the crate level, not necessarily at the extension level, but to reuse the… authentication mechanism that we, we start to support, through the extension.
Not saying that we have to use extension in this specific case, but at least that we can… I don't know that's something we need to… to define.
We can reuse the code that has been used by those extensions.
Joshua MacDonald (Microsoft) 00:13:10 I suspect you'll want a different extension interface, but the same extension.
Laurent Quérel 00:13:14 Yeah, a different kid.
Joshua MacDonald (Microsoft) 00:13:15 ability.
Laurent Quérel 00:13:15 Yeah, for this one, definitely, because they don't belong to the NUD extensions.
Yeah.
Do we have a… Sometime today.
Is this… Anything to add?
Okay. Anyway, it's an important, desk?
A durable idempotency key is to pee data.
I will be interested by understanding This one, do we have Mike?
Sit in with us.
Joshua MacDonald (Microsoft) 00:13:58 I can speak to this one. I updated it yesterday. So, there's a history in OpenTelemetry of asking for item potency keys, and if you chase the links, you'll find that I was involved in the history. My old employer wanted exactly what we're talking about here, so I tried to propose it a couple times. It got rejected, and I… Have some thinking about that now. So the idea of an idempotency key is that you want to put some sort of unique identifier on each request, so that when it gets replayed, for example, through the durable buffer processor, that you are able to identify, oh, I've already seen this request, it succeeded, I don't want to duplicate it.
It's counts or whatever. So, so the typical place that you want to put in this idempotency key is right before durable storage, and that was exactly what my old… my old employer wanted as well.
And the way that this was proposed by this fellow, would be to add a UUID7, so that's 16 bytes, I think, of randomness, or not quite all randomness, to the context.
And I want to push back a little bit, but I think I have an idea here. And the pushback is that, you know, this is a feature that will cost something, and if users don't really want it, I think we should not need it.
so that this should be sort of something you choose to do, because you know you need it. And that means you would be able to configure it.
So, stepping back just a little bit, I've got this open proposal. I'm not prepared to really talk about it in depth today for multi-tenant support, and what that's been moving towards is just really specifying how we control context propagation at a fine grain, and how we use context for conditional behavior. This looks like just another piece of request context that we might be able to inject using the multi-tenant features and these extractors that we're talking about. So right now, I've talked about extractors to pull in a transport header and make it into some sort of key value.
I would like to say that there's an item potency key I should just be able to synthesize right on site whenever I need it. So the definition of a tenant token would be able to incorporate an item potency key.
and then be very explicitly manual throughout the pipeline. That's what I would propose for this, and I've said as much, I think, on the… actually, maybe didn't say that yet on the issue, but I was working up to it.
This would make an example for multi-tenancy.
Laurent Quérel 00:16:24 Thank you.
But, do we have to inject this impotency key At the receiver level, or,
Joshua MacDonald (Microsoft) 00:16:37 Could be a…
Laurent Quérel 00:16:37 And where…
Joshua MacDonald (Microsoft) 00:16:38 Kind of durable.
Laurent Quérel 00:16:39 where…
Joshua MacDonald (Microsoft) 00:16:39 buffer processor.
Laurent Quérel 00:16:43 Okay.
Okay, okay. And, yeah, for example, for the Kafka… Exporter, we will do the same thing.
What I'm trying to figure out is, is it… a spatial processor? Is it something that we have to replicate in different locations? We… we try to be, to, to follow a more composable approach.
when that makes sense. I'm just trying to determine if this specific case This specific, capability is in the comp of the… Composability or not.
Joshua MacDonald (Microsoft) 00:17:29 I see what you mean. The way I've been thinking about it, still work to do, is that each component that has a… I don't know the right word yet, but some components ignore context, they just pass through, but some components are going to intercept context and create new ones, like batch processor is an example. But topic exporter and topic receiver, there's a… there's a context traveling across the wire there.
So there are, and I think there are more, so transform processor, I believe, will create new outputs.
And so, what I believe is that there are a subset of our nodes which do create context. It's all the receivers, but some of the processors as well. And then, there should be a standard configuration model.
for nodes which receive context and do something, and then nodes which export context and do something. And so, a durable buffer processor would just be an example of a complex processor that receives context, maybe injects a potency key there, writes it to disk, pulls it out, and then pushes out a new context.
So that there would be standard configuration structs that many of these nodes have.
For the intercepting and modifying and exporting of context.
Laurent Quérel 00:18:45 Yeah, I'm thinking maybe a third option.
That could be, a policy-based approach.
where we… For every node,
Joshua MacDonald (Microsoft) 00:18:57 Oh, it's in the policies area, for sure.
Laurent Quérel 00:19:00 Yeah, and we could… yes, and we could imagine some, Policies that are applied before the reception of a PDATA message by a processor or by an exporter.
And we could basically express directly in the policy section of the corresponding node, or I'd like to ensure that we have this hidden potency key.
And automatically, the engine will inject it if it's not already there.
That could be a life watch.
Joshua MacDonald (Microsoft) 00:19:40 E.
Laurent Quérel 00:19:40 I take that.
Joshua MacDonald (Microsoft) 00:19:42 Yeah, I've seen that as well. Let's keep talking about that.
Laurent Quérel 00:19:47 Yeah.
Okay. Just taking… making an adding a notice here.
Joshua MacDonald (Microsoft) 00:20:21 So you can see that I wrote something already on the issue.
Laurent Quérel 00:20:24 Oh, okay.
Yeah, yeah.
Joshua MacDonald (Microsoft) 00:20:27 But go ahead with what you're saying, too.
Laurent Quérel 00:20:29 Yeah.
Joshua MacDonald (Microsoft) 00:20:29 as… pardon.
Laurent Quérel 00:20:30 this hidden potency… Dude.
Joshua MacDonald (Microsoft) 00:20:50 this concept that you just stated is one that I crossed over in my head yesterday. Like, the idea that certain properties of the tenant token are dictated by the downstream use, so if you have a user downstream who expects an ideopotency key token, then you must produce it, and then we can check the configuration.
Or we can just automatically fix it when it arrives at that node. I'll work on that.
Laurent Quérel 00:21:16 Yeah. Yeah, yeah. Like, pre- and post, action.
Joshua MacDonald (Microsoft) 00:21:22 Yeah, and in my current prototypes, I have these properties called bag and retain, and I don't like the names of either of those, but one is saying, I'm going to extract this key later, but it could be inferred automatically, I think. And then the other, so anyway, the point is, we can refer quite a lot about the graph of tenant token usage, and I'll look at that.
Laurent Quérel 00:21:40 Yeah.
Okay, great.
So did I create naming convention, too?
Drew Relmas 00:21:51 I guess if you scroll down, I'm curious who… Mark just says, needs discussion again. Oh, it was Tom.
Okay.
We need to just, pick something and do it, instead.
Laurent Quérel 00:22:06 Yeah. Continuing to talk about it.
Drew Relmas 00:22:08 about it.
Laurent Quérel 00:22:08 We renamed recently the project, Hotel Arrow, Dataflow Engine.
Drew Relmas 00:22:18 These are…
Laurent Quérel 00:22:19 So I think that we have to align the prefix, with that.
So, what about hotel?
Pierlong, that's the problem. Hotel dash Arrow dash…
Drew Relmas 00:22:41 Branch to a light bulb panel.
Joshua MacDonald (Microsoft) 00:22:43 Hotel-DFE.
Drew Relmas 00:22:45 Yeah, we could do that, hotel dash Arrow dash…
Joshua MacDonald (Microsoft) 00:22:50 It starts getting long when you add hotel and Arrow and DFE.
Laurent Quérel 00:22:59 Looks how Arrow is.
Joshua MacDonald (Microsoft) 00:23:01 the most recognizable name associated with this project, I would say.
Laurent Quérel 00:23:06 hotel room?
Like that?
Or, I'm just, writing it so everyone, Tel Arrow DFE, that's another, another option… And the last one that has been mentioned is DFE directly, that's… So we basically have a choice between those three.
Kennedy Bushnell 00:23:31 These are just prefixes, right?
Laurent Quérel 00:23:34 Sewing?
Kennedy Bushnell 00:23:35 These are prefixes.
Correct? Yes.
Laurent Quérel 00:23:38 Proceeds, yeah, yeah, yeah.
Drew Relmas 00:23:39 prefixes.
Kennedy Bushnell 00:23:41 Can we play with, like, what we think the longest crate name is? I think staying under 64 characters is the recommendation.
Laurent Quérel 00:23:48 Oh, that's a good point.
I don't know, let's see, and it's like…
Drew Relmas 00:23:55 Telemetry macros, maybe?
Laurent Quérel 00:23:58 Yeah, probably. Did you check?
Drew Relmas 00:24:01 Off the top of my head, it's telemetry macros, but… No, that's true.
Laurent Quérel 00:24:08 Beside the top of my head.
Yeah, it's definitively, I guess, under the, yeah, the 64.
Kennedy Bushnell 00:24:16 Yeah, that's… That looks well under that.
Laurent Quérel 00:24:20 Yeah.
Drew Relmas 00:24:25 We have component inventory syntax.
And Query Engine Playground.
query engine languages.
Laurent Quérel 00:24:36 I think, so components, inventory, syntax.
Drew Relmas 00:24:42 Inventory syntax.
Laurent Quérel 00:24:46 Whoa.
How much? Let's see, I'll take care… Les details.
Kennedy Bushnell 00:24:56 I know this is straw man, but, like, comp for a component would be totally readable, too.
Like, if we needed to, for lunch.
Laurent Quérel 00:25:05 Yeah, yeah.
Kennedy Bushnell 00:25:05 So that's not a terrible one, but, like, I think it would even still work with components, so… Hotel Arrow DFE, Looks…
Laurent Quérel 00:25:14 Is your preference?
Kennedy Bushnell 00:25:16 me, I think so… I think so.
It says all the things we want it to.
Laurent Quérel 00:25:21 Yeah.
I'm okay with that.
Drew Relmas 00:25:26 R.
Laurent Quérel 00:25:27 And, and for people that know Ten Arrow as it is today.
Drew Relmas 00:25:31 Okay.
Laurent Quérel 00:25:31 So… We are fine with that.
Joshua MacDonald (Microsoft) 00:25:38 Which one did we find with?
Drew Relmas 00:25:40 I guess.
Laurent Quérel 00:25:41 We cannot…
Drew Relmas 00:25:41 Everyone in this call can race.
Laurent Quérel 00:25:43 This, this prefix, the one that is fully explicit.
That's okay, Joshua?
Joshua MacDonald (Microsoft) 00:25:52 Tear with me, yeah.
Interesting.
Drew Relmas 00:25:55 sprinkle and optional panels right about here.
Laurent Quérel 00:25:59 Okay…
Drew Relmas 00:26:00 Let's not all jump to make the PR at the same time.
Kennedy Bushnell 00:26:09 It's a gig.
Laurent Quérel 00:26:09 Agreed.
Kennedy Bushnell 00:26:10 Somebody.
Laurent Quérel 00:26:11 Yeah. So, this one is done, and I think that's, definitively.
Drew Relmas 00:26:18 first person…
Laurent Quérel 00:26:18 Dude.
Good.
Drew Relmas 00:26:23 First person to comment gets it.
Laurent Quérel 00:26:31 I'm not part of the… Okay, remove legacy PDATA component matrix, yeah, this one… It's… it's part of the effort of,
Drew Relmas 00:26:44 Yeah, this probably… Yeah, sorry, I think I have some audio delay, I'll keep going. This is probably something we don't need to spend too much time on. I think, Laurent from other PRs that we've been looking at, I think you're fine removing .p data. Because a lot of our metrics about messages and items passing through the engine.
happen at the channel level now. There's not really a point in keeping .pdata on the node-specific metric sets, just because we really should only be using those to talk about node behavior itself, which isn't tied to the internals of the data representation. So, that was my thing, if ever… I'm assuming we're all pretty much on board with this, and it'll just be a cleanup effort to get rid of P data everywhere we see it.
Laurent Quérel 00:27:40 Yup.
And, yeah, it makes total sense for me, and just for the context.
I think this… I just want to… Show again, I think that's… oh, no, that's not the one. That's probably this one.
I was looking for, yes. We have this, gitHub issue, maintain.
created by Drew, which basically enumerates all the… The nodes extension also are included for… not sure.
No, extension outlet.
Drew Relmas 00:28:14 So that…
Laurent Quérel 00:28:14 Okay.
Drew Relmas 00:28:15 Maybe I'm missing extensions, okay.
Laurent Quérel 00:28:18 Hey, that's right.
That's strange, because I remember seeing it, but probably I totally… I'm transferring into an LLM now. So, yeah, so the… we have a lot already covered, we still have a few processors here and there, and core exporter, receiver in general, and exporters, so it's making a lot of progress.
Don't hesitate to participate if you are interested by improving the quality.
Drew Relmas 00:28:51 There are…
Laurent Quérel 00:28:52 And, the consistency of the internal metrics.
System. Okay, so this one is done, Structured Security Repo RMS for DFNG. Siju.
to AFC Joe this morning.
Joshua MacDonald (Microsoft) 00:29:10 Hmm.
We don't.
Laurent Quérel 00:29:12 Hmm.
Okay.
So let's read it. Anyone know this one?
Joshua MacDonald (Microsoft) 00:29:21 No.
Laurent Quérel 00:29:24 Okay. Hotel repo are seeing more low-signal CV report, scanner, AIG, speculation, blah blah blah.
Yes.
Make it cheap for a reporter to demonstrate a real bug, and cheap from a robot later to replay that demonstration again.
Kennedy Bushnell 00:30:00 It is a cool idea.
Laurent Quérel 00:30:02 Yeah, I think it's, I think we can keep it, mid-discussion.
And hopefully we will have SIGO maybe next week.
That would be nice, To create a special topic for that.
Maybe we can, send a message to SIGO, to check with him if it's possible.
To join the meeting next Tuesday.
4PM… And have him, adding him to… Yeah, to discuss about that.
Joshua MacDonald (Microsoft) 00:30:43 I agree. This looks like a good idea, we need a little bit more description.
Laurent Quérel 00:30:47 Yeah.
Okay, and the famous, Hotel Arrow Festury. So we, we did some, we had some discussion yesterday among the, the maintainer.
We definitely need to refine this list.
And this list will be communicated to the governance committee.
We just need to make sure that we don't have anything in this list that is, Yeah, we will, we will, make sure that this list is compatible with, This idea of, getting the review and the approval from the guidance committee.
Is there… so, I… no, there is no specific, so, what I will ask is… for people interested by the definition of this Phase 3, if you have strong requirement.
That are not represented here, to add maybe a comment here, and then we will, Discuss that, soon.
And we will publish this list to the governance committee.
So I stay… I keep this, this one still open.
the discussion.
Great. So the next is about the stale.
GitHub issue. OTAP gRPC propagates error status code.
Joshua MacDonald (Microsoft) 00:32:30 I think we did some… little bit of work on this.
Albert Lockett 00:32:34 Yeah.
Laurent Quérel 00:32:35 Yeah, I think so.
Albert Lockett 00:32:37 I… I thought we… Dude, I thought this was done.
Try… I'll try to find them.
PR…
Joshua MacDonald (Microsoft) 00:32:45 the way that issues stated it's about propagating error code. Like, gRPC… exporter receives an error code, and then it propagates backwards. I don't know if that's necessary.
been discussed in the Go Collector as well.
Laurent Quérel 00:33:02 Okay, so I, I, Albert, I'll let you, maybe, just double-check what we did, and add, the corresponding gitad, PL?
Albert Lockett 00:33:13 Yeah, sure. And I might have been thinking about something else. I was thinking, correcting the retry behavior based on the GRPC status code, but I'll,
Laurent Quérel 00:33:22 Oh, okay.
Albert Lockett 00:33:24 I think I was mistaken.
Laurent Quérel 00:33:27 Okay, so I'll let this one stand.
And, and next week, either we close, or we remove the stair, depending on the result.
Consolidated back-off configuration, handling, and implementation.
Joshua MacDonald (Microsoft) 00:33:50 As I recall, there were a couple of different exponential back-off configurations in our configuration model across the repository.
And the Go Collector has a common library for that.
Laurent Quérel 00:34:03 Yeah, definitive is something we… At the minimum, we need to… To check the current situation.
Josh, are you okay to check that?
Or I can just keep this one open, and we,
Joshua MacDonald (Microsoft) 00:34:27 I'm okay to leave it.
open. I don't know that it's a great big problem. We can… like, we don't have priorities on these issues.
Laurent Quérel 00:34:35 Yeah.
Okay, so I removed the status for now. Processor do not have a start return.
Joshua MacDonald (Microsoft) 00:34:42 These are all mine, what is this all about?
This… this we can close. I think you've answered this a bunch of times. Why don't processors have start methods?
Laurent Quérel 00:34:54 I don't sell this one.
Joshua MacDonald (Microsoft) 00:34:55 I think you have.
Laurent Quérel 00:34:59 Yeah, when I saw that this morning, I was still, You know what? I will assign it, to me, because I need to think about this one a little bit more.
Joshua MacDonald (Microsoft) 00:35:17 Yeah, I can't remember what I concluded, it's been a while now.
Andres 00:35:30 What would be the use case for that one?
Laurent Quérel 00:35:34 So it's, it's, so right now, we, we have two places So a processor will have… A kind of elite method, because we… We have the option to, for example, register a matrix set into the creation phase of a processor.
And we have a process method.
Which received a message.
Process it and deliver one or several messages.
the question was, do we need, an intermediary method that will be… So, when the controller and the engine basically initialize the DAG, We… we have a creation phase.
Basically, we create all the nodes, then we have a connection phase, we connect those nodes with the values channel.
And, and once everything is done, we basically start, and we are ready to process messaging.
The question was, do we need, Basically a method to specify, okay, the… we are ready to start, and maybe you have something to do, before. I'm not sure that we really need that, because we already have these two Let's say, Ukpeted to, to act.
So that gives you a little bit more context why we had this question at some point.
Joshua MacDonald (Microsoft) 00:37:12 It has to do with getting your async runtime handed to you before you get processing requests, because you only get synchronous at start. That's what this is about for me, but I'm also… I'm still learning Rust, honestly. Kennedy?
Kennedy Bushnell 00:37:27 So, we already have the control channel, right? Is that plumbed in at this point? Because if it is, then we could just have a new message across that channel with a known, like, life cycle, where that happens before you start listening to other messages, or something like that.
And then not have to special case this, and then you could… Special case it within your… your own process.
Yeah. Whatever node you are.
Laurent Quérel 00:37:53 Yeah.
Joshua MacDonald (Microsoft) 00:37:55 So, a node control message to say, you're starting now.
Kennedy Bushnell 00:37:59 Yeah, and it's just known that you're gonna get that message type before… most other messages. Like, we could have certain… Life cycles of those message types.
Laurent Quérel 00:38:11 Yeah, I agree. Just adding,
Andres 00:38:29 I don't remember the code at this point of the processor itself, but… Does it not have, like, some sort of constructor of the struct, or something like that, where you pass… the configuration parameters.
Laurent Quérel 00:38:42 Yes, we have a constructor, and that's what I mentioned as a limit method, or a construction method, that's exactly that, yes.
Joshua MacDonald (Microsoft) 00:38:51 And it's called synchronously before the async runtime is handed to you. That's part of the question.
Laurent Quérel 00:38:59 Yeah, I think I also need to, To refresh my memory on the… maybe some detail around that. So, I will put, I will add in my to-do list, the fact of revisiting this, this issue, and, hopefully to discuss that, Next week.
Okay, I'll just need to take it somewhere else.
Okay, great. I think we are… No, we're still… oh, that's your day.
No, we already discussed this one, sorry, yeah, and scope attributes are pre-calculated, but not limited.
or recycled.
Joshua MacDonald (Microsoft) 00:40:09 Yeah, so… What I wrote is true. There's an unbounded memory structure, and I don't know that it will ever grow, but I want to know what Utkarsh wrote, and now I can't remember.
Utkarsh 00:40:35 Wait, too.
Yeah, could we check the original thing?
Laurent Quérel 00:40:42 So you probably have a comment… Okay, that's the one.
Joshua MacDonald (Microsoft) 00:40:58 If entity keys can be minted at runtime, then this eventually will run out of space. That's… that's the key.
Utkarsh 00:41:14 Yeah, I think… I don't remember.
Joshua MacDonald (Microsoft) 00:41:16 It feels like a really minor issue at this point.
Utkarsh 00:41:18 But yeah, it was just mostly that, like, to get around the unbounded issue, I think the suggestion was just that cap the size of the capacity of the HashMap, don't exceed the… The targeted size, and… do the, like, you know, the brute force thing once the size is reached, otherwise just look up the hash map.
But…
Laurent Quérel 00:41:42 Yeah, I have the feeling that that will not be good enough, because the comment I put there live reconfiguration, Is really a thing, and For example, for a SIG, we will have, long-lived, instance of the data flowing gene.
With potentially a lot of reconfiguration.
So the, yeah, the number of nodes, to a specific identity will potentially be, be important, so we already need to have A cleanup, a clean-up, mechanism in place.
To make sure that, we are not just accumulating things.
So, for me, the fact that there is a cap The cap is not related to… at any point of time, we could have a maximum, but I agree. I don't think we need to use this maximum as a way to protect the system against an expansion without end.
We, we have… we need a cleanup method to, to be in place.
Otherwise, we will have some kind of memory leak in some form.
Stone…
Utkarsh 00:43:15 Yeah, so I think, like, before, like, when I committed, I haven't, I hadn't factored in the live configuration part, so… That time, the suggestion was just that we can avoid the cost of eviction. Any eviction algorithm will come with some complexities, so… If we know that the… If we… if we can assign a reasonable size, a reasonable bound for the hash mark capacity.
and we know that we won't exceed it, then we… most likely, for all the cases, we would be able to just have their entries in the hash map.
And if we, for some, pathological case, we start getting a lot of newer entities, we don't have to… we can still, not write stuff into the HashMap, but I think the other… but if you don't look it up from a hash map, you have to do more processing to get the same processed value out of it. But, yeah, it's a minor thing, I think.
Laurent Quérel 00:44:18 Yo…
Joshua MacDonald (Microsoft) 00:44:21 Why aren't the entity keys just carrying their own encoded scope, is one question.
Laurent Quérel 00:44:28 Yeah, I think we need to, I don't have everything in my mind right now to… anyway, to make a decision, I think, yeah, that's probably the same thing for the three of us.
Maybe we need to… Yeah, we need to look at that. It's probably not urgent, like you said, but that's something I think, I like to avoid any situation where we could have some form of memory leak, just because we… We didn't consider the level configuration as a common event.
In our case, it's a common… it could be a common event.
So, that means that this kind of, Bookkeeping, is, is a relatively fundamental.
So because it's more important for me, I think I will, Just, the…
Joshua MacDonald (Microsoft) 00:45:33 I'm gonna add a couple of related issues. One, Drew tried to fix something about dropping of entity attributes, and they're not formatting correctly, so somebody pointed out that, like, when you get an error message in the console logs, that the entity doesn't print correctly.
So it seems like there's a bunch of related work about Representation for entity keys, which are not… First class.
Drew Relmas 00:46:00 I'm dropping in the chat to the Zoom the issue you're talking about, Josh.
Joshua MacDonald (Microsoft) 00:46:07 Thank you.
Laurent Quérel 00:46:09 Okay, I will open it.
Where is my booking message?
Drew Relmas 00:46:19 It's, 3598.
Laurent Quérel 00:46:22 Yeah, opened.
Terminal pipeline errors can be dropped when the error enum is included as a debug field.
Drew Relmas 00:46:34 So, this was through, if you recall a few days back, there was a query engine filtering bug that I found, which resulted in a, like, pipeline runtime error, and it gave me a lot of trouble because the error cut off what was actually happening.
Laurent Quérel 00:46:55 Mmm.
Drew Relmas 00:46:56 All I got was pipeline terminated with a runtime error, and one dropped, meaning, like, it didn't give me the actual details I needed. So,
Joshua MacDonald (Microsoft) 00:47:07 So those… that one that Drew mentioned, and then the one that I linked, is also related to missing information in logs, and I connect them together.
Laurent Quérel 00:47:19 Okay.
Joshua MacDonald (Microsoft) 00:47:21 Right now, the entity key prints as its, like, interned, like, token value, so you see, like, 3 characters, which is my entity key, and it's meaningless.
And somebody ran into that when they were staring at Drew's issue, basically.
Laurent Quérel 00:47:40 Okay, looks like an important, bug to fix.
Okay, great. I think we… We can switch to the… The topics, okay, Stefan and Kennedy.
Does OTAP support unsigned 64-bit Bonsai… Stefan, can you maybe, Describe that a little bit more.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:48:09 Sure.
Laurent Quérel 00:48:10 So…
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:48:11 There was a discussion that came up in the hotel network SIG.
They're working on the semantic conventions for the network metrics.
And they're considering adding a whole load of, sort of new attributes and metrics.
And one of the questions that came up was in terms of the data types, and in particular on the network side, for high-throughput network interfaces, such as terabit interfaces.
Unsigned 64-bit counters are common.
And there wasn't any, kind of.
So, basically, I'm doing some discovery now to understand, the… the extent of support for unsigned 64-bit ints across different parts of the stack, including, sort of, backends, OTLP, OTAP, that kind of thing.
So far, what I've found is that, for the backend that I looked into, which is Prometheus.
They support only Float64.
So there is, definitely some loss there, and… One of the Prometheus maintainers told me that it would be several years for a new type to be added, with the most recently added type being the native histograms.
So in terms of that particular backend, that was a bit of a dead end, with the, sort of, highest range value being a float 64.
On the OTLP side, I spoke to some GC members, And… They said that the… I think the highest range value is assigned 64-bit integer.
So again, just as part of this information gathering, I thought I would ask on the Otal Arrow SIG, Just out of interest.
is, is there any kind of support for unsigned 64-bit ints here? It's not necessarily a feature request.
I'm just kind of out of interest again, just doing some information gathering.
it does look like we're going to have to look at some kind of alternative, you know, lower resolution, or maybe pre-calculated rate aggregations or something for these metrics. But again, just thought I'd ask the question, just so that I can kind of fill up the discussion on the, hotel network side.
Laurent Quérel 00:50:17 Okay, I guess multiple person will be interested to answer that.
I can provide a… Out of the response, So, right now, we are aligned with the OTHP specification, so we… Unfortunately, only support, int, sign int.
Fundamentally, there is nothing permitting us to support and sign it.
the problem will be… I mean, it would not be a big default, I think, because, And I guess it's about attributes, right? Oh, no, it's in the metric, metric part? Metric value?
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:50:59 Metric value, correct.
Laurent Quérel 00:51:02 Okay. Yeah, I don't think that will be, A complex thing to add, in the engine itself and in the protocol itself.
The problem will be, in my opinion, more on how the… this unsigned Metric value will arrive to the engine.
There is no, as far as I know, there is no, Client SDK supporting that.
You could imagine that, you… So… Then, the question will be, is this information will arrive to us as an OTLP message? In that case, the question is, how do we, make that happen, that we require to have some changes into the OTLP representation anyway.
and the client SDK? Or do you consider to have an OTAP client SDK, and and if we support it at the OTAP level.
I think that's a story that could work.
So, on my side, I don't see any problem, and I can understand why unsigned hits are important in this specific context.
I think we will have the same problem on our side.
But the question is, what kind of instrumentation and client SDK will you use into your specific context?
Because the product is not only at the particular level, it's, end-to-end.
Joshua MacDonald (Microsoft) 00:52:45 Yeah.
we have to… I think we have to raise this at the higher level in OpenTelemetry, like, as a spec-level issue, because the number data point doesn't have an unsigned value, and I could imagine, like, a convention where you stuff a 64-bit unsigned and assigned value and put a metadata annotation on it.
Because that's… otherwise, it's going to be, like, a version change to get new fields added to OpenTelemetry's protocol.
That sounds hard.
But I also have seen this issue come up, that floating points definitely not find enough resolution, and… People want unsigned.
Because it makes sense.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:53:24 Oh, okay, so it has actually come up in some discussion before then.
Joshua MacDonald (Microsoft) 00:53:29 Well, I just am familiar with it from my old… my old company, like, that was… like, they were aware that Floating Point was not universally good enough, they could see Prometheus was doing it that way, and, like, I'm just aware of it.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:53:42 Okay.
Well, no, that's, that's good to know. Thank you for the discussion. This is, some great info.
Laurent Quérel 00:53:49 And, Joshua, are you sure that that will be a new version? I mean, it's, for me, it's a minor modification into the protot.
Because if I remember well, there is, like, A one-off… For the, the value?
Which is either a float or an int.
So I'm not sure that, adding a new one of… a new… Additional variant to this one-off.
will… will make the existing, plant SDK and consumer of this, OTAP.
Protobuf, invalid.
I think it's a, it's a supported, additive modification.
Joshua MacDonald (Microsoft) 00:54:38 That's… I don't disagree, it's just a… pretty big one. Like, you need a minor version, at least. You need to tell people what to do when they receive this data that they haven't learned about yet.
Laurent Quérel 00:54:52 Hmm.
Joshua MacDonald (Microsoft) 00:54:53 And there's been this topic of, like, protocol negotiation. Like, wouldn't it be great if you could talk to the collector and say, okay, what version do you understand? I want to upgrade to a newer protocol. Like, none of that's been done.
So you're kind of left with, like, the receiver might be on 1.0, and then that's, like, 5 years old, what are you gonna do?
Laurent Quérel 00:55:16 Yeah.
I think there is hope, because… there is hope, because recently, for example, you're probably more aware of that than me, but I think recently they added the metadata Filled into the metric, right?
Joshua MacDonald (Microsoft) 00:55:34 Right, but there, the argument is you can ignore that field, and it's not going to change the meaning of your data.
Laurent Quérel 00:55:41 Yeah, okay.
I think we can have the same argument for this one, because no client SDK will support the… Yeah, I think it's not a discussion here anyway, but… I'm trying to figure out.
Joshua MacDonald (Microsoft) 00:55:57 to add gauge histogram in OpenTelemetry, and I'm seeing the same issues, but we'll… I think we should take this one offline. I'm very eager to hear from Kennedy right now.
Laurent Quérel 00:56:05 Yep. Great.
Oh, sorry, Kennedy, I didn't look at the clock.
So, let you, talk about PREOC.
Kennedy Bushnell 00:56:15 Yeah, no worries. So, Josh and I met earlier this week and had a good discussion about a couple of things that we can do here, but… I mean, this is a topic that has come up several times in the SIGs over the last couple of weeks, is that as we invest more and more people, kind of on both sides, and more and more people are, like, showing up to these meetings, we're getting lots more PRs, and the number of maintainers is not growing, and kind of is… limited intentionally in cases. So there's a couple of… Things that we came up with.
That… that we thought could help kind of ease the maintainers. One is investing in kind of teaching the AI PR review more of our Kind of things that we look for.
So… I will get my team to build out kind of the foundation for this, and then we can all kind of update those rules. So, things like don't use I don't know, this type of hash map, or mutexes, or prefer send over sync, or the other way around, and all these different things. So, kind of the… The call to action here, kind of in the short term, is… start thinking about those types of rules, the things that you look for in your PRs, and kind of just get them noted down, so that when that lands, you can you know, send a PR to kind of update those rules.
The second thing is… I mean, this might be more of a problem on my side. I don't know if it's something that we're not pushing for, kind of generally, but getting more people to do PRs, even as not maintainers, and kind of get… make it easier for the maintainers, therefore, by Having some of the kind of lower-hanging fruit already called out, and things like that, and then obviously build the trust.
The third thing… is, kind of related to that as well, using PRs and maybe mentorship or something to kind of ramp all of these people up, right? A lot of the people, at least on my side, don't have strong Rust backgrounds, and they're kind of ramping on Rust. They're… you know, just other languages. They're strong devs, but… What's it called, I'm drawing a blank on the word I'm looking for, but writing, like, real Rust code versus just C++ that's kind of transposed to Rust. I've seen that several times. So… That's gonna take some… you know, investment from all of us to comment on those PRs that, hey, let's go make this better, and then help everybody kind of grow, and then we'll have a lot more eyes on these things, a lot better, higher quality review comments from non-maintainers as well. So… thoughts and additional things there? I know that we're kind of almost out of time, and we should probably roll this into the next one as well, but… Definitely want to see what we can do to help.
Here in general.
Laurent Quérel 00:59:33 totally agree. I think, yeah, that's… yeah, I'm totally aligned with the SPE proposal.
They are, complementary, anyway.
Any other, proposal… proposal in, ideas in this space from others?
Kennedy Bushnell 00:59:56 Those were the main ones that we came up with that I remember, John.
Laurent Quérel 00:59:59 Oh, okay.
Kennedy Bushnell 01:00:01 the two of them.
Laurent Quérel 01:00:01 On the Microsoft side, okay.
Joshua MacDonald (Microsoft) 01:00:04 Yeah, that summarizes it. I just want to find ways to get more people reviewing code. I think the path to becoming proficient here is to, like, review. Just review, review, review all of it. The more you review, the more you will understand.
And the more you'll demonstrate that, you know, that we can trust you to do reviews and, like, give lighter reviews for the… For the approvers and maintainers, therefore, and then you'll grow into those roles.
Laurent Quérel 01:00:36 Yeah, I'm thinking about… so, for example.
On the first, the first proposal.
Sometimes we have some campaign, and a good example of that, the introduction of enum-based attributes.
Drew Relmas 01:00:55 Yeah, I fully agree.
Laurent Quérel 01:00:57 Yeah, so we need to take time and look at the value sphere, And derive new rules.
that we can, ask the AI to check every time. I think that will save us a lot of time, and also making sure that we have some consistency.
Invariant also observed We can derive a lot of knowledge and value and rules from this kind of big event.
Drew Relmas 01:01:29 Yeah, Kennedy, when this lands, I would be more than happy to write up some guidance about the new instrumentation we're doing for metrics. I would love to do that. It's a good idea, Laurent.
Kennedy Bushnell 01:01:42 Yeah, AI is, like, the perfect tool for those types of things, where you kind of change the recommendation of a product over time.
and say we're doing this type of thing now, so then you just codify that, and then now it will start to happen going forward. It won't go clean up old code, obviously, but you can also just do another pass to kind of get there, so it's… Nice in that way.
Laurent Quérel 01:02:08 I don't totally agree.
Yeah, we need to be more systematic with, and maybe that's something for also for the maintainers.
To, to help each of us to… To reduce the work. When we add a comment, when we add, basically a specific review, we have to ask us, okay, is it something that we can codify as a rule?
And then, add this rule somewhere, or at least open a GitHub issue to track the corresponding rule.
Joshua MacDonald (Microsoft) 01:02:47 Right, because an example of Drew…
Kennedy Bushnell 01:02:49 Oh, go ahead.
Joshua MacDonald (Microsoft) 01:02:49 Drew's… we've done 3 or 4 or 5 of these now, and at this point, you should be able to look at the 3 or 4 or 5 PRs to guide you through the 6th and 7th, and… and… There could be a process for learning the review style for that type of work.
That gets automatically updated. That sounds good to me, too.
Laurent Quérel 01:03:09 Yeah.
Okay, thank you so much. Have a good, end of the weekend, and see you next week.
Joshua MacDonald (Microsoft) 01:03:18 Thanks, all.
Drew Relmas 01:03:19 Thanks, bud.
Kennedy Bushnell 01:03:20 Thanks a lot.
