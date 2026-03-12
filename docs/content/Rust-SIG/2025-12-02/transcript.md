SIG: Rust SIG
Date: 2025-12-02
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**BA Björn Antonsson** 01:54 Hi there.
**Cijo Thomas (Microsoft)** 01:57 Hello, can you hear me?
**BA Björn Antonsson** 01:59 Yep.
**Cijo Thomas (Microsoft)** 02:00 Okay… Maybe another minute to see if anyone else joins, otherwise we can get started.
We don't have anything in the agenda, maybe we can just… Have a free flow.
Or anything in particular we want to look at, we should be able to do that today.
**BA Björn Antonsson** 02:57 Yep.
So I… there is, this, PR… I… I pinged you on it. It should really be merged. I think it's the one that fixes the… Case where you call, current context within the processor.
**Cijo Thomas (Microsoft)** 03:19 Yeah, I had a very brief look at it, let me take another look today and merge it in.
I believe there were a few open items here.
I think there was a discussion about refactoring span processor. I think you already saw that, like, we have an existing PR from…
**BA Björn Antonsson** 03:42 it's, it's, it's, it's my, I mean, so there's a PR now, but there's also a PR from, from Paul, from earlier, so…
**Cijo Thomas (Microsoft)** 03:51 Yeah, because I was also looking at what we are currently doing in Tracer for doing the span start.
It looks like a lot of work is being done there.
I was looking at this old issue.
**BA Björn Antonsson** 04:04 Yeah, okay.
**Cijo Thomas (Microsoft)** 04:07 this is something which I want to see if we can do something to improve, because we had this for a long time, and .
**BA Björn Antonsson** 04:14 Mmm…
**Cijo Thomas (Microsoft)** 04:15 The idea is, like, we create Span Builder, and then… use, like, tracer.start or one of the overloads.
But the… question or concern here was to create the span builder itself, it's a lot of… No trivial amount of work, because we accept a vector, so people have to give up the…
**BA Björn Antonsson** 04:37 Okay, okay.
Okay, that would be interesting. Could you just ping me on that?
**Cijo Thomas (Microsoft)** 04:45 This would be, like, interesting. The main reason is, thing I, I, I, I… I saw another comment from you on this one. Let me actually… the extra convenience one, yeah, I think… I did see your comment about the marking. I want to, like, spend some more time, like, discussing that.
Yeah, it's not…
**BA Björn Antonsson** 05:09 Yeah, no, I completely agree, because, I mean, in the tracer in spam thing, I don't think it's really… Good thing, because… As soon as you put it in the context, you have converted into a synchronized span, and you have a mutex around every set attribute call, etc, so it just becomes… prohibitively expensive.
So, a better thing would be in… I mean, the tickets you showed looked interesting. I haven't really gone through all their tickets properly, which I maybe should.
Because, yeah, the builder is not the… it's kind of a heavyweight.
The way it is, right now.
**Cijo Thomas (Microsoft)** 05:59 Yeah, one idea which we were, like, floating at that time was, like, we want to be, able to Call the start span.
And come to a sampling decision at the cheapest cost. And once the decision is favorable, like, which is, like, if it's in the recording state, then we can afford to be, like, slightly slower, because if span is recorded, then the user has already committed that, okay, I'm spending some time, or I'm going to spend on this span, so it's okay. But the typical pattern which we've seen is, Only, like, a small percentage of spans are sampled in.
So the majority case is the unseumbled case, which is why we want to see if we can improve that.
**BA Björn Antonsson** 06:45 Yeah, but on the other hand, we compute stats on all the spans, so it doesn't really matter. You want to have all the tags on the span.
**Cijo Thomas (Microsoft)** 06:54 Oh, that's for the Span 2 matrix pipeline, right?
**BA Björn Antonsson** 06:57 Yeah, I mean, we do it in our trace exporter right now for Datadog.
**Cijo Thomas (Microsoft)** 07:03 Yeah. Yeah, I mean, like, for people who are willing to pay that cost, that's generally fine, because they accept that I need to create the span, I'm going to extract metrics out of it.
So it's kind of implied that, okay, they are willing to spend some performance cost, but I was mostly worried about the other end, where people are doing, distributed tracing. They usually go with 1% or, like, very low, percentage of sampling.
Oh.
**BA Björn Antonsson** 07:29 Yeah, but I mean, that's… that's… that's still… I mean, that's for what you send to the backend, and not what you compute metrics on, or stats. But, I… I think, I think, yeah.
It's fine. I will look at the other, other, ticket and, and, and see if you can list.
**Cijo Thomas (Microsoft)** 07:50 Yeah.
One thing which I remember is, from the span builder, it's… it's… not yet at a point where we are committing to a span. We are trying to see if there is a span going to be created, so Span Builder could potentially accept a… Slice, instead of… Full vector-owned one, and in the event sampling decision is favorable, it can internally do away.
copy of, slice in vector one. I believe we were… yeah, this was the original one, I mean, this was created, like, 2 years ago. At that point, like, we were… all the time, like, whenever someone creates a builder with span attributes, it accepts anything which is into iterator, and then we created some internal data structure.
Which pretty much involved, like, copying everything into a heap and doing some sorting and deduping. This was quite heavy, but now we are not that heavy, we are simply doing a vector.
So anyway, I'll share the link, see if it's something we can do to.
Yeah, and there are, like, very large number of low-hanging fruits in the… start span path, I did take a look yesterday, like, even, something very simple, like, we are creating a span ID even before samplers are run, but that's something very easily avoidable, because we don't need Span84.
samplers, it's not an input for the sampler, so we can delay…
**BA Björn Antonsson** 09:17 Kind of depends.
**Cijo Thomas (Microsoft)** 09:20 Can you elaborate? Like, what's the need for Span AD to be…
**BA Björn Antonsson** 09:25 I mean, the… that… that, if you have… if you have a fully randomized, span ID, according to the W3C spec, you could use that to, like, drive your…
**Cijo Thomas (Microsoft)** 09:43 No, span AD is not even an input to the sampler, it only accepts…
**BA Björn Antonsson** 09:47 Don't you listen?
**Cijo Thomas (Microsoft)** 09:49 It is only trace-ady.
**BA Björn Antonsson** 09:52 Okay, so it's… oh, so it's only the trace ID, and… Exactly.
**Cijo Thomas (Microsoft)** 09:56 Tracy, then, like, the parent… Parents' sampling decision, then any Attributes which you provided as part of the…
**BA Björn Antonsson** 10:07 Oh, okay, okay, okay.
**Cijo Thomas (Microsoft)** 10:09 Inspired is, like, not even an input, which is why we can do that.
**BA Björn Antonsson** 10:11 then it's… but, I mean, on the other hand.
But of course, you… OTL has that as a byte array or something, I guess, so…
**Cijo Thomas (Microsoft)** 10:23 Yeah. Yeah, anyway, like, I just meant, like, there'll be, like, few improvements.
**BA Björn Antonsson** 10:26 But, I mean, for the width span and other things, the real cost is actually converting the span into a synchronized span and cloning the context.
So, that's… that's the cost.
**Cijo Thomas (Microsoft)** 10:42 Can you, like, tell me something about, like, what is the typical pattern which you have seen? Like, is it the… one pattern which I have seen is… for the incoming request, which is likely the root span inside a given process, you create the span activated,
**BA Björn Antonsson** 11:00 Yup.
**Cijo Thomas (Microsoft)** 11:00 And then, you probably have, like, multiple child spans, but those spans… Are only created Depending on the sampling decision, like, if the sampling decision favorable. They try to not even activate the context.
**BA Björn Antonsson** 11:16 But I'm not sure whether it's a common… That's not usual for…
**Cijo Thomas (Microsoft)** 11:21 I see,
**BA Björn Antonsson** 11:22 I mean, most people don't really look at, what's this sample do this or that, because.
generally have some type of Lambda-style thing, and you… you create your span, and I mean, that's why it needs to be really… really cost-effective to create the span and activate it, etc. But, yeah.
Maybe it's different in Rust. I haven't written enough Rust applications to know that, I would say.
**Cijo Thomas (Microsoft)** 11:52 Okay, yeah, because we did something in, .NET which is not, spec compliant, it's pretty much, like, in violation of the spec. What it does is.
We create the span for the root one, like, if there is no parent, this is the first span in that process, we do all the heavy lifting.
But subsequently, if you're trying to create a child span, and we realize that the… sampling decision is unfavorable, we don't even create the new span, like, we just keep the original parent as the active span throughout, so we don't have the cost of activating any of the child spans. It's not in the spec-compliant way. I did have, like, some issues opening the spec to see if spec can bless something like that.
I think you… once you read this issue, you'll probably see, similar.
Like, discussions where, like, you don't, want to, like, spend any cost on all those child spans, because you already determined that from the parent itself that you're not going to assemble it in.
So any work you do for all the child span, including the cost of activation, deactivation, converting that to synchronized plan, all of them are, like, just wasted, because we are not going to send it to the backend, and if you're not doing metrics pipeline, then you're not Going to do anything with that spans at all.
But anyway, like, since it's not spec compliant, I don't want us to do that by default, but maybe a, optional thing, which people can obtain. But anyway, let me do one thing, I'll…
**BA Björn Antonsson** 13:23 Nope.
**Cijo Thomas (Microsoft)** 13:24 tag you here, and I'll tag you in the spec issue also, just to see, like, if.
**BA Björn Antonsson** 13:28 Okay.
**Cijo Thomas (Microsoft)** 13:29 Like, your customers have.
like, hit similar issues and they want to do something very fast, because our… the Rust's synchronized span is a very, like, it's quite concerning, that… especially with the lock and all.
It's… we don't have a benchmark which spins up multiple threads, because all of them are doing, like, normal single thread. We will only know, like… I mean, in this trust test, I think we added, like, tracers, but I don't think we are activating… yeah, we are not activating the… context of… I mean, this kind of tests will easily tell whether it's creating any real contention, because if it is, then, like, we really need to Like, try and improve that.
Okay, yeah, any other things which we want to… Because there are a few open… PRs, but yeah, this one we covered is… I think these are, like, relatively small one, we're already reviewing it.
This will be discussed, there is this PR about metric validation, I did… reply to it. I don't know whether you have any context on matrix validation.
**BA Björn Antonsson** 14:45 Not that much.
**Cijo Thomas (Microsoft)** 14:46 Okay, yeah, then I'll just skip it. That's something which we want to do, but we'll need some help from the… specification to make it happen, yeah.
Yeah, I think there… there is nothing, like, critical to be discussed synchronously. We should be able to look at things offline.
**BA Björn Antonsson** 15:05 Yeah.
**Cijo Thomas (Microsoft)** 15:07 I mean, I also had, like, one PR in the tracing OpenTelemetry yesterday while I was looking at the the bridge thing, yeah. So, based on the refactoring which you have done, to do the convext activation, I believe now we have reached a point where the tracing OpenTelemetry does not need the SDK dependency at all. It was taking… Sorry, it was taking a dependency on the SDK previously. I did try to remove it in the past, but at that time it was not possible because it was doing something, but after URPR went in.
I think you did some cleanup, which means we don't really need a SDK dependency. We still need it for the, like, testing purposes, so we can still keep it as dev dependency, we don't need this one for… Yeah, I sent this PR, I mean, I know that you're not active in that report, but if you want to take a look at it, I'll put the link to the chat so we can take a look. It's failing for a different reason, not for…
**BA Björn Antonsson** 16:06 Yeah.
**Cijo Thomas (Microsoft)** 16:06 this one, but yeah. It's just a good way of, like, in general, like, Open Elementary wants people to avoid SDK coupling, so in their… events, they want to replace SDK with something else, they can do it. So, yeah, it's very rare, but still, like, yeah, let's stick with the spirit of OpenTelemetry, yeah. Anyway, I'll tag you here, so you can also review from an OpenTelemetry perspective.
**BA Björn Antonsson** 16:27 Yeah, no, I mean, that sounds good. I… of course, yes, it's only using the builder… Yep.
**Cijo Thomas (Microsoft)** 16:34 Yeah, yeah. There was something in the past which required SDK, I cannot remember what it is, but yeah. No, I mean, it was the pre-sample tracer and other things.
Okay, got it, yeah.
Yeah. Anyway, that actually reminds me of, like, you did some cleanup in the in the tracing API, I believe, like, we still have, like, a few more… to be done there, I mean.
**BA Björn Antonsson** 17:02 Good?
**Cijo Thomas (Microsoft)** 17:03 like, feel free to, like, self-assign if you're working on it, but if you need help, feel free to, like, tag me. I should be able to, like, help with, some of them. I don't know which one I want to pick.
But I will, by default, assume that you are working on it, so I won't touch it unless you explicitly tell, because we don't want to, like, work on… Same thing, yeah, for example, like, this is another thing.
We have this…
**BA Björn Antonsson** 17:30 Ling and related.
**Cijo Thomas (Microsoft)** 17:31 the concert.
**BA Björn Antonsson** 17:31 Hmm.
**Cijo Thomas (Microsoft)** 17:33 Yeah, there is some sampling construct, yeah, sampling decision. These are in the API grade, open elementary.
We needed it in the past, because of the tracing open telemetry thing.
**BA Björn Antonsson** 17:43 Yeah, yeah.
**Cijo Thomas (Microsoft)** 17:43 Where we goaded of this, we should be able to, like.
**BA Björn Antonsson** 17:46 Simply lifted to the… Absolutely. I mean, that can just be moved into.
**Cijo Thomas (Microsoft)** 17:51 Yeah, yeah, I think, like, there are, like, few more, issues like that. The… And there is another thing here, which I believe, yeah, Tracer and Span Builder, like, I'll tag you in a few of the issues to see if you…
**BA Björn Antonsson** 18:05 Oh, yeah, that's fine, yep.
**Cijo Thomas (Microsoft)** 18:07 Yeah, yeah, again, this is something… these are, like, something which I did work on, like, in the past, but since then, I never got a chance to finish it because I moved to logs and metrics, so this is time to, like, come back and do… Yeah. But anyway, by default, I'll not be working actively on any of those things, but yeah, if you want to, like, it has some help, like, feel free to tag me, and then we can split, so that we don't, like, accidentally work on the same thing.
**BA Björn Antonsson** 18:33 No, no, I mean, that's fine. Feel free to tag me on those. You have a way better, knowledge about the tickets, existing tickets, so it's… I'll get to some of them.
**Cijo Thomas (Microsoft)** 18:45 Yeah, we also have the, tracing API stable milestone, which I believe I did link everything, which I believe should be covered, into…
**BA Björn Antonsson** 18:54 Yeah, okay, cool.
**Cijo Thomas (Microsoft)** 18:55 So this should be a reasonable thing to, for us to look at it.
Okay, yeah, I think that's pretty much what I wanted to cover. Hey, Christian, looks like you joined a bit later. I'm not sure, like, at what point you joined. Anything which you want to discuss? We were otherwise about to wrap up.
**Christian Leghadjeu** 19:18 Nothing special for me.
I mean, nothing special for my entity school.
**Cijo Thomas (Microsoft)** 19:26 Sorry, I didn't get the last one, can you repeat?
**Christian Leghadjeu** 19:31 Are you good to me?
Can you hear me?
**Cijo Thomas (Microsoft)** 19:36 Yes, I can hear you now.
**Christian Leghadjeu** 19:38 Oh, yes, I see nothing special for me.
**Cijo Thomas (Microsoft)** 19:41 Okay. No.
**Christian Leghadjeu** 19:42 I just proposed on a… on an issue to work on it.
Yeah, yeah, I think I got the notification just now, so I'll…
**Cijo Thomas (Microsoft)** 19:52 Take a look and assign it to you. Thank you.
**Christian Leghadjeu** 19:55 Yo.
Good, thank you.
**Cijo Thomas (Microsoft)** 19:58 Okay, I think we can end early, beyond, like, I will tag you in the issues which we just discussed, and we can continue the discussion in GitHub.
**BA Björn Antonsson** 20:08 Absolutely.
**Cijo Thomas (Microsoft)** 20:09 Alright, thanks a lot for today.
**BA Björn Antonsson** 20:11 Bye.
