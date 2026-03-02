SIG: RPC Sem Conv Stability SIG
Date: 2025-10-08
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao** 01:36 Hey, hi, Chaska.
**Trask Stalnaker** 01:38 Hey, Steve!
How you doing?
**Steve Rao** 01:41 I'm good.
Yay.
Yeah, today is the first day of, after our holiday.
**Trask Stalnaker** 01:49 Oh, yeah, yeah, welcome back.
**Steve Rao** 01:52 Yeah.
**Trask Stalnaker** 02:20 Hey, James.
Alright, I think that Lydnila is… Out.
**Steve Rao** 02:52 Okay.
**Matthew Hensley / Grafana Labs** 02:53 Yes, Lou Miller's out this week.
**Trask Stalnaker** 02:56 Cool.
Why, yes.
You're both at Grafana now.
I can see…
Let's… Dart with the board.
Alright, let's… Look at our in-progress stuff.
Okay, looks like this is… Ready, but just… Probably need to wait for… Let me lie…
This one… let's see, it's back in draft, waiting on… Jrpc.
**James Thompson** 04:26 It's… Yeah, there's a… I think there's 3 PRs that's waiting on the gRPC one.
**Trask Stalnaker** 04:34 Okay.
**James Thompson** 04:36 Yep.
**Trask Stalnaker** 04:38 Because either…
**James Thompson** 04:40 Either gRPC gets merged first, and then I rebase the draft ones.
Or merge the other ones, and then have to rebase gRPC.
**Trask Stalnaker** 04:52 Okay.
Let me, skip.
I will see if I can get, another maintainer.
To look at this…
Alright.
Got it. So, just from a merge conflict perspective… This one is blocked, okay.
Even from a merge conflict perspective, though, we could still review it.
**James Thompson** 06:00 Yep.
**Trask Stalnaker** 06:06 Let's see… fixes… Add network protocol name version 2 span and metrics.
It's… What is, size duration?
The metric… oh, the metrics related to size, duration, right now on that, okay.
**James Thompson** 07:05 Yep.
**Trask Stalnaker** 07:07 They're on all of the RPC metrics, right?
**James Thompson** 07:12 Corporate.
I've just… it's literally just been added to the…
**Trask Stalnaker** 07:20 Sorry, last, last… thing you said.
**James Thompson** 07:23 It's… yeah… It was added to the common attribute group for metrics, and the common attribute group for spans.
**Trask Stalnaker** 07:31 Okay, so can we simplify this and just say on the spans, now on…
Well, do we need, no ads to all…
Do we want to say all RPC spans and metrics?
Okay, and then probably we don't… Probably we don't need… this, then…
Okay, this is just… Table generation…
More table generation…
I wish when there was an easy… Way of, like…
Automatically hide from the diff everything that's auto-generated.
**James Thompson** 08:51 Yeah.
**Trask Stalnaker** 08:53 Okay, so then we add to… RPC… Client… Okay, metrics, RPC, client… Okay, and…
this one, ID, RPC…
**James Thompson** 09:17 And let's use both Spain.
**Trask Stalnaker** 09:19 Let's use… okay.
And what about our PC… so, our PC server…
Doesn't have protocol, doesn't have it.
**James Thompson** 09:34 It extends from RPC.
**Trask Stalnaker** 09:38 RPC metrics…
**James Thompson** 09:41 The group RPC is used by client and server.
**Trask Stalnaker** 09:46 But what about this one?
**James Thompson** 09:48 It extends from the one above.
**Trask Stalnaker** 09:51 Extends… oh, I see, gotcha. Thank you. I see. So what does it do? It extends and… okay.
Perfect.
Okay, so comments were only on the changelog entry.
You said there were 2 more blocked on…
**James Thompson** 10:22 Yep, they're in the no status.
**Trask Stalnaker** 10:25 No status, okay.
Gotcha, so that one is in progress.
Progress, let's see… Error type.
Let's see, our issue… error type…
spans now contain RPC…
PC.error type.
Is that what F, or…
**James Thompson** 11:34 No, it should be… it should be just the AirTalk.
**Trask Stalnaker** 11:36 Okay, okay.
**James Thompson** 11:38 Yep.
**Trask Stalnaker** 11:47 Did I submit that last review?
I forget to do that a lot. I did, okay.
**James Thompson** 11:53 the arc.
**Trask Stalnaker** 11:54 Cool.
her type.
Following well-known values, other… Yes, our standard.
your type…
I assume this is on… ID, and this is… so this is only for spans.
**James Thompson** 12:49 Yep.
**Trask Stalnaker** 12:51 do, is… Adding it to metrics something different, or something we don't want to do?
**James Thompson** 13:01 Metrics has already been done.
**Trask Stalnaker** 13:04 Oh, it's already on Metrix.
**James Thompson** 13:07 Yes, I believe so.
**Trask Stalnaker** 13:15 Indeed.
Hmm, okay.
And I just want to check… on the RPC metrics…
here.type… Soon… Object name…
**James Thompson** 14:15 Yeah, we're probably coming by the group.
**Trask Stalnaker** 14:20 And the group would be under comment.
**James Thompson** 14:23 Correct.
**Trask Stalnaker** 14:29 Metrics, RPC client, gotcha. RPCF… Okay, and that is exactly…
**James Thompson** 14:37 Yep.
**Trask Stalnaker** 14:39 Same thing…
Yes, and… Only if… the… oh, I see, this is span status is…
**James Thompson** 14:52 Error.
**Trask Stalnaker** 14:56 Yes.
For other ones, what do we say?
**James Thompson** 15:23 I'm pretty sure I copied it from HTTP.
**Trask Stalnaker** 15:27 Yeah…
So I wonder if, over here, if this is shared… Operation failed.
Span status…
I was trying to think if there's any issue with citing span, tying it to span status specifically, and or why we haven't done that previously.
**James Thompson** 16:58 Amazon?
Doesn't the recording error document state…
To do this, this way, set error type when span status is error.
**Trask Stalnaker** 17:16 I don't know, I'm looking for…
this text in these semantic conventions, and I'm not finding that specific text.
But it could very well say that in a different way.
So, in… Recording errors… Error.type…
out of the errors…
Oh, do we see anything about spam status?
Guardian era…
**James Thompson** 18:12 Yeah, so it says… When an error set the status code to error, should set the error type attribute.
**Trask Stalnaker** 18:25 Yeah, yeah, I was just thinking, I mean, it doesn't look like we use this terminal, like, this specific.
thing elsewhere…
And just thinking of making it, like, agnostic of span status, even though it's under spans, like, it's…
**James Thompson** 18:42 Oof.
**Trask Stalnaker** 18:43 Essentially the same, we could just say operation, the same thing that is listed in the metric…
If and only if the operation failed.
And…
Network local.
**James Thompson** 19:40 Yep, it's the same as HTTP.
**Trask Stalnaker** 19:52 And these are… these are opt-in on HTTP, right?
**James Thompson** 19:56 Correct.
**Trask Stalnaker** 19:56 Okay.
**James Thompson** 19:58 Yes.
**Trask Stalnaker** 20:00 Hmm…
Local address, network local port.
Do we say… So, one question is if we…
Feel we need to add them… in… since… They're automatically opt-in, basically.
I think in… let's see what we do in… we might have brought them into metrics, I mean, into HTTPS opt-in.
Specifically to add more context about how to capture them.
Let's see… HCP YAML… Bands… Order… Whoa.
Server spans… Should we put them on metrics?
No…
**James Thompson** 21:45 Nope, it's on the spam.
**Trask Stalnaker** 22:05 Yeah, let's hold on this one, till Ludmilla, because I'm kinda…
curious. I'd like to know her thoughts on… weather…
This is imp…
important to even add, right, given that, I mean, you can always pull things in as opt-in.
Unless there's something important we want to say in the brief, and, you know, we definitely could just copy this over.
**James Thompson** 22:39 Yeah, and that's what I did do. I copied that brief.
**Trask Stalnaker** 22:43 Oh, did I miss that?
**James Thompson** 22:50 Oh, no.
Authority.
**Trask Stalnaker** 22:56 Yeah. Yeah.
I would… yeah, go ahead and…
**James Thompson** 23:06 But also, what's the default brief?
I might have had it and removed it when I saw the default brief. What's the default?
**Trask Stalnaker** 23:16 Local address of the network connection, IP, local port number of the network connection.
Yeah, I mean, I agree, this is… Maybe not terribly useful.
That much more useful.
I'll leave a comment.
Let's see, there was…
**James Thompson** 24:21 You need to finish your review.
**Trask Stalnaker** 24:22 Thank you.
Oh, I forget that too often.
I wish there was, like, a… Github would auto… Like, if you haven't commented.
Updated it. In a few minutes, it would just post it.
Okay.
Yes, the other ones I remembered because I hit approve. Yes, okay, this is my problem.
What did I do here? Oh yes, I saw you approved this, thank you!
So we should move that to… In progress…
Alright, let's see what we've got. Remove network type from RPCs.
And…
**James Thompson** 25:26 Best in progress.
That's the one you assigned to Copilot.
**Trask Stalnaker** 25:35 So, in progress…
It's a… Kate… Oh, JSON RPC, yes.
Rename, align…
BB Messaging…
Okay.
I think I saw one…
From you, James, the RPC briefs.
And I was going to suggest…
Let's… Since we're going to… let's wait until we…
switch this over to RPC, protocol.name.
Oh, speaking of that…
Let's look at your PR about…
guidance for RPC protocol versus framework.
Yeah, sometimes. When in Java only.
**James Thompson** 27:39 Yeah.
**Trask Stalnaker** 27:40 Oops.
I'm not sure that's… yeah, I would… Probably support just dropping this.
I just don't think,
RPC…
Oh, oh, I see, it's a separate doc that… oh, I know, a separate section, okay.
So, I notice you're using rpc.transport.protocol. Why not just rpc.protocol?
**James Thompson** 29:16 So, I originally did have RPC.protocol, But… I… are more… I didn't feel it was…
Pacific enough to indicate this is for the transport.
Right? Because we're only talking about how it's transported.
**Trask Stalnaker** 29:42 Yeah.
So… I mean, I would… I'm… my inclination is to go, like.
I feel like the RPC… the trans… the protocol is the important thing that we want to capture.
And highlight.
in the similar sense of, like, it's the corollary to db.system.name…
**James Thompson** 30:17 Or messaging.system.name…
**Trask Stalnaker** 30:21 is rpc.protocol.name.
**James Thompson** 30:25 Yep.
Yeah, look, I'm not phased either way.
Right. Yeah.
**Trask Stalnaker** 30:32 Okay.
Where… so… Yeah, where do you… I'm trying to think of where this should live.
**James Thompson** 30:45 Yeah.
**Trask Stalnaker** 30:47 Hello.
**James Thompson** 30:47 At the moment, I have it on just the general RPC page.
**Trask Stalnaker** 30:55 Yeah, I'm, like, once we have, say…
I mean, can this be more just, like, RPC, when we… Add rpc.protocol.name, And…
define there what a protocol… what RPC protocol is.
**James Thompson** 31:22 Yeah, I think quite a bit of it could be moved across to there.
Alright?
Right? But I also think having on that landing RPC page Right?
Because we want to list what are the protocols that we're documenting.
**Trask Stalnaker** 31:42 Oh, I see with the tie-in.
**James Thompson** 31:46 Yeah, right, so you can go to the RPC page and see what… you've got gRPC… etc.
**Trask Stalnaker** 31:59 I see, okay, so because the sub… okay. So… that makes sense… Protocols.
I think I would… Let's see, let's look at… Database…
I think I would pull that, let's see…
pull that up higher, kind of like with database, where, like, that's, you know, I mean, that's, like, what the next thing you want to know after kind of generic
And… Here are the… RPC protocols, and then…
I think I would almost, like, have that… underneath there of, like… What?
This, sort of, as an explanation of That of this list.
**Steve Rao** 33:28 Yeah, I have a small question, just as I left my comment here.
**Trask Stalnaker** 33:36 Yeah.
**Steve Rao** 33:37 Yeah.
I think, yeah, you can scroll up, yeah, maybe we can see the RBC protocol.
Here, he lists some protocol.
Yeah, I think, it's not very clear here. Maybe, give my… the feeling there are some protocol, and, maybe I click on the protocol name, I can, understand, I can get the link about the introduction of the protocol.
But now it's a link to the semantic convention.
Oh, okay.
**Trask Stalnaker** 34:18 Hmm…
**Steve Rao** 34:21 So, it's a bit different.
Compare with other semantical.
**Trask Stalnaker** 34:31 Yeah, that makes sense to me.
I, I kind of… About… Go ahead.
**James Thompson** 34:37 I'm not following, because if you look at the database one, you have…
the list of the database providers, and then you click on it, and it takes you to Semconv, anyway.
So…
**Trask Stalnaker** 34:50 Right, the difference is that here it says, technology-specific semantic conventions.
Are defined for these, And here… It's just saying, you know, some…
**Steve Rao** 35:05 hospital.
**Trask Stalnaker** 35:06 transport protocols, these are some transport protocols, as opposed to, like, these semantic conventions for transport protocols.
**Steve Rao** 35:19 Yes.
**Trask Stalnaker** 35:26 Does that… Make more sense?
**James Thompson** 35:31 Okay, then we'll just rework the wording.
Right.
**Trask Stalnaker** 35:35 Yeah, yeah. It's all just wording.
I do think I would highlight… I do think I would pull these up.
up here… Marissa's should the press be removed?
Yeah, up much higher, like, maybe, like, right here.
Because, like, the list of… that's one of the main things you come to this page, and you're like, okay, I'm reading, and oh, I really want GRPC.
semantic convention, so I want to click on that link.
I don't want to read our definition of RPC Transport Protocol versus RPC Framework first, before I get to that link.
Now do you think that this… oh, I see some… yeah.
And I think I would… I mean, my preference would be to focus on transport protocol.
And defining that, since that's what our drill downs are.
And you could compare it to an RPC framework, but, like, I wouldn't…
probably link to here, because I feel like this
I don't know, it gets a little confusing, but I can take a closer look.
But I guess my main feedback there would be to bring the… Transport protocols up.
Here.
I can leave a comment.
Outcome extended…
Cool.
Wait, I was gonna leave a comment here…
I like to… Comment on files so they can be collapsed later instead of commenting mainline, if possible.
**James Thompson** 38:49 But also, at the same time, those briefs don't touch any of the RPC.system.
So…
**Trask Stalnaker** 38:58 Oh, they don't?
**James Thompson** 38:59 RPC? No, no.
**Trask Stalnaker** 39:01 Okay, my bad.
Okay, thank you.
So what… our RPC spans… Registry…
**James Thompson** 39:18 It's… It's providing description of what the error codes mean?
For Connect RPC?
**Trask Stalnaker** 39:32 And…
**James Thompson** 39:33 and message time.
**Trask Stalnaker** 39:34 OTC message type. I see.
**James Thompson** 39:44 And those… those texts are copied straight from the ConnectRPC docs.
For the error code.
**Trask Stalnaker** 39:50 Okay.
Okay, so this just… this falls into the…
Enum brief, the general enum brief quandary.
So, we can… Come back to that.
**James Thompson** 40:10 I think the other topic we need to think about is how we handle JSON RPM.
Be safe.
Right, because that was one I deliberately left off RPC framework versus protocol, because… It's…
If you really look at it, it's more of an envelope of how the message is structured.
Right? It's what the data is in the payload.
Alright.
So, is it more a message specification? Because if you really… you can do it over HTTP, if you really wanted to, you could do it over gRPC,
Alright, it's just specifying what the message looks like.
So, I almost see it like cloud events, where it just defines a message.
Definition.
**Trask Stalnaker** 41:51 Would you… Would you ever do…
JSON RPC over another RPC protocol.
**James Thompson** 42:05 You, you, you do it like…
with HTTP, you do a standard I.O,
Those are the two most well-used ones for it.
**Trask Stalnaker** 42:19 So, I mean, while… It may not… meet…
quite the same definition as our other RPC protocols. If we did add it as an RPC protocol, at least it wouldn't
Be, like, some weird overlap thing.
**James Thompson** 42:42 But you could also do it over ConnectRPC.
Alright.
**Trask Stalnaker** 42:46 Kenya?
**James Thompson** 42:47 Yeah, because all it is is a JSON envelope. It's specifying what the JSON envelope is for a message that's sent.
Pick it.
Because, yeah, it's just specifying what that JSON properties are.
**Trask Stalnaker** 43:28 Does, I assume, connect RPC… So, like, like, they define status codes…
Right.
**James Thompson** 43:41 Yeah, they define status codes.
But JSON RPC just defines a value of the properties in the envelope.
**Trask Stalnaker** 43:52 Which includes status.
Don't they have a status?
**James Thompson** 43:56 There is an error code one.
There is one error code property.
Yeah. Alright.
Yes.
**Trask Stalnaker** 44:28 Sorry.
Steve, from the… Double…
I forget, you support gRPC, you support double native protocol, do you support Connect RPC or JSON RPC?
**Steve Rao** 45:10 No.
**Trask Stalnaker** 45:12 Okay.
**Steve Rao** 45:21 But, yeah, recently, yeah, if I remember right, there is a PR to support, to support,
JSON RPC, in… Hotel, Java Instrumentation report.
Yep.
Yeah, you can scroll, down. And, yeah, I… I saw you left a comment.
Ew.
**Trask Stalnaker** 46:12 Oh, yeah, yeah, yeah.
**Steve Rao** 46:33 Yeah, if we want to support it, maybe we can, yeah, support it best on this PR.
**Trask Stalnaker** 46:47 So, but the question is, do we…
Are we comfortable? And, well, sorry, we just hit our time, so I think this is a complicated question, so let me just write it down here.
**Steve Rao** 47:05 Yeah, baby.
this.
**Trask Stalnaker** 47:08 JSON RPC is… JSON RPC… A receipt protocol… Hmm…
Okay, actually, I do think that's probably worth…
Issue…
**James Thompson** 47:48 There is an issue.
**Trask Stalnaker** 47:50 Oh, there is for the… Okay.
PC… JSON RPC…
**James Thompson** 48:02 Yeah, capture the message specification is where I talk about it.
Right? Because that's what I came up with when I was looking at JSON RPC, trying to work out how it fit.
**Trask Stalnaker** 48:27 Okay, let's just blink that…
Okay.
Cool, we will chat more about that.
Tricky one.
Next time, if we don't have any… Ideas before then.
Alright, thank y'all.
**Steve Rao** 48:58 Yeah, thank you.
