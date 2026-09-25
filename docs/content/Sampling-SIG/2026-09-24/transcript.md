SIG: Sampling SIG
Date: 2026-09-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Joshua MacDonald (Microsoft)** 01:54 Hello.
Good to see you all. I… We fixed our Zoom problem. Hooray!
So, Peter, last week, you and I spoke for a while, and then I hung up, and you hung up, and then we all spoke again for a while. No big deal. I might… I think I'm expecting, Mike Goldberg.
Mike Goldsmith, excuse me, Mike Goldsmith from Honeycomb.
today.
otherwise, I have no agenda, and, it's good to see you all.
My usual question is, when are we going to have a feedback loop with a server that sells… sends Sampling configuration to SDKs?
I'll just lead off right there with my wish list.
I said I'd project, didn't I? There's nothing on the agenda. Not yet.
And I just pinged Mike, so he might join us.
Otherwise, we could use this time.
To raise any topics. I apologize, I always feel this, like, little bit of guilt every week when this meeting comes along, when I say I have nothing to say. I am involved in some work on the hotel sampling with my .NET team, but it is veering off into places where I can't share it yet.
At least I'm building up some knowledge base there. They're deep in the .NET runtime, it's complicated.
**Yuanyuan Zhao** 03:46 I have an update.
**Joshua MacDonald (Microsoft)** 03:48 Yes, please.
**Yuanyuan Zhao** 03:49 I have left Data as of last week, so I am now joining as an independent contributor, and contributing purely out of passion.
**Joshua MacDonald (Microsoft)** 04:02 Very good.
**Yuanyuan Zhao** 04:02 There's no obligation from work.
**Joshua MacDonald (Microsoft)** 04:07 Maybe you'd like to begin, tinkering with a, collector processor that Obserbs the stream of data and produces sampling instructions.
**Yuanyuan Zhao** 04:18 Yeah, that's a good idea. Actually, I am looking into expand, my, open source contribution a bit.
**Joshua MacDonald (Microsoft)** 04:31 Could be that, the assignment could be, do what Datadog Agent did.
**Yuanyuan Zhao** 04:35 Well, we could probably, that thing is, has been there for a while, right? And, we can do a state-of-art thing.
**Joshua MacDonald (Microsoft)** 04:50 And just to… since we're here, Peter, you have contributed a declarative configuration for sampling that's, like, ahead of us all, I think. And if we were to do this dream I'm dreaming up, we would use your configuration specification.
**Peter Findeisen** 05:18 Oh, I was muted, sorry.
Okay, yes, yes, so, the work that was done For the configuration, it was proposing just a few fundamental building blocks that would allow us to build more complex policies.
as far as I know, that's not been, yet reflected in, declarative config work, but I believe it should be relatively easy to do, except for the predicates that… that… This is… Something that needs to be worked on a little bit more.
**Joshua MacDonald (Microsoft)** 06:02 I was under the impression that we had done a little more than that. Maybe I'm… That something was already merged into the declarative specification protocol.
Now I have to find.
**Peter Findeisen** 06:16 Yes… well, okay, some of the… yes, it's not a complete work, though.
Yes, I… I don't remember exactly what the status is. Yeah, you're right.
**Joshua MacDonald (Microsoft)** 06:31 Never easy to find these repos. What's the name of their repo?
I'm looking in a different browser window, so you can't see me fumbling for things that I can't find.
Declarative… Configure… okay, so it's just OpenTelemetry configuration.
Web searches can't find me. Okay, so… So, where are we then? We are… Here… And, I've… There's an example that has the kitchen sink in it, which is how I always find, well, maybe not.
Sampler, parent base, root, always on. This is what I'm thinking of.
**Peter Findeisen** 07:23 Yeah, that's the old stuff.
**Joshua MacDonald (Microsoft)** 07:24 That's the old stuff.
Didn't we… didn't we… didn't we have anything in there?
Hmm.
So this is the JSON schema, which nobody can read.
Yeah, so Sampler… As always off, always on, always record. Experimental, composable.
Experimental Jaeger.
Experimental probability.
Trace ID ratio based.
So yeah, some… Some stuff appeared.
Experimental, composable, always off.
Did we actually have a composable always-off?
**Peter Findeisen** 08:17 Yeah, we have to have it, yeah.
**Joshua MacDonald (Microsoft)** 08:20 Okay.
So here would be… anyway, this is the stuff.
I was imagining.
This is if we have an SDK that implements this.
And, processor, for example, that could produce this, then maybe we could have this dream of a feedback loop between the collector and the SDK, which, again, is, roughly speaking.
what the Datadog agent was doing.
I just thought I would share that vision.
Let's put this in there.
**Yuanyuan Zhao** 08:55 The, the, the first, Datadoc, like, agent, control sampling, so it actually was a feedback loop, that… returns the new configuration in response to an export from the SDK. So it's basically piggyback.
on that.
**Joshua MacDonald (Microsoft)** 09:20 Yeah, that will be a little bit of an extra lift in OTEL. I could imagine it happening, so you would have maybe an extension for the receiver that's like a, I am the type of extension that can inject responses.
And the trailing… and the HTTP trailers, for example, and then… And then your sampler.
looks for the same extension to say, I want to convey information to my receivers. Isn't because it's hard to propagate information backwards?
**Yuanyuan Zhao** 09:50 Perfect.
Because you need, right, you need a way, right, for the agent and the SDK to communicate, but if it's purely from configuration files, they could… agent and SDK could be in different containers, so there's a natural wall.
in between them, right? You can't guarantee them what doesn't exist, because it depends on how user… Configure the connector, and so that's… There needs to be some shared channel that, that is there regardless.
Of how the isolation the compute isolation is configured.
Yeah, those are, like, some of the detailed things we need to consider. I was actually just thinking out loud, since you mentioned this, but I think there are lots of, nuances that needs to be considered.
**Joshua MacDonald (Microsoft)** 10:56 Right, that's a good point. So I remember looking at the Datadog agent, and it responds directly to the SDK, so that's an easy way to do it. You're saying it doesn't require a new network access.
The, jaeger remote goes through a different port, at the very least.
And… I… I recognize that my container networking knowledge is not enough, so I could imagine using a separate port on the same, like.
Post, and then maybe your firewall will let you through, but… The, the thing I just imagined with, the collector has these extensions.
The sort of sidestep I can imagine is to have an extension that both the sampler and the receiver are talking to, and the receiver just says, I'm about to respond to this connection, and, you know, do you have any sampling instructions for me? And then the processor could inject them into the extension, and the receiver would pull them out of the extension.
Suppose we would need an SDK that fully respects the declarative configuration as one of the first steps, and that's, its own major project, I'm sure.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 12:08 Yeah, I do think we could also get fairly far with… like, if we… if Jaeger could accept the… if we could have the Jaeger shims and all of that.
work well with the spec? Like, that would get us pretty far on this for everyone who's using Jaeger today.
Might be… that's a place we've looked at a little bit, just because we happen to be using.
Jaeger Remote Config a lot internally.
And there's not much appetite for moving off of it, to be honest.
**Joshua MacDonald (Microsoft)** 12:38 Cool. That's… that's actually good information. So, I don't have any real problems. I guess I have two problems with the Diego remotes, actually.
But they're not major. So, the first one, I think, is the technical one that people in this room know about. Like, they're the major rate limiter mechanism in Jaeger Remote, which is, like, one of its selling points is token bucket-based, it has no probability foundation.
So… you will… you will need to do some change in there to get to the place where you're reporting your sampling probabilities. Now, I've had this conversation with Yuri many years ago, and maybe more than once, where the question is, like, why is it so hard to get sampling information out of Jaeger?
And the response has always been sort of like, you're asking for something that we don't need, why are we doing this? The server controls Sampling.
And, why should the client then send its sampling instruction? And I never had a good, great answer to that.
But… So you could imagine the Jaeger… system returning, like, a unique identifier, like an opaque policy name, or a policy identifier, which is to say that this is the policy you're using right now. If you're not going to self-sell me my sampling probability, at least tell me my policy.
Doesn't work for… That doesn't work for situations where the… SDK controls the threshold.
Yeah.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 14:19 I'll take a look more at the bucket ones. Like, a lot of the times we just use this as, like, there's an internal config, and it has some percentage, so it's actually fairly easy for our internal cases to map.
**Joshua MacDonald (Microsoft)** 14:28 Yeah, like, there's some of the Jaeger…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 14:30 a bit more, and see if we…
**Joshua MacDonald (Microsoft)** 14:31 work and some don't, I guess. And then, I think the plan would be to replace the ones that don't work with just equivalents that use Probability instead.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 14:42 Yeah.
**Joshua MacDonald (Microsoft)** 14:43 So I guess that's the first… part of this.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 14:46 The other thing that I've been looking at recently is what is an appropriate rate to send back to the SDK?
As, like, I haven't found that much that is like, yes, you should be using… A tenth of a percent, you should be using 5%, like… So that's one area I've been looking at. I don't know if you all have resources or significant thoughts in that space of, like, once this is all set up, how do we actually calculate what a good SDK sampling rate is.
**Joshua MacDonald (Microsoft)** 15:19 Yeah, that is actually where some of the interesting stuff comes out, and I think that's where freedom to experiment with algorithms would be nice.
I have, you maybe know, like, like, part of… one of my objectives is always to just, like, balance, like, I don't care what the spans are, but I want the same number of each kind.
And I want 100 per second or whatever, like, that's the sort of… And there's no right answer to that. There's sort of, like, a gradient descent, or some sort of, like.
You know, something like that, a little bit, approximate.
So I would imagine, something along those lines.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 15:58 Yeah.
**Joshua MacDonald (Microsoft)** 15:59 The other issue I have with Jaeger is not structural, or… it's just that it predates OpenTelemetry by so long.
that… It just doesn't resemble the OpenTelemetry terminology very well, and that's a minor, honestly, but it has concept of an operation, and like, how do you map that?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 16:21 Yeah, and that's… I mean, that's where we are still using it, and no one has appetite to change it, is it was… it's been used for a decade.
**Joshua MacDonald (Microsoft)** 16:28 Yeah, so, like, we should just write the specs so that it's, like, part of… this is what… I don't know, I always wanted Yuri to do a little bit more of this, but never… here we are.
Yeah, if you… Chris, since you seem to have the experience here, like, this… it is an embarrassment to me that we are 6 years into OpenTelemetry, and we are still… you know, Jaeger Remote is still the dominant technology, so there's a topic for us.
So, so I guess I could imagine extending it, let's just say, never mind replacing it, extending it with the work of OCTEP 235, so to get threshold information in there. And then, I guess, maybe just, like… if we had semantic conventions that were part of the tracing repository, or the specification saying, to translate your OpenTelemetry concepts into Jaeger remote concepts, here's how you do it, and just, never mind, it's fine. Like that.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 17:26 Like, I think that's a fairly pragmatic approach, just for…
**Joshua MacDonald (Microsoft)** 17:31 Okay, so we're not inventing a new SDK. Well, anyway, Peter, that's sort of what we're up against, so for our very nice and neat declarative configuration, is that the world is still using Jaeger Remote, and we still don't have a solution for Jaeger Remote that does probability.
Well… At least we have talked about it.
I'm encouraged, Chris, to hear you talking about that as well. And Yuanuan, there's… maybe there's an opportunity here, if you're interested to… to fiddle around a little bit.
**Yuanyuan Zhao** 18:05 Sure.
**Joshua MacDonald (Microsoft)** 18:06 maybe there's a brute force or, like, a quick and dirty solution here, where you just use Jaeger Remote as the SDK, get something working, and then we can… envision the future of, like, if there's something that needs to be cleaned up, or… honestly, I doubt the users really actually care, and that's where I… my hypothesis for this whole time, is that users come in and say, I want configurable sampling.
and you give it to them, and they're like, no, no, no, I just want, like, low-cost sampling, or sampling that I don't have to think about. I just don't think that users really care to go in and touch these Jaeger remote rules, and so… maybe the evolution of this is that we… users don't think about Jaeger Remote, that they just have a sampler that… Sampling system that works, and they don't configure the Jaeger instructions themselves anyway.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 18:57 Yeah, I would love to see that. That's kind of, yeah, that's, I guess, where I was going a little bit with the, like… how can we calculate what, like, appropriate head sampling rates are? I've been thinking very much multi-stage of, like, here's an appropriate head sampling rate that we can ideally push to an SDK level, but even a collector level gets you pretty far.
**Joshua MacDonald (Microsoft)** 19:16 Yeah, I've been…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 19:16 Tail sample for… for… to cut it down further,
**Joshua MacDonald (Microsoft)** 19:22 Right, there's a balancing act where I was… like, you won't get everything if you do heavy, heavy sampling on this, on the Tracer, like, SDK side.
But you also can't, you… because… because head sampling, you know, if you want a coherent full trace, you just have to, like, flip coins, and you're never gonna, like, have that crystal ball or trace everything, so…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 19:46 Sending everything is too expensive.
**Joshua MacDonald (Microsoft)** 19:47 Telling people 10% sampling is… like, let's just have the SDK pay 10% of its normal full cost, and then we'll tail sample the rest. And that's a sort of, like, striking a balance between, you know, cost of unnecessary tracing with you know, the adjusted risk of loss, or something like that.
And then you go and you do something fancy. I still think… That we might… find a situation where, you know, 10% is a good number for most of your operations, but then there'll be a long tail of very rare operations, or a heavy hitter that's, like, slamming out all the operations, and that's where I want to say, on average, let's do 10% sampling, but it might… might end up being, I want 1% for my heavy op, and, like, 100% for my rare ops, and 10% in the middle somewhere. That's the sort of adjustment I could imagine wanting.
I'm not sure how to do it.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 20:56 I've had pretty good luck with, like, I mean, effectively, like, log transforms, or various other types of power transforms. Pick your poison. That seems to work fairly well for splitting that up.
Which, like, that's what Honeycomb… I guess, or Adaptive… what is it, the Adaptive thing does now? I think they use log.
**Joshua MacDonald (Microsoft)** 21:20 The power of logarithms.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 21:24 Right.
**Joshua MacDonald (Microsoft)** 21:26 Well, this has been a nice, free conversation. I… feel that it is important that we remind ourselves where the, where the North Star is.
Yeah, so I'm glad to hear that, Chris, both you and Yuanyuan are thinking about this. I am, of course, still thinking about it, but I really can't commit much other than to steer my .NET team and, As you all know, I'm working on OTel Arrow, Dataflow Engine. This is, some pretty major deliverables are ahead of us, and Sampling is not on the short-term list, but, in a, you know, 6 months to 12 months, I think.
There will be more than one choice in collector-like technologies, and then I will have more motivation to work on the server side of this type of story.
not to disrespect the Go Collector, honestly, it's fine code, but the power of data fusion and Arrow and, the compute availability when you get down to the hardware a little bit more, is amazing, so… it's coming, and it's not meant to unseat the Go Collector, so I would be very enthusiastic about seeing this happen in the Go Collector, because it's really easy to rewrite stuff in Rust, honestly, and let's get something that works great.
**Yuanyuan Zhao** 22:59 Inc.
**Joshua MacDonald (Microsoft)** 22:59 That's a…
**Yuanyuan Zhao** 23:00 We can't…
**Joshua MacDonald (Microsoft)** 23:01 tour.
**Yuanyuan Zhao** 23:02 Okay. So we can, take a two-step approach on this one, right? The first two… establish the way of sending anything into the SDK without recurring them from startup. That's, like, some major planning that needs to happen there. And then the second thing is a collector that can decide What is that thing we want to send over?
This other…
**Joshua MacDonald (Microsoft)** 23:31 That's coming up, right?
**Yuanyuan Zhao** 23:32 major steps that I can think of. Absolutely.
**Joshua MacDonald (Microsoft)** 23:35 thing is to connect a Jaeger remote with a collector processor, or something along those lines.
**Yuanyuan Zhao** 23:41 Yeah.
**Joshua MacDonald (Microsoft)** 23:42 And it could be a collector extension that talks to both a sampler and a… Like, maybe… here's an idea. We want to integrate with either the tail-based sampler or the adaptive tail sampler, or both. We'll create an extension, which is the Jaeger feedback mechanism.
And… it opens a port on the same host network that's, like, I'm the port 8001 Jaeger remote.
And all the SDKs that are talking to this collector will then know to talk to the same port.
So then you've connected the Jaeger remote with the port that's an extension, and then the samplers both talk to that extension, and the samplers do their job independently. They periodically, let's say every 10 seconds, they compute some sort of, like.
nudge, we'll call it. Like, I am getting too many of this type of span, and not enough of that type of span. I want to rejigger the relationships, I'm gonna change this and that, and that, and everything else stays the same.
And then it goes to the extension, the extension then is advertising on that port, and then SDKs will eventually get the instructions, and now we're feeding back. It's through an extension.
that… I was… I was… I'm imagining just opens the port.
So it's not talking to any of the receivers. The receivers… And the… this is a difference from… from Datadog, but this is how Jaeger works. So the extension has the port, the SDKs talk to the extension, and then the sampling plugins talk to the extension. And there's some sort of language or interface between the extension and the samplers to say what they want to change.
That would be a cool project, because then it would work for all the… all the samplers.
**Yuanyuan Zhao** 25:26 Right?
**Joshua MacDonald (Microsoft)** 25:29 Cool vision. I mean, I don't know, I just said it. Very cool. Idea is to experiment with a collector extension that… Advertise this on port… N for Jaeger Remote Sampler.
Talks to the collector… Sampling processors, which… Give it feedback.
I mean, that's the sketch.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 26:04 And I think, like, yeah, I agree with this vision, like, we're working slowly towards it, just, it's a long-term vision. There's a lot of other stuff to be working on, too, as you're familiar with.
But yeah.
**Joshua MacDonald (Microsoft)** 26:14 Well, I think that's an acceptable place to leave it, if we are comfortable with this. Yuanuan, I am glad to consult on this, if you'd like to hear any more on it, since you seem interested, and Chris, I'm glad to hear about it. Let's keep talking, maybe two weeks from now.
**Yuanyuan Zhao** 26:31 Yeah, we can sync up on Slack.
**Joshua MacDonald (Microsoft)** 26:35 Yes.
**Yuanyuan Zhao** 26:35 Okay.
**Joshua MacDonald (Microsoft)** 26:37 Okay, well, thank you all. I think we did it.
Another meeting. See you in two weeks. Cheers.
**Yuanyuan Zhao** 26:44 The guest didn't show up, right?
**Joshua MacDonald (Microsoft)** 26:47 Yes.
**Yuanyuan Zhao** 26:47 Okay.
**Joshua MacDonald (Microsoft)** 26:49 Right.
I will… I'll see you in two weeks.
**Peter Findeisen** 26:52 Yes. Bye. Bye.
