SIG: RPC Sem Conv Stability SIG
Date: 2026-06-25
Duration: 120 minutes
============================================================

## Zoom Recording Transcript

**Trask** 04:43 Hey, Meadow.
**Madhav** 04:45 Hey, Tras, how are you?
**Trask** 04:48 Dang… Well, actually, I woke up here, and power is out at our house.
**Madhav** 04:57 Oh.
That's a shame.
**Trask** 04:59 Yeah, yeah, so I will just… And then on my face here over…
**Madhav** 05:05 Like, your house, electric, Connection issue, or just the entire area has some problem?
**Trask** 05:13 It's the area, but we live out, Kinda in… Slightly rural, forested area.
**Madhav** 05:24 Oh, okay.
Nice. Where do you live, man?
**Trask** 05:27 Outside of Portland, Oregon.
**Madhav** 05:30 Okay, nice.
**Trask** 05:33 So it's… we lose, we lose… unfortunately, we lose power kind of a lot during the winter months, with, like, trees falling on things, power lines, but it's unusual to lose power in the summer.
**Liudmila Molkova** 05:50 Oh, you're on the shower!
**Trask** 05:52 Yay! Yay! I don't know what happened. Yes.
But they did give us an estimate already, like, it's, only 4 hours, hopefully.
Which is… since it's unusual, they don't have In the winter, it takes a lot longer, since there's lots more power outages around anytime, and… We usually get deprioritized since… Not very much density.
people here.
**Madhav** 06:26 Okay.
Cool.
**Liudmila Molkova** 06:31 Telemetry is stuck… gets stuck without trust.
**Trask** 06:36 I'm here.
**Liudmila Molkova** 06:40 Yeah.
Okay, so let's see… What do we have?
**Madhav** 06:45 So… Right. I wanted to… Just update. So, I had an internal alignment with all the leads, and we basically have gone through the entire stuff, entire semantic convention proposal for gRPC from OpenTelemetry.
And, I think, Lyudmila, I gave you, Uncooked version of what was discussed.
So, there are some changes that, we want to request. Can I just file, like, a GitHub ticket for that?
**Liudmila Molkova** 07:20 Yeah, absolutely.
Do you want to present them here, or do you feel…
**Madhav** 07:26 I am okay with everything, so I was just busy filing the ticket, maybe I'll just present it, and then if you need any more details, I can add them in the ticket before I file it. Let me share my screen.
**Liudmila Molkova** 07:36 Oh, wonderful. Okay, let me stop sharing.
**Madhav** 07:44 So… I won't share… Right.
So… Yeah, let me start with the metrics part first. So, the first problem is we need to have the documentation section in the metrics.
Populated, currently it's not, and then there's a lot of confusion as to… What has to be read from where?
Okay.
Because I think the span section is very detailed, and for metrics, it says just refer to RPC metric convention, and over there, we have generic metric descriptions, but then we have specific attribute meanings, which are described in the span section, and the loop doesn't close. So we should basically have an explicit section for the metrics.
Then.
**Liudmila Molkova** 08:54 Can we stop here for a sec? It's… I have a question, but not to you, but probably more to Trask and Steve, or everybody.
It's… in semantic conventions, we historically, like, break down things into span metrics, logs.
I want to propose refactoring, and maybe our PC is the good place to start with it. It's where we focus on operations.
And we also, like, there are some new features in semantic conventions where we can actually specialize RPC metrics to gRPC and, render a table.
try to see if my dad… do you think it would be useful to just refactor, starting with RPC, and focus on individual operations, span metric.
And then, yeah, we'll do the refinements for gRPC.
**Trask** 09:56 Yeah, I mean, sounds… sounds fine. I'm trying to follow the… is the… Problem that the metric Age… the duration, kind of references the span, duration.
The descriptions, the operation descriptions that are present in the span page.
**Madhav** 10:21 No, it doesn't reference anything. Right now, the metrics section is empty. It just says go to RPC documentation.
But the actual explanation is in the spans section, which is never linked back.
So, it's, like, currently… All over the place.
**Trask** 10:43 If you give me a sec, I just want to pull it up and… See what your… what we're talking about.
**Madhav** 10:52 Sure.
**Liudmila Molkova** 11:07 So, to our side of that.
metric, there is a metric section in your PC Doc.
And it says that it points to the general semantic conventions for PC metrics.
And it does not explain that the attributes are specialized, right, to gRPC.
**Trask** 11:28 Oh, I understand what the… Sorry, I thought we were talking… Yes, yes, so it's the GRPC metrics section that is…
**Madhav** 11:41 Yep.
**Trask** 11:42 Yes.
**Madhav** 11:43 Oh, sorry, I have the wrong link over here. Sorry.
I should mention GRPC metric section, sorry.
I think I've.
**Trask** 11:52 It's early, and I have no… I've had no coffee because of no power, so…
**Madhav** 12:00 Nobody's not honest.
**Trask** 12:03 Yes, yes, that is… Certainly.
**Liudmila Molkova** 12:07 And now, we can render the actual table there, right?
**Trask** 12:11 Right.
**Madhav** 12:15 Okay, cool.
Can, can we move her?
**Trask** 12:20 Yeah, yeah, Lydmilla, to,
**Madhav** 12:23 I have… I'm going to file a ticket, so you will get… get all of it.
**Trask** 12:29 Okay, sounds good, yeah, let's… let's move on.
**Madhav** 12:32 Yeah.
The second feedback was the general RPC guidelines for the buckets.
is very broad. We have a special, we have specific GRPC bucket windows, which are much more granular, because we operate at microsecond latency, so… We would want, like, we would want that to be explicitly mentioned in the gRPC documentation, that the buckets should be used from gRPCs.
So, there was actually some discussion around here that this could point to the actual gRPC documentation, but that sounds like the other way around. We should actually have hotel specifying the convention that, yeah, the gRPC buckets are going to be like this, and we should be pointing to That, I don't know, but it's not conclusive, like, I'll leave it to you how you want to mention it, but ideally, we should… be using the buckets that gRPC already defines, because it's much more granular, and… It makes more sense for GRPC.
**Trask** 13:42 Do you have a link there to the buckets?
**Madhav** 13:45 Sure, I will add it.
We do have it.
**Liudmila Molkova** 13:54 I'm curious, are there… Are you concerned about the default buckets? Because, like, they're highly customizable, anyone can… Pick a different set, or people usually, what we would actually recommend to use exponential histograms and then the buckets.
Explicit buckets become irrelevant.
**Madhav** 14:17 It won't make a difference if the… Will it make a difference, like, when we are defining the metric itself using Motel plugins?
If we are not emitting it as per the bucket size.
You can't really customize it, right?
**Liudmila Molkova** 14:37 You can… you can customize hotel metrics. There is an advisory parameter… That you provide during metric creation, and this is a default, unless overridden by users.
But if you have a different default in gRPC, then it makes sense.
For, for us to be in sync and, come up with the same default. So, yeah, please find the link, Oh, you already have backed steroid.
**Madhav** 15:09 Yeah, we have buckets over here. Let me ping it in the Slack channel, I will format the… document, the issues with Markdown properly after the call.
So, over there, if you will go to the metric schema.
You have buckets over there. Let me give more specifically look at it.
Yeah, this is the one.
Cool.
And, yeah, now I think I should have… Posted the message in the… Zoom chat, not in the Slack channel.
Right? But we do have buckets over there, which are much more granular, as against the default that is specified.
Then, the third thing is the RPC response status code has to be changed to a more suitable name. We want it to be RPC status code, because, response is just… and this we discussed already last time, right?
response just creates, confusion. It has a specific semantic meaning that the Status code is being generated from the response.
Then, another… point was, for the server address, I see, you have given explanations that other than DNS and UNIX, everywhere else, what we have is just, we'll just paste this string as is, the entire target string as is, right? But, The gRPC leads, actually said that, like, it's… DNS is just the only case where we are actually separating into address and port, and we might, Like, we might have other schemes and other, resolution, changes in the future, which might, again, not support the address and port split. So we just want to keep everything… map the server.address to gRPC target as is. We don't want to make the split. So if we can add that in just the explanation, that would… Like, help us keep it aligned for now, at least.
**Trask** 17:30 What about if it's a direct… Connection, just a server colon port.
Is it okay to split that?
**Madhav** 17:41 We… we will… We will never have, like, just a server call input. We'll always have scheme and authority, and, like, we will…
**Trask** 17:52 Oh, right.
**Madhav** 17:53 Yeah.
**Liudmila Molkova** 17:55 Wait, the API allows you to set address.
Like, the, the, server address and port.
Cause I'll get the dress or something.
**Madhav** 18:08 Yes, it does, it's just for the… basically for the… sake of uniformity, like, if we split it in one place, and then there are going to be some schemes which will have address and port, but which will have other things also, and we will not split over there. It will… basically, for keeping it uniform and for future as well.
They suggested that we just stick to mapping a target as is to server address. That way, we will… Never.
You know.
semantically confuse our users. That's… that's what they're trying to do.
**Liudmila Molkova** 18:50 You would still confuse them, because if they provided, not… they didn't provide your PC target.
And they provided, a regular address.
Which is supported by, at least in some languages, for… in Java, for sure.
Than they would… See their address and port.
There's one string and server address.
And everything else they use breaks them down into two different components.
**Madhav** 19:27 distributions from…
**Liudmila Molkova** 19:28 not the only thing they use, right? They also…
**Madhav** 19:31 Right, right, right.
**Liudmila Molkova** 19:33 databases and everything else in the world.
**Madhav** 19:37 Hmm… Alright?
**Trask** 19:38 Would it help if we had gRPC.target?
And that's the consistent… you know, target…
**Liudmila Molkova** 19:51 Then we would repeat it, right, most of.
**Trask** 19:54 a good time.
**Liudmila Molkova** 19:54 For most of the cases.
We can talk more about it. I… I can see the world was raised, but the idea was that if you… if it makes sense to split.
We can extend the list of schemes, and it's not set in stone, the algorithm of how things are split.
Right, and instrumentations can do an amazing effort splitting specific, or even custom, schemes.
into server import. If it's not splatable, the fallback option is always to set.
The whole thing.
So it can be extensible either way. I can also see the world where you said that The same every time.
**Madhav** 20:49 Right, right. Cool, sounds good. So, anyhow, like, what we can do is we can continue this discussion on the ticket itself, so that it is transparent for everyone, how we are arriving at whatever decision we are arriving at. I don't think we are too… rigid about this specific thing. This was more… the worry was more, if we commit to splitting it over here, there are going to be other places where we might have to split stuff up, and then there it wouldn't be performant. And, you know, at microsecond latency, adding a string split… Just for emission of metric might have a performance overhead, and that…
**Liudmila Molkova** 21:28 Bro.
**Madhav** 21:29 one of the concerns. And also, semantically, will it make sense if we add some more ways we are going to construct addresses in the future? So, yeah, that's the reason why they just wanted to keep it simple, because we already have a target attribute on our existing metrics, and they work. But let's have the discussion on the ticket itself. I think that will make sense.
**Liudmila Molkova** 21:55 Sure.
**Madhav** 21:57 Cool.
**Liudmila Molkova** 21:59 The status code you mentioned. So, the proposal is the RPC status code, for the reasons that the response is too vague and could be misunderstood.
**Madhav** 22:12 Yeah, yeah, yeah. Response means it is generated from the response of That is coming from server, and it is not coming from server, for sure.
Thanks, so… That's what… that's the reason we want to change it. RPC status code by itself will work for, I think, all our PC systems of it.
I think that that makes more sense.
**Liudmila Molkova** 22:41 Yeah, so a couple more things you have, I'm not sure what, I understand the RPC method… oh, I remember, okay, yeah.
The error type, everything that is not okay, what does it mean?
**Madhav** 22:55 Yes, so, for error type, in… there are some specific… on the client side, I think, everything that is not okay is an error. For server-side, I think there are some specific errors that I think they're mapping back to how HTTP denotes errors, right? But, in gRPC, It is not built to be able to differentiate between different types of error that are coming on the server. So, if we go specifically to… The error codes. Let me just… like, for example, resource exhausted, not found.
already exists, permission denied, unauthenticated. They can still be Caused by genuine failures of server.
And it can get propagated as error. So… the leads, they said that gRPC by gRPC semantics, everything that is not okay is an error.
So, we don't want to… Then put down specific error codes.
Which can be errors sometimes as not errors.
**Liudmila Molkova** 24:14 Okay, so the hotel philosophy, the client, the errors that their client errors, like, Not found, or… canceled by client.
Are not a server error. They show up as errors on the client.
They don't show up as errors on the server, and you're saying that For a gRPC, you treat every not-okay response state as code by server as server error, too.
**Madhav** 24:48 Right, so for a failure that is happening on the server.
the application can map it to any of these error codes, right? We have no way of knowing whether what they're doing is a… Is a good job, and it's actually an error which is… occurring because of a problem in the request that the client is making. It can easily still be something that is a problem on the server. So, the gRPC's philosophy is everything that is not okay is an error.
Because we are looking, again, because it's not an RPC status code, generally, it's not a response status code, we are looking at the status code on the RPC as a whole.
**Trask** 25:37 Yeah, I think we understand your… Position there. Okay.
you know, I… we… we will… I think what will help is we can… we'll basically take this list and sort of write up the things that are… Kinda, there's certain things that are broader OpenTelemetry conventions, right, that we need to follow to fit into the whole OpenTelemetry I'm trying to convince.
**Madhav** 26:05 So I understand, which is fine, you can respond that way, and I think they were also not very rigid about this thing. We just want you to understand the position, deliberate upon it, and see if that makes sense, and if that does, then we would want to keep the semantics for OTL version of gRPC metrics, and for the gRPC metrics itself, like, the same, and then that… Basically helps us… Yeah.
Cool, moving ahead, I think a lot of it is repeated in the span side.
there was a nitpick about text. There is something… reverse proxy lookup mentioned in the server address and port. It should actually be reverse DNS lookup. It's just a nitpick.
And apart from that, again, the same thing that we discussed for metrics about address.
and target.
And then we have network peer address and network peer port.
Here, as well, the leads said that we would want to keep the server input together.
**Liudmila Molkova** 27:16 This is… wait, so… this is the… Actual peer address and peer port.
**Madhav** 27:25 Yeah, yeah.
**Liudmila Molkova** 27:28 Wh-why, why?
We might keep them together.
**Madhav** 27:35 Same thing, performance, considerations, and we don't want to split them specifically, and… Yeah. I think for here, it is just the performance, and then… Having uniformity with… The server address and port.
**Trask** 27:53 Hey, you know what I think would really help us here on your issue is if you could… this is a list of, you know, things that you, like, request.
**Madhav** 28:01 The reasoning as well.
**Trask** 28:02 Yeah, yeah, there's no reasoning here. Yeah.
**Madhav** 28:06 Sure, I will add… I will add that, not a problem.
**Trask** 28:08 Cool. Great.
**Madhav** 28:09 Makes sense.
So…
**Trask** 28:13 Because I would say, like, for performance, for example.
Right. Or network peer, you know, some of these things can be done once.
Split once on the… at the connection level, and as opposed to having to split every single request.
**Madhav** 28:32 Alright, fair enough.
**Liudmila Molkova** 28:33 Same with Target.
**Trask** 28:35 Right, right.
**Madhav** 28:36 Boom.
Cold point.
And, yeah So, there was one more thing, I think, in the metrics section, which I didn't discuss, which was, we want to exclude RPC method original. We don't want to support that, because this will basically lead to cardinality problems, and it is already taken care of in the spans, so it is not.
**Liudmila Molkova** 29:05 Yeah, it's… should be taken care of in the metrics, right? We should mention it there, but we need to preserve the original method on the spans, where the performance is not…
**Madhav** 29:16 That's what I'm saying. So… There is a mention in the metrics as well, so we would want to remove.
Yeah. Oh, fantastic.
**Liudmila Molkova** 29:25 you.
**Trask** 29:25 tricks?
**Liudmila Molkova** 29:27 I see you want to drop it on the spans, why?
**Madhav** 29:31 Yes, so I'm coming to that. We want to drop it on the spans, because the… we already have RPC method present in the span name, for one.
And the other thing is, in the span, we can actually populate the methods straight up.
in the RPC method itself, we don't need a separate attribute. In case of metric, we populate it other, but in case of span, we can just populate it.
to be the actual value that is coming through. We don't really worry about cardinality in span of it.
**Liudmila Molkova** 30:03 Well, there are concerns. First, the… the attributes and spans and metrics should be consistent, right? So if you… truncated on metric, you should also truncate it and span the span names!
Has to have low cardinality.
Because it's very common to query based on the spend name, or to group by span name, give two up top and spend names. People calculate metrics from spans, don't ask why, but they do it a lot.
And spending…
**Madhav** 30:34 branching.
**Liudmila Molkova** 30:34 It has to have low cardinality.
**Madhav** 30:37 But span name description that OTL specifies also says.
we should populate it with the RPC method name, actually. And gRPC currently is doing that.
**Liudmila Molkova** 30:49 I think if we don't see it, properly, we should fix it, but I think what it's saying, that the RPC method should be on span name, and our PC method is the one that you, truncate, or you don't let it go unbounded.
**Trask** 31:10 Yeah, go ahead and just, yeah, write up the reasoning here, because there's some, there is some complex, you know, historic, like, re… like, thoughts.
thinking that has gone into this in the… already, that is not apparent from the semantic conventions, but we can reply with and explain why it is that way. There are good reasons, but we…
**Madhav** 31:37 Fair enough.
**Trask** 31:38 Right, right, that hub.
**Madhav** 31:40 Right, right, right. Sounds good. I will give the reasoning for everything. Great. For the RPC request metadata key and response metadata key, we are okay with this. We see how it is going to be used.
The only thing is, like, we won't be able to support it right away until some people come and ask for it. I see it is anyhow optional as of now.
We will support it in the future, but, Again, over here, what we… what this suffers from is the same problem, the response metadata.
**Liudmila Molkova** 32:18 How should they call?
**Madhav** 32:19 Wait.
Because we have headers and trailers, which are… at the RPC level. I don't know how they will map specifically to request and response for us.
**Liudmila Molkova** 32:34 So that both request and response has… have headers and trailers.
**Madhav** 32:39 Yes.
**Liudmila Molkova** 32:40 And you would rather make a… made it called RPC, response, headers.
key, RPC response trailers key, or… Like, what to…
**Madhav** 32:53 could be…
**Liudmila Molkova** 32:54 The name that would work for you, if you eventually decide to support it, that would be… not… I don't know, match the terminology properly.
**Madhav** 33:04 Okay, let me… let me think through it. I didn't… we didn't discuss it a lot since we anyhow decided we won't support it, but I understand we have to at least finalize the convention now, even if we support it later. I will add a suggestion based on what is accurate in the ticket itself.
**Liudmila Molkova** 33:21 Awesome, thank you. It's like, it's okay, totally okay not to support it, it's just that if you eventually decide, it would be unfortunate if it's already stable.
**Madhav** 33:31 Yeah, yeah, sounds good.
And, other than that, the only thing is, yeah, for the server-side dispense, we… everything that is not okay should be an error type. So, I will add all the explanations, but that's the entire list, but more or less, I think other stuff It's very closely aligned with what we have today, so… Like, if… most of these changes are done, then we should also be able to design and implement it by November, is what… at least I am planning as the observability lead on… gRPC.
**Liudmila Molkova** 34:12 Wonderful. Great.
Thanks a lot.
**Madhav** 34:15 Thanks, so I'll add the reasoning and create the ticket, and I'll ping in the Slack channel, and then we can… take up the discussion from there. Does that sound okay?
**Liudmila Molkova** 34:23 Nice. Yeah. Sounds great.
Thank you. Thank you.
**Trask** 34:28 by…
**Steve Rao** 34:29 Bye. Meh.
