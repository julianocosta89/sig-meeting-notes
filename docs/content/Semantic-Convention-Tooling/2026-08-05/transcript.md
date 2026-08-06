SIG: Semantic Convention Tooling
Date: 2026-08-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:27 Hello, hi, Josh.
**Josh Suereth (Google LLC)** 01:29 Hey, I think Jeremy's in the wrong Zoom.
Because he added a whole bunch of stuff, and he adds the document open.
**Liudmila Molkova** 01:37 Okay.
Pretty odd.
**Josh Suereth (Google LLC)** 01:40 This whole Zoom changeover has been, kind of a disaster.
**Liudmila Molkova** 01:44 I agree.
**Josh Suereth (Google LLC)** 01:46 Yeah.
Alright, I'll present the notes, and then hopefully Jeremy jumps on. How are you doing?
**Liudmila Molkova** 01:55 I'm doing fine, thanks. It's very smoky here lately.
**Josh Suereth (Google LLC)** 02:02 I saw pictures from, But our… my… my TL, Ron.
**Liudmila Molkova** 02:10 Right.
**Josh Suereth (Google LLC)** 02:11 He's in Portland, he said it was orange.
**Liudmila Molkova** 02:16 Yeah, I think it's worse in Portland, but yeah, it's pretty bad.
**Josh Suereth (Google LLC)** 02:22 Yeah, so don't go into the forest and just light stuff on fire? Is that what we're learning?
**Liudmila Molkova** 02:28 Wow, such a surprise, right?
**Josh Suereth (Google LLC)** 02:33 Yeah, what's crazy is… You know, like, this is just a thing that happens, right?
So… there's some question in my mind of, like.
If I were in the Middle Ages.
And suddenly, it was really smoky and orange outside.
what would I think is going on?
if I didn't understand, you know.
Because, because when, what was it, like, a month ago, the Canadian wildfires?
hit Pittsburgh, and it just, like, became cloudy and smoky all day, and it smelled like things were on fire. But you could have gone miles and seen nothing, you know?
So, if I were in the Middle Ages, or earlier, you know, when, like, technology and communication was slow.
what would I have thought?
**Liudmila Molkova** 03:24 Well, something of… God's… the active guide of some sort.
**Josh Suereth (Google LLC)** 03:30 Yeah, I would have burned a witch, that's what I would have done.
**Liudmila Molkova** 03:33 Oh!
**Josh Suereth (Google LLC)** 03:34 From Monty Python or whatever, yeah.
Okay.
Ugh, okay, I'll ping Jeremy, because I think his discussion's the most important one for us to have.
Okay.
I do want to do a little bit of follow-up on all of the, the bugs that… came from multi-dependency. I think I was going through, like, some of what happened, and basically, we made a few decisions which independently weren't breaking, but when you added them all up, became breaking, right? So, the dependency on having Schema URL have valid version.
when I added that, I had added all of the version tracking ahead of time, but made it completely optional, and then when I made it required, all of the tests already had valid versions, so I had no idea that I had broken anything.
**Liudmila Molkova** 04:43 we could have solved it in a couple of ways, I think. Like, no amount of tests we have in Weaver was able to discover some tricky issues we had when we used Weaver and, let's say, semantic conventions, where the things are complicated, right?
Yeah. Those ones we hit because we didn't have a realistic registry that used We were… That we could test Weaver against.
And I think Jeremy's… Registries are like that, but they're private.
**Josh Suereth (Google LLC)** 05:24 Hmm.
**Liudmila Molkova** 05:26 So… If we could replicate some of the Realistic stuff.
But let's say in waiver examples.
Like, I, I, I actually hate our tests.
It's impossible to understand what they do, right? We just compare the output, that's it.
**Josh Suereth (Google LLC)** 05:51 Yeah, like, if you write them, you know what they did, but if you didn't write them, it's hard.
**Liudmila Molkova** 05:57 I mean, the Rust code is fine, but the YAML and expected output… It's like, it's so much that you cannot reasonably review it.
**Josh Suereth (Google LLC)** 06:09 Yeah, it… I mean… If you're making a small feature.
generally, you can figure out what happened, but when you have something, like, that's why we have the colored diffs, because no matter what you do, all the refs change. You add one attribute, every ref number changes across the whole stupid thing. So you have, like, a giant diff, so you have to, like, know to ignore all the ref number changes, you know?
So I, I hear ya.
Yeah. I was looking at this one here, I didn't have a chance to do a full review yet, but yeah, how did… how did this happen? Where did… where did it break?
I remember it was a pain in the ass to get this correct, and I kept having Providence get dropped random places. Oh, hey, everyone's here now, okay.
**Laurent Querel** 06:57 Aye.
**Jeremy Blythe** 06:59 We need to update the link in there.
In the document.
**Josh Suereth (Google LLC)** 07:04 Oh, it's the link in the documents the problem? I put it right here, though.
**Jeremy Blythe** 07:08 No, the one at the top, where it says, here's the Zoom meeting.
**Josh Suereth (Google LLC)** 07:13 This one here?
**Jeremy Blythe** 07:15 Yeah.
**Liudmila Molkova** 07:16 But isn't it the newer?
**Jeremy Blythe** 07:18 That has a different password.
**Josh Suereth (Google LLC)** 07:20 No, this is… this… one of… what?
**Jeremy Blythe** 07:24 What are these two, then?
**Josh Suereth (Google LLC)** 07:26 Why is it, like, a thousand different places? Hold on, let's delete that one.
**Jeremy Blythe** 07:31 But that's exactly what I clicked, so I'm confused, but hang me.
**Josh Suereth (Google LLC)** 07:35 Yeah, this is a different one, and I don't know… oh, this is from my calendar.
Let me… let me actually… I'll fix the Zoom link quick, and we'll,
**Jeremy Blythe** 07:50 I swear, that was what I clicked on.
Because I would…
**Laurent Querel** 07:53 Duh.
**Jeremy Blythe** 07:54 Because I can never remember it.
**Josh Suereth (Google LLC)** 07:56 Yeah, let's do this. Okay, I put it… That should be right now. That's the one that I clicked on.
Okay, I'm gonna get rid of this here.
Okay, I updated all the notes. We were just going through this, and I was trying to figure out where this had broken, This one's good to review, though, right, Ludmila?
**Liudmila Molkova** 08:25 Yeah, it is.
**Josh Suereth (Google LLC)** 08:26 This might be related to some of the stuff that Jeremy's seen as well. If the provenance is not right, like, things would be horribly broken.
Okay.
I'll take a look at this after the meeting. Do we have any other major issues that came in from the releases we need to take a look at?
**Jeremy Blythe** 08:46 this debug With live check still… truncating.
That's still not fixed. I want to fix that by… having a… having the client request the report, and then when they're happy and they've got the report, then they send it, okay, now stop. Because it's just, like.
Trying to do that in some way where we're, like.
timing out, or monitoring what's happening at a TCP level, or whatever, it just seems, like, so complicated.
Yeah.
that we're gonna have to do a braking change. You go get the report, and then when you're happy, then you go, okay, now stop.
**Josh Suereth (Google LLC)** 09:38 I mean, the timing of this is just rough, right? Yeah.
**Jeremy Blythe** 09:42 It's really horrible, and it's just, like, it's just gonna get more and more horrible and never, ever be quite right in my… like, I just… it's one of those things where we can carry on banging our heads against the wall, or we can just go, like, you decide when you've got it. You decide when you want to finish.
**Josh Suereth (Google LLC)** 09:58 Well, yeah, having the server try to send a response and then kill itself when the responses act is rough.
**Jeremy Blythe** 10:05 Yep.
**Josh Suereth (Google LLC)** 10:06 Yeah.
**Jeremy Blythe** 10:06 It is.
**Josh Suereth (Google LLC)** 10:07 So, stop and report being separate commands makes more sense.
**Jeremy Blythe** 10:11 Yeah.
**Josh Suereth (Google LLC)** 10:12 Okay.
Cool. So… I think… I've checked benchmark, repeated Rego shared context cost before optimizing. No idea.
**Jeremy Blythe** 10:24 I think… I mentioned to that contributor that there may be an optimization that could be done, and they've then, obviously, just used Codex to take my words and Run some kind of benchmark test.
**Josh Suereth (Google LLC)** 10:40 Okay.
Interesting.
**Jeremy Blythe** 10:43 Not urgent at all.
**Josh Suereth (Google LLC)** 10:47 Alright, so I don't think we have anything new outside of THE issues. We have the attribute resolution issue, which, this is the one I wanted… like, this is your topic, right, Jeremy?
**Jeremy Blythe** 10:59 Yeah, that's right.
**Josh Suereth (Google LLC)** 11:00 Okay, so let's get through your topic, because I just want to make sure we're dealing with all the, like, major issues here.
Ludmila has a fix for some provenance issues that we need to make sure we get in. I think this is probably worth a point fix.
Just calling that out, so I'm gonna throw it on to consider for next release.
or… What do we have?
Sorry, wrong thing. Where's the project?
Come on.
**Jeremy Blythe** 11:32 Where are we really with V2? Are we telling the world V2 is ready? Or do we still have the… warnings in place that say, hey, this is experimental. Because all the problems we're finding really are in V2 still, right?
**Josh Suereth (Google LLC)** 11:46 Yeah, yeah, but that, like, we're in the bug fix V2 phase, I think, is what we are. So, do we want to call a release candidate? If you look at… one of the issues Liudmila has here, I think, is, like this here, remove deprecated from stability, in V2, I think this is a kind of thing we probably should do prior to going release candidate. So, we're still evaluating and opening bugs. But that said, I think we're really close. I'll put this as to consider for next release.
**Liudmila Molkova** 12:19 Oh, right, yeah. Oh, yeah, I also…
**Josh Suereth (Google LLC)** 12:21 captured.
**Liudmila Molkova** 12:22 Yeah, I also have, proposal, we don't have to talk about it right now, but, I want to challenge the need to have stability and deprecated on attributeraphs.
Because we don't really have a use case for it, and they're just making things wrong, and we don't have… we don't even have tests for them.
**Josh Suereth (Google LLC)** 12:43 Oh, yeah… I think they exist just because of momentum, not because of, like, planning.
**Liudmila Molkova** 12:51 Yeah, so, like, if we drop them, the life would be easier.
**Josh Suereth (Google LLC)** 12:56 Okay. Alright, let's get into, Jeremy's discussion here.
So… do you want… do you want to present, or do you want me to pop this open and look at it?
**Jeremy Blythe** 13:06 If you just open it, I think… So, with V2, I started, like… this came about because I started looking at things in serve, because in serve, I would click a link, and then I would get a 404. I'm like, this is wrong.
and then… Oh…
**Josh Suereth (Google LLC)** 13:29 This here, by the way.
**Jeremy Blythe** 13:31 Yeah.
**Josh Suereth (Google LLC)** 13:32 So the idea is… If I'm doing CodeGen.
I can… I only have to look at refinements.
I do not have to look at… raw.
metric definitions. Every… every… metric that's defined has a single refinement guaranteed, which is the exact same as the metric itself. So that if I look in the refinement list, I get all possible refinements, including the original definition.
**Jeremy Blythe** 14:04 Okay.
**Josh Suereth (Google LLC)** 14:05 That's… that is what that is, if that is confusing you.
**Jeremy Blythe** 14:09 Yeah, that's why I just put that in as a, is this right?
**Josh Suereth (Google LLC)** 14:13 That's by design, it looks a little weird. So we can discuss whether we like it, whether we're using it, but it's supposed to make CodeGen templates easier, because you can actually just only look at refinements and get all the possible, like, code gen you need.
**Jeremy Blythe** 14:32 The… oh, if I cut to the meat of this, like, the… the issue is… Today.
What LiveCheck does is it just… It gets the… For all of its attribute.
checks. So when it's checking the type, whether the attribute even exists, and things like that.
the stability, things like that. It's going to that, top-level list of all of the attributes that you get.
So if you think about V1, you've got this, like, here are all the attributes that are used, list, and then it just uses that.
In V2, you only get that, attribute list for things that you've defined locally, because that's registry.attributes.
So you're only getting that for attributes that you've defined locally, not in something that's upstream that you're depending on.
Sorry, downstream, you're depending… upstream? Anyway, thing that you're depending on. So if you… follow some of the things we've been recommending to people, like, because they want to do live checks over a subset of a registry, for example. One of our recommendations is, oh, hey, just make a registry that just has imports for the things you want to test against. Like, you can't do that.
Because I have no way to import an attribute.
Not possible.
I can do… I can make… an attribute group.
And then I can reference all the attributes that I want to pull in.
But I could have, I think, multiple attribute groups that reference attributes, and then I've got… now I've got more, sort of, conflict resolution to do, which one is the right one that I should be checking against, things like that. Anyway…
**Liudmila Molkova** 16:29 Jeremy, the importing attributes doesn't feel like a right… Solution for this problem, because It effectively means that you need to import everything you reference from dependencies.
Right?
And… It… it's just… unnecessary thing. If we want definitions to become part of available. We would just include them in some fashion.
When we reference.
Something.
**Jeremy Blythe** 17:08 Yes, I think that's what I'm… Trying to get at.
In this discussion.
is… do… do I sort of implicitly… some… canonical, like, list that's created of all of the attributes that I've… referenced.
In… in my local, registry.
Depends.
**Josh Suereth (Google LLC)** 17:36 signal.
**Jeremy Blythe** 17:36 I can check against, which is what this attribute origins thing is, maybe a terrible name, but it's like, here's, like, here's the, like, original definition of this that hasn't been refined, isn't sat on a signal with some extra annotation on it. It's like, this is how it was originally defined.
So if you do… if you want that, Origin.
It's here available, and you can just use that.
Or I can explicitly say, I want that.
And live check against that.
Or some mixture of it, or something. I just… it's like, what do we want to actually…
**Josh Suereth (Google LLC)** 18:11 what's the goal here in LiveCheck? Like, what are you actually checking? Because, like, to some extent, if you have a signal.
and you want to check the attributes on that signal, and you've defined the signal, and it's a refinement, I should be able to look up the refinements applicable by schema URL and say, okay, here is… here's a refinement that has a bunch of extra attributes on it, and then that's the set of attributes I use to validate that signal.
**Jeremy Blythe** 18:38 Go ahead. That's exactly right, and there's no… We don't need to have a dis… that's fix number one.
Which is, if I've matched against the signal, I should be using the definition that is defined on that signal for that attribute. 100%.
No argument there. It's what do I do when I haven't matched the signal, because what if a signal is untyped, like a resource, or an instrumentation scope, or a span, or a log, or… I don't match a signal, but I still want to go… oh, this is a metric I don't know about, but I can at least tell you how good your attributes are.
I secured those today.
**Josh Suereth (Google LLC)** 19:20 I see. Like, so… I think that's not a use case we designed V2 for.
Yeah. Like, you, you could, you could basically say, yeah, yeah, like, because what you could do.
is if we give you the same resolve schema that we're planning to… sorry, the forge schema we're planning to have.
you will actually have… here is, like, a schema URL, and all of the attributes for that schema URL. But then you would also have, here's the dependencies of it, and then you'll have the attribute registry for all the dependencies. So you could go through all of them and say, this attribute looks like it's from this schema URL, this attribute looks like it's from that schema URL.
But, like, what's the goal of this? You know, if the goal of live check, if that is a… because, again, you're not specifying a schema, so to some extent, I think whatever you do is best effort.
In this case. So it's like, hey, I have an attribute, you haven't defined it, I think it's this schema URL, and if it were, here's what I would say as, like, a warning, cool, that makes sense.
But what… what I think we want to do then is get you the list of dependencies, so you have… when we resolve this, you have, like, a whole set of schema URL resolve schemas, and in each of the resolve schemas, you have that… that attribute list for all the definitions from all the dependencies, and then you can look through all of them, so it's like a big, big ol' loop.
**Jeremy Blythe** 20:44 And is that… Would that gathering of all of that information be… in that, resolved schema that you give to LiveTrack.
**Josh Suereth (Google LLC)** 20:56 it won't be in the resolved schema, but it will be in the forged schema. In live check, what I'm suggesting is we give you… we give you a key-value pair of schema URL resolve schema for the entire dependency chain, and we tell you what the root is.
**Jeremy Blythe** 21:13 Do I have to go and fetch that from somewhere, or will that be enforced?
**Josh Suereth (Google LLC)** 21:17 It's already cash.
So, forge schema will have it.
**Jeremy Blythe** 21:22 Okay.
**Josh Suereth (Google LLC)** 21:23 Yeah, like, that's, that's, again, that's part of this whole restructuring that I did with the, like, being able to look up schema URLs and cache them and have the dependency and stuff. I don't know if you saw that, but effectively, in Forge schema, the strawman proposal was we add a new dependencies, or resolve dependencies.
you know, thing, and that will have a key-value pair of schema relative forward schema.
For all your dependencies.
So, you can then, from that, like, you know, figure out everything.
**Jeremy Blythe** 21:57 Okay.
So LiveCheck today uses Forge, it actually doesn't use Resolved.
**Josh Suereth (Google LLC)** 22:05 Okay, so it sounds like we should do this fix, and then you can use the fix to get access to all the attributes. So first, first you do fix number one of using the signal, and then for this attribute use case, once we fix forge schema.
then you get everything else you need. Because, we need this in Forge for other reasons. Like, we want to be able to do cross-references to dependencies, so you could have, like, this schema URL has its documentation here, so if I'm generating Markdown config, I can, like.
link out and say, oh, the provenance says that this comes from dependency X, I can generate a link to dependency X, because I can look up where it is, and all that kind of joke.
Or I can embed Dependency X's, you know, definition locally if needed, and that kind of crap.
**Jeremy Blythe** 22:51 Okay, that sounds good.
I'll have one of those.
**Josh Suereth (Google LLC)** 22:55 I have to drop in 5 minutes, so apologies. Is there… since I was out for a week and all hell broke loose while I was out, is there anything else I broke with dependency resolution that needs to be fixed? I still feel bad about that.
**Jeremy Blythe** 23:10 I don't know, but I think we… Don't have complete enough… Tests.
To expose all this kind of stuff.
So I think…
**Josh Suereth (Google LLC)** 23:23 100%.
**Jeremy Blythe** 23:24 We have found a bunch of things, sort of, by… accident. Afterwards, kind of like, I wonder if I can do this? Oh.
And then I'm met with something that turns out to be, maybe it's like, oh, that's not what we planned, which is in this case.
Some genuine bugs.
**Josh Suereth (Google LLC)** 23:43 This is a good… so, to me, it's a good signal that, I think prior to this, I thought we had sufficient tests.
And now I know for sure we don't.
So, we might need to go through, like, a testing. What I don't want to do is just add tests that make the build longer and longer, but don't provide value. But we might want to go through a quick testing sprint before we mark V2 ready, where we have confidence that we're not going to break users as we make changes.
**Liudmila Molkova** 24:14 I'm thinking maybe this is awesome and we should do it, but maybe we can also do this.
in Semantic Convention, Semantic conventions, Gen AI, where we can have a CI, That tests against that… them against latest Weaver, where we can do the nightly check in Weaver repo for these registries.
And we can also test Weaver examples. It wouldn't cover important things, like, Jeremy, yours, because they're private, but we talked that maybe we can contribute some of the similar examples to Weaver examples.
So that they are covered, and we check them, actually.
**Jeremy Blythe** 24:58 Yeah, so a lot of the fixtures that I've been adding.
Have been sort of distilled from… my… our, like, company, the way we're using it, right? To just, like, oh, I need to make a minimum, like.
reproduction of this thing.
Yeah.
**Liudmila Molkova** 25:21 So, like, we just had a CI that… in Weaver, that runs against the three.
Or whatever set of real… Real and example registries we have.
And this is a smoke test, if we are ready to release.
It's a blocker for release failure in them.
**Jeremy Blythe** 25:41 Yep.
**Liudmila Molkova** 25:44 Oh, unless it's a bug fix.
**Jeremy Blythe** 25:51 Okay.
**Liudmila Molkova** 25:55 I think a lot of the things… I kinda… maybe I'm naive, but I have very high hopes for the time when we remove V1.
it will remove so much complexity from the repo, and we can clean things up. I would love to… I think a lot of the issues come from the fact that we reuse Models between, Definition and resolved, and also as a carrier between, and we limit ourselves to types that would be serialized.
And if we separate this all, it's a lot of boilerplate, but it will give us more stability of, like, what goes where.
**Josh Suereth (Google LLC)** 26:55 Alright, I have to drop… I agree with that, Ludmila. I do… like, the whole resolution algorithm, if we can get rid of V1, will be way simpler.
Because refs are more explicit and obvious, so I think we can make that code a lot easier to read. And then all the V1, V2 crap, we can get rid of, a whole bunch of, like, layers of isolation, possibly. But, yeah, let's, We'll keep Fortune ahead. Okay, so for this, Jeremy, you're gonna do this one, right?
And… this would be… I can take a crack at this, I think I have time later this week.
To finish that up. I don't think this is gonna be too hard.
Given where things are.
But I'll send that to you for review, because I think once that's in, there would then be a live check change that's needed as well.
**Jeremy Blythe** 27:48 Yeah, so that will go into that PR that I've copied there. So that PR currently has a test suite.
That covers all sorts of, the different things that I brought up in that issue. Gotcha. All currently failing. So there's, like, 10 tests in there that are for different scenarios that currently failed.
that once your PR is in, and I've done the other fix, I'll put it into this… I'll put it into this PR, and it should go green, and then we've got a good test suite.
**Josh Suereth (Google LLC)** 28:17 Cool.
Cool. Okay, I need to drop, it sounds like for multi-dependency bugs, You guys cleaned up the mess right now, so if we find anything else, let me know, or we'll, Still.
You know… integration tests.
Okay, let me know if you need anything, and hopefully I'll see you next week for the full hour.
**Jeremy Blythe** 28:46 Okay.
**Liudmila Molkova** 28:47 Yeah.
I can take a crack at the CI against what we have so far, outside the fever.
**Jeremy Blythe** 29:04 Yep.
**Liudmila Molkova** 29:17 Do we want to talk about anything else?
**Jeremy Blythe** 29:20 Dude.
So one of those… Sorry, there was a PR that you had, right?
one of the dependency bugs that Josh just mentioned, right?
**Liudmila Molkova** 29:33 Yeah, I've been… Trying to make sense of… The issue you report… you had, and how to… how can we fix it, and… in my discussions with AI, I found… bunch of small problems that… that made things worse, but I don't think they are, like, as we discussed, it's not strictly related to life check problems. But… I think you mentioned it somewhere, that we don't report provenance for reps, for… Some of the refs.
Oh, in the resolved YAML, we don't report provenance for… I'm already lost. It's been yesterday, but yeah.
**Jeremy Blythe** 30:27 There was… there was one to deal with… the provenance.
That I actually fixed, so it sounds like you found another one.
**Liudmila Molkova** 30:38 Oh, okay.
**Jeremy Blythe** 30:40 There was one that was fixed before.
**Liudmila Molkova** 30:44 Okay, and this one is…
**Jeremy Blythe** 30:46 Similar to that.
**Liudmila Molkova** 30:50 Okay.
I'm trying to remember what was the fix for it, and I think… It, it was this one, tracking.
Origin, because at some point, you no longer can tell.
Okay, I'll, I'll dig into…
**Jeremy Blythe** 31:11 Okay.
**Liudmila Molkova** 31:12 That one, This… this is an nasty one, and I think it's super related to the discussion we had on the issue that if you had an You had the foo defined somewhere, then you… Inherited server refinement.
Oh, so you are refining it here, and you're updating the brief?
And because it's defined in the dependency, we don't have the definition for this attribute.
And then, when we… Actually, when we use it on some other metric, here, what it gets… Is not the original one.
But the refinement of… metric.
B, which is completely unrelated.
**Jeremy Blythe** 32:15 Right.
**Liudmila Molkova** 32:18 It looks so…
**Laurent Querel** 32:18 Vichie.
**Liudmila Molkova** 32:22 It is, but the fix is… Kinda trivial, so… I think this is the… This is… This is the fix, so we kind of keep track of what… so, okay, so this is the example where we abuse models.
we create… the attribute… We pretend that attribute reference is attribute definition, and at some point after, like, dependency resolution, we can no longer tell whether it's an original attribute or if it's a reference.
And the fix… I think a good fix is to just separate models from each other forever, and never reuse the same model for definition and reference.
But in the short term, like, unless we want to rewrite everything, the solution is to have a flag on the… On this thing that appears in the catalog, that it's a definition, and then use it for the conflict resolution.
And always pick the definition of a reference.
**Laurent Querel** 33:40 Lia, can you go back to the… the… I think it was the PR description or something like that.
So in the previous version, let's imagine that you have two metric refinements. So we… It was not exactly this way in the UN, but, we could do something similar. Let's imagine that you have two refinements, Ierating from, the same… B-metric, but you already find attribute two times.
the Semattribute, foo.
was too brief.
I'm curious to see if… At the end, and let's say that the briefs are exactly… we redefine them exactly the same way, with exactly the same text.
we should… Behind the scene, once the resolution is done.
We should, in fact, have the same… the base, when I see the… Yeah, the, the, the… The metric that is… available after resolution should be the same, with the same number, right? Because, in fact, you are modifying No, sorry, I'm, I'm, like, correct there. The attributes, should be the same.
Because we… okay, we… we refine it with the exact… the exact same brief.
So the… the corresponding resolution of this attribute, once the resolution is done, should be the same.
Let's say it's attribute zero, it's still attribute 0 for these two metrics, even if we have refined them two times.
I'm curious to see if that's the case.
**Liudmila Molkova** 35:36 Oh, I see what you're saying. Here… so… We… First, if we add a brief or anything in reference, if we modify anything at all, even if it's the same value.
We would currently produce a new… Rough… rough… AttributeRef in… Resolved schema.
**Laurent Querel** 36:02 Yes.
**Liudmila Molkova** 36:03 And this is the index in the result schema.
**Laurent Querel** 36:08 Yes.
**Liudmila Molkova** 36:09 And… like… This is a pointer to the attribute, and it should point to the original The original one.
**Laurent Querel** 36:21 In that case, yes, because you… you refer to C metric, which has, indeed, nothing to do with C.refind.
But I was thinking about a potential other issue, related to metric refinement.
Where you refine… The same metric, B metric, two times.
So, with two IDs, ID, CRefine, and, C-Refine, and D-Refine.
And… and you would define, basically, the attributes, but… In fact, you are redefining the attribute exactly the same way.
With the same brief XXX, for example.
I'm thinking that… At least what we did before was the corresponding attribute definition Because it's exactly equivalent We are not trying to… We'll present it two times, in the… in the underlying, schema.
we detect that they are, in fact, exactly the same, and… and C and D The refine are, in fact connected to the same attribute specification in that case.
**Liudmila Molkova** 37:48 We… I can do this… so I think the way we do it today.
Is that we define… so we define an attribute group.
And we don't repeat the brief, right? And then we reference the group.
On the… Metric refinement, or anywhere, right?
And this way, one definition becomes one.
Sorry, one reference in the group becomes one reference in the result schema.
What we don't have is that if you repeat the attribute reference and you modify it in exactly the same way, then we collapse it to 1.
We could do it, right? Yeah, that's a… would be an optimization.
Or is there more?
**Laurent Querel** 38:40 Yeah, that's what we did in V1, but, I don't know if, if the… My point was not necessarily related to optimization.
Was more related to… Better understand the underlying approach.
To see a potential other, miss resolution. It looks like it's, an approach… I can understand the approach. It looks like you are trying to keep The… the refinement visible Ever after resolution?
So… Basically, refine and derefine, keep the brief.
Even if they are the same, and reference to the same original attribute.
Okay.
Yeah, I think that's fine.
**Liudmila Molkova** 39:44 Meetings still work. I don't… No, on top of my head.
**Laurent Querel** 39:52 Okay.
**Liudmila Molkova** 39:54 No.
And there is a third kind of nasty issue.
So, let's say we had this… defined in Registry A.
And we had B and C, and C depends on B. It does not declare direct dependency on A.
And then it references FU.
What should happen?
Because there is no definition of the… Who in B.
**Laurent Querel** 40:35 But the agency, right? Oh,
**Liudmila Molkova** 40:38 There's one in E.
But we… here we reference something from A.
Oh, okay, okay. The definition of it does not exist in… B. There are some references.
So… it, like, was… if we give Weaver just resolved schemas.
Then things work correctly today. We crash… well, we don't crash, we error out, we say that the foo is not resolved.
which seems to be a right. Assume, like, our principle is that we don't re-expose things from dependencies. They are not public by default.
And then…
**Laurent Querel** 41:27 If…
**Liudmila Molkova** 41:28 we give definition schemas to Weaver. Like, if we give B… If… if we give… if… we give… B definition schema to C.
Then, it doesn't ever out.
Even worse, it says that it comes from B.
**Laurent Querel** 41:52 Well, that was not my understanding, but I missed so many iterations on V2 that I could be wrong, but my interpretation of matrix refinement, the IDB refined ref A metric.
My interpretation in that case was.
I inherit everything from a metric.
So the attributes are illerated.
And the refinement is only additive or overriding things.
It's not removing.
In this specific case.
So, my expectation for… Name symmetric, attribute F2, I expect to see Foo, because FU was based… was existing in A.
If who… if who exists in A, I should see… I should see who.
**Liudmila Molkova** 42:48 Right? What version, right? So, like…
**Laurent Querel** 42:51 The… the version from… Bom… I think it's a choice, I… Because there is no refinement of in B, I was expecting to see the attribute from A, but maybe… The choice could be, oh, because there is a refinement, we inherit every attribute, and we redefine them by default, in the context of B, That I don't know if that was the choice.
**Liudmila Molkova** 43:27 So the… I think the… the choice, the design choice is that Let's say I'm a B, And I… reference some attributes. So, rule a refinement or directly.
Then, my results schema.
contains… Only the refs for external attributes.
But not the original definitions.
And I don't make… Like, we require explicit dependency on something to use its definitions, signals, or attributes.
You cannot get definition of something through transitive… from transitive dependency.
**Laurent Querel** 44:19 But it's a form of dependency. If you are refining… a metric in B, you are basically saying that you have a direct dependency on all the attributes of A.
**Liudmila Molkova** 44:34 All the applicable variants of these attributes.
**Laurent Querel** 44:42 Alright, I didn't fall asleep.
**Liudmila Molkova** 44:46 So let's say… It has… Who, and the brief is the fu.
**Laurent Querel** 44:58 Yeah.
**Liudmila Molkova** 44:59 And B.
I have metric… Be metric?
**Laurent Querel** 45:06 D.
**Liudmila Molkova** 45:07 I guess,
**Laurent Querel** 45:11 You have biometric or a metric? Amyric.
I guess.
In B, you have a reference to A.
**Liudmila Molkova** 45:18 Oh, right, yes.
I have metric, rough… Or… Okay, so I have… a metric.
That's cool.
And then I have metric ref.
Where I see… Who?
It was brief.
from B.
than in C.
So, as… if we're looking to resolve schemas.
What would they see from B?
Only this version of fool.
**Laurent Querel** 46:29 The Fouffron bee?
That, I understand, but that's not the last example you had in, Oh, maybe I'm misinterpreting, yeah, this one.
you, you, you… you didn't, in B.
You didn't… okay, oh my god, I think I understood.
No,
**Liudmila Molkova** 47:03 B only exists here to reference some version of foo.
**Laurent Querel** 47:08 Okay.
**Liudmila Molkova** 47:11 And the test is version and C.
should not use this version of it should… Error out.
And given a different design choice, if we allowed to use things from transitive dependencies.
We would resolve the original definition.
**Laurent Querel** 47:34 Mmm.
Yeah, the full year is… Yeah, okay, I agree, yeah. If we consider that Whatever we inherit, it's reserved.
And then what is believable in the resolution… in this resolution is… is like in life check. In fact, it's metric… it's signal-driven, so we have all the signals that are reserved.
So the… the… basically the attributes that are of a lean or… or fear, orphan.
Of any signal are not visible anymore.
So, Fu… if Fu was not… Because it's who, in that case, is, outside of any signal scope.
Then, yeah.
**Liudmila Molkova** 48:35 Right.
**Laurent Querel** 48:36 We can't, I totally agree with that. Now, the question, probably, that you have is… Is it an expected behavior to be able to get access to an attribute that, let's say, that is defined in Semantic Convention.
I would say probably yes, because, that's the purpose of the… the standard open telemetry Semantic Convention Registry to offer A catalog of attributes.
So we should be able to… To get access to the attributes bar.
Yeah.
**Liudmila Molkova** 49:25 it's kind of a choice, right? So, I think… I think it's the… the principal design decision. So, I think Josh really felt strong about, following, like, JavaScript or Rust principle that you're… you don't re-export.
Things from your dependencies by default.
but… If we… Followed a different design choice of everything that depends on semantic conventions.
Would include all of the semantic conventions in the result schema, right?
Because, like, Or all the consumers will be forced to re-resolve semantic conventions again.
**Laurent Querel** 50:13 Yeah, but in Rust, for example, if we had to do… to emulate that, We… in the, in the root Semantic Convention, the one from Upper 1083, we will have to say, oh, by the way, I want to expose publicly all my attributes. So you put the decision of what to expose, where those attributes are defined.
And then, now you have a custom registry iterating from OpenTelemetry.
It's your decision to propagate, To the… to the upstream, registry, potentially.
But at least if you iner it, we are supporting, multi, multi, inheritance, right?
Okay, so we could have someone, inheriting from registry A.
And inheriting from open telemetry Registry.
And then you will get access to the public attribute that has been exposed into OpenTelemetry.
Even if A didn't re-expose them.
Because it's… for me, A is… not necessarily, but it could be, like, a terminal registry. It's a… it's a registry representing an application, a service.
And, it happens that you want to extend it for whatever reason, service A prim or application B.
Then, in order to serve this, non-exposure of attributes, because it's a choice of A, You could, iterate the attributes from OpenTelemetry, and that should work.
I think the… That's how that will work inside REST, in fact.
Because, indeed, in the crate, if you don't re-expose something that you already get from a transitive dependency, that will not be visible. But you could, you could if you want.
And no symptoms.
**Liudmila Molkova** 52:31 This is the… the imports, right? I would… I don't… don't remember, but I think imports is the mechanism.
**Laurent Querel** 52:37 Yeah, the, the use, pub, pub use, I think that's, How you make, when you say use blah.
If you put pub in front of use, then you are basically saying, oh, by the way, this use is public.
And then it's becoming part of Maguire definition.
**Liudmila Molkova** 52:59 Right, and then for Semantic… for… registries, this is the imports. So you can say, I import.
**Laurent Querel** 53:05 Yeah, yeah, yeah, yeah, yeah.
**Liudmila Molkova** 53:07 And what Jeremy is saying, that there is no imports for attributes, so I cannot re-export them.
**Laurent Querel** 53:13 There is no way to specify in open telemetry registry.
That, for this one, we consider all attributes public.
And maybe that's what is missing. Obviously, this ability to make things public Could be used, for any registry, even if Sweet.
We could imagine that, let's say, we are in a big company, Google, Microsoft, or whatever, and And there are some intermediary registry.
implemented by a business unit. They are not terminal, because they are not corresponding to an application or to a service.
In that case, we could use the same mechanism that we use into the… that we could use into the Semantic convention, because it's something that is intended to be shared and reused many times.
then we just explicitly say, okay, that is public, public, public, public. Maybe something, some element will be just internal for the purpose of Minimizing the… the rewriting, or, But, and then we have… Custom registries that are related to an app or a service.
Then we don't have to re-expose, because they are usually terminal, except maybe in some very specific situation, and we have a full-back approach. We have a mechanism to… In the case where we want to inherit from those final registries to get the… The, the region, of the transitive dependency and included it directly.
**Liudmila Molkova** 55:03 Yeah, I think that the imports for attributes is useful. It has to be our target, not to the life check problem we have, because life check needs to relate against everything, not just what is meaningful to be re-exported.
**Laurent Querel** 55:21 Yeah, when I, when I, I was listening, My frustration was, okay, life check is… is… Signal-driven, and not really attribute-driven.
But one point, I think, that was fair from… from Jeremy was, what he said about resource.
Similarly, we could say the same thing for scope.
I think there is something missing in the Semantic conventional registry.
To express that, because, yeah, we should be able to say… that, I'm expecting in the context of my… app or enterprise. I'm expecting some… Required attribute in resource.
**Liudmila Molkova** 56:09 Yes.
This is entities, right? The entities have type, and…
**Laurent Querel** 56:14 for me.
**Liudmila Molkova** 56:14 Did you sleep?
**Laurent Querel** 56:15 Space Resort.
**Liudmila Molkova** 56:16 courses.
**Laurent Querel** 56:19 I don't think, yes.
We resulted it slightly differently in our case. We used it as a scope attribute.
Oh, okay.
**Liudmila Molkova** 56:33 Oh.
**Laurent Querel** 56:34 And the reason… and the reason why we do that, and personally, I strongly prefer this approach, but, it's… maybe it's totally wrong, but the… for us, an application or service is a collection of interrelated entities.
So the, and, and we want to be able to… to every… event or metric Produced or emitted by an entity.
Are, basically sharing the same attributes of this entity, and they are represented into the… as a scope… a set of scope attributes.
So we could have as much as entities into a single process that are properly interrelated.
It's working because we… resources are for the global process. They are not necessarily related to an internal entity. Internal entities are representative risk of attributes, in our case.
**Liudmila Molkova** 57:35 Yeah, sorry, I need to drop. It's very interesting, by the way, and you're… I think you should tell Josh about it, because he is actively working on this.
**Laurent Querel** 57:48 Yeah, yeah, yeah.
**Liudmila Molkova** 57:49 The multi-tenant story, yeah.
**Laurent Querel** 57:51 Yeah, hopefully, like I said last time, in August, I should demo… I should do a demo of the… how we… we… we did internal telemetry into the Hotel Arrow project.
Because the intent is definitely to use Weaver and Semantic Convention.
And I will present this way of representing entities, and why I think it's… It's powerful to do this way.
**Liudmila Molkova** 58:18 Yeah, thanks. I need to drop.
**Laurent Querel** 58:20 That's great to see you.
**Liudmila Molkova** 58:21 Yeah, be around.
**Laurent Querel** 58:23 Yeah, bye.
