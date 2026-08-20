SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-08-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Igor Kiselev** 00:30 Alrighty, luck.
**Zach Montoya** 00:38 Hello.
Alright, I can get started, since we are a couple minutes… Past the hour. Let me share my screen.
Alright… So, I guess first… first off, do we have any topics in particular you guys wanted to… Discuss.
Besides our regular agenda?
Alright, no worries. We can just get started on just the regular agenda we have. Looks like we have a bunch of pull requests. I'm actually going to just go to the view that excludes the renovate ones, so all the auto-updates.
From last week, there's a couple new ones. There's doing the trace contents propagation over Postgres, which I believe is… I'm not sure if this was the SQL comment or not.
Okay.
I see, okay, so this one was actually… I think we prepared a separate, a separate query.
So as to not affect the, any caching. So, this is up, I think it's… the design is to send an additional requests before Doing the actual traced one, so we, a lot of the times we'll end up with two individual calls to the database rather than one, but at least then we have set the… trace parent to do correlation. So, definitely opt-in.
So we can take a look at that offline.
We have a shared open source scorecard.
We'll take a look at that later.
Mask OTLP headers and named bug logs. This is actually a pretty good change, because there could be sensitive API keys and stuff.
Yeah. Okay… And then… some… test stabilization. Okay, so nothing too crazy in the past week, but… While we're here, was there any PRs that you guys wanted to…
**Eftiquar** 04:25 There was one, Paul, let me… Actually, I reviewed it yesterday.
The one that Pyotr, requested.
some sync up from Datalog, I'm trying to look up.
**Zach Montoya** 04:39 Oh, this one, the update native?
**Eftiquar** 04:42 Here.
**Zach Montoya** 04:43 Okay.
Yeah, I actually haven't looked at this one yet.
**Eftiquar** 04:47 Yeah… 3… 5355.
**Zach Montoya** 04:50 Yes, yes, I have it pulled up right now.
**Eftiquar** 04:55 Yeah, so I… looked at it, I've… I've found that there's… there are some bugs and issues, but more importantly, probably there are quite a few things that can be rolled back. We don't need that arbitrary instrumentation rule, the wildcard matching, and refactoring around JIT, because It is not giving us any value add, for example, arbitrary method tracing. OTEL does not have a feature that needs it, and it complicates the pre-existing path unnecessarily.
So I have detail as to what are the issues with that wildcard matching thing. I have also looked at the multi-byte-to-wide care mechanism that is used for generic string conversion, and I found an issue with it. So it is a real bug that needs to be fixed. But overall, bulk of the changes, they need to be rolled back, because they are not consumed, and they are adding to the complexity.
**Zach Montoya** 05:49 Okay, so, sorry, is it… How many of the changes?
Yeah, I guess… So is it, like, the entirety of the changes that you're suggesting we roll back, or only just a subset of them?
**Eftiquar** 06:05 a subset of them, but bulk of the changes will be rolled back. That cancellation and the wildcard conversion, that stays. Refactoring of rigid module, that is not needed. Wildcard support is not needed. Number one, it is not consumed, and number two, its semantics are confusing and Buggy.
**Zach Montoya** 06:24 Okay.
**Eftiquar** 06:25 not coherent. So I have put in why it is not coherent and why… what is the issue. But basically, this TR does not add as much of a value add as much of the changes and the culture, so… Yeah. Strong pushback.
**Zach Montoya** 06:40 Okay, yeah, that… I think that's really good feedback, and I'm… I'll take a look at changing that as well, but…
**Eftiquar** 06:48 myth.
**Zach Montoya** 06:48 Yeah, I'm… I'm fine with us, you know, only porting a subset. I think… I think it's good still to, that this is actually just raised so that we can do tried to update incrementally, and then we only include the relevant parts. So, yeah, I think that's really great feedback, and I'll take a look as well, and then we can just, If we're all on the same page on that, then we can just roll back some of those commits.
**Eftiquar** 07:15 Yeah, of course, yeah, I'll look for your comments, and we can take it from there.
**Zach Montoya** 07:19 Okay.
**Eftiquar** 07:21 Thank you for.
**Zach Montoya** 07:25 Alright, any other PRs at the moment?
Alright, let's, go on to issues, Is process-wide… oh, I think you were talking about this maybe last week, or we don't have, like, Strong, semantics for how we update, like, the settings and… Continuous profiling.
I see, okay. Yeah, this will require… A good review later.
**Eftiquar** 08:04 Yeah, it's quite verbose, but I just wanted to know if, like.
do we need… do we need SIG approval? What is the approval process? Because this is definitely a non-trivial change. The semantics of how sampling works, that is not being changed, but how it is configured, how we can dynamically start and stop, how OPAMP can… alter the behavior of all that stuff, right? Because existing model of sampler is very simple, it just boots up during start and continues to work.
Now, it can boot up and stay silent, and then Opam signal will ask it to, okay, now start sampling memory. Okay, now, stop sampling memory. So, you see, it's a lot of dynamic churn that the sampler is not designed for, and plus, in the .NET framework world, app domains arrive and disappear, so who owns the exporter?
All those complications.
And the dynamic behavior. That is why there is so much of churn, but… Yeah, I just want to make sure that we are advertising what we intend to do, and if there are any procedural things that I need to follow before we actually commit.
**Igor Kiselev** 09:15 I agree.
By the way, it's interesting, how ZAT is connected with what we discussed some time back about, Conflictor of domain.
When we talked about config per up domain, we said that we probably need to modify it some way, but it's not necessary to do right now, because it's hard to make it different, configure different applications. Here we have another ugly thing to visit, because with a pump.
It becomes much easier to update a config in different subdomains in a different way.
And our, snapshot mechanic is shared per entire application. That's why a pretty big section from the car's notes is about, how we govern it, and yeah, my personal feedback was with Optical. Yes, we can probably do it, better in future for different subdomains, but I'm not sure if we need it or not. Updomains is already a legacy thing.
But it's pretty great that he defines it, okay, let's say that one of the main is governed, and we will just ignore everything else until that first subdomain is not unloaded, also.
So, it's… VART… On the surface of how we instrument it, but unfortunately, it requires work.
**Zach Montoya** 10:41 Yeah, I'm thinking maybe even a first step here is, in our docs, to outline we… I haven't looked at these in a while, but to document our design of how we're gonna handle how we handle multiple app domains, how we handle configuration, and basically just set up a ground… a ground truth there, a shared truth, and then from there, maybe we can, dive into the, like, how OpAmp… how we expect to handle op-amp. So, yeah, maybe… maybe we first start with some Markdown files to To basically codify what we want to do, and then… and that can also be a great place to have feedback, too, like, on a PR. I think that might be effective.
Because we'll have to do… if we don't already have configuration of how we're, like… oh, we have config, maybe these are just flags, though.
**Eftiquar** 11:34 So that… okay, so the design, that is why it is so detailed. It does outline what happens if you bootstrap with no config, and then opam signal arrives later on, and all that thing.
**Zach Montoya** 11:46 Yeah, so maybe… yeah, maybe what that can… maybe we can do for that is start just, like, a separate Markdown file that discusses how we want to do the, op-amp updates before we even do, maybe, profiling, and then… And then that way we can just have suggestions, feedback, and then that can make it into a… A shared doc here.
**Eftiquar** 12:10 Yeah, so there are two things here.
the OPAMP semantics, basically listen to OPAMP signals and build the config settings. That is the managed site's job. It understands what OPAMP is, it interprets the fields from the OPAMP, and then the profiler is actually a slave to that.
Profiler just needs to expose an ability to dynamically alter its behavior and ability to start and stop sampling, meaning Profiler is totally unaware that it is OPAMP that's sending me these signals. So that's why the first recommendation was to split the original… this basically came out of a PR from Yoini.
Where he had done initial work. So, I propose that we split this horizontally, and let Profiler first design its sampling machinery that is dynamic.
And it is totally shielded from OPAMP semantics, so the horizontal split was like that. And then the managed layer, which owns, OPAMP, That manipulates the underlying profiler. So, profiler, changes, they are totally insulated from what are the OPAM semantics, how we merge different signals, like, you have existing config, and then OPAM changes one bit.
So we merge that, and Profiler is always presented a full config for all the sampling and memory. It does not interpret those, it just executes those.
So, that's why the two were split. So what we could do is, I can parallelly start implementing the native side, and the managed side, OPAM signaling, and on, that can evolve, because that is the front end, and that's where we decide what happens when An abdomen unloads, then which configuration prevails, and all those things. So that is the complexity.
division.
Does that, make sense?
**Zach Montoya** 14:01 Yeah, yeah, I think it would be… that sounds good to develop the, sort of, profiling contract separately, and we can start there.
**Eftiquar** 14:08 Yeah.
Because regardless of whether it's OPAMP or anything, the profiler needs to… support the dynamic activation and pause and abort, etc, etc. That machinery can build parallel. And the top layer thing, that will evolve, we'll have more details on how the managed side looks at OPAMP and how it behaves, How it responds to the changes.
Yeah, so… So you want me to create some mockup documents in that docs folder?
No.
**Zach Montoya** 14:41 Yeah…
**Eftiquar** 14:42 That's your recommendation.
**Zach Montoya** 14:43 Yeah, that would be my suggestion, that way… because I think… I don't think there's any pushback for establishing the contract, so I think, it'd be easier to, discuss it over a PR, that way it's very clear, like, we can… Update wording, change things. Yeah, I would say let's do that.
**Eftiquar** 15:07 Sounds good. Thank you.
**Zach Montoya** 15:11 Igor, did you want to add something? I saw that you came up mute.
**Igor Kiselev** 15:14 No, no.
**Zach Montoya** 15:16 Okay.
Alright, let's see, let me just say… Suggests that we… Sorry.
So let's get to the phone, and I'm gonna do the meeting… Stockholm.
Oh my gosh, it's so hard to type.
Right.
Alright, I think that was the only issue we had.
So… let's see, what else? Discussion… no… Anything on this milestone?
Okay, and then I guess the last thing is the project board.
I think… I don't… I don't think there's any updates here… Feel free to add anything if… It's not already covered.
Yeah, I'm… I think we're pretty good on updates for today.
Cool.
Yeah, I guess any other topics?
**Eftiquar** 17:16 Looks good to me.
**Zach Montoya** 17:20 Alright, well, I'll give some time back. Thanks, everyone, for, for joining.
**Eftiquar** 17:24 Thank you.
**Rajkumar Rangaraj** 17:25 Thank you.
