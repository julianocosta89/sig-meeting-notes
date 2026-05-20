SIG: Event WG
Date: 2026-05-19
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 06:22 Have you heard from Robert? Do you know if he's coming?
**Trask Stalnaker** 06:27 No, he was at the spec meeting, though.
**Liudmila Molkova** 06:55 Yeah, I ping him.
Hello!
Okay, so it's been a while, almost a month.
**Pellared** 07:52 Yeah.
**Trask Stalnaker** 07:53 Hey, hey!
**Pellared** 07:55 Hello?
**Liudmila Molkova** 07:59 So… We exist.
Yay!
**Pellared** 08:03 They're still alive.
perjuasis.
**Trask Stalnaker** 08:08 Yeah… oh…
**Liudmila Molkova** 08:15 Okay, so this is our… Stabilization, we're quite, And we are blocked on prototypes. I didn't do any Python prototyping.
**Trask Stalnaker** 08:38 If there's any languages, that CJ works in, I know he's interested in events… So we could probably… Rope him in.
**Liudmila Molkova** 08:54 Right, I was going to, Let me… since we're here, and I'm going to… Pink Sigil… Should I ping him right here?
**Trask Stalnaker** 09:17 Sure.
**Pellared** 09:20 It's fine.
**Liudmila Molkova** 09:50 And we are specifically one… the… Prototype similar to this one.
Quay.
Do we have… Yeah, so this came from… some conf, general, SIG, it would be cool to have defining events section. I think we have… Actually, everything we need to write it down.
And we mostly have it covered in… either events MD somewhere in this report, or recording exceptions, and stuff like that.
So… If anybody's interested in writing, go ahead.
**Pellared** 10:59 So you think it will be just following, these guidelines and hyperlink?
Yeah. There's something more.
**Liudmila Molkova** 11:08 There is an issue, let me find it.
A bunch of… Points we can cover.
Yeah, and this would include things like, okay, severity is not an optional, please make sure to set it.
Probably never set severity text unless you know what you're doing.
And stuff like that.
**Pellared** 11:57 You can assign me to Dumua, because I guess you are going to the Observability Submit, or not?
**Liudmila Molkova** 12:04 No, I'm not.
**Pellared** 12:04 result?
**Liudmila Molkova** 12:07 I'm not going anywhere. I'm still…
**Trask Stalnaker** 12:10 No longer a DevRel.
**Liudmila Molkova** 12:12 I'm no longer a Devereaux.
I'm jobless now.
**Trask Stalnaker** 12:22 Not to worry.
Soon to be. When do you… when's your start date?
**Liudmila Molkova** 12:27 In a week from now, next Tuesday.
**Pellared** 12:30 And where now? So you can search for the top, yeah?
**Liudmila Molkova** 12:34 Yeah, I'm going to be at Google.
**Pellared** 12:37 Okay, nice.
**Liudmila Molkova** 12:39 Oops.
Okay, so… I'm… I'm going to assign you… I… I just… I'm super busy with all the Gen AI stuff that's going on, and it takes all my writing powers and mental…
**Pellared** 12:59 I understand.
**Liudmila Molkova** 13:00 Energy.
So, if you… if you send a PR, I'm happy to review, but I… I… Yeah.
**Pellared** 13:07 Sometimes reviewing this piece takes more than doing it, so you know.
With you.
**Liudmila Molkova** 13:15 at least it's an external motivation. I don't have internal.
**Pellared** 13:18 Yes, I know. I know, I know how it works.
**Liudmila Molkova** 13:24 Yeah.
Awesome.
So this we can do, and then…
**Pellared** 13:32 This is related. I noticed that there is a PR for adding an event.
And they just…
**Liudmila Molkova** 13:39 Care?
**Pellared** 13:43 Zooming?
**Trask Stalnaker** 13:45 In this…
**Pellared** 13:45 I mean… I mean, I thought that maybe we want to check out if they are following these event conventions, etc. These are things that are worth calling out.
If you can see my four comments, for instance, in the… I, I… I added to YAML? Oh, I'm surprised, I thought I added it to the MP file.
Or maybe I have not published my comments?
**Liudmila Molkova** 14:17 Yeah, it is, it's just I'm in the wrong file.
**Pellared** 14:21 Okay.
**Liudmila Molkova** 14:25 I have a lot of feedback, but it's not about event modeling, but more like the domain-specific things.
**Pellared** 14:35 Yes, here I was more trying to review it from the, you know, kind of… even structuring know from the HTTP domain.
So, I think I pointed… Here are 4 things.
One was, The first one is that the proposal here was the timestamp, will be the first thing which happened.
So… It will be strange for me, but maybe it's just I'm biased.
That, that you emit the event.
When you have everything gathered, so you place something with the timestamp at the end, and it's… maybe I could agree with it, if there will be only one timestamp, but the issue is there are multiple timestamps here in this proposal. There's some DNS started, you know, some calls started, etc, etc.
then I thought that probably I would just want to have observable timestamp and have… and the other thing is that this proposal has things like end time, start time, which they propose to have relative kind of milliseconds from the timestamp, which I think can be… kind of awkward, and I think that the duration is… probably they just want start time to have something, some absolute time, and duration for relative time. I don't think… I think that would be the most usable combo.
From the metrics perspective, and… I don't know.
Mr. Run.
**Trask Stalnaker** 16:19 The metrics… Chris?
Dude… You mean the record time?
The time the metric's recorded.
I see.
How were… were they… you said they were suggesting to do some relative timing, though?
**Pellared** 16:41 Yeah, I don't know why they want to have it. I think it's confusing, given the existing semantic conventions says that time, I think it's using a unique, you know, epoch.
And I think there are other places where it says when there's a relative thing, it should be using duration.
but then duration will be awkward if everything is absolute from the beginning of the time step, that's why I proposed the start time, and then you have the other one, which is, you know, relative to the start time.
It will be the duration.
This is just my proposal.
**Liudmila Molkova** 17:19 So to do, for the sake… what you're saying is that we should never… Assign a different meaning to timestamp or observe timestamp when the meeting events.
**Pellared** 17:31 I'm not sure here, because maybe… not really, because I imagine a scenario when you… when you, for example, you're… Dumping some existing events from my external system.
And you have these timestamps.
you know, you're parsing some, I don't know, log file, or whatever, and you have these timestamps, then I imagine that it will be better just, you know, convert this timestamp and put it here, and the observed time will be, maybe, for instance, when you have captured and parsed this file, or something like that.
So when it was put to the telemetry.
I think this is the way it's even defined in the specification, the data model.
**Liudmila Molkova** 18:11 So for bridging purposes, for mapping purposes, it's okay.
**Pellared** 18:15 Yep.
**Liudmila Molkova** 18:16 Huh.
But when we design events, that are native to OpenTelemetry.
This… smells.
**Pellared** 18:28 Yes, that's my opinion.
**Liudmila Molkova** 18:54 I mean, so what they… generalizing. The problem is, okay, there will be more events like this, the timing events, when you dump a lot of different timestamps In one event, or every meet event per Huh.
Or event.
**Pellared** 19:24 I have no idea, I hit the snake fought.
I get the exact same for Trilogy covered, yeah.
But then, if you emit an event per, you know, per start-end, isn't the span… would it be any different from a span?
**Liudmila Molkova** 20:09 Oh, we lost track.
**Pellared** 20:11 Yeah.
**Liudmila Molkova** 20:16 Yeah, so if it's one big… Bing.
Why? Those are not… just… attributes on Span.
I…
**Pellared** 20:30 expense.
For each start and end.
**Liudmila Molkova** 20:34 Yeah…
**Trask Stalnaker** 20:36 And.
**Liudmila Molkova** 20:37 So…
**Trask Stalnaker** 20:38 Zoom crashed.
Hopefully you noticed I was gone.
**Liudmila Molkova** 20:43 See how we did. We did.
**Pellared** 20:44 started to tell… you wanted to say something, as rapidly develops.
**Trask Stalnaker** 20:49 I don't remember what I wanted to say now.
Oh yes, I remember. The… I would… I hope that events… are small, like, that there's not… I mean, the proto should be small, this should be… like, it should be okay to emit lots of events.
And… it does seem preferred to have a separate event marker for each of those, if only from, like, I'm thinking from a… Ui perspective, or an analytics perspective.
like… They know what that… means the timestamp is associated with that event. Like, you can display it on a timeline.
Versus if we encode the timestamp into attributes?
It's going to require a lot more… semantic convention knowledge… To render that.
**Pellared** 21:55 Do you know why they are not just spans? Because if I saw the attributes, I think they were only start and end, or maybe I'm wrong.
**Liudmila Molkova** 22:09 I… this is the good question on modeling. There was some discussions in the past.
I think in the current shape, it's not even implementable, because… The connection pooling and everything, it's asynchronous, and you just cannot attach.
**Pellared** 22:33 Okay.
**Liudmila Molkova** 22:33 some of those things to an HTTP call span. And there are spans, where there is a different way to model where DNS is a span.
Those are more, like, the main questions, right?
**Trask Stalnaker** 22:55 Oh yeah, that's a lot of… Timestamps…
**Liudmila Molkova** 23:07 But I, I think I… I like this.
this approach… Either those are small spans, Where there's our events.
But they are individual.
**Trask Stalnaker** 23:34 Now, I think this comes from client devices. The motivation here, at least for Serbi, I think, was for… Android… I don't know there's always that kind of… Contention of keeping Telemetry Compact.
But I would… I don't know if event… like, there's a lot of fields on event, but I don't know if, I mean, if the event is… Like, when we send it over the wire, there shouldn't really be much… on it.
Should be pretty compact.
**Liudmila Molkova** 24:22 There are, like, what…
**Trask Stalnaker** 24:24 I don't know.
**Liudmila Molkova** 24:26 of them. So the envelope size… start to become problematic. And this is exactly the consequence of us deprecating span everywhere and sexual.
This… these are spins… I feel like these are span events.
**Trask Stalnaker** 24:48 The envelope. What do you mean, the envelope?
**Liudmila Molkova** 24:54 And the trace context, event name, Attributes, bag… That's…
**Trask Stalnaker** 25:06 Let me see… with… Span events… okay, I see. Span events don't have the trace context, yes, because they're nested.
Yeah… That is a lot of attributes.
A lot of events.
**Liudmila Molkova** 25:49 Some of them are opt-in, though.
Wow.
Assuming it's a browser thing, or the client.
**Pellared** 26:09 It is… It is, I'm just… yeah.
**Liudmila Molkova** 26:15 Hit.
I… I… I think it would make sense for them to do something in the client domain?
That makes sense for them.
And they're very special. We would not design it further.
**Pellared** 26:30 From what I read.
I think it makes sense to do what you proposed, Trask, that there just should be little small events, because they said that the model is asynchronous, and they cannot connect it to the span. That's why they do not want you to model it as spans.
And they do not have the span contacts, so they just want to have any information that something started and ended.
In some cases.
**Trask Stalnaker** 26:58 They… they gotta be at… Have to be able to correlate all of those things together somehow to stamp them all on the same event, though.
**Pellared** 27:06 Yeah.
And what they'll do, create some artificial… I see.
**Liudmila Molkova** 27:18 I mean, let's not… Okay, so what we can take from… from this?
it's… To me, it's an edge case.
**Pellared** 28:10 Yep.
**Liudmila Molkova** 28:13 Our guidance is probably… Something per event, per occurrence of something.
And… The timestamp should be meaningful of that occurrence, unless there is a strong reason.
**Trask Stalnaker** 28:45 Yeah.
But then the… this… This one being an edge case.
Sort of… all bets are off.
I mean, they can violate, I mean, it is… it's very common, I think, for, like, browser timing events to be reported in terms of Relative timestamp, since page load.
So I'm not opposed to… that for… planned.
But yeah, I think… Like, this… Maybe our recommendation is just, yeah, model this in the client SIG or client's And even though, yeah, some of this stuff is useful in general for HTTP clients.
We might choose to model it differently for… You know, or less of those things, or… regular HTTP clients.
Or non-mobile.
**Liudmila Molkova** 30:20 Yeah.
**Trask Stalnaker** 30:26 So start time and end time here are… those are… Integers… Dura… relative durations.
**Liudmila Molkova** 30:40 Yep.
**Trask Stalnaker** 30:47 And there was a prototype of this, right? I think it was even in Java.
I should probably look at that.
**Liudmila Molkova** 30:58 Yeah.
So they can get it from OKHCTP?
**Trask Stalnaker** 31:06 Yeah, let's see, are these, like, callbacks?
Extends event listener. What is the event listener? Is that okay HTTP, probably, yeah.
**Liudmila Molkova** 31:21 Yeah.
And then it would apply to all, like, HTTP instrumentations.
Makes it tough.
**Trask Stalnaker** 31:41 Why don't they… and that's not correlatable to the span?
But it's correlatable to something.
They're not making some assumption about it being single-threaded.
Or…
**Liudmila Molkova** 32:43 It's probably a network timing thing.
It's probably per… created per… Request written down. It can get the parent context.
It's 1.
**Trask Stalnaker** 32:57 Okay.
**Liudmila Molkova** 32:58 Span per everything.
**Trask Stalnaker** 33:03 So, they can get it.
So why not stamp these on the span directly?
**Liudmila Molkova** 33:29 It doesn't look like they do emit any logs in this prototype.
**Trask Stalnaker** 33:40 Oh, maybe they are stamping it on the span?
Search for a set… Attribute… Put attribute, set attribute…
**Liudmila Molkova** 33:50 Oh, log rack, oh, okay.
**Trask Stalnaker** 33:57 Log Builder… Can we see where they're creating the log? Oh, there it is, down there. Create Builder with deferred attributes.
Creating it, they're getting the contacts…
**Liudmila Molkova** 34:26 Oh… Wow.
Cry.
So this is effectively… a log record that mimics HTTP span.
There's all this additional… Data.
And it would… the life would be easier if all this additional data was in its pan itself.
**Trask Stalnaker** 35:15 Yeah… I'll leave a comment on the semantic convention.
PR…
**Liudmila Molkova** 35:33 Correct.
Cool, thanks.
**Trask Stalnaker** 36:10 I'll have to comment. Alice, that's something to… follow up on…
**Liudmila Molkova** 36:21 Okay, and the last, but not the least… The log bridge name and the log bridge first.
**Trask Stalnaker** 36:29 I've… all of that has paged out of my brain.
**Liudmila Molkova** 36:34 I… okay, I think there are two parts. The first one is important, the second one is bike shading. The important part.
We had a discussion in SPACSIG, right?
A week ago, or maybe longer.
about… Instrumentation scope attributes, and it… It's a difficult topic, right?
**Trask Stalnaker** 37:06 It was difficult because… Java doesn't implement them.
**Liudmila Molkova** 37:12 Yeah, I think Jack brought up… Yeah, that it's…
**Trask Stalnaker** 37:18 performance.
**Liudmila Molkova** 37:19 paraphr, right?
That the current implementation is built on assumption that there are no instrumentation scope attributes ended in another lookup.
would be… Something.
**Trask Stalnaker** 37:34 more costly.
I think in the… Like, in the normal usage, you have… you cache your logger.
So you only have that lookup once.
But I think, that it was in the log bridging… logging appenders.
Where each time you're getting from the log… you're getting the logger name dynamically from the logger.
And so you'll have to look up the… Open telemetry logger each time.
**Pellared** 38:20 I have a question.
Regarding lookup, because I think we have implemented in Go, so, you know, the lookup and hashing.
So I think if, in general.
if there… if you have a structure that, you know, has, I don't know, two strings and attribute set, if the… If you just add this to compute the lookup, the hash set.
I think if they'll be just empty, it should not increase, you know, increase the performance.
Because they'll just calculate, probably, to almost nothing.
like, there'll be only… I think, I think if you just, you know.
change the internal implementation of the lookups, you'll probably just add a static, you know.
For usual use cases, when they are not used, it will be a static thing.
And for attributes, as long as there's only, you know, 1, 2, it should also be, you know, a linear, linear, you know, performance class.
Probably needs to be validated, though.
**Liudmila Molkova** 39:30 So, you can optimize it.
Further.
You can cache… Wow.
**Pellared** 39:46 Basically, just hashing.
**Liudmila Molkova** 39:50 But Elsa, you probably have… Normally, 1.
Instrumentation scope.
Oh, sorry, not one instrumentation scope, one combination of… one bridge in Europe.
**Pellared** 40:04 drip.
**Liudmila Molkova** 40:05 A few of them.
So this loop up should be… Fast.
**Trask Stalnaker** 40:12 I would think as long as the bridging doesn't… as long as you can't get arbitrary… as long as your bridge doesn't support instrumentation scope attributes, like, dynamically being passed in via the log.
Because I would think, then… That… Yeah, you would just have… I mean, you could essentially have Your own cash in the bridge of logger name.
to… instrumentation scope with… both the… Yeah, I mean, you… Seems doable to me.
**Liudmila Molkova** 41:04 So I think the other… it's probably, yes, although the other concern Jack shared, if I remember correctly, that…
**Pellared** 41:09 I think, just one thing, I think maybe not in bridges, but I know that with some instrumentations.
we are caching the attributes to not make the allocation, we're having pools for the attributes. Because when we are bridging and translating, we do not want to make, you know, a lot of key allocations and bridge the same, you know, kind of allocate the same attributes again and again.
And I think that's the biggest optimization that we need to do with some instrumentations in Go.
**Liudmila Molkova** 41:48 Yeah.
So I think the other concern Jack brought up was, I don't know how… I don't relate to this, but… That… It's somewhat specific to logs, because in retracers and meters, we use library name.
As the scope name.
I think this is… not the long-term.
Direction, we should have scopes.
We could have scopes for tracers and meters more granular than that.
I think .NET does already.
**Trask Stalnaker** 42:38 And users… users should.
Kind of, to… Have different parts of their app, kind of similar.
To what we do.
With splitting up instrumentations, but they can split up their app.
**Pellared** 43:26 But the thing that Jack mentioned was just Some… there was some collection, or it was just a notice?
**Liudmila Molkova** 43:39 I felt that he is reasonably concerned with introduction of instrumentation, scope, attributes, and We probably need to socialize it more in the spec call to make everybody more comfortable with it.
But I think it's… It's…
**Pellared** 44:00 Historically, this came from his feedback and his proposal, like, a few years ago.
To use this.
Because the reason was that the logger name, which is the instrumentation scope, is, you know, the instrumentation scope name, and he didn't want to use the logger name and instrumentation scope for the library, which we proposed in Go, because we do not have this notion of logger name. And yeah, we are making circles.
**Liudmila Molkova** 44:29 Yeah, and also, I think… We already have people struggling, like, especially from the Prometheus community with our resource attributes and signal attributes, and this is the third layer.
That's… yeah.
We definitely should be cautious about using it.
So I think what we can, tell CJ is to socialize it more on the spec call, and we can probably help him push it a little bit.
I had a bike-sharing comment. I thought we are… In the world of… Instrumentation… Library name and instrumentation library version.
**Pellared** 45:23 So, CJ also didn't like this proposal, which he responded here.
**Liudmila Molkova** 45:40 But then…
**Pellared** 45:41 even… I think he even mentioned some… I think I had a chat with him, that I think for Rust, he even had some… some example, or possible example, when this might conflict.
**Liudmila Molkova** 45:59 Alright, so we'll have log bridge name, log bridge version, but we will also have instrumentation library name and instrumentation library version in the long run for tracers and meters.
Heaven… Two of them.
Oh my gosh.
**Trask Stalnaker** 46:16 Yeah, I didn't… I… Can you remind me your reasoning?
**Pellared** 46:23 The reasoning is that CJ felt and Einstall had the same concern for Go.
that some instrumentation libraries, which may not be, for instance, Contributed, but, you know, some custom third party or whatever, may prefer using some libraries like S-Log, which is instead of Library of Go, instead of our, our Logs API, and it's easier to have told me that For .NET, people would use iLogger, for sure, etc, and other things, which may also be problematic.
And for Rust, I think he also mentions that there are some logger, logger libraries that people may prefer using. I think the reason is also, I'm sure there's a logs API in Rust.
Like, what she's… you… You know, user ready.
So I think that's… that's it.
But I think the main reason golf.
**Trask Stalnaker** 47:19 What's the problem with that?
**Pellared** 47:24 They wanted to have the information about the iLogger version.
which is, you know, a separate assembly in .NET.
And then they wanted to have a separate information about the bridge, which is bridging iLogger into the SDK.
**Liudmila Molkova** 47:48 Okay, so… Wouldn't that be…
**Trask Stalnaker** 47:50 Instrumented library?
iLogger… Sorry, let's take the iLogger example.
You have, A pen.
**Pellared** 48:06 Instrumented library is the instrumentation's opening.
**Liudmila Molkova** 48:12 No, instrumentation, instrumentation scope name is the logger name.
**Pellared** 48:17 Yes, so… so kind of the ins… Yeah, you're right.
Yo.
I need the ins.
Patient.
So, instrumented library will be iLogger, right?
**Liudmila Molkova** 49:42 Oh, whatever, the assembly name, Microsoft Extensions Login, or whatever.
**Pellared** 49:46 Yes, you're right, you're right.
Instrumentation library name.
will be the thing which you're instrumenting with. It doesn't need to be login, it can be, like, HTTP something.
So that's the reason, and then the bridge name will be hotel, like, Logger, Appender, or something like that.
**Liudmila Molkova** 50:07 H doesn't know where the log came from, if it came from HTTP library.
So the instrumented library is HTTP library, then, if it knows.
**Trask Stalnaker** 50:23 Unless there's a proposal to pass that.
To the… over the lager, somehow.
**Liudmila Molkova** 50:37 But then it's… it cannot be instrumentation scope, it's paralog record.
Well… Yeah.
**Pellared** 52:19 Yeah, I think that you're right, the only way to do it would be just to pass this instrumentation library name explicitly.
What are some conventions?
**Liudmila Molkova** 52:36 Oh, so maybe in .NET there is a funny problem.
Because there is no instrumentation for our logger.
And it's part of Upper Telemetry SDK.
**Pellared** 52:49 Yep.
Indeed.
**Liudmila Molkova** 52:52 But then, it's not an instrumentation library, it's some sort of an artifact, or the instrumentation library is a telemetry SDK itself.
I mean, I would abuse it.
And just… For the… the auto… Ramo.
This friend, up until the tree logs, up until Emmetry Logger.
this one.
Oh… This is honest.
And this… I think I, I, I had this rant of bike shedding with myself somewhere in this issue already.
**Trask Stalnaker** 55:05 Yeah, this issue's been going on for a while.
**Liudmila Molkova** 55:12 So… The collector instrumentations or serverless things are not necessarily libraries.
And you can.
Yes.
Okay, can we make any progress without a procedure here? Like, we… I'd rather not introduce unless there is a very strong reason to have a log bridge and… namespace.
Because there's nothing special about log bridges, I think.
**Pellared** 56:16 Yeah, let's just put this a comment, and let's see what we'll follow up. I also think with CJR.
**Trask Stalnaker** 56:26 Yeah, I mean, I… if it's needed, it's needed. I just… I just want to be really clear on… Agreed.
It is a confusing…
**Pellared** 56:41 Issue.
**Liudmila Molkova** 56:44 Okay.
Cool.
Robert, can you… Also, if you're going to chat with Sijo, can you point him to the discussion with Jack? Like, Jack's concerns in the spec call?
**Trask Stalnaker** 57:07 He lost his headphones.
**Liudmila Molkova** 57:08 Yeah.
Oh.
Are you back, Robert?
**Trask Stalnaker** 57:18 Okay.
**Liudmila Molkova** 57:23 Talk to you later.
**Trask Stalnaker** 57:24 Alright, have a good one. Bye.
**Liudmila Molkova** 57:26 Thanks, bye.
