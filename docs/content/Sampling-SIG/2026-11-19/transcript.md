SIG: Sampling SIG
Date: 2026-11-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Joshua MacDonald (Microsoft)** 00:38 Good morning.
**Peter Findeisen** 00:42 Good morning!
**Joshua MacDonald (Microsoft)** 00:45 I, I am here. I am glad to see you.
Today is the 19th.
I have, a little bit to report from visiting KubeCon.
And, and it may be not much more than that.
So, what do I have to report from… Kubecon is… We were talking about whether we are ready to stabilize the, trace state probability Sampling specifications.
We think there are at least 3, definitely maybe 4 implementations.
And that is enough to call it stable, Or at least to say it's out of experimental.
So I think that's pretty big news, and I'm here to share it with you.
**Peter Findeisen** 01:41 Yes.
**Joshua MacDonald (Microsoft)** 01:42 Nice.
Buddy? What?
Congratulations. Us.
Usually there's a few more people here. I actually invited some people, Special, but maybe too late.
There's this new, I think we've… oh, hey, David has shown up. Hello, David.
Sometimes this meeting is very small, sometimes it's just a little small. Right now, it's very small.
David is, joining us from Google, and I don't think you've come to this meeting before, but we have a small crew, and we talk about sampling. You and I were speaking about how it's time to think about stabilizing the trace date probability Sampling specifications. I was just relating that to Peter.
And that is actually pretty easy. I think. I can go… I have a couple of things on my to-do list for spec-level stuff.
And I could imagine going in there and sending a PR that says, this is now out of experimental.
And probably don't need to discuss that very much, but David, I was interested. I was about to tell Peter what I learned about policies last week, and Thought maybe, for me, one of the Most promising aspects of our conversations about policies was the potential to I see us build real systems that use collector to SDK feedback to configure sampling.
And, I suspect Peter might object at this point. We have already written some specifications… no, no, no, I don't mean it that way. We have already written some specifications that are how to configure this SDK samplers, or, what the declarative configuration for sampling looks like. And that is… not, I guess that is… that is a fact. And then there's this project coming along that Google's interested in. David, maybe you could tell us a little bit about it, but the idea to have, a widely parallel configuration of many different filters or samplers or rules.
is emerging, and I… and I want to see it fit together with sampling.
**David Ashpole (Google LLC)** 04:10 Yeah, sure, so I can give a brief introduction to telemetry policies, and apology, I have a bit of a cold, so… If you need me to repeat anything, just let me know.
Yeah, so telemetry policies, the idea is… We want to define portable rules for what happens to telemetry.
We want to define it outside of any particular component, so it's not meant to be… tied to an SDK implementation or a collector implementation.
And… they… They're designed to be… they're designed in a way so that it's hard for people to mess up each other's policies, so ideally, they're idempotent.
That's ideally. And, You end up basically defining a whole bunch of these Policies, and they all get merged together into one set.
And they can be enforced.
At various points in your stack, so they should be possible to hand them to SDKs or instrumentation, and have them enforced there, or it should be possible to have… to hand them to a collector, or to some managed service somewhere, and for it to be enforced at those points as well.
So the way that these policies generally look is that they have a matcher, Which is… just a matcher on a piece of OTLP-shaped telemetry.
And then they have some action to take, right?
Which, in the sampler case, is… Whether to sample it or not, right?
**Joshua MacDonald (Microsoft)** 06:03 I've pulled up the OTEP, it may still be up to date. I was looking for… so we see some of these… Field selectors.
And then some matchers. This is the matcher section.
**David Ashpole (Google LLC)** 06:19 that…
**Joshua MacDonald (Microsoft)** 06:19 I could imagine putting Sampling configuration in the same place.
**David Ashpole (Google LLC)** 06:30 Oops, sorry.
**Joshua MacDonald (Microsoft)** 06:31 David, I didn't hear you, actually. What did you say?
**David Ashpole (Google LLC)** 06:33 There's a PR in the OpenTelemetry Proto repo, which is more up-to-date.
**Joshua MacDonald (Microsoft)** 06:40 Sure. I love…
**David Ashpole (Google LLC)** 06:44 Let's see, the thing that I think is maybe most exciting for this group is… I think the consistent probability sampler It's a very good fit.
for policies.
Because… You can apply the same consistent probability sampler two or three times in a pipeline, in theory, and you end up with the same result, right? So that's actually a really important property for, any sort of sampling that is done via policies.
So the…
**Joshua MacDonald (Microsoft)** 07:16 Sampling policy that we've, implemented is an example of one, where you set the probability absolute terms, and then you get… you can apply it more than once.
**David Ashpole (Google LLC)** 07:33 you can also very easily merge these kinds of policies, right? Because… If one policy samples at 10% and another at 50%, the more restrictive one wins.
Right? So, it's very easy for you to have different policies for different… with different matchers, and to easily resolve what should actually happen to… in terms of sampling rates to each particular span as it comes through.
I think the… I'll kind of rehash some of the discussions that Josh and I had at KubeCon, and that… I think the biggest challenge for us right now, and why I'm coming to this group here, is that You can obviously do sampling at a number of different places, and that comes with different, behavior, right? So if you do sampling as part of the actual sampler interface, then you propagate context, and that has an impact downstream.
You could also do sampling and have access to more fields, like whether or not a span was an error.
right after the span has ended, right? Like, as a span processor, you could very easily implement 95% of the probability sampling algorithm there.
Just not propagate context, right?
And then, obviously, a lot of people, what they really want is not span sampling, they want whole trace sampling, and so they… You know, group their spans together via collector pipelines, and then do sampling all the way, on whole traces.
And so… the discussion we had at KubeCon was kind of one… For policies, which one of those Three, do we actually want to support?
Are they the same thing?
And… Which, if we're going to start with one of them, which one should we start with?
And… I'll just state the conclusion we came to, and then I'm happy to answer questions, or I'm sure Josh can maybe add more color, but for now, I think we're gonna… not have them be the same thing. I think it would be confusing for users if they asked for a sampler and it didn't propagate context.
We renamed it to, Span Sampler.
To make room in the future if we needed, to have a trace sampling policy.
That sampled whole traces.
And for now, it will be required to propagate context, so it'll only be actually implementable in SDK samplers.
I think they're… There's an open question, kind of, of whether we… for span Sampling would want to allow a span sampler to Not propagate context if it matches on… A field that's not available.
In span samplers, like the error or something?
But we haven't… for now, the plan is just to start with Basic span sampler definitions.
And try and get that working.
I know, Josh, if you want to add anything from our discussions.
**Joshua MacDonald (Microsoft)** 10:54 Thank you. That, helps me remember some things. I, I, I really was approaching this, from the kind of ecosystem level of… of wanting to see, span Sampling, combined integrated span trace Sampling system that users, many users could benefit from without a great deal of configuration, and so I think… The technology is almost less important than the requirement that there be a simple configuration for users.
Once… when we talk about sampling, there's all kinds of, like.
Ways that people think about configuring rules, and rates, and probabilities, and throughput, and Essentially, what I'm… my… my belief is that Sampling configuration is effectively too complicated for most users, and if we can find solutions that, automatically do good things, that would be ideal, and I've… I'm seeing a sense of… This is a… approach to… Configuring… collection and sampling that is integrated and could be maybe close to what I'm looking for, in the sense of… You could imagine a collector that is given a directive to control sampling It sees its own rates, and then it's able to, like, issue a policy that says, turn down your sampling, everybody, we have too much data coming in.
And… It's true that that all could have been done, with the basic… some of this could have been done with the basic probability sampling, the rule-based stuff that was in OTEP 250, But this… this proposal, I'm sensing, has a lot more, practical solution built in. So, like, having the ability to do filtering integrated with your sampling, I don't know. I'm… I'm actually… now that I'm here talking about it, I'm struggling to identify exactly why I like this, or what is different from You know, filtering can be… can be expressed as sampling.
In some sense. So I'm not sure I have a good answer.
How's that sound, David? I don't have a good answer.
**David Ashpole (Google LLC)** 13:34 there's… I mean, there's one thing that I forgot to say, which is maybe, I don't know if I have a good answer for you either, but the one thing I forgot to say as well is policies are meant to be dynamic, so they're small, and they're served… they're expected to be served over things like op-amp or… Maybe via… maybe via files, but, this is… Maybe you could see this as, at least the sampling portion is being somewhat similar to, like, Jaeger Remote Sampling in Spirit, where we want to define lots of little rules and provide them
**Joshua MacDonald (Microsoft)** 14:12 And that some recipient is going to compile them, in some sense, into the efficient implementation plan that we want.
**David Ashpole (Google LLC)** 14:22 Hmm.
**Joshua MacDonald (Microsoft)** 14:24 So, at some level, what we're just presenting is, at last, OpenTelemetry seems to be getting serious about dynamic configuration… Especially within filters, samplers, and so on. I guess I heard one of the more substantial questions or topics that you have is whether we've ever thought about controlling, the propagation of spans or of context Through a sampling configuration.
I… realize I don't think we've ever done anything like that. I, I'm thinking of, for example, the… Idea that sometimes we want to Record a span.
Know what probability we recorded it with.
Without propagating context, because… simply because we want to record a span.
Simply because a span can represent a distribution of operations, and I can compute a histogram from their latencies after slicing by attributes that I care about.
So there have… I have seen more than once a request to consider whether we could just record spans and not And export them.
Record is usually what we mean in memory, so exporting spans that were unsampled.
Having seen that desire occasionally.
Your question then becomes, can we take these policies and use them to… Configure exporting of spans that were sampled, but were not That… for which there was no context propagation.
And I think the answer is probably yes, I can imagine that, but we don't have any way in the protocol in the OTLP data model to… Present a span.
At least none that's been documented to present a span that was… that has no sampled flag set.
And yet has been exported. It would look like what? It would look like a very old span from OpenTelemetry before we added span flags.
There will be no way to say this didn't have its context exported, so it might be part of a broken trace.
**David Ashpole (Google LLC)** 16:46 I think my… what I was interested in is actually maybe simpler, which is… I feel like the… and… I feel like the classic use case that people want is… I want… Error span sampled at 100%.
And the rest of spans sampled at 10% or something, right? Like, that's, like, the classic… you know, I… I want high-value stuff at a high percent in, you know, And I think the… you know.
with policies.
it's unclear what the best way is to express that. Like, I'd like to be able… I'd love for someone to be able to write you know, policy that says this, right? That says, you know, essentially, sample Non-air spans at 10%.
But today.
If they write… if they implement that as a sampler, they don't have access to whether it's an error or not.
Right.
So it's… it's more… I think the question is more, like.
If someone writes a sampling policy.
And depending on which fields they set, sometimes it propagates the… Sometimes it will propagate.
It's Sampling decision, and sometimes it will always Claim it's sampled, and then basically do, like, mini tail sampling.
like… That seems like… I guess… even ignoring policies. If somebody says today, I want to do 100% of errors and 10% of the rest of spans.
what do we tell them today? Like, do tail-based sampling, use the collector probability sampler.
Am I wrong? This is the thing that everybody says they want?
**Joshua MacDonald (Microsoft)** 18:39 Okay, there's something here. So the idea… Is you can imagine a policy that says We want 10% of spans and 100% of errors.
And it translates into, I'm going to… Attach a span to all my contexts.
10% of the time, I'm going to set the sampled flag, And… when I get to the end of my span life, I will look at its error state.
It's been recorded, so it's in memory, it was attached, there's a real object somewhere.
And then… My policy is telling me if it's an error, keep it. At which point, again, there's not really a spec that says how to write out a spam that was… Well…
**David Ashpole (Google LLC)** 19:29 You view this as.
**Joshua MacDonald (Microsoft)** 19:30 There's nothing wrong.
**David Ashpole (Google LLC)** 19:31 keeping a span, That was actually sampled out, not… you wouldn't… like, the way I would implement this today is, like, sample 100% in the real sampler.
And then do my… essentially implement this policy after the fact as a processor. But you're viewing this as actually, no, your real sampling rate is 10%, but you're deciding to keep some spans That didn't propagate context. Is that what…
**Joshua MacDonald (Microsoft)** 20:00 Something like that.
**David Ashpole (Google LLC)** 20:00 think about it? Okay.
**Joshua MacDonald (Microsoft)** 20:01 I guess so. I'm open to both interpretations.
**David Ashpole (Google LLC)** 20:11 I mean For… for my purposes, with… policies, that would be a nice solution, because… We would just get to say, that… the sampling only applies to head samplers, and then we could describe a span filter that allows through non-recorded spans, or something like that, right? And we could say that… I don't know, by default, you're… non-recorded spans get filtered out, right? Like, we could… And then… that feels like maybe more of an intuitive thing. I guess the question is, would people… If we didn't propagate context, or if for error spans that we keep.
we don't propagate context for those. That seems okay.
Maybe?
**Joshua MacDonald (Microsoft)** 21:10 Well, it's too late to propagate context before you know the error, right?
So, one way of interpreting this scenario is that everything might be traced You get to the end of your error span, Yeah, okay, I said everything might be traced. What I mean is to say there's nothing preventing us from interpreting this as all spans were traced.
But, you know, but except for 10% of them, or errors, we dropped them, breaking the trace propagation, so that you may have propagated context that is now incomplete because you didn't actually record it.
And that… I guess there's nothing necessarily wrong other than you're recording partially complete traces all over the place, and that might bother some people, for legitimate reasons.
So… I liked your… I liked your framing best, actually, David, the one that you just gave, which is, consider this to be 10% sampling with propagation, and a catch-all that's sort of, like.
Filtering and exporting recorded spans.
Knowing that they are exemplars of an operation, that they're basically log records at that point.
Calling out an error, not a… not a trace. Of course, If every child also experiences an error, and also records that trace, you're going to have a trace, even though you didn't try to collect it.
If everybody decides to record that trace ID.
I feel like this is leaving an interesting question.
I know there is an issue in the spec SIG… in the specification repo from years ago that's basically saying, I want a way to export spans that weren't sampled.
I think of this as what they mean.
You can dig that up.
For me, it's always been a recognition that those span events are effectively raw histogram measurements, and I can use them to construct histograms, and various dimensional… Like, breakdowns of the spans, which I've seen be useful.
you know, span to metrics pipeline works very well with this scenario, and you don't need… You don't need to collect traces just to make a good met… a good sort of latency diagram from a spam.
**David Ashpole (Google LLC)** 24:02 the… if… if you… If you were to keep So you record the sampling probability in trace state, right? To say that here's a span, and You know, this span is a representative sample of 1% of the Of lifespans or something, right?
If we keep a bunch of extra ones, Does that mess with your… Histogram, you know.
Aggregation later on, or can we just ignore the… if they come up as either not sampled or non-recorded?
kept anyways. I assume you can exclude them.
**Peter Findeisen** 24:43 Here comes our concept of zero count, which is pretty useful in this case. We discussed this during our last meeting.
So we can use that to mark those spans, and they will simply not count it when metrics are calculated.
**David Ashpole (Google LLC)** 25:02 I see.
**Joshua MacDonald (Microsoft)** 25:03 Yeah, we had… we had… this was actually two weeks ago's conversation, where… There is no… affirmative way to say, I'm recording something that I didn't sample.
Because if you leave off trade, then it looks like it's a legacy span with a count of 1.
So thank you, Peter. Yes, that… that… I was… I was seeing that proposal as well coming out. I've… So that might be… I had earlier in this meeting, I had said, well, you could just turn off the sampled bit. There's a sampled flag in the span as well. Right.
However, I mean, it's part of the trace flags in the span. However, that span flag was not always set either, so there's an old old SDK somewhere that never wrote that bit.
So, so… Having spam flags become… be not exactly reliable suggests maybe that there's a… TraceState setting that you could do to convey the same I would also… argue that potentially… TraceState, I have to think about this a bit more. ZC, the zero count idea, is that everything… I don't… is that ever anything that you propagate?
I don't… I understand it to be something you put on a span to say that this shouldn't count. You could also have a… if you're just looking at spans, you could have a bit mask in the span flags. We have a bunch of those fields left.
like, bit 14 or whatever says, I'm, being recorded, but… You know, don't count me… Or, don't expect me to have part of a trace, because… Because I wasn't like that.
Not coming to a strong opinion right now.
**Peter Findeisen** 26:59 So, originally, our concept of zero count was mostly for collector, not for head sampler, because the head sampler Would never set that, but here is a new use case for it, so… It can be set by the SDK.
**Joshua MacDonald (Microsoft)** 27:19 Do we ever propagate? ZCC?
A zero count.
**Peter Findeisen** 27:25 Well, so, Chris created the issue, so he suggested some specification for that.
So… it's mutually exclusive to have, zero count or threshold, so we would not put threshold in there, and would just put… Zero count, which would be automatically propagated if we decided to to propagate that.
But…
**Joshua MacDonald (Microsoft)** 28:00 Is there a issue that Chris opened?
I bet there is.
**Peter Findeisen** 28:06 Yes, I think it was in the Slack channel.
**Joshua MacDonald (Microsoft)** 28:10 Okay.
I can find that.
Let's just jump over here.
**Peter Findeisen** 28:24 Yes, that's it.
**Joshua MacDonald (Microsoft)** 28:28 All right, well, now, so here's some progress.
Well, this might provide some of the solution, David.
**David Ashpole (Google LLC)** 28:42 Yep.
**Joshua MacDonald (Microsoft)** 28:44 I will have to look at this.
I'm gonna put it back into the notes… Too many tabs are open here, people.
**David Ashpole (Google LLC)** 28:56 Yeah, I think it's… it's very interesting, because… I think it's… It's actually a good solution for the SDK to model it this way, where you export you sample 10%, but have the ability to maybe keep some non-recorded things. It doesn't… Doesn't work as well for… like, if you have a DOM SDK and a policy-aware collector, you'll still want to sample 100% and You know, do your probability Sampling in the collector or something.
but… And obviously, like, the collector has no way of getting access, at least today, to non-recorded spans.
Maybe that could be a thing in the future if we wanted this Filter, or whatever, to be able to preserve Some non-exported spans.
But I could definitely see a future where this this scheme could work within the SDK, or… an SDK working with a collector. So I think that… It gives me a way forward, at least.
And I do think it's safer to propagate it is definitely safer to propagate a context that says, I didn't sample, and then later decide to preserve a span.
than it is to propagate a context that says, I sampled.
Yeah.
**Joshua MacDonald (Microsoft)** 30:27 I agree.
**David Ashpole (Google LLC)** 30:27 So, I… I like that, that framing.
**Joshua MacDonald (Microsoft)** 30:32 Here's the issue, I found it. I… I've… let export… let SDKs export all the spans, regardless of their sampled flag from… the 2000 series, so quite old. There it is.
So, there's something here.
and… I like it. There's something concrete here. The ability to configure spans at export for policy reasons.
Which might use the zero count.
stop sharing so I could go search things without you all watching me, but here we are.
I call this progress.
**David Ashpole (Google LLC)** 31:26 Yep, yep.
**Joshua MacDonald (Microsoft)** 31:28 So, we have some things to think about. Now we can see, Chris's, issue, and maybe we'll take this to either a Slack or, Discuss it in the issue.
I feel like we made progress today.
As you all know, I love it when we can end a meeting, or at least there seems to be nothing more. Thank you for coming, David. This will give us some things to think about. I will, in the next two weeks before the next of these, I will put something… I will read and comment on that issue. I will also put something about, stabilizing or taking out of experimental. Go ahead, David.
**David Ashpole (Google LLC)** 32:15 I was gonna say, are people interested in more topics? I have more sampling-related things. I don't know if this group would find…
**Joshua MacDonald (Microsoft)** 32:22 Band Sampling Policy, let's talk about it.
**David Ashpole (Google LLC)** 32:24 No, that's the same thing.
**Joshua MacDonald (Microsoft)** 32:25 Same, okay.
I… we have more time. Okay. I just get nervous and don't know what to say, so I always try to end the meeting.
**David Ashpole (Google LLC)** 32:32 Okay, that's fine, yeah. Let me find… You told me to bring this to the Sampling SIG a while back, so I'll bring it now, since I'm here.
Sure.
So I wanted to raise the topic of… The… Tracer… So I, I had… Yeah.
I'm just gonna paste everything that I… had drafted and sent to you in Slack, Josh.
**Joshua MacDonald (Microsoft)** 33:14 Okay.
Oh, I remember this now.
**David Ashpole (Google LLC)** 33:18 Oh man, is this… this is way too large.
Okay, so… The context is… I really apologize for just.
I'll clean it up later.
**Joshua MacDonald (Microsoft)** 33:33 Okay.
**David Ashpole (Google LLC)** 33:35 The… the context is… in the… actual span start API.
There's no way to clarify how important a span is.
And so… Right now, if… if you… If you have… there's no, for example, concept of a debug span, right? I don't know if this topic has ever come up before with anyone, but.
**Joshua MacDonald (Microsoft)** 34:00 I know that we've talked a little bit about when a span is sampled out, but it has parentage passing through it, you end up with a grandchild with no grandparent, and that is a perceived weakness that we've talked about. I believe Otmar has raised this a couple times.
**David Ashpole (Google LLC)** 34:20 that… I came about this because I was interested in instrumentation being able to pass some notion of importance to the metrics API, right? So I want to be able to say, here's an instrument, and… it's either opt-in or opt-out, right? So that's what I've added to the metric API, but the question came up.
of… well, should we use levels? Like, should metrics, logs, and traces all have Error, info, warning, debug, trace levels, like logs do.
So that I can say, hey, this span is really important, or this span is not very important at all.
And… My personal conclusion is, no, I don't want them to all have levels.
But I did… it did get me thinking that I think Trace is missing The trace API is missing some knobs.
for… Instrumentation relating the relative importance of spans to each other.
if I want to do cost control today, I kind of have to say, like, hey, this, I'll just control my global sampling rate for this, like, path.
And then… Because everything does parent-based sampling, more or less.
You get fewer whole trees, but there's no way to, like, simplify your trace trees.
In my mind, in an ideal world, if I wanted to cost control, I might reduce I would use the consistent probability sampler, right, because it's awesome, and… But I would also have different spans within a tree sampled at different rates, right? So there might be, like.
some that I would want to sample at, like, 0.001%, because they're really spammy.
and some that I would want to sample most of the time, right? It's like, I would love for, I guess, sampling to… Allow for that kind of thing to exist.
So I was trying to figure out what like, what would the API look like? What's missing from the sampling interface to make that actually feasible?
And yeah, I really value… this was just an idea about a month ago that I shared with Josh, and he said, bring it to the Sampling SIG. But I never… I didn't have the time, but now I'm here, so, I'm sure you guys have thought about this.
And I'd love to hear your thoughts or ideas or, huh? Yeah.
**Otmar Ertl (Dynatrace)** 37:03 isn't this already specified? I mean, it's… The current specification allows to set different sampling rates for every individual span within the trace, so… So we passed.
**Joshua MacDonald (Microsoft)** 37:19 I mean, we can use the… each span can have its own sampler, so yes, I guess on the surface, this is true. What I feel like David's asking is more… and I… I don't… I'm not sure I agree with any of this. I, What is interesting to me is that we have, so far, three signals that we're studying, and they've each taken a different approach to this problem. So, or that's roughly what David is summarizing, is that Logs have this classic info warning error designation, and then… In metrics, we've been debating whether there's an opt-in, opt-out, and I've actually proposed or promoted one approach I like, which is what the Go Collector is doing.
And it has more of a kind of, like.
Simple naming scheme that's… that's not info warning error, it's basic, normal, and detailed.
And so that there's sort of, like, a categorization that can happen of importance.
And then that's trying to make it… Sort of easy to configure.
which you see, because in logs, you have this choice. Do I run with error, or do I run with info or warning? And then there's… that makes the same type of choice in metrics, which is like, do I want a little bit, a lot, or a ton of information?
And… Then, so event and metric… so we have two approaches. Metrics and logs have different approaches. Now we're trying to answer the question for spans. Which should we do? And we'd like there to be consistency.
But, doesn't seem to be. So… If you were to apply what the metrics in the collector does with metrics, you might say, we're going to have some simple names that allow us to put symbolic importance onto these spans, and then at runtime, I can configure what percentage each symbolic category actually samples at, so that I can… instead of having to configure the sampling of 72 different spans, instead I'm able to configure the sampling of 3 different categories of span, maybe, I think is what I… what I'm… what I'm hoping or seeing here.
**Peter Findeisen** 39:38 Well, from my perspective, the ideal solution for SPAN, we can talk about SPAN priorities or something like that, which would, match what is being asked here. And, yes, we can use, probability sampling to filter out those spans that are less interesting, but it has a big… problem. Namely, if we sample out some spans in the middle of the trace, the trace is becoming inconsistent. We are… the parent of the child span.
will be, might not be present at all. So, ideally, the solution would be to make… some spans in the SDK transparent, meaning that They are passing everything up to their parent.
So… Any child of such spanse would see the grandparent as its parent.
I'm not sure if I expressed myself Clearly, but…
**David Ashpole (Google LLC)** 40:54 That's… that's exactly… I completely agree. That's exactly what I think We will have to do, if… to make this work, yeah.
**Otmar Ertl (Dynatrace)** 41:03 This is exactly, I think, what we were already discussing years ago.
Not just the grandparent, but also the number of spans which are in between, right? This was a further extension that you do not just have your grandparent or crank pair, and whatever is next, right? So, also, you have the number of skips between, right, and you… Could be additional information that, you know, at least know, okay, it's below this one.
But there were, like, 2 or 3 spans in between, which were dropped.
**Joshua MacDonald (Microsoft)** 41:43 Yes, I recall that as well.
And I think we've never come up with or thought through the technical requirements that we would… I think, Otmar, your proposal was to put a count of skipped parents, I think, at some point?
But there seems to be a, no solution that we know of here.
**Peter Findeisen** 42:06 Well, my proposal for that would be to keep in trace state, keep the… Span ID, Of the last sampled… ancestor.
If you do this, the… the collector… Some processor in the collector can reconstruct the trace from that.
Which would be consistent.
**David Ashpole (Google LLC)** 42:38 Right, I… I think… I like the idea of counting the skipped ones. I think you could just… You just have to propagate that with the context?
I don't know if it would go in tree state, or…
**Otmar Ertl (Dynatrace)** 42:54 I mean, you can have this on top of what Peter proposed, right? So, I mean, it is actually the minimum, what we need, what Peter proposed, and then In addition, it would be nice to also have the number of skips, right?
**David Ashpole (Google LLC)** 43:07 Yep.
**Joshua MacDonald (Microsoft)** 43:14 Alright, well, now we've definitely covered a topic, two topics, even. I notice we have a new arriver. I want to say hello to Rob.
We're above… we're above 4, that's good.
If you'd like to say hello or introduce an interest, we'd love to hear from you. Glad to see you.
**Robb Kidd (he/him)** 43:31 Sure. As mentioned, my name is Rob. I work at Honeycomb. I work on our tail sampler, refinery, and I help my goldsmith, with the contributed adaptive tail… what are we calling it? Adaptive.
**Joshua MacDonald (Microsoft)** 43:43 Adaptive.
**Robb Kidd (he/him)** 43:44 Yep. In the collector. Sampling is of interest to us. I hear this discussion, and I'm like, I reach for tail Sampling to solve this problem, but I realize not everybody wants to do that.
So I'm… Intrigued by these ideas, and how we can… Make all of these options available somehow.
**Joshua MacDonald (Microsoft)** 44:06 Cool, yeah, thank you for joining. I know we, used to have Kent with us for a long time, and then he stepped away, and Mike, it's hard for him to reach this time, but I,
**Robb Kidd (he/him)** 44:15 That is among the reasons why I'm attending. I don't think I have anything to contribute as far as solutions. It's, this is me engaging to, to… to get involved.
**Joshua MacDonald (Microsoft)** 44:24 Cool.
**Robb Kidd (he/him)** 44:25 Yep.
**Joshua MacDonald (Microsoft)** 44:25 Well, earlier, and you can see the links here, we, David, talked about some new work called Policies, you might want to take a look at that. This is, effort underway. Okay, well, thank you, Rob. Let us know how we can help with Honeycomb and the contributions. I am excited by that.
Yeah, okay, we just covered a topic, it seems like an interesting one that people have thought, but there's nothing active or in flight on this, so if anyone wants to… come up with a great idea and propose something on this, I think we're going to be open to it.
But it, it, it worries me. I haven't thought through it yet, so maybe it's gonna be complicated.
And…
**David Ashpole (Google LLC)** 45:10 Well, it sounds like this was… it sounds like this has been proposed before. Am I wrong, or…
**Joshua MacDonald (Microsoft)** 45:17 I don't remember an actual proposal, I just remember a discussion.
**David Ashpole (Google LLC)** 45:21 Okay.
**Otmar Ertl (Dynatrace)** 45:23 It was not the official proposal, I just brought it on the table, I think, some years ago, but that's it.
**Joshua MacDonald (Microsoft)** 45:32 Maybe it exists. Yeah, I remember, from my own background, a hackathon.
**David Ashpole (Google LLC)** 45:37 That's true.
**Joshua MacDonald (Microsoft)** 45:38 where I tried to do this, and, yeah, I recall… I'm taking some shortcuts. I think I… anyway. Point is, this wasn't easy.
Especially for a hackathon. As I recall, the shortcut was that I was generating IDs for spans that didn't exist, and then there was some, like, list of all your parents by the time you got to the child that was missing its ancestors. So I took a shortcut, but, the idea was to experiment with at least the user experience.
Because I've seen too many spans.
**David Ashpole (Google LLC)** 46:17 I mean, I think we have… We have today, like, a very, very poor version of this, right? Where the… Tracer Configurator exists.
So that you can turn off a tracer entirely, and then it does not propagate context.
It doesn't touch it at all.
Right, so you can basically just be like, yeah, this library doesn't exist anymore.
And so you get that, like, suppression behavior.
And it… I assume that's, like, sort of cost control… like, you want it for that?
But… obviously, like, it's not… it's not very granular, and it's up to users to go and actually do that. So if you write a bunch of very busy instrumentation in a library, then users are forced to turn off the whole thing if they want to exclude it from their tree, right?
**Joshua MacDonald (Microsoft)** 47:16 So then they're gonna have multiple tracers for their different levels of information.
**David Ashpole (Google LLC)** 47:20 Yes, yes, you'll have your debug tracer, it's lovely.
So, and just to circle back, Josh, I completely agree that users need easy, high-level knobs.
And so, even for metrics, like, basic, detailed, like, I love that.
I see it as being built on top of.
Some of these lower-level primitives.
I think the… the interesting question for me Right? Is… generally speaking, I feel like your sampling rate is already… a… A relatively good user-facing knob for turning up or for turning down.
verbosity. Like, if I set it to a bigger number, I should get more, and if I set it to a lower number, I should get less.
I think the, like, maybe interesting or new piece of what I had in mind was… If the instrumentation could provide a hint.
When starting a span that says, Sampling me it.
Half of whatever the normal sampling rate is, or a quarter of whatever the normal sampling rate is.
Then a user that changes their overall sampling rate.
Could still get proportionally the same traces.
But… You would… it would be… it would be kind of the equivalent of saying this is a debug span, right? It would be this span is sampled at a proportionally lower rate than other spans.
in the tree or in the application. So that was one of the interesting ideas to throw out, but I guess for me, from an instrumentation perspective, or, like, from an API perspective.
I don't know necessarily what… we… I think we could do, like, debug spans.
And then it would be up to the sampler to interpret what that actually means. So you would have, like, a debug sampling rate, maybe, configured?
here's, here's the rate I want.
you know, the other ones, and here's the rate I want the debug ones at, right? So I think… there's definitely interesting ways we could make this work. But I like the idea of using sampling rate As the knob.
for turning up or turning down individual spans. It feels better than the all-or-nothing we have today, certainly from, like, Tracer, Configurator.
**Joshua MacDonald (Microsoft)** 49:54 Yeah, I'm picking up on this. I like the idea of a, well, a symbolic label that is essentially saying, I'm going to… well, either automatically or manually, I'm going to put a special kind of, like, adjustment For all spans of this category, So that I can… Have a simple way to control many spans.
And then, I could imagine a, Like a, let's say, a fancy tail sampler that, is looking at all the spans you have coming in and saying, well.
We're gonna have to sample quite a bit in order to meet our budget.
But rather than sampling flat at 5% to meet our budget, what we're going to do is we're going to set a, 1% on all the noisiest spans.
Which is the noisy category, or, you know, the verbose or the debug category.
It gives you a way to kind of think in terms of your groups. So I have… if I have 3 or 4 groups of span with different levels of… of information content, then my sampler could adjust those four knobs instead of trying to adjust 72 or whatever the number of spans actually is. Giving you just some sort of symbolic Configuration ease.
**Robb Kidd (he/him)** 51:18 Is the… Question, because I'm not yet fully conversant in all of the options for the tail sampling that exists in the hotel, toolkit.
Is there a tail sampler that will restitch the tree to… the trace tree, if it decides to… Pluck out interstitial spans that have descendants?
**Joshua MacDonald (Microsoft)** 51:39 Yeah, I think none of this really exists right now.
**Robb Kidd (he/him)** 51:41 Okay.
Because I can, I have seen patterns, for instance, in the, in the previous bullet. Consider a case where A user wants 100% of errors sampled and 10% of spans.
That is possible with the adaptive tail sampler today, as long as you substitute spans for traces, where… A trace that contains an error can… all traces that contain a span that has an error can be kept, and then traces that don't contain errors, you get 10% of traces. But… Sniffin' out.
Pruning pieces of the… of the… trace tree.
Actually, leaves can be pruned. It's that whole continuation of some descendant that you want to keep. You want to get rid of the interstitial stuff, is… That doesn't exist yet.
That I'm aware of.
**Joshua MacDonald (Microsoft)** 52:37 Well, we have covered an interesting topic. Sounds to me like we could all Well, think about it a little bit.
Would you like to see a solution here? David is interested. If anyone here comes up with a good idea, we should share it.
Come maybe 2 weeks from now.
I feel like that that's an appropriate place to leave that conversation, unless anyone has more. I like it.
I haven't thought through the, like, scope of effort required yet.
**Robb Kidd (he/him)** 53:09 This is one of those that fall into my, like, I understand why you want that. Yeah. It is reasonable for you to want that. Hmm.
**Joshua MacDonald (Microsoft)** 53:16 Yeah, and the hackathon that I referred to was from, I think, 2017, so it's not moving fast, this idea.
But thank you, David, for joining us.
**David Ashpole (Google LLC)** 53:31 You're welcome.
**Joshua MacDonald (Microsoft)** 53:32 I, I… I… it would be cool if, if metrics and Traces shared some common Something common, but they're different. Never mind.
Let's resume this conversation. In two weeks, perhaps, we'll have more to say, or we won't, in which case, maybe it'll be another 10 years.
**Peter Findeisen** 53:55 Okay.
**Joshua MacDonald (Microsoft)** 53:56 Thank you all, see you in 2 weeks.
**Peter Findeisen** 53:59 Thank you. Bye.
**Otmar Ertl (Dynatrace)** 54:01 Good, flat.
**David Ashpole (Google LLC)** 54:03 Bye.
**Joshua MacDonald (Microsoft)** 54:11 I'm still here, I'm looking at the chat before I hang up.
Thank you, David. See you soon.
