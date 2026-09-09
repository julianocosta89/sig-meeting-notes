SIG: GenAI SIG (APAC)
Date: 2026-09-08
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 01:33 Hey, Ludmila! Hey, Victor.
**Liudmila Molkova** 01:37 Hey, good morning!
**Trask Stalnaker (Microsoft Corporation)** 01:39 Good point.
**Victor  Lu** 01:39 Is today some, holiday?
**Trask Stalnaker (Microsoft Corporation)** 01:44 Yesterday, Yeah.
**Victor  Lu** 01:47 But, yeah. Last time I come to this meeting, it was, like, 10 plus people right now.
**Trask Stalnaker (Microsoft Corporation)** 01:54 Oh… Yeah, we did have a… Normally this meeting has been a little quiet, but yes.
Yeah, that's a good thought. I had a hard time getting up this morning and making it to the meeting.
**Victor  Lu** 02:11 Yeah, so, I did bring up the need for Kohsi people to come here, so I'm sure two or three people are going to come, either this one or the new one.
I'm not sure which one, so I'm just trying to see who comes.
**Trask Stalnaker (Microsoft Corporation)** 02:28 Great. Hopefully the… the noon one, Eastern… Since that has… the broadest audience.
**Liudmila Molkova** 02:49 Okay,
**Trask Stalnaker (Microsoft Corporation)** 02:56 Ludmila, we can… Sorry, I didn't… I… was looking at… your… I think what you were saying about the… Oh yeah, the metrics. The metrics, you mean.
Yeah, I had forgotten about our whole broader metric renaming.
all the things.
Wait, is that… no, I'm not allowed to pick me.
**Liudmila Molkova** 03:30 it was an issue, I don't think… Oh.
**Trask Stalnaker (Microsoft Corporation)** 03:34 Oh, yeah, but I wanna look at your… PR… Okay.
So, yes, yes, okay, so the detailed… Started to make… Sent to me… in that… histograms… normally we don't have a counter, right? For example, like, HTTP… Request count.
**Liudmila Molkova** 04:11 Right.
**Trask Stalnaker (Microsoft Corporation)** 04:12 Because it can be derived from the histogram.
**Liudmila Molkova** 04:16 Right.
**Trask Stalnaker (Microsoft Corporation)** 04:18 And that's why these are, like, detailed… That's the… what detailed means, sort… Sort of…
**Liudmila Molkova** 04:31 Because it's by modality, and by whatever else.
That would come.
**Trask Stalnaker (Microsoft Corporation)** 04:40 Yeah, that part I don't, like, I mean, everything, all… Counters are split.
But, I mean, if they have dimensions… I mean, you could… I was like, why, why are, why detailed?
what's detailed about them versus our… trying to think of the other… Metric naming in the… outside of GenAI.
**Liudmila Molkova** 05:08 This is pretty unique, I don't think we have a similar situation.
And detailed is… it's a breakdown, right? If we… you would use it for breakdown. It's probably more… more advanced than title? Well, you can use it as a title, right? It's even better.
**Trask Stalnaker (Microsoft Corporation)** 05:28 Yeah, I mean, you would use it as a total, right, like… I mean, the problem is that you can't… you just can't drive it from these guys…
**Liudmila Molkova** 05:38 Well, I mean, total input, or the sum input, or some output. You could use the first two for this without…
**Trask Stalnaker (Microsoft Corporation)** 05:46 Oh, for these children.
**Liudmila Molkova** 05:47 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 05:48 Yes, yes, but not these.
**Liudmila Molkova** 05:52 the main part, we just need the distinction between these two groups that… that is meaningful. And what I hear is that detailed is not meaningful, and maybe I need to go find a better word for it.
But I would love if you could help me and suggest something, because I'm… I'm a little bit lost and…
**Trask Stalnaker (Microsoft Corporation)** 06:13 Yeah, yeah.
**Liudmila Molkova** 06:14 how to call them. So, one idea I had is to stamp.count after, So it would be usageInputToken.count.
And it would be obvious that it's a counter. We would have plural in one place, and singular in another.
Because we don't.
Pluralized namespaces, and because we need to have We cannot have a collision.
**Trask Stalnaker (Microsoft Corporation)** 06:46 Yeah. One other question, yeah, I will, I will think about, I will… I will make some concrete proposals. I just wanted to kind of talk through, sort of.
At a high level first, to understand… The other question I had was usage.
I think region usage… Thought we had…
**Liudmila Molkova** 07:18 Right, somewhere in the metrics.
And…
**Trask Stalnaker (Microsoft Corporation)** 07:23 It was, like, a percentage or something…
**Liudmila Molkova** 07:28 Yeah.
It's general metrics, or something, or metrics naming… Or…
**Trask Stalnaker (Microsoft Corporation)** 07:47 Usage, instrument naming usage measures amount used out of a known total limit.
I mean, we're probably making it a namespace, so, like, it's… I mean, we could wiggle out of that if we wanted, but I wasn't sure… Like, what… Do we gain anything versus… Not having the usage there, if we just… your usage out everywhere?
**Liudmila Molkova** 08:16 Yeah, so there, I think there is option… 3?
Without it, and…
**Trask Stalnaker (Microsoft Corporation)** 08:25 Oh, I see.
**Liudmila Molkova** 08:26 the… The only tricky part is why I didn't strip it out, is that we have attributes.
that are GenAI… Something, input tokens?
If we put them… they are… the object for pretty much every model that holds this information is called usage.
And… Attributes look wrong and ugly to me without it.
It's like we don't provide the reasonable namespace.
You're probably looking for attributes.
**Trask Stalnaker (Microsoft Corporation)** 09:36 Yeah…
**Liudmila Molkova** 09:36 Ugh.
**Trask Stalnaker (Microsoft Corporation)** 09:43 GenAI… usage…
**Liudmila Molkova** 09:52 So we can say, okay, attributes have the namespace, and metrics don't.
And it's okay.
But also… like… It's okay with usage, too, given it's a different usage.
**Trask Stalnaker (Microsoft Corporation)** 10:14 Cool.
Okay, I think I understand, your… where you're coming from. Let me… let me think on it some more, and I will… propose some… Either… Either the same, or make some op, Give some options.
**Liudmila Molkova** 10:40 Yeah, sure.
Thank you.
**Trask Stalnaker (Microsoft Corporation)** 10:45 Cool. Shall we… shall we call it for this meeting?
**Liudmila Molkova** 10:50 Yeah, maybe one more thing.
It's about conformance and Brighton.
So, I've been switching Python to the conformance repo.
And… Alex actually created an issue.
But that we don't set proper instrumentation scope.
We used the same one, and we… Yeah, I think that's the problem.
I was thinking it would be super cool to make confirmments with validate the scope.
And I have a PR as the proposal to… By default, validate.
that… scope, name, and schema URL are provided.
**Trask Stalnaker (Microsoft Corporation)** 11:49 Okay, so not validating the content of them, but just making sure they are provided.
**Liudmila Molkova** 11:56 Yeah, and, like, you can use the expectation syntax to validate actual values, but it's under the signal, it's not a default.
There are a bunch of, well, I would say violations, So, yeah, if you look here, There are… Some of them that come without the schema.
And we can express them as expected violations, we can opt out from, like, failure because of this.
But… since you're here, and since you know why.
**Trask Stalnaker (Microsoft Corporation)** 12:38 Lovely.
**Liudmila Molkova** 12:39 You can't tell me if it's a bug or not.
**Trask Stalnaker (Microsoft Corporation)** 12:43 Awesome.
**Liudmila Molkova** 12:44 This is the self-observability thing, I believe.
**Trask Stalnaker (Microsoft Corporation)** 12:52 Oh, okay, okay, I'm like… Totally lost, yes. Yes, yes, yes, that makes sense. Okay, so we'll ignore this, This is more interesting, and yes, I… did we really never… fix that. We've had… we had an issue open forever, and… Mystery.
patients go.
No, not scope, SKU URL. Skema URL.
Maybe we fixed it, Emmett… Yes. Okay, there it is.
alright.
That is… I love this, conformance, testing of the Java instrumentations. Yeah, there… it found a few things earlier, That, you know, that, just in some random instrumentations, and yeah, it makes it very easy to be like, yep, yep, that is important to have conformance, so let's do it.
**Liudmila Molkova** 14:00 Oh, okay, so this is the answer, if we should keep it.
I mean, in the conformance. That's what.
**Trask Stalnaker (Microsoft Corporation)** 14:07 Oh.
Oh, for sure. Yes, yes, I love it. Yes.
**Liudmila Molkova** 14:15 Okay.
**Trask Stalnaker (Microsoft Corporation)** 14:15 Yeah, this is the only thing that's annoying, if we can… Find a way to sup… press… the health… metric… Help.
Yeah.
**Liudmila Molkova** 14:34 Yeah… Okay.
Yeah, I think…
**Trask Stalnaker (Microsoft Corporation)** 14:39 I mean, we could have… I think we should have a different conformance test for the health metrics, specifically.
But, like, I don't think those should… those violations should count against… specific instrumentations.
**Liudmila Molkova** 14:55 You don't want to disable these metrics for other tests.
**Trask Stalnaker (Microsoft Corporation)** 15:00 I would love to if I had a way.
**Liudmila Molkova** 15:02 Oh, I see.
I see. Okay.
**Trask Stalnaker (Microsoft Corporation)** 15:07 God.
**Liudmila Molkova** 15:09 So, like… Opt out, even from the findings here.
**Trask Stalnaker (Microsoft Corporation)** 15:17 Yeah.
**Liudmila Molkova** 15:19 Okay.
I'll… I'll think about it. I'll find a way.
**Trask Stalnaker (Microsoft Corporation)** 15:25 Yeah, I think in one of my, PRs that I was working on until I, here I was… yeah, just some… even if it's just, like, kind of hacky.
For now, in this repo, and kind of specific… even if it's specific to whatever.
And we can… yeah, and just, throw an issue, a tracking issue open, and you can assign it to me for, like, a long-term, you know, I can look at what we can do in Java.
**Liudmila Molkova** 16:03 Yeah.
I'm thinking about making missing attribute, or whatever it means that it's a known attribute.
to never be a violation. I kind of want to know that they were omitted.
So maybe we should put them in the… Oh, okay, sure Extra.
**Trask Stalnaker (Microsoft Corporation)** 16:23 attributes.
**Liudmila Molkova** 16:24 Yeah, so we currently dropped them from the… Things above.
We don't report them there. But maybe we should, and we don't report them as findings. This way, you can see what it actually means.
But you don't… Get the annoying stuff.
**Trask Stalnaker (Microsoft Corporation)** 16:44 Yeah, I mean, it's an interesting… Question, look for… I mean, I… for open telemetries, communities, instrumentation.
kind of… I think we kind of have a preference that we… only emit… No, I guess it's fine. I guess the… I saw one example in .NET where they were emitting a, the active requests.
HTTP instrumentation was emitting the active requests, metric, which is still in development.
I'm trying to think if… That's… Yeah, I greed, like, that… that's fine. I mean, having extra… extra things is fine. They have to manage the stability Of that themselves.
**Liudmila Molkova** 17:53 I mean, if we were in a very strict world, we would say, okay, you emit extra things, you publish your own schema.
you give it the schema, the proper schema URL in your telemetry, we validate the signal against the schema, and if it's non-documented, what you emit, you get a violation.
But currently, nobody publishes schema URLs for their stuff except us, and even we don't use it pretty well, so, everybody on this call, I guess, except Victor, and then we just… maybe we will enforce it at some point later, but currently we… we probably… I just want to make it visible in some way, but not as… it should not be reporting. Yeah, yeah.
**Trask Stalnaker (Microsoft Corporation)** 18:47 Makes sense.
**Liudmila Molkova** 18:52 Cool.
Maybe, oh, maybe we have these attributes with, like, requirement levels?
In the spans, like, command metrics, and we call this unknown, where the level unknown.
Or… group unknown, whatever.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 19:15 At least, the only thing that I've been looking at so far is the findings piece. Like, is it a violation or not? Like, that's the, Where would it show… where would it even show up, then, if we were, like.
What you're proposing as a secondary place where it gets emitted.
**Liudmila Molkova** 19:39 Let me share my school… So… Let's open one of them… Let's see… This friend.
So… Let's say, this guy.
Instead of reporting fighting here, we would have… oh, we don't have requirement levels here.
I see.
It's… it's somewhere else where we had requirement levels. I was thinking that we would report… we would still report them under the span.
So it would be an attribute on the span.
Where it, it appears.
**Trask Stalnaker (Microsoft Corporation)** 20:37 Oh, I see. Yes, so it would be here. Yes, we just wouldn't mark it as a finding. Yeah, yeah, that makes sense.
**Liudmila Molkova** 20:45 Yeah, and this would remove the need for… Like, it's a clodge or jargon reducer, or the coverage reducer, which produces the, report out of the river, full river report.
And this, I think, is the only thing that makes GenAI Reducer special, that it trains unknown attributes.
**Trask Stalnaker (Microsoft Corporation)** 21:11 Oh, yes, because of all the external instrumentations.
**Liudmila Molkova** 21:16 Right.
**Trask Stalnaker (Microsoft Corporation)** 21:19 Yeah, makes sense.
**Liudmila Molkova** 21:22 Cool.
I'll write it down.
So I don't forget.
Okay, then…
**Trask Stalnaker (Microsoft Corporation)** 21:30 Alright.
**Liudmila Molkova** 21:31 See you in…
**Trask Stalnaker (Microsoft Corporation)** 21:32 Steven.
Stay tuned.
**Liudmila Molkova** 21:34 Sometime in an hour again.
**Trask Stalnaker (Microsoft Corporation)** 21:36 Yeah.
**Liudmila Molkova** 21:37 Okay. Bye. Bye, Victor.
