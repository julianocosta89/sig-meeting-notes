SIG: Semantic Convention Tooling
Date: 2026-11-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:58 Hello, hi Josh.
I can't hear you.
**Josh Suereth (Google LLC)** 02:09 Oh, how about now?
**Liudmila Molkova** 02:11 Yeah, I can hear you now.
**Josh Suereth (Google LLC)** 02:13 Okay. I'm doing some horrible things in Weaver.
Not horrible. I, I've been working on the, refactoring of V1 and V2 resolution.
And guess what?
Never got implemented because, forgot.
I think it got dropped because of all the conversions.
**Liudmila Molkova** 02:40 Jalenia.
**Josh Suereth (Google LLC)** 02:41 I may have caught this, and I don't remember if you have a PR. What?
**Liudmila Molkova** 02:44 lineage.
**Josh Suereth (Google LLC)** 02:47 No, lineage we purposely dropped. We do, we do the schema URL tracking now.
So we don't need lineage tracking if we have refinements.
Entity associations with refinements.
**Liudmila Molkova** 03:00 Oh, okay.
**Josh Suereth (Google LLC)** 03:03 So, you can't refine entity associations at all.
Which might be okay, but literally, like, there's nothing for them at all. They don't inherit… there's nothing. They're just… They don't inherit.
**Liudmila Molkova** 03:17 Oh, they… they lose them.
**Josh Suereth (Google LLC)** 03:19 Yeah.
**Liudmila Molkova** 03:20 Oh…
**Josh Suereth (Google LLC)** 03:21 And… and so, I forget if it was Claude or Gemini, one of the two was like, hey, did… I was looking at the algorithm, I noticed you didn't implement this, is this intended? I'm like, oh, gosh. No, it wasn't.
But, you know how we're doing all the conversion from, like, V2 to V1, where it's, like, all chaos in V1, and… Yeah, so apparently today they're not pulled over, because of how we do the, dependency lookups and stuff. So, I have a CL coming.
I don't know how you want this in reviews, by the way. The plan from… I have Claude doing my planning, and it wants to make 7 different CLs, all of which are going to be large.
I could do one godawful CL that's huge.
I can do a bunch of CLs where I probably should share with you the plan, so you can see where the end state is, so you know why each CL is needed, because they look terrible by themselves.
**Liudmila Molkova** 04:18 Realistically, what I would actually review is the APIs, like, the building blocks.
Not the, like, I would totally delegate the content to AI.
**Josh Suereth (Google LLC)** 04:31 Yes, that.
**Liudmila Molkova** 04:31 Jesus.
**Josh Suereth (Google LLC)** 04:32 That's exactly where I am. So, the high level, like, I can share with you the plan, or I'll figure out if I can get the trajectory and share it. But the high-level plan is there's gonna be… you know how I made the V1, V2 split everywhere else?
There's gonna be a V1 and a V2 split for the resolution algorithm.
And then, inside of that, there's a shared graph, module.
that does, like, dependency lookups and stuff. And if you remember the dependency lookups where we say, like, look up group summary info, right?
And how there's a V1 trait and a V2 trait?
it basically takes that approach. So we take the set of graph lookup things.
And we have, traits for V1 resolution, traits for V2 resolution. And if you're looking at a V2 registry, you pull the V2 things into V1 if you're doing V1 resolution, and if you're doing V2 resolution, you do V2.
Important things, okay?
If you specify dash dash v2, It will try to do V2 resolution for you.
But if you have anything V1 in your definitions, it will issue a warning and say, sorry, I can't do this, I have to go back to V1.
**Liudmila Molkova** 05:44 Mmm.
And then it will convert V2 to V1, and then use V1 resolution.
**Josh Suereth (Google LLC)** 05:49 And then use V1 resolution, then convert it back to V2.
The way it does today.
The other thing is, the… and I like this, there's going to be, like, in the PR that I send.
there will be, a flag where everything gets converted to V1 resolution back to V2 by default, and there's a flag you turn on to do V2-style resolution to begin with, so we can run our integration test with both, on and off.
Well, I should say where it's relevant.
**Liudmila Molkova** 06:22 Yeah. That…
**Josh Suereth (Google LLC)** 06:22 That part, I haven't seen what the agent's done, but I like that as, like, a general principle of, like, where we're gonna go.
But yeah, right now it's just doing some cleanup and renaming of things to, like, basically refactor what we have today to say it's V1.
And I don't know if that's worth sending a PR that is basically a bunch of renames with no actual new code. Oh, it… sorry. It fixes entity association.
And, and add some tests for it. But it's just, like, a bunch of renaming that looks gross.
And the reason it looks gross is not obvious, because you don't see the V2 showing up yet.
**Liudmila Molkova** 07:00 Yeah, from what I… my impressions reading this, there is this… I don't remember the name, but there is this big giant method that does… Everything.
And… It's… Not clear when it does what.
And it's broken down by the… Not the… phases of… Not by definitions, but by attributes.
Or maybe they are all mixed together. And… at least from, like, a meatball perspective, reading the code, I have no idea what's going on there.
And I was thinking that, It would be cool to, like, split it up and have some added names that tell something, and then we can have some stages of this algorithm.
**Josh Suereth (Google LLC)** 08:01 Hold on, let me… let me find this plan for you. It does that.
**Liudmila Molkova** 08:05 Nice.
**Josh Suereth (Google LLC)** 08:05 So, so, here's the difference, though. For V1, I'm kinda… I'm declaring bankruptcy and just letting it go.
**Liudmila Molkova** 08:11 Yeah, makes sense.
**Josh Suereth (Google LLC)** 08:13 to… I have to copy this out of our proprietary crap, but I'll put it in our meeting notes. Give me one sec, and I will do that, so you can see. I actually, this is one of those things where… you know, you give it, like, you're, like, guiding it and telling it things, and then this is one of those where it's like, hey, here's the code I'm planning to write for what the, algorithm looks like, and I'm like, hey.
This is awesome. This is, this is, I wish I had thought of it.
Here we go. Where is our… Come on, Semcov. Okay, meeting notes.
We are on Next, apparently.
Gosh.
Come on.
**Liudmila Molkova** 09:03 Give me a sec, my coffee's ready, I'll just go for myself some coffee.
**Josh Suereth (Google LLC)** 09:07 Yeah.
**Liudmila Molkova** 09:45 And back.
**Josh Suereth (Google LLC)** 09:47 Okay.
I'm not presenting yet, am I?
**Liudmila Molkova** 09:50 No.
**Josh Suereth (Google LLC)** 09:51 Okay, let me do that.
Alright, so this is the basic gist of the algorithm.
Okay?
So, Resolve from V2, you have your V2 sources, you have your V2 depths, and you have the schema cache lookup for, like, looking up your dependencies from cache, right?
As we do today.
So first, we build symbol table index and duplication checks of, like, you know, what… what entities exist, what metrics exist, all that kind of junk.
Then we create the attribute catalog of all the attribute definitions.
First, we grab local.
Or no, we grab all the local and put them into the catalog, right?
Then we expand your attribute groups, so all your attribute group refs, and expand them into the catalog.
Then we do all of the signals, the base signals. So we do, you know, metrics, logs, traces, then we resolve refinements off of our base signals. So this uses The groups, the depths, the… the, attribute catalog, and the signals.
Then we resolve imports. So this is where the, you know.
Near the end, we import all of the upstream stuff that you say you want to re-expose.
Then we do entity association resolution, which I think you added this, where it, like, does the entity check and issues errors.
Then we do the implicit validation on every individual signal on its fully resolved state.
And finally, we emit the schema. So we take all of our temporary buffers and things, and then turn it into the actual, you know, minified struct.
So…
**Liudmila Molkova** 11:43 I love it.
**Josh Suereth (Google LLC)** 11:44 Yeah, it's so much more clear what we're actually doing. I mean, this is what the resolution algorithm looked like on V1 at first.
And then we just… You know, made it convoluted as hell because we changed all the rules, but we didn't change what it was doing, you know?
**Liudmila Molkova** 12:04 And we added refinements, inputs, associations, and everything.
**Josh Suereth (Google LLC)** 12:10 Yes. Yeah. So, like, I'm hoping that, going forward.
we can kind of keep this kind of a structure for most things, and I'm also hoping, with V1 that I can tickle the agent to get it to look like this as well.
So it's clear the steps it's taking. But V1 had a bunch of other things it was doing, like it does lineage tracking, for example, right?
This does lineage tracking, but we're only tracking schema URL sources.
Because the lineage is implicit in a refinement.
**Liudmila Molkova** 12:48 Yeah.
That's awesome, and I don't need… I don't think we need to change V1.
Just because it inevitably comes with some bugs, and… Yep. Which is done.
have to do it, but since it's the same codebase, it's probably will make some changes, and we won anyway.
**Josh Suereth (Google LLC)** 13:11 Well, the other thing I'm trying to do is, V1 should be relatively contained in a directory, so whenever we're ready to deprecate, we can literally just kill that whole module.
Like, across the board, just rip it out. So…
**Liudmila Molkova** 13:25 Yeah.
**Josh Suereth (Google LLC)** 13:27 Which I know… That's a fuck's cool.
Yeah, yeah, I'm pumped.
I told you I was gonna do this, and it takes me a while to get to these things, but a lot of it is just the decision-making, you know? These are like… You can get… you can get the agent to make a plan and, like, 10 seconds.
But reviewing the plan takes, like, an hour.
**Liudmila Molkova** 13:49 Right. So, in the past, like, you know the decision-making fatigue. In the past, you're, like, you make the decision, and you go, like, implement it for hours. And now, you… their life is just decision-making, there's nothing else.
**Josh Suereth (Google LLC)** 14:05 Yep.
Ugh, and some of the decisions, like, you know, Claude particularly, is, like, this… I feel like it's, like, an OCD person, if you will, and this might be offensive, but it just, like, agonizes over the most trivial decisions, and you're like, this doesn't matter. Like, why… why are you asking me about this 30 times? I've told you 7 times, it's fine, and you keep telling me that you find other reasons why it's not okay.
I don't know what to tell you besides, you know, anyway.
That's fun.
**Liudmila Molkova** 14:37 So, when you ask AI to do quad review.
And I tend to ask, like, like, a goal. Do until, like, all the major things are identified.
it's given a task to criticize. It will criticize as long as it's… I don't know, it has the power.
**Josh Suereth (Google LLC)** 14:57 Yeah.
**Liudmila Molkova** 14:57 And you have tokens. So, it's just… it's… it sounds like you need to, at some point, I see, okay, there is just the noise, and it means it's good enough.
**Josh Suereth (Google LLC)** 15:10 Yeah.
Yeah, I… That is definitely true, because, I read… I read a book about this recently, where one of… it was… it was just a bunch of short stories about different characters.
It's a really good book, but one of the characters wanted to be an author.
And wrote all these wonderful stories, and was, like, apparently a very good author, where everyone said their stories were awesome, but wanted their work to be perfect, and so went to a bunch of workshops for the story, and would listen to all the feedback.
And then when they finally got to an editor, they're like, this is over-workshopped. Like, whatever you had got destroyed by all the feedback, because you, you know.
Yeah. Yeah. And I feel like that's a little bit what happens here.
Okay, we have an agenda item someone added that I don't think can attend, so I'm gonna show this. This is about, benchmarking Rego shared context.
Do you remember this, PR?
**Liudmila Molkova** 16:09 Yeah.
**Josh Suereth (Google LLC)** 16:11 It's a criterion benchmark. I wanna… I definitely wanna have criterion benchmarks.
What I don't know is what the, you know, in here.
Is this V1 or V2? Like, is there… Jesus.
**Liudmila Molkova** 16:33 This is Life Check Regal.
**Josh Suereth (Google LLC)** 16:36 Yeah.
And they want to do a criterion benchmark for LiveCheck Rego, but I'm not… certain… I think adding… adding Criterion benchmarks is awesome. I'm… I'm a fan. I've used Criterion before, it's a really good way to, like, improve things.
What I don't know is… you know, is this specific to just live check? Like, what's our… what… Why do they want it in, and what's the goal?
**Liudmila Molkova** 17:09 I think I'm fine, too.
**Josh Suereth (Google LLC)** 17:11 By the way.
**Liudmila Molkova** 17:12 Yeah, I mean, it makes sense for life. I… probably don't care how fast REGO is for static checks.
Probably matters at some point, but, like, for a life jack, it matters 10 to 10,000 times more.
**Josh Suereth (Google LLC)** 17:29 Yeah.
This might be part of the, This might be coming from the Hotel Arrow, folks.
I'm not sure, though.
**Liudmila Molkova** 17:43 I don't think so, but… I had this question myself, like, how much Rigo can handle.
When running in life checks.
Yeah. If you don't have any concerns merging it, let's merge it.
We're… Jeremy had some thoughts.
**Josh Suereth (Google LLC)** 18:08 I think this will be parked for a while.
maybe we need to ping Jeremy on this. I mean, it's out of date right now. But the other thing is, I don't know… the only thing that would block this in my mind, is… if it's using an API on live check that we don't want it to. But, like, this is just defining the API for how to make a benchmark.
What the fixture is.
And then, this is where we call into LiveCheck, right?
So we make a new sample span… And then… where does it actually run?
As an expected finding… We had a policy, we expect that it compiles, wonderful.
We check that it succeeds in pre-flight.
And then it produces a finding.
Benchmark.
**Liudmila Molkova** 19:21 Oh, so this is, like, a setup, I would imagine.
**Josh Suereth (Google LLC)** 19:24 Yeah, this is set up… I'm just trying to look at where it's actually calling into…
**Liudmila Molkova** 19:29 I think Benchmark Regal Advisor?
**Josh Suereth (Google LLC)** 19:32 Yeah.
Where is Benchmark Rego Advisor, though?
**Liudmila Molkova** 19:38 Oh, you've been there.
**Josh Suereth (Google LLC)** 19:40 I went past it.
**Liudmila Molkova** 19:42 Yeah, it was under the pre-flight.
There you go.
**Josh Suereth (Google LLC)** 19:51 Yeah, but that's… that takes the criterion thing, grabs all the fixtures, runs pre-flight, and then runs the fixture, but where are we actually calling into… This is where we serialize things.
Benchmarks, input, serializes, so we measure how long it takes to serialize in JSON, okay?
That's fine. This, this could be independent, like, we could literally just measure JSON serialization and other things. We don't have to do it here. Like, this doesn't have to be specific, but yeah.
**Liudmila Molkova** 20:23 Line 233.
Oh, this is set input?
**Josh Suereth (Google LLC)** 20:29 Yeah, that's setting the input to the engine.
**Liudmila Molkova** 20:32 Okay. An evaluation engine.
Next.
**Josh Suereth (Google LLC)** 20:38 Yeah, so the benchmark engine thing is what is returning the actual live check engine.
Yeah, the only con… so the concern, I think, that might… that might make sense here is we need to look at Benchmark Engine a sec.
Where's… where is… where are you?
Benchmark Engine.
Gosh.
Okay.
Bench.
Mark Engine.
Yeah, this. I think that this is… this is… this is the live check engine, okay? And you had a poly… no.
This isn't the live check engine.
That's our policy engine.
This isn't… this literally is not testing the actual live check at all.
The only thing that's true is the third serialization of LiveCheck, and then our Rego policy engine from Weaver Checker, right?
**Liudmila Molkova** 21:35 Hmm.
**Josh Suereth (Google LLC)** 21:37 So, the question would be, like, the only concern I have in my mind is, I think having a benchmark is awesome.
Where do we have the benchmark?
Like, I think having a benchmark around Weaver Checker makes sense, in that crate, where we can then say, hey… because if there's a slowdown here, you don't even change live check at all, you go change that Weaver Checker code, right? If there's a slowdown in serialization, you would change, possibly, the CERD implementation.
In Weaver Live Check, that's fine.
But I think the… the only concern I have right now is where… where it lives. I can make that comment. But I don't… I don't really see us wanting to block this, just saying, hey, move this test here, move that test there, then I think it's good.
**Liudmila Molkova** 22:26 Yeah, I imagine maybe the author didn't realize that we have two different policy… Places, and they… Naively tested the weaver checker policy, thinking it's a life check.
But yeah, we can…
**Josh Suereth (Google LLC)** 22:46 No, LiveCheck uses the same policy engine as WeaverCheck.
**Liudmila Molkova** 22:51 Oh.
**Josh Suereth (Google LLC)** 22:52 So what I'm saying is, this benchmark is literally just checking the performance of the policy engine.
And that policy engine is reused between live check and not live check. So, like, what's…
**Liudmila Molkova** 23:03 S.
**Josh Suereth (Google LLC)** 23:03 What's the value of the benchmark, And what does it… what does it prove? If you're benchmarking that Weaver Checker crate, put it in the Weaver Checker crate. If you're benchmarking the serialization of live check samples.
Yeah. Put that in live check, but that's the only bit that's live check specific.
**Liudmila Molkova** 23:22 Right, and the end-to-end would look like a real, load test, not the microbenchmark.
**Josh Suereth (Google LLC)** 23:30 Yeah, yeah. So basically, this is more about how to use Criterion in our repo. So, I can make that comment of, like, hey, all of the engine checks where you're actually checking Wrigo policy should move to Weaver Checker.
And we can do, like, we can have a micro-benchmark there and have a optimization cycle there, but I don't think it belongs here in Weaver Live Check. I… we can also talk to Jeremy.
Okay.
**Liudmila Molkova** 23:56 mind leaving a comment? And I think Jeremy can reply.
**Josh Suereth (Google LLC)** 24:01 Yeah, yeah, I will do that.
**Liudmila Molkova** 24:02 There's such.
**Josh Suereth (Google LLC)** 24:06 Microbench… Mark, that, doing on this actually belongs.
Sugar. Great.
My gosh, I can't spell.
Okay.
Cool.
Do we have anything else to talk about? It's just the two of us.
**Liudmila Molkova** 26:17 Yeah, so downstream checks are not fixed.
**Josh Suereth (Google LLC)** 26:22 Yes, I saw that.
**Liudmila Molkova** 26:22 Yeah.
So, I'm not sure if you saw the PR, but the problem is that we cannot fix them, because the problem is in the released version. So, when we do the, compatibility checks, right? We pull the baseline.
And the baseline is broken.
So, what I'm… Suggesting to do.
is to… Maybe we need a CLI flag for this, but hopefully not.
So when we do the compatibility check and we pull the baseline, we tolerate, non-fatal errors in the baseline.
As an approach.
And… make the… whatever it was, the entity identity, a non-fatal error for this purpose. In V2, it's always… Firing?
in V1, it would be a warning, And this way, we can… Make it work.
**Josh Suereth (Google LLC)** 27:32 Yeah, I was, like, when you asked, like, why don't we warn on this, and why aren't we enforcing Weaver, this is why, because it just broke everything.
**Liudmila Molkova** 27:39 Right, yeah.
Sorry.
**Josh Suereth (Google LLC)** 27:42 No, it's fine, I thought we were further along and we could fix it, yeah. Okay, so basically what we're doing is we're just reverting the behavior of how we enforce it, but we're going to still enforce it on V2, but we're not going to enforce it if we have V1.
**Liudmila Molkova** 27:56 we are enforcing it on V1, we just don't enforce it specifically for the baseline.
Because, like.
**Josh Suereth (Google LLC)** 28:04 Okay.
**Liudmila Molkova** 28:07 So you know how we, have a special… how is it called?
The special command where we do the compatibility check.
Oh, when we provide the baseline.
**Josh Suereth (Google LLC)** 28:19 Oh, oh god, yeah, yeah, for the diff, yeah.
**Liudmila Molkova** 28:22 Yeah.
**Josh Suereth (Google LLC)** 28:24 Okay.
**Liudmila Molkova** 28:26 So we do at the absolutely minimum relaxing possible.
And… Yeah.
There's another… Is she a… That has multiple solutions, but because we can refine refinements.
We did, in Gen AI, by accident.
But we'll fix it. I don't want to open this, possibility today. I prefer to close it and just fix the GenAI repo.
**Josh Suereth (Google LLC)** 29:05 Okay.
I mean, I'm… I'm fine with that. Give me one second, I gotta send a chat.
Okay, I'm fine going this direction. Yeah.
I bet.
Just thinking.
Okay.
Do you think we have any other holes here, or there's gonna be a big blow-up or friction for people consuming Weaver?
Because it's not gonna work on previous versions, and I know, like, the Go community might freak out about that.
Or no, maybe they… maybe they don't care.
Yeah.
**Liudmila Molkova** 29:51 Than previous version of Semantic conventions.
**Josh Suereth (Google LLC)** 29:54 If you try to resolve with the V2 flag on an old version, it's gonna fail, always.
Right.
**Liudmila Molkova** 30:01 Yeah.
**Josh Suereth (Google LLC)** 30:04 Or on any released version, actually.
**Liudmila Molkova** 30:08 on any released version with V2 flag.
**Josh Suereth (Google LLC)** 30:11 It will fail, yeah.
**Liudmila Molkova** 30:13 It will fail, but… I… why would they do this? If… if it's… it's immutable, it's already generated.
**Josh Suereth (Google LLC)** 30:25 You mean the code? Like, for CodeGen? Yeah. For Wave for CodeGen.
**Liudmila Molkova** 30:29 Right, but I, like… the Go SDK wouldn't care.
About anything else.
**Josh Suereth (Google LLC)** 30:37 The Go SemConf modules, they have, like, a different package for every version.
And they, they generate them.
**Liudmila Molkova** 30:45 Right. And they don't generate them.
every time, right? They generate them, they commit them.
**Josh Suereth (Google LLC)** 30:52 I think so, but I'm not positive, yeah.
**Liudmila Molkova** 30:55 Okay, I can check, I'll check.
**Josh Suereth (Google LLC)** 30:57 Okay.
**Liudmila Molkova** 31:01 I mean, it's broken already, with, whatever, 126, is the earliest we support anyway.
**Josh Suereth (Google LLC)** 31:12 That's true.
That's true. Okay.
Alright, yeah, I'll look at your PR and, try to get that merged. I gotta jump to another call, I think.
So, is there anything else urgent we need to talk about with Weaver?
**Liudmila Molkova** 31:30 No, nothing urgent.
**Josh Suereth (Google LLC)** 31:33 Once we get the downstream checks fixed, that would be ideal. Do you think we should issue a SEMCOM release before we cut the next Weaver release, or not?
**Liudmila Molkova** 31:42 We didn't have to.
**Josh Suereth (Google LLC)** 31:44 Okay.
**Liudmila Molkova** 31:45 We can, but we don't have to. Oh!
I see. We probably have to.
**Josh Suereth (Google LLC)** 31:51 Yeah.
**Liudmila Molkova** 31:52 Yeah. Yeah, okay.
**Josh Suereth (Google LLC)** 31:55 Okay.
That's… that's why I'm worried about it being, like, a blocking failure. Like, I almost would want, Because I don't think those resource entities are actually being used. If we had a mode where we… Don't fail to resolve, but we give you a warning that we're dropping them because they're invalid.
Or that.
**Liudmila Molkova** 32:17 Automatically converted.
**Josh Suereth (Google LLC)** 32:18 Reporting them to attribute groups, because they're invalid, you know?
**Liudmila Molkova** 32:22 Oh, that's interesting. So, accept them, but convert them into attribute groups.
**Josh Suereth (Google LLC)** 32:29 And say that they're getting better.
**Liudmila Molkova** 32:30 show up in the results schema. You can depend on them, but…
**Josh Suereth (Google LLC)** 32:35 Yes.
**Liudmila Molkova** 32:36 Or maybe you cannot refine them.
**Josh Suereth (Google LLC)** 32:38 You can't refine them, you can't treat them as entities, but you could, like, see them.
and treat them as an attribute group locally for resolution, yeah. So it doesn't kill everything, but it… yeah.
**Liudmila Molkova** 32:50 Right.
Okay.
Let me think about it. We're… it's a great escape hatch.
**Josh Suereth (Google LLC)** 32:57 Okay. I, I know, I'm trying to not break the whole ecosystem, is my goal.
Yeah. And still get people to stop doing bad behavior.
**Liudmila Molkova** 33:08 Okay.
Cool, I'll check, I'll check something, but yeah, go jump on your other call. I'll think if you can do that.
**Josh Suereth (Google LLC)** 33:16 Ping me on, Ping me in Slack, and I'll review it if you… after you take a look. So I'll either approve what you did, which I think is fine, or if that works out better, that might be a little more flexible and have less breakage, and we might get nightly working sooner.
**Liudmila Molkova** 33:31 Okay, cool, yeah, thank you. Awesome. See you.
