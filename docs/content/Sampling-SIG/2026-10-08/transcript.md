SIG: Sampling SIG
Date: 2026-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 02:25 Hello!
**Joshua MacDonald (Microsoft)** 02:59 Good morning.
Templars.
Can I hear you?
Maybe.
I don't know.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 03:11 Hello.
**Joshua MacDonald (Microsoft)** 03:12 Oh, yes, I hear you.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 03:15 Excellent.
**Joshua MacDonald (Microsoft)** 03:15 It sounds very low volume.
Good morning.
**Peter Findeisen** 03:22 Morning.
**Joshua MacDonald (Microsoft)** 03:24 We may have a we may have an agenda.
And remember… remember where we were the last time.
We were talking about… Sampling feedback and feedback loops and so on.
I also am aware that there's a message in our Slack So I… so I'm looking at our notes, and I have no agenda at the moment.
So think fast, everybody. I know that there was.
Of course, we never need to absolutely do this, but Mike has put… Mike and Chris have both put messages in our Slack, and I think now would be a great time to respond to them.
So, Gosh, I could almost, I could almost share that, couldn't I?
I'm now using Slack on my, On my work… on my… in the browser.
Okay.
Yeah.
How about that? Get that.
So, without an agenda, otherwise, I'm gonna start looking at what Mike said. I know he wants some approvals. This may not be a big deal.
Are you able to see… This screen right now?
**Peter Findeisen** 04:53 Yes.
**Joshua MacDonald (Microsoft)** 04:54 Can't tell. Okay, you're on it. Okay, so.
Mike is asking for, oh, man, fleet wide.
Fleet Tracker Extension, so it sounds like they're pushing the refinery design all the way in here.
Fleet Tracker… Redis Fleet Tracker, okay.
an extension.
Okay. Well, Okay.
I can sort of see what's happening here.
I'm just gonna, like, you know, since we're here… about Slack threads… So… What I'm seeing is a tail sampler extension for, contacting a Redis cluster.
I haven't read the depth here yet.
But, I can certainly review this for Mike. I… there's… I'm very easy to approve Sampling PRs. That's more of an infrastructure question and about Extensions, which is also an area that I know pretty well.
And that was an issue, not a pull request.
This is the pull request. Yes, here we go. So I'll be willing to approve this later today.
I don't know that we need to to go closely through it.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 06:28 Yeah, like I don't feel strongly about it. Like if it's helpful for people, great. Otherwise.
**Joshua MacDonald (Microsoft)** 06:32 I see. So all this is doing is saying…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 06:34 Like, we just refresh config to do this, like, we see autoscale, and we update the config everywhere to divide properly, and it's fine.
**Joshua MacDonald (Microsoft)** 06:44 Gotcha. So… This is more of a, like, responding to autoscaler events by writing your account into Redis.
Yeah.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 06:58 And we respond to auto-scaling of it, like, we see how many instances there are, and then we just update the config and restart the processor.
Okay. Well, really, it's just usually for tail sampling. I guess I don't know about adaptive goal one. For tail sampling, it's just restart the policies. Like there's already a hook to do that.
**Joshua MacDonald (Microsoft)** 07:17 Right.
Do you read new YAML files? Are you writing Kubernetes configs or CRDs or whatever?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 07:25 We… we have a little Go wrapper that embeds it. We don't actually spin up the collector as the collector binary, we… We import the code.
**Joshua MacDonald (Microsoft)** 07:36 Nice, okay.
Alright, well, And the only weirdness here for me is that we're using what it was designed as a storage extension for storing your data to store metadata, and that's… I guess that's okay. I don't see a problem.
This could be… This could be… more of a general service, I suppose. Or, as you say, you could… You know, monitor the auto scale, or something like that. Feedback on your metrics.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 08:12 Okay.
**Joshua MacDonald (Microsoft)** 08:14 I don't know, not too exciting. And then Chris, Not too exciting.
Okay, I'll read this stuff. I'll do… I'll do what my guest. No more actions required here.
And then… oh, sweet, this sounds good, this sounds interesting. You want to talk about it, Chris?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 08:32 Yeah. So I we talked about this a little bit last time. I went and into the Jaeger.
the Jaeger sampler, and put in Juan Juan's work, thank you! We can do the prob… we can use the probability sampler in here now for everything besides, like, the rate limiting, where this isn't supported.
For rate limiting, I have it just delete any threshold, which I believe is the correct thing to do, as that is no longer a valid number.
**Joshua MacDonald (Microsoft)** 09:05 Got it.
I want to use my, like, Zoom emoji reactions to, like, cheer here, except when I'm sharing, I guess I can't. Anyway.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 09:14 Yeah.
**Joshua MacDonald (Microsoft)** 09:15 So yeah, me, this is me clapping. Very well done.
Yeah.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 09:19 I looked internally, it's literally… this will work for every single internal service except one that we run with Jaeger. There's one service that uses rate limiting.
**Joshua MacDonald (Microsoft)** 09:30 And… and we should be able to do something about that. It just might require, like, going off… off book, or off the spec, or innovating a little bit, right?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 09:40 I think so. Like, this gets us…
**Joshua MacDonald (Microsoft)** 09:44 Peter has… I've written a spec on, like, the contract for adaptive sampling, and in this room, we have discussed the, you know, this… a number of approaches, all of which average out to some sort of adaptive, smooth rate.
I guess we would be pushing on Jaeger to do something about that, since it's literally their protocol and their struct.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 10:09 Yes, and my hope is, like, if this… which, this has one approved already, which is great, somebody approved it pretty quick.
Yeah, I'd like somebody from this group to just make sure I didn't mess up anything obvious.
**Joshua MacDonald (Microsoft)** 10:23 I will… I will… we'll do that, but I'll do it for real, so I won't do it in front of us here.
**Yuanyuan Zhao** 10:28 Yeah, I am also looking at it.
**Joshua MacDonald (Microsoft)** 10:31 Thank you.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 10:32 Thank you.
But yeah, otherwise, seems… yeah, like, I'm… I think this will work pretty well, especially for, yeah, us internally. We'll actually be able to use our… our metrics internally for the first time in years at this point.
**Joshua MacDonald (Microsoft)** 10:48 Awesome.
Very good.
So then, if we wanted to do that last case of yours, which has the rate limit.
I, aside from breaking the, like, Sort of contract, quote unquote.
I could imagine literally changing the implementation not to use a token bucket.
and to use adaptive probabilities and just wave our hands and say, this is no longer An absolute token bucket limit, the way you imagined it was, and now it's probabilistic, and might go over its rate slightly, and that's the nature of probability, or whatever.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 11:28 Yes.
And I think that would work, I've ran into Like, in practice.
that works okay, but, like, I've ran into issues where I've never managed to be able to, like, nicely tune a exponential weighted average, or, like, something to actually get a good probability out.
For, like, spiky workloads, like, we get a big spike of traces every… You know, 10 minutes or something.
But like every service is a little bit different on that and So I have struggled with actually using that approach in practice.
That's it.
**Joshua MacDonald (Microsoft)** 12:13 Adaptive, yeah.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 12:14 I would like to do some more exploration in that space.
**Joshua MacDonald (Microsoft)** 12:19 Cool.
That's great. Any commentary other than from me?
No requirements.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 12:33 Oh, I.
**Yuanyuan Zhao** 12:34 Yeah, I did.
you are talking.
**Joshua MacDonald (Microsoft)** 12:36 the.
**Yuanyuan Zhao** 12:37 This is PR, right? This one, right?
**Joshua MacDonald (Microsoft)** 12:39 Well, Chris's PR and or this topic of rate limiting, which is sort of the corner where Jaeger Remote refuses to be probabilistic.
Or, I'm saying we can bend them… bend it a little bit, and make it probabilistic. But, Sure.
**Yuanyuan Zhao** 12:57 So when we…
**Joshua MacDonald (Microsoft)** 12:58 the way.
**Yuanyuan Zhao** 12:59 Yeah, go ahead.
**Joshua MacDonald (Microsoft)** 13:01 Well, I was gonna say, the way I interpreted Chris's remark, it's like, adaptive sampling has, like, there's some neat math you can do to show that it averages out, and but users are so afraid of sampling, no matter what, and they're very touchy about Anything with sampling, honestly, and so.
What I hear… what I heard Chris say was, like.
the fear that adaptive Sampling is going to miss exactly what I want when I want it is.
Is there, and it has to do with, like, this… concern over, like.
rates that fluctuate, I guess. So, like, you were in a high rate period, and so you started dropping stuff, and then something slowed down, but you kept dropping stuff because you hadn't reacted fast enough, or, like, that type of concern, I think.
That was all I was gonna say.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 13:57 Yes, that, that, that is the concern and like.
You're always just a little bit behind.
**Joshua MacDonald (Microsoft)** 14:06 Yeah.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 14:08 And I was trying to figure out if you could somehow do, I don't know, some sort of callback, but, like, you've already made a bunch of traces that have this sampling decision, so… Or a bunch of spans that have the sampling decision.
Because, like, we can work around this in tail sampling by just having a bucket and then choosing in the bucket, but not so much for the SDK level.
I don't know.
**Joshua MacDonald (Microsoft)** 14:38 Well, I'm a believer in probability. I guess I.
It.
And in some ways, when I see types of problem, this type of problem mentioned from a user, or theoretically from a developer, I guess.
I'm inclined to kind of throw more… more averaging at it, you know, like, instead of having one adaptive sampler run once a minute, you know, like, give each… like, run two adaptive samplers and stagger them, and give each of them half the rate quota, and like… like, just begin averaging in other ways.
collect sample, different… collect different samples, and so on. That was… that's how I would approach that, and I am facing some little bit of a story, similar story right now internally, where We've proposed a fancy thing, and I've shared it here, like, just weighted sampling.
And it's like, well, that's… that's complicated. What if you just had a fixed number, like, per unit interval, and like, you know, what if you did something simple, like, just saved the first N per period, and then threw your hands up, and… I'm… I'm still struggling to give good answers to this sort of thing, like, I… like, I don't think users will be happy with that, because they can't count their… their… their… their events after that very well, or… Anyway, this is where… this is what I'm struggling with as well.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 15:57 Yeah.
**Otmar Ertl (Dynatrace)** 15:59 It's also a bias, right? If you just take the February minute, for example, then you have maybe some spans which occur exactly right after the full minute and you favor them.
**Joshua MacDonald (Microsoft)** 16:12 Yeah, that's exactly the type of response I want to give, but also it feels like I'm off in math territory when I do, and they're like, well, but this sounds complicated, and what if we just simplify it? So yes, that's it. It's bias and wanting to be able to count that I'm after, but I… it's hard to convince users, honestly.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 16:30 Yeah, I do think we could get pretty far with just having an option, and maybe, I don't know if it's a config option, or just something in Jaeger, or maybe it's just… this is where Jaeger lives, and there's a new way to… there's an op-amp way to configure all of this that just, from the get-go, goes, we're going to… this is a probabilistic target rate limit. It is very clear that it's not an exact rate limit. Whereas, yeah.
changing the semantics of that in Jaeger is going to be a harder sell, I think.
**Joshua MacDonald (Microsoft)** 17:05 Sure, yeah, Jaeger's… the way it is. Anyway, so last time we were speaking at the end of our meeting about a potential, and I'm still excited by this, so I thought I'd mention it, which is.
as you have this Jaeger remote capability, and now you can control your fleet of samplers in the SDKs, and as you have a tail sampler in your collector that's viewing a slice of your data.
the question, I feel like, keeps coming back, and this comes down to, like, I know a lot of users are happy with what Datadog does, and I, so the idea is that what if we had a way to tie our sampler to our to our SDK configuration.
So that we could… what? But, The idea that I thought was kind of appealing that we mentioned briefly last time is that there might be some sort of maybe abstraction where there's the notion that there's a sampling information provider, and there's a sampling information consumer, and the Jaeger remote will consume from any sampler that's running in the collector to get an idea of how to reconfigure itself.
This is just a big idea. I liked it, so I thought I'd mention it again. Mainly because I know users would be excited if we had a simple thing that's just like, this is gonna do your trace collection, and we can set a number.
And we will both.
Hit that number from the collector, and we will also lower cost as possible, as permitted.
by some math, essentially, by using Jaeger Remote and the feedback, and then choose your sampler. It should still work because of this abstraction. Now, that sounds complicated, but it's just an idea I like.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 18:51 Yes, so I'm happy to… so, my vision on this right now is it's effectively… I mean, what we're calling volumetrics, what Mike contributed, the Refinery, Adaptive Sampler is the name now.
I want to be able to effectively use the math that is used in those.
But.
At the SDK level. I want a component that re… that… It's ingesting all your traces, it has an idea of the distribution by service, by various other resource attributes.
That it can then go, I know I can configure.
Say, oh, you're this service, you have these resource attributes, I calculated that you need a 5% head sampling rate. This other, much slower, much less commonly called service, you can have 100%.
And that all averages out to be whatever your spend budget is, close enough.
**Joshua MacDonald (Microsoft)** 19:51 Right.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 19:51 That's my vision there,
**Joshua MacDonald (Microsoft)** 19:54 And so the natural challenge or question is how to implement that efficiently. And if it's possible to do abstractly, especially abstractly efficiently, that sounds pretty hard, actually.
But the… at least the hopeful vision I have is that when we do all this math correctly, and we have good adjusted counts on all the data coming out of the sampler, at some level, you can reduce it down to These are… this is the sample I'm seeing.
With its effective adjusted counts.
And if you just did some math on the output of the sampler.
Abstractly, even, it should be able to, like, count.
the data, and, like, do the math. That's…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 20:38 Yep.
**Joshua MacDonald (Microsoft)** 20:39 I'm still waving my hands.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 20:41 Yes, the interesting part to me is, what do we do for users that, like, like, I don't know.
What I think of, like, what users set up is they set up maybe, like, a set of tail sampling policies or something like that. I want to keep high latency, I want to keep, errors.
How do we calculate head sampling rates given those policies is something that I think is interesting as well. The user experience I'm thinking about is like.
I come in and I say, for my service, I want to Capture… requests that are slower than 3 seconds.
And I want to capture.
Things that are errors and, like, some percentage of the rest, like, that's kind of what I very commonly see both for myself and other people at my company.
How do you turn that into probabilistic?
Sampling rates is an interesting problem in my mind.
**Yuanyuan Zhao** 21:42 could have something that's composite, right? That's like rule based.
So if it matches an error, you apply this, this, Sampling Rate. If it matches, does not match an error, it's like okay status, then you apply another one and.
As long as the decision in the two stages are orthogonal, then you would be able to just attach the… The corresponding TH, and that would, I think, would be fine.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 22:17 At SDK Sampling Time, we don't know about errors or how slow it is.
**Yuanyuan Zhao** 22:22 The error thing typically are done in tail samplers.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 22:27 Exactly. So we need a… so what we need is a rate that works for head, like.
We need a high enough rate of traffic that tail sampling will be effective.
But you're not going to blow your budget.
By egressing all of these traces to some other availability zone, or something like that.
**Yuanyuan Zhao** 22:47 Right. So.
**Joshua MacDonald (Microsoft)** 22:48 That's way.
**Yuanyuan Zhao** 22:49 You apply in stages, right? That's the two stages of the pipeline.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 22:55 Yep, so then you have multi-stage, which works now with… Like, I think the PR I have will make this actually possible in current implementations because we should be able to actually control Jaeger sampling rates now and have that feedback loop.
But yes, where do we…
**Joshua MacDonald (Microsoft)** 23:12 to this… Set up that you are interested in that whole… so, ignoring the latency and the errors.
you have a flat sample of everything, that was your small percentage. I would use the small percentage of everything As a first order to set my feedback.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 23:34 Yep.
**Joshua MacDonald (Microsoft)** 23:35 my SDK sampler rates, and then I feel like I've… touched on this a little bit like, if you have a sense that one particular span is creating a bunch of errors.
you could see that from your two samples, or you could see that all the… like, you could use an inference about one of your samples to, like. probe what you're trying to find. Like, I think this span is producing all my errors, so I'm going to raise its sampling probability to find more of them.
That's where it becomes, like, very open-ended, and I don't know… Yeah.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 24:07 A bunch of errors is actually not what I'm worried about, because, like, a bunch of errors, you'll get some examples through, that's fine.
It's the, this thing doesn't produce that many errors.
And therefore you might have an incident and you just never sample them because you just don't know.
**Yuanyuan Zhao** 24:25 so.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 24:25 about.
**Yuanyuan Zhao** 24:26 In SDK, then, you will have to apply a higher rate, right? And and then… in the tail Sampler.
You control exactly how much egress.
From yours.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 24:41 So how do we get the math on that to work out is my current question, I'm thinking of trying to, like, kind of base it in, like, SLO world like, if you're trying to defend a 99.5% SLO.
you want to have, say, 3 examples of traces that would fail that SLO in some time period.
Is my current mental model. And then you can do some math based on that to figure out what a head sampling rate should be for how busy your service is.
Okay.
**Joshua MacDonald (Microsoft)** 25:19 Right, there's a risk tolerance that says, like, I'm gonna set some sampling, hopefully I don't go over my budget, and there's a risk equation there.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 25:28 Yeah.
**Peter Findeisen** 25:32 Yes, I think we should realize that there is a separation of concerns between the head sampling and tail sampling. So, with head sampling, the concern is about budget, and only the budget.
With tail sampling, you want to choose what interests you, so errors, high latency, and so on.
So… you don't need, really, this feedback loop. I… in my mind, I… it… It's not appropriate. It is… If you… if you feel unhappy with what you are getting as input for your tail sampling, you have to increase your budget. That's it. You have to pay for it. You have to increase the volume of spans and traces.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 26:25 Yes, like generally yes, but I wouldn't say it's entirely, it is a trade-off between budget and information.
**Yuanyuan Zhao** 26:35 And also, the budget is not just a thing. It's not just a concern of the SDK head sampler, right?
You, you pay for the thing that got out of SDK but you also pay, for network egress that's eventually going out of the tail sampler.
So there's budget… budgeting over there as well.
Or maybe you mean something else, Peter?
**Peter Findeisen** 27:06 Well, by budget, I mean not only the financial aspect of it in terms of dollars, it's also technological constraints, right? So if you… If your network is simply getting saturated with too many spans, even if you don't pay for it, it's something that you cannot afford. That's… What I meant.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 27:30 The other thing I see commonly, I guess it's more among customers than internally, but it's… these are two different groups of people. There is a group of people who care about The dollars that tracing costs in there is the group of people running their service.
That wants to be able to debug their service, and… There's a natural friction between those two groups, especially for tracing.
I.
**Joshua MacDonald (Microsoft)** 27:58 I have an observation on top of this. So, even if you have a budget, what we know, I think, is that it's pretty simple to set up flat sampling. Like, I will sample every span at 5%.
And then what you're seeing at the tail sampler is 5% of these dumb spans that do nothing, and 5% of the interesting spans, which are not quite enough information. So, like, and I've been describing this, like, log… pure log sampling thing that I'm doing.
Because most… many of our users just don't have tracing yet, and, which is not great, but.
you can imagine that, like, I have one sample of all my logs coming in, and I see this event, and, like, I know there is a log event. It is an error, or whatever is happening.
But I keep not getting a span for it.
Because it keeps happening in an unsampled context.
Now, if I had a way, and this is hard.
to, like, know Which context would… should be sampled when I see that log. So if I knew the, like, the name of the root span that was missing.
or the category of span, or whatever query I would need to boost to find this span whenever I see that log.
Then I could do some sort of, like, compute, like, math, not gonna try and do it here, but to say that I want to boost the one span that is likely to give me the thing I'm trying to find, so that I turn the other spans that are not very interesting down, and I turn the one span that might produce my errors up. I think that's… also what people are imagining, but that's not what Datadog's doing. Datadog's just trying to kind of, like, balance all the spans, I think, so they come out equal, which is one of my favorite approaches.
**Yuanyuan Zhao** 29:50 But depends on which one you are talking about. The one that you are just talking about is probably what I did.
The adaptive sampling, right? They're sampled by what we call the resource names.
That it it's but so it's while we use it it.
interchangeably with, like, the endpoints, which is basically the, resource name, or… that's not open source equivalent, but think of something like a spend name, something like that. The sampling rules are keyed off.
those kind of endpoints, and then the sampling rate are modulated, between them. It tries to, do it proportionally, but with a floor and a cap.
**Joshua MacDonald (Microsoft)** 30:44 Okay.
That sounds… that sounds appropriate.
Just to say that you're adjusting spans, but it's a little bit more than just something simple. It's like. We, you know, we want more of these, but not too many of these across.
A few dimensions, both the producer and the resource name, I guess.
**Yuanyuan Zhao** 31:08 Yeah.
**Joshua MacDonald (Microsoft)** 31:11 Okay.
**Yuanyuan Zhao** 31:13 If we still have a few minutes, I would like to, discuss a technical point, related to Chris's PR. Okay. I… I just glanced it, so, like, 5 minutes.
Let me know if I'm off track. From your description, it sounds like if there's rate limiting, the TH is erased.
So, when is rate limiting applied? Is it like for, that, when there are a lot of When we already sampled enough spans, then we just cut off all the sampling for the rest of… on spends in the current time bucket? Is that.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 32:08 We… we were… if… if a span matches, like, if it… if the decision is made based on a threshold.
Or based on a rate-limiting policy, we strip the threshold, no matter what, because otherwise you would be multiplying by 20, 20, 20, 20, 20, and then suddenly we strip it out once we hit the rate limit, and you would have very odd metrics at that point.
So I think we have to always strip it out just to say we don't know what this was.
**Peter Findeisen** 32:41 That's right.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 32:42 Cool.
**Yuanyuan Zhao** 32:43 So.
**Joshua MacDonald (Microsoft)** 32:43 Sounds better.
**Yuanyuan Zhao** 32:44 So if we want to have 10 spans as the maximum.
What?
The 10 samples are the maximum and we sampling by 10%. Usually there's like when there are 100 of them coming in within the unit of time.
We would, perfectly, use up the budget of 10.
I… so it's basically that there's a budget within the unit of time, and if there are suddenly a spike of 200 coming in, then within that unit of time, we would get 11, 12, up to, 20 that could potentially be, sampled. And, we then… Oh!
When we see… when we already sampled 10 within that time, then for whatever that comes in. We dis… we throw them out.
And.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 34:05 Yeah, that's how Jaeger rate limiting works, yeah.
**Yuanyuan Zhao** 34:08 So.
So then, The count, right? Oh.
Downstream. So we already send, out the 10 Sampled Spans.
Right? And we throw out, another 10, which the 10 sample spans actually had an adjusted count of 10.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 34:33 Well, we would, that's why we stripped the threshold, right? So we stripped the threshold off, so there's just, yeah, no adjusted count.
**Yuanyuan Zhao** 34:40 Oh, this is in tail sampler. So we buffer the 10 for the unit of time. Is that?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 34:46 Hmm.
**Yuanyuan Zhao** 34:47 So, okay, because if we already send out a 10, there's no way we can… okay, that's…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 34:53 Yes.
**Yuanyuan Zhao** 34:53 So we basically, within the unit of time, we buffer everything, and if rate limiting was ever triggered within that unit of time, then we strip out the TH for everything, and then still sent the 10 sampled, span out. We still export it out of the tail sampler, but they no longer have the TH value.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 35:22 Yeah, I think in tail Sampling we actually.
Keep it now, because we know… we buffer it for the amount of time We buffer everything and if the rate limits hit, we can calculate, we can just move the threshold.
To how many traces were hit.
**Yuanyuan Zhao** 35:39 Oh, so you I mean we adjusted it.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 35:41 Yeah, we in the tail sampler we adjust it, but that is but we can't do that here. Because we just we don't have any sort of actual like we can't just go, I know of every trace that happened in this one second. We just don't have that info.
**Joshua MacDonald (Microsoft)** 35:58 So you're… I've… Okay, I followed this. I felt like we crossed topics, though. It was. It was.
The spans or traces which get rate limited by Jaeger.
When rate limiting happens, you erase their threshold, but there's also this mechanism where you… where when the number of traces is over your budget, you start dropping them and changing the threshold.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 36:27 Yeah, so those are… that was in tail sampling. So yeah, there's two different things. So in Jaeger.
If there's rate, if there is a rate limiting policy, we strip the threshold for every single.
Span that matches that policy, because we don't know… we don't know if rate limiting will be hit or not.
**Yuanyuan Zhao** 36:47 Oh, okay.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 36:48 In any given bucket, in any given period of time, we just… when we make that decision, we don't know.
**Joshua MacDonald (Microsoft)** 36:53 Right, right, right, right. No, we can't.
**Yuanyuan Zhao** 36:54 think.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 36:55 to strip it.
**Yuanyuan Zhao** 36:56 Yeah, so we scripted regardless, right? Anything that would match a, if you have like a rule base, then, then there's a rate limiting on that rule base. Anything matches that. Yeah. That, then that would work. Otherwise, I think it won't. Okay. Yeah.
**Joshua MacDonald (Microsoft)** 37:11 And then… At the tail sampler, you just do whatever you're doing, and if you have spans that have no threshold, they're just part of that trace, we still don't know anything about them, but the trace has a threshold.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 37:23 Yes.
**Joshua MacDonald (Microsoft)** 37:25 Okay.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 37:26 typically.
**Joshua MacDonald (Microsoft)** 37:26 I think this is okay, this is good. I think it's okay.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 37:30 Okay, I think it works. Like, it won't be perfect.
But you can at least know that, oh, this doesn't have a threshold. There will be randomness as well now, so, like, other policies will work correctly.
But yeah, we strip the threshold out for anything that gets, that might be rate touched by a rate limiter.
**Joshua MacDonald (Microsoft)** 37:53 Okay, well… It sounds like we're putting this into production, and we're gonna know a lot more.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 38:00 Excellent.
**Yuanyuan Zhao** 38:02 But, what would be the rule look like?
Would that be, like… so, if we are calculating accounts on some spam names.
The rule has to cover the whole span names, otherwise, right, the… If the rule always applies to… A subset of the, of the spans under that name, then we would, we would actually.
Count things wrong.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 38:34 Yeah, and that'll end up depending on how Jaeger's configured. Like, most people run Jaeger with, like, parent-based… or do something.
At which point, it'll just take a parent… it'll just take the parent decision, and then you would just keep the same threshold all the way through, because we're not changing a decision.
If it's parent-based, so… Some people do configure it where, like, nope, we don't do parent-based, this service just has this rule, and then you might have different thresholds throughout that same trace, and you just Have to do the math on each span.
**Joshua MacDonald (Microsoft)** 39:15 This is progress.
**Yuanyuan Zhao** 39:19 It is progress as we are touching some concrete problems. I'm not sure that it would work in the general case because it heavily depends.
On the condition that would lead to the rate-based, rate-limited sampler, right? If we're doing counts under certain span names, but if they… the… The rate limiter will have to cover that whole span. Otherwise, the whole, right, every span of that name.
Otherwise… Then you have… A undercount of.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 40:06 Yes, if something is being sampled by a rate limiter right now, you will undercount your metrics. Like, that's just… That's just the trade-off people are gonna have to make for using a non-probabilistic rate limiter.
**Joshua MacDonald (Microsoft)** 40:19 We can improve, I think, the counters to say, I saw a span with no threshold. I am ambiguous at this point, right?
Can't remember exactly what we did in the span to metrics counter, but we're making progress. That's the summary.
**Yuanyuan Zhao** 40:35 Yeah, in the span connector, if we don't have any TH, we count it as one. And we also attach a attribute.
That says it's counted instead of extrapolated.
**Joshua MacDonald (Microsoft)** 40:57 Okay.
So that would be the signal that someone's got…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 41:01 This is happening.
**Joshua MacDonald (Microsoft)** 41:02 Yep.
All right.
Okay. Very good.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 41:10 Moves it in the right direction. But yes, I agree, rate limiters will be undercounted. Yes.
**Joshua MacDonald (Microsoft)** 41:17 As we gain more experience, we'll know if this matters. There will be growing pains. I'm happy with this, Chris. And thank you, Yuanyuan. And thank you, Peter and Otmar.
I think we've reached the end.
And I really appreciate it. So we'll see you again hopefully in two weeks.
**Yuanyuan Zhao** 41:33 See you next time.
**Otmar Ertl (Dynatrace)** 41:34 know.
**Peter Findeisen** 41:35 Bye.
**Joshua MacDonald (Microsoft)** 41:36 Progress.
