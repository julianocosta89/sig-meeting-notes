SIG: Sampling SIG
Date: 2026-01-29
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/zcEDGCVsE00Kx5ADFn8oeiUTiovhH-apFcUB2XTs_r5Q0YqLlECg-i2fcwGo1YsI.7wK6-vpXZb3BbLwd
============================================================

## Zoom Recording Transcript

**jmacdonald** 02:55 Hello.
My volume is very loud for a second, but here we are.
**Peter Findeisen** 03:02 Good morning.
**jmacdonald** 03:03 I see a few items, and we're all here… I mean, enough of us are here. Good morning, Peter. Good morning, young one.
So I pulled up our notes.
I was excited to see… Pop.
Peter has put up a new PR.
**Peter Findeisen** 03:25 Yes, so… of course, this is not… directory affecting any samplers, but this flag is exclusively used by samplers right now, so I think it's relevant, and we build, Our consistent probability sampling.
solution based on assuming randomness of trace AD, so this is… Important and relevant.
So, whoever is familiar a little bit, even, with the SDK, Java SDK, please have a look. It is a very… Simple fix, really. I added one flag to ID generator that would indicate that it is compliant with W3C Trace 8 Level 2.
Specification for randomness.
And, of course, we have to implement the new flag in the trace flag class, and… The last change is to propagate those things to the sampler.
**jmacdonald** 04:37 Cool.
So I take it this is the first, sort of the first step of adding that random flag, getting us to the W3C level 2. Interestingly, Yuan, Yuan, and I were talking about the same change in Go, basically. Like, that's step one in any SDK.
So this looks good so far. I, I can, I can review this. I can read Java.
**Peter Findeisen** 05:00 Thank you.
**jmacdonald** 05:01 And it's delightfully small, so that's nice.
**Peter Findeisen** 05:05 It is.
**jmacdonald** 05:06 looking at some very large PRs lately. So yeah, this… is there anything controversial or anything you stumbled on that you would like to talk about? I would be glad to approve this.
**Peter Findeisen** 05:17 Well, no, I don't think there… there is a lot of controversy. There could be some next steps, which… which are, Well, I, I, no, let's, let's not mess up this. Let's keep it simple.
Yeah.
**jmacdonald** 05:38 Great, yeah, and I think, this is the appropriate way to do it in steps. I would, Yeah.
Very good. Hey, Yuan Yuan, have you… did you, would you say that we, have any progress on the Go SDK? I know that you and I were looking at it, it doesn't mean you've done anything.
Just in getting that random flag started. Like, the same PR as this one in Go is something that we need, I guess, and… Anyone can do it, obviously, but, I had that old, PR, in the Go repository, just, like, doing the same as this, but we… I don't need to… we don't need to bug Peter about that.
Very good.
I will be glad to approve this. Peter, thank you.
**Peter Findeisen** 06:31 Thank you.
**jmacdonald** 06:33 Before this meeting, I… I was…
**Peter Findeisen** 06:37 Oh.
**jmacdonald** 06:38 Going over all my…
**Peter Findeisen** 06:39 We cannot hear you. Yeah, you asked a question in the chat here.
Something is…
**jmacdonald** 06:47 I can't hear you.
**Peter Findeisen** 06:48 I don't know.
**jmacdonald** 07:10 I can't hear any, Oil, I hear Peter.
Yeah. Well, she can work that out. While we're here, Peter, I will share that there's something happening in the collector, it is a… proposal for donating a new sampler. It's a… not asking for any help. I've agreed to do some work to review this. It looks… I mean, I wouldn't say no to any good… any sampling component tree. This is by the author of the tail sampling processor.
They have been using it, in a… production pipeline, as far as I can tell, based on OTEL components, so it's the OTEL trace, sorry, tail sampling processor, and then this new pruning processor.
And it has… Totally disregarded any of our work on… on, sampling probabilities, but that was also the problem with tail sampling processor. Yes. And so… but I am…
**Peter Findeisen** 08:15 Sorry for interrupting. Yeah, I just read this, description this morning, and I left one comment at the bottom.
Oh. And I think it's a fairly simple thing to make it compatible. He just should aggregate only spans which have identical trace state.
That would mean that they are sampled with the same probability, and that means that The backend will correctly take… Count both approaches, of course, because it needs to read those additional attributes that he has for aggregation, but also looking at the sampling probability, and it should work.
**jmacdonald** 09:02 I think I'm following you, and I was looking, because I've glanced over this already, there's a grouping, a group… Group definition. Spans are grouped by span name, span kind, status code. I think what you're proposing is that if… as long as we put trace date in this list, mostly this will just work out correctly. That's really good feedback.
**Peter Findeisen** 09:24 Yes.
**jmacdonald** 09:25 And you said you left a comment, but where?
**Peter Findeisen** 09:28 At the very bottom.
**jmacdonald** 09:30 Here, okay, good. Yes, thank you. Alright, that's, that's all I needed, I… I will be helping this get merged. I see no reason not to, basically, but that's good feedback. As I review the code, which is a great deal, it's gonna take some time, it's like 9,000 lines of code.
I will keep that in mind.
Anyway, I, I felt like it was the right thing to do, so I'm… I'm saying I will.
Thank you for that feedback, Peter. Glad I mentioned it.
Cool.
Well, I have no more on that topic, and I wonder now, Yuan Yuan, if your microphone is working and would like to talk.
Draft PR attached, hey.
**Yuanyuan Zhao** 10:35 Yes?
**jmacdonald** 10:36 Oh, there you are.
**Peter Findeisen** 10:37 Okay, we can hear you.
**Yuanyuan Zhao** 10:40 Okay, I haven't pushed the latest until this, I… I… I went off, forgot pushing. But I think that it's close to a state.
that we can, have it for review. I can tell you what the current status is. So, Peter, do you have the context of what we are doing over here? Josh and I have been talking, so we have the context. This is basically calculating the extrapolated metrics from, sample spans. So there are, a couple of, technical challenges. One is, like, the fractional counting, right? We use the stochastic counting.
I had to do it in a way that is actually stochastic division, so that it doesn't deal with floating-point numbers, instead just the integers.
The details is in the file. That actually improved the performance. There is another, performance drag, which was from the parsing of, W3's, trace state. The majority of that is in, the regex matching.
So, I did…
**jmacdonald** 11:58 And…
**Yuanyuan Zhao** 11:59 I don't know whether it's… it's already pushed there or not, but I… I did some comparison, which basically, instead of using regex to match, which checks the valid, validity of the trace context, the trace state string, I… well… actually clawed.
I asked it to, to basically, generate, the kind of, like, sequential, validation, and that improved the performance by quite some.
I also added a very simple, one last, last value, one last value.
Because when you are, like, generating… processing traces, there are typically many spans, and they could have the same trace contact… trace state.
So if we just cache the last one, there's a chance for a good cache rate. So all of this together has dropped the performance degradation, from, about 80% increase to under 4%, and this is also only in A benchmark with a trace comprised of only 3 spans.
So if there are more spends, then, the impact will be even more amortized.
The… the change to… To the, validation, change away from using regex, by itself, should be… it produced a lot of performance savings. I think dropped something from, like.
670 nanoseconds to, it dropped by, more than 500, close to 600, so in the end, it was only, like, under 100 nanoseconds, or, Added overhead for extracting the… extrap… The stochastic… adjusted count.
So, that's there. The current, status of the PR, which I probably haven't uploaded the latest file, is that I… I left some performance comparison Between the regex match.
to, the hand validated match over there. So, that… that's basically for the intermediate phase of the review.
It's not there.
**jmacdonald** 14:48 I got a… I got…
**Yuanyuan Zhao** 14:52 Yeah, this is an older version. I will upload a new one right after.
**jmacdonald** 14:55 Let's not look at the code, then, right now, I understand, and I've forgotten to push a hundred times. So, The question… I have a couple questions that I… maybe you can help. So, where the… so I saw, briefly, and I… when I opened that PR, I saw the use of this package called sampling. So this was the code that the other sampling component is using. I saw you using this.
**Yuanyuan Zhao** 15:18 Yes. I don't believe this uses regexes to parse.
**jmacdonald** 15:21 So I was…
**Yuanyuan Zhao** 15:23 W3C TraceState.go.
**jmacdonald** 15:26 It does? It does use water? Yeah, look at it, look at it. Oh, I remember, yeah.
**Yuanyuan Zhao** 15:30 stay.
**jmacdonald** 15:30 Kent asked me to. He's like, don't…
**Yuanyuan Zhao** 15:33 Yes, that's expensive. That's expensive. And I have a new, benchmark file that… that compared this, and the new implementation. I'll just push that. This is expensive. This is the majority.
Of the overhead.
And then also, I… I… there is also some cash thingy, which you, you should review after the meeting. Yeah, that's… That's actually a good part.
**jmacdonald** 16:01 Part 1 is you don't use the regex. Part two is you remember the last value.
**Yuanyuan Zhao** 16:06 Yeah.
**jmacdonald** 16:07 So that you can… Yeah. Okay.
**Yuanyuan Zhao** 16:09 The last value, cache was basically that, the API is in adjusted count.
which the get stochastic adjusted count, and, it allows the caller to pass in a cache.
But it provides a cache interface, so that the caller… and it is thread compatible, not thread-safe.
So, it's the caller's discretion of whether I just use a function local variable, right, outside of a loop, or that I use something else. That's how the interface… this is not the interface. I apologize, I should have got this sorted out.
Before, yeah, because all… the interface of, like, stochastic increment… actually, I changed that, because it deals with floating point. I changed it to, like, a stochastic division.
So it's a stochastic integer division.
it's like 5 divided by 3, you got sometimes 1, you got sometimes 2. It's done that way, so that we only deal with integers. That's also your… a bit of performance savings. But the bulk of the savings came from the regex, swap to the hand validation, the manual validation.
And also, the last value cache. The last value cache is at the outermost layer, and it's, I think that in the realistic case, we will get more amortization than the microbenchmark.
**jmacdonald** 17:47 Cool. I would say I'm not so concerned about the cache, maybe, because it might not work in practice, but I would like to see, like, the regex stuff is just… I agree. I originally wrote it without regex, and can't stop me, so, So, I would love to see that, and hopefully, you know, now that we've got this code stable, like, all we're doing is changing the implementation, and the tests will still pass, and… Yeah.
**Yuanyuan Zhao** 18:13 So my plan is that I will leave… I will first push the current state, which contains the comparison of the benchmark, and then we do a revision to just remove the old implementations, because I want to give you more context on the motivation behind those changes.
**jmacdonald** 18:34 I would recommend that instead of… well, instead of mutating, like, your PR in flight, what… it would probably be nice to just pull out the change of, like, regex to hand parsing as a pure, separate PR, which makes it really easy to review, and then get it merged, and so on.
**Yuanyuan Zhao** 18:52 I thought of that as well, and that's a good suggestion.
**jmacdonald** 18:57 Thank you.
So we'll look at your stochastic division after you push some stuff, maybe ping us in the Slack channel. I have, this leaves me with just one, I guess, recommendation. I think this was an open question, and I haven't… I haven't read this in a week or so, but, The… what I… what I was hoping to recommend, and I wanted to bounce this off everybody here, is… something about… I think estimation… And it comes down to the idea that, well, some of our spans come in with no trace state, some come in with a definite trace state, and when we do this approximate or stochastic counting.
there's sort of, like, different errors introduced in different places. If you're… if you have no trace state, you're counting one, like, that is an assumption, like, that's an assumed thing, and if you have a trace state, you're… you're making some stochastic randomization. There's no… there's an assumption there about, like, unbiasedness or whatever.
**Yuanyuan Zhao** 20:03 Yep.
**jmacdonald** 20:04 And in a stream of metrics coming from a stream of spans, you will have incremented the counter in both of those paths. So, some spans have no trace state, you'll increment one, and some spans have a definite trace state, and you'll increment some stochastic amount. The way I understand the OTEL metrics data model, it's built for this type of, attribute value subsetting. So you can say, I have a sum, it is the total span count estimate, and it's broken down two ways. There's the assumed counts plus the approximate counts, and that way they're separate, but because we've used a counter, and because OpenTelemetry's metric data model tells you, you can say, I've split my counter in two, I've got an attribute to distinguish the two halves, and I can then distinguish which counts were assumed one, and which counts were made from trace state values.
And then that would at least give us some… At least, maybe an ability to.
**Yuanyuan Zhao** 21:07 Yeah, I don't know. Yeah, I added, I added two attributes.
One is that it's extrapolated?
The other is the… that was actually from you, adding, like, a sampling method.
**jmacdonald** 21:20 Okay, that's exactly what I'm…
**Yuanyuan Zhao** 21:22 Right, right. I think that's a good idea. The, the thing to look at over there is that, since this thing is kind of, like, part of the UX, right, or API, I would say, right? Then, I mean.
by that, I mean exposed to, others, to customers, and so, we might want to think about the name, whether, what is there is appropriate, whether there are additional things that needs to be done, like, I don't know, I haven't looked at your semantic convention, you replied on that with… with a PR or something. I haven't looked at the PR, so.
**jmacdonald** 22:10 Well… Maybe don't, but that was an old piece of work. The reason that came up, just for context for everyone, is when we do… in the OTEL probabilistic Sampler Processor, sorry, the collector's probabilistic Sampler Processor, which is the one that I modified years ago based on that library that we just looked at.
it had a logs path already existing, and so I was sampling logs, and I had… and I had, like, all the concepts applied, but I had no place to put the trace state, so I made up semantic conventions and put in attribute values, and then I sent that PR saying, this is what I did, and it got kind of torn apart, and I said, okay, I won't do that.
**Yuanyuan Zhao** 22:51 Okay, I think I got you all the vice now.
**jmacdonald** 22:55 Yeah.
**Yuanyuan Zhao** 22:56 Okay.
**jmacdonald** 22:57 But otherwise, this sounds really good, and I'm glad to see it.
**Yuanyuan Zhao** 23:00 Yeah, I was sold.
**jmacdonald** 23:01 You're going to review.
**Yuanyuan Zhao** 23:03 Okay, so I will update… upload the latest PR, which serves as a draft, and then I will peel out, the, different parts into multiple PRs for, easy review.
**jmacdonald** 23:19 Great. That sounds excellent.
**Yuanyuan Zhao** 23:22 And next, I will look at the Go SDK. I briefly looked at it a bit, but I will look more. Yeah, I think that having this both pieced together, it allows us to make sure it's consistent.
**jmacdonald** 23:39 Yeah, I really should catch up with Rust. I, I… I should. I can.
Thank you. Well, folks, I think we can call it here. I'd be glad to… why don't you ping us when you have your stuff uploaded again? I'll review Peter's PR. Atmar, by the way, Peter has a PR, you can see the link, please.
you know, maybe you can prove it. Thank you all. And I'll see you in two weeks.
**Peter Findeisen** 24:06 Thank you. Bye.
**Otmar Ertl (Dynatrace)** 24:08 Bye.
**Yuanyuan Zhao** 24:08 I'll talk to you on Slack.
**jmacdonald** 24:10 Real quick.
