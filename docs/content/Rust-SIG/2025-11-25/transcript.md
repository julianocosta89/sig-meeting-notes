SIG: Rust SIG
Date: 2025-11-25
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Prasad Sawool** 02:56 would it be?
**Cijo Thomas** 06:22 Hey, Bjorn, sorry, looks like just two of us.
**BA Björn Antonsson** 06:28 Yep.
No worries, I saw that you were being late, so…
**Cijo Thomas** 06:34 Yeah, I had to drop the kids today at school. I'm still on my way back home.
So it's from my phone.
**BA Björn Antonsson** 06:42 Okay, so I, I only had really… I mean, there are… three things I am gonna paste into the agenda. There's my small, convenience method PR that should be good. I addressed your comments.
**Cijo Thomas** 07:05 Okay,
**BA Björn Antonsson** 07:06 And then there's… A fix by an external contributor for, current context.
Inside of the span processor.
On-end method, which was, like, actually crashing before.
**Cijo Thomas** 07:26 Yeah, yeah, I remember that point, yes.
**BA Björn Antonsson** 07:29 Yeah, so it has… Some percents, but very low number, degradation of, of, like, context attached and other things in general.
**Cijo Thomas** 07:41 Okay.
**BA Björn Antonsson** 07:42 But I think that is perfectly fine, because we need to… I mean, we can't have it.
**Cijo Thomas** 07:48 that way. It needs to be fixed, so I reviewed his first.
**BA Björn Antonsson** 07:54 proposal, and then the, the, the, changes he made from, based on my comments, and I think it's, good to go.
**Cijo Thomas** 08:04 Okay, so I just need, like, another review, and we can get it in.
**BA Björn Antonsson** 08:07 Yeah, absolutely. And then he… race… But maybe we can take that up the line. He raised possible ways to implement support for For the… for the… what is it called? AutelPropagator's environment variable, and I, I… I need to wrap my head around what the spec says and what we do right now, but I would like for things to… I would like… Or… that it's not too automatic, and I don't… would not like any, like, dependencies on the SDK from the from the… from the, like, API, which he kind of proposes, or move things to the API.
Because… I mean, as a, as a… Outside contributor, and we are trying like, Datadog is trying with our, Set up.
helpers to, like, override some configuration based on OpenTelemity config, and old data.config, and then eventually, based on what the… what the… what the new, specification… like, configuration…
**Cijo Thomas** 09:42 base config.
**BA Björn Antonsson** 09:43 bio-based one. And… and if… if… if we don't separate the reading in, and then, like, processing, and then setting things up, and it just automatically installs the global ones, I think that would be unfortunate, so to speak. But we can discuss that in the issue.
That he commented on.
**Cijo Thomas** 10:09 Okay, got it, yeah. So this is specifically on the propagators.
**BA Björn Antonsson** 10:13 support. Yes, I mean, there's, there's, outpaced in the, the relevant, Issue.
And then we also have, Paul from Datadar, proposed some changes to… Was it the spam?
processor or exporter, one of the APIs, because we had to clone data right now.
**Cijo Thomas** 10:44 Oh, yeah, I think, Paul sent a proposal, like, a few weeks ago. Is that…
**BA Björn Antonsson** 10:49 No, I mean, it's… I think it's more than a few weeks, but it was sort of, like, pinged by Scott a few weeks ago. Yeah. Yes, that's the one. I can… I can just sort of, like.
Paste them all into the agenda if you're, like, traveling right now, so then we can, like, maybe discuss it offline, or you can take a look at the… PRs.
**Cijo Thomas** 11:11 Yeah, the only reason why I didn't get, like, much time to look into the SDK side of things, But I'm wondering, like, do you think, like, we have, still… API cleanups left in the tracing API? I know that you cleaned up a bunch last week.
Are there, like, more changes in the API? Because I'm trying to see if we can at least call the API side of tracing relatively stable, and then start tackling the SDK things. Totally up to you, like, I'm not enforcing any ordering, it's just that in my mind, API always…
**BA Björn Antonsson** 11:44 No, no, I agree. So I have one… one… more… thing that I'm looking at, and that is sort of… Trying to, like, the no-op spam right now is not so no op. It actually does a few, like.
What do you say?
It creates, It creates a synchronized span that actually takes lock just to jump into methods that don't do anything, for example.
Got it.
**Cijo Thomas** 12:25 And that might…
**BA Björn Antonsson** 12:29 do something with the trades. I'm trying to figure out how to do this nicely, but, apart from… apart from that, it should… should, be good to go, and I'm gonna try to… Get that done this week.
**Cijo Thomas** 12:45 Okay, yeah. Yeah, maybe, like, next week we can do one joint exercise going over the… tracing API, all the public one, just to see if there is anything which looks incorrect or deviating from the spec or anything. We did the same for metrics, like, a few months ago, and that was very useful, so we can do the same for tracing.
**BA Björn Antonsson** 13:07 Absolutely.
I'm trying to figure out exactly what should happen if you have an invalid span context.
When you create… when you create spans, and I'm… I think that I'm… I mean, I… I try to use that to do some optimizations, and I think I'm a bit too aggressive. It seems that… You're actually gonna propagate the… trace state and the flags and treat them as if they are valid, even, even though the actual, Context is sort of like, empty. I'm not sure how that… that… But I'm trying to figure out, exactly how it should work without breaking what is there, if… and see if we're… because all the discussions on GitHub are, like, old, and kind of go around in circles, it feels.
**Cijo Thomas** 14:05 Oh, okay.
**BA Björn Antonsson** 14:06 It's, it's really old, like, before the, the, the, like, this spec was finalized, and it's sort of, like, V0.6 or something.
Okay.
But… but I think we, as in Rust, is doing… something right now, which is sort of okay, but we could do it a little bit differently. Java, for example, they… if you have an invalid trace or span ID, you set them both to zero, but you still propagate the rest.
**Cijo Thomas** 14:43 When you say Rust, tri-State is the only remaining thing, right?
**BA Björn Antonsson** 14:48 Yeah, and flags.
**Cijo Thomas** 14:50 Okay, and Flexa, okay, good.
**BA Björn Antonsson** 14:51 Yeah, so… But, which fields… I mean, the flags should maybe be zeroed out as well, I don't know, but .
**Cijo Thomas** 15:01 Okay.
**BA Björn Antonsson** 15:03 Yeah, so… so I'm… maybe that is something we should do, because… But, Yeah, I don't know. I'm gonna look into it anyway, at the same time that I tried to make the knob span a bit faster.
**Cijo Thomas** 15:21 Yeah, I think there were, like, a few more, discussion on some of the tracing APIs in the past.
We never, like, actively looked at it. We had, like, people raising comments, engaging in discussions, but we never, like, actually did anything about it. I'll try to find, like, some of those issues, because now it's time to, like, act on them.
Because now we don't… because a lot of them boil down to, unwanted exposed APIs, which we have… at least part of them is now removed, so we should be able to look at them and see if we can do better. And the… the no-op span performance, that was something which many people raised as a concern.
So thanks for, like, addressing that, because in pricing, the number one thing people would ask was, if I don't sample it.
which is basically an op span, or if I don't have tracing enabled, then it should be, like, as close to zero. But unfortunately, we are paying much more than zero.
**BA Björn Antonsson** 16:19 Yeah, absolutely. And, yeah, we'll see if, if, If we can sort of, like, remove that, A bit.
Okay. Especially for the no-up span. I think… I think we can.
**Cijo Thomas** 16:41 Yeah, there were even…
**BA Björn Antonsson** 16:42 good.
**Cijo Thomas** 16:43 Yeah, there were even discussions about the very idea of no ops span, because it made sense for most languages where if you create a span and the sampler returns, like, drop, if you return, like, a null kind of thing, it would have been, like, very bad for most languages. So there were some discussions In the, like, 2 years ago, people were saying.
**BA Björn Antonsson** 17:07 It'd be.
**Cijo Thomas** 17:07 don't need, like, no op span, we can have an option of span, so if it's not there, then we'll just return none, the variant. So we need to be more idiomatic to the Rust way instead of doing the spec way. There are a lot of discussions from the previous maintenance, but unfortunately, there was no one to continue that discussion at that time. This was the time when I really joined the OpenTelemetry, so I didn't have, like, much expertise to check.
But yeah, I'll try to dig up.
**BA Björn Antonsson** 17:37 I went through that, that, PR and that discussion at that point. I think, I think… I mean, it also, even if it's more idiomatic, it also Adds a bit of, Like, complexity is not the…
**Cijo Thomas** 18:01 Huh.
**BA Björn Antonsson** 18:02 Right thing.
**Cijo Thomas** 18:08 Yeah, I think we can, like, use the, like, offline discussions for that. Yeah, I'll discuss that.
**BA Björn Antonsson** 18:13 Absolutely.
**Cijo Thomas** 18:14 Yeah. Okay, any other topics which we want to cover?
**BA Björn Antonsson** 18:21 No, I mean, that was mostly it.
**Cijo Thomas** 18:27 Okay, yeah, if that's the case, we can end a bit earlier, and hopefully by next week, we'll do the protestation, like, one week.
US-friendly, and next week, Europe-friendly.
So scored, and I will make that happen by next week.
**BA Björn Antonsson** 18:43 Yeah, excellent.
**Cijo Thomas** 18:44 Alright then, thank you.
**BA Björn Antonsson** 18:46 Okay, bye.
