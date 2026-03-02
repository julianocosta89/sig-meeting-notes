SIG: RPC Sem Conv Stability SIG
Date: 2025-12-03
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:24 Wonderful. Me and Bot. Let me kick you out, Bot.
**Steve Rao** 03:07 Hello?
**Liudmila Molkova** 03:09 Hi, Steve. How are you?
**Steve Rao** 03:12 Yeah, I'm good, thank you.
**Liudmila Molkova** 03:16 Let me kick out the bot.
**Steve Rao** 03:20 Okay.
Yeah, do we need to wait for Trasko or Gems today?
**Liudmila Molkova** 03:52 Let's pick Trask, I think he should be here.
**Steve Rao** 03:56 Okay.
**Trask Stalnaker** 05:06 Hey, folks.
Thought I set a reminder.
**Steve Rao** 05:15 Hmm.
**Trask Stalnaker** 05:16 I did last week. I put in our Slack channel, I thought to send a weekly reminder for this meeting, but I don't see it, so I must not have done it correctly.
9…
**Liudmila Molkova** 05:29 You only missed me kicking the butt out. I used the time productively.
**Trask Stalnaker** 05:34 I've given up.
**Liudmila Molkova** 05:36 I know, yeah.
**Trask Stalnaker** 05:39 But I fully support… Reminder…
Okay, says at 3pm every Wednesday.
**Liudmila Molkova** 05:49 It's worth… Ian?
**Trask Stalnaker** 05:52 Yeah, but it's supposed to give the reminder
Yeah, that it's starting in an hour at 3pm.
**Steve Rao** 05:59 I see. Okay.
**Trask Stalnaker** 06:00 But it didn't do it.
Hmm.
I don't know, I'll look into it.
Those were the try.
**Liudmila Molkova** 06:22 Okay… So, let's take a look at our board. I've actually, spent some time triaging issues.
Most of them were related to streaming. We have a couple of issues.
If it doubts… Thedas.
And I think we should, triage them.
**Trask Stalnaker** 06:51 Cool.
**Liudmila Molkova** 06:53 So the operation… Type.
So, I think we have a different…
So the operation we have, it's just a call, whatever call. It's streaming or not streaming, I don't think we… we cannot have this attribute because…
The notification, the processing or sending are not
Are sub things under the larger… pen.
But what I think makes sense is capturing the type, like, the…
Whether it's an Unary, or it's a streaming call.
**Trask Stalnaker** 08:03 Right.
**Liudmila Molkova** 08:05 And… we can… We cannot postpone it, because it should be on the metric.
**Trask Stalnaker** 08:15 Right.
Yes, correct.
Yes.
**Liudmila Molkova** 08:32 So, Don, let me write it down…
So I'm going to leave a comment, I'm going to say it's accepted to do…
So many things here.
Okay, and then the purpose of request-response subnamespace.
So I think… The useful part here… is…
If I look into gRPC documentation.
**Trask Stalnaker** 10:02 Can you pull up the RPC, our RPC SEMCON first? I don't… not remember what's under request response.
**Liudmila Molkova** 10:24 Let's go to… Oh, man.
Maybe in here.
Oh, just this, friends. Okay, I'm actually addressing some of them. I'm addressing them in a pull request that they… I just sent.
The metadata, that's it.
**Trask Stalnaker** 11:15 Okay.
So do we understand what the issue is about, then?
**Liudmila Molkova** 11:28 So,
I think it's… there is some ambiguity what request and response means, right? It can mean the initial request and final response.
It can mean individual.
Requests and responses in messages.
And… JRPC…
Let's see what they use.
So, if you look here… Just a basic example.
Here's request and reply here, as the message things.
**Trask Stalnaker** 12:40 But what's the practical, application to semantic conventions? Where do we use… Request and response.
**Liudmila Molkova** 12:53 and metadata.
**Trask Stalnaker** 12:55 Oh, okay, so just for metadata is the question of… Okay.
And is metadata, transferred on any streaming?
**Liudmila Molkova** 13:10 No, metadata is only applicable to the first request.
And final… response.
**Trask Stalnaker** 13:20 Not even, like, the original request and the final response.
So in streaming, it can be the final… response.
In the streaming case.
**Liudmila Molkova** 13:36 E-Yeh.
So, in case of streaming, the gRPC sends status after the final response, along with…
trailers.
**Trask Stalnaker** 13:51 Okay, I understand.
Yes, that makes sense. It's the beginning and end of the whole… interaction.
**Liudmila Molkova** 14:01 Right, yeah.
So, I mean, there is some ground to the issue, and we can consider, I don't know, some…
Ways to… Threshold.
what I'll probably do, I can do some research on what is used, in JIRPC and ConnectRPC.
Maybe Steve, do you…
Is there a concept like metadata in… Double?
**Steve Rao** 14:48 Boom.
Yeah, in, in double protocol, yeah, it's, there is a metadata concept, but I'm not sure it's, equal to, to what you mean, so maybe I can check it later.
**Liudmila Molkova** 15:05 Yeah, that would be great,
So, what I mean is the gRPC metadata, it's like the additional headers, like, you would use for authentication.
Some metadata stuff like this.
**Steve Rao** 15:20 Okay, yeah, it's, Israeli have a similar concept.
Double.
**Liudmila Molkova** 15:26 There is one?
**Steve Rao** 15:29 but to…
**Liudmila Molkova** 15:47 Oh, additional parameters? Is it the one?
Attachment.
**Steve Rao** 15:54 Yeah, it can set some attachment for a user.
And.
**Liudmila Molkova** 16:12 I'm curious, did they… did they come…
Like, if I have streaming, would they come with every message, or would they come with…
Like, the… in the start and the end.
**Steve Rao** 16:30 Yeah, Force Jamie, I'm not very sure about this point.
I can do some research later.
**Trask Stalnaker** 16:40 I mean, it makes a lot of sense to me that they're, like, streaming is supposed to be very lightweight, like, little…
Packets going back and forth, but…
That makes a lot of sense that there's some things that are big, that are… And, and request response.
fits very nicely with at least Unary and HTTP and our understanding. Even of HTTP2,
Right? Which can be streaming, But we still have request and response… request headers and response headers.
**Steve Rao** 17:17 Yeah, yeah, the… in… in… in triple protocol, yeah, it's, yeah, it's a subprotocol of gRPC. Maybe I think it has,
is have the same concept of metadata with gRPC.
**Trask Stalnaker** 17:40 So if the question is only about metadata, Mmm…
In favor of request and response for metadata.
**Liudmila Molkova** 18:00 Yeah.
So, let's see, unused the data… oh, sorry, unused.
Request, response, or metadata…
So the conclusion, the practical conclusion, let's stick with request and response for the… Metadata for call-level things.
**Trask Stalnaker** 20:32 Yeah.
I like it for call, if it's…
For anything that's really just call level.
Because it maps so nicely to HTTP and the simple RPC cases.
**Liudmila Molkova** 20:46 Right.
I don't think we need to document it, if we don't document…
**Trask Stalnaker** 21:08 I was just gonna say, if somebody had a… Some other proposal.
that made sense, then I'd be happy to, you know, think on it, but I… I…
satisfied, at least, with request response. I don't feel the… need to… Try to find something else.
**Liudmila Molkova** 21:38 So then I'm going to…
Needing for a decline.
I guess I'll just close it.
**Trask Stalnaker** 21:55 Yeah.
**Liudmila Molkova** 22:21 Okay.
Yay, non-alitious.
**Trask Stalnaker** 22:25 One column down.
**Liudmila Molkova** 22:27 Perfect.
So, do we have something in the agenda?
No, then… Let's, see what we have in progress.
So there is this PR… There is some…
about the status quo. There, there was… there were some comments from Armin.
I addressed them… I'll ask him to take another look.
is asking… But additional errors, but…
**Trask Stalnaker** 23:10 I agreed with your response.
**Liudmila Molkova** 23:13 I'll cry.
So, let's just give him a chance to take another look, and hopefully… We'll get it merged.
The other PR I just sent is about consolidating core PC metadata attributes. You have GRPC request response, connector PC request response.
And, I'm suggesting to… well, the suggestion here is to consolidate them.
There's an issue from James about it.
He played around two ideas, record them as HTTP request trailer, or… Heather a trailer.
I think it's not the way you're… That we should capture.
**Trask Stalnaker** 24:04 Yeah.
I like… I like your Proposal.
**Liudmila Molkova** 24:10 Yeah, and I kinda want to start working on the…
System-specific naming, and it makes sense to first deprecate these ones, so that we don't need to deal with them later.
**Trask Stalnaker** 24:25 Yeah.
**Liudmila Molkova** 24:29 Cool, so Dan, this is just something to review.
An easy one. Yeah.
**Trask Stalnaker** 24:36 It does… it looks easy. I will look at it.
**Liudmila Molkova** 24:44 And… We can start, brainstorming some new stuff.
Or think about what we should do next.
**Trask Stalnaker** 24:58 So this is something… Yeah, we can… let's go through some to-dos.
**Liudmila Molkova** 25:12 So… This one, I think we kinda clarified… This was the… duration metric.
We're saying that's a logical operation.
And… If it's logical… then there will be underlying HTTP spend, could be underlying HTTP spend for gRPC.
**Trask Stalnaker** 25:48 Yep.
**Liudmila Molkova** 25:52 So I don't know if we need… I don't believe we need to document anything else.
Oh.
Yeah, we documented.
Sorry.
Is there anything else in this issue?
Okay, it's still in messaging conventions. Okay.
**Trask Stalnaker** 27:00 Okay.
I feel like we've clarified it in…
our brains, at least, through the… in the… during the database semantic conventions, and I think we documented it there.
But I could see it just being needed.
Be needed to be documented elsewhere.
I'm not sure.
**Liudmila Molkova** 27:28 Yeah, so what I want to do, maybe we should remove it from the RPC board.
But I don't… Want to close this issue, because it's also on the messaging board.
**Trask Stalnaker** 27:40 Yeah.
Makes sense to me.
**Liudmila Molkova** 27:51 Quay!
This is the main one.
**Trask Stalnaker** 28:05 I mean, I think the important, like… It feels like the… We have aligned… At least in our definition.
I mean… If it's… just a rename…
I think that's going to be okay at the end of the day.
I think it would be more problematic if we had incompatible definitions.
**Liudmila Molkova** 28:38 Yeah, so maybe what we can do? Or… is…
You know how we have these mapping documents?
Indifferently.
**Trask Stalnaker** 28:48 Yeah.
**Liudmila Molkova** 28:49 Maybe we can have a non-normative mapping, or even normative one. Wow.
Doesn't matter.
**Trask Stalnaker** 29:00 Yeah, I think that's a good idea.
**Liudmila Molkova** 29:33 Sorry.
So I don't know if it's possible to do a simple translation, but maybe we can… we can…
To write to make it possible.
**Trask Stalnaker** 30:32 Yeah, I mean, I like the next step of just documenting the mapping.
**Liudmila Molkova** 30:42 Y… yeah.
Good?
**Trask Stalnaker** 31:03 Yeah.
**Liudmila Molkova** 31:08 Cool. It remains a to-do item.
And… Okay, so this is a 3-wheel one.
I… Think…
It's related to…
most friend…
**Trask Stalnaker** 32:01 So, and as far as the version… Network protocol version.
**Liudmila Molkova** 32:09 Yeah, I don't… I don't think this is right.
**Trask Stalnaker** 32:11 Okay, okay.
**Liudmila Molkova** 32:32 So for this one, it, it kind of makes sense, and
Let me see, am I deprecating it in the Lost Pure?
Oh, nice. It's already… Deprecated. Oh.
**Trask Stalnaker** 33:05 Alright.
Does that work?
I don't think so.
**Liudmila Molkova** 33:51 The first one works, the second.
**Trask Stalnaker** 33:52 Yeah.
**Liudmila Molkova** 33:52 And… no.
**Trask Stalnaker** 33:54 If you put fixes for the second one, Then it'll close it.
**Liudmila Molkova** 34:00 like, 2 times?
**Trask Stalnaker** 34:02 Yeah.
**Liudmila Molkova** 34:02 Like this? Fixes.
**Trask Stalnaker** 34:03 Yeah.
**Liudmila Molkova** 34:06 Okay.
Well tested.
**Trask Stalnaker** 34:09 Should be able to see… oh yeah, it popped up down in the,
Link showed up down there, may close these bottom right.
**Liudmila Molkova** 34:16 Oh! Nice!
**Trask Stalnaker** 34:20 Yeah.
**Liudmila Molkova** 34:20 I learned something today.
So this is effectively in progress.
Yeah, canceled plans.
**Trask Stalnaker** 34:46 So, remind me why this is important for our PC.
Oh, because they have a canceled status code.
**Liudmila Molkova** 34:58 Yes, and also, gRPC has some patterns that are especially
We're onto it like hedging, when you send a lot of requests at once, and inevitably.
Oh, but one are canceled.
So I think we… what do we have to… D.
**Trask Stalnaker** 35:24 Oh, that's a good…
**Liudmila Molkova** 35:35 So now, you know, like, we have a span status section for HTTP where we… Talk about caveats.
**Trask Stalnaker** 35:51 I mean, we're labeling it with the…
canceled, right? I mean, if it's truly gRPC canceled.
**Liudmila Molkova** 36:13 Oh, maybe we should keep it on set for clients as well?
**Trask Stalnaker** 36:21 Yeah.
**Liudmila Molkova** 37:16 So, should is good.
But we can…
Do okay, you're canceled.
**Trask Stalnaker** 37:38 Yeah, I mean… A little tricky, right? Like…
Canceled because it timed out, like, because there was a client-side timeout?
It's kind of.
**Liudmila Molkova** 37:53 Right.
**Trask Stalnaker** 37:55 An error.
**Liudmila Molkova** 37:58 So, for HTTP, we would consider them Errors.
Like, because, like, let's say… In case of Java, it most likely will manifest as an exception.
and exceptions.
By default, or… Errors.
**Trask Stalnaker** 38:28 Typically, yes. In our HTTP client instrumentation, it would Probably do that.
But if you were, like.NET, and you were instrumenting the HTTP library itself, You would have the option.
Of what to do on a… if you have, like, a… Client-side timeout.
**Liudmila Molkova** 38:55 Yeah, you don't… as you mentioned, you don't know if it's a timeout, Or it's a deliberate consolation.
**Trask Stalnaker** 39:02 Yeah, yeah.
**Liudmila Molkova** 39:06 And for what it wears, for HTTP, we actually explicitly say that constellations are…
**Trask Stalnaker** 39:13 Canceled.
Okay.
It's canceled.
Yeah, I mean, maybe hedging is just sort of a future…
Layer on top of the semantic conventions, which then…
If you are in a known hedging case, and you cancel because something already came back.
You could set it more appropriately.
**Liudmila Molkova** 39:55 Yeah, and that's why we should probably add the same blurb as here.
**Trask Stalnaker** 40:00 If you have additional context, use that additional context.
Yup.
**Liudmila Molkova** 40:09 Hmm.
Oh.
**Trask Stalnaker** 40:24 Right, yep, yep.
Oh, last week! I missed it.
**Liudmila Molkova** 40:28 Right.
And… I… The somewhat category doesn't change what we're…
need to do… we need to have a default.
And we want to give flexibility to sub to… to instrumentations.
If eventually there is a cancellation status, it would come handy.
**Trask Stalnaker** 41:49 Yeah, yeah.
I agree that we shouldn't block on… That…
That needs to be something that can be layered in later.
I would just, merge the third bullet into the second bullet.
Yeah.
**Liudmila Molkova** 44:59 Okay, wonderful. Super productive today.
**Trask Stalnaker** 45:02 Yeah, thanks for driving through… driving us forward.
**Liudmila Molkova** 45:07 Thank you.
**Steve Rao** 45:08 Poo.
**Liudmila Molkova** 45:09 Thanks, Dave.
**Trask Stalnaker** 45:10 Alright. Yeah, thanks, Steve.
**Liudmila Molkova** 45:13 Do we have…
**Trask Stalnaker** 45:15 I think we… Oh yes, we still have 2 more weeks of… meetings.
Before I… the holidays. Alright, sounds good.
**Liudmila Molkova** 45:27 Thank you.
**Steve Rao** 45:28 Okay.
