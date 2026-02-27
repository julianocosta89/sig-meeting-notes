SIG: Sampling SIG
Date: 2026-02-26
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Kent Quirk (he/him)** 01:56 This is Kent.
**Peter Findeisen** 02:01 I can't.
**jmacdonald** 02:45 Good morning.
My computer's being really slow, so hang on a moment.
**Otmar Ertl (Dynatrace)** 02:54 Right?
**jmacdonald** 02:56 Here we are, once again. Glad to see you all. We have a few
More than normal. At least one more than normal. Hello, Chris. Nice to see you.
We are…
going to start… I will just start doing this. I'm gonna add an entry. We skipped last time, I remember why, but never mind. Oops.
So we are once again, together. I'm gonna start thinking about the agenda in a second, and if you have something to speak about, please prepare yourself.
**Kent Quirk (he/him)** 03:31 I, I, I do quickly.
**jmacdonald** 03:34 Good.
**Kent Quirk (he/him)** 03:34 Sorry, sorry to say.
**jmacdonald** 03:36 No worries.
**Kent Quirk (he/him)** 03:37 My, my company's had quite a reorg, and, basically…
I'm not going to be able to continue on this group. I'm working on a new team, and different projects, and… and not associated with sampling at Honeycomb anymore. So, I don't know if anybody else will be coming anytime soon. The entire
project of this has been… has been de-emphasized in favor of other work. So, I'm unlikely to show up again.
In the near future. And,
it's the vagaries of modern business, I guess.
**jmacdonald** 04:21 I guess I take it you're not, leaving Honeycomb, and that's good news to me, I guess. So… and I know where to find you, at least as long as you're still somewhat involved in observability.
Thank you for your involvement, Kent, and for your, you know, reviewing and talking about this for years now, so thank you.
**Kent Quirk (he/him)** 04:40 You're welcome. Thank you.
It's… it… this is…
There's a lot exciting going on, but there's also, like, there's been a lot of changes, so…
**jmacdonald** 04:50 Yeah.
It's a crazy world.
**Kent Quirk (he/him)** 04:52 I can focus on right now, so…
**jmacdonald** 04:54 And we will still look to the refinery example as a, you know, like, kind of a North Star, in my opinion. Like, the community wants such things, but, you know… Yeah.
**Kent Quirk (he/him)** 05:04 Yeah, and there's… Nothing gets built for free. Cool stuff is still happening, but it's just gonna happen a little slower, and without my involvement, I'm working on other stuff, so…
Anyway…
**jmacdonald** 05:15 Our industry's changed a tremendous amount in the last year, so we understand.
**Kent Quirk (he/him)** 05:19 Yeah. Goodness. Anyway, thank you. I'll, I'm gonna drop, because I have other meetings, but, it's good to see you all, and, I'll try and stop in at some point.
**jmacdonald** 05:28 Okay.
**Yuanyuan Zhao** 05:29 Yeah, I just want to say good luck with everything.
**Kent Quirk (he/him)** 05:32 Thank you so much, I appreciate you all.
**Otmar Ertl (Dynatrace)** 05:33 Opest to you.
**Kent Quirk (he/him)** 05:34 Thanks.
**jmacdonald** 05:38 Well, okay, that was news. We're back to 5 then. Welcome, Chris, you're gonna have to take Kent's place.
Yeah, I don't entirely know what that means, but we'll see.
You know, I recognize that you've been pinging about some stuff with sampling and the collector. This is usually a really small group, and I know everyone else here, so I'm gonna recommend that you're here, so we should talk with you to craft the agenda.
Would you mind telling us what you have in mind?
**Chris Marchbanks** 06:11 Yeah, so I can give a brief intro, so I'm Chris, I'm actually coming from… I've been a long time, like, Prometheus maintainer and, like, in the observability space, but have been moving towards, my day job is more and more on traces these days, and sampling has been somewhere I'd like to focus,
So I want to join the group.
see what all, what all is happening. I mean, even back to, like, I see Atmar is here, like, you had a paper that you wrote probably 5 years ago now on, like, partial trace sampling. That's something that…
Is relevant and being considered, so it seemed like a good group of people to get some context in, and…
Help out with both tail sampling and some, like, head sampling, partial trace sampling ideas, things like that.
**jmacdonald** 06:57 Fantastic.
Yeah, so I know you're… I know you're familiar with the, kind of, collector component.
**Chris Marchbanks** 07:03 There's a little bit of a discussion happening about…
**jmacdonald** 07:07 tail sampling processor needs maintainers, and I've stepped up a little bit, but, like, it still needs decision making, and then…
there's a… there's a little bit of a Grafana-heavy question here and there, and then there's, like, you know, there's new components being proposed, and it's all a little bit chaotic, but in this group, we at least keep our principles in mind and talk about, like, rigors of sampling
And so on, and I like to think that the work we're doing is slowly influencing the others, the surrounding territory, and hopefully that's true.
So…
there's still ongoing work, you know, pushing SDK specs on sampling. It came up recently, we're all aware of it, but I'm glad you're here.
And was there anything specific that you had in mind? I feel like I was out for a week, and so that's part of what… like, I know there was a Slack thread, I think you asked me to review something. What was… what was going on?
**Chris Marchbanks** 08:04 Nothing too specific. I… you reviewed what I… what I wanted to look at, that was just a little tail sampling processor. A lot of it's just context.
for me that I want to learn about, a little bit more… I mean, I'll say partial… partial trace sampling is the big one that I'm curious about, and trying to experiment in ways to do that.
without having to re-instrument everybody's code, which is challenging. Some of that then goes into, like, the trace context, and…
all sorts of that little bits of information that become important. So that's what I'm curious around.
Yeah.
**jmacdonald** 08:44 Great. I think that this group has a little bit of a handle on, or at least awareness of the kind of potential we know about
how to configure SDKs for sampling, but the sort of more advanced version of
configuring and, you know, to avoid re-instrumenting is to have these composite sampler supports, and then configuration supports, and maybe op-amp support. And, like, it's… it's a lot to ask for all at once, and that's why, you know, here we are, years later, still kind of…
Stepping forward, step by step.
And… but the more… the more interest from the more vendors we get, I think the better and the faster it moves.
**Chris Marchbanks** 09:25 Nope.
Yeah, and for awareness, yeah. I do work at Grafana Labs. I'm trying not to become, like, here's even more Grafana Labs influence on tail sampling process there, but…
**jmacdonald** 09:33 That's okay. I actually have tons of respect for Gafana, you know, they've always held open source up, and I think that's important. So, you know…
It's okay. It comes with having so much presence in a small space, I think.
So, glad to help as well.
The topic that I would kind of respond with is that there's this,
Sean Porter has proposed this trace pruning processor, and it's going to require a lot of review work from a lot of people to support, and I'm… I'm weakly positive on it, meaning I don't want to be the only reviewer for it.
But it, sounds like it's aiming towards
some of the stuff that you just mentioned, this partial trace sampling would come up, and you know, this group… in this group, we've talked about how tail sampling, and this would be Kent's, like, like, major emphasis, if he was in the room right now, is that the tail sampling processor has almost no rigor about
counting the outcomes. And it, you know, one thing we could imagine doing is, is starting to,
Have that rigor so that when you've sampled a window of time, that you pretty much know how many spans were through… went through you, and that if you over-exceeded a memory limit during that period, that you
that you did the right thing, and that… and you kept track of how much sampling took place, which is a lot to ask, and when we've… we've all… Kent and I have mostly have looked at the tail sampling processor, and…
it's not clear that it's in a state that can be fully rescued without essentially rewriting it, and so that's the hesitation I feel whenever we talk about it.
But… but we're practical people here, and, like, tail sampling is the thing we have, and we have to maintain it and make it better, so I'm… that's my position, is it's not… not exactly what I want, but we have to hold it… hold it up.
**Chris Marchbanks** 11:31 Yep.
Yeah, it's reasonable.
**jmacdonald** 11:39 Are you gonna be able to review the trace pruning processor? Do you know Sean, or…
I get the sense that there's a… Grafana has, like, a… like, a number of sub-organizations, and that Sana's in a different one than you were in.
**Chris Marchbanks** 11:54 I'm actually… I recently moved… well, it was, like, a few… I don't know, 4 or 5 months ago now, I moved to the same org as Sean. I have reviewed the partial, or I have reviewed the SPAN pruning processor.
Good. Something we would like to have in OpenTelemetry Collector, that said…
There's been a handful of these experiments that we've been wanting to try out, so we have recently made an open source repo that could house it as well.
**jmacdonald** 12:20 At least it's still in open source this way.
**Chris Marchbanks** 12:22 But it reduces some of the…
single maintain, like, I don't know, basically asking you to review everything as the only non-Grafana person on that.
**jmacdonald** 12:34 Yeah, I'm not… I'm not totally against it. I'm… what I'm… my bigger concern is that it's really hard to maintain a collector component outside of a collector repo, because we're still making breaking changes, like, so frequently, and so that's… that source of pain is, I think, too much to ask, and we should…
**Chris Marchbanks** 12:50 Yeah.
**jmacdonald** 12:51 you know, we should do something, but it can't… one person can't do it, so I… but that's what we're talking about.
**Chris Marchbanks** 12:57 Yeah, so we're… I don't know, we're going to see… we're gonna experiment with that a little bit. We're going to… we've got, effectively, a couple comp… it'll probably be the…
the span pruner, and then I'm looking at a…
exten- basically extension to probabilistic that looks at partial trace sampling and has some ideas there.
**jmacdonald** 13:18 As, like, these are very experimental, let's see how painful it is to…
**Chris Marchbanks** 13:23 experiment with them outside of collector contribib, with, like, hopefully we could contribute them eventually if they see adoption and success as the goal.
**jmacdonald** 13:32 Alright.
**Chris Marchbanks** 13:33 I'm curious. And maybe we could learn more, like, yeah.
**jmacdonald** 13:36 Cool, I'm curious about that, maybe not right for right now, but what you have in mind for probabilistic sampling as well, how… what an extension looks like to you. That was the only thing… I hope that we're not boring the three other people talking… listening to us talk, but
The, there's also someone talking about a Pebble extension for tail sampling processor.
**Chris Marchbanks** 13:58 It's awesome.
**jmacdonald** 13:58 And I don't think they're from Grafana.
And that's… that's the type of tension I'm feeling, is that, like, this is also some major piece of functionality being requested for this
Fairly valuable, common code.
And I know there's just pushback on everything in the collector-conscribed repository, because it's become so huge and hard to maintain, and, like, it's got too many components and so on. So, adding a new extension
doesn't sound good, because it means adding a new Pebble extension. Extension interface means adding a new Pebble extension, and that means…
But that is the right way to do it if you don't want to bloat everyone's binary by the size of a pebble library. And that binary is really big already, so…
That's the… that's the conversation. I don't think it's a conversation for this room. I think it's actually a collector maintenance issue. So, that's under discussion, but kind of not sampling.
Just tech… technology is for mixing code with options, essentially.
Yeah, I've been doing a bunch of work on extension models in Go. I have a blog post I'm working on.
Cool. Well, thank you, Chris. Let us know if there's anything specific.
**Chris Marchbanks** 15:10 Will do.
**jmacdonald** 15:12 And, glad you're here.
How about… so I know Yuan Yuan's been working on span counting, so I know there's a little bit of an update there.
**Yuanyuan Zhao** 15:22 But, yeah, well, I am officially on PTO, this week, so I haven't looked into it, but, I think later last week.
What's his name? Israel. But I have some more comments, so I'll look into that.
I think he Stages, some more tests, and yeah, go ahead.
**jmacdonald** 15:47 Yeah, I saw the feedback. I've also approved the PR, you know, like, it's good to make it.
**Yuanyuan Zhao** 15:52 Long time ago, yeah.
**jmacdonald** 15:53 But it was a small comment, and looks good. We should be able to get that, too. I'm also now an official approver in that repository now, so my approval counts, which is good.
**Yuanyuan Zhao** 16:04 That's great.
The other thing, I opened, that's the, Go SDK implementation of Trace ID ratio-based.
I opened a new issue. I actually started working on that. I got a bunch of, like, your draft PRs, and I'm starting, like, building things off.
There is something, that's…
I think the… supporting the random bits.
in, trace context, that's a… dependency… we have.
I mean, that's strict in terms of, like, we can't make any moves, before that. But it is a dependency for the whole thing. That was filed
Some time ago, and was taken up.
Just a few days
Before I was going to, you know, take some ownership, official ownership on the issue. So, that one has been in review for a while for a very small
feature.
It is, on one hand, not very…
I mean, we certainly shouldn't, you know, like, preemptively do something, right? But it is kind of in the… in our past.
**jmacdonald** 17:43 So, it sounds like one of the Go maintainers or contributors, started working on something that maybe got a little bit in your way.
**Yuanyuan Zhao** 17:53 Yes, it's just supporting the, trace ID, random bits in the trace ID.
**jmacdonald** 18:01 Okay.
**Yuanyuan Zhao** 18:01 This is the one up.
Pasted here.
**jmacdonald** 18:04 Thank you. Yeah, we can… we can marshal some help on that.
**Yuanyuan Zhao** 18:07 I would ask David Ashpole to take the lead on it, just because he has a better relationship with the maintainers.
He… he is work… he's reviewing that one.
**jmacdonald** 18:17 Yeah, so I will… I will trust in him, and if we need help, I can talk to him directly.
Cool. Yeah.
That's the right way to go.
**Yuanyuan Zhao** 18:26 Yep.
**jmacdonald** 18:27 Alright.
**Yuanyuan Zhao** 18:28 Okay, hopefully that, We should wrap up the spend metrics connector thing very soon.
I…
I'm off this week, but I will, possibly working on it this afternoon if I have some personal issues to take care of, but I might have time.
**jmacdonald** 18:50 Cool. Well, thank you, Johan. Thank you, Yohan.
Well, here we are,
I'd have no more further agenda on sampling topics.
And if I could entertain you all for one second, unless someone else has an agenda item, I have a math topic and a brief conversation to have with Atmar, if I may. And you might all want to listen or not.
But.
**Carlos Alberto Cortez** 19:22 I have something in the agenda. It's not super important, but that's something before I forget again. So, you may remember the newly added, always record sampler.
Which is in development, and so I was talking to the JavaScript maintainers, and they said that they have the prototype, but it's, like, straightforward, relatively.
And there are many prototypes, like, what's the plan? It doesn't sound too controversial.
So, what would be the next steps? You think that…
Is there something needed on the front to verify from some back-end side, or anything, or… collector processor sites.
Otherwise, it looks like… I mean, this PR was merged a couple of months ago.
**jmacdonald** 20:08 So, to… to bring us to the… just to help the room, in case there's any confusion there, this is about, the always record sampler decision is one that's meant to support, like, the ZPages use, or the you have an in-process.
sort of, like, Servlet or daemon somehow intercepting live span data, and you're not exporting that data.
So it was a fairly narrow feature request, and it made sense in the sense that, like, we're not… if we're not exporting, then the sampling questions don't really…
Get in our… like, it doesn't come up, essentially.
But I'm… I'm reminded that we…
probably have a position. It's probably pretty straightforward to say if you're going to emit a span that was
not sampled. You know, like, that's the next step, is people have asked to be able to export those spans that were not sampled.
And they would come out looking exported and unsampled.
And we have several ways to say unsampled, but mainly the sampled flag is not set.
And the reason why that's gonna raise, kind of, complexity is that there's no flag to say unsampled, so,
you have to presume that the sampling flag works correctly before you can say, oh, this is not sampled, because this bit is not set. And the problem is that the bit was not there in the earliest days of OpenTelemetry. So, like, an early span from the early days will have a zero, even though it was sampled.
So, you know, that's kind of a, like, non-issue, but it's not zero, or not, you know, it's something.
But I don't have an issue with… I don't see any issue just directly, like, the always record feature is…
not… Not interfering with sampling.
It's just a step towards an interference pattern.
That helps.
Yeah.
Anyone here have feelings about… Wanting to be able to… record… Spans that were unsampled.
The other reason why I've seen that desire is, like, you want to record raw histogram measurements, and you don't want to record whole traces, so you encode spans, and you just export them, but they were unsampled, so they don't have traces. But they have a histogram measurement you can derive.
For example.
**Yuanyuan Zhao** 22:41 Yeah, that's… they always record something might be coming from…
People who have doubts on statistical approaches.
**jmacdonald** 22:52 Yeah, that's… that is for sure. The other reason quoted for this type of feature is to let you have perfect metrics, meaning, you know, no loss of fidelity for your metrics, but then just not record those spans.
Not export those spans, not sample those spans.
So, right, I don't have an objection to it, it's just, it doesn't go quite as far as I know that some… some people want us to.
Yeah, if there's a spec issue and you'd like me to approve, I will be glad to.
**Carlos Alberto Cortez** 23:29 Yeah, okay, in that case, yeah, I will open a PR, probably talk to the original author of that PR, you know, probably he got more feedback, on his own company or anything like that, so yeah.
Okay, let's do that.
**jmacdonald** 23:44 Cool, thank you.
**Carlos Alberto Cortez** 23:45 For you.
**jmacdonald** 23:46 And now if I may co-opt this meeting to talk about the exponential histogram, which is not exactly sampling, but the connection is that Atmar and I have worked on it, and we've worked together a long time now, so I have a question, it's a…
And I'm gonna put up…
So, as I was… as I was saying to,
Kent earlier, our industry has changed a lot, so I will say, I've been using an AI assistant here, because I couldn't have done it in the time I had without it. So this is not ready for public review. I don't like throwing code from the AI out like this, but…
We had… so there's two old prototypes from New Relic and from Dynatrace, of a table lookup that's exactly correct, given a size of table that's got pre-computed logarithm.
significantans in it. So there's two algorithms, and they're almost identical.
And,
there's a sort of sizing question of, like, how much memory do you devote to these pre-computed tables? And then there's a slight difference between these algorithms, where the New Relic put a secondary… there's a secondary table for linear lookup.
And the secondary table has either two N or N buckets. So, Atmar's algorithm uses n buckets, and then afterwards, it uses two corrections.
And then the New Relic uses two sides… twice as big of a linear lookup table and one correction.
And I was trying to ask my, you know, and I'm like, this is all stuff that we learned years ago, but I was trying to ask my agent, and like, this is, like, irritating to me, because I never would have gone for a theorem here, but the theorem says all those numbers are irrational numbers, therefore there's never an exact equality on a power of
a prefix of a power 2. Therefore, we know that a greater than or equals is equivalent to a greater than, except at 0.
And the case that I was… I wanted to discuss briefly is that
I didn't write this, I don't feel comfortable sharing it, but… so there's an algorithm here which says.
they're the same algorithm. You do a lookup in the linear table, and then you do up zero or one or two corrections, and that's the answer. Like, this is the algorithm.
And this is what I wanted to talk about. Why is the out… why is two… two corrections for the… the Atmar version of this, and one correction for the New Relic version of this?
And the reason that I'm asking is that I wanted to make a change. The change has to do with the upper versus lower inclusivity question, and this is, like, sort of airing the old
dirty baggage, but if you recall, when we first designed exponential histogram, we used lower inclusive boundaries, and it's been debated, like, so much text was spilled over this topic.
that we would, that because the IEEE floating point standard, and because hardware, it's, like, actually easier to do a lower inclusive boundary for your histogram when you're doing
bits and floating point and binary. However, Prometheus was adamant, absolutely convinced that we were breaking and hurting them.
like, really strongly. So there was this, not just, like, technical, but emotional component of, like, okay, fine, we are going to adjust the spec. We're going… we're not going to change the inclusivity between the boundaries, but on the boundary, we'll make that special case. And I've written a lot… lengthy text myself, there's links in this document.
The point is
We have to do one more tiny special case, and what we could have done is taken those old algorithms.
which required one or two corrections, and then fix them up. The fix is, if you have a significant hand of zero, subtract one.
But then I'm doing 3 checks, or 3 corrections, and I don't want 3 corrections, I want 2 corrections.
So, the proposal was to put in a sentinel value. These algorithms already have sentinel values on the right edge, so that you can always correct and go off the end of the array and still have your correction. So I'm putting a sentinel at the beginning to handle the zero case, this really weird special case.
And I was then trying to convince myself, how come I only need 2 corrections, and not 3 corrections?
And…
I don't believe the argument here, but this is my AI assistance argument, which is that because we have a size of N, and there, you know, the factor is that each linear bucket can cover up to 1.4, or square root 2,
logarithm buckets, because of the derivative. Hmm? I don't know if I believe this, but… Therefore.
That's the reason why it's 2 or 1. And this sentinel that I added at 0 doesn't change the argument. I still only need 2 corrections, because I only need to cover 1.4 boundaries, and 2 corrections will always cover 1.4 boundaries, whether I have a sentinel or not.
That is the argument I'm trying to make.
And I had a lot of trouble convincing myself, and this didn't even convince me. This did not convince me, but it's the best I could get.
In my small amount of time.
Atmar, how's that sound to you?
**Otmar Ertl (Dynatrace)** 28:58 Yeah, I mean, I think this should work if I implemented that myself, because when we started to update the reference implementation on DanaHist, I wanted to do it,
Already a long time ago, but never found time for that.
But now I wanted to really,
provide a layout in Dynast which is fully compatible with the spec, and…
Yeah, I did it a different way, but this has other reasons, because I wanted to use the same lookup table for the old implementation of the new one.
And I also needed, but this is specific to Dynahist, that, positive infinity.
Infinity has to be mapped to an index which is larger than that of double max value.
And so I had to… Yeah, so this cannot be solved with this ethanol value.
And, because with the exclusive mapping, automatically the positive infinite value would go to another index.
**jmacdonald** 30:09 Yeah. Friends…
**Otmar Ertl (Dynatrace)** 30:11 But this doesn't work with the… Sentinel value anymore.
Yeah, yeah, that was the reason, but I think your approach is right, yeah.
**jmacdonald** 30:25 It feels right, but if I couldn't.
**Otmar Ertl (Dynatrace)** 30:28 Goods.
**jmacdonald** 30:29 So…
**Otmar Ertl (Dynatrace)** 30:30 And I also implemented it that way, and also did all the unit tests in Dynast, which really tried to
test the exactness, you know, its boundaries, right? It's not just the mapping…
add… yeah, full double radius fields to the boundaries, if they're mapped to the right boundary. I mean, it's not a formal proof, but .
**jmacdonald** 30:57 Yeah, I did an exhaustive test for one of the buckets at scale 20, so a million entries…
**Otmar Ertl (Dynatrace)** 31:02 the…
**jmacdonald** 31:03 etc. And… and there's, like, 3 billion floating point values in there. But, you know, and at 1.7 nanoseconds, we could actually test them all reasonably fast. So I did… I did some of that, but it didn't… it's not approved, and that's why I'm asking you, kind of.
**Otmar Ertl (Dynatrace)** 31:17 F.
**jmacdonald** 31:18 Anyway.
**Otmar Ertl (Dynatrace)** 31:18 No, but… This is what I wanted. But it's groupables, for sure, yeah. So much… it's faster. That's interesting.
**jmacdonald** 31:25 Excuse me, sorry.
**Otmar Ertl (Dynatrace)** 31:27 Just want to add to the history you told, you know, because, you know, there was this discussion about inclusive exclusiveness, and actually, it didn't make much sense, because,
in the spec, it's allowed to do an inexact mapping anyway, you know?
**jmacdonald** 31:47 Yeah.
**Otmar Ertl (Dynatrace)** 31:48 Because this is actually what they wanted to achieve back then, to have a meshing independent or platform-independent mapping, you know, based on the IEEE standard, how every value of the double precision format gets mapped to a certain index.
And this can only be achieved with such a lookup table, and where I showed you how such a mapping makes sense, because it's always fast.
But there were also, you know, discussions not about the intensiveness and exclusiveness, it was also a discussion about the maximum supported scale value.
And, in my opinion, a scale of 10 is more than enough for any practical use case, but, you know, there was, I think it was by New Relic.
They wanted to have scales, I know, up to 20 or so.
**jmacdonald** 32:39 I support up to 20 in my reference implementation, which is to say, like, a million buckets per interval, which is…
**Otmar Ertl (Dynatrace)** 32:46 Stable is huge, then, you know, if you really want to support.
**jmacdonald** 32:50 Yeah, I… it's actually more of a, like… for me, it was more, like, I really enjoyed doing this. The reference implementation aspect of it is, like, yes, technically, you can support up to…
Well, at least 20 is reasonable, but depends on your BigNome implementation, because you're going to actually, at some point, have to correctly compute the exact value, and the way I've computed the exact value is to raise 2 to the…
K, and then square root n times, so you… 2 to the K, and then 20 square root operations.
But 2 to the K will end up being outside the range of a 32-bit exponent, and the big num library in Go
for a 32-bit, or bigger than a 32-bit exponent, so 20 also is the maximum for that reason as well.
**Otmar Ertl (Dynatrace)** 33:35 In my… no, I mean, in my Java implementation, I have, an exact computation of the lookup table, you know, using,
You know, big, integers and so on, you know, you can.
**jmacdonald** 33:51 Yeah.
**Otmar Ertl (Dynatrace)** 33:53 So, not a problem computing the constants, but the table gets huge, and it's not practically anymore if you have a lookup table which is a size of 1 megabyte.
**Chris Marchbanks** 34:05 Anyway, well, thank you… I'm sorry, Chris, please. Out of curiosity, what scales do you typically see people using? Like, Prometheus goes to 8.
**jmacdonald** 34:14 Yeah.
**Chris Marchbanks** 34:14 I've seen somebody go past 8.
**jmacdonald** 34:16 Yeah. The, New Relic may be… and it was just discussed as, like, a maybe this is what you want if you're doing scientific something, something, something, and, like.
**Chris Marchbanks** 34:25 Hmm…
**jmacdonald** 34:26 The… the…
**Otmar Ertl (Dynatrace)** 34:27 I know the argument… I know the argument,
It was like, you know, if you have, a distribution of values which is highly concentrated, let's say around 1, or, like, one between 1 and 1 plus 10 to the power of minus 6, you know?
And, and let's say it's,
you're interested in the shape of the distribution, you know? Then you need high scales.
**jmacdonald** 34:57 Yeah.
**Otmar Ertl (Dynatrace)** 34:57 Yes, okay, we are moving past…
**Chris Marchbanks** 35:00 most pragmatic monitoring use cases here.
Okay.
Makes sense, thank you.
**Otmar Ertl (Dynatrace)** 35:08 And in my opinion, was the main purpose of this exponential Instagram grant is to reduce, you know, the data.
And… and so such fine, fine resolutions do not make sense, yeah? I mean, if you…
**Chris Marchbanks** 35:22 then just store your old data, and you're fine, you know? Just store the data and do some analysis at that point, like…
**Otmar Ertl (Dynatrace)** 35:30 Thank you.
Yeah, but there was no way to convince them, you know, that an upper bound of the scale would make sense, because then we could have defined it in a platform-independent way, because then you could say, let's define the constants in the lookup table, you know, up to scale 10.
And then, on every platform, the mapping would be the same. But, yeah, this was…
**Chris Marchbanks** 35:58 Because right now, yeah, you can't do, like, the platform differences will… yeah, as soon as you stop using lookup table, you hit that.
**jmacdonald** 36:03 Well, if you're using the logarithm, but if you're using the exact lookup table, in theory, we get… we fix it. That's why I want to do this work, finally, is to… is to have the OTEL spec write down the exact table lookup form.
At last. We haven't done that. So that's what I wanted to do.
The, the precision and resolution sort of question aside, which I don't… I don't mind it, but I… like, 20 is the limit for me, just based on Big Num support.
It sounds like there's a question here about infinity. Chris, one of your colleagues has recently been involved in this effort to stabilize the hotel to Prometheus histogram mapping, and there was discussion about infinity values and NAND values.
And in my sort of simplistic formula, like, thinking of hotel in the past, we outlawed those. Like, you can't have a NAND value, you can't record that.
Same for infinity. Like, why are you putting infinity into a histogram? But I… but what I also know is that infinity is just, like, literally the upper bound of the last bucket.
And so… and that was that… the reason why the Sentinel doesn't always help you, that I think Otmar was referring to. So we could actually support the infinity value, but it… it's the type of wrinkle that will cause an entire day of thinking to… to go by, and I don't really care about it.
**Chris Marchbanks** 37:24 Right, yeah.
**jmacdonald** 37:26 like, it's, like, going to be a boundary condition where you're like, oh, I thought that the value could never be more than this, and one of the… one of the cases I know that I like to remind myself is scale negative 10
is the smallest rational scale you could ever use, because it gives you one bucket for less than zero, or less than 1, and one bucket for greater than 1. So that's the smallest possible histogram, is two buckets that covers the entire range. It's 1 through infinity on the… on the high side, and it's, you know, 0 through…
one on the low side. But…
But that means that you're admitting that the infinity value falls into your second bucket, which is correct in an upper-inclusive world. So really, the only weird ambiguities are around the, like, subnormal values, which…
Which,
you know, 1P-52 falls into a third bucket under my… and that boundary condition on the bottom is the one that causes you to need 3 buckets for scale… for scale negative 10.
**Otmar Ertl (Dynatrace)** 38:30 Yeah, definitely.
**jmacdonald** 38:31 That's what I don't want.
**Otmar Ertl (Dynatrace)** 38:33 This is actually what the mapping in China is. It's actually just numbering buckets, which
to which at least one of the double precision floating point numbers are mapped to. You know, if there are gaps in the subnormal range.
There are no double precision values for all the buckets there.
And there's a… the smallest buckets, or… which get… could get filled is… is, you know, if you take double min value, or… yes, min value, or a subnormal mean value, you know?
**jmacdonald** 39:11 Yeah, it's like 2 to the negative 10 seconds.
**Otmar Ertl (Dynatrace)** 39:12 Non-negative, the smallest, Positive, double position value.
matched to one bucket, and this bucket gets in my mapping index 1. Yeah, 0 is mapped to 0,
this.
**jmacdonald** 39:29 I see.
**Otmar Ertl (Dynatrace)** 39:31 Yeah, so there's a continuous… numbering, yeah? There are no gaps in between, yeah? Every bucket…
To every bucket, a double precision value can be mapped to.
**jmacdonald** 39:40 Thank you, now I remember this.
Like, I don't think I really understood subnormal values until I encountered this the last time you explained it to me.
But then I learned a lot. So, okay.
Thank you. I'm going to be pushing to standardize, like, by writing supplemental guidelines. This is how you can implement a table lookup algorithm.
I will look for some help from you, Atmar, but I'm willing to do a lot of this, and as you saw, I have a Rust implementation. I'm trying to make a Rust implementation that doesn't do any allocations, so that what I would like to give you is you can have 160 16-bit counters
And if… if you run out of 16-bit counts, you're gonna… you're gonna have your… you're gonna start using 32-bit counters in the same allocation. That's what I'm after, just as a preview, I'm excited about it.
But I'll be working on that.
**Otmar Ertl (Dynatrace)** 40:34 This is also what Dinah is just doing, actually, so…
**jmacdonald** 40:37 Cool.
**Otmar Ertl (Dynatrace)** 40:38 Yeah, it starts with actually one bit. I mean, it has,
Dynamic mode, where it starts with one bit counters, actually, and then always doubles the…
**jmacdonald** 40:50 Huh.
**Otmar Ertl (Dynatrace)** 40:50 You know, for the count.
**jmacdonald** 40:52 Interesting. That's cool. I'm gonna… I'm gonna think about that for a moment, but after the meeting. Thank you so much, Atmar. I really appreciate, you know, just… I'm glad that I had a chance to ask you these questions, and it's, like, one of the greatest things about OpenTelemetry for me, so thank you.
**Chris Marchbanks** 41:09 This was surprisingly relevant, as I soon have to implement exponential.
**jmacdonald** 41:13 There you go. So we'll see you in two weeks, Chris. We'll be back.
**Chris Marchbanks** 41:16 I did actually have one question before you leave. What is the status of, like, the trace flag sampling rate?
Like, is that something I could depend on in, say, a server-side component for, like, customers, is if it's there, I can use that for metrics and things like that. Like, right now, we force people to configure. My head sampling rate is 50% or whatever.
**jmacdonald** 41:39 As an attribute on the span?
**Chris Marchbanks** 41:41 Yeah, yeah, we make people either configure an attribute as a span, but, like, we now have trace date where that information is stored, like, this has been sampled this much.
**jmacdonald** 41:50 Yeah.
**Chris Marchbanks** 41:51 Stable enough to depend on, or not quite yet?
**jmacdonald** 41:53 I don't think that there was ever a stability promise made for this sampling rate as an attribute. That's an old idea. I don't know that anyone has it there, so…
**Chris Marchbanks** 42:03 Sorry, not as an attribute, like, the as the trace state…
piece of information. That's… so that's what Yuan Yuan was here talking about. Yeah.
**jmacdonald** 42:12 slowly inching forward, and we need the SDKs first to adopt the randomness ostracure and promise and set the bit, and then second, we need to upgrade the trace ID ratio-based sampler to do this stuff.
And I've prototyped it in Rust and Go, and Yuan Yuan took my Go prototype and is now trying to push it through the Go SDK. And I'm not pushing the Rust SDK stuff, but… but I could.
We need to make… we need to get all the SDKs to start using TraceState, and that's…
that's been really what we were pushing for in this group, and why Carlos came… like, we need to keep pushing the spec and all the SDKs for that. So if there's an SDK that's important to you, we should start channeling that attention there.
**Chris Marchbanks** 43:01 Okay, that makes sense. I mean, GO's probably most important. And if we see that piece of information there, we can go like, yes, we can use that.
**jmacdonald** 43:11 That's according to our belief, is that we've done all the… we've found all the reasons when we need to know that it's not correct, and we've covered them, so that, like, you can trust the trace date.
If it's present, we think, unless there's a bug. If it's missing, that's where you have to, like, sort of shrug.
**Chris Marchbanks** 43:27 Then we'll just fall back to, is there an attribute, is there… Somebody just confirmed.
**jmacdonald** 43:33 Otherwise, assume it counts for one, is what we do, and then in the, the span to metrics,
component that we were talking about earlier, she has set it to use an attribute to say whether the count is exact, or known, or trusted from a trace date, or whether it originates from guesswork. And that's one way you can do it, is if your counting spans, you're like, this count used trace date, we believe that.
But there's some approximation. This count was, like, made up one values that would be incorrect if it was actually sampled, and there's no information. And then there's this legacy that you're aware of, where there was a practice of using an attribute that you could also fall back on. Plus, there's,
You, you, you mentioned knowing about the probabilistic sampler processor, so, like, there's some conventions there as well.
That's all we have.
**Chris Marchbanks** 44:23 Okay, cool.
**jmacdonald** 44:24 One day we could write a semantic conventions document, but you'll, you'll, you'll understand what, you'll understand at some point. Maybe, maybe you can help.
**Chris Marchbanks** 44:33 Alright, thank you very much.
**jmacdonald** 44:35 Thanks, thank you, Chris. Thank you, Atmar, again. See you in two weeks. Bye.
**Otmar Ertl (Dynatrace)** 44:39 Theo, what?
