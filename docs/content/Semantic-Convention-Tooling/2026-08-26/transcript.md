SIG: Semantic Convention Tooling
Date: 2026-08-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 02:10 Hey.
Are there really two Ludmilas here?
**Liudmila Molkova** 02:19 Okay, so… I joined… And I was alone here, and you know how we have two versions of Meetings now, so I left.
And join again, and that's the hold with Mila. She's still… Check-in.
Cool, so it seems we are ready to release a new weaver, right?
**Josh Suereth (Google LLC)** 02:53 I think so, I think that's the main thing to talk about today. Jeremy's not gonna be able to join until 10.30.
Yeah. Yeah, I was going through… there's, There's a fix someone has here that I didn't have a chance to, like, look in detail or think through.
Did they get merged already?
Truncating local paths that contain at.
It… Yeah.
There's some implications on that one.
And then we have, Rust just updated.
to… like, the new one came out, so I don't know if we want to, like, bump Rust and do all the clippy fixes and things now or later. I'm fine doing it later.
But that's the… that's, like, one of the pending PRs here, is, Rust is 1.98 now. In terms of what it fixes, The one thing I think actually might affect us, but only in good ways, which is stuff around floating point and const, which we do kind of use in our, mini ginger.
Repo.
like, I remember the release notes actually specifically mentioned Mini Jinja for some reason as impacted by the new Rust update, and I don't remember why. There was something that it does better.
**Liudmila Molkova** 04:20 Mmm, better, that's good.
**Josh Suereth (Google LLC)** 04:22 Yeah, I don't remember what it was, though, and so I don't know if it's urgent that we pull it in.
By the way, that's not the only place we have to update Rust, that is just for the Docker image.
**Liudmila Molkova** 04:37 Right.
We can then update them independently, we don't need to do it atomically.
Wait.
**Josh Suereth (Google LLC)** 04:43 Yeah, I don't think we need to do either of that for the release. I think we could actually cut a release, and then do the Rust update, and then deal with the changes post-release, unless we are afraid that we have anything breaking. But nightly passed, right? You got Nightly working?
**Liudmila Molkova** 04:59 Yes, nightly passed twice. I didn't check this night.
But… Yes.
**Josh Suereth (Google LLC)** 05:08 Let me look at the Insulin Tree Bever packages, because I think there was, You have… you have a few changes here, right? Yeah.
**Liudmila Molkova** 05:20 Oh.
**Josh Suereth (Google LLC)** 05:21 Oh, my fixed Weaver nightly build that I have don't merge until Weaver's released, you actually… Did it anyway.
**Liudmila Molkova** 05:29 Oh, sorry, I didn't notice you had a PR for this.
**Josh Suereth (Google LLC)** 05:32 Okay, alright.
I was gonna… I was gonna release Weaver and then remove it, so that people who aren't using the latest Weaver still get errors, but it's fine. I don't think people are really using this that much anyway.
**Liudmila Molkova** 05:46 Oh, I made it in a compatible way, so the fixes the shape of the entity.
association, and I just conditionally skip the policy if, it's a complex object, because we…
**Josh Suereth (Google LLC)** 06:05 I see, I deleted the policy entirely. Okay.
I'll close mine for now. We'll figure out what we want to do with that later.
Cool.
**Liudmila Molkova** 06:17 Yeah, oh, by the way, Joe posted a skill.
I probably will leave some comments to update to V2, the definition.
**Josh Suereth (Google LLC)** 06:30 Yeah.
**Liudmila Molkova** 06:31 And… how do you feel about keeping skills?
Industry Paul.
**Josh Suereth (Google LLC)** 06:36 I'm okay with that, I approved it.
**Liudmila Molkova** 06:39 Oh, no! Oh, cool.
**Josh Suereth (Google LLC)** 06:41 I don't know…
**Liudmila Molkova** 06:42 I didn't notice, sorry.
**Josh Suereth (Google LLC)** 06:43 Yeah, we probably need to spend some more time in, making sure we maintain this repo, because I think he did that 3 weeks ago.
But it can't be merged because it's out of date.
And I don't have access to update it.
**Liudmila Molkova** 07:04 You don't? Okay.
**Josh Suereth (Google LLC)** 07:06 No, I don't know where he has the PR, but I can't, like, update to main. It, like, I think he has that disabled on his account.
**Liudmila Molkova** 07:14 Right.
Yep.
**Josh Suereth (Google LLC)** 07:19 Which, that might be a security feature we all do in the future.
**Liudmila Molkova** 07:26 Well… I don't know.
We, maintainers.
**Josh Suereth (Google LLC)** 07:35 Yeah, damn.
Let's see… so we have… Is that… I think, yeah, and nightly passed. I'm fine cutting a release if we want.
I noticed no one else is… I made a, a GitHub co-pilot, like, agent that you asked to go write the changelog for you, because I always forget to update changelogs, I've been using that. Is that something you did last time you cut a release? Because I don't think anyone else has used it. I think I'm literally the only person who's ever used it.
**Liudmila Molkova** 08:09 I think I didn't use it because I told my local AI to…
**Josh Suereth (Google LLC)** 08:16 I had to do it.
**Liudmila Molkova** 08:17 joke.
**Josh Suereth (Google LLC)** 08:18 Gotcha.
**Liudmila Molkova** 08:19 And if it was a skill in the repo, it would be more useful, I think.
**Josh Suereth (Google LLC)** 08:25 Yeah, I couldn't figure out how to make a skill in the repo that GitHub Copilot would also use as one of its dumb agent things for a workflow at the time. This was before skills were popular.
**Liudmila Molkova** 08:38 It should, like, now you define it somewhere in the GitHub and the skills, it should work.
**Josh Suereth (Google LLC)** 08:45 Okay, so maybe we move it into a skill. That seems like a good task to do. But anyway, do you… do you want to cut the release? Do you want me to cut the release? Are we… do we feel like we're ready? I'm just looking through the issues here, see if there's anything else that popped up.
You know, most of them are from you. The entity resolution tracking issue looks like it's done, all PRs are merged, but the… oh, the issue is closed, okay.
Provenance for original definition in refinements… that's one that I was curious about, similar attributes seem to be NC associations. Provenance for original definition in refinements. I… we're not actually keeping provenance on those.
**Liudmila Molkova** 09:32 I don't remember. Is it from me?
**Josh Suereth (Google LLC)** 09:35 Yeah.
I mean, it was 2 weeks ago, so that was like… The equivalent of 10 years, yeah.
**Liudmila Molkova** 09:41 Yes, exactly.
ship.
**Josh Suereth (Google LLC)** 09:44 Yeah, it's an issue. I was just going through the issues of things to see if there's anything that, like.
**Liudmila Molkova** 09:49 Oh.
**Josh Suereth (Google LLC)** 09:49 Is urgent, yeah.
Documented live check config section is ignored. We got a bug from someone.
about this, but I think the live check OTLP documentation, we haven't cut a release yet.
No, it's a bug from Jeremy.
He's probably aware of it. He doesn't have it listed as… to consider next release.
Mmm…
**Liudmila Molkova** 10:16 You know what, I think maybe this issue is fixed, because I created it right during the Weaver call, and we probably need Jeremy to check.
**Josh Suereth (Google LLC)** 10:27 I think he might have fixed it, yeah. I don't know… I don't know if he fixed the refinements thing, I think we fixed the… entities thing.
**Liudmila Molkova** 10:36 Right.
**Josh Suereth (Google LLC)** 10:36 Yeah. I don't know.
**Liudmila Molkova** 10:38 I don't think… even if it's still relevant, I think it's okay, because nothing… It's hurting because of it.
**Josh Suereth (Google LLC)** 10:47 Yeah, okay. So, let's… I think we're probably… if nightly is passing, I'm inclined to just cut the release.
Because it has so many fixes in it. Nightly's working, so we know we're not wholesale breaking people.
And then we can go from there. Cause we still… we still know we have more fixes we want to make going forward anyway.
We're gonna stop fixing.
**Liudmila Molkova** 11:15 Yeah, and I can cut it if you would rather not.
**Josh Suereth (Google LLC)** 11:20 If you could, I'm trying to buy a car, so I'm trying to sneak out early today.
**Liudmila Molkova** 11:25 Okay.
Good luck.
**Josh Suereth (Google LLC)** 11:27 Yeah, so combined with all of my current workload, it's a bit insane.
yeah, just looking.
Man, 3 passing downstream checks?
It's like we're a whole new project.
**Liudmila Molkova** 11:55 It's temporary, it's just today's an error.
But I think we need to finish the V2 stuff, because we are holding back on pretty much any other things in Weaver.
accept the V2 and life check improvements.
**Josh Suereth (Google LLC)** 12:12 Yeah.
**Liudmila Molkova** 12:14 If we were to do some configuration stuff, we wouldn't be able until we finish the V2.
**Josh Suereth (Google LLC)** 12:21 Yeah, what… so, let's talk timelines there a little bit. We're… V2's getting mass adopted, in my opinion, not mass adopted, but we're hammering it pretty hard with Semcom Gen AI with, that. I think the other thing is we're not… it's not just landing V2, it's landing the whole multi-dependency hell.
That we decided to do and are now in the middle of, and I think we have a decent first cut. What do you think is a blocker for… declaring V2 stable at this point.
**Liudmila Molkova** 12:53 The part that nobody implemented yet is publishing, the real one.
**Josh Suereth (Google LLC)** 12:59 Cool, good, good, okay, we need to start publishing.
**Liudmila Molkova** 13:09 It's… just mechanical. I hope that maybe Jaw would pick it up, but he didn't, that we would just publish semantic conventions, right, Paul.
The deaf and non-deaf.
Oh, this is also where I need to go and make spec changes.
Because it's, it's ATAP.
And it's not, anywhere in the spec that we're changing the schema URL. But I don't, I don't feel it's a problem. It's just implementing the OTAP, it should be just words missing.
**Josh Suereth (Google LLC)** 13:42 Yeah, I still think you're gonna get… the… the general freakout. I think you and I talked about this, earlier.
About the current state of the spec.
So, I do think that I would… that's one of those things we should make early, because we have to let people's emotions calm down to review it.
Eventually. There's always a, you're making a change, and I'm angry about it.
emotion now, that I… Yeah.
**Liudmila Molkova** 14:14 Yeah.
Well, I think that the precondition to having a spec change is having an idea of how it will be published on Hotel.io, and have a buy-in from Hotel.io people.
I feel it would move us relatively far.
I just didn't have a chance to play with it yet.
And it should be.
**Josh Suereth (Google LLC)** 14:35 No.
**Liudmila Molkova** 14:36 Jill.
**Josh Suereth (Google LLC)** 14:37 For getting into OpenSilmsh.io, gotcha. Yeah. Okay.
**Liudmila Molkova** 14:40 And, like, with agents, it should be easy. The AI will figure out how to do this. I will just sit and wait, and wait for approvals from one potential laboratory.io.
**Josh Suereth (Google LLC)** 14:53 Yeah.
**Liudmila Molkova** 14:54 so.
And there is a bunch of other things and semantic conventions that need to happen before, because the V2… oh, V2 output should be fine.
Just the documents should not be fine.
Oh, and we cannot publish until we finish the migration, because it's ugly as hell today.
**Josh Suereth (Google LLC)** 15:17 So we have to do the migration before we can publish. Gotcha.
Okay So, in terms of tasks to pick up, it sounds like if I were to spend time on V2, timeline might be better spent in Semconv.
or… You know, like, what could I help there?
the… How do you want to divide up the work, I guess?
**Liudmila Molkova** 15:43 Yeah, I'm just writing down the things we need to make it happen.
Okay, so… The autologo design, I… I don't know.
It's… it should be trivial.
If you want to take spec changes, you would have a very high chance of success.
**Josh Suereth (Google LLC)** 16:31 I can… I can do that, yeah.
**Liudmila Molkova** 16:35 Sorry.
**Josh Suereth (Google LLC)** 16:36 Go ahead and assign that to me in the notes, and that'll help me remember.
**Liudmila Molkova** 16:46 Hey, I will instruct my botch.
To do this… And… Oh, this is our sonni.
**Josh Suereth (Google LLC)** 17:09 That one, hopefully with some kind of migration… that's one we can chart out. How has that been going, by the way? I've been a bit… Disconnected from some kind of maintainership, the past two weeks, just from… some work things that prevented me on Mondays.
But that should be fixed next week, like, I can actually… start attending the meetings, but I haven't been doing my pull request reviews, so apologies.
**Liudmila Molkova** 17:36 No, it's fine, but we didn't make much progress, so… Joel is busy with something… M-mos… Most of the things we can cut, because… We discussed it on some conf call that some of these groups, we don't want them public. We will probably just remove them.
**Josh Suereth (Google LLC)** 18:09 Yeah.
Okay, and this is… so, Zhao has the big tracking issue, right?
Yeah, this is… Yeah, is this a thing where I can just, pick up one of the things and… Yep. Make progress on it? Okay.
Update markdown snippet templates, I thought someone had made changes there for V2, or did that, like, didn't you do that, or is that not true?
Sorry, I'm looking at… I'll put this in the notes.
Here we are.
**Liudmila Molkova** 18:46 There's…
**Josh Suereth (Google LLC)** 18:47 This one, yeah, yeah, you're looking at it now, too.
**Liudmila Molkova** 19:00 Are you seeing the raw markdown now? I'm just checking, because I was showing it for a long time.
**Josh Suereth (Google LLC)** 19:06 Oh, I was… I was looking at my own thing, yeah, yeah. Oh, so that one, that's the one that, like… Are you, I thought you had done that, but am I… Misremembering.
**Liudmila Molkova** 19:18 I think it's the combination of the two, let's merge them together.
**Josh Suereth (Google LLC)** 19:23 Okay.
Okay, open tracing, deprecating, stop rendering, interesting.
Cloud events, public group, or spend. So there's decisions to make here, too.
**Liudmila Molkova** 19:37 There are decisions… There was a SMCON call a couple of weeks, maybe 3 weeks ago, where we talked briefly about it.
And decided that… We need to keep network and service and important things.
But, like, the details, network core, network connection, and carrier can just be removed, because… We have them in attributes registry.
We don't need them as public groups, they don't show up pretty much anywhere.
**Josh Suereth (Google LLC)** 20:10 Betsy.
**Liudmila Molkova** 20:12 I'll probably keep a file on network. Yes, there are decisions to be made, but they are easy decisions, and there shouldn't be pushback, because we already talked about it.
**Josh Suereth (Google LLC)** 20:22 Okay.
So… Are… do… is every… is most thing… are most things moved to V2, then, already? Like, it's just these… the last hard ones?
**Liudmila Molkova** 20:34 No, these are the things that are… we can… where it's controversial how to move them to V2, because they are attribute groups that they render.
Or something else.
Gotcha. And we didn't move, any of the big things, like HTTP or databases or RPC, And we have some help from some of the contributors, but it's harder to explain them what to do than to do it ourselves.
**Josh Suereth (Google LLC)** 21:14 Yeah, that's… that's the problem with delegation. It depends on whether those contributors are going to be people who stick around after they understand it and continue to contribute, or not, right?
**Liudmila Molkova** 21:26 Oh, we have some, energy from James.
But it's the case where it's sometimes hard to…
**Josh Suereth (Google LLC)** 21:35 So…
**Liudmila Molkova** 21:36 Separate, like, refactoring from just mechanical changes?
**Josh Suereth (Google LLC)** 21:40 Yeah.
Gotcha.
**Liudmila Molkova** 21:46 Okay, so then… I'll try to put some energy into some of the things.
**Josh Suereth (Google LLC)** 21:55 If we, yeah, if we were to start making, like, service peer and that sort of thing, if we were to start taking some of these and moving them to V2, where it's just fully mechanical.
Does Semcom start breaking if we do that?
**Liudmila Molkova** 22:08 Shouldn't, no.
**Josh Suereth (Google LLC)** 22:10 Okay.
**Liudmila Molkova** 22:11 Service peer, no. Network core, we shouldn't move it to public group. And then it will start breaking because we cannot render anymore.
**Josh Suereth (Google LLC)** 22:20 Yeah, okay, gotcha.
Gotcha.
Okay.
Well, we have a lot of good work in front of us.
But I do think that this is, like… If we finish this… And GenAI Semcov is happy.
then I'm fine marking V2 release, because then I think it's bug fix time.
Like, we still might need to make changes and all that, but in terms of, like.
Big rocks, making sure all the major pieces have landed and are not horribly broken.
I'd say we're ready.
I think it'll take some time before we make V2 the default, but I don't know how long that will be. Like, once SimConv has it as the default, once GenAI has it as the default.
How many Weaver releases do we want to warn people that V2 will become the default?
And how much time do we want to give them?
Because we do…
**Liudmila Molkova** 23:28 And…
**Josh Suereth (Google LLC)** 23:29 A lot of users… We have a surprising number of users who aren't in the hotel ecosystem, necessarily, like Jeremy's company, that are using Weaver, yeah.
**Liudmila Molkova** 23:38 But not V2. I think we're… You know, how we've started working on V2 and everything was right until we faced all this… tricky cases. Like, if… to feel absolutely comfortable, I think we need to publish, right? And we need something to use the published version.
We don't need to publish stable schema, by the way, right? Because we can publish the def one to start with, and hold back on the… like, publish the original… well, that's the word combination, but we can do this. Yeah. And then if somebody starts using it, okay, let's say we onboarded GenAI, and we onboarded Semantic Conventions, and GenAI uses the published version of Semantic Conventions, and it works fine.
**Josh Suereth (Google LLC)** 24:29 Yeah.
**Liudmila Molkova** 24:32 And then we could make it the default, and we would keep it unstable, but we will trade it as stable.
For a couple of releases, and then we call it.
**Josh Suereth (Google LLC)** 24:45 I think that makes sense, and in terms of a couple releases, to me, it's like, it might be a couple releases. Like, if we're releasing every month.
Do we give people 6 months to migrate? Do we give them a year? Like, I… I don't know. It's, that's a judgment of our ecosystem and our users. So, I… I'm leaning towards at least 3 months.
So that'd be 3 major release… er, 3 releases, if you will.
**Liudmila Molkova** 25:16 We can do this in two ways, right? We can start building a clean version of liver.
That's V2 default.
Drop all the crap we have from Vivan.
And we can publish it from the branch, it's very difficult, we don't have people to do this.
But… yeah.
It's just, I'm trying to see, okay, if somebody cannot move. Remember how we did the beaver migration, and there was a very little long tail of repos that never updated? I'm not sure if they updated today, like Swift or something.
**Josh Suereth (Google LLC)** 25:57 Well… That… partly that is, we need to get them frickin' on Dependabot, so they get… because they're gonna have, vulnerabilities if they don't upgrade.
Because the Docker image they use Or just the version of binary will have vulnerabilities, so if they're not… like, it's OpenTelemetry policy that you're updating your… your dependencies, so the ones that don't, like… That's one reason why, with SemConf, you know how we have that weird dependencies Docker file, so that DependAbot and Renovate can tell us when Docker images need to be updated? That's for SALSA compliance. That's not… it's not like a, oh, this is a fancy thing that is annoying. It's like a mandatory thing that's part of OpenTelemetry. So, I think we can, we can push on that. Folks who are hiding the Weaver version somewhere have to find a way to update it. And that is… that's a… that's a security problem, not a… adoption problem for Weaver.
I mean, it is an adoption problem for us, but it's a… So, I'm more worried about keeping, external to OpenTelemetry folks happy.
that are using Weaver successfully.
So… I also… I also want to cut a 1.0 of Weaver at some point, so it's more clear.
That we're stable, that we're gonna keep things stable, how long our stability… guidelines are, and that if we have a 2.0, we'd have a 2.0, like, main becomes 2.0, and there's a branch for 1.0. And if you want to make fixes for 1.0, contribute them, because we're kind of, you know.
Not… we're only doing security patches on it, that kind of crap. I'd like to get to that point at some point, where we can do that, but since we're still unstable release land.
we're… we're kind of the… we are the problem of open telemetry, you know what I mean?
**Liudmila Molkova** 27:48 Yeah.
So… external people.
They have a little bit more wiggle room than us, because they have their own registry.
And they can go through a migration independently.
That the interesting problem is that they depend on OpenTelemetry Semantic conventions, and once it goes V2, they have to update Weaver.
**Josh Suereth (Google LLC)** 28:18 to be able to consume in its V2, yeah, that's very…
**Liudmila Molkova** 28:20 Right, so they will be stuck on the old combination of semantic conventions, their own registry and old Weaver.
**Josh Suereth (Google LLC)** 28:28 Okay.
By the way, Jeremy, we're talking about, first of all, we want to cut a release today, or this week.
For all the fixes.
And then we're talking about V2 timeline, of how to get, like, what do we need to do to get V2 mark stable?
And then, what kind of a transition period do we give people between V1 and V2 and Weaver? And then I'm talking about, I want to get Weaver to 1.0.
where we have, like, a stability guarantee, and people know that we're not gonna be breaking them with, like, V2-ish things.
the way we might be doing now, but I also want to give people enough time to migrate from V1 to V2, particularly not, like, inside of OTEL, because of the way version updates are required for SALSA compliance, everyone should be updating Weaver, and if they aren't.
we can actually say, hey, there's a security review where you're not updating your Docker images and things, and so you're out of compliance with OTEL, like, you have to update, sorry. So go fix your stuff so you update quickly.
Non-OTEL people.
I don't want to just break the ecosystem, you know?
And say, hey, V1's gone. I want to give people a transition period, and how long should that be?
**Jeremy Blythe** 29:48 Just on the topic of things left for V2 compatibility… we need the live check stuff that I'm working on. Live check in V2 is basically broken.
**Josh Suereth (Google LLC)** 30:00 Okay.
**Jeremy Blythe** 30:01 So we need the thing… I mean, I'm about two-thirds of the way through that… from that matcha spec.
But it's really not usable without that. It kind of… you kind of get away with it if you've got one registry all standing on its own, but as soon as you add in a dependency, it's… it's pretty useless.
**Josh Suereth (Google LLC)** 30:20 Oh, the dependency part is broken. Yeah, yeah, yeah.
**Jeremy Blythe** 30:24 Gotcha. Just because then you don't have any attributes, and everything just goes wrong at that point. Yep.
I'm not sure it's a big problem… for a release today? I really don't think it is, but, you know the… In the forge output, you… you added a thing where the registries, like, appear as dependencies.
Inside of the forge output.
That is duplicating registries, so it's making a kind of a flat Flat.
And a tree at the same time.
I've got a… branch open for that as well, but I don't know whether we… that's entirely necessary.
For today, because it's just the materialized output.
**Liudmila Molkova** 31:26 I mean, if we can fix it, it would be better.
**Jeremy Blythe** 31:31 Okay.
**Liudmila Molkova** 31:32 Yes, somebody will start using it.
Some rogue agent.
**Jeremy Blythe** 31:37 So I was going to try and make it recreate the tree.
Rather than having, like, The dependencies duplicated into the… The top level as well.
**Josh Suereth (Google LLC)** 31:55 Wait, say this again, so what's… what's happening?
Why is it dependent.
**Jeremy Blythe** 31:58 The people…
**Josh Suereth (Google LLC)** 32:01 Yeah.
**Jeremy Blythe** 32:02 you've got… A depends on B depends on C.
**Josh Suereth (Google LLC)** 32:06 Yeah.
**Jeremy Blythe** 32:06 what you'll see in the forge output in the new dependencies section, Is you'll see… A depends on B depends on C, where they're copied into each other.
Then you'll see, also at the top level, you'll see B on its own, and you'll see C on its own. So you've got ABC in a tree, and then you've got B and C duplicated at the top level.
Last one.
**Josh Suereth (Google LLC)** 32:31 BNC are in the top level, too?
**Jeremy Blythe** 32:33 Yeah, that's the book.
**Josh Suereth (Google LLC)** 32:38 What did I screw up for that?
I look forward to the fix, because I don't know what I did there. I thought that that would…
**Jeremy Blythe** 32:47 I don't know, because we all reviewed it as well. We all reviewed it. Oh, that's good.
**Josh Suereth (Google LLC)** 32:52 Yeah, and my test case didn't test for that.
Because I'm like, oh yeah, I don't think this could ever happen. Alright, cool.
**Jeremy Blythe** 32:59 I really… yeah, sorry, I parked that, I was working on it, and then I parked it, and then… because I was doing something else, and then…
**Josh Suereth (Google LLC)** 33:06 Yeah.
Well, I think we can still cut a release now, and then fix that as, like, another minor release, or do you think that is release blocking?
**Jeremy Blythe** 33:17 That was my question.
**Liudmila Molkova** 33:21 if, like, Jeremy, if you already have a fix, it would be nice, because Somebody will take dependency on it, and next release will be worried about breaking them. Well, we won't be, but we will break them.
**Jeremy Blythe** 33:37 I, Okay, I'll see if I can get that in today, then. It might not be till a bit later.
Sorry, I… Trying to find the time in the day.
**Liudmila Molkova** 33:52 If you have a fix, or if you have a repro.
If you can ask your EA to create an issue with the repro.
Where I can take a look, or I can.
**Jeremy Blythe** 34:03 I think I've got it all… I'm pretty sure I've got it all done.
And then I parked it, and, like, I think it's ready. I just… I've got to find… I've got to grab, like… 30 minutes.
-Oh.
And make sure it's not got too much slop in it, because I did use some AI for it.
**Josh Suereth (Google LLC)** 34:25 Well, there's always gonna be a little bit of slop, right?
**Jeremy Blythe** 34:29 The slope, and then the slope there.
**Josh Suereth (Google LLC)** 34:30 Here's the thing, there's my personal slop, and then there's the AI slop, and it's which one do you prefer?
**Liudmila Molkova** 34:35 Oh, there is the EI slope you created, and there is EI slop somebody else EI slop. Oh, that's true. They are quite different.
**Josh Suereth (Google LLC)** 34:45 Yeah, but here's the thing, there was always my personal slop in every PR you ever reviewed. So now it's someone else's slop, which is always worse than your own slop, right?
**Liudmila Molkova** 34:55 Great.
Okay, so then, Jeremy, you will, work on the fix, let me know, I'll review it right away, and we will hopefully cut a release this week.
I think it's okay, we can wait a couple of days.
**Jeremy Blythe** 35:18 Honestly, it should be today, it just might not be till this evening.
**Liudmila Molkova** 35:27 Okay.
**Josh Suereth (Google LLC)** 35:32 Okay, so we know that we have, for V2 timeline, just to recap everything, we have live check-related changes, we want to get publishing.
Out and used so that we, can use it in anger.
then we can start stabilizing the V2 format. I think we could actually, and I think this is true today, should we consider the V2 format stable, practically, at this point?
and only make non-breaking changes to it. We've kind of already been doing that, so I think that that's not really a big diff.
**Liudmila Molkova** 36:05 I see two changes, for… where I'd like to actually make them before I call it.
This one.
**Jeremy Blythe** 36:16 That's exactly the one I was gonna bring up.
**Liudmila Molkova** 36:19 And it's actually really.
**Josh Suereth (Google LLC)** 36:20 Oh, that is breaking, yeah, crap, yeah, let's… 100%, let's get that in. Did… I haven't reviewed this yet, have I? Okay.
**Liudmila Molkova** 36:28 No, you haven't, and… There is another one I was working on, and it's a little bit tricky, even though it doesn't look like that.
So…
**Josh Suereth (Google LLC)** 36:41 Was this the flexibility one?
**Liudmila Molkova** 36:43 No, the deprecating it.
**Josh Suereth (Google LLC)** 36:47 Your, your flexibility one I consider non-breaking.
You're joking.
**Liudmila Molkova** 36:55 That's right.
**Josh Suereth (Google LLC)** 36:56 No.
**Liudmila Molkova** 36:57 So, it turns out to be, complicated, because… Wee… Reuse stability, but reusing stability is okay.
The problem is that we reuse, you know, members.
spec between V1 and V2.
And the amount of… Okay, there are two ways to approach it if we want to do this. Either… it's a giant PR with tons of plumbing changes and duplication of types between V1 and V2.
Or some crazy hackiness that produces what we need, but does some custom deserialization on selected passes and whatever.
**Josh Suereth (Google LLC)** 37:48 So, here's the thing. Let's, especially with AI, I know the review's gonna suck.
let's duplicate everything into V2. Like, I… and I can take a crack at just throwing tokens at this, and I… and I mean this, nothing is shared between V1 and V2.
all of the definitions are brand new in V2, and there's into and froms and that kind of stuff for transitioning between the two types. The reason why I think we should do this is because when V1 is gone, we frickin' delete it.
Bam, gone.
Right? And there's no ambiguity.
of, like, what's there, what's missing. There's no ambiguity of what's V1 and V2. I know this is gonna suck, but I'm gonna propose it, because I… I think we're gonna be happier on the other side of it.
And AI will be the one hoisting a lot of the hell, I hope, outside of our, like, reviewing being rough.
And I think we will have to leave a paper trail.
for AI agents of really verbose comments, so they understand what the hell we've done and why there's two everywhere. So, I am happy to take that, because that's actually been something I've been exploring, of how to make AI less stupid when we have to have horrible architectures that are confusing and easy to misjudge. I've been doing a lot of experimentation with that.
so I can take a crack at that if you want, but yeah, I… I… I understand what both options are, without you having to go into detail.
it sucks. I don't think… I don't think we have a good solution here, so I'm proposing, let's do the… Let's just start duplicating everything, and Jeremy, this will mean I have a lot of live check PRs for you, probably. You already have a thing in place to split everything.
just probably we have to go deeper, further, and I hope what this means, if we've done it right, and I'm gonna try to give AI instructions that V1 goes into V1 directory, V2 goes into V2 directory, and then when we're ready, V1 directory is dead.
and we remove all those references, and hopefully then we're ready to move on with our lives. And… Yeah, that's… that's my proposal.
**Liudmila Molkova** 40:11 Is it… It's essentially two branches, but merged in one branch.
Could it help us?
**Josh Suereth (Google LLC)** 40:20 Could it help us to have… no, because we… if we have a compatibility layer where you have two things at the same time, you know what I mean? Like, I have to be able to pull in them both and convert between them and all that hell. So… I don't think this is a branching thing.
Necessarily. This is… this is the general L of V1 and V2 of an API needing to coexist together.
**Liudmila Molkova** 40:47 Okay, yeah.
But I was thinking that, essentially, these are… it can be as independent as different crates, with just one thing known about both.
**Josh Suereth (Google LLC)** 40:59 Oh, like, make it a completely separate crate. I was gonna make it a separate module within the crate.
So I was actually going to move V1 into a V1 module.
So V2 is already in a module, but it's not… like, it's not cohesive. So I was gonna set up a set of agent rules.
Which, by the way, do we have an ancient D? I think we do.
**Liudmila Molkova** 41:19 No, we don't!
**Josh Suereth (Google LLC)** 41:21 Okay, I'm gonna make an agency.
**Jeremy Blythe** 41:22 I don't need to donate it, but I haven't.
**Josh Suereth (Google LLC)** 41:25 Okay, well, here's the thing, by the way, with AgentsMD that I've learned. If Lududmil and I are using Gemini.
then you don't want Mariage and MD.
if you're using Claude, then I can use your Agent MRD, and Gemini will ignore it anyway.
But, like, we want kind of a… our AgentMD kind of targeted at Claude, if Claude is, well, like, whatever the agent we're most using.
If it's ChatGPT, if it's Gemini, if it's Claude, the HMD should be slightly tuned towards it, because what will happen is Claude will auto-update HMD every time you use it now, with Opus 5.
Claude needs less in an Agent MD to be useful.
Gemini needs a lot, to the point where Claude starts to pay attention to things in ways it shouldn't be paying attention to things, that Gemini needs to just function.
So, I think we start doing a little bit… like, I'm happy to make an Agent tailored to Claude.
with some rules that Gemini pays attention to, and then Gemini, we can actually layer on additional rules. There's ways that we can do that with, like, anti-gravity, where you have, like, an anti-gravity skill that gets layered in on top of the Agent's MD.
Great. So that, we're not polluting AgentsMD for all agents, we're just putting the things all agents should pay attention to, and then agents that need additional instructions, we put into, like, a .gemini folder or whatever.
How's that sound?
**Liudmila Molkova** 42:53 Or just share them…
**Josh Suereth (Google LLC)** 42:56 Yeah, go ahead.
**Liudmila Molkova** 42:57 just share them in a way that I would copy it into my general Gemini-specific instructions, global, or whatever, yeah.
**Josh Suereth (Google LLC)** 43:07 Yeah, like, for context, I have a crap ton of skills specific to Weaver for Gemini that I would not put into a project using Claude.
**Jeremy Blythe** 43:17 Right.
The stomach.
**Josh Suereth (Google LLC)** 43:19 There we go. What?
**Jeremy Blythe** 43:21 I just have a Clode MD.
Because that is Claude. So I just have a Claude MD. I don't have an agent's MD.
**Josh Suereth (Google LLC)** 43:28 Oh,
**Jeremy Blythe** 43:29 I've just been gradually taking things out of it, actually, because I found… I've found recently that… It's getting so much better at… Not… you know, that it's actually… it's kind of sending it… starts to send it down the wrong path if you have stuff in your CloudMD. You actually need to be much more brief.
And it's only recently, like, Opus 5 is, like, seems to be really bad at writing comments and… and doc paragraphs, like, terribly bad. So, I just… my Cloud MD now is, like, the first half of it is, like, how to write English better.
**Josh Suereth (Google LLC)** 44:09 Interesting. Okay.
**Liudmila Molkova** 44:11 My personal one is don't write comments unless I ask you to at this point, because I gave up. I hate generated comments. It's impossible.
**Jeremy Blythe** 44:20 I hit the jackpot the other day. I told it… I said, write this like a software engineer, in plain English.
Without anthropomorphizing.
That sentence then suddenly gave me so much better comments.
**Josh Suereth (Google LLC)** 44:38 I have been using Gemini to do my comments, and Claude to write my code.
For, like, all… on my personal computer and all that.
I… this is publicly recorded. Well, whatever.
Anyway, I hear your pain, because Cloud got more verbose with its output and more jargony, and sure.
I like it, personally. I don't like its docs, but I like the output the Cloud has now, because I can understand what the hell it did better in its reasoning.
So I'm a big fan… I actually really like Opus 5. And to the point that I was trying to make, Jeremy, you nailed it. You need less in your Cloud MD.
I would still like to have an AgentMD that's shared, so the way I set up all my projects is I have an AgentMD, and I have a ClaudeMD that references the AgentMD, and then you can add explicit instructions to Claude there. Gemini, I do the same thing, but Gemini automatically pulls in… sorry, not Gemini, anti-gravity, automatically pulls in the Agent's MD.
So you have an additional GeminiMD file that has the specific Gemini things, and so we can lay out a project that way. Here's my concern.
Opus 5, by default, updates AgentsMD after it uses… and Skills after it uses them, to refine them automatically.
**Jeremy Blythe** 45:51 It does.
**Liudmila Molkova** 45:52 I didn't see this, it didn't happen to me.
**Josh Suereth (Google LLC)** 45:54 It has happened to me consistently. Are you… are you adventurous enough to use auto mode?
**Liudmila Molkova** 46:00 Yeah, of course!
How else would you…
**Josh Suereth (Google LLC)** 46:02 Yeah, never mind. I have this in my called MD, sorry.
I… okay, maybe it's a me thing. My… I set this as a global thing for Claude, apparently. So one of my ClaudeMD files tells it to do that. I'll have to go look that up, but… It's really good at it.
So, basically what happens is, and I do this frequently, when I go through and use a tool, and it does something stupid, after I'm done with the conversation, I say, hey, go update all my skills. And Claude now… and CloudMD. And now it does it automatically for me, every time.
**Liudmila Molkova** 46:38 It's fun, right? Because if it's… it will show up in the review, and if it's fine.
We will accept it.
**Josh Suereth (Google LLC)** 46:46 That's what I'm just worried about, like, should we have those CloudMD changes came in as separate PR? Should we include them in the original PR? Like… how do you guys want to manage that? Because my opinion is, with these agent files, is they're living documents that need to change very frequently.
to be tuned. Like, it's not like we write one and then it's useful forever. It is actually a constant tuning process. So I want to make sure we can all do that. But I also don't want a giant, like, file that we all fight over, that every single PR blocks each other for conflicts, because it's stupid CloudMD, or AgentMD.
**Liudmila Molkova** 47:22 If it's not user-facing, we're not changing development processes, not changing policies much, it should not change, right?
**Josh Suereth (Google LLC)** 47:32 It has been my experience so far that I have changed that file Kind of monthly, on every project that I'm using.
To optimize it.
**Liudmila Molkova** 47:43 I mean, monthly, not purely.
**Josh Suereth (Google LLC)** 47:46 Well, with 3 of us, that's 3 times a month.
But, sure. Fair. Maybe I'm too worried about it. I'm used to Google, where there's thousands of people touching one file.
Because we don't think about it as a godfile, and then it becomes a disaster. So… but there's only 3 of us, so it's probably not that big a deal. Anyway, I'll submit an HWD.
**Jeremy Blythe** 48:07 Why don't we try it?
And if it becomes unmanageable, then we'll fix it.
**Josh Suereth (Google LLC)** 48:13 Okay, I also want a general notion that, in my opinion, for now, Claude should win, if Claude and Gemini disagree on what should be in Agents MD, and that we have the ability to put Agent-specific additions in, like, a model-specific file.
Does that sound good?
So, like, if we have a policy around AgentMD, AgentMD is the bare minimum.
CloudMD references it, and you can add things specific to Cloud if it needs it.
And then Gemini MD can have things for Gemini. ChatGPT, I don't know, I've never used ChatGPT. I've used OpenCode, which is just AgentsMD, but, we can figure it out as we go.
Does that sound good?
**Liudmila Molkova** 48:54 for the CloudMD, you wanted just the hard link? I was thinking about SimLink, that's what we use in other repos.
**Josh Suereth (Google LLC)** 49:03 So, the CloudMD file, the thing that I have, it just is an at to AgentsMD.
But then you can also raise…
**Liudmila Molkova** 49:11 Tim Link.
**Josh Suereth (Google LLC)** 49:12 Is that a SIM link? It's not a real SimLink, it's like the ClaudeLink thing.
Honestly… You can do a sim link, but, like, if you're on Windows, that's awkward and that kind of crap. But also, if you want instructions specific to Claude that aren't used by other agents, you can't do that then. So, my ClaudeMD, I just put the at sign to the agent's file, and then you can add more things if you need it.
**Jeremy Blythe** 49:35 Yeah.
**Josh Suereth (Google LLC)** 49:37 That's also how I get Claude to read skills from… or workflows from… from anti-gravity. I don't know if you know what an anti-gravity workflow is.
**Jeremy Blythe** 49:47 Have not used anti-gravity.
**Josh Suereth (Google LLC)** 49:49 Yeah.
Anyway… There's a whole set of practices that I'm aware of for making those two work together.
That I will set up an initial thing, you can… you can say what you think of it. I don't want to over-engineer it. I want it to be… Super dead simple for what we have initially.
I also might pull in some of my skills.
I literally wrote a skill, for how to understand W result.
And that improved my agent so much. I don't know if we need that in docs or what, but I will probably also contribute my W result skill, if we're okay with that.
**Jeremy Blythe** 50:31 Oh, speaking of dogs…
**Josh Suereth (Google LLC)** 50:33 Yeah.
**Jeremy Blythe** 50:34 Okay. Speaking of dogs, one of the things I started looking at No.
is whether we should have a book for Weaver. Because Weaver's getting, like, really detailed, especially in live check now, and especially with the new stuff I'm adding.
**Josh Suereth (Google LLC)** 50:49 Yeah.
**Jeremy Blythe** 50:50 Like, one big long README, That's pretty tough now. So if we had a… we had a book,
**Josh Suereth (Google LLC)** 50:58 It's an MD book.
Right? I think, yeah, we should have it.
**Jeremy Blythe** 51:04 And then… but then where do we publish it? Because… The experience of using that sort of book in a Inside of GitHub.
You wanna… you want a GitHub.io published version, right?
**Josh Suereth (Google LLC)** 51:18 That's where we want to talk to OpenTelemetry I.O. They might be able to give us a place where we can dump the book and have it posted.
**Jeremy Blythe** 51:25 Of course.
**Josh Suereth (Google LLC)** 51:26 Awesome.
**Jeremy Blythe** 51:27 We've got README in docs and stuff all across, like, spreading crates and, you know.
I've generated a bunch inside of LiveCheck. Some of it is actually generated as well now, like, the finding in the is generated from the YAML, you know, because it's a proper V2 thing. Dogfooding.
**Liudmila Molkova** 51:47 Maybe we should have the… the GitHub pages, just publish the… the website.
on the GitHub.
**Josh Suereth (Google LLC)** 51:57 We can do that. I think what you're asking, Jeremy, is where do we keep it for ourselves in the repo to make the book? I think it has to be a separate directory. Like, we have an MD book directory that we start having our docs in there, and then we can have a READMEs reference the book.
Instead of have the README be the… hold the content, yeah.
**Jeremy Blythe** 52:17 Yes.
**Liudmila Molkova** 52:18 What is what Java folks do? They have the special knowledge, for agents. I don't know if it's, like, a pattern recognized by CatPilot or something.
That this is the way they organize stuff.
**Josh Suereth (Google LLC)** 52:31 I think it… can you go to their Agent's MD? Because they have a knowledge index, read me. Does their Agent's MD point at that? I… I bet it does.
Because I can… I can do this for my W result.
**Liudmila Molkova** 52:43 Yeah, knowledge, read me. So it's… okay, so their agents MD is essentially an index into stuff.
**Josh Suereth (Google LLC)** 52:49 Exactly, and this works really well.
Because then you don't have to, the context doesn't get exploded and killed by all these descriptions of everything in AgentsMD. Okay.
**Liudmila Molkova** 53:04 Let's right. Well, what works quite well, I think, at least for me, and for, the co-pilot review.
is… This is the… We Silver Edge and SMD.
So this is kinda long, but it's… Very… it's insane how to do things right.
And it works well. I rarely need to, leave review comments for people when they just… have agents do follow this. Maybe it's too long, yeah.
**Josh Suereth (Google LLC)** 53:44 Well, this is where I think you can put some things into that knowledge base with the index and say when to look up pieces. That actually works out pretty well for… because that way you're not pulling in that into your entire context window. If you have an agent that's doing something small, that's great. If you're doing some major design, and it has to load that entire thing in before it starts the design.
You can get into weird… territory, where, again, this might be more specific to Gemini, but… If the initial context is long, it has to do a lot of processing, the initial context starts to fall out.
By the time it starts making decisions, and you get that context explosion of, like, it forgets the instructions it had to begin with, and starts just doing wonky, stupid things, or, you know, you told it you only want to design, and it starts implementing it.
And you're like, why, you know… Yeah, that kind of crap.
**Liudmila Molkova** 54:38 Yeah, I think what works well, actually, here is that you can make hierarchical LegendsMD, and you can have special instructions for small things, and, like, individual things are very, Prescriptive for important things, and agents actually follow them, and they prioritize the inner one over the outer one.
**Josh Suereth (Google LLC)** 55:03 Yeah.
Okay, I'll put together a proposal based on these things, of, of what… what I'm gonna write, because I'm going to first write the Agent's MD, and then use it to do the giant V1, V2 refactor.
**Liudmila Molkova** 55:19 Cool, and I feel…
**Josh Suereth (Google LLC)** 55:22 how that goes. Go ahead.
**Liudmila Molkova** 55:24 I feel fine holding this back, it's pretty minor. I don't care if we break it a little bit later.
**Josh Suereth (Google LLC)** 55:31 We need to do it before we launch, but yeah.
**Liudmila Molkova** 55:34 Of course, yeah. Not this release, I mean.
**Josh Suereth (Google LLC)** 55:37 Oh, oh, from this release? Yeah, yeah, that's good. Okay. So, the only thing we need to… we have one fix for this release that Jeremy's gonna work on.
And then we're probably gonna release later this week, is that right?
That's the, ABC…
**Jeremy Blythe** 55:51 Nope.
**Josh Suereth (Google LLC)** 55:52 Dependency problem.
**Jeremy Blythe** 55:53 No, wait, there was another one… The other one you showed, Lana, the,
**Liudmila Molkova** 56:02 This one, the disallow stability and deprecated. This is trivial. This is super easy to review, and yeah, if you can…
**Jeremy Blythe** 56:09 people.
**Liudmila Molkova** 56:10 Look, fine.
**Jeremy Blythe** 56:12 Yeah, that'd be a good one to do as well.
**Josh Suereth (Google LLC)** 56:15 I'll review this now.
**Jeremy Blythe** 56:18 Yes, I will… I mean, later this week, yeah, probably, like, tomorrow.
**Josh Suereth (Google LLC)** 56:25 Yes, if we can get a release out tomorrow, that'd be amazing.
**Jeremy Blythe** 56:28 Discord.
**Liudmila Molkova** 56:29 Awesome. Looking forward to reviewing it. Thank you. See you later.
**Josh Suereth (Google LLC)** 56:34 And in that one, if you want to submit an Agent's MD or a ClaudeMD, feel free, and then I can refactor in my PR. Like, either way, let's start getting that shared.
**Jeremy Blythe** 56:44 Sure, I could throw it in, but yeah, it sounds like we want to pare it down a bit.
**Josh Suereth (Google LLC)** 56:48 I… but I can start with what you have and then pare it down. Whatever's easier.
**Jeremy Blythe** 56:52 Sure. Okay.
**Josh Suereth (Google LLC)** 56:53 Or, no, why don't you copy-paste in chat? We'll start that way.
**Jeremy Blythe** 56:58 Okay.
**Josh Suereth (Google LLC)** 56:58 Yeah, so put it in the… in the maintainer's chat and Slack, and then I'll… I'll take that and use that as my foundation for everything that I do.
**Jeremy Blythe** 57:08 Yep.
**Josh Suereth (Google LLC)** 57:10 Cool.
Alright, see you.
**Liudmila Molkova** 57:11 Yeah.
**Jeremy Blythe** 57:12 Right.
