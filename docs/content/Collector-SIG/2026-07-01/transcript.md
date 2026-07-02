SIG: Collector SIG
Date: 2026-07-01
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Pablo Baeyens 00:02:49 Hello!
Is there a bot or something, John?
Jade Guiton 00:03:20 Yeah, I don't know if you… maybe you can't see it, but… Read that AI meeting notes again.
Pablo Baeyens 00:03:27 Oh, okay, maybe, maybe it left, you know.
Paul.
I guess we can get started with the stability things for people.
a lot more… items. I don't know, Christus, if you want to… talk about this yourself, or I'm happy to present it.
Christos Markou 00:04:20 Feel free to do it, yeah.
Pablo Baeyens 00:04:23 Okay.
So, yeah, I posted the issue on the… meeting notes, let me put it also on the Zoom chat, So, the Kubernetes attribute processor, is… like, try to graduate to be a stable component. There are… A number of criteria for that to be… done, which are on that link, that's also on the issue. And so, as part of that, when we have this issue template, this would be the first component on contribute, and the first processor to be marked as stable.
So, we are, to some extent, figuring out the process, but I volunteer to be the maintainer reviewing this, and… Well, I guess I'm looking for feedback on… the component itself, if you use it in production, you're able to talk about it publicly, it would be great to have comments there. If you cannot talk about it publicly, but are willing to reach out to me, also happy to talk on Slack.
And, yeah, once we have that, I will review the… order requirements, and hopefully we can get this to stable.
So, please leave your feedback there.
Mikołaj Świątek 00:05:57 That component doesn't use configHVP, right?
Pablo Baeyens 00:06:01 No, it doesn't use, the public API of that component is, stable right now, it's one point something. But right now, to be clear, we are marking the component as stable.
That is, preview step to marking it as one point something, but the… I want to consider the two separately. Right now, it's just marking it as stable.
Just because we have to figure out how to modify the release pipeline and all to be able to release a one-point-something component. And also, I would like to have the config thing blended and, like, have OTLP receiver, if possible, before.
Christos Markou 00:06:50 So, it won't be released as, V1 separately?
Is this correct?
Pablo Baeyens 00:06:59 I think this is the first step to releasing it as V1, but I would want to first mark this table, and then do the release as V1.
I hope the distance between those two steps is small, but I… I want to focus first on the stable thing.
Christos Markou 00:07:20 My main concern with this would be that, we can discuss this on the issue, but I have sent also a draft PR that suggests actually applies the switch, from better to stable for the signals, and also changes the stability level for the feature gates, for the schemas, the SMAT conventions, essentially.
And… I think once we do… if we merge these chains, when we merge these chains, we effectively change the default schema.
So my suggestion would be that, we only do this, we only merge these specific… at least the feature gates, we only change the schema, once we are ready to release it as V1, because if we merge this, and we continue releasing this as the zero.
It would be actually an effective breaking change to VES0, release, let's say, change. So that… that… I would see this as a problem. I would prefer, having the schema change on the first, release of V1.
If possible.
Pablo Baeyens 00:08:32 Okay, we can… discussed that on the issue.
Christos Markou 00:08:38 Yeah, we can figure it out. I agree.
Pablo Baeyens 00:08:42 I… I would hope that we can launch the config.http thing soon, and… Yeah, the OTLP receiver should be ready by then.
Okay, any… Other topics for the stability of components?
Okay, then we can move on to… Thanks, topic, and… I have a pending reviewer.
Blake Rouse 00:09:22 Yeah, yeah, again, this is just, might be really quick, Matt's just, informed, just still looking for reviews on the Phase 1 of the receivers, for partial reload. We are testing this and using it, and it's working, with our collector.
So… We're just trying to get that into core so we don't have to, like.
use a fork or anything like that, so I can keep maintaining it and keep using it, so… We're just trying to get, get some reviews on it, so if you could get… if I can get some eyes on it?
That'd be great.
That's it.
Mikołaj Świątek 00:09:55 I will say that testing has shown that The hotel collector at large is incredibly undisciplined about mutating config in all sorts of places, so you gotta be a little bit careful about how you, when you snapshot it and what you compare. That's one of the things that came up in practical testing of it.
Blake Rouse 00:10:23 Yeah, that is true. There was places where Preparing the config was failing because, it was saying it was always changing, because the… The current config that was being stored.
was being manipulated.
So… there's some stuff in there, you can see it, it's commented on, like… Lots done there.
And while it's done the way it is.
Yeah, that might be something else to look at, in the future, making… somehow making that config, immutable.
At that point, at least.
Pablo Baeyens 00:11:09 Okay, yeah, it's on the top of my list, sorry, I… I meant to get to this, last week, but there's… Fires to put out every day.
Blake Rouse 00:11:22 Totally understand. I appreciate it.
Hopefully we can get to this week.
Pablo Baeyens 00:11:28 Yep.
Mikołaj Świątek 00:11:35 Okay, so I actually… does anyone else have anything? Because what I have is some… something that might be kind of an open-ended discussion, and I was intending to leave it for the end of the meeting, to not eat time.
From… from things which are more tightly scoped.
So, I'm kind of opening a call if anyone has a topic that they haven't put in there.
Jade Guiton 00:12:08 Then you're good to go.
Mikołaj Świątek 00:12:10 I guess I'm good to go. Alright, alright, so… So let me… let me paint you a picture first of the kind of problem. I think there's an issue about this opened by my coworker somewhere in corporate, and that issue is a bit more complex than is needed for this discussion, so… we have an exporter helper queue, right?
that queue has a bunch of options. In terms, for example, it lets you configure whether you want to block when you… whether you want it to block when it's full, or whether you want it to return an error when it's full. Similarly, you can choose to just get a response immediately, or it can block until it actually sends the, Let's call it a request for now. The terminology is a little bit overloaded in some cases.
So, I'm wondering, kind of, one in general, but also in specific about a particular case.
How should offers of components navigate this.
And part of the problem here is that we now have batching in Exporter Helper, which is good.
The way the batching works.
is if you decide to use the queue in a synchronous way. For example, you have an in-memory queue.
you want to have a guarantee that the data you've submitted was sent. So, what you do is you configure the queue to wait for the result.
This works… this works correctly. There's no problem with it.
In general. The issue that comes up there is that if you do batching in this case, and everything has to be synchronous.
Then batches are essentially assembled from parallel consume calls coming into the exporter. And I don't think there's really any other way to do this while keeping it synchronous.
So it's understandable.
The thing is, If… if this relies on concurrency, the pipeline concurrency is… Controlled by components, usually by the receiver.
Like, there is a receiver which decides whether it wants to create a go routine per consume call, or whether it wants to just have a completely synchronous loop where it just submits stuff.
And that matters, right? Depending on how the queue is configured, you might get into a situation where, for example, you're… you have a loop where you're submitting 100 items per call.
The batch size is 2,000.
So… but your, you know, your concurrency is 1. So, you're only going to submit 100, then you're going to wait for the flash timeout, and then submit 100 again, and wait for the flash timeout.
The batching just doesn't really work that way.
So that's, like, kind of a problem from the perspective of someone writing a receiver. You know, how do you interact with the rest of the pipeline in such a way that You're good at what you're doing makes sense and works.
Irrespective of what the user said in their queue configuration.
And in particular, there's kind of a problem there, where, because of the semantics, there isn't really, like, if you're a single receiver, you know, even if you know you're a single receiver.
In the pipeline, consuming a queue. There isn't really any good way to do flow control.
In the sense that… you don't know what your concurrency should be. If your concurrency is unlimited, you might just… you might just reproduce an unbounded queue by opening a lot of Go routines.
And there's just kind of no way to tell, no way to configure the queue, at least in synchronous mode, in such a way that You kind of get reasonable limits.
on both the concurrency, and you also get to use the queue and the batcher in a reasonable way. So, I'm sorry this is a little bit rambling, I'm not as well prepared as I would have liked, but I kind of wanted to see if… if I'm right, if I'm wrong, does anyone agree? Does anyone disagree? Am I, like, thinking about things correct… incorrectly, or if I'm missing something.
And, you know, we don't really have a guidance on how to use it, right? We've kind of… we've rewritten the exporter helper queuing and batching, and added a bunch of options, but components, I think, largely haven't really updated anything on their end. And I'm not sure how to actually kind of solve this interfacing.
Problem in general.
Jade Guiton 00:17:09 The way I personally think about it is that… Receivers don't really need to think… About it too hard, as long as they behave like the OTLP receiver, which is to say, unlimited parallelism, there's no synchronous… It's just, whenever there's a request, it spawns a Go routine and then sends it to the rest of the pipeline.
Which, yeah, like you said, is a problem, if you're using block on overflow, because it means you fill up with good routines.
And I think that's a problem with block on overflow. I don't think that's a problem with how the receiver handles it.
in an ideal world, like… Every receiver would implement, like, the memory limiter extension interface or whatever, so it could be shut down when memory pressure is too high.
But yeah, I don't think memory… the block on overflow… Option makes a lot of sense.
if you have, receivers like the OTLP receiver that have unlimited concurrency.
But I think for the most part, the other options… kind of… All based on this assumption that other receivers work the same.
Mikołaj Świątek 00:18:38 Yeah, so maybe, maybe if that's what we think the model should be, we should issue some kind of guidance.
that this is… this is how we expect you to interact with the queue. I will say that maybe for OTLP Receiver, this works correctly, because OTLP receiver is really a kind of a proxy, in a sense, right? It gets requests, it sends requests.
And if you disable block and overflow, then you just get an error, Q4. And if you get an error, Q4, the OTIP receiver can just send that error downstream.
Right? And be okay.
Jade Guiton 00:19:15 Right?
Mikołaj Świątek 00:19:16 But if you're, like, a file log receiver.
it's not really fully clear what you should be doing if you get a… if you get Q4, right? You can… pause, maybe? The other problem is that you… like, again, memory limiter kind of solves this, but there's, like, kind of an inherent race condition in this setup, right? You write something to a pipeline, maybe you get a queue full, or maybe you'll block until your data is sent. And a priori, there's no way for you to distinguish between these things.
Right? You can just wait until you get… until something returns, which may be fast, and, you know, maybe… maybe, non-blocking or might be blocking. You kind of… the API treats both of these things, via the same call.
So, it's a little bit awkward to do that, and I'm not actually sure what to do with file log.
In that case. If you can try to retry.
If your call fails because the queue is full, you can try to send some signal downstream to… to kind of… to do flow control. But… I don't know, it feels kind of awkward to me, like, it feels like you… if you're in that case, you kind of end up implementing something like congestion control in the receiver for this to kind of work reasonably well.
And I'm not sure if that's a good idea. Does that make sense?
Jade Guiton 00:20:49 Yeah, I think… I guess… It depends how the file log… it's kind of a more general problem about how the file log receiver and scrapers in general handle errors, right? Even if they're not errors from the queue being full.
What do you do in that case, right? If you don't have a way to signal to anything and apply back pressure.
I don't know that there's anything better you can do than to just, kind of, drop the data.
Maybe with a warning or an error log.
For the file log receiver specifically.
My understanding is that there may be a way to just kind of… stop at the current offset, I guess?
But I don't really know… Best possible in general.
Mikołaj Świątek 00:21:36 I think it's possible in 5-log receiver, but it's… it makes the architecture really strange. Like, in an ideal world, you would have, like, a natural back pressure, where you say… or natural flow control, let's call it, where, for example, you do something like… or at least this is something I would like to do. It makes very… it makes a lot of sense in my mind to do it this way.
Where you just have a single go routine, and you just read from some channel, and that channel is, like, something that everything else in your receiver writes to, and it's a natural place where stuff gets blocked.
And then you just read from that channel, submit to a queue.
And that works perfectly fine. You can even, like, spawn a new coroutine to submit to the queue, but then you get into the, you know, how many coroutines is too many. You don't know how big the queue is, or what the batch size is, so you don't really know how many coroutines you should spawn, and you don't really even know if there are other receivers, how much data they are consuming.
In writing to the same exporter.
And to the same queue. So, you kind of need to… So you kind of need to do some kind of tracking on your own, even whether you decide to block an overflow or not, it's kind of… Comes out to a very similar… Problem, in the end, in this case.
Or you don't know what the right level of concurrency is for you, and unlimited concurrency is… a bit dangerous. It's another… there's another problem, actually, where you say unlimited concurrency, and again, in OTLP receiver, there's no problem, or there's no decision to make, because you just get a packet of data, and then you forward that, and you're done. Whereas in… places like FileLog, and maybe even in scrapers, and for, like, for receivers for protocols which don't have… which are, like, streaming protocols, they don't have, like, a natural batch site, let's say, where if you try to submit Requests, which are all a single item.
which might be the natural thing to do while writing a receiver, you're going to be very unperformant, even if you give yourself unbounded concurrency. So you kind of usually want to do some level of internal batching.
Before you submit something.
So there's this whole, like, set of problems which make it unclear what the right thing is to do when interacting with the rest of the pipeline. And it's not even clear what to do, even if you know what… what the configuration is, on the other hand, on the other end. And I know because I thought about this problem in a specific case where I do control the configuration of the queue, and I know what it is, and it's still kind of, you know, do I have to implement congestion control, or do I just, like, accept that I'm sometimes going to have, like, double my queue worth of, data in memory, just because of concurrency?
Blake Rouse 00:24:46 Yeah, I would say even knowing the size of the queue, like, still is a problem, right? Because you as a receiver don't know what the other receivers are doing in that same queue. So, right, so now, like, it's like… if you're saying, oh, my batch size needs to be this size before I can submit, if you have other Receivers running that are producing events that would cause you to reach that batch size, which you don't have context of, then, you know, you're waiting for your batch to reach that size limit, even though you don't even really need to wait that size limit.
And if all 3 batches are waiting for that size limit, and then they get merged in the queue.
Right? That might go over the minimum… the maximum size, and then that's got to split it apart and do all that stuff as well, which takes it longer. Now they're all blocked longer, because now we have two requests instead of one single request, or however that could shake out to be. It could be 3 requests on the exporter side.
So, I would… Yeah, and I think… I think, Michael, you're right, on the single request per… like, like, if you have one event and you send it per Go routine, that's super inefficient from the standpoint of, like, Go is gonna allocate a 2KB stack on the min size of stack size.
for every single Go routine that you're trying to send just one event, and that's gonna balloon the memory greatly.
Jade Guiton 00:26:13 I'm… I feel like if you are in the situation where you're receiving things one at a time.
you should do internal batching, regardless of the concurrency. Even if you don't… internal batching, regardless of… even if you don't do any concurrency, you should still be batching, because there's still some overhead in, you know, calling the whole stack of the pipeline once.
And then, returning from everything, and then going back down.
Mikołaj Świątek 00:26:41 I don't know how big, though. How big, though, right?
Blake Rouse 00:26:43 Yeah, I'm saying, like, what, yeah, what is that amount?
Jade Guiton 00:26:46 Well, I don't think it matters what the exporter helper parameters here, like, this is purely an optimization, like, it should not matter… To the exporter helper what your receiver decides to do for internal batching.
As long as it's, like, emitting things in a timely manner.
Mikołaj Świątek 00:27:11 I think that's right. I also think that if we were to do a review overseas and Contrib and see what they're doing, it might be, like, a whole dark forest of different ideas.
In there. I remember, what was it? What was I looking at? I think Fluent D receiver some years ago, and it was like this. It was, like, we were doing some batching, and we're… and it's probably not durable, for example.
Sorry, Israel?
Israel Blancas 00:27:41 Yeah, it's actually interesting that you raised this, because recently I saw, ticket in core. I am sharing the pull request, because Briefly, there was some activity there.
That is actually… I don't have related to this, right? It's about doing this thing from the exporter helper, right? When you are doing something in your backend, right? So, depending on how your backends responding, right? Like, I don't know, maybe you are trying to send too much data, right? And you're back in and saying, hey, I cannot add more, right? Or maybe you need to improve to increase the number of consumers, something like that, right?
Maybe there is a… it seems that it's a problem, right, that we have in different parts from the pipeline.
So maybe something that we can revisit on, well, I think this… this work that is being done And the PR is good, but maybe it seems that we can't… have something more general, or something, right, that we can't reuse. I call different components, because I also understand your thing, right? We, in the past, suffered some… Issues with different receivers, where we saw, right, these kind of problems.
For instance, in our case, I remember with the Kubernetes object receiver, right, in a big cluster.
Where we were, like, trying to get the information right, and it was dropped because our queues were full, right, because something.
Because of that, it was not easy to… we have to wait, I… if I remember properly, right, until the next poll or something on what… it was… it was a little bit problematic. So yeah, maybe… maybe it's something, right? But we have to… Create appropriate about trying to define a strategy across the full pipeline.
Mikołaj Świątek 00:29:31 I would even say that, like, a lot of the things that Jad said in this meeting should be in the document somewhere.
Sorry, sorry, Dad. Take it. I'm here.
Jade Guiton 00:29:42 Yeah, I absolutely agree that… I think this has absolutely nothing to do with Exporter Helper, I'll be honest, but I agree that we should have some recommendations on how receivers should behave, so we can kind of… You know, plan… things like export a helper's behavior based on that.
and from the discussion, it sounds like there's kind of 3 different areas that… Are concerning internal batching, first of all, how to handle it, what… How to handle it, and… yeah.
Like, what batch sizes should we use? What timest should we use?
I don't think durability matters as long as you correctly You know, you don't… acknowledge anything? Oh, Yeah, as long as you don't acknowledge anything until the batch is emitted.
But I… yeah, there's internal matching, then there's concurrency. Should we have unlimited concurrency? Should we have a limit?
Do we need to have concurrency?
And finally, there's error handling for scraping receivers, because for… request-type receivers, you can just… you should just forward the error.
But for, I guess, perceivers that don't have a way of sending a message back, do we retry, or do we just log?
I think writing down all that and kind of standardizing could be… could be helpful.
And I guess maybe also separately, revisiting lock on overflow, because I do not understand the rationale, to be honest.
Blake Rouse 00:31:23 I had a… I just have a question on the… on the whole… the whole thing. So what is our… so, like, if… If a receiver batches, say, 100, And the export helpers, you know, mint events is 1,000.
And a flush timeout is, like, say, 10 seconds, right? It's only gonna push 100 events.
Like… I guess it… I guess you… you were saying… you would just keep spinning go routines until it hits the limit, is what you're saying?
Jade Guiton 00:31:55 Yeah, at least that was my assumption of how most receivers worked, until now, but yeah.
Okay. If you have, like, a really long timeout and a really large minimum batch size, and also the exporter helper queue set to being synchronous, then you do run into this problem, yeah.
of, I guess you could call it head-of-the-line blocking.
Mikołaj Świątek 00:32:20 Yeah, I'm… I'm not sure… I haven't looked at… even, like, half the receivers in contrary, but from the ones I've seen, I think none of them does what OTLP receiver does.
I think, for example, in FileLog, FileLog without the new feature flag just has, like, some fixed number of worker threads in the converter, which submit the batches of 100. And in the new version, which is… it doesn't actually drop data when you When you kill the process, it's, like, one go-teen per file.
And… No, I think… I think none of… the new option also isn't ideal, but at least it doesn't drop data. So, if the intent there is to… if file log, for example, should do that, it should just do unbounded concurrency, then we need to go in there and fix it. I'm not sure… But I think this is… this is the most common thing I've seen, that there's, like, some… Either we just submit things in a loop.
synchronously, or we have some fixed number, or fixed, maybe, depending on the CPU count, number of submission of consumer thread, consumer grow teams, what's called.
Blake Rouse 00:33:46 I believe it's done by her file, so each file gets its own go routine, and it reads a set and submits, and that's… and that's just what it does.
Mikołaj Świątek 00:33:54 This is the new behavior, yes. But this is bad behavior if you're in this situation, and you have one file with a high data rate.
Blake Rouse 00:34:04 Yeah, exactly. Yeah, like, yes, exactly. That one file is very slow now.
Whereas if we could somehow submit to the queue and wait for a callback, we could continue to submit.
you know, and batch up those callbacks until they all come, is another way of doing this, where you don't need to create a go routine for every single call.
Mikołaj Świątek 00:34:33 By the way, by the way, just for a moment, I'm sorry if, like, this is essentially the end of this meeting, there's no topics afterwards, so if you're uninterested in discussion, feel free to drop.
We might stay here for a little bit longer.
Jade Guiton 00:34:51 Hmm.
Blake Rouse 00:34:52 What I worry is, is also this pushes… like, let's look at the file log receiver case, like you… like you described, like, a heavy… write heavy file, it's writing really heavy, and, you know, it's serialized, it's only… it's only sending X number of events per… Per thing. You know, with file log, you would want wait for result on, so you know that, you know, you have at least delivered one event.
To the exporter, and that it's there before you update your cursor, so you definitely want to wait for a result. So you have this, like, really slowdown. Now, a way to solve that slowdown is to ensure that the batch size that the file log sends is bigger than the min size.
I mean, that would solve it, right there, but… The downside to that is that you're pushing the configuration where it just doesn't work out of the box, right? Like, your configs that you do here, you need to make sure you have your configs right over here. Which is fine, I just think we should… either document that or make that clear. Like, if you're running with these settings in the queue.
There's no way for the receiver to get information about what their queue is.
Intrinsically, and… or through some interface, and then… you know, you need to configure those settings as well here. And if you misconfigure, you're gonna get a very slow… file read.
Jade Guiton 00:36:20 Hmm, I feel like… We shouldn't require too much coordination between the receiver and the exporter, especially the exporter helper specifically.
I think… Really, the… the only thing the receiver should be able… should… should… should… do is they should try to submit as much in parallel as possible, and then we need to have some kind of auxiliary signal to tell it to stop.
which… I guess the memory limiter extension kind of works like that, but it is a bit of a… it's not great, right? Basing yourself off of memory… Maybe not ideal.
So maybe we need to… think of a new way to tell receivers to slow down, I guess.
Mikołaj Świątek 00:37:08 I, I can tell you what… something that we… that… we thought about, because we, like, well, adopting, like, OTEL as our kind of framework, where we run things like beats, like FileBeat or metric beat.
as auto-receivers, and we had to bridge the queue models, which is how it's all kind of a ball of yarn going on in there.
So we thought about this quite a bit, and for example, one thing that makes it easier, that would make it easier to reason about this, or to have consistent behavior for this, like, how much concurrency is the right amount of concurrency.
is if your queue had, like, a promise model, essentially. Because right now, you kind of submit to a queue, you get back an error, or you submit to the rest of the pipeline. You get back an error, maybe you block.
But you don't know whether you're gonna block or not ahead of time.
And if what you got out instead was, like, a promise object, like, so you submit it, and it's a synchronous call across the processors, at least.
And in return, you get a promise, and now you can decide whether you want to wait for the promise or not, and you can wait for the promise in a go routine. And if you happen to, for example.
And if the queue is full, then block on overflow makes sense, because then you just block on it, and you can have a submission loop that's completely single-threaded, which just submits things and gets promises, and then just waits on them in the… In goutines. Then you detach the waiting for things to be sent from waiting for there to more room in the queue. And then you don't… you kind of naturally get to control how much data you have in flight.
Jade Guiton 00:38:59 Yeah, I mean.
Mikołaj Świątek 00:39:00 The problem is…
Jade Guiton 00:39:00 This is what I meant by unlimited concurrency, right? To me, the Go version of An asynchronous call that returns a price is just spinning up a Go routine that does the call, and then sends back a result on a channel, or something like that.
Mikołaj Świątek 00:39:16 Yeah, but ahead of time, you don't know whether it's gonna, like, for what reason it's gonna block, right? You spin up this go routine, and… If you have block on overflow enabled, then you don't know whether you're blocked because the queue is sending your stuff, or because the queue is full.
And if you don't have block on overflow enabled, then… you're kind of… maybe you can kind of figure things out, but if you're… you kind of have an inherent race condition, where, depending on how fast the pipeline tells you the queue is full, you might have spawned a bunch of other Geroutines in the meantime. It kind of depends on the timing in there, and even if the queue tells you it's full.
like, it returns an error saying it's full, it's not really clear what you should do with that information, or, like, reacting to that information is quite complex, from the perspective of, like, a receiver that just wants to submit data in a loop.
Does that make sense?
Jade Guiton 00:40:12 the way I see it is that the… the behavior when you're not blocking an overflow, when you're returning errors, is an edge case. It's when you're really stressed the collector, to the max. And so.
I don't think the receiver needs to be too smart. It should treat it like an error. It means we can't send data to the pipeline, or at least we can't send this data.
So it can keep… collecting data, spotting go routines to send them, and they are immediately going to return that the queue is full. It's not… it's a bit of a busy loop, so it's not ideal. But unless we do this kind of complex out-of-band signaling to tell the receiver to shut down, that's the best we can do, I think.
And I don't… again, I don't think the receiver needs to care too much about whether the promise will block or not. That's up to… That's kind of up to the person who configured the exporter helper.
I don't think that there's much the receiver helper could do with that information in the first place.
Blake Rouse 00:41:18 I would say about not blocking… I assume what you're trying… what you're saying is that you think that a block on overflow should just always error, and we shouldn't block on overflow?
Jade Guiton 00:41:29 I mean, yeah, to be honest, I don't understand in what context block on overflow true works.
correctly.
Blake Rouse 00:41:37 I would say… that I wasn't gonna answer.
Jade Guiton 00:41:39 screws?
Blake Rouse 00:41:41 But what I was gonna say is that if you don't block on overflow, one of the things I do see is that all the… the pro… so, like, you're not gonna know until you get to the right… until you get to Export Helper, so if you have a bunch of processors in between.
They're gonna do some work, and then you're gonna get to the export helper, it's gonna error, it's gonna come back up… up the pipeline, and then now all that processing work Will have to be repeated.
Jade Guiton 00:42:07 Yeah, I mean, that's the problem for… with block on a workflow as well, like, you always have this issue that you can't know until the queue is… the queue is full.
Blake Rouse 00:42:15 It wouldn't reproduce the work, though, you know what I'm saying? It wouldn't redo that work again, because they're gonna sit there, waiting.
Until the overflow's gone, and then go out.
Jade Guiton 00:42:25 That's only true… Wait, what? Oh, so you're assuming… that… The receiver has a retry loop, then?
Blake Rouse 00:42:37 Right. Yes. Well, you have to. File long receiver cases have to.
Like, it would have to retry. Like, it has to get those… it has to get those events through. Like, it can't update the cursor of the file until it gets those events through. So if it… if it fails on block on overflow, we're just sending the same events again until it doesn't block.
Jade Guiton 00:42:57 Right, yeah.
Blake Rouse 00:42:58 Until it doesn't error, in which case, every processor from the point of leaving the receiver to the exporter is repeated on every retry.
Jade Guiton 00:43:06 Right, I guess it is less performant, in that sense.
Not on CPU, at least, but on the other hand, in terms of memory.
I don't know if having a bunch of hang-and-go routines Is much better than having the receiver Like, hold the data in whatever way you can.
Alright.
Blake Rouse 00:43:28 Well, holding a channel is a lot smaller, and selecting from a set of channels is a lot smaller than holding a 2K stack for every call.
Jade Guiton 00:43:37 Yeah.
Which is, I guess, an argument for… in terms of memory, for document universal false.
Yeah, I guess there's also that consideration.
Mikołaj Świątek 00:43:48 you can probably… I think block an overflow false is possible to, like… if we take the file lock option, because the cases where we have a scraper are the cases where we're receiving data from elsewhere, these are simpler cases in this respect.
In the sense that the scraper can just drop the data and just emit new data on the next… on the next loop revolution, and a… and the receiver, receiving the data from… from elsewhere can just propagate the error downstream.
But in the case of, like, file log errors and similar situations.
you kind of, again, you don't really have a choice. It's a similar thing, for example, when you're reading objects from Kubernetes, like Israel noted, like, if you're just reading changes, like reading events in Kubernetes, for example, that's also just, like, a serial list of stuff, and if one of your calls fails, you don't have a choice. You have to retry… keep retrying it somehow in a loop. It would be great if you could block there instead of do a busy loop, right?
But… you have to do the busy loop if you do block overflow files. Like, you don't really have… like, the logic of your receiver forces you to do that.
Right?
Jade Guiton 00:45:07 Do you have to? Blake? Can you not… Completely drop the… the data, because, like, you can't ingest it.
Mikołaj Świątek 00:45:15 I mean, the idea is that if you're giving an error that's queue full, maybe in the future… like, the assumption is that you have some temporary remote failure, let's say, network partition. There's some, like, transient reason why it's failing, and so you just resubmit it because you hope eventually it's gonna clear up, and you'll be able to send it, and you can't really drop the data. I mean, you know…
Jade Guiton 00:45:40 To me, that's the job of the exporter helper. It stores a bunch of data in the queue, and it retries on its end. If it gets to the point, if the failure is not so temporary that the queue can actually hold it all, I don't think we should have Like a separate silent cue inside the receiver.
Mikołaj Świątek 00:45:58 Yeah, yeah, but that's exactly why block on overflow was added, in my opinion, so… because whoever added it had the thought that this is exporter helper's job, right? Why should… why should the receiver do this busy loop inside of it?
Where the exporter helper can just do the retries, right? And the receiver should just wait.
That's right.
Jade Guiton 00:46:20 I don't.
Mikołaj Świątek 00:46:20 I think that makes sense.
Jade Guiton 00:46:21 Like, to me, when you're on overflow, the… you're already in the situation where the collector cannot do its job anymore, because the exporter helper is responsible for retrying, and it can't do that anymore because it doesn't have any more space.
So… forcing… Forcing the data to remain in memory as a goroutine, I think it's just… it doesn't really make the receiver's job any easier, really. It starts blocking, and it doesn't help with the current situation where the collector is overwhelmed.
The best you can do is, like, for a scraper receiver that is single-threaded, like, it's gonna prevent it from sending anymore, but I think that's more of a… an intended side effect than anything else. Like, it's not gonna work for anything like the OTLP receiver.
Mikołaj Świątek 00:47:13 Like, I think for scrapers, it's… again, it doesn't necessarily matter, in the sense that…
Jade Guiton 00:47:20 Yeah, I mean, I'm including the fire log receiver as a screeper here, to be honest.
It's slightly different in the sense that it's, like, I guess it's an ordered scraper?
Blake Rouse 00:47:29 A bylog receiver cannot lose…
Mikołaj Świątek 00:47:33 I mean, it depends on what your, you know, it depends on what your model is, but typically, people are… like, in terms of just the semantics of the data, and what it's used for, it's usually fine to lose metrics that you're scraping, because you'll eventually, like, metrics are very biased towards recency, so if you lost some older ones, once you get new ones, those are going to be the most valuable ones that you have. But this is just not the case for logs, especially if you're in some kind of Audit logging situations when you absolutely have to guarantee that you're going to ship everything that you can ship.
Jade Guiton 00:48:14 If you need to guarantee that.
You can't rely on a retry loop inside the collector.
Because you need to have some persistent volume that keeps track of, yes, we've read this and sent it… sent it. And if that's… if you have that, if you have a way of keeping track of, I guess, the… the offset, like in Kafka.
then do you have an option of saying that if I receive an error from the pipeline.
I just keep the index where it is.
That way you don't use up additional collector memory.
Mikołaj Świątek 00:48:46 I mean, but this is… this is already what file log does. Like, FileLogReceiver in and out of itself, does keep track of that stuff.
Right? It does have a… it does have an on-disk state store where it keeps track of all the offsets, and it does only advance the offsets once it gets confirmation, or once the rest of the pipeline says, you know, okay.
Essentially.
Jade Guiton 00:49:09 Perfect, man.
Mikołaj Świątek 00:49:10 Which is the only thing it can do, right? But, like, that's not like a… but… But it still doesn't have to somehow solve… it still somehow has to solve the problem of… of the queue being full, like, what happens if the queue if the queue is full? You know, we submit… we submit things, in… you know, we do the same thing as OTLP receiver. Right now it doesn't, but in principle, let's say we're submitting things in one… like, a new guarantee per consume call to the rest of the pipeline.
And this works fine as long as the queue isn't full.
But the moment the queue is full, and the queue can easily be, like, full for…
Jade Guiton 00:49:52 I guess…
Mikołaj Świątek 00:49:53 flow control reasons, right? It doesn't even matter that the remote is wrong, it might just be that your… like, your file is gaining entries faster than you can actually export this. Like, this is something that can just happen in the world.
Jade Guiton 00:50:06 Right, and yeah, what I'm thinking is that I guess I should amend my statement that you shouldn't have a retry loop.
In the receiver. You can have a retry loop as long as it's not… like… keeping data in memory. Like, if you're reading from a file, you can read from the file again.
In the same way that you would when the file log receiver starts up and sees that, oh, I missed some messages.
I think in this case, having a…
Blake Rouse 00:50:32 How would you… I don't understand, why would you want to read the same line again you already have in memory that you're trying to send?
Jade Guiton 00:50:41 Well, to… because… to avoid an out-of-memory condition, because everything is full.
If you're reading one line at a time, that's probably fine.
If you're always sending in the, in the in order, then it's always fine to keep one line in memory.
Blake Rouse 00:51:00 They have to go in order. They can't… Can be sent out of order.
Jade Guiton 00:51:06 Right, yeah.
Mikołaj Świątek 00:51:08 I mean, technically they can, depending on what you put in your, like, file log.
We're close.
Blake Rouse 00:51:15 No, no, they have to, because they have to go in order, because the offset, the offset, the sync offset.
It has to go in order.
Unless you somehow know, like, the gaps you missed, in which case you're gonna resend.
The gaps, and now you're storing not just a single offset, you're seeing… you're storing, like, ranges.
Mikołaj Świątek 00:51:35 No, you mean, like, you have to submit them in order, but they don't actually have to be sent in order, because, for example, something you can.
Blake Rouse 00:51:43 Correct.
Yes, absolutely, yes. Yeah, I meant they… I was talking about just to submit, like, the consume… like, the way the consume logs is called… they have to go in order. Like, if you do them in groups of 100, like, those 100 have to be in order.
Well, actually, those 100 don't have to be in order, but, you know, you need to send the consume logs calls in order, but you're right, those hundred don't need to be in order. Another thing I'm bringing… Yup, is that… File log… For it to be durable, you have to configure your export helper to make it durable.
durability configuration.
Requires, now, all your other scrapers that might not be… need to be… Durable, to inherit that.
That, you know, you might not want these scrapers that are scraping metrics to have this durability. You don't really care about that durability. The file log does, and so now.
How do you…
Mikołaj Świątek 00:52:49 Honestly, I think that's just…
Blake Rouse 00:52:51 away.
Mikołaj Świątek 00:52:52 We can make this.
Blake Rouse 00:52:52 Where it doesn't have that…
Mikołaj Świątek 00:52:57 H.
Blake Rouse 00:52:59 I was gonna say, that's just pushing more on… on the… Writing the config to… Provide that durability.
On each one, and then even… and then splitting it across different exporters now. It's like, now they have, you know, exporter 1 and Exporter 2.
One for their metrics scrapers where they don't care about durability, and other ones where they don't, where it'd be great, you could mix those.
In my opinion, where you have one exporter.
And the receivers are saying whether I'm a durable receiver or not. Like, hey, I'm gonna send you the events, I need to know If they were… Done.
On the other case, and the other ones would be like, I'm gonna send you the events, I don't care whether they win or not, I'm just gonna send you another event in 30 seconds anyway.
Mikołaj Świątek 00:53:53 I'm not… I'm personally not that bothered about, like, having to configure exporters differently if you want different… delivery guarantees.
But it is… because even… you might even have file log where you don't care.
Like, this is just, like, a decision of the… collector operator.
Right? Where you have to decide which part… which… which parts of your data you absolutely have to have delivered, and for which you're okay dropping some under certain circumstances, and getting, like, performance in return.
Like, that's not something that weaken, I think.
Generically solve for anyone.
Blake Rouse 00:54:41 Yeah, that's true.
Mikołaj Świątek 00:54:43 Anyway, Jad has run away from us, but I do think that they're… that they're right, and we should, Create an issue to talk about this?
Does anyone else left in this call have opinions about this? Or should we… should we end? We're 5 minutes out.
Israel Blancas 00:55:08 From the… One thing that Jeet, mentioned about… Filling a ticket, right, with some recommendations and everything.
Something that maybe we can do, it's for those… Receivers, right, that are not behaving.
directly as the OTLP, like, for instance, PyLog and so on, right?
Documenting, maybe, at least on the rhythmi, what are we doing right now?
Right? Because I… Boom.
I know that operators sometimes have Problems, understanding exactly how the different components behave.
In these terms, right? Not just… On when they did return errors, but also sometimes, like, when they need to tweak performance or whatever, they need to figure it out.
the component has some kind of U or not, right?
Yeah, I think… I think this… this is one of the points where we need to maybe start, right, like, helping Yeah, maybe… maybe at some point we can get, consensus, right, and have all the procedures behaving in the same way. But in the meantime, I guess that the best that we can do is just to document how each one is.
He's behaving.
Mikołaj Świątek 00:56:32 For file log, this is actually documented.
Somewhere.
Israel Blancas 00:56:38 A word.
Mikołaj Świątek 00:56:39 It's documented somewhere because there's a feature flag which changes how it behaves, so… and that feature flag is documented.
So… It is.
Right? I don't know about many of the other receivers, but yeah, we should, like, have some… Have some model of… You know, depending on what kind of receiver you have and what it does, you should handle, you know, you should interact with the rest of the pipeline in one of these, like, specific ways.
Israel Blancas 00:57:13 Yeah, another thing that I was thinking is that maybe, I don't know, right, maybe it's a crazy idea?
Oh, that thing about knowing what's happening.
in the pipeline, right? Like, with the downstream components.
Well, I don't know if something… can be implemented, you see?
The health check extension.
Maybe.
Right? Where you can, like, from your receiver, you can query the… what… hold the… the health check-in point, right? Since we have that in components thing, where now you can… see the… health check from the different components. Maybe there is something right, that information there that we can expose or get from there.
That could… could help, right? For… I don't know.
Or if they self-check… Their thing is there, right? Maybe you can get some extra feature, right?
Oh, no.
Mikołaj Świątek 00:58:05 Yeah, but you'd have to have the… you'd have to guarantee that the health track is in the… Either you'd have to somehow guarantee that this always exists in the collector, like, maybe not the health check extension, right, but some component that lets you do it.
Always, so you can rely on it.
and also… I am trying to make things easier for receiver offers, not harder.
Israel Blancas 00:58:32 Yeah, yeah, yeah.
Mikołaj Świątek 00:58:33 you know, query who's in front of you in the pipeline, and what their status is, and what's going on. Yeah, you know, we could add an API where you can track what the queue is doing, but ideally, just, like, trying to send the data would tell you what the queue is doing. Right, so… I don't know, like, I actually consider doing something like, again, congestion control, where you kind of just send… you do what Jad said, you do unlimited concurrency, but you also track how… what your latency is on each send.
And if it starts growing, then you kind of back off and reduce your concurrency. And if it starts going back down, then you increase your concurrency. So basically do the same thing as CCP does, or congestion control. And that actually kind of works, I just don't think it's, like… Something every receiver should be doing.
Blake Rouse 00:59:27 Well, I think it'd be something that, if we wanted something like that, it'd have to be something that… Would be some helper or something that the receivers would use that just inherently gives them that, because…
Mikołaj Świątek 00:59:39 Yeah, but it's… it feels like a failure to have to… a failure of the QAPI, right? To have to do this kind of thing.
Blake Rouse 00:59:48 Yeah, I mean, I agree. That's true as well. I agree. Like, if you have to do… if you have to wrap the queue in something else to make this work, then yeah, the queue is broken.
Mikołaj Świątek 01:00:00 Yeah, and kind of, I feel a similar way, because this, like… congestion control approach is kind of similar to what Jad said with the, you know, disable block on overflow, and if you get an error, then just do some spin in there, right? And block every… and block your whole receiver on that.
spin, like, as long as you're spinning and trying to submit, and you can't, then everything else should stop. In principle, you can do that, but it also, like, feels like a very… A kind of a weird, complicated construct for something that the queue should just do for you.
Blake Rouse 01:00:40 Right, yeah, I agree, like, why wouldn't blocking just… just pause you right where you need to be? But to go back to the one about the helper, you are right that maybe the queue should do that?
But, if it was done in a helper where only the receivers that care about that, it might be enough? You see what I'm saying? Where, like, there are some.
Mikołaj Świątek 01:01:00 5 over Z.
Blake Rouse 01:01:01 that… Don't care?
Mikołaj Świątek 01:01:04 Yeah.
Blake Rouse 01:01:04 You know what I'm saying? Like, you know, if you're just scraping metrics every second, you know, you're gonna do…
Mikołaj Świątek 01:01:11 We just drop, right?
Blake Rouse 01:01:15 Yeah, you just don't care. Like, at that point, they're like, I submitted and whatever. But, like, in the file log receiver case, you care more about what you talked about, like, congestion control and the… and all that stuff, where a helper is valuable.
Mikołaj Świątek 01:01:29 Yeah, and…
Blake Rouse 01:01:30 Yeah, it does give us a way of… about having… Away.
Mikołaj Świątek 01:01:36 And in the OTLP receiver case, again, you don't care, because if you get an error saying Q4, you just send back, like, a rate-limited HTTP, you know, code down to whoever sent you the data.
Blake Rouse 01:01:53 Right.
Mikołaj Świątek 01:01:54 And that also works.
Blake Rouse 01:01:56 I mean, I kinda agree with maybe… We shouldn't have block on overflow?
Mikołaj Świątek 01:02:06 recollect We could try, we could try. We could try, like, turning it off and see what happens.
Blake Rouse 01:02:11 CPU.
Yeah, the only downside, I feel like is that with those events… I don't… what… that is a question, like, are those events manipulated in place? So, like, if they go through the processor again, do they just do the same thing again, or…
Mikołaj Świątek 01:02:27 Yes.
Yes.
They are manipulated in place.
So you'd have to also make a copy every time, which you kind of don't wanna, right?
Or, you know… Right.
Blake Rouse 01:02:40 No one, yeah.
Mikołaj Świątek 01:02:40 every time. You don't have to make a copy every time, but either your pipeline has to be idempotent, which I guess most of them will be, in a practical sense. You'll just redo the work.
But yeah, like, if you don't want… you don't want to make copies of a.
Blake Rouse 01:02:59 Right. No, the reason I was saying that, I wonder if… I mean, it's more… it's more work for processors.
Or would it be… or could we know that it's already went through the processors? And even though we returned an error, if you submit it again, we don't go through the processors again, but…
Mikołaj Świątek 01:03:15 I mean, you can't… We can construct that for our own purposes, right? But it's going to be hard to make it a generic collector.
mechanism.
Because you would have to have every processor, kind of like… or I guess maybe not, I guess just the collector should… Like, the collector should kind of…
Blake Rouse 01:03:36 Electric can know, right?
Right, yeah, the collector could know. It could say, I sent it through the processors, it could put some marking on the… on the event.
And then, if you send it again with that event, and that marking's there, it's the problem.
Mikołaj Świątek 01:03:52 Yeah, it's… it might… it might be… it might be a bunch of additional complexity in the collector.
Blake Rouse 01:03:58 Yeah, I agree, it might be… I think we'd have to look at that, but… and I'm not saying we would even do it, I'm just… I'm just… Sing time at this point.
Mikołaj Świątek 01:04:11 You're… you're breaking up…
Blake Rouse 01:04:12 Probably.
Mikołaj Świątek 01:04:12 By the way.
Yeah, we should end this meeting. We should leave. Nobody kicked us out. I don't even know who is the host. Who is the host? Who has the power?
I don't know.
Anyway, thanks, thanks for the… thanks for the discussion, you too. You too, Israel.
And.
Israel Blancas 01:04:33 No, thank you.
Mikołaj Świątek 01:04:35 Yeah, we'll open the issue and see where we can get. And I'll look at what the PR you linked, because it's also of some interest.
Alright.
See ya.
Israel Blancas 01:04:49 Mine…
