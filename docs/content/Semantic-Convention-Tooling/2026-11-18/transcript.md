SIG: Semantic Convention Tooling
Date: 2026-11-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 00:36 Hey!
**Jeremy Blythe** 00:38 Hello?
**Josh Suereth (Google LLC)** 00:40 A little slow, sorry. How you doing?
**Jeremy Blythe** 00:42 I'm good, how are you?
**Josh Suereth (Google LLC)** 00:44 Not bad, not bad.
I spent 2 weeks on that PR.
**Jeremy Blythe** 00:51 HPL's that? Sorry.
**Josh Suereth (Google LLC)** 00:53 The one I put in chat. I'm gonna… I'll add it to our… Notes here.
It's a doozy.
**Jeremy Blythe** 01:06 Oh, this is the, oh, okay. Yeah, that's a big one.
**Josh Suereth (Google LLC)** 01:14 Yeah, I was trying to figure out if I can fragment it, and what that would be.
like, the original plan that I walked through with, like, Claude going through all the different pieces was, not something I would inflict on the rest of you.
Because it was, like, a lot of little tiny things that each step looked really stupid.
Yeah, the goal was that this is what we get down to for Resolve, so this is what Resolve is supposed to look like. It actually changed a little bit.
But the notion that you have, like, attribute definitions, and then groups, and then signals, and then refinements, and then imports, and then, look for span name attributes and validation, and then emit the schema. It's kind of similar to this, it's a little bit bigger, though, it's like a 15-step thing.
Because… I found a ton of dependency resolution problems.
Where there were weird things where if you converted from V2 to V1, V1 allowed all this stuff that, when you implement V2, you're like, why are we allowing this?
So, yeah, if you want, I'm not… I don't think I'm presenting. I'll walk you through the, the main changes, so you know what it changes.
Semantic Convention Tooling… Here's the PR.
I haven't had a chance to do a lot of code review either, so apologies, because I was doing tons of code review on this. This is… this… I let myself get swamped by this, but effectively, the resolution algorithm is… we build, like, symbol tables, we validate uniqueness, we do dependency resolution and conflicts, we linearize our dependencies, that kind of crap, right?
Then we initialize our catalog and define local attributes.
Like, so we know what the local attribute catalog's gonna be that you resolve with.
Then, we expand all the attribute groups, so all the ref groups get expanded.
Then we resolve all the base signals, so we go through every signal.
and expand all the refs on every signal. Then we resolve all the signal refinements, and make sure we expand all those into full definitions. Then at the end, we resolve all imports, where you have those import statements, or you say include all unreferenced, and we expand out all the capabilities for imports.
Finally, we look for entity associations, so we make sure every entity association is valid, and we create our real attribute catalog, where everything's minimized and indexed and all that kind of crap.
And we dump out the V2 schema.
So, each one of these steps is a lot easier to read with V2, because everything's in V2.
What I want to show you, though, Because this is huge.
There's a lot more tests and changes that we added, so, like, the… Added a few more expected changes, and… things that weren't tested before, so you can see what all of those are, because I wanted to expand test coverage ahead of time.
Here, let's start with this. So if we go to the changelog.
you can see breaking changes. First one.
You could define duplicate refs in the ref list.
Don't know why we allowed it.
Don't know why you would do it.
But it was in some of our test cases, so I just… it's now an error.
I hope that's not… Contentious?
**Liudmila Molkova** 05:00 No, not at all.
**Josh Suereth (Google LLC)** 05:02 Okay.
The next one's kind of fun. When we were doing dependency upgrades, right, so if we pick a newer compatible version.
We could do an upgrade where the new version doesn't actually have the attribute.
Because we never actually resolved the new version to make sure of. So if we only ever saw the attribute in the previous version, and we don't actually look at the new version, we would just silently make an upgrade, but not check.
So this one actually now checks the new version. It will look for it.
Where before it didn't. Before it would, like, say, oh, you know, I have that transitive dependency on something where one is on version 2.1 and one is on version 2.0. It will actually resolve 2.1 and look at the attribute in 2.1, for sure.
And say, does it actually exist here? And if it doesn't, it'll tell you, hey, you're depending on something in 2.0 that doesn't exist in 2.1, and we have to be on 2.1.
So you actually have a dependency conflict.
Where it wouldn't before.
In practice, I don't think this has happened.
But in our test cases and things, it did. So, cool.
Alright.
Next breaking change… There… we have this, like, imports That was pre-resolved?
This is a breaking change, I need to change what this means is breaking change. This is a breaking change to users of the API.
So the API for talking to the resolver has changed.
The cash that you get back and the way you interact with the cache is slightly different.
You'll see that when you look in the code.
So, this was… I was yelling at Claude for having terrible documentation and not marking things breaking, and I think it was a little aggressive.
But that is… it is a breaking change for people who use our API, it's not a breaking change for Weaver users.
Okay, next thing.
It turns out, if you had dependency resolution exclude true across dependency boundaries, there were some instances where things were able to slip through. I don't know how.
But I added some explicit exclusions to make sure they weren't crossing boundaries.
Okay?
**Liudmila Molkova** 07:28 I read that you didn't… don't know how.
**Josh Suereth (Google LLC)** 07:32 I… yeah, well, when you… if you read the code, like, this one, when it sent me the diff for the fix, it was obvious that, oh yeah, that's a problem, and V2 caught this, and it's broken, and we shouldn't do it, but I don't… when I read through our algorithm that we had before, I don't know how it slipped through.
**Liudmila Molkova** 07:49 Yeah.
**Josh Suereth (Google LLC)** 07:50 Which is a sign that maybe we should be cleaning up the algorithm.
Okay.
The next thing here, we actually start getting deprecated signal ref groups. So this is… this is a… this was a decision. We could make this be a breaking change, but I did not, because, Semantic Conventions GenAI uses this. If you use refgroup.
And you target something that's not an attribute group, like you ref group a span, or you ref group a metric.
It is allowed, but marked as deprecated.
And tells you to stop doing that, and turn it into an attribute group.
**Liudmila Molkova** 08:27 Wha- why is that… why cannot we just… rejected?
**Josh Suereth (Google LLC)** 08:33 We can reject it, but it's actively in use by Gen AI Semantic conventions.
**Liudmila Molkova** 08:39 I'll check. I don't think it's intentional.
**Josh Suereth (Google LLC)** 08:43 Okay. It could be that I was working on a stale checkout of GenAI Semantic Conventions and you fixed it, but it was… it was something that was actually being used, and so I, I decided to… by the way, if you use dash dash future, it is a full error.
Okay. But that's why I was like, okay, let's just mark it deprecated, let's clean things up, and then we can come back and make it be a hard error later.
**Liudmila Molkova** 09:07 Okay, I'm… I'm going to check, but keep… keep going. I'll just ask you to check.
**Josh Suereth (Google LLC)** 09:15 Yeah, I can also ask, ask Cloud to tell me where that was a problem. The last thing was, we had an issue where refinements, that it would inherit entity association.
An event name from Refined Signal, right, so… If you tried to inherit from, events, there was some cases where entity associations were not inherited correctly.
Like, they were just not even put there. They were dropped.
We didn't have tests that caught it.
Again, that's another one where you're like, how did we miss this? I don't know, but it was literally just missing a copy the entity refinements over block.
Event name was also missing.
as a thing from Refinement Signal, so the, I need to go take a look at this again to make sure that that was fixed correctly, but that's another… another one we had bugs with, where you were able to change the event name, but you shouldn't have been.
And the other thing we do is we linearize the dependencies, before we send to Forge.
So that's, like, the Python notion of linearization, so you get, like, one version for every dependency and a big line, and then when we send it to Forge, since we've linearized the dependencies, you get them all where you don't have to follow all of the weird, like, you have two versions of the same thing.
You get the full, like, just one definition and list for everything.
That one, I think, Jeremy, I want you to take a look at to see what you think, because this has impacts on, it uses all the stuff that you created for Forge and for, live check?
It's just the experience is slightly different now because of how we are looking at the dependency chain.
**Jeremy Blythe** 11:14 Okay.
**Josh Suereth (Google LLC)** 11:16 Okay, so that's the set of differences. Does any of that seem scary?
**Liudmila Molkova** 11:22 No.
**Jeremy Blythe** 11:23 Okay.
**Josh Suereth (Google LLC)** 11:24 Now for the fun, I'm gonna show you… oh, by the way, I have a hard stop in 15 minutes, sorry.
So, I wanted to get through this, and then, and then, but… I want to get through the basics so you know how to review this. Alright.
So inside of… Inside of Weaver Resolver.
Let me go up here and close some things. Hold on.
So, in Weaver Resolver, there's a lot of new test cases that have been added, or updated. You can take a look at what those are, it's things like, moving moving directories so that they have a consistent naming scheme, because I updated the test harness to be more consistent, and I'll show you that in a second.
We have docs for how… The resolution should work, and how dispatch works.
That I would recommend reading if you want to see, like, what it built. These are a little… I had Gemini go try to clean up the Claude comments.
Because sometimes that's successful, but they're still entirely too AI-y, in my mind, so it takes you a little bit extra to grok them. Apologies, I can clean them up further.
Here's… here's… here's what's… what's changed. First off, we have a graph library.
The graph library is about looking at the dependency graph, dealing with conflicts, upgrading dependencies from version A to version B, so if you depend on an attribute, but… and it's at 1 and you have to go to 2, all that logic is in graph and is now shared between V1 and V2.
Okay?
So I'm actually pretty, I'm happy with this at a high level. The details, like, if we want to nitpick the different APIs and things, let me know, because I can go clean those up. But at a high level, I think this made it a lot clearer, and actually helped us get rid of a lot of bugs.
Okay.
Next, we have a V1 and a V2. V1 is V1 dependency resolution.
This gets used any time V1 is involved.
Even if you specified the V2 flag, but you'll get a warning saying, hey, you specified V2, but you have XYZ in V1 format, so I have to fall back to V1 resolution.
**Liudmila Molkova** 13:44 Okay, and there we would have… we didn't change anything for V1, so there are probably some bugs there, but we don't care because, yeah.
**Josh Suereth (Google LLC)** 13:55 This, this, theoretically fixed those bugs for V1.
**Liudmila Molkova** 13:59 Okay.
**Josh Suereth (Google LLC)** 14:00 Which is why there's a bunch of diffs here.
Now, was I able to read V1 and say, yes, I think this is how it should be? We were already at the state where maintaining V1 was problematic, and I was wrong half the time anyway, so… For context, I'm relying on the unit test to tell me whether or not this code is correct.
And I'm admitting that publicly in a recorded meeting.
V2, I think, we were able to kind of go through and look at. So, let me close this and go to V2. So, in V2, there's a dependency… oh, both of them have a dependency submodule, which is how to take dependencies, like resolve schema from V2 and turn it into the things you need. So, for example, if you remember, we had this, Yeah, we had this notion of a dependency, and on the dependency, you can… that's how you get it from a resolved schema.
Where is that? Yeah, we had, like, lookup attribute, give me the schema URL, look up a signal, right? There's a different version of the dependency abstraction for V1 versus V2.
And then there's, the V1, when it… when you call, like, lookup signal, it will convert it into things that we need in V2 style, so it actually does the conversion on the fly.
like we had before, but there's, like, one for V1, one for V2, since we're resolving in V2 shape. So when you read the actual algorithm, it's a bit easier to read.
So when we get to… mod, this is, like, the big, the big algorithm here, okay?
is this resolution algorithm, and this is a bit longer than I want. It is… I think, if we look… Where did we get to?
It's like a… it's about 100 lines of code, right? But it's that set of things I was telling you about, where there's, like, 11 steps, where the first thing we do is we kind of resolve, We resolve all our dependencies appropriately.
We linearize our dependencies and get our chosen versions, that's what this is.
And once we have our pinned schemas, we go make sure everything's pinned to those chosen dependencies.
And once that's all done, the real resolution algorithm can start.
So, this is where we're finally done pinning dependencies, and everything looks good, and we have this V2 way of resolving them, where even if the dependency was V1 or whatever, this gives us the V2 view.
So then, I can actually start, okay, creating my lookup indices.
This is where I start creating, for efficiency reasons, because I actually did a performance pass-through. I'll create a thing that can do fast lookups.
by version, by signal name, that kind of crap. This is where we create the catalog, where all the attributes will be, and then we start doing all the shenanigans of, okay.
expand all the groups, right? Take all of the, all of my attribute groups and look for the refs and the ref signals and ref groups and expand them. Let me start resolving all my signals, so I go look at all the signal definitions and anything that's a ref, I start filling out the ref groups and the refs from the stuff I've expanded so far.
Then I do my refinements, because I need signals to do refinements. And then I resolve all the imports. These are all the import definitions, or that, you know, include unreferenced crap.
Resolve the annotations.
and then finalize the catalog. And each of these is actually relatively easy to read through and see what it's doing. So, like, if you want to see resolve associations for entities, it's not necessarily that it's small.
But if we go to… Resolve.
Associations? What was it called?
Oh god, I'm searching across the whole stupid thing. Hold on.
I have so many pop-ups right now. Sorry.
Let's come back here.
I'll just scroll down.
And I already passed it, didn't I? Yeah, that's schema.
I guess I could show you that, because this is actually creating, like.
We're creating these key lookup values and things, and looking for entity refinements and vectors, turning them into a schema thing.
That's the test.
Did I pass the logic already? Was it that small?
I might have.
I'm sorry, guys, I'm, like, struggling in GitHub to show you what this looks like, because it's not my editor.
Symbols want to resolve directly into V2 format.
Wait, this is a mitt.
This is an entities, where's the entities one?
Here it is. Is this… this is it, right?
No, this is a mitt again.
What the… did… Am I insane? Git… I've clicked on entities, and GitHub is showing me the emit, which is the final schema emission.
**Liudmila Molkova** 19:29 It sometimes opens something else.
**Josh Suereth (Google LLC)** 19:32 Because I think this is just too big. Yeah, you might actually have to check it out and enjoy it. Anyway, let's try… maybe refinement?
Here we go.
Again, this is… it's a bit of code, but this is the refinement code. So if you look at this, you can see all the checks are like, is this the wrong kind of base, is now a check.
Where we look and say, if it's a span, but it shouldn't be a span, issue invalid refinement. If it's a metric, and you're refining something that's not a metric, it issues an error. All that kind of junk.
Helper methods are decent, and prepare refinement attributes. Where's the actual logic here?
Further down, I think it's near the bottom.
Apply attribute overrides. Again, all of these methods were a lot easier to read. I… This is annoying. I… right before this meeting, I told it its comments were super ugly.
And not useful, and that it should clean them up, it deleted them all.
So, I'll add the method comments back. I asked it to follow your guide, Jeremy, and this is what it did.
**Liudmila Molkova** 20:41 copy Anslop skill from GenAI Semantic Conventions.
**Josh Suereth (Google LLC)** 20:45 I, I, I think I need to do that, the unstop skill? Okay.
Anyway, these are pretty good. So, like, apply span attribute overrides, right? We just iterate over all of the, merge items, which are the group attribute items and the ID of those things. We iterate over the existing attribute and RECS and the existing, ampersands, and we do our merge.
And resolve the attribute in the catalog.
So, I found this a lot easier to read, it does create a lot of temporary structures, so for example, for metric refinements, it creates a structure for you to understand who the parent is, which is kind of a duplication of the underlying signal, and it's like.
then creates a lookup, so you can actually read the lookup logic to say, is it finding the right signals from the current catalog correctly?
And it's using some shenanigans to deal with V1 versus V2.
But I was, I was pretty happy with the outcome of this.
Okay, I only have 5 minutes left, and I wasted a lot just walking through the code, maybe uselessly.
Here's the question.
what do you want me to spend time on with this going forward? Like, do you think it's reviewable now? Do you want me to spend more time… I spent about 2 weeks of clawed hell, getting it to the state it's in now.
I think the… if you look at the unit tests, which I think I forgot to show you, the unit tests are actually kind of awesome, because what it does, it takes… it took every V1 unit test and made a secondary harness that will run it through the V2 resolution algorithm.
And validate if you go through V1 and V2, you get the same thing.
In V2. So, if you go through the V1 path and get to V2, and then if you go through V2, you would get the exact same resolution after this, which I was really happy with.
I also had it run your downstream check with this build.
I need to go check that again to make sure that we didn't get the error that says it's not using the V2 resolution.
Because I forgot to do that. I was just like, oh, it built, and it succeeded. Great. But I need to make sure that we didn't get that error message.
But yeah, I'm curious, like, what you guys want to see from this before I mark it for review.
**Liudmila Molkova** 23:10 I… created… I don't know if it will be fixed. So, okay, so I created… the draft for a Semconf core published schema, and during this, I found a few funny issues, for example, I don't know, we have some attributes in catalog that nobody is using, some refs, orphaned refs, that were supposed to be gone, and a bunch of…
**Josh Suereth (Google LLC)** 23:38 That's… that's one of the bugs I found, yeah.
**Liudmila Molkova** 23:40 Oh, cool! So, I'll just take the bugs that I filed, and I'll ask AI to check them against your PR and see what stays.
**Josh Suereth (Google LLC)** 23:51 Okay.
That sounds good.
I'm gonna go through and try to clean up some of the function signatures and maybe prune down some functions.
maybe get rid of some helper structs over time, because I think it was a little bit aggressive with those.
I'm… like, right now, I think the code is readable?
But not, like, clean clean, right?
And my focus was on getting the unit tests and the actual feature set done.
for whether or not we can maintain this going forward. So.
My opinion is this is more maintainable than what we previously had.
But…
**Jeremy Blythe** 24:29 Did you say there was a, like, a spec document that describes Yes. Everything that it's doing now?
**Josh Suereth (Google LLC)** 24:36 Yeah, there's a markdown document that describes how the V2 resolution algorithm works.
**Jeremy Blythe** 24:40 Okay.
**Josh Suereth (Google LLC)** 24:41 And that, I would argue.
**Jeremy Blythe** 24:43 Is that, like, reverse-generated from… Like, is that… was it… did Claude generate that at the same time it was writing the code, or did you write that and then it used that to write the code, or, like, it was like a feedback loop?
**Josh Suereth (Google LLC)** 24:56 Feedback loop.
**Jeremy Blythe** 24:57 Okay, yeah.
**Josh Suereth (Google LLC)** 24:59 Yeah, we started with the spec document, wrote that down.
then as Claude made changes, it would automatically update the spec document to make it less readable.
**Jeremy Blythe** 25:08 Yeah.
I think… I… what I would… what I can't do, what I will do, I'll check it out.
And then, do a whole, sort of, battle-test it with feedback loops of, like, Here's the spec.
How about it, like…
**Josh Suereth (Google LLC)** 25:32 Yeah.
**Jeremy Blythe** 25:33 you know.
Break it.
Be super pedantic and break this thing.
And then… and see what… see what it comes up with, because something of this size, it's like, we're not going to go through every line of code. There's no way.
**Josh Suereth (Google LLC)** 25:46 Yeah, agreed.
**Liudmila Molkova** 25:48 But most of this are the test stuff. I checked, like, if you collapse the test directory, the data directory, the rest is relatively small. But I would not read it all anyway, yeah, I agree.
**Josh Suereth (Google LLC)** 26:00 I… the thing I want to make sure that we agree on is the spec for the algorithm.
**Jeremy Blythe** 26:05 Yeah.
**Josh Suereth (Google LLC)** 26:05 And, like, that these are the right actions to take.
And then, the things I'm doing with dependency resolution with, like, graph and conflict upgrades, I'll try to make sure that's more apparent to everybody what's going on.
Because that's also a bit, that was fun, I should say, to get all that up, up and running, and that is the trickiest code we will have in Weaver overall.
Right? It's all the dependency diamond hell, conflict resolution stuff.
I'm happy with where we're getting to, because I think… the primitives we have in this are the right primitives. Whether or not those primitives are the right shape, or we can clean them up, or make them easier to understand, I think there's still work to do there. But I think we're getting to the point where we have the right primitives in place. Like that graph library for interacting with the dependency graph.
I don't know why I didn't think to add that earlier. That is incredibly meaningful and helpful, and I think will make our maintenance burden a lot easier here.
**Liudmila Molkova** 27:08 Nice.
**Jeremy Blythe** 27:09 Okay, looks good.
**Josh Suereth (Google LLC)** 27:11 Cool. I wanna talk about releases and things, but I gotta drop for another meeting, I'm sorry.
thanks for the time and attention, though. Good to see everybody.
**Liudmila Molkova** 27:21 Yeah, before you go, sorry, should we release, or should we wait for this PR to get in?
**Josh Suereth (Google LLC)** 27:28 I would like to wait for this PR if we can get it reviewed.
**Liudmila Molkova** 27:33 Okay, yeah.
**Josh Suereth (Google LLC)** 27:34 Which I think means we release early next week, right before the holiday and all that, yeah.
But…
**Liudmila Molkova** 27:41 Thank you.
**Josh Suereth (Google LLC)** 27:43 If we don't think we can review it in a week, then let's release this week.
**Liudmila Molkova** 27:50 Let's try to release it… sorry, review and release it next week.
**Josh Suereth (Google LLC)** 27:55 Okay, cool. Alright, take a look at the spec, hammer on it.
send me all the stuff, and I will be doing the same. I'm gonna add all of the, the doc comments back, because that… that was a… miss. Alright. I'll see y'all.
**Liudmila Molkova** 28:09 Awesome, thank you.
**Jeremy Blythe** 28:09 Cheers.
**Liudmila Molkova** 28:10 Bye.
Oh, we lost the person who came, right?
**Jeremy Blythe** 28:18 Maybe they heard us say buddy.
I was just gonna say that I got a bit of time So I did a few tidy up some live check, and you've been looking at them. I'm just going through now, and Match, match, match, match, match.
**Liudmila Molkova** 28:40 Yeah, yeah, thanks a lot for working on this.
**Jeremy Blythe** 28:44 No, it's good. They also tidied up a bunch of, really old issues. I think there were ones you had already commented on, saying, hey, can we close this? I'm like.
Okay, well, you said, can we… So I sucked it by closing it.
Cyclops. Yes.
And there were a couple of others that were just old and out of date, but I just thought… I was just trying to, like, do a bit of a tidy up, and… catch up on issues, and I had some old PRs hanging around from ages ago, like the HTTP one. I actually wrote that ages ago.
And so we tested it off and got it back out again.
**Liudmila Molkova** 29:19 You cannot imagine how much easier it makes, everything.
Like…
**Jeremy Blythe** 29:25 huh?
**Liudmila Molkova** 29:25 We already, we already… So the problem is that the gRPC libraries, in Python specifically, are very, demanding for the environment, and they need a bunch of setup.
something is not available, let's say, in Windows or in some other places, that are more exotic.
And then we have all this hockey workarounds to say, okay, we only do this on, let's say, Linux, and so on.
So, yeah, we already built a bunch of prob- like.
workarounds for this, but now we can clean things up in, let's say, conformance repo, where we primarily use Python to slope.
the conformance tests.
**Jeremy Blythe** 30:11 Okay, so this… This is still the… protobuf, but over HTTP, though, right? Is that a problem? Because there's also the standard, which is JSON, over HTTP.
**Liudmila Molkova** 30:24 Okay, maybe. Anyway, so… at… let's see.
**Jeremy Blythe** 30:30 See what it is? Yeah, so there's another, like, Couple of steps.
to take, so the next one is to then support Jason And then, I guess we need… Zip, as well.
**Liudmila Molkova** 30:47 Okay.
**Jeremy Blythe** 30:49 Because most… lots of people, if they're running it in an environment, they have, like, zip As well, right?
Yeah.
**Liudmila Molkova** 31:04 I mean, we can just wait for somebody to ask, or I'll run it and I'll see.
**Jeremy Blythe** 31:10 Yeah, see if it helps you all.
**Liudmila Molkova** 31:11 Just product of office makes the difference.
**Jeremy Blythe** 31:14 If it's helpful, but… If it's still not helpful enough, then I think there are more steps to go. But I left those as a… we'll do that in another PR thing.
Yeah, and the rest of what I was doing, I was just like, what are all the issues for live check? Let's see if I can, like, squash some of these down. I think there are things that we need discussions on, maybe? I've left them out.
But yeah.
I don't think I've got… I don't really have… Anything… you went to GooCom, is it good?
**Liudmila Molkova** 31:47 Yeah, it was great. I wanted to show it, so there was… Laurent was here… was there?
And turns out, we never… Shown what we did for the… Conformance repo, have you seen the conformance stuff?
**Jeremy Blythe** 32:08 Not for a while.
**Liudmila Molkova** 32:09 Okay, so let me find the GitHub page for it, because… I think we built something awesome with The conformance with the life check.
And you played a giant role in this, so you should know. So this is a report built from the Weaver Life Check.
So we can pick some spots, so here it's the HTTP server.
And we can compare different instrumentations, and there are maybe way too many for this view now.
But we can, for example, limit it to, I don't know, something reasonable, PHP.
And then kind of see the different, coverage for attributes across this. And some of this is just the test.
we test Happy Pass and, not some edge cases, so, like, we don't see many of… some of the attributes here.
I can also see what specific instrumentation has.
And, for example, I don't know… Anthropic native.
And we can show the score. There are some findings.
And we can see… what, Findings were for specific attributes, and… and… and so on.
**Jeremy Blythe** 33:45 Wow.
**Liudmila Molkova** 33:47 And… This is all… built in this way, so there are scenarios, let's say there is GNEI stuff, and by language, and then let's say we have This is just, let's say, the typical library usage. There is no open telemetry here, even.
Right, and because it's auto-instrumentation, And there are, like, 5 of them.
They… what they do is they… Configure this, slopped YAML file, but it's the same. It essentially controls the, conformance tests.
It says… gives some metadata, it says where the, like, we'll use mock servers, environment, and these are the scenarios.
So, like, there is this hotel conformance, runner.
That, knows how to run the scenario, knows how to start Weaver and coordinate between them.
And then… what… Each of the scenario… sorry, what we produce As the outcome of this test is data JSON.
This is, I think, maybe… it's not perfect. It needs to be better.
But this is essentially the coverage report.
Like, what received telemetry produces in terms of semantic conventions?
How much do you cover?
And this is what we've seen across all different scenarios.
And these are the findings we found.
And one of the things we probably should do at some point, we would… Say, okay, like, all of them are… have the… all of them are violations, but still not all of them are equally bad. For example, that attribute is missing in the registry, Well, honest ban.
I mean… Kind of wording.
But, like, if required attribute is missing, this is, like, the real violation.
So, maybe we need to introduce something more there, but even without it, it's pretty awesome.
It's been helpful to find so many different issues in all the different places, and to build all this stuff. And then there is some that the conformance report is built on these data JSON files.
**Jeremy Blythe** 36:29 as an.
**Liudmila Molkova** 36:30 Good.
**Jeremy Blythe** 36:33 So you're… Somewhere in here, you were parsing the… output of LifeJack into these Files.
**Liudmila Molkova** 36:42 Yeah, yeah.
**Jeremy Blythe** 36:44 Okay.
So one of the things I hadn't appreciated is… that that JSON output from LifeJack is now, like… it's not… it was just made… I just went, oh, let's put some stuff… Do you know what I mean? I don't know that it was really… you know, there isn't a sort of a schema for it.
But now this is… being heavily relied on, I guess it needs a bit more love to… check that we're not gonna break it. We almost need to version that output, maybe.
Because there are problems.
**Liudmila Molkova** 37:26 Yeah…
**Jeremy Blythe** 37:27 there already are problems in it, right? The… before I… I made that before the… before the thing that… where… where, entities were invented.
Or maybe I didn't know about them when I made it. So I was using… I was using the term entity just like you would use, you know, object or structure. I was using it in that sort of very generic sense. And so now, in that output file, it talks about entities.
But they're not the entities… they're not hotel entities, they're just, you know, generic entities. And so there are already problems in the file that… would mean I would want… like, I really want that entity, I want to change it to samples, but I've not done it because I know I'm gonna… I would break some things.
But it does seem like more care needs to be… There needs to be a bit more, like.
Something in there that, if somebody… does the PR that's going to alter that structure, that's going to cause a big problem.
**Liudmila Molkova** 38:37 Mmm… yeah.
this… I mean, this is still early.
**Jeremy Blythe** 38:46 Who is it.
**Liudmila Molkova** 38:46 Yeah, it's straightforward to fix, right? So, like, we would just… okay, if there is a breaking change in Weaver.
we would update this repo with AI to preserve the outcome. I… I'm not super worried about this for us, at least for this repo.
I'm thinking, like, in the long term, we probably want maybe some more opinionated reports, not just the Bright Jason, but, like.
some, either a limited version of it, or, like, something that would produce a report.
And maybe, as we iterate in this repo, we'll figure out how the report How useful a report could look like.
And we just propose it, and we would put it behind, like, additional, flag. We'll say, okay, like, not just JSON, but… but dash dash, I don't know, report, coverage report.
Or it will be some… some diagnostic format.
That would produce it.
diagnostic template.
**Jeremy Blythe** 40:05 Right.
Because you can provide LiveCheck with, Ginger templates already.
**Liudmila Molkova** 40:14 I… I'm blanking on this. I… I think I tried on something, it didn't work, so it… it does some Python code around, but I'll… I'll recheck.
**Jeremy Blythe** 40:27 Okay.
Well, that's cool. It's very cool to see that used.
It's excellent.
**Liudmila Molkova** 40:35 And we are going to… Hopefully. But, like, the future for this would be the conformance program for OpenTelemetry.
I would actually put something in OpenTelemetry I.O. saying, okay, they saw some people say they are auto-native or whatever, but here is what it means.
In reality.
**Jeremy Blythe** 40:57 Oh, so you could… Do you mean you could be a… you could be a user of OpenCentry, you've got a library?
And you want to get a badge to say that you're… you're conformant, because you're emitting those… conventions.
In your library.
**Liudmila Molkova** 41:16 Well, a page or some other form of endorsement, because, like, if you go to OpenTelemetry.io, there is a registry, there's the ecosystem there, and a lot of things claim that they are OpenTelemetry compatible or native, but it might mean they just emit OTLP and don't support anything else.
Don't follow conventions, don't, like, use spans for logs and whatnot.
**Jeremy Blythe** 41:40 Okay, so you would have to… How would you prove it, then? You have to… Run these conformance tests somehow to prove That your li- your library is… like, if my company wanted to get the hotel conformance badge.
**Liudmila Molkova** 42:00 Well, it's more like for the… If you give… If you use OTEL yourself, probably not.
But then, if you… Provide the library with instrumentation, or you provide a component.
that supports… that works with up and telemetry, and… Like, it meets up in telemetry, telemetry.
And it, let's say it follow… it should follow HTTP conventions, or, like, whatever cloud provider conventions.
**Jeremy Blythe** 42:31 Then…
**Liudmila Molkova** 42:32 You… we would ask to contribute test here.
And the test would show… what's… conformant and what's not. So, for example, This is… Provided by open inference of rice.
This is not up in telemetry instrumentation.
So we just used the same scenario, and we used their library here.
And it tells us what's great in their setup, what's not.
**Jeremy Blythe** 43:06 Right, so you'd have to contribute to this project.
**Liudmila Molkova** 43:11 Yes, if you want.
to open telemetry to… recognize that you were properly support up in telemetry. And, of course, it's… in early stages, all I'm saying, for anybody who is listening, it's not… Something you redo yet, but it's just the first.
Thing in… in… on the way.
**Jeremy Blythe** 43:36 Yeah.
I guess I would also… One of the things we're exploring.
is that it's not necessarily a library, but it's a product. So we make a product And the customer hosts that product.
And if they wish to, they can have the telemetry that the product's producing Send to the backend that they may have.
Right, so they're using our product.
And they've got an observability backend.
It would be good to… if the product itself was… had… had a, A badge on it to say, this product produces conformant.
OpenTelemetry as a commercial closed-source product.
**Liudmila Molkova** 44:28 But then, it is producing your conventions, right? It's not producing something up in telemetry.
**Jeremy Blythe** 44:35 Well, it's a mixture, right? Because now we've got multi-registry, so I've got our own conventions, but they are using open telemetry underneath. So… for example, we'll have, within it, within the product, there'll be HTTP servers.
And so you want to be able to say, well.
You're going to receive, you know, logs and traces and metrics that are… That are compliant. Alongside our… conventions as well. There are… compliant, you know, to such and such a level of open telemetry.
I don't know, I don't know, it's just a thought, but…
**Liudmila Molkova** 45:20 Yeah, it's interesting. I think we are very far from this. It's, like, we are just trying to see if instrumentation libraries are conformant.
alert.
**Jeremy Blythe** 45:33 Yeah, I just wanted to have over… To take it.
**Liudmila Molkova** 45:37 Yeah.
From KubeCon, I've met a per- sorry, go ahead.
**Jeremy Blythe** 45:42 Luna?
**Liudmila Molkova** 45:44 I've met the person who randomly told that they are using Weaver, and they're just a big fan.
And they're using it to represent the whole Splunk Internal, they have on-prem solution.
And they actively use it, and I think they also do the life checks and everything, so it's… it's nice, it seems people are using Weaver, people are excited, and they never show up at these calls or in Slack channels, but they're just using it.
**Jeremy Blythe** 46:17 It's weird, I don't know.
How do you find out who's using it?
**Liudmila Molkova** 46:25 at the conferences.
But, like, the federated conventions, it was also something people were excited about.
And there are… bike.
A lot of external organizations who kind of want to Do this, or are already doing it?
And it's even without us advertising or, like, talking to them. It's just, I don't know, some… Who have I heard of? Well.
We've been actually selling federated conventions to a lot of places, some security foundations, some… other groups in Linux Foundation, but also just random teams at Google.
Or, like, okay, we probably want it.
So?
Great job.
**Jeremy Blythe** 47:26 Wow.
Alright, well, I'll keep squashing the issues.
**Liudmila Molkova** 47:32 Yeah.
I hope after we stabilize the schemas.
I kind of… I want to, for, like, internal Google reasons, to stabilize the… at least some of the commands, the CLI interface.
**Jeremy Blythe** 47:47 Okay.
**Liudmila Molkova** 47:50 Not, like, probably not everything at once, but, like, some of the things. So if we publish, let's say.
Stable schema for semantic conventions, then… The binary that produces it should probably also be stable.
**Jeremy Blythe** 48:07 Yep.
**Liudmila Molkova** 48:08 Yeah, and it seems for Antoine to… Publish Crates, and Crates.io.
**Jeremy Blythe** 48:16 I would like that too, so I… what I've been doing internally… Actually, it is… I decided to… well… I did post it, but I think everyone's busy, but I decided to make it open source, but it's in my… it's just in my name at the moment, but it could be donated to OpenTelemetry if we wanted, but… With AI generating everything now.
We've found that… languages that are really good, that are telling you that your code is bad, like Rust, where the compiler output is so good, the quality of the code that AI produces with Rust is so good, because it has that.
So, I made a library, I'll send the link again if you're interested, but… Specifically for Rust, you can use, prog macros to basically make something like a domain-specific language, so, you know, you can just go, like, put a macro in.
So what it does is, you give it a V2 registry.
And then it basically makes it so your… in your code, you will go spam.
exclamation mark, and then the code you type in looks like the AML that you have in your registry. So you put the name of the… the event.
And then it's type-checked, so it's all then type-checked, because it's built Rust code for the registry. So, it means you get compile time failures. So if you've typed a… if you've typed an event, because you want to emit an event.
But you missed one of the required ones in what you're typing out, you'll get a compile time check that you've missed an event. So it's very opinionated, because now you have to, like, specify… you have to use this language.
It's like a language extension.
So it's really opinionated, but it means that you… your registry and your code Stay aligned.
And now we're using that throughout everything. Like, there's loads of stuff we've been AI generating now.
Where… you've got this feedback loop now, so it's like, well, you can only… you're asking the AI to, like, build you more tracing, or do more… You know, oh, make a metric for this thing, and the only way it can do it is by building something into the registry, following your rules for the registry, and then means it gets back in the language, that means it can do it, and it can, like, loop through and fix the compiler error it would otherwise get, right?
So… these giant, sort of, registries and code are, like, building alongside each other. It's pretty cool.
**Liudmila Molkova** 50:56 Yeah.
Okay, so you build… you write your registry in Rust.
And then it's your library.
essentially converts it into YAML.
**Jeremy Blythe** 51:10 No, no room.
**Liudmila Molkova** 51:11 this.
**Jeremy Blythe** 51:12 You write it, it's… it's a standard Weaver, depackaged output.
**Liudmila Molkova** 51:19 Huh.
**Jeremy Blythe** 51:21 and then in Rust, you make this one call, it's registry. You say registry, and you give it the path to your… A packaged file.
**Liudmila Molkova** 51:31 Huh.
**Jeremy Blythe** 51:33 And then it turns that into… with proc macros, it turns that into Rust code. It turns the entire registry into Rust code.
Which then means as you're typing in, you've got compile time tracks.
**Liudmila Molkova** 51:45 I see. And it's not like the code gen, it's just the schema itself.
you boost the rest, you're able to validate immediately what you type in YAML.
Okay, okay.
**Jeremy Blythe** 51:58 And then AI really likes it, because… It produces compiler errors.
you won't compile, because it's part of… because now it's part of your code, and you're breaking Rust.
So it's all type-safe.
I'll send you…
**Liudmila Molkova** 52:12 Nice.
Yeah.
It's better than JSON schema, because, like, in IDE, you would use a JSON schema validation for this.
**Jeremy Blythe** 52:24 And, so I was going through it with… I was saying, what, what?
could I do this in other languages, Claude? And it's like, whoa, a C Sharp would be a really good one, because it has a similar way of doing, that kind of language extension stuff. And I think there's a whole bunch of stuff in C-sharp where you… you just kind of fall into, like, SQL or things like that.
Similar thing to that.
Yeah.
**Liudmila Molkova** 52:47 It also has static, like, the code generation, that you… it can generate C-sharp code and hide it from… from… The ugly one, yeah.
**Jeremy Blythe** 52:57 And then for… there's something in Drava that… It says… is… close, something in Go that's close, and then it's like, well, but if you want to do Python or whatever, you'd have to write linter.
But you could still do something.
Anyway… I'll send the link.
**Liudmila Molkova** 53:17 Yeah, that's cool.
**Jeremy Blythe** 53:19 It's, so I… just… Inside of this library.
What I really wanted to do was use the Weaver Great. So this is the… Just coming back to why it would be nice to have the crates.
Because, really, I… I ended up going, like, oh, well, I can't use the crate, so I'll just… Generate those structures.
Again.
Whereas I'd like to just use the WeaverSimconf.
Crate.
Because it's… this library's in Crates.io. Yeah.
**Liudmila Molkova** 53:59 Yeah.
I think, like, we would eventually provide this. It's just, I feel like we never put any thought, any good thought, into what public API should be.
And documentation for the API, and, like, the entry points that are clear.
So, probably, we'll need to massage it a bit. But, like, if we ship batter, it's fine.
**Jeremy Blythe** 54:25 There you go, I just gave you the link.
Yeah, I just put it in Create Slayer.
**Liudmila Molkova** 54:36 Nice.
Can you write a dashboard in Rust?
**Jeremy Blythe** 54:43 The dashboard?
**Liudmila Molkova** 54:44 Like a query.
Like, semantic… the query around semantic conventions.
In rest.
**Jeremy Blythe** 54:55 to do what?
Sorry, I didn't…
**Liudmila Molkova** 55:01 So, we kind of miss… the piece in Semantic Convention that tells how to… how to… Query the data, because there is no common query language.
And, like, What if we could generate a query in… some languages.
Assuming… The data is this.
The data is based on semantic conventions.
**Jeremy Blythe** 55:30 What are you querying, though? Sorry, I don't follow that.
**Liudmila Molkova** 55:34 like… give me the P95 of this metric, or give me the…
**Jeremy Blythe** 55:40 Oh my god.
**Liudmila Molkova** 55:41 all the spans with a certain type or name, and… I don't know, aggregate over. It's probably some form of SQL, but it's just that If you can write it in a language.
And it's probably query language anyway. Yeah, sorry, I was…
**Jeremy Blythe** 56:02 So to, like, query your back… query your observability backend.
Right, yeah.
I mean, it depends on the backend, right?
**Liudmila Molkova** 56:15 Yeah.
But I could… it's just… you made me think about this, because you mentioned the C-sharp that has the, like, the SQL-style programming.
And essentially, it's pretty similar, or like… the… in Rust, the query would look pretty ugly, but it still has the same properties, right? You have, I don't know, a vector of spans, and you… filter them, and then you map them, and, aggregate, and, like, this, pattern of doing processing, it exists in pretty much any language.
It's just the… the… Efficiency depends on the storage and specific syntax.
**Jeremy Blythe** 56:59 No.
**Liudmila Molkova** 57:02 Yeah.
**Jeremy Blythe** 57:03 I guess there are probably some… Libraries like this.
Fourth, full sequel.
They probably already are.
It's, it seems to be upon those.
It was actually a colleague, was like, hey, have you thought about doing it using proc macros? Like, the guy who wrote all the survey stuff has got a really good guide for how you do it, and Libraries and all of that, that… you can pull in, and I'm like, really? Oh, let's go have a look. Of course, it's easy now, because proc macros are horrible. The code for proc macros is really horrible, but, like, it doesn't matter if Claude can write it, I don't have to write it, so it's fine.
So, yeah, and it just turns out to be… It's just really nice, and what I found… No, it's like… because we're not writing the code, the AI's writing the code, but when you want to go and look at it, you can now see, oh, it's… there is… there's my span, it's got url.path, and it's got http.root, and that's… I'm looking at it in there, and it's not just a mess of, like, constants and things that don't look like the conventions anymore.
Because I'm reviewing the code, I can go like, oh yeah, that's a good span to put there, you know, if I'm getting that detailed. So that's kind of where I was coming from with it.
Because I don't think you can type it in by hand.
But it's very visible.
**Liudmila Molkova** 58:27 And then it kinda is a replacement for the code generation, right?
**Jeremy Blythe** 58:33 It is, yes. So we're using this, and we're not doing coaching.
We don't need to.
**Liudmila Molkova** 58:37 Okay.
**Jeremy Blythe** 58:41 Anyway.
We're at time, so…
**Liudmila Molkova** 58:44 That's awesome. Okay, yeah, thank you.
**Jeremy Blythe** 58:46 Alright, have a… see you next week. Cheers.
**Liudmila Molkova** 58:49 to you.
