SIG: Sampling SIG
Date: 2025-09-25
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/gXZs_0-67T34p0QRqcTKwGT8TfEGxn7N2iUIeZDfB53yXnMy6XLwXOsKFTU1Xgsb.3EHAlQPJi37QXbFm
============================================================

## Zoom Recording Transcript

**jmacdonald** 01:59 Good morning.
Hello. I'm gonna pull up the notes. I see two familiar faces, and, I'd like to introduce Elf. You, spoke at the Collector's SIG yesterday. Thank you for joining us today. I'm gonna pull up the meeting notes. Maybe I'll let you introduce yourself while I do.
**Alf Kenny** 02:17 Sure. I am a,
a big fan of the Hilltop Collector. I've been working with, specifically with the tail sampling processor quite a bit to achieve some of the goals that I have in my team for tracing.
One of the things I've been working on recently is to use the tail sampling processor and a few other components within the hotel collector to
minimize the number of traces, of useless traces going into our system. We have, I'm sure we, as a lot of teams do, a lot of… a lot of spans and traces that are being sent in that are never, ever intended to be queried, because they're kind of worthless.
And we're trying to build a solution that would allow us to
Focus specifically on traces that people have a high probability of actually needing to access.
And so, the thing I'm going to be bringing up in this meeting here is, one very… what I believe to be a simple tool that would help us to achieve our goal that doesn't seem to be in place currently. It's a policy.
**jmacdonald** 03:19 Yeah, thank you. So, we've had a couple more… oh, we had one more join us. I'm just gonna, take it from there, since… since you introduced yourself, and I want to describe… I'd like to pull up the PR that you showed us. I think you showed us the PR, and put it in the notes. But while you're doing, I'll say this much.
Two issues came up this week, both of them about collector sampler processors, so it's good that we're talking about this here. I really wanted to call out something very exciting about what you shared yesterday.
I don't believe anyone has ever, in earnest, tried to do a sample, sampling configuration that selects for incomplete traces. And you talked about why you wanted this NOT rule in your configuration, and it being a way to identify traces that didn't have a root.
I thought that was pretty fascinating, since no one's done this type of thing in OpenTelemetry, so I wanted to congratulate you on tackling something there.
So… so then, we are in… now, the group here knows more… a lot… quite a bit about the tail sampling processor,
So… So what I… what I… what I've said in this meeting in the past is.
is that we've talked to Sean Porter.
The group here has worked out a specification for open telemetry signaling trace thresholds, or sampling probabilities.
Combined with, an apparatus based on W3C for conveying that in the trace and so on. So that gives us this sort of, like, ability to have coordinated sampling policies and to count them at the end by knowing the probability. So then.
once we had finished that, kind of, we have… we have pending SDK specification work that's in the experimental phase. We're working on SDK support so that you can get samplers to send how much thresholds they've been… what their threshold is, so that we can count the spans and so on, plus combine them in pipelines that continue sampling and so on.
So that's, where we are with the SDK. And so as that was kind of reaching a stability point, I started looking at the collector processors. And there are two. One's called probabilistic Sampling Processor.
And I have a note on that topic, but the one that you've been looking at, tail sampling processor, is, I think, where most of the user's interests lie.
And we went in there looking…
at it, with the question in mind that I just described. How could we add the support for these specifications where we're counting spans by using a field in the trace state called threshold and randomness?
And what I found was, like, a little bit of a spaghetti, plate. The code, the way it stands, is a bit hard to follow, and it, has that feature gate that you noticed.
feature gate to remove, some inverted match logic, which has to do with not, as you noticed.
But the logic is quite convoluted, and every time I sort of step back to try and explain, say, to this group, here's a summary of how this priority evaluation works. They're looking at
The point is, there's some question in my mind that I think is legitimate here, which is how do we get from the…
Simple work we've done. Peter led this work on sampling configuration, where you have rule-based configurations. You can say, I want to do a rule based on some attributes or whatever, and you can combine them into a composite sampler. How do we do that in the tail sampling processor?
you get in there, and you see that it has its own notion of precedence and some, like, evaluation order stuff, and what I really want to do is take the decision, which is yes or no in that code, and turn it into a
threshold base, where you say, I want to sample this 80% of the time, or I want to sample this 20% of the time, instead of saying yes or no.
The size of the change to do that much
was starting to look enormous. That's kind of why we sort of stopped.
when I have talked with Sean about that code, it was also… there's an interest… I have an interest in reservoir sampling, and I've spoken with this group about some of the technicals there.
We think it would be nice if you could get to a place where
The amount of memory is fixed, and samples go in, and…
samples with thresholds come out, but we're not quite there yet. So, that was mostly just background to introduce you to that we know about this situation. I'm excited by what you're doing.
And I'd like to just help… if you think the change you have is solid.
and viable, I'll approve it. I'll review it and approve it.
If you tell me this code's starting to fall apart.
I'm thinking about starting from scratch. That's what we keep hearing.
So, I don't mean it to be a negative on that code.
But that's what we've…
**Kent Quirk (he/him)** 08:24 Can I… can I just ask, I came in just late enough that I've missed some… what I think must be important context.
**jmacdonald** 08:31 Yes, please.
**Kent Quirk (he/him)** 08:32 what started this conversation? .
**jmacdonald** 08:34 I'll introduce it very briefly, and then pass it back to both of you. So, Alf joined the collector SIG yesterday, introduced himself, and said he had done some development on the tail sampling processor.
Because in earnest, needed to be able to sample out traces that had no root span. And there was no way to write a sampling configuration that says.
Do not sample traces without a root.
As far as I can tell. And…
when you get into that code, I know you've looked at it as well, Kent, like, it's a little bit hard to wrap your head around the evaluation order stuff, as well as the, like, mixture of old feature flag code for something called inverted match, and…
**Kent Quirk (he/him)** 09:17 Yeah, as you noted, the binary… the binary nature of the composition basically makes a lot of that stuff really difficult.
**jmacdonald** 09:25 Yep.
So that was… that was where we were. Me saying that maybe the tail sampling processor is ready for a start-from-scratch effort. Not… not to say that I want to throw away its configuration, that's interesting to me, but, you know, maybe we could re-implement it
In a new codebase, is sort of what we've talked about.
So, Al, back to you. You've learned a lot about this,
I mean, Kent, unless you have more questions, I'm passing it to either of you.
**Kent Quirk (he/him)** 09:53 No, so you're saying that,
Alf, you've… you've submitted a PR or something to the collector?
**Alf Kenny** 09:59 Well, I didn't want to get too far ahead of myself, but I just… I made an issue that described what I was trying to do, what the alternatives I attempted were, and why they didn't hold water in this case.
And so, just as a brief, just…
summary of what I'm trying to do. We've got… in our… in my company, we've got, you know, some teams that are sending hundreds of thousands of spans per second.
And we did the math on it, and they're querying maybe…
0.0001% of those… of those spans that are being generated. And the issue is because most of them are business as usual, most of them have no problem whatsoever, but people still want things like metrics, the span metrics associated with them. And so we figured, okay, maybe we can do some… some…
Put a sidecar, an auto-collector sidecar, next to an application, and then have those applications send their telemetry through that sidecar.
And the hotel collector could do the work of saying, like, alright, this is not worth sampling, this is worth sampling, and even the stuff that's not worth sampling, we're going to use the spam metrics connector and the service graph connector to generate some metrics for those things regardless, so that people can still do some sort of A-B testing if need be later on.
But in our case, one of the major things was that in our… in the company, we do have a lot of services that are connected to one another.
And because of that, they're generating distributed traces. So, we could have a situation where, locally, the trace that's being generated by an application doesn't seem to have anything interesting in it, but taking on aggregate the multiple, sort of, like.
pieces of this distributed trace that are being generated together might have something interesting that should be sampled down the line. So we kind of wanted to have a multi-level sampling scheme, where locally, there'd be some checks to see, is this a monolithic trace that only exists, that sort of seems to start and end within this application, or is this potentially a section of a distributed trace? And to do that, we have to have one check, at least, that says, is there a root span? Is there a span
Is there any span within this trace that's been generated that has a nil parent ID, signifying that it at least started it here?
And we have… I tried to look at some ways of doing this, potentially working with drop, and always sample afterwards, but the issue there was, as you look at the code, drop takes precedence over everything, so if you get one drop, then any other sampling decision is completely ignored in the process. And that doesn't work in our case, because we want to do things like, say, hey, is there a root span? Or…
Potentially. Is there some communication happening with one of these bands with a different service within our infrastructure somewhere?
So we need to have the combination of two things.
And so, I built, like… initially, just as a perp… just, like, as a test, a proof of concept, I just made, like, a root span, policy, just to check for that. And that works, that gets the job done, but in looking into it, I feel like what would be a more… a broader approach that would allow for a lot more… there's better decisions to be made across all policies, is the ability to say, hey.
Look for something that matches this condition.
And then put a knot on top of that. So we could say something like, look for something with a root span, and then just put a knot on top of that to say, like, oh, there is no root span, or there is a root span based off of this.
Because, like, the OTTL policy, I find very useful. I've, I haven't really seen what the performance is like on that, but regardless, if it's just sitting on an application, it's not going to be too bad. But… but that seems to be doing, like, basically everything we need, aside from this idea of just, like, hey, can I just, like, tweak this to say not this… this condition?
**Kent Quirk (he/him)** 13:32 Okay.
**jmacdonald** 13:33 This makes sense to me. I, I… I had… when I…
when I sort of studied that feature flag and the addition of a drop policy.
I was trying to understand the conceptual requirement, and I… it's a little… a little hazy at this point.
why did we need to add a drop policy? Why… and there's this notion of a, like, a no-decision policy, where you basically say, I don't have any claim on this sampling decision, which is a, like, a pass, essentially.
And this evaluation ordering is to address the fact that some things say pass, some things say drop, and some things say yes or no.
And we want… And…
So I think the open question that maybe you've addressed, and I need to think about it a little more, is does the NOT policy take away the need to have evaluation ordering? Because evaluation ordering keeps confusing us.
It's… it's like, why this tail sampling doesn't neatly fit into our model from the OTEP
About, say, rule-based sampling.
that is my feeling and my takeaway from the conversation about not. It sounds like the right decision
It'd be great if we could stop having this… this sort of, like, funny algorithm that doesn't quite fit.
The straightforward notion of… You either have a sampling decision or not.
You know, it's… the way we'd like to do is turn every one of these yes-no decisions into a zero to one, like, threshold, and then drops should be close to zero, and…
Inverting should be subtracting from the max value, so we should be able to do all those things without precedence, I think, but now I haven't… that's as far as I've gotten into that idea.
I don't know if that's a helpful way to respond, because as I said, there has been some resistance to mucking around in this code. I know that it's been forked by one group at Elasticsearch, I think? No.
Atlassian has forked this module, and they're using it, and they have enough changes that it's already just two codebases. Sean Porter.
has an interest in some feature work that I haven't seen yet. So there's, like, there's more than one piece of person working in this code, and it's already become quite complex. That's all I have.
On tail sampling. I should say, actually, that's not all I have. Last week, I spent an entire week on a hackathon, and I did try to work on tail sampling.
I, have not… I've not prepared to share a report. It's too messy. And I was working in Rust, so it won't benefit a collector in Go right away.
that said, the reason why I started from
from zero on a new sampler was because, as what I said, is I don't think we should try and
Too hard to… to salvage this tail sampler.
That said.
again, we have people filing questions and asking issues, or filing issues and asking questions here. I just noticed this one, aligned decisioning with probabilistic policy.
with a probabilistic sampling processor. So I mentioned one more issue, I haven't even put it up yet, but it's a user who's been using a two-stage probabilistic sampling processor, meaning two collectors. So they've got apps sending to an agent, sending to a gateway, sending… and they're two sampling stages.
And what the user has finally noticed is I put in a, an obstacle.
I… I guess I'll admit I did it on purpose. So, the probabilistic sample processor has modes now.
The legacy mode's called Hash Seed.
And if you have hash seed, it will construct a randomness value, and translate the hash value into that randomness value, and output a threshold.
that's this compatibility, this, like, backwards method for upgrading all of our legacy samplers onto the OTEL mechanism. So this legacy logic produces a randomness value and a threshold, and that's its decision.
The second stage sees that. It's also configured with HashSeed, and the way HashSeed was supposed to work is you'd configure a different HashSeed on the second stage, therefore it's not… it's independent.
And it would just work.
And the goal, when I upgraded the probabilistic sampler processor over a year ago, was that we would properly support OTEL sampling. So, when HashSeed sees randomness, it says, I don't want to do this sampling decision. I'm in a mode already where we're using OTEL sampling.
So the second stage sample rejects it, saying, I tried to… I'm in hash seed mode, and I see a randomness value. I don't want to sample this. That's me being a little stubborn to try and push users into the OTEL sampling, and it just worked.
Of course, they filed a bug report instead of doing the thing I wanted them to do, so I've now been helping the user. I have an issue. The point is, these two issues are saying the same thing.
we want to make sure people understand how to use the probabilistic sample with the hotel sampling for weight first for sampling threshold, and then we want the tail sampling processor to use that number as its weight when it's deciding what to sample. And again.
That's what it means to me to upgrade the tail sampling processor with support for that.
sampling threshold logic. It means that you're using a weighted sampling algorithm. It means that you are choosing things that have been
More sampled ahead of you.
less… with a different probability than you're choosing things that haven't been sampled, for example. All those things are things that we talk about in this room and we know how to do. We've talked about papers for adaptive threshold sampling that can be applied there, but it's so far out that… can't really imagine it yet.
And that's what we have.
**Kent Quirk (he/him)** 19:16 I gotta tell you, what I'm hearing here, what I think.
**jmacdonald** 19:19 Shit.
**Kent Quirk (he/him)** 19:20 be done, is… we should…
I think, declare the current tail sampling processor deprecated, and write a new one which is threshold-based.
And I don't care very much if the configuration language is identical or not. Like, we could decide either way to do it on that, but I… I don't think…
I think we've been… we've literally been talking about this for, like, 3 years.
And… and I think we've waited too long. I think it's time to just declare that we've…
not had a victory on this, that the architecture of that existing sampler is fundamentally broken. You can keep using it if you're into it, we're not going to take it away, but we're gonna have a new tail sampling processor, and this is the way you should do it going forward.
**jmacdonald** 20:13 Yeah, that's easy to say, except no one's here is volunteering to, like, prioritize… To write it, yeah. Of course.
I keep threatening to, and I've fiddled around with it, so I spent at least a week digging into that code. I spent at least a week on a hackathon project for something new. As you all know, I've said… you don't all know this, I have been working with the hotel collector group as well on
trying to look at their rate limiting question. How do you rate limit on this, like, thing that has all these circuits passing through it? There is a model for that. Envoy has a good model for that. But if you start looking too closely at both of these models, the Envoy model for rate limiting, and the tail sampling configuration model for rate limiting.
You end up with these two really different models in your head, and that also bothers me a bit.
Which is to say, my… I have an open question about whether the configuration model is ideal, but I'm not going to say it's bad.
When… when I, when I look at the, the rate-limiting
configuration model for Envoy, you see people doing almost all the same things that you ask for to do with sampling. So, I want to say, if an attribute value matches priority user, then give them this sampling bucket configuration. Like, more samples for high priority user. If it doesn't match this, then go to a different bucket. That type of configuration is not yet integrated with a tail sampling processor.
So it's gonna keep getting more complicated if we don't start over again.
And if we're going to start over again, you might want to think about those other models. That's… that's what I'm… what I'm… that's sort of a wishful thinking statement.
**Alf Kenny** 21:51 I'm kind of new to looking at the other aspects of the… of the…
the OpenTelemetry collector, but is that… is there not, like, the routing table you can provide to the routing connector? Would that not allow you to have some sort of bucketing, or…
**jmacdonald** 22:04 For my…
That… that's a, interesting idea. I… yes, there's many overlapping functionalities in the collector.
And, so… if you have completely independent samplers, like, I have,
a high priority sampler and a low priority sampler, and I have a routing processor, I can say, high priority user goes to this sampler. Then you've taken the configuration that Envoy would bake into its rate-limiting configuration, you've moved it into another processor. I'm not saying that's wrong, it's just sort of like.
There's more than one ways to solve… solve here.
And… and… and I don't want to push us too far towards the dream here, but there… sometimes people come up with policies that are kind of like.
I'm… I'm not sure.
how much space I have. I wanna, like.
I want to add one sampler, and I want to say, you know, like, be unequal, like, recognize what's rare, and be adaptive. You know, like, I want one pool of memory, and I want to dynamically respond to what's there, rather than having this static configuration, which is, again, going to be…
You know, static.
So, we talk about… in the tail sampling policy, Alf, you've probably seen there's one called composite. It… the naming is confusing, because we have a composite in our spec for this SDK now as well, but the composite in the tail sampling processor is really a…
Like a weighted… a weighted selector, where you're saying.
10% of my weight should go to this category, and 25% to that category, and the remaining 30… 65% or whatever to the other category. That's, in the sampling policy, and that's when it gets quite tricky to talk about, and that's when you ask the guys in this room, hey, how do we do adaptive threshold sampling? And you read the paper, and, you know, that's the kind of thing that we could…
we can get to.
So… but I think I asked Sean the same question, and very few users of the tail sampling policy… tail sampling processor seem to understand that composite policy. It's not being used widely, as far as we know.
**Alf Kenny** 24:17 Yeah, I've given it a shot, and I did end up getting a bit confused by a few things. It took me a couple days to fully understand what I was doing.
**jmacdonald** 24:25 Yeah, I think, again, that's one… all of us who have looked at that end up feeling a little bit uneasy about keeping it or continuing it, unfortunately.
in my… my wish list, if I can do it myself, when I… and I did on a hackathon last week, what I always…
kind of start with… my starting point is always, like, you have a fixed amount of space, and you… and you just want one example of everything. That's my only param… my no configuration other than, like, try and get something of everything.
And… and the rough… the rough sort of setup is, like, look at what you just got in your previous window, invert all those probabilities, use those as weights, do your weighted sampling.
divide by your weights, those are your estimated frequencies. That's the rough idea there, but, like, that's, again, like, so far in the future that I… I like to think about it, but…
Well, we've been talking, and I just… I think we've kind of come around on the tail sampling processor. If you're… I think I got the issue linked right, Alf. If you try to make a small PR, and it's, like, good enough for you, and it makes sense, and it looks clean, I will approve it.
I'll tell Sean I'm doing that. I don't actually… I'm not listed as an owner yet, but I'm trying to get there.
And I think Sean will agree if it's, like, not making a big mess.
**Alf Kenny** 25:41 Sure.
**jmacdonald** 25:43 And if you find otherwise, you know, you're welcome to come back, and, you know, I at least will continue talking about this, idea of rebuilding it, and I keep trying to find some time to…
To break ground on that as well.
**Alf Kenny** 25:57 Okay, yep, I'll make a… I'll make a ticket with my team to… to build some… to put that together, and then I'll submit that to you.
**jmacdonald** 26:05 I just described my dream sampling algorithm, this issue here, a new policy to capture low-frequency attributes. That's about the same idea, maybe. I think samplers should be good at selecting things that have been… are rare.
I haven't… I haven't opened this one carefully.
We covered this one. The fact is that the tail sampling processor has no awareness of OTEP 235 or thresholds, and that's what this is asking for. That's what I want, but that's what looks really hard to do in that code.
The last issue I have, I mentioned it, I haven't put the links in, but we're kind of done talking about it. The idea that, if you set two hash seed probabilistic samplers in a row, it will complain, and I did that on purpose, and we could make a flag to work around it, but I would rather them just upgrade to using the OTEL modes. So.
So, where was that issue?
I don't think anyone here cares about this, so I will… I will, here it is.
I will leave it here. Anyone else have a topic for this agenda?
Here is the new issue.
Sorry, I didn't get that copied right.
I've already responded. The point here is, if you have two collector pipelines, you set them both with hash seed. HashSeed 2 and hash seed3. If you set the same hash seed, you don't have independent sampling, it's doing the wrong thing. That's sort of a gotcha.
We, a year ago, replaced… added a new mode called Equalizing and proportional. They do the right things, and then what the user wanted was 50% in their first layer and 10% in their second layer, and it said, it's failing in the second layer, you can either use proportional of 10%, or you can use
Equalizing of 5%, you'll get the same result, and, that was the answer.
we will, so, I'm ready to start pushing people towards the OTEL sampler modes at this point.
Is what I had to say.
Okay.
If you were here last time, you know that I wrote a draft blog post and then did nothing with it in the two weeks since. So that's still out there.
I didn't do anything, because hackathon.
But I may reach out to some of you, or the next time, two weeks from now, perhaps have more progress on a blog post draft. I've been thinking about what you all said the last time.
So I don't… my intention was to say no more, and unless we have more topics, I think we can end the meeting.
**Kent Quirk (he/him)** 28:57 Sounds good.
**jmacdonald** 28:58 our SDK changes are almost in, so we'll have SDKs with these samplers soon, everybody.
Thank you all. Have a great day.
**Peter Findeisen** 29:08 Thank you, bye.
**Kent Quirk (he/him)** 29:09 See you guys. See ya.
**Carlos Alberto Cortez** 29:10 Pute.
