SIG: RPC SemConv Stability SIG
Date: 2026-10-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:40 Hello.
How are you?
**Madhav Bissa** 01:45 I'm just drowning in work.
**Liudmila Molkova** 01:48 Oh, sorry.
Looks like you're in the office, and it's probably very late for you.
**Madhav Bissa** 01:55 Yeah.
8 PM for me.
**Liudmila Molkova** 02:03 Thanks for making it.
**Trask Stalnaker (Microsoft Corporation)** 02:05 Hey, Madhav.
**Madhav Bissa** 02:07 Hey Trask, how are you?
**Trask Stalnaker (Microsoft Corporation)** 02:08 Library.
Good, thanks for the ping, Liudmila.
**Liudmila Molkova** 02:13 Yeah, it was every other week Meetings. It's hard to remember.
**Trask Stalnaker (Microsoft Corporation)** 02:17 In my head, yeah, I'm really bad at my calendar. Never reminds me about things.
**Madhav Bissa** 02:26 Set alarm.
**Trask Stalnaker (Microsoft Corporation)** 02:28 Yeah.
**Madhav Bissa** 02:29 In the phone.
That's the only thing that works for all of us.
**Liudmila Molkova** 02:37 And then you need to remember to set the alarm.
Okay, saw it… See?
I think Steve is not joining today. Not sure about Matthew.
I'm sorry, and I cannot type yet.
Okay.
We have a few things.
That are waiting for reviews.
And this one we just I'll chase Matthew to take a look.
It seems to be non-controversial. It might have, if you want to take a look.
would be nice. If not, that's also fine. It's the thing we discussed about the…
**Madhav Bissa** 03:34 Yeah.
**Liudmila Molkova** 03:34 Adderson trailers.
**Madhav Bissa** 03:36 Sure.
**Liudmila Molkova** 03:38 I would love to get your approval on it.
But, yeah.
Even if it's not, like, if it's gray.
Or.
Then… notch.
Nothing really interesting here.
This one, I think Trask, you… oh, you didn't approve.
**Trask Stalnaker (Microsoft Corporation)** 04:05 No, I thought I looked… Called it… Yeah, I will approve this.
**Liudmila Molkova** 04:22 Cool. Thank you.
And there is a similar PR for double.
And I am going to approve it. They both have the problem of… duplication.
Because they copy over things between… Spans and metrics.
I am… Actually, I want to switch maybe the… the span… Stands to refinements, and this would help us.
Remove duplication.
I think it's a good idea for us to switch them to the refinements for the stability purposes.
Because… It.
If span type becomes sticky, becomes… Something on the OTLP, we should rather… Have it the same.
Cool. But I'm… I'm going to leave a comment on this one for Steve, and a similar one for Matthew, too.
Well, I… Anyway, I have a… I have a… commit, I will show on how to do things.
So it's easy.
**Trask Stalnaker (Microsoft Corporation)** 05:53 So that's… sorry, I didn't quite follow. This is… Oh, I see, this is… these are… these PRs are for metrics refinements only, and you're talking about span refinements.
**Liudmila Molkova** 06:07 Yeah, and essentially nothing will change in Markdown for spans, it's just that they will be the refinements.
Right.
Okay, nothing substantial.
here…
**Trask Stalnaker (Microsoft Corporation)** 06:26 And does… for those… sorry, do these PRs… Is it useful to do the span refinement in the same PRs, or could we merge the metric refinements and follow up on the span refinements?
**Liudmila Molkova** 06:44 We can merge. My worry is that there is some duplication here.
Like, it's literally copy-paste from Spanse.
**Trask Stalnaker (Microsoft Corporation)** 06:52 And… Why?
So, sorry, I'm not quite following why, the metrics… is overlapping with the spans. How would span refinement solve that?
**Liudmila Molkova** 07:12 Okay, so… In order to share the… the customizations here, right? What we do usually is that we have an attribute group, and we inherit from it In both spans and metrics.
Here for refinements, it's V2 only, there is no inheritance, but you can.
**Trask Stalnaker (Microsoft Corporation)** 07:37 Oh!
I see, because the span is V1 schema, that's why… and this is V2. Okay, I understand now. Thank you.
**Liudmila Molkova** 07:48 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:49 Sounds good to… yeah, cool.
clean up in these PRs.
**Liudmila Molkova** 07:53 Yeah, and I'm not super worried about, like, letting it in and then following up with span refinements, it's just that If… There is something that happens in between, we'll likely miss it, and there will be some inconsistency.
Okay, but I'll help people, it should be relatively easy to do.
Okay, so these are the… PRs.
There is one more.
It's pretty minor.
But it closes a lot of.
issues. This is the thing we discussed last time, that It's just a little bit over-explains what we have documented elsewhere.
But since it raises so many questions, I'd like us to explicitly say that instrumentations May use additional context or configuration to customize what's in error.
**Madhav Bissa** 09:18 So, an update around this, I think we discussed last time… This is about the error codes for server side, right?
**Liudmila Molkova** 09:26 For both.
**Madhav Bissa** 09:28 Yeah, I mean, specifically the server side. On client side, everything not okay is still an error.
So, I did speak to the leads in GRPC, and they agreed to the… Design decision that we discussed last time Trask about having a configurable list.
That allows users to… Decide what they want.
As error, and what they don't want as an error.
And we can, give… Default hotel… Semantic conventions aligned list.
If someone wants, they can choose that, or… they can stick to what GRPC semantics Suggest, or they can even customize.
So that's the reason why my, proposal for proposal for all these changes is not yet out, because I'm still incorporating that part, so it will be out probably today or tomorrow.
Yeah, but they agreed in principle to what we discussed.
**Liudmila Molkova** 10:35 wonderful.
**Trask Stalnaker (Microsoft Corporation)** 10:36 Cool.
**Madhav Bissa** 10:37 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:43 So for this PR, Limila… These instrumentations.
Harm.
I'm gonna use… so, certainly, configuration options.
is… a no-brainer.
additional context. What do… what do we mean by… additional context that I might use.
**Liudmila Molkova** 11:12 Is that like…
**Trask Stalnaker (Microsoft Corporation)** 11:13 For, like, around cancellation and things that maybe it… are ambiguous sometimes.
**Liudmila Molkova** 11:20 I would imagine that if you know that there is a timeout.
And you know that the specific cancellation is this timeout.
At.
Wow.
You can still make an argument.
At.
We can remove additional context, but that's the the clause we use everywhere else in Http in the recording exception recording errors document.
**Trask Stalnaker (Microsoft Corporation)** 11:51 Oh, okay, so this is standard, standard language.
**Liudmila Molkova** 11:55 Yeah. So like we imagine that you have a specialized implementation.
**Trask Stalnaker (Microsoft Corporation)** 12:00 Status codes… Okay.
**Liudmila Molkova** 12:21 And it's just the same thing repeated.
Over and out.
**Trask Stalnaker (Microsoft Corporation)** 12:25 Yeah, yeah, yeah.
Alright.
Looks good.
**Liudmila Molkova** 12:33 Awesome.
So that's it for the ongoing work. And have you mentioned that GRFC is still in progress?
**Madhav Bissa** 12:46 Yes, that's the last part that I discussed with them. I got an approval from them on Monday. I've not been Able to incorporate that yet, so, yeah.
Hopefully today.
**Liudmila Molkova** 12:59 Yeah, sounds good. Thank you.
**Madhav Bissa** 13:02 Yes.
**Liudmila Molkova** 13:03 We still have an issue for the histogram boundaries.
And I think what we discussed last time is that for GRPC We would document… What GRPC does?
But for everything else, we will… update the… Update what we have.
I think it's not in progress.
Yeah, but it's in our to-do list.
**Trask Stalnaker (Microsoft Corporation)** 13:41 Yeah, and I mean, the question was whether we wanted to… so definitely, we would, the gRPC will… Lock in those bucket boundaries to what you're doing today. It might have… But I keep going back and forth on whether we should change the default.
RPC histogram buckets.
Because, I mean, like… HTTP… Http is also can represent very fast requests. I mean, if anything, Rpc. Is on top of Http. A lot of times.
So, like, in that sense.
It… feels fine to use the… our HTTP. Like, we haven't heard a lot of complaints about the default HTTP Bucket boundaries.
I think people… who need… You know, more fine-grained ones.
I mean, people tune them.
For… cost, and… What they need.
And we have… we always have exponential histogram bucket boundaries as well for basically unlimited granularity.
So, I… I think I've… I've talked myself into that it's fine to leave them.
But I… I don't… I think it would be fine to also… add more fine-grained ones, I guess.
I don't have a strong… feeling there.
**Liudmila Molkova** 15:31 Given we didn't have any feedback for HTTP.
R.
**Madhav Bissa** 15:41 But isn't, like… HTTP… By.
I am not aware of other RPC systems, how they perform, but aren't they, like, faster?
in most cases than HTTP.
Because usually RPC systems would be used within.
the network for… Inter-service communication, and they would operate at much faster speed, then… General HTTP… Calls, so then the bucket boundaries should reflect those latencies, right?
**Trask Stalnaker (Microsoft Corporation)** 16:26 I mean, think, though, of, like, all the HTTP, you know, REST microservices, REST APIs over HTTP microservices that exist. They're essentially RPC, they just… aren't using an RPC framework.
**Madhav Bissa** 16:51 Yeah, I'm too inexperienced to comment on that, but I, like.
Everyone will have a typical range of.
Latencies that they operate on.
Usually.
And it need not be same between different RPC systems. It's… What I'm saying, so the bucket boundaries that we are defining over here.
should align closely more with the RPC systems that we are defining the boundaries for.
And it shouldn't matter how HTTP Or what HTTP is doing.
**Trask Stalnaker (Microsoft Corporation)** 17:33 Your… your bucket boundaries today include… what's your largest boundary… bucket?
**Madhav Bissa** 17:41 Launch… I don't remember everything.
Specifically, not the largest ones.
**Liudmila Molkova** 17:49 100 seconds?
**Madhav Bissa** 17:53 Yes…
**Trask Stalnaker (Microsoft Corporation)** 17:57 Jared E. So that's actually slower than our largest bucket boundary.
**Madhav Bissa** 18:04 Yes, but this is for… very long-running streaming RPCs.
Exactly, so that's what I'm saying, so the… The boundaries should make sense for the specific RPC systems, right?
If we are opening up a stream, and let's say the same stream is used for A huge number of individual.
Messages being sent on the stream.
Then that can extend.
long time.
I mean, let's say if it's just a unary RPC.
on gRPC… Client and server.
And it's a very small payload, it would be much faster than… HTTP, so the… even the… Lower end of the bucket boundaries is.
Much smaller than… HTTP.
So.
**Liudmila Molkova** 19:15 I can see that for like streaming for HTTP, we would not capture the duration of the stream, right?
**Madhav Bissa** 19:25 Yeah, there won't be any stream.
**Liudmila Molkova** 19:27 Well, there could be a stream, but we want we just for HTTP we don't capture it for RPC for for streaming would capture the duration.
And.
as Probably, like, the percentile stopped making sense if you, like, establish a stream for 10 minutes.
But, like, the correctness might still be interesting.
So maybe we do need, at least sometimes, different bucket boundaries.
But I think that the the most interesting part is whether we want.
More… faster ones, right? And maybe we don't need that many in the middle.
for, like, the generic case. Like, I think what we're talking about is the gRPC will get its boundaries in the gRPC page.
There will be something in common, just because we want to provide some basic considerations, right? We already provide them.
And other systems can overwrite if they need to.
It's not a question of whether they have different ones, they can.
more of a… What is the reasonable default could be?
**Trask Stalnaker (Microsoft Corporation)** 20:53 And, you know, as I'm looking at this, this was so copied from HCDP, which is before we kind of established that.
our pattern for bucket boundaries. So this actually has more in the middle than we… Has one more, or two more… No, I mean, it matches this, but it doesn't match, sort of, the… the… What did we use it for?
I guess we kind of used it for, we have a issue… I think I linked it from Madhav's issue, if you find it. It was Jack, had proposed, sort of.
Jack and I had kind of discussed and proposed some guidance.
Our general bucket guidance from that issue.
Oh, okay, so Jack has the 3 inner bucket boundaries down below, that matches HTTP, but we could… we could reduce that.
To, sort of, one inner bucket boundary.
And cover more range.
Without… adding more buckets…
**Liudmila Molkova** 22:31 Yeah, What do you think about conditional boundaries, streaming versus Hunery?
**Trask Stalnaker (Microsoft Corporation)** 22:45 How would that work?
**Liudmila Molkova** 22:49 Oh, I see. Yeah, it wouldn't.
Yeah, okay.
So, more range, with the same number of buckets.
Okay, and tennis… Definitely kind of low.
Okay. Trash, would you?
**Trask Stalnaker (Microsoft Corporation)** 23:28 Oh, and gRPC goes up to 100?
**Madhav Bissa** 23:34 you.
**Trask Stalnaker (Microsoft Corporation)** 23:35 So we could do 10, 50, 100, and then we could do… probably one extra… Order of magnitude on the lower end.
As 500 milliseconds, 100 milliseconds.
And we'd probably end up with… More or less the same number of buckets.
**Liudmila Molkova** 24:04 As here.
**Trask Stalnaker (Microsoft Corporation)** 24:06 No, as we had before.
**Liudmila Molkova** 24:08 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 24:12 Yeah, I can…
**Liudmila Molkova** 24:13 you.
**Trask Stalnaker (Microsoft Corporation)** 24:14 Yeah, I'll send the PR for that.
**Liudmila Molkova** 24:18 Awesome.
Okay, we have 4 minutes. There is one more thing, on our board that I think is worth addressing.
Oh, if I can find the board… So most of the things in to do are essentially things we are working on. I just discussed.
So, or to do it in progress. So, talked about histograms, this is just the stabilization stuff.
There is one more thing.
That I'll probably want to make a call on.
I wanted to send a PR, but I didn't.
And we won't have time to talk, but I just want to introduce this and see if we can… Maybe talk about it more next time.
So the TLDR is that how useful are spans for streaming calls?
And… It seems the answer, it depends.
But… Also, it's not clear… Well, there is no harm in the spans per se. They're probably very low volume anyway. You can only have that many sticky connections, right? Concurrent.
But it seems the negative effect.
Is that if we make the context current.
Then, depending on the implementation.
Anything that's reported within the stream could… Share the context.
So, I've been thinking, and I think what we can do.
Is.
maybe to… Not even make context current.
For streaming calls.
Or make it some way of opt-in behavior.
The other thing we can consider is to report storage step events.
But I don't think it's helpful.
Because, okay, we report start and stop events. Well, start event is kind of interesting, because you see that something has started not after it ends, right? Especially if it's… If it ends non-gracefully, and we never report this pen. But… If we just report events, we still need some means to correlate them.
And we'll just invent the context without the context.
So I'm kind… and we can always add events later.
So, I'm thinking that we… I'd like to keep the span, but just remove the harm.
That potentially comes from, from the ambient context.
**Trask Stalnaker (Microsoft Corporation)** 27:52 I'm just trying to mental… mental model it. So, you have a… you have a long running Stream… And… The things that are done inside of it.
on.
I'm trying to think why you… So, the reason why you don't want The parenting is just because… Chris H: Because it's the wrong parent, because there's a better… I'm not quite sure I'm… Oh, perfect.
Figured why you don't want the parent.
**Liudmila Molkova** 28:36 because the… you establish a connection, it's essentially a connection.
And the things that run within the stream.
Are effectively independent of this connection.
An example… Which is slightly related.
**Trask Stalnaker (Microsoft Corporation)** 28:59 No, go ahead.
**Liudmila Molkova** 29:01 Like, in MCP case, there is the longest running Like, the client connects to the server, it just connects, and then this channel is used for, like, notifications, which are completely independent of the start context.
**Trask Stalnaker (Microsoft Corporation)** 29:20 I see. So there wouldn't have any parent, but that's what we want, because it's not really tied to the connection anyways. It's an independent.
**Liudmila Molkova** 29:33 Kinda, and it's a tricky question, right? Because I can easily imagine it depends on the application, what they want.
I'm.
**Trask Stalnaker (Microsoft Corporation)** 29:43 And if you do have… if you're propagating context.
in those messages, like MCP, right, we're propagating context anyway, so that would Be the parent in that case.
**Liudmila Molkova** 29:55 Right. Yeah.
So the key question is, is it a good assumption that in BD streams.
The messages that flow through are independent of each other.
Maybe it's a question that you might have for everybody else.
**Madhav Bissa** 30:21 Sorry, can you repeat the question?
**Liudmila Molkova** 30:25 Like, is it a fair assumption that in most, like, it's common for BD streams?
To have the streaming as just the transport, and messages within the stream are largely independent of each other.
**Madhav Bissa** 30:44 That completely depends on the application.
We don't decide what goes into the message.
**Liudmila Molkova** 30:58 When… Your report.
Message events, I think you report them as spend events, right?
**Madhav Bissa** 31:07 No, each message is not a spam.
**Liudmila Molkova** 31:10 Spend event.
**Madhav Bissa** 31:17 I'll have to check that.
**Liudmila Molkova** 31:19 Don't worry, like, we can check, we can… we are out of time anyway.
But, okay.
Let's talk about it next time, and I'll think more about it, and maybe do some research.
**Trask Stalnaker (Microsoft Corporation)** 31:35 Yeah, and I mean, I think it's okay if it's.
If it's a it depends kind of thing, and we decide that, okay, least harm is not to set it to current as the default.
I'm… that… Sounds reasonable. I mean, there's certainly a good argument to be made for connection-based Stuff that… I mean, a lot of those Yes, a lot of those bidirectional streams are, like, established ones that, like, applications start up and then, you know, continually are just always there.
So, it… Easy argument to make.
**Liudmila Molkova** 32:16 Yeah, and I think this is the… we can… we can do this, and I'll see if we can do anything better.
**Trask Stalnaker (Microsoft Corporation)** 32:23 Cool.
Thank you.
**Liudmila Molkova** 32:25 Awesome. Thank you. Good to see you all. Have a good night, Madhav.
**Trask Stalnaker (Microsoft Corporation)** 32:29 I…
**Madhav Bissa** 32:30 Bye, thanks.
