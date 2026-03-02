SIG: Sampling SIG
Date: 2025-08-28
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**jmacdonald** 02:14 Hello. Where's my video?
Ugh, okay.
Come on, Windows, you can do it. Alright.
I see some agenda item, which is great, because I didn't have much.
… So…
Oh, neat. Okay, cool. We have two agenda items. One was from last time. First one… Hi, Peter, good morning. Hi.
So, Trent, I didn't see this one, but hotel sampling Slack, Java implementation uses different names… okay, oh yeah, yeah, I did see that one.
Oh, wow.
….
**Peter Findeisen** 03:01 So, I see three ways of dealing with this. One is do nothing. Just, comment that
In the code, that the corresponding specs are using slightly different naming.
If that's okay, of course. Second is, wait until we want to…
promote this implementation from the contrary repository to the core repository, which would also imply name changes, because we are using
This funny package name.
with, 56 suffix.
to differentiate, between the alt implementation.
So, since we will be making some name changes, it would be a good opportunity to change the class names as well.
And… well, the third option is to make the change, as is right now.
Breaking, of course, people's code.
**jmacdonald** 04:16 Yeah, I guess I would say it doesn't sound great to break people's code.
**Peter Findeisen** 04:20 I agree.
**jmacdonald** 04:22 Especially as we're, …
going to move and deprecate. I… so, I don't have a strong opinion. I'm not sensing a tremendous enthusiasm for implementing all this stuff that we've seen, but I'm glad to see,
this question come up. I think I would propose to fix it when it's moved into this the core…
Out of the contrib.
But…
We might want to revisit the names. So, I… I think what I did in my prototype was… was…
I had… composable was for the sub-policies, and I had composite for the… the transition from new thing to old thing.
So I didn't use consistent, but, …
Anyway, what do you think is best?
**Peter Findeisen** 05:18 Well, the third option, I agree, is the worst one, but I'm split between the first two.
**jmacdonald** 05:29 … I would be…
What about changing the names to match what's in your implementation in the spec, since there aren't very many of these at the moment?
**Peter Findeisen** 05:42 Well, okay, there is at least one Python… there is a Python prototype for that, which used
The names with… from the spec.
It would be quite rude to make the change right now in the spec.
So, ….
**jmacdonald** 06:01 Yeah.
**Peter Findeisen** 06:03 Okay, I, I'm… so, the first…
The first option, which is do nothing, just comment things.
I think it makes a lot of sense. It's not very elegant, I agree, but it will not break anyone's code, because nobody really
cares about matching the names between Python implementation and Java implementation.
If they understand that this is matching the same concept, this will be sufficient.
**jmacdonald** 06:37 Yeah.
Historically, I think the Java API and SDK have had this type of, …
outcome, where they prototyped something long before the group, and then leave something in place. So that, that might fit.
… do we have an… …
Do we have an issue? I wouldn't… I would be glad to just quickly, quickly run this by the spec SIG on Tuesday, if it makes people feel better. …
I can… I can handle that, if that was… Sure, sure, yeah, we… we… we need some input from other people as well here.
Okay, if… if I will… what I'll do is I'll follow up on the Slack, and I'll, post an issue, or something along those lines.
But I can take care of this for sure.
… Just reminds me that there is a… PR that I wrote up.
And… we needed to talk about that, especially at some point. Okay, well, Peter, I can take care of that one, and I'll come back.
**Peter Findeisen** 07:50 Thank you.
**jmacdonald** 07:51 So… and then I see, ….
**Otmar Ertl (Dynatrace)** 07:57 Yeah, I can, I can, agree with you.
Discussion.
**jmacdonald** 08:02 Sure, yeah. So, hi, hi, Admir, I remember that you were talking… we were talking about this two weeks ago. I briefly, raised….
**Otmar Ertl (Dynatrace)** 08:11 I had a quick look on the, on the, …
Composite, rate limit sampler in the tail sampler.
Still processing sample?
And, I mean…
They are, it's… there's a different meaning, or they have this example, right? So, if the span…
satisfies certain properties, then it's sampled with…
a certain rate, right? And if, …
If there's another… if the span falls into another category, they take another rate, and then for the rest, in order to fill up the capacity.
They, usually always on same floor or something like that, so…
And I was wondering, it's pretty, difficult to achieve, or to calculate
You know, the, the, multiplicity, or the, the trustee count, all that.
First of all, it's, you know, a condition probability, yeah, so if it's…
Actually, it's also not well-defined, yeah, what falls into…
This process is the always-on sampler, those which were not accepted by the first.
rate-limited samplers, so it is not clear. And so I thought a little bit how we could define it in general, what is maybe easier to understand, and I came up so far with two options.
Which I could imagine could work, and where you could also easily compute the probability, which is the requirement to…
Come up with the trust accounts.
So the option A is that you have, you know, it's too old.
Capacity, like, for example, 200 spins per second, and then…
you divide the span, I think this is something what Peter mentioned last time, that you really divide, you know, the overall stream of spans into substreams, into… ideally into disjoint substreams, because then you…
Handle every spend just with one.
… Rate-limited sampler.
And, then, for example, in this example, I could scroll up, but it's, like, …
for Category 1, we have 100 spans per second for the other one, 60, but here we have, Category 2 is defined such that it does not include those spans of Category 1, so they are those with property B, but not A, so that's important, yeah.
Because otherwise, we could have an overlap.
And for those spans, we use maybe 60, a rate of 60 spans per second, and then for all the remaining spans, the other 40 which remain. And overall, we have 200. Of course, it's not guaranteed that we fill up the capacity with that even,
if there are enough spans, but if they're all from property A, for example, or if all spans had property A, then we would only sample 100 instead of 200.
So, if you want to achieve that, you have to go for option B.
Where you just define, depending on the properties of the spans, or, you know, a weight, a sampling weight.
So, which tells you how important the span is relative to the others. So, it's just a relative weight. So, in this case, you would, for example, give Category 1 a weight of 100, yeah, 260, and all the remaining spans would get a weight of 40.
And then, what you try to achieve then is to choose the sampling probabilities
Proportion now to this weights.
Such that you meet exactly the global sampling rate of 200.
So, of course, this is not so easy to achieve, because you cannot go beyond 100% sampling probability for one category, so this is…
You cannot take more than all.
And this is a little bit more complicated to achieve, right? But these are…
Two meanings of… or two definitions, how you could….
**jmacdonald** 12:34 Sure.
**Otmar Ertl (Dynatrace)** 12:35 We are defined composite.
Rate-limited sample.
**jmacdonald** 12:40 That makes sense to me. The first… the first option, I would say, option A, sounds straightforward, and I appreciate the summary. The second option I think I've reasoned about before, but I always get into a place where I'm not sure I'm
that what I'm thinking about is actually correct, I guess. …
But my understanding of some of the, like, bottom-case sampling algorithms are that sort of, like, what they're doing. So you… so if you have a span with property A that you give weight 100, then you sample it using weight 100, it comes out with adjusted weight of 200,
Well, then I declare there are two of those spans.
In my sample, meaning I would give an adjusted count of the… the ratio of the outcoming weight to the incoming weight.
But I don't know if I'm avoiding conditional probabilities, I think is what I'm….
**Otmar Ertl (Dynatrace)** 13:38 I mean, I was not talking about how we can achieve that with consistent sampling, it's just about, yeah, how in general you can do the sampling. So, to achieve
To do that in a consistent way, you know, using the…
Yeah, shared randomness. It's possible.
But it's, it's… complicated, yeah. And….
**jmacdonald** 14:05 Well, this is a good… I think this is great. I appreciate the report. I wrote at the bottom of the notes that I had spoken, last week with Sean Porter, who is maintaining this code, and …
I could give you a backstory, but I don't think it would be very interesting to all of you about the politics of that component. Anyway, what he said was that the users were not very…
The users don't understand this option anyway, so maybe it's not very important.
And I think that probably Peter's construction with independent limits and stratified, like, sampling is a lot more logical to users, so…
I don't think we need to belabor this point.
My goal in raising the question of tail sampling processor still exists. I think that, I spoke with Sean about
essentially.
My wish list, if I could have it, to upgrade the tail sampling processor with first OTEP235, you know, like, recognition of the incoming weight.
And then the second step, admittedly, is a lot more to ask, but it would be some sort of memory limit that respects
Sampling, in the sense that whenever we need to shrink the amount of memory we have, we're going to adjust counts and output them.
…
For me, this is gonna be an ongoing but low-priority thing. I don't have much more to say about it this week.
**Otmar Ertl (Dynatrace)** 15:33 Regarding the tail sampling process, one thing to add, because if I'm correct, I saw that the rate-limited sampling is implemented in such a way that you just
Take the first few spans every second.
**jmacdonald** 15:50 Yeah.
**Otmar Ertl (Dynatrace)** 15:50 budget, so there's no randomness.
**jmacdonald** 15:53 Yeah.
**Otmar Ertl (Dynatrace)** 15:54 That means it's not pretty probabilistic, and so you… it's also hard to….
**jmacdonald** 15:59 Yeah.
**Otmar Ertl (Dynatrace)** 15:59 But it's all not fair, and it's also hard to compute the actual sampling probability, which you need to get the adjusted count.
**jmacdonald** 16:08 Yeah, so I basically laid out a plan, and I have it in my head right now. It's gonna take a lot of
work, but, the… the complicated piece I was trying to put in place there, I described roughly as
I'm gonna take my budget, whatever it is, for memory, and I'm gonna slice it into, you know, some 10 slices, or something like that. So if it's a 30-second window, and I've got a budget of 100,000 spans, I'm gonna give
1 tenth to each window first. That's just a simplifying assumption. Now, for my 3-second window, I'm going to have a fixed quantity of memory, and
And I'll use consistent sampling
following the paper you gave us a few weeks ago, two or three weeks ago, two or three meetings ago, which I read through and understood, so that, you know, within each bucket, you're now just, like, shifting the threshold until you've got the right number, and
this would require swapping in a whole bunch of new logic, and I was thinking about, like, a transition plan, which might look like, you know, create an interface for the old logic, which is non-probabilistic.
does exactly what it's doing today, swap in a new thing that's maybe experimental at first that will do this. But it's a big change, and it would take a while, so I don't want to make people, overly enthusiastic, but I would like to get that.
….
**Otmar Ertl (Dynatrace)** 17:35 But what you described, or what is described in the paper is more or less a consistent…
version of a reservoir sampling approach, which uses consistent sampling, right?
**jmacdonald** 17:46 Yeah.
I read… I read it. It made sense. I struggled.
**Otmar Ertl (Dynatrace)** 17:50 Yes.
**jmacdonald** 17:50 through the paper a little bit, but I did get there, so… that's exciting.
**Otmar Ertl (Dynatrace)** 17:54 That's also…
And the question is also if you really need a consistent sampling in the tail sampling process or not, because
Make, the same sampling decision anyway for all spans of the trace.
It's maybe not that… important, if you will.
**jmacdonald** 18:15 Yeah, I agree.
**Otmar Ertl (Dynatrace)** 18:16 Same randomness.
**jmacdonald** 18:18 As well okay. Well, I don't have, enough time
So here, I think this is all interesting, I just don't want to promise that I'm going to get much progress, and we can keep talking about it, but I don't want to take much more time on it.
I will come back to the issue above where I said I would help with that terminology question. What this reminds me of, and I know Carlos is here listening, is I… we talked about making a blog post, something to, like, remind the OpenTelemetry community that we have done some work, and that something is coming.
… I think it's probably time for that.
….
**Carlos Alberto Cortez** 18:56 Yeah, I agree with that. I think it's time, even if it's not stable.
**jmacdonald** 19:00 Would you agree?
**Carlos Alberto Cortez** 19:00 It's a way to get people's, you know, hands on these components, you know.
**jmacdonald** 19:06 So at least that would stir up the SDK maintainers to help us.
I… I've already volunteered to do a lot, so I don't know if I can promise anything in the next week, but I'm writing it on my list like I want to do it, and …
what I'll do is I'll… I'll… if I do… if I do anything, I will communicate in Slack, like, here's my outline of a… of a short blog post.
It shouldn't be very hard. I want to do it, so I will… I will at least accept responsibility for getting it done, and try and, ask for help.
**Carlos Alberto Cortez** 19:42 Yeah, I think that it, … I can do that as well, but if you want, I would rather rely on you, but if you find yourself busy in the next 2-3 weeks, just let me know. In the meantime, I still need to review the item prototype, you know?
**jmacdonald** 19:56 Carlos, at the very beginning, I think before you dialed in, we had a question about naming. I'm gonna scroll back up. It's… it's… I'm in a, …
there's a Slack question, I'm gonna create… I'm gonna file a spec issue, and then I will paste it, and I'm gonna ask your help thinking about
you know, legacy names in the Java implementation, how do we handle them? You know, we've already got a disagreement between Python and Java. The specs is one thing, Java says another thing. It's hard to resolve, but I'll follow up on that.
**Carlos Alberto Cortez** 20:27 Yeah, I think, yeah, just to make it more obvious, just sign this issue to me.
Yeah, you would trade the issue, correct? Yeah, okay, assign that to me, so it's clear that….
**jmacdonald** 20:36 File the issue, assign it to you, and we'll be done.
Yep.
Thank you all. I think we've reached the end. I like to keep these short. I'll see you in two weeks.
**Peter Findeisen** 20:46 Thank you.
**jmacdonald** 20:47 Yeah. Bye.
**Carlos Alberto Cortez** 20:48 Joe.
