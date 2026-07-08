SIG: Collector SIG
Date: 2026-07-07
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 00:50 Antoine.
**atoulme** 00:54 Hello.
There you go.
**Andrew Wilkins @ Elastic Observability** 00:58 Yeah, I'm good. Thanks.
**atoulme** 01:00 Good.
Let me kick out this thing.
Yes.
All right, let's go on.
**Andrew Wilkins @ Elastic Observability** 01:29 I guess you didn't add that then.
**atoulme** 01:53 I'm.
Don't think Sean will be joining us today. I've got the agenda up.
I really don't have anything today.
**Andrew Wilkins @ Elastic Observability** 02:41 I don't have anything either, so… Potentially just… Have a, like, a 2-minute meeting.
I do have a… I do have one PR up, but it's on Core.
You're not an approver on core, are you Well, you are an approver, but you're not a.
**atoulme** 02:59 Yeah, I mean… Can bring it out.
Go ahead.
**Andrew Wilkins @ Elastic Observability** 03:16 So… My browser loads.
been talking about this for quite a long time. This is the ability to add extensible… scraper controllers. It's got one approval from Josh.
and off a review from Can't remember who it was now. Oh, Pablo. Anyway, if anyone watching, if you or anyone watching would like to review it, please go ahead and let me know on Slack if you have any questions.
I think it's ready to go.
**atoulme** 03:54 I'll just put that in on the agenda as well.
**Andrew Wilkins @ Elastic Observability** 03:57 Thanks.
**atoulme** 03:59 So.
This, that.
Oh yeah.
Jeez.
**Andrew Wilkins @ Elastic Observability** 04:17 It's bigger than like a PR that I would normally create, but there's a lot of boilerplate.
**atoulme** 04:24 It always does.
**Andrew Wilkins @ Elastic Observability** 04:25 Sorry.
**atoulme** 04:34 It's been sitting here for a while.
Oh, you got your own mock host again.
We have so many of those, we need to… Stop.
**Andrew Wilkins @ Elastic Observability** 04:50 Yeah, should probably create a test package or something.
**atoulme** 04:54 Yeah, I mean, don't do it just for that. You can do it later. We don't want to mess up with your PR. I'm just… Just my own observation that we have been.
preparing the packages with host implementations.
Sometimes because they do one thing, like getting the extensions, sometimes just nothing.
Most of the time, nothing.
okay so there's a helper you got a test helper okay I'll just mark that as you Oh, okay.
So we're still trying to do the… this RFC for… Scrapers, huh?
**Andrew Wilkins @ Elastic Observability** 05:40 Yeah, this is the main… basically, this is the biggest change, and then we'll need to add… like a reference implementation.
I can't remember which one that was now. It was mentioned in the RFC, but I'll come back to that after.
**atoulme** 05:55 I'm approving it. Well, it's got some conflicts, but just if I… Andrew Wilkins @ Elastic Observability 06:01 Yeah, yeah, thanks. I'll fix it up now.
**atoulme** 06:05 It's… Got two approvals now.
So, anyway, okay. I really don't have much, I… We really need to, just for your entertainment, I can tell you that.
Recently, I've got some, interactions with customers who are looking to have a better I.O. for the file-based persistent, the queue. So, Dimitri told me that he's actually opened something about that.
If I find it, that'd be cool.
I mean, in general, like, the file-based persistence mechanism we have is not using a queue?
Approach is just key-value pair, so it's not very fast, could be better.
And we could do that to reduce the I/O load on that.
And there are probably some additional just low-hanging fruit things that we could do to just make it better.
So, there might be some work that we would look to get into soon, especially because it's, It would allow all sorts of disaster recovery strategies, you could buffer on disk for a bunch of time, or whatever, right? So, this is just, intent around that.
**Andrew Wilkins @ Elastic Observability** 07:21 So the, like, the issue at the moment is it's random, random access, and we want to move to a sequential… is that the, like, the, the… Wonderful.
**atoulme** 07:30 Umm.
Yeah, I think there's that, so.
They're, the interface in Go that allows you to do, persistence to is a file database or Redis. It is using a key value, and it was never meant to be meant for a queue. It was meant to just be, like, a checkpoint.
And it's been abused a little bit towards that queue setup. It looks like, this is feedback I'm getting from Dimitri here, it's like we should really just build on top of this extension or whatever.
build a separate interface that would allow folks to have a better semantics around Q, which then allow you to have a better implementation behind that, because it currently does not allow that.
No, after that, you can have, like, qualms about the difference… file-based persistence approaches we've taken. The current one we have is this B-Bolt thing, which is supposed to be writing atomically to disk and all that. It's not always good. It's got some panics in there.
You can, you can have some, If you were to shut down the collector abruptly, you could actually have some corruption of the data.
In some cases, not always, but if you were to really be atomic, which it's not enabled by default.
So you end up, like, having worse and worse performance the more you're trying to really do a good job with that.
Personally, I… for a Redis storage extension back when, because I figured that none of the stuff we could come up with would be good enough.
if there's one thing out there that's just going to give you, like, 5 different ways to configure itself as Redis, right, you can do so many things with it.
But it's not really getting that much traction, and I think it's… customers are just… not geared towards Redis cluster.
Nothing too surprising for you, I'm sure.
So.
For now, I think we should just hang about and just make sure that the I/O for whatever we use for file storage needs to be somewhat good. I'm trying to get a real throughput figure so we can work with that, and then once we have that, I'll be able to kind of make sure we benchmark to that level.
**Andrew Wilkins @ Elastic Observability** 09:47 For what it's worth, I've thought a little bit about this, not a lot in the past with in relation to the Kafka components. I think they're sort of abused at the moment.
frequently as a queue between collectors. We definitely use it like that, and they would be a good fit for some kind of internal queuing mechanism.
**atoulme** 10:11 Yeah. So you could do an extension that would then pretty much be an interface on top of some Kafka stuff, and then it would, it would be some transparent. Yeah.
Not that Kafka is a panacea user, right? I mean, it has its pros and cons, but for sure, like, in some high throughput situations, you… if you're serious, this is actually a discussion I like to have with customers, where they are bouncing me back and forth, and at some point, I just have to tell them, like, if you're asking me for a Kafka queue.
Are you ready to run Kafka?
Okay, well then.
degradation of knowledge and degradation of features and expectations comes now, right?
**Andrew Wilkins @ Elastic Observability** 10:50 Yeah, I'.
**atoulme** 10:50 This is a golden standard, and now we're going to work with you on where you want to land without having to run this much infrastructure yourself.
Okay, alright, well, great catching up.
**Andrew Wilkins @ Elastic Observability** 11:04 Okay.
**atoulme** 11:05 See you next time.
**Andrew Wilkins @ Elastic Observability** 11:05 Nice chat.
**atoulme** 11:07 Cheers. Cheers.
