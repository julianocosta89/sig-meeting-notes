SIG: RPC SemConv Stability SIG
Date: 2026-10-15
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:40 Hello, good morning.
**Trask Stalnaker (Microsoft Corporation)** 00:42 Good morning.
**Liudmila Molkova** 00:47 We are at the end of this.
Workstream.
**Trask Stalnaker (Microsoft Corporation)** 00:52 That's awesome.
**Liudmila Molkova** 01:03 Should we try to get stable by KubeCon?
When we could.
**Trask Stalnaker (Microsoft Corporation)** 01:09 Yeah, let's do it.
**Liudmila Molkova** 01:21 Oh, I saw you push the double refinement.
Fixes.
**Trask Stalnaker (Microsoft Corporation)** 01:28 Yeah, yeah, yeah, thanks for reviewing my AI's work there.
**Liudmila Molkova** 01:37 Do you like Unrest?
**Trask Stalnaker (Microsoft Corporation)** 01:40 Yes! That's awesome!
Yeah, let's go… let's just go through what's… It's… So I.
And… Okay. Histogram buckets.
Yeah, let's look on the… maybe… Well, let's see, you added stuff, so let's look at your…
**Liudmila Molkova** 02:55 Yeah, I'm trying to merge. Yeah, I put moved double in the merge queue.
Yeah.
For the long streaming spans, The last time we talked about.
Maybe… I.
I have an option to not make context current.
So remember, there is a long span, very long span.
Or.
Essentially, the connection time and messages in between.
And… Yes.
Like, there are concerns in this issue that this span is never ending, then it's not reported.
Which is… It depends on how application is stopped, right? But realistically, it's probably There is usually a timeout, like, 10 minutes or something.
From the volume perspective, these spans are… should not be problematic comparing to everything else.
The… there is a concern that the… Everything is correlated to it, and they have a lot of long traces.
And this is, I think, a valid concern.
And.
The idea was, okay, the spans are not problematic, the context is, so maybe we don't call the spans current, don't make them current.
For bidirectional streams, where we expect it to be long.
And I entertained the idea of, okay, let's say we don't make them current by default.
The consequences are not great.
And… I might have had the MHU we're talking about.
Bidirectional streams and long spans.
So what if we do not make the spans current?
Then, the first consequence is that if I have an application.
That creates its own spans.
Right, for each message, let's say, I decided that that's what I want.
I no longer can parent to the current span, or I cannot link it. The only thing, the only option is that I just don't establish any relationship between The message.
and the stream, even if I wanted to.
Is there is no way to propagate from.
the RPC instrumentation to application otherwise.
So, we definitely now need a config option to… for some users to opt out of this behavior.
But then applications that do not create per message spends.
Like, I don't have manual instrumentation. It's even worse, everything becomes a root.
Everything that happens on there.
Law correlation is questionable, they are not correlated at all, or correlated to the subspence. Arguably, it's even worse than long traces.
So if in the first case we had a problem of sampling as per.
Long stream. In the second case, we have a problem of sampling is completely random.
So I'm kind of arguing that.
We should keep spans current by default, because it's better.
It gives more options and applications that do manual instrumentation.
It's in their full power to decide whether they want to parent to the current context.
Or they want to link it or drop it.
And it's not that they need to do anything, it already works for them if they have this instrumentation.
And they already had a choice, and they could choose For our multiple options.
So I'm kind of thinking we don't need to do anything.
Right now. And if there are some… Instrumentation level concerns that adding configuration option.
To make it not current, Can always be done. Later. It's not the semantic conventions where Stability… concern.
**Trask Stalnaker (Microsoft Corporation)** 07:43 So, just trying to think through this, So.
On the… the blue… law, the… Long pull, bidirectional stream.
This represents, like, a connection style.
Currently, so… By propagating… I'm trying to think of this here. By propagating… So that's… yeah, Focusing on if the app doesn't do anything, sort of.
They're correlated to one, so… We don't… we… Aren't today producing a per message event?
I realize we don't… I mean, at the sort of protocol level, it's not really a span anyway, because it's… Fire and forget, like, there's not a duration there.
But sort of like the thinking of like messaging, like process message.
If there is a process message.
I don't know, like for gRPC or something, like there's there is a there's gotta be a hook.
In those frameworks, so there's, like, process message.
**Liudmila Molkova** 09:24 Right.
**Trask Stalnaker (Microsoft Corporation)** 09:25 and That could be the span.
**Liudmila Molkova** 09:34 Yeah.
So you're saying we could create the per message span.
And if we did that.
This is where we would decide how to parent it, and maybe default option would be to link.
The tricky part is.
We don't know if message has its own context.
But then we would get the… Propagator as a configuration option.
**Trask Stalnaker (Microsoft Corporation)** 10:08 Yeah, I mean, it… I… I'm… I remember those… Events being very noisy.
**Liudmila Molkova** 10:18 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:19 So, like, it feels like an op… Opt-in kind of a thing.
And I wonder if it even… Okay, so if you… Opt in to that, you get the message spans… And then… Possibly there's another option there of whether you want it to be… The property of the parent who, if you want it to be parented or not.
**Liudmila Molkova** 11:01 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 11:03 I'm trying to think what the default there, like, if you want these per message spans.
**Liudmila Molkova** 11:14 Basic.
**Trask Stalnaker (Microsoft Corporation)** 11:16 Go ahead.
**Liudmila Molkova** 11:18 Linking could be a default option.
For video streams.
**Trask Stalnaker (Microsoft Corporation)** 11:24 Oh, Madhav.
**Madhav Bissa** 11:46 Yes?
**Trask Stalnaker (Microsoft Corporation)** 11:47 How does that sound from, your perspective, because I think you had had some concerns about the bidirectional screens… I forgot what… your… Concern was, I might be mixing up things.
**Madhav Bissa** 12:24 You mean, like, in terms of suggesting the solution that app creates in its own per message spans, right?
**Trask Stalnaker (Microsoft Corporation)** 12:34 No, we're… I mean, from the perspective of what should we.
So yeah, if… let's assume app… Don't create permissive spans, because we kind of… I think our, at least in OpenTelemetry, like, instrumentations.
So, I… I… Well, I don't know, maybe this is me from Java Instrumentation.
Perspective that we assume that people aren't doing manual instrumentation.
The… what, for these long… bidirectional streams, connection-based, sort of, bidirectional streams. What are you capturing today?
**Madhav Bissa** 13:24 We are capturing call level spans, right, so…
**Liudmila Molkova** 13:33 I think there are span events for the individual messages.
**Madhav Bissa** 13:40 Let me quickly check, I don't think so.
**Trask Stalnaker (Microsoft Corporation)** 14:15 Yeah, Lumila, I kind of like this.
Idea of the process message.
And… Similar to, like… because it gives us… Something to wrap these things in.
And… It.
Feels to me like it aligns, sort of, with messaging… Where, when we have these, unidirectional kinds of… Things, there's a process span… versus if it's… 8.
synchronous, a unary call, I guess, it's… You know, we get the… normal.
It's still sort of a process span, but it's… We don't need to think of it that way.
**Liudmila Molkova** 15:16 Yeah, given these things would be obtained.
The opting into them.
Can come along with picking the behavior.
**Madhav Bissa** 15:29 Yeah, we do have span events for inbound message and outbound message.
I guess so, yeah.
In the bedroom.
**Trask Stalnaker (Microsoft Corporation)** 15:40 Okay.
And.
Instead, so what we're… Possibly, what we're kind of thinking through here is… So with the SPAN… events… Well, I guess, in that case, you are propagating the… context.
From the parent's bidirectional stream, in order to stamp the span events onto something.
Oh, can you even do that? How does that work?
**Liudmila Molkova** 16:21 The light.
**Madhav Bissa** 16:22 Pan events need context, I didn't understand.
We are already in the span when these things are happening, right, so we already have that context, you just fire events at that time, that's it.
**Trask Stalnaker (Microsoft Corporation)** 16:39 Oh, yes, I'm sorry, I understand.
**Madhav Bissa** 16:42 Right?
**Trask Stalnaker (Microsoft Corporation)** 16:44 Yeah.
**Liudmila Molkova** 16:51 Okay, I can… Writing down the proposal here for potentially.
I'm in the process per message.
Spans that instrumentation would emit, and some opt-in behavior that would pick the context propagation way.
**Madhav Bissa** 17:12 So, are we saying we'll have per message spans? Because that would be very…
**Liudmila Molkova** 17:19 Locked in.
**Madhav Bissa** 17:20 It.
**Liudmila Molkova** 17:21 And… Like, to be fair, I think we're entertaining this idea for the future. I don't think it's a stability blocker. It's the… Like everything about additional features for bidirectional streams we've been pushing away for now.
And this would be the solution for this problem that we designed, but we don't do it right now. That's what would be my…
**Madhav Bissa** 17:48 But what exactly is the problem? Why… can you scroll up a little bit?
I just want to revisit what the problem is. Why is it never-ending span? If it's a… what, is it a long-living stream?
**Liudmila Molkova** 18:01 It is a long stream, yeah.
And the problem is that during the stream, there could be a lot of telemetry.
That's created, and all of it would be correlated to the stream.
And it creates problems for… in some scenarios.
Well, in the original form, the span never ends, but it's just a matter of how application is stopped, right?
**Madhav Bissa** 18:36 Right.
**Trask Stalnaker (Microsoft Corporation)** 18:39 So, it's especially common for when you're, Doing communication from the server back to the client, right?
**Madhav Bissa** 18:48 You open up a connection.
**Trask Stalnaker (Microsoft Corporation)** 18:49 And then that's basically… Open for the lifetime of the client.
**Madhav Bissa** 18:55 Yeah, I understood. Until the time the span doesn't end, it's basically not recorded.
**Liudmila Molkova** 19:01 Yeah.
**Madhav Bissa** 19:02 Yeah.
Okay, sure.
**Liudmila Molkova** 19:05 I I'd like to talk about another issue while we have Madhav here. Oh yeah. I'll follow up on this one. We'll see if if anybody who commented on that issue will have thoughts. So Madhav, you created this issue that this will be a performance overhead.
And, I think Trask, suggested that maybe caching the server address and port per channel at construction time would be a solution to performance problem. And I think you have concerns about, like, plumbing things through and having a caching layer.
And I did some AI-assisted research, so some… some… some… There could be some problems here, but my assisted research and, prototype It seems that for Java and C++, it's not a problem at all, because there is already a cache layer, and the implementation for Java is… pretty much trivial.
for… Go and Python, it's a little bit more interesting, but still, there is some caching.
That could be done, and the Python implementation is very inefficient regardless, so it would create more problems. So, I'm kind of trying to understand, should we do something about server address and port?
And… I…
**Madhav Bissa** 20:35 So.
**Liudmila Molkova** 20:35 I think so.
**Madhav Bissa** 20:37 So, I think this is, In principle, we have agreed that we will omit that, right? It may or may not be a performance issue. When we come to implementation, we'll have a look, whatever is the best way, we'll basically… use that.
So, I think, Odin's, I think that for that… I mean, to that extent, we should be okay, right? We have decided that we'll emit that, and if there is a performance overhead, whichever is the best way of implementation we find, then we'll give the users an option to Opt out of just… that performance overhead.
If we need to.
**Liudmila Molkova** 21:23 Awesome.
**Madhav Bissa** 21:23 Yeah.
**Liudmila Molkova** 21:25 Should we close this issue?
**Madhav Bissa** 21:29 Let me respond to it today. Yeah, yeah. Maybe the next meeting we can close this, yeah. Should be okay.
**Trask Stalnaker (Microsoft Corporation)** 21:35 That would be great, because, yeah, I think we weren't clear whether that was… whether you meant that we don't… you can't commit to implementing it, or commit to, like… like, immediately, or just the… yeah.
**Madhav Bissa** 21:49 Yeah, yeah, understood. No, earlier there was some resistance around it, but I think I got the leads on board that it's fine, even if there's a performance overhead or not.
It is feasible. If there's a performance overhead, we can give our customers an option to just not do this specific thing of hotel conventions, if there is a performance over it. But for now, like, since we are okay with both the options.
The problem goes away for you, at least. We are okay to align on the total.
**Trask Stalnaker (Microsoft Corporation)** 22:19 Thank you.
That one was… Oh, haha.
the… Right… It's all right. No.
Instagram buckets.
Oh, I sent this one.
Yeah, Madhav, if you could take also a quick look at this, just, make sure this looks good to you. This is aligning the… Let's see, wait, wait… It doesn't say GRPC… oh, yes. So, we are… we are changing the general RPC boundary… bucket boundaries, sort of based on what we've learned from the gRPC bucket boundaries.
But they don't align with the gRPC boundaries, but we also, are specifically overriding the gRPC bucket boundaries in these semantic conventions to match yours, so that you will be compliant with the gRPC If that makes sense.
So if you look at the gRPC-specific semantic conventions, they have your… bucket boundaries.
We can't hear you.
**Madhav Bissa** 24:02 Sorry.
So if, yeah, if they are aligned with what A66 has, I am, I'm good with that.
Yeah.
Sounds good.
**Liudmila Molkova** 24:12 Trask, you have the compatibility with GRPC Open Census metrics.
It's because it's… since Open Census days?
**Madhav Bissa** 24:27 No, A66 is not open census, it is hotel.
specific.
Oh, yes, okay.
**Trask Stalnaker (Microsoft Corporation)** 24:41 Okay, yeah, let's remove that.
Amen.
**Madhav Bissa** 24:56 Cool.
**Liudmila Molkova** 24:58 I think it appears in multiple places.
**Trask Stalnaker (Microsoft Corporation)** 25:00 Okay.
**Madhav Bissa** 25:04 Ludmilla is reviewing the code.
While discussing stuff.
**Liudmila Molkova** 25:09 Oh, I, I was, I reviewed it yesterday, I was like, okay, it make, it kind of makes sense, it's just I decided to ask.
**Madhav Bissa** 25:17 Okay.
**Trask Stalnaker (Microsoft Corporation)** 25:20 Let's uninstall this, and… Okay, and you said you merged this…
**Liudmila Molkova** 25:40 Yeah.
If you're open… the board, it brings us to one more issue in to-do. Oh, sorry, in no status, which I think we agreed on.
But we.
I think wanted… I might have you to… ArcHit, and then we would close it, but… or if you want, we can talk about it more.
So I think the original issue was that.
The Medit Original is… holds the extra unknown methods.
And it potentially has high cardinality.
And it does not appear on metrics, and the method is capped to the known methods, but it appears on spans.
Because we want the RPC method to be the same across signals, and we also need span name to be to have low cardinality.
**Madhav Bissa** 26:47 Yeah.
I I think yeah.
The leads were okay with this.
**Trask Stalnaker (Microsoft Corporation)** 26:58 Cool. If you don't mind.
**Madhav Bissa** 27:01 I will, yeah, I'll reply. Yeah.
**Trask Stalnaker (Microsoft Corporation)** 27:05 Okay.
**Madhav Bissa** 27:06 Cool.
Sounds good.
You have assigned me action items in the notes, Ludmila.
**Liudmila Molkova** 27:17 Oh, put it in the notes? Sure.
**Madhav Bissa** 27:20 Trask presenters presenting.
After the advent of AI, I have been getting tagged in so many GitHub issues.
**Trask Stalnaker (Microsoft Corporation)** 27:28 Oh, I don't know how to… can I tag you? No.
**Madhav Bissa** 27:39 Okay.
**Trask Stalnaker (Microsoft Corporation)** 27:41 Do you have the link to the notes?
**Madhav Bissa** 27:44 Yes, I have linked to the notes. Okay.
**Liudmila Molkova** 27:46 And also a server address, the…
**Madhav Bissa** 27:49 Yeah.
**Liudmila Molkova** 27:50 This one.
**Madhav Bissa** 27:51 Because what has happened is after people have got access of AI, There are just too many issues and too much noise with GitHub notifications, so I've just turned them off.
**Liudmila Molkova** 28:03 Tell us about this.
**Trask Stalnaker (Microsoft Corporation)** 28:05 you.
**Madhav Bissa** 28:05 I get, like, 100, 150 per week, and I'm… my mailbox is going crazy, so I've just turned it off.
**Liudmila Molkova** 28:14 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:18 All right.
Yeah, and so, let's see, oh, we do have a couple of things. Okay, we've got a couple of things in progress. We've discussed… all of these… To do stabilize, stabilize…
**Liudmila Molkova** 28:36 Stabilize. Decide what to stabilize.
**Trask Stalnaker (Microsoft Corporation)** 28:39 Yeah.
Alright, so yeah, Ludmila and I were just… discussing, at the very, very beginning, before you all joined, that, maybe we can stabilize before KubeCon.
**Madhav Bissa** 28:52 Yeah, I am aiming for that. I have a design discussion lined up with the leads today.
Hopefully there are not too many… Blockers, if there aren't, I will let you know.
Then.
**Liudmila Molkova** 29:07 Yeah.
**Madhav Bissa** 29:08 And let us know.
Yeah.
**Liudmila Molkova** 29:11 That's awesome. Let us know, like, if you have any blockers right away, we can try to resolve them.
**Madhav Bissa** 29:17 Yeah, yeah, that's the reason I am… Doing it face-to-face and not offline with them.
Yeah.
**Liudmila Molkova** 29:23 Awesome.
**Madhav Bissa** 29:25 Okay, cool. Thanks, guys.
**Liudmila Molkova** 29:26 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 29:27 Thank you.
**Liudmila Molkova** 29:28 to you.
**Madhav Bissa** 29:29 Bye.
