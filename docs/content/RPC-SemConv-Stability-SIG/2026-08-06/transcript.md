SIG: RPC SemConv Stability SIG
Date: 2026-08-06
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:02 Hello, folks.
**Trask Stalnaker (Microsoft Corporation)** 01:07 Hey, Steve. Hey, Matt.
**Matthew Hensley** 01:09 Hello!
**Liudmila Molkova** 02:07 Hello, hi folks.
**Trask Stalnaker (Microsoft Corporation)** 02:13 Good morning.
**Liudmila Molkova** 02:15 Let me ping my talk, maybe he's in the old call.
**Trask Stalnaker (Microsoft Corporation)** 02:18 Oh, right.
**Liudmila Molkova** 03:17 There are no bots in those new meetings.
**Trask Stalnaker (Microsoft Corporation)** 03:20 Yeah, I've been noticing… I don't know if it's just a matter of time, or… so they're gone for good.
**Matthew Hensley** 03:34 I guess they need LFX accounts, and so it's probably pretty easy to, knock them down.
Since they'd all be sharing one.
**Trask Stalnaker (Microsoft Corporation)** 03:47 Yeah, that's a good… so would they need to… they would need to log in with their users… Credentials, yeah, that does seem… Like, a good obstacle.
**Liudmila Molkova** 04:13 Since he's offline, maybe I'll just quickly jump on the other call, and if he's there, I'll tell him.
**Trask Stalnaker (Microsoft Corporation)** 04:20 Okay, sure.
**Liudmila Molkova** 05:03 Well, Madhava's not there, but all the bots are.
**Trask Stalnaker (Microsoft Corporation)** 05:07 I love it, it's a bot trap, honey trap for bots.
**Liudmila Molkova** 05:12 Right.
Okay.
And now it's 5 minutes past.
Do we have anything to discuss without him?
Maybe we can quickly, look through the issues and see what is actionable.
**Trask Stalnaker (Microsoft Corporation)** 05:32 Sure.
**Liudmila Molkova** 05:34 a… let's see… Here…
**Matthew Hensley** 05:38 Yeah, I'd definitely like to do that. I was looking through these earlier, and… There's obviously… Good number of them.
But some don't have any… comments or anything, it might be useful to at least propose something, even if it's… Wrong.
At least to get it moving.
**Liudmila Molkova** 05:59 This is wonderful. Emma, Emma, I am sharing, great.
**Matthew Hensley** 06:03 Yes.
**Trask Stalnaker (Microsoft Corporation)** 06:03 Yeah.
**Liudmila Molkova** 06:04 Okay, and I was going to open semantic conventions… Okay.
So, I think we have a board, but we also have this.
K… R… Let's open this one, let's see… They are… On the board, and they have no… Datas.
Oh, this is one of the friends that is actionable.
Let's take a look at others.
R… Trask, I thought you fixed it, no?
**Trask Stalnaker (Microsoft Corporation)** 07:04 And spans…
**Liudmila Molkova** 07:08 Oh, no, no, no. This… you fixed the method original appearing in metrics.
So I think we just close it as one fix.
**Trask Stalnaker (Microsoft Corporation)** 07:22 Yeah, I mean, I would like to get… Ideally, gRPCs, like, teams… Acceptance of it.
**Liudmila Molkova** 07:34 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:35 But yeah, I agree that, it is what it is.
**Liudmila Molkova** 07:41 So, well… Non, Cupid.
Around… What else do we have?
I already have it.
Yeah.
Okay, this friend, this friend… Seems to be the same, we're keeping it… Separately this friend.
This is new, it's not for Madhav, I think.
**Trask Stalnaker (Microsoft Corporation)** 08:25 Yeah, I missed that.
**Liudmila Molkova** 08:29 Okay.
Symmetrix… Don't have enough information.
And that's true. This is all we have.
We didn't have… A way to define the metrics Well… Yeah, before, but now we do with Schema V2.
Mind some… bugs? Sorry, Trask.
That's true.
**Trask Stalnaker (Microsoft Corporation)** 08:57 No worries.
**Liudmila Molkova** 08:59 But we'll fix them, and what I was thinking, we can… convert, or just define, the metric refinements for gRPC and have them rendered here.
**Trask Stalnaker (Microsoft Corporation)** 09:16 Cool.
**Liudmila Molkova** 09:19 Hmm.
If somebody is interested in learning how to work with Schema V2, You're welcome to take it, if not, I can take it.
**Matthew Hensley** 10:01 I've been doing some stuff with, Schema V2, and happy to take a look, as long as… Note to add here.
**Liudmila Molkova** 10:11 Cool, I'll… Let me know if you need any help.
We have some precedents, so I think… Well, we have them for spense.
Not for metrics.
But it should, it should be easy. Oh, we have them for semantic conventions GenAI.
So we should have examples.
**Matthew Hensley** 10:36 Yep, I've been tracking that.
**Liudmila Molkova** 10:39 Oh… wait a sec.
We… oh, we can render them.
Yeah, we can render them, that's fine. Hardware metrics are the example, yeah.
Okay, and then, yeah, we're moving it to do-do… The next one, the man who just talked about this… Yeah.
Oh, I remember we've been talking about it, and that there are others and trailers, but metadata does not express it. And I think, Steve, you posted some research Somewhere, right?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:27 Yeah.
**Liudmila Molkova** 11:28 Do you remember where.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:30 Yeah, maybe I fell in the Google Doc.
**Liudmila Molkova** 11:38 Oh, cool.
**Find it… Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:56 Yeah, you can, Yeah, yeah.
You can see the description in the Google Doc. I, left the comment.
I betcha.
Yeah, you can see on the right.
I left a comment.
**Liudmila Molkova** 12:28 Oh, I see.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:29 Next one, next. The last one.
**Liudmila Molkova** 12:32 Yeah, oh, okay.
Mind if I copy them to the GitHub issue?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:39 Okay, sure.
**Liudmila Molkova** 12:41 Yeah, thank you.
So just so we have everything in one place.
quote, an attachment.
Both request and response method.
Oh, request attachment and headers, response attachments and response trailers. Interesting.
Okay.
So then, we have… Oh.
So… might have, doesn't mention Chris… Request trail… okay, so there are no request trailers.
There are headers, request and response, and response trailers.
And for double, it seems… or triple, it seems.
There are request headers and response trailers.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 14:34 Yeah.
**Liudmila Molkova** 15:10 And those are request attachment, or just attachment.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 15:15 Tetrant.
**Liudmila Molkova** 15:16 Just attachment, okay.
And… For something like JSON RPC, if it was a real article.
It would be the, whatever, the underlying thing.
the HTTP… Oh, okay, so the HTTP also has… Request headers… I would imagine there are no request trailers, or… does anybody know?
**Trask Stalnaker (Microsoft Corporation)** 16:03 So…
**Matthew Hensley** 16:04 Not offhand.
**Liudmila Molkova** 16:08 There aren't, right?
**Trask Stalnaker (Microsoft Corporation)** 16:09 I don't think so.
**Liudmila Molkova** 16:18 But still, there are trailers.
The response trailers.
Okay, so what if we just converted this metadata into three, the request metadata into reco… sorry, request metadata into request headers, and response metadata into response headers and response trailers?
It would not align with… Ripple terminology?
Metadata doesn't align either.
**Trask Stalnaker (Microsoft Corporation)** 17:02 So, at the API level, gRPC… Calls them metadata.
**Liudmila Molkova** 17:12 Mmm. Oh, I see.
Sorry, I messed up. Yeah.
**Trask Stalnaker (Microsoft Corporation)** 17:16 How… how do… is it just a matter of, does metadata always end up in… response trailers… what are response headers, then, in gRPC?
Or are they both, and it just kind of magically gets split?
**Liudmila Molkova** 18:28 So, like, what metadata is… We used… on? Is it the… Only in the context of request and response, and then it makes sense.
**Trask Stalnaker (Microsoft Corporation)** 18:45 So what I'm, what I'm getting at is, If we were modeling it kind of at a… Logical layer? Like, is metadata At the API level, do you just set something called metadata, and it magically… Turns into either a header or a trailer, depending on whether you've committed the response yet.
**Liudmila Molkova** 19:21 Sweet.
What's that cooler flow.
Oh, new outgoing context.
**Matthew Hensley** 19:42 Yeah, I'm reading the… this stock right here.
Put in the…
**Liudmila Molkova** 19:51 Thank you.
**Matthew Hensley** 19:59 Looks very much like the, summary that was on Google, but…
**Trask Stalnaker (Microsoft Corporation)** 20:03 Metadata that a client can receive includes header and trailer.
So, I guess kind of what I'm wondering is, I mean… Maybe metadata's the right abstraction for the logical layer, and… whether it's… A header, or a trailer.
be… Physical layer, Bing.
**Matthew Hensley** 20:54 That's kind of what I'm reading here.
I was also surprised to see that gRPC puts the final status code, looks like, in the trailer.
**Liudmila Molkova** 21:07 That's it.
**Matthew Hensley** 21:08 That's a little strange.
**Liudmila Molkova** 21:27 If I would be what was so easy.
Oh, so this is metadata, yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:35 They do have a set header and a set trailer.
**Liudmila Molkova** 21:42 They create the metadata, but then they… Set it on header or trailer.
**Trask Stalnaker (Microsoft Corporation)** 21:49 Yeah, okay. It's on the server side. So on the server side… That's distinct.
On the client side.
You may only get the combined… Resolve.
**Liudmila Molkova** 22:08 Because there is no… the request trader.
There's on the header.
**Trask Stalnaker (Microsoft Corporation)** 22:23 Oh, no, maybe you can.
**Liudmila Molkova** 22:27 You can receive one or another.
**Trask Stalnaker (Microsoft Corporation)** 22:30 Yeah…
**Liudmila Molkova** 22:37 So what… what makes me worried about… it's in, like.
Imagine we play out the case.
Where we have… metadata.
Athological.
And then it would lead to your PC request header.
And so on.
that… Where… introduce… a notion of metadata, but for, like, if somebody instruments practical level, they would need to use a different attribute.
Maybe it's the… it's a good choice.
But it's also maybe unnecessary.
**Trask Stalnaker (Microsoft Corporation)** 23:33 I mean, given that they have, APIs to, it looks like, set and get the… response headers… And trailers separately.
That, I think, alleviates my concern about them being Not exposed at the logical layer.
**Liudmila Molkova** 24:05 Okay…
**Trask Stalnaker (Microsoft Corporation)** 24:09 So we would have, like, Request headers, and we would have response header and response trailer.
Which kind of, I mean, that maps well to HTTP also, we just have never… Added.
response trailers.
**Liudmila Molkova** 24:35 Okay, so then… Then… Let's play it out, focus on our piece. You're right.
Yes.
**Matthew Hensley** 24:57 And just for fun, I pulled up the… gRPC node.
example, and seeing how the API looks there versus Go, and it… His name's slightly differently.
**Liudmila Molkova** 25:10 Can you share the link?
**Matthew Hensley** 25:11 Yeah, it's weird.
**Liudmila Molkova** 25:12 Let me show you things.
**Matthew Hensley** 25:15 So this is the server receiving it, and instead of header, it's call.metadata, And then… You have send metadata headers, but down at the callback… There's trailers set up in here somewhere, unless I'm… Yeah.
**Liudmila Molkova** 25:36 This, again, this is metadata.
**Matthew Hensley** 25:39 Yep.
I just thought it was interesting that it's kind of implicitly headers. It's just like, when do you send… obviously, it's metadata, but the naming's a little bit different than the Go.
SDK version, so… I think conceptually, what we're talking about probably makes sense here.
**Liudmila Molkova** 26:04 Tristan.
They call it sun editing.
You know, we can do more research. Probably whoever picks this task would need to check different sources.
Okay.
Is anybody interested in picking this up?
Okay, I'll see questions…
**Trask Stalnaker (Microsoft Corporation)** 27:22 You can leave it there, also unassigned if I, I can try to chip away at different ones there.
**Liudmila Molkova** 27:33 Yeah, I mean, I like doing research.
**Trask Stalnaker (Microsoft Corporation)** 27:39 I like your research.
**Liudmila Molkova** 27:41 Thank you, I appreciate it.
Okay, we have 2 minutes left. I don't think we will get through this one. I… I… I don't… I'd rather keep us consistent within semantic conventions, but your PC implementation can… can deviate from this.
**Trask Stalnaker (Microsoft Corporation)** 28:08 Sure.
**Liudmila Molkova** 28:15 I just hope it couldn't… it wouldn't be a blocker for… for us, like, resulting in us having two different instrumentations.
**Trask Stalnaker (Microsoft Corporation)** 28:24 Yeah, yeah.
**Liudmila Molkova** 28:29 Okay, so Dan, let's talk about it next time.
**Trask Stalnaker (Microsoft Corporation)** 28:33 Sounds good.
**Liudmila Molkova** 28:34 Thank you, Al. Good to see you.
**Trask Stalnaker (Microsoft Corporation)** 28:36 Yeah, excuse me.
