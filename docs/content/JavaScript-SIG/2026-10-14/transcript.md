SIG: JavaScript SIG
Date: 2026-10-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (Palo Alto Networks)** 02:09 Hey, what's up?
**Trent Mick** 02:13 you know.
**Hector Hernandez** 02:14 Hello!
**Marc Pichler (Dynatrace)** 02:23 Hello.
**Jared Freeze (Palo Alto Networks)** 02:26 Hey, Mark.
Nice collection, Hector.
**Trent Mick** 02:50 What just happened?
**Hector Hernandez** 02:52 Thank you.
Still missing, like, 20 more guitars there.
**Marc Pichler (Dynatrace)** 03:23 Alright, I guess, we can get started.
irwin: David has a topic here, but he's not on the call yet, I think.
**Trent Mick** 03:37 Yeah, let's skip him, and we'll come back if he'll get on. We'll be soon.
**Marc Pichler (Dynatrace)** 03:40 Yep, alright, then let's proceed with your topic, Trent.
**Trent Mick** 03:49 Sure. These are just some notes I've made for the agenda that I have today. So… There's… they'll need a reviewer from… JS on the JS content changes. Julian, who's… Has done reviews for stuff… oh, It looks like you had some stuff on there, Mark, that I hadn't seen, so I have to get back on it.
Oh no, that's pending.
**Marc Pichler (Dynatrace)** 04:13 It's been submitted.
**Trent Mick** 04:14 Benedict.
**Marc Pichler (Dynatrace)** 04:16 Oh, no.
Let me just do that real quick.
**Trent Mick** 04:21 We'll take a look afterwards.
**Marc Pichler (Dynatrace)** 04:23 It's, I think it's half aligned, actually. The first part that you had here, Where is it, though?
like this one wasn't aligned before, but it is now actually aligned.
Because that refers to the server part and the one below. I wasn't sure whether It was supposed to be the same.
Exactly as in the demo.
**Trent Mick** 04:56 Yeah, I wasn't sure either, but at least I got it… well, I mean, I basically just copied it over modular formatting.
Yeah.
Okay.
**Marc Pichler (Dynatrace)** 05:05 Yeah, so I think this is, This is good. I had one comment here as well.
that, like, that's used in the Docker file, and it copies stuff around, so that's why the script was the way it is.
from But yeah, I approve. Once that's sorted out.
**Trent Mick** 05:26 Cool.
And a couple to-dos, which, I mean, don't have to be a need, but, I might do… You talked about Marc having a… PR manually set up and contrib kind of ready to go. I don't know how easy that'll be, because we'll want to do a few things, right? For example, we want to do the… Redo the… bump the minimum version.
And those kind of… I don't know if we want to have… Multiple separate PRs, or one big PR that's doing that too?
Maybe it's.
**Marc Pichler (Dynatrace)** 06:03 Yeah, dude.
**Trent Mick** 06:03 and a oner.
Don't know.
**Marc Pichler (Dynatrace)** 06:06 I think it would be fine to do the… dependency updates in 1PR, We've already prepped most of it, so it should really just be a version bump for… those, and then, the minimum version, the minimum Node.js version.
would touch the same files, so I think doing it in one PR is, Easier.
**Trent Mick** 06:36 Okay.
**Jared Freeze (Palo Alto Networks)** 06:38 So is main… so is contrib main already… 3 compatible?
**Trent Mick** 06:44 No.
Oh, well.
It's still using 2.0 dependencies, because it's… we don't have a non-pre-release Release of anything that's 3.0.
The main significant One of the significant changes in the 3.0 era is dropping SDK trace-web node base. But in the 2.x era, you can make that transition to SDK trace and WebCommons, so we've done that.
So at least that chunk of work is done, if… I don't wanna… off the top of my head, I can't remember if there are other breaking changes that we'll have to adapt for, so I think it's probably close to 3.x already, but not sure until we try, which is why we want to have this PR set up to try it.
**Jared Freeze (Palo Alto Networks)** 07:31 Okay, yeah, so the, The very much deprecated, but web, instrumentations do have an interface change.
So, as long as there's a PR that goes out after Like, I don't think… If you change dependencies, the browser test will pass.
But I can't update the browser.
instrumentations until the dependencies are bumped. So… I think we either exempt that folder, or do a fast follow-up and have you guys override the unit tests that are failing.
**Trent Mick** 08:11 Okay, what… are there specifics to the change? Like, could we include that in this PR that we're gonna do, or…
**Jared Freeze (Palo Alto Networks)** 08:17 Yeah, it's basically just adding is enabled it. I, I think I already have it. I can also just.
If you…
**Trent Mick** 08:24 I mean, I'm fine if it's two PRs. Well, though, if we want to see test passing, we'll need it all in one merge PR, but we can… Have that as a draft one to show that tests will work.
Okay.
**Jared Freeze (Palo Alto Networks)** 08:36 Yeah, what I'll do is I'll base it off of Whatever you give me.
I'll just include all the changes for the dependencies, show you that the test passed, and you can make a decision whether or not you want to pull in the changes or not.
**Trent Mick** 08:50 Okay, great. Thanks.
Okay, that's that. The… did we want the… final state of the docs, or the migration doc, to be like we have it, so we have doc 3.x.
There's the announcement MD and the… Migration.md, if we want to keep it that way, that's fine.
I was gonna do another pass to the migration doc.
**Marc Pichler (Dynatrace)** 09:24 With another pass, you mean reviewing it again and see?
**Trent Mick** 09:27 Just reviewing it and probably adding some more front matter, because I imagine people aren't going to go read Because… so the way we had it this time, we had the announcement that you wrote, which was good, because we didn't have any migration information, so that was kind of the main landing page that people had.
Before we hadn't for 2.x, we hadn't really done anything like that. So we just had the migration page, and it started with some kind of front matter explaining what are we talking about here.
I might put some introductory material there too.
on… And maybe some other things, like, if you're using Auto Instrumentation's node, you don't have to change anything, you just have to upgrade, because I think everything should work.
For doses, just people who are down in the weeds doing… mucking with the SDK classes that are gonna have to do a number of migration things.
At least I hope that's the case.
**Marc Pichler (Dynatrace)** 10:19 Yeah, I think that, makes sense. So… I'm wondering if there's anything that's missing from the migration talk, too. I would have another look as well.
**Trent Mick** 10:36 Okay.
Can't remember.
**Marc Pichler (Dynatrace)** 10:46 All right, and the last one is doing the real release.
**Trent Mick** 10:54 Yeah, do we want to do this week to make October 15th-ish, or do we want to do next week?
**Marc Pichler (Dynatrace)** 11:04 I'm… somewhat in favor of doing doing it on Monday.
**Trent Mick** 11:16 So we try to get everything up and ready.
**Marc Pichler (Dynatrace)** 11:19 Yep.
**Trent Mick** 11:20 Sweet. Okay.
Works for me.
**Marc Pichler (Dynatrace)** 11:27 All right, then let's do Monday. I'll write another comment on the announcement and… We'll also write in slack.
So that people are aware.
**Trent Mick** 11:40 Okay, cool. Yeah, never mind. Don't ask questions you don't want to answer to.
**Jared Freeze (Palo Alto Networks)** 11:48 I do have one thing to add. I think on the migration doc, we might want to add a note that says.
That we want to discourage people from using instrumentation base for new web instrumentation.
This kinda goes along with all the deprecations that we made in core and contrib for the other web stuff, encouraging the new browser repo.
I can't actually mark it as at deprecated in TypeScript, because the types are shared with Node.
So I think to get code hints.
I don't think code hints are gonna work here, because we obviously want people to use instrumentation base for Node.
So I think it just deserves a comment or a note.
In docs, somewhere. And then… That… I think that's the only way to really do it without code enforcement, as far as I understand.
So.
I'll think about it a little bit, but I couldn't get the…
**Trent Mick** 12:44 estate.
**Jared Freeze (Palo Alto Networks)** 12:45 center.
**Trent Mick** 12:45 What's the alternative for… I mean, I'm basically gonna ask you to write those docs, but what is the alternative for… That you point a… Prospective web instrumentation author to…
**Jared Freeze (Palo Alto Networks)** 13:01 I mean, the alternative is something that does not exist yet. It's sitting on a branch. I know, it's part of the problem. I'm trying to hustle it through. David had good, very good feedback. I think I'm gonna simplify the model, hopefully get it out, and then publish it.
Most people are on the older… you know, I mean, there's a lot of third-party instrumentation just sitting on top of You know, the core interface, so…
**Trent Mick** 13:28 Yeah. Okay.
**Jared Freeze (Palo Alto Networks)** 13:29 I don't know, trying to hustle it through, but honestly, we can't really say, like, hey, go from fetch, old fetch to new fetch either, because it doesn't have the same data model.
So we have some thinking and writing to do about that.
**Trent Mick** 13:43 So there's definitely writing to do on the browser side for that. Like I agree that, but I mean, you do want people to make that transition, I'm guessing, right? Because you guys wanna stop supporting the older instrumentations or like.
**Jared Freeze (Palo Alto Networks)** 13:54 Yes, definitely.
**Trent Mick** 13:55 So there's, like… Yeah, some writing to say, here's the plan. Start and… Getting used to the plan, people, but yeah.
**Jared Freeze (Palo Alto Networks)** 14:03 Yeah, it's we we have all those things. They're not centralized and they're definitely not in core, like even linked. So we will make sure that happens. I think, you know, just as a vendor, like we can't make the transition now because we have to do back end mappings, right?
I would hesitate to tell everyone just, hey, drop it in, because they're not going to get the same data, so… Umm.
**Trent Mick** 14:25 Well, I know, it's a… yeah, it's a problem. I mean, you're personally speaking to… the… the back end.
Maintainers, right, Mike?
**Jared Freeze (Palo Alto Networks)** 14:34 Yeah.
**Trent Mick** 14:34 People, yeah, it's a hard song.
So yeah, if you have something you want to… definitely add to the migration doc, or, like, throw something rough and I can add it at a time.
**Marc Pichler (Dynatrace)** 14:57 Right. I guess we can have another look at the milestone later on.
But we can move on to David's topic for now. That's okay with everybody.
right?
Save it.
**David Luna Bistuer** 15:14 This is just a heads up.
That, there's going to be a… A generic policy to disallow pull request target for public repositories.
I've checked, we have this, two workflows in Core and four workflows in Contrib, that is using request target.
So, here the recommendation is just to use all the pull requests if it's possible, and if not, just to add a policy that overrides it. So, I guess for this… Six workflows that I've checked that So I think with the SysMore already we was already giving some warnings on this.
And we disabled the checks of Seismo.
Because we are not checking any… we are not checking out any code here. We're just adding, changing the title, adding comments, labeling the PRs, which is completely fine.
But still, with… since the repositories are public, this on November 2, the 2nd, yeah, it's going to be applied for all repositories for public. So we need… what we need to do, at least, what the recommendation says that we need to do is just to create our own policy.
That allows specifically that event.
For the given… for those workflows.
I'm trying it right now, and I'll send it to an elastic public repository, so… As you can provide, maybe later I can provide more insights on that.
**Marc Pichler (Dynatrace)** 16:52 Yeah, thanks for the heads up, that's good to know, and thanks for looking into that.
I'm wondering actually if some of these we could migrate away from using pull request target.
Sorry, Trent, you were about to say something.
**Trent Mick** 17:07 I guess I would try to hit up Marilia, because I think she's set up that survey and first-time PR in, like, lots of hotel repos.
**David Luna Bistuer** 17:20 I can… I can ask it, but I think that they're necessary because Portico's target has this, the token, so we have more privileges here, so we can modify the PR. And actually, those workflows, that's what they're doing, they're modifying the PR.
So that's what we did on the pull request, only we have read-only tokens.
So then we cannot add labels, we cannot modify the PR title, we cannot add some comments, so I think it's necessary.
So, yeah.
**Marc Pichler (Dynatrace)** 17:50 Yeah, I think the only way around it would be to have, to have a full-fledged GitHub app, which is… A lot of overhead, so…
**David Luna Bistuer** 18:02 Yeah.
**Marc Pichler (Dynatrace)** 18:17 I wonder, though, if the PR title won't be good.
at least migrate away, but I'll look into that separately.
I think it just verifies that the PR title has a certain format. It doesn't really change anything. So Oh.
That one.
**Trent Mick** 18:37 Yeah, maybe yes for that one.
**Marc Pichler (Dynatrace)** 18:38 Cute.
**David Luna Bistuer** 18:39 Yeah, I agree.
**Trent Mick** 18:40 The other ones might still need to… Higher permissions.
**David Luna Bistuer** 18:50 That's it.
**Marc Pichler (Dynatrace)** 18:52 All right, thank you.
Does anybody have anything else to discuss?
If not, then I guess we could have a look at the SDK 3.0 milestone.
There we have only docs updates left, and the deprecation of the packages as well as actually publishing the release.
Which… We said, we're gonna do on Monday. So Looks like everything's on track there.
**Trent Mick** 19:38 I'd added that last one, which was something Jared had started. I don't know if it doesn't need to be part of the… Or does it?
**Jared Freeze (Palo Alto Networks)** 19:46 It's safety. I you can see I left a note at the top there.
It… Yeah, I… it's… it's useful. What it… what it actually does is checks The… Code interface of Node and Browser, and makes them match.
So, I think it's incredibly useful. It helps prevent drift, as we saw in the past.
it's pretty coarse, the way it's doing this, like, everything needs a config, and you have to remember to add the config and add the test every single time there's a new package. I guess that's pretty rare, you know, it… the docs are updated to say, hey, make sure to pull this from the template.
But it is a little more overhead. You know, it's pretty ugly. You can see it's 58 files because everybody gets a new TS config.
It's it's useful. I mean, it's really for you guys to review. It's not quite ready. I'm gonna see if there's anything simpler. Let me see if I can drag this to root somehow.
And have it just walk the tree to do this, with workspaces. But if I can't, this'll be something I encourage us to do.
You know, at least figure out a way to do the check, so…
**Marc Pichler (Dynatrace)** 21:00 Yeah, thanks for working on that. I think it would be very useful to have the check-in.
Oftentimes, the types diverge.
Not even because somebody wants to change, Something, but as you saw in the, get Env.
thing. There was, like, a Boolean, or undefined in there which made its way in.
Unintentionally. So, I think it's good to have this one.
Alright, I guess, that is… it for 3.0. We also do have the SDK logs and Api logs. Ga.
Milestone… Looks like everything's done there.
Already, I have seen the issue that requests the TC review. I don't think anybody has reached out yet to me.
Oh… Haven't seen any messages. Trent, has anybody reached out to you?
**Trent Mick** 22:24 No, I was just finding the link and put it there. There's been nothing on us on their inbox. I don't think we need to wait.
I don't want to wait, because otherwise the whole release is stuck in limbo waiting for that, but… I'm gonna assume we're good.
**Marc Pichler (Dynatrace)** 22:41 Yeah, sounds good.
And there's still time until Monday, so if anything comes up, we can… maybe squeeze that in.
to the 3 to 0.
work.
**Trent Mick** 22:58 Yep.
**Marc Pichler (Dynatrace)** 23:00 Right.
I guess. If there's no other topics we could look into untriage box where we don't have anything in the query pool.
And there's one in the contract repo.
From…
**Trent Mick** 23:42 This is the first issue with both Next.js and Nest.js in the same… I'm not helping, but…
**Jared Freeze (Palo Alto Networks)** 24:04 Yeah, this might be… We might want to run… Nip.
Here, I think I have a branch to do this, that I was playing around with, to find… Undeclared dependencies that rely on transitives.
Where, like, if you… Get enough packages, sometimes you… Hit the jackpot and get all the right dependencies.
Maybe what's going on here where there's.
**Marc Pichler (Dynatrace)** 24:31 think.
**Jared Freeze (Palo Alto Networks)** 24:31 Like, TS Down has one that's missing as well.
I'm not sure.
**Marc Pichler (Dynatrace)** 24:37 I think what's going on here is that the instrumentation itself tries to… Do this to figure out… something…
**Trent Mick** 24:54 Load patch file. It is doing lazy requires.
And some exports.
It's crazy.
**Marc Pichler (Dynatrace)** 25:02 I think that's just what, then causes the build error.
Let me look…
**Trent Mick** 25:12 That was added 5 weeks ago for NestJS12 support.
**Marc Pichler (Dynatrace)** 25:18 Probably I reviewed that PR even.
**Trent Mick** 25:23 PR sent the link.
Is NestJS Core 12 on ESM?
Only so there were… I guess gross changes are… Yeah, I don't even remember making this comment, but there was a… I added a comment after it was merged.
questioning We want to do it that way.
Way down at the bottom, yeah.
**Marc Pichler (Dynatrace)** 26:09 Oh.
**Trent Mick** 26:19 Oh, and I open a PR to revert it.
Okay.
And haven't followed up.
**Marc Pichler (Dynatrace)** 26:29 probably seen all of these Prs and didn't Didn't follow up on that.
Wait, though.
**Trent Mick** 26:51 Are you… okay, I'll take a look again, then.
**Marc Pichler (Dynatrace)** 26:54 There's another Pr here.
**Trent Mick** 27:03 Is that doing similar to mine?
Oh no, mine's just an issue.
Okay.
**Marc Pichler (Dynatrace)** 27:17 Yeah, that's removing that, and then, adding this, I think that's probably what would fix it.
I'm just gonna link that PR here.
And this issue.
**Trent Mick** 28:01 I can go take a look after the call at these things.
**Marc Pichler (Dynatrace)** 28:05 Thank you.
I wonder if we would want to do another release, because that's gonna be the last version that's gonna be supported for Sdk, 3 dot. O, officially.
before Sdk, 3 to do comes out.
**Trent Mick** 28:29 To fix this bug, yeah. I mean, it'd be nice, yeah. I don't… Yep.
If we go look at PR, there might be other PRs open for other… Instrumentations that are in the same bag, so yeah, yeah.
But if it's totally broken, then for sure.
**Marc Pichler (Dynatrace)** 28:47 Yeah, releasing contrip is a little bit easier because we don't need to.
go through the whole process of updating our dependencies and then releasing another repo. might be.
Well, it might be.
**Trent Mick** 29:02 We had to do a release right before, yeah. So maybe we try to get a release out tomorrow, so avoid Friday. Okay.
**Marc Pichler (Dynatrace)** 29:10 Yep.
I'll look into it tomorrow morning in case the Pr is merged. I might ping you, David, for approval. Then.
All right. Looks like that's everything for Contribux. Does anybody have any more topics to discuss?
**Jared Freeze (Palo Alto Networks)** 29:38 I was gonna ask if David's contrib Build system update needs to go out.
With the 3.0 update.
**Trent Mick** 29:50 pieces.
But I think that one had been waiting on doing the… if I'm… this is the TS down.
Change and contrib?
**David Luna Bistuer** 30:00 Yeah.
**Trent Mick** 30:01 Okay, yeah, okay, so there's another one, thanks for reminding me, that I think having one PR ready that's gonna have I don't know. I guess… I'll take a look later today to see if I can have a draft PR that's depending on the 3.0 pre-releases of things in Core to get contrib ready to be updated, but it might be cleaner if we merge a number of separate PRs.
when we do that on… on Monday. But, okay.
**Jared Freeze (Palo Alto Networks)** 30:36 Yeah, it changes the paths, so it's… it's the same issue where… seeing code like that with the React, sorry, the require, into… deep into a file, then nest-factory.js.
I'm not sure that will still be possible.
**Trent Mick** 30:54 So I think we're getting rid of that, but I wonder if there are other required things that are going to give us some surprises in Contrib.
**Jared Freeze (Palo Alto Networks)** 31:01 Yeah.
Especially because the, you know, I'm not sure what people are up to, but, you know, if you're doing deep imports, they disappear immediately. And also, the extensions change.
So… Anyone looking for a .js file, there will be none.
**Marc Pichler (Dynatrace)** 31:28 Yeah, I'd say, having the built, update.
Would be nice to have.
Yeah. I think there's one package that is stable already in Contrib, or the rest are experimental, so it is possible to defer to later.
But yeah, preferably we would have everything done in one go.
Alright.
Any more topics to discuss?
If not, then, thank you, everybody, for joining.
Have a nice week and see you next week, hopefully with 3.0 published.
Cool.
**Trent Mick** 32:32 Thanks. Yeah.
**Jackson Weber** 32:33 everyone.
**Marc Pichler (Dynatrace)** 32:33 Thank you, bye.
**Jackson Weber** 32:34 But…
