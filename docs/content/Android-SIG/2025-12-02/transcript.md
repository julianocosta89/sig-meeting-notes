SIG: Android SIG
Date: 2025-12-02
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**JP Jason Plumb** 00:56 Good morning.
**cleverchuk** 00:59 Hello.
It looks like it's just gonna be us.
**JP Jason Plumb** 01:10 Yeah, it's pretty slow this morning, huh? Might be like this for the rest of the year, I guess we'll see.
**cleverchuk** 01:15 Yeah.
**JP Jason Plumb** 01:26 Are you a West Coaster?
**cleverchuk** 01:28 Middle East.
**JP Jason Plumb** 01:31 What's that?
**cleverchuk** 01:32 East? Yeah.
**JP Jason Plumb** 01:42 Well, let's give it a few more minutes and see if or who anyone shows up yet. Have you had a chance to play with RC1 yet?
**cleverchuk** 01:51 No.
**JP Jason Plumb** 01:55 Cool. I understand, I mean, it just happened last week, so… Just, I don't have a lot of topics, but I did think of a few things yesterday.
But if it's just you and me, we'll push it till next week.
**cleverchuk** 02:10 Yep, sounds good.
**JP Jason Plumb** 02:13 It looks like I might have some DMs, let's see.
Nope.
Hey, Iroh, we're still waiting for people to show up.
**Jairo Mendoza** 02:50 Hello. Good morning.
**JP Jason Plumb** 02:52 How's it going?
**Jairo Mendoza** 02:54 It's going good.
**JP Jason Plumb** 03:06 I swear my home office is, like, directly over my furnace, and, like, first thing in the morning, it kicks on, and it gets so hot in here. Hold on.
Well… I was chatting with Cleverchuck, and it looks like, It might be a pretty slow week.
If people aren't showing up, I know that Cesar is out until January, I'm not sure about the Embrace folks, or Mustafa, or anyone else, Manuel… so we don't have to necessarily talk about my topics unless you want to, or if, unless you have anything else that is on your mind, I'm happy to bump these to the bottom of the agenda if you'd like.
I was soliciting, if there's any feedback yet on RC1, and I'm not sure, Jairo, if you've had a chance to check it out yet.
**Jairo Mendoza** 04:11 I have not… I've… I saw that it was released.
**JP Jason Plumb** 04:16 Yeah.
Cool.
I mean, it's also a weird time, like, it was during the Thanksgiving break here in the States, so, you know, maybe just people have not had a chance to… to check it out yet, or… Yeah.
I don't think there have been really any new issues or anything on it.
Yeah, there's nothing specific, doesn't look like anything… specific to RC1 yet.
Hi, Jamie.
Looks like a pretty slow week.
Any topics on your end?
**Jamie Lynch** 05:03 I… Didn't have anything myself, I think Hanson should be coming in a minute, so we can ask if he's got anything.
**JP Jason Plumb** 05:11 Cool.
Once again, I appreciate your help on reviews. It's very helpful.
**Jamie Lynch** 05:18 Oh, no problem.
**JP Jason Plumb** 05:19 Yeah.
**Jamie Lynch** 05:20 Yeah, it has been slowing down a bit, in terms of PRs, which is, thanksgiving, I guess.
**JP Jason Plumb** 05:26 Yeah, I'm assuming that's why.
Okay, well, yeah, any feedback yet on RC1 from anybody on your side?
Jamie?
Seems like no one's… no one's kicked it around yet, so I guess we'll wait.
If any feedback comes in, feel free to add it to that umbrella issue.
I'll just… the intent is to leave this open… Is it this one?
get this one.
We'll leave this open until we actually drop the 1.0, so… Hey, Hanson.
**Hanson Ho** 06:16 Hey!
**JP Jason Plumb** 06:19 Okay, so yeah, I'll just leave that there. If you or your users have any feedback, they can drop it into here, async, or bring it up next SIG meeting.
I did want to bring up this thing.
Because this is kind of like… This is kind of like the UI one.
That's been hanging out forever, and we don't have a clear path to merge this. You know, in the… I think in the UI one.
Let me double check.
I think in the UI one, there's only one dependency, and it's from the demo app?
No, it's not. It's for the Compose instrumentation. Okay, so it is very similar.
in that we have these dependencies that we cannot update. In this case, specifically, our min SDK is older than what the library requires. So my question is, what do we think we want to do about this?
**Hanson Ho** 07:20 once 1X becomes stable, we cut 2x, bump it in SDK, and bump this stuff.
**JP Jason Plumb** 07:31 Yeah.
**Hanson Ho** 07:32 Cuz… I think we said we were gonna tie our min SDK to Play Services, and I think Play Services bumped Min SDK to… what was it, 26, or something quite high.
**JP Jason Plumb** 07:45 Are they really?
**Hanson Ho** 07:46 24… it's something quite high, I remember. Shockingly high. Okay.
So, I think… I mean… until we satisfy the MIN requirements, we can't update these libraries. So we should probably either close it or do some sort of deferral. And then when we can.
by bumping up, like, we should also consider bumping up, Kotlin, dependency, or Kotlin, compatibility. So for the Embrace SDK, you know, we did a, a review of a bunch of, basically, our, our, our, minimum requirements, and, you know, having Kotlin 1.8 is restrictive, having… but necessary for certain Gradle version support. If this project doesn't support that, we could start thinking about bumping some of that stuff up so that when Kotlin 2.3 arrives, you know, we wouldn't be caught flat-footed.
And… and with these as well, there comes a point where, if… if everybody in the Compose, Mainstream says, hey, you need a certain or not, not Compose Mainstream, but, like, the, the, the Google Play Store Android dependency… You need Min SDK24, everybody who uses Play services.
then it's almost like, well, we… folks need to use Play Services, so it's time for us to bump as well, so… Yeah.
**JP Jason Plumb** 09:21 Yep.
And I was just double checking that we do have this written down, and that's good.
And so… we don't have the actual number in here, but we linked to it.
Is it easy to find…
**Hanson Ho** 09:50 23…
**JP Jason Plumb** 09:52 Is it this?
**Hanson Ho** 09:54 Yeah, I think…
**Jamie Lynch** 09:56 That makes sense why I felt like we bumped to 23.
**Hanson Ho** 10:00 Yeah.
**JP Jason Plumb** 10:02 Right, so this is because we're still supporting 21, and so that's where this… breakage comes in. Okay, so your suggestion, Hanson, is to… Wait until we've released 1.0 and then immediately bump everything up and release 2.0.
**Hanson Ho** 10:17 Not really.
**JP Jason Plumb** 10:19 Yeah.
Okay. Well… I mean.
**Hanson Ho** 10:23 I feel ya. That is an approach. It is…
**JP Jason Plumb** 10:28 Considerably more work to maintain two release branches.
**Hanson Ho** 10:33 Oh, I think no one's gonna use… one.
Unless… unless they… or rather, people won't be, like… I'm hoping people won't be, like, Keep improving one.
The alternative is we make this change in 1 and say, sorry, there's not going to be a stable version that supports 21.
Which… may be okay.
But… like, I think we were talking about, having to be a bit more radical, anyway.
**JP Jason Plumb** 11:09 I mean, that's definitely our opportunity to do that, you know, and what we would do is we would have… to be our main line, right? We would be building 2.x off of main.
It's… but then, that's challenging… Because do we call that stable, right? And I guess we kind of have to.
Because that will be… I mean, that will be people's expectation.
**Hanson Ho** 11:41 So, and we could… I mean, that's actually another fair thing to do, would be… would be declared, cut 1X, go 2X, Declare it, you know, bump up all the min versions that we want to have, like, a maintainable base.
Declare that stable.
And then anybody who wants… who really needs two, like, 21 could go with 1.
And then 2 becomes our line going forward.
Because it's as stable as one. And the hope is that people won't… like, unlike a backend component, people won't grasp onto 1.0 and be like, I will never change from this. Especially if we start adding features only to 2.
**JP Jason Plumb** 12:28 Yeah.
**Hanson Ho** 12:28 And we compel upgrade because it is better, and it has better features.
**JP Jason Plumb** 12:36 So I think what I'm… I think what I'm hearing, too, is that bumping min SDK is always a breaking change for some users.
**Hanson Ho** 12:46 Potentially, yeah.
**JP Jason Plumb** 12:48 And so, will we need… anytime we bump… like, once we've gone stable, like, we've gotten away with it so far because we haven't been stable. Once we're declared stable, anytime we're gonna bump a min SDK version up, does that mean we need to do a major version bump?
And if so, then my follow-up question is, how often does Google bump that version?
**Hanson Ho** 13:09 Not very often, I think it's been 21 for a long time. 21 is… is Android 5?
And that was 11 years ago.
11? Or 12? I don't know, I can't do math.
**Jamie Lynch** 13:23 I'd say it's fairly infrequent, maybe every year or two, that play services themselves would bump.
I think… maybe… the other thing to consider is there will be other versions that are going to start ratcheting up, so, like, Android Gradle plugin.
**JP Jason Plumb** 13:44 Yeah.
**Jamie Lynch** 13:44 But the other ones, like, some of the jetpack libraries might… Go higher, because they do their own versioning.
Coppin, for instance, that's… Releasing at least once a year, and they only support the four last minor versions.
**Hanson Ho** 14:05 Like, we should probably consider… Major version bumps.
at least once a year, if not more frequently, just… frankly, just to keep up with the min version requirements. Kotlin's the one that's gonna push us.
Forward, because, Compiled against 1.8 compatibility, I don't think it will work.
If the math is right, with 2.3.
So when that happens, and people try to, in their app, deploy a 2.3 at runtime, they'll be like, -oh, we can't use this. So at that point.
And, you know, if we do this quick 2.0 stability plan, we could not only bump the min SDK, but we could look at some of the other, dependencies, like AGP and Gradle, and Kotlin, and Java, and basically say, hey, we're gonna, we're gonna bump all those up as well.
So, it'll be significant in the sense that we're gonna drop a lot of, like, dead… not that old, dependency versions. And basically start… Fresh.
**JP Jason Plumb** 15:17 Yeah, I wonder… I wonder in practice how we do that, so… Let's say this week we decide to make 1-0 official.
And it lands, and we're… we've… we've published 1-0.
And then… Tomorrow we're like, okay, cool, we've got lots of free time, time to get 2X going with all these updated versions of… Kotlin, AGP, min SDK. So, we will already have a release 1.x release branch.
Without RC in the name. In fact, oh, I think that's something I discovered… During the release process is that we… Have… this 1X, branch… Oh, it's 1.0.x. Okay, so the next release that we do… I think, given the way that the release, pipeline is currently built.
I think we should do a 1.1 as our next release, that will still be RC2. I know it sounds weird, because we're kind of, like, bumping two versions. If we don't, then we… then it will… need to be 100RC2, which is… which is the plan. I'm talking this out loud, sorry, I'm not awake yet. And that'll go into the same… The build process will try and create a release branch with the same name, but it already exists, that's probably fine. And then the tag… will be like this. That should also be fine, because it'll be RC2. Okay, sorry, this has been nagging in the back of my head since that release happened, so, The disconnect between the tag and the actual branch is what's been concerning to me.
**Hanson Ho** 17:07 Hmm.
**JP Jason Plumb** 17:08 Ideally we would have… I don't know, something else in here. But I think RC2 will need to come out of the same… branch, which means any PRs that we're merging now are not in this branch.
If that makes sense, right? The release branch is cut from Maine.
And in our case, we already have that release branch, and it's now fallen behind main.
That's my… that's what I'm getting at.
So there's some… There's some work around this, there's some… there's going to be a challenge, and I don't know what that looks like yet, but I'm gonna make a note of it.
**Hanson Ho** 17:45 Well, main is effectively 1.1.
without us saying it. So, anything we have to… we want.
in… Correct. Go to Maine and cherry-pick, right?
**JP Jason Plumb** 17:58 Yeah, I mean, that is a good point, and we could just cut RC2 off of that existing branch with no changes, right? If no one has feedback on RC1, then RC2 or 1.0 is solid.
is just built off of that RC without any other changes, right? I mean, I guess that is how people develop software.
I'm gonna have a little more coffee.
**Hanson Ho** 18:24 I feel… I feel one is… is basically us just taking what we have and calling it stable.
And… and… because people are using it, we don't want to make a ton of, like.
housekeeping changes. But two is, I think, where we're gonna be like, okay, do we seriously support AGP 7.4, or whatever?
**JP Jason Plumb** 18:46 Oh yeah, so I got distracted as I was talking through that process, right? So, we released, like, this Stable 1.0, This week, let's say. And then next week, we decide to do 2-0.
So, in the main branch, do we just change the version to 2?
Do we pull stable back off of… the… initializer of the agent? Do we… do we pull… do we turn that back to alpha for some time?
**Hanson Ho** 19:17 How does it work? Like, how…
**JP Jason Plumb** 19:21 The, like, logistics of it?
**Hanson Ho** 19:23 Yeah, like.
**JP Jason Plumb** 19:23 Yeah, yeah, so there's, do we… do we lose stability when we declare a major… like…
**Hanson Ho** 19:28 That's not…
**JP Jason Plumb** 19:30 That's not normally the case, right? Normally, you're working toward a stable version, like the next stable version.
And so, I don't actually remember how we did it with Java.
Because I am still not awake yet.
**Hanson Ho** 19:46 So, so say we, say we could, like, bump Min SDK without changing the major version, and we do that.
and we basically have 1.1 that is, like, a bunch of, like, dropped a bunch of versions. What's the difference between that? Like, in a practical, you know, tagging and… Yeah, yeah, it's… but if we're calling… if we're bumping the min version.
**JP Jason Plumb** 20:09 If this is a breaking change, right? If we bump to 23.
That's a breaking change.
The assumption is that you cannot do braking changes without a major version bump.
**Hanson Ho** 20:20 Right.
**JP Jason Plumb** 20:21 That would need to happen in a 2.
**Hanson Ho** 20:23 Okay.
But do we lose the stability tag because we've done a major version change, or do we just still keep it?
**JP Jason Plumb** 20:34 No, I think we keep it.
**Hanson Ho** 20:36 Okay.
**JP Jason Plumb** 20:37 Yeah So I think… I think we need to keep it.
**Hanson Ho** 20:41 Like, then we'll start releasing, snapshot builds that are gonna be 2.0, but, like, obviously with all the things, and then when we next release, it'll be stable 2.0.
**JP Jason Plumb** 20:55 Yeah, which is maybe why we should probably have a 2.0 milestone that we now start adding stuff into, which is, like, let's bump GP, let's bump up them in SDK, let's bump up Cotton, let's get those issues created, and put them into a 2X milestone.
Yeah, it's good. I can't believe we're already talking about 2X, but it's exciting. Like, it is, I think, I'm following this train of thinking, I think it's good.
Okay.
**Hanson Ho** 21:25 Android libraries move a lot faster, and really, the reason we're cutting… the reason we released Windows as it is is because it won't just be too disruptive. We say, okay, you can keep what you use, but don't expect new features on it. And the major upgrade is going to be I think trivial for people who are already, like, in SDK 20, you know, 3 and above.
**JP Jason Plumb** 21:47 Yeah, so the… my… I guess we don't have a policy around this, but we need to come up with one. How long do we keep doing, releases in the previous major version?
So, in this, in this hypothetical scenario, we cut one today, we cut two next week. How long do we keep, How long do we keep Dependabot turned on, the 1X branch, for starters, and then how long do we do releases out of there? If it's purely ad hoc or, like, on demand.
then we should talk about that, but I think at least having Dependabot working over there seems like a good idea, because that will address many security issues.
Right. I mean, that's the main reason we get dinged, is because there's an upstream security issue, and we depend on older versions, so Dependabot helps to keep that up to date.
**Hanson Ho** 22:41 So… there are rarely Android dependencies that lead to security.
Issues.
Like, I don't recall releasing a new version because the dependency had a security issue that needed to be, that needed to be inserted.
**JP Jason Plumb** 23:05 Oh, I bet you OKHCP has had one in the last month.
**Hanson Ho** 23:11 Really?
**JP Jason Plumb** 23:11 I bet you it has.
**Hanson Ho** 23:13 Hmm.
**JP Jason Plumb** 23:14 But, if not that, then something else.
**Hanson Ho** 23:19 I would… I would be… Yeah, maybe this is worth a longer discussion. I would be… I would be, I think once 2.0 is, like, the first version is out, and people can start adopting it, there would be a really… you have to have a really good reason to update, and release, 1X.
Like, like you said, like, security issues. And yeah, if we wanted to keep Dependent Bot turned on just for security issues, it basically auto-closed everything else. I mean, clearly the things that require, admin SK bump, we can't merge.
So we all, like, permanently ignore those ones. And, and basically, but, like, for, for non-security updates, I wouldn't even, like, if there's a new version of, like, OKIO or something like that, and, you know, it's just features, then, like, no.
**JP Jason Plumb** 24:13 And then, probably only cut… I don't know, like, maybe we do, like.
2 or 3 months of releases, and then we say it's on demand after that for another 3 months or something?
I just don't… we don't have it written down. It'd be cool to have consensus on how long, because it is work to do that stuff.
**Hanson Ho** 24:33 Yeah, I think… I think as little as possible, because we wouldn't have new features in it. I think that's what would compel, like, an upgrade. So if we want to keep doing releases for it, I think there has to be a really, really good reason why somebody would want to upgrade to 1.0… well, 1.1.
And if it just ends up being dependencies, then… We could let it build up, let it build up, and see if anybody wants it, and then if somebody wants it for some reason, then we release it, and then… and as you said, like.
Have that slowly peter out as people adopt, too.
Like, what would Splunk do, if we bumped this? Like, would they, would they still keep one? If, if, you know, the SDK is okay to have transitively bump the min SDK?
they'd probably look at the customers and see who would not be able to use it, but they could also use the old version of Splunk.
**JP Jason Plumb** 25:30 Totally.
Yeah, I can speak to how we did it in our Java agent. Now, I understand that it's different on mobile, and maybe there's, like, fewer… Dependency problems, but we, we had stuff sneak in for a few months, like, and by sneak in, what I mean by that is we had… we had issues that were raised that we needed to do releases that tracked all the way up to Upstream for, like.
I'd say at least 3 months. It might have been slightly longer, because we had people that could not upgrade yet, and we had… we had, like.
It was mostly security issues that were found.
**Hanson Ho** 26:06 Hmm.
**JP Jason Plumb** 26:07 through dependencies.
And then eventually we said, well, we'll just stop releasing this, and we'll do it as on-demand, and that worked out fine. So I think on-demand…
**Hanson Ho** 26:21 Yeah.
**JP Jason Plumb** 26:21 is probably reasonable. So, like, once you've decided this is stable.
I think… so there's a window, then, between… when you've declared that 1X stable, and you've decided to maybe not do more releases out of it, and then the time that you do the next major version bump. So you kind of… you kind of need to be ready with that next major version bump. Otherwise… No, because that next major version is going to be coming off of… No, it needs to be a… it needs to be a major branch, because, As soon as we bump any of these breaking things, it needs to be in a different branch.
**Hanson Ho** 27:02 Well, I mean, the… the one… the current branch we have for 1.0x would be the trunk for 1.1. So.
**JP Jason Plumb** 27:14 True, yeah.
**Hanson Ho** 27:15 So… so, like, as you said, we could… we could… Maintain it.
**JP Jason Plumb** 27:20 Although right now, right, any changes that are happening, those are going into Maine.
**Hanson Ho** 27:26 Yes, because we haven't declared anything for main. Main is still implicit 1.1 right now, so we have to basically say main is no longer 1.1 by breaking it.
**JP Jason Plumb** 27:39 And that needs to happen as soon as we… as soon as we do the stable release.
This is… sorry, I'm breaking my brain. I think I'm overthinking this, to be honest.
**Hanson Ho** 27:56 I, I think, I think, I think your plan of, of releasing for a few months and then on demand is, is good. I think even releasing on… releasing for a few months.
that could also be, like, is anybody gonna use it on demand kind of thing? Like, we can still update the repo, and with dependency updates that are safe. And, you know, once somebody says, hey, I can't switch to 2X, And there is a critical change I need in this, then we'll do a release.
I don't think there's gonna be that many to cause, like, a lot of work, which is why I think it'll be okay for us to kind of keep in that state. And then once, you know, two has gained momentum, and people are basically creating PRs on top of that, and we're doing new features and all that stuff.
One will die simply because it's… it's inferior.
So I think mobile apps, people are a much more, willing to kind of give new SDK versions a try, just because the surface area is, is, there are less concerns of, like, it nuking a whole bunch of bad things. So… hoping that we could find some stats eventually to say, hey, basically this is unused, or very rarely used. And frankly, if it's not, then, you know, we make changes there. But… I somehow don't think so. I think you… people are using it a lot from, like, the Splunk distributions, the Honeycomb distributions, and the Elastic distributions. So as long as you know.
the people in charge of those kind of forks are updating. Their customers will be updating implicitly, so…
**JP Jason Plumb** 29:46 Yep.
Okay, so I think to answer this question about what do we do about this, for example, and whatever the other one was, that I think I already lost, but… Yeah, this one. So, like, one's like this, but these two are the open ones that I'm aware of right now. I think what we should do is we should pin these… to the current version. So we should go into the Dependabot config, pin these so these PRs don't happen, close these PRs, and then just say, and file an issue to bump them up after we do the major version bump.
Does that sound… Like, a plan? Is that… are we aligned on that?
**Hanson Ho** 30:27 Yeah.
**JP Jason Plumb** 30:27 Okay.
**Hanson Ho** 30:36 Are there any outstanding PRs that's on the 1-0 line?
That folks are still working on?
**JP Jason Plumb** 30:42 I mean, there's a ton of PRs right now.
Yeah, so it's gonna be this, this one, this one… I mean, I guess I could go into the Dependabot issue and see these more easily, but it's like… Let's see…
**Hanson Ho** 31:03 Actually, you know what, that's fine, because those are against main, so once we flip main to 2, they will implicitly be… be targeting 2 in the… for these PRs.
**JP Jason Plumb** 31:11 I thought there was an umbrella issue for this.
Yeah, this thing.
So this one, this one, and this one… okay.
So we'll have 3 that we need to pin.
And I can look into doing that.
And sorry, Hanson, to your point, you were saying that, I mean, there's a bunch of these that are still targeting the main branch.
**Hanson Ho** 31:47 Yeah, I think I just talked myself into it being okay, just because they're targeting main, whatever main is, they are targeting that. So if main is 1.1, they're targeting 1.1, main is 2, then I'm targeting 2. Yeah.
**JP Jason Plumb** 32:00 Yeah, okay.
Yeah, we're in this weird… we're in this weird state right now, though, where people… including me, might be thinking that changes that are currently going into Maine would make it into RC2.
**Hanson Ho** 32:16 Oh, really?
**JP Jason Plumb** 32:18 I mean… Yes, that's… I think that to be true.
**Hanson Ho** 32:24 I thought when we cut a branch, the bar goes higher because we have to cherry-pick, and…
**JP Jason Plumb** 32:30 It certainly does, but I think it's easy to overlook.
That… The… the… I guess another thing to consider is that, 1… 0 should follow 1.1.0, sorry, 1.1.0 should follow 1.0.0.
And if we're cutting 1.0.0 off of… the branch… then anything that we cherry-pick into the… any changes that make it into the RC now, any changes that go into here. And I appreciate you letting me talk this through out loud, because I don't have anyone else to talk this through with. Any other changes that go into here will be in RC2.
And anything that we do allow to make it into RC2 needs to be cherry-picked into main so that it lands in 1.1.
Are we aligned on that?
**Hanson Ho** 33:32 Unless we're saying 1.1 is gonna be cut from Maine.
**JP Jason Plumb** 33:36 It will be.
**Hanson Ho** 33:38 If 1.1 is cut from main, then this is just 1.0. So, 1.0.1 will be cut from this branch.
So, I think, I think it's… what… what… what is main? Maine right now is 1.1, so I think, we release our seat 1.0… RC1?
will be coming from that branch. If we merge something, into main.
that will need to be cherry-picked if it needs to be in 1.0. But if it's okay to be in 1.1, then we don't need to cherry-pick it, and that just goes into 1.1. So… so if we… there are features that we still want in the 1X branch.
then we'll basically leave 1X without the bumping dependencies, have that merge, cut at 1.1, That wouldn't be RC, that'd just be 1.1, you know, whatever, right?
**JP Jason Plumb** 34:33 Yeah, yeah, and I think the way to think about this, I think, we should treat this like a patch release. Like, as far as the workflow is concerned, right? So the patch releases come off of an existing branch.
**Hanson Ho** 34:46 Yes.
**JP Jason Plumb** 34:47 Which we… don't have a good description of in here, is that true?
**Hanson Ho** 34:53 patch release come… oh, okay.
Wait.
**JP Jason Plumb** 34:56 Have we ever done a patch release in Android?
**Hanson Ho** 35:01 Oh, yeah, a patch release, yeah, yeah, the third, the third of the… okay, yeah.
**JP Jason Plumb** 35:07 Yeah, and so I consider that RC that's hanging off of there kind of like a patch, right?
**Hanson Ho** 35:14 Yes.
**JP Jason Plumb** 35:15 What we have right now is what we consider to be our release candidate.
We think very little will go in there, just like after we cut… A.B.C, you don't expect anything else to go into C, and you would rev it to A.B.D.
By being very finite in what you've chosen to bring in there.
Okay.
**Hanson Ho** 35:42 I think RC should… like, RC2 should be… if we cut it RC2, it should be identical to RC1, unless… Yeah, exactly. Unless there's something… yeah.
**JP Jason Plumb** 35:50 I mean, I think if we get no feedback on this, maybe it's a weird time, we should just wait until January to cut 1.0, because everyone's out, and vacationing, and holidays and stuff, but… I mean…
**Hanson Ho** 36:04 I think the longer we wait on that, the more challenging it becomes.
if we release it this week or next week, and somebody comes in January and says, hey, I really need something there, we could always do 1.0.1.
**JP Jason Plumb** 36:19 Yeah, or 1.1.
**Hanson Ho** 36:22 Yeah, so maybe the thing that we stop and wait on is bumping all the min releases, the MIN SDKs, in main. So main is still potentially 1.1.
and then we'd wait till January and be like, hey, everybody cool? Nobody wants anything? Like, the ones that are outstanding, the PRs, no one wants to get it into 1.1. If everybody's okay, hey, we're gonna bump the inversions and have a 2.
you okay with upgrading in there? Cool, we can do that. And then… then we just bring that forth, and… and break shit.
**JP Jason Plumb** 36:56 But I think… I think we do con… let's just say… let's say… I think the idea right now is that we should just continue every month releasing 1.1, 1.2, 1.3 off of main. Until we think we're ready, until we have our ducks in a row to do the 2X, which I think really is… Taking everything from the 1.whatevers, and then also bumping all the min versions.
**Hanson Ho** 37:21 Yep.
**JP Jason Plumb** 37:21 So that's why I will take that milestone that we have… that way we have a pretty good list that we can.
**Hanson Ho** 37:25 I like that.
**JP Jason Plumb** 37:26 toward… And then, every month, we'll just continue bumping, you know, the minor version, as we always have.
Okay.
**Hanson Ho** 37:38 And the whole thing by February would be… Good enough to be like, okay, let's just… Bump all this other stuff.
**JP Jason Plumb** 37:46 Yep.
**Hanson Ho** 37:48 We should forget when Kotlin 2.3 is being released, because I think that would, That would be a very good motivator.
**JP Jason Plumb** 37:55 What version of Kotlin are we on? 2?
**Hanson Ho** 37:59 We are… I think we're… I think… I think we do, we're using 2.2, runtime.
**Jamie Lynch** 38:09 building… With the latest, but targeting the oldest.
**Hanson Ho** 38:14 Yeah.
**JP Jason Plumb** 38:15 So is it this? That's what we're.
**Jamie Lynch** 38:16 Yeah, that's…
**JP Jason Plumb** 38:16 Okay.
**Jamie Lynch** 38:17 You… yeah, we compile with 2.2, and then we target 1.0.
**Hanson Ho** 38:22 Yep.
**JP Jason Plumb** 38:24 Which is going away.
In what version of Kotlin? 2.3?
**Hanson Ho** 38:29 Yep.
**JP Jason Plumb** 38:30 Okay.
**Hanson Ho** 38:32 I think… I think Jamie and I are working on… on the… based on the floor version math, that… that… That 1.8 compatibility is not gonna be… Oh, hey, January 2022, or 2026.
**JP Jason Plumb** 38:49 upcoming… Yeah, okay. That's real soon.
**Hanson Ho** 38:54 Yep.
**JP Jason Plumb** 38:58 Cool.
Alrighty, that's fun.
What else do folks want to talk about?
**Hanson Ho** 39:19 Nothing right now.
**JP Jason Plumb** 39:20 Yeah, I have this other… I have this other item in here.
I just want to remind folks again that, like, having Additional eyes, on pull requests is very, very helpful.
even the dependency ones, like, going in there and having Jamie having had called out exactly why that one, Dependabot or Renovate, rather, PR was broken, it's because, you know, of the min SDK version of the dependency. Like, having that in there is, like, even… even stuff like that is, like, very helpful.
to a maintainer, to be able to, like, to not have to do that legwork, to know instantly, like, why that was broken. And any feedback on other pull requests is also super helpful. Like, again, Jamie chiming in on that massive PR and, like, working with that person.
to break that down into smaller units, super helpful. You beat me to the punch, and it was really, really great. So, that work is super appreciated.
But that's also true of people that are not maintainers, so if you… if you're on this call and would like to become a triager and work your way toward approver, like, that… just even going and making comments on these and making suggestions or saying, looks good, like, that's all really helpful.
Like, even if you don't get the green check, just having comments in there is really nice.
**Hanson Ho** 40:43 We talked about putting in additional usage of tags and stuff. Do we formalize any process about that?
**JP Jason Plumb** 40:52 No. We talked about it, like, two, two, two meetings ago, I think.
**Hanson Ho** 40:57 Yeah.
**JP Jason Plumb** 40:58 Yeah, I don't think we… I mean, we added a few more, and… I don't know… I don't think… I don't think we've used them that much.
No, I don't think… I think the answer's no.
**Hanson Ho** 41:17 Okay.
Might be good to have… have some guidance on… on, like, how… how the… how we want to use the tagging, and… Because we talked about, hey, maybe somebody should just go in there once a week, or, like, do a rotation where, you know.
every Tuesday, this person does it, every Wednesday, this person does it, and just kind of…
**JP Jason Plumb** 41:37 I would love us to all be doing it all the time. Like, that's… I think there's enough… I think there's enough activity now that it's becoming challenging for me alone to keep up with, and especially with Cesar out, it's like… Just as, like, one arbitrary example, because I had it on screen, like, this is an old PR, right? It goes back a ways. I was chatting with another maintainer from a different project about some of the process kind of stuff.
And… I was, like, I was speaking to the idea of the role of maintainer, and, like.
I come back in on these, and I'm like, this has been sitting out here for a while, are you coming back? Ad needs author feedback. Yeah, okay, still working on it, still working on it.
hey, it's close, can you come back? Yeah, let us know. And then, like, they've dropped off, it seems. But they came back, okay, cool. So basically, like, nurturing this PR, but at some point, it's like, well, you haven't been in here since June 3rd. We're trying to cut this major release.
And, like, you haven't been able to come back. And, I mean, life happens, and people's priorities change and stuff, that's always gonna be the case.
But I did end up, you know, adding needs author feedback again, and I think even on this issue, I think I took them off of it. Yeah, they were assigned to this issue, I think, and I took them back off, like, yesterday.
Because I'm like, it doesn't seem… like, this is a, like, just a small wave to maybe get their attention, like…
**Hanson Ho** 43:06 I have no… like, you're no longer assigned to this issue, maybe someone else will pick this up now.
**JP Jason Plumb** 43:11 And eventually, if they don't come back at all, then hopefully, I think… this needs author feedback, we'll kick in and mark this as stale, and it will get closed. I know that that happens for issues, but I want to double check that it happens for PRs, so let's do that.
Stale.
**Hanson Ho** 43:33 I feel like if I had a PR that's been going back and forth, for, like, a year, and it gets auto-closed because of an activity, there should… there should be no qualms about it.
**JP Jason Plumb** 43:44 Yeah, yeah, totally.
So, this did get marked stale. Yeah, so needs author feedback.
was put on there. There was… no activity? I don't know what this comment made Doesn't count, but it did get marked stale. Yeah, here it is. So, it needs author feedback, 21 days, so I think that's pretty generous. Like, no traction for 3 weeks, and then it gets closed as stale, Two more weeks, or… Yeah, 2 more weeks after that it gets closed. So, you have 3 weeks until stale, and then 2 weeks on top of that before closed. And if you're the author, you can still always reopen it, right?
**Hanson Ho** 44:22 Exactly.
**JP Jason Plumb** 44:23 It's not like the end of the world, but it's a way to help keep that list down.
**Hanson Ho** 44:27 Yep.
**JP Jason Plumb** 44:28 So marking things that are old with needs author feedback, like, actually, like, putting a comment in there that says, hey, we have open questions, they're X, Y, and Z, or can you respond to this thread? And then marking needs author feedback, that's an important activity for… contributors to do. I mean, approvers, I think, are the only… only… approvers and maintainers are the ones that can add labels, I think.
But that's a super important activity for approvers to be doing.
**Hanson Ho** 45:00 Yeah, Tuesday's my day of looking at this stuff, and last Tuesday, I was pretty much out, so… and today's Tuesday, so I can still look at this stuff.
**JP Jason Plumb** 45:07 Sweet.
Okay, I did, I did make another little baby comment in here about maybe having an open call for contributors, because I think we could use help, and every project in OpenTelemetry is basically understaffed right now, and it's hard to get more contributors. We've… we've grown and grown and grown, and we're kind of like, maybe that growth is slowing down a little bit. I know that in Java Core.
I think it's still the case.
They have this… Let's see… They have this little blurb.
And I was thinking that maybe it would be valuable for us to have something similar. That way, when there's interest or people come across the project, they see that they're looking for additional contributors, and you can click on this… And it drops you down to the Help Wanted section. So, they have the little blurb at the top, and then further down the page.
they have what it takes, right? Or what we're looking for. I was just curious if people thought it would be a good thing to add to our README.
**Hanson Ho** 46:17 I think so, but, to add that to the remake, you'd also have to have, like, all the other stuff downstream. It's like, hey, this is what you can do, these are some issues, and… This is how you… so, that'd be nice, but it takes a bit of work and thinking.
**JP Jason Plumb** 46:34 It's true, but, like, letting people know that pull request reviews are equally or more helpful than code contributions. That may not quite be true in Android yet, although I'm inclined to say it is. Certainly in Java Core, they get more pull requests than they can review.
And, I mean, we're maybe not quite there yet, but I haven't reviewed these.
I'm a little bit behind on reviews, so… I don't know.
**Hanson Ho** 46:59 So, do we want to brainstorm, maybe not this meeting, but, like, the next one, about, what, what we want to say, and then basically have someone just type it up?
**Jamie Lynch** 47:09 Can we just, kind of, copy what's in… OpenTelemetry Java.
**JP Jason Plumb** 47:15 I'm inclined to, honestly, and maybe… maybe edit it a little bit, but yeah.
**Hanson Ho** 47:21 Yeah?
**JP Jason Plumb** 47:26 Let me link to that.
Oh, yeah, just… just because we don't have a really packed agenda, and I remembered this, and I thought it was a little bit interesting, if you haven't seen this yet, and I bet you most of you have not, check out this thing.
So yesterday… This PR was added.
and merged, and what it allows is… so, if you haven't seen the CLO monitor.
The CLO monitor is a CNC… I think it's a CNCF project. I mean… I don't know, maybe CNCF is… using CLO Monitor.
But CLO Monitor is a tool that will evaluate your open source repository for kind of, like, industry-accepted best practices, and it's broken down into several categories, and it kind of is a suggestion about the maturity and, longevity potential for a given open source project. And look at how good our score is now! So that PR that was in there yesterday, bumped this up. This used to be red.
And now it's green. So if you give these any sort of attention, you can see, like, what each of these is. Like, you click on changelog, it takes you to our changelog. If you click on, like, the list of maintainers.
It shows you who the maintainers are… well, it shows you what the group is, whatever. You can go into the groups for the org and find out who those are. Anyway… pretty interesting CLO monitor, and the thing that was linked to here now, license scanning, so if you click on this, it takes you to FOSA, which is a tool that's used to scan the licenses to make sure that we're not depending on some… Not accepted, usually GPL, style licenses, or closed source license, or, proprietary license.
So if you haven't seen the CLO monitor, it's pretty interesting. I don't know if we have a build badge for it, that would be kind of… It'd be kind of interesting to link to that from the, like, from a build badge. I don't know if other repositories do that. But you can see that we're 92, everything's green, licenses look good, best practices… we've got a few exceptions here.
So I think Trask put these in. I don't fully understand all of these exceptions or why we don't work toward them, but we do have, like.
You know, we do have this scorecard on the OpenSSF, That's pretty cool.
We've got some criticals, apparently.
But it's green, so I'm not… I don't know.
**Hanson Ho** 50:27 Just kidding.
**JP Jason Plumb** 50:27 do some, again, more maintainer work that I don't have cycles for, but there's also a security section, that's where we get dinged on a few things, is we… we don't have an SBOM that we're publishing.
We don't have… I don't know, so there's docs on how to, like, make this go green.
And we're not currently signing our releases. So, you know, there's room for improvement here. Every OpenTelemetry pro- not every, but most OpenTelemetry projects are in the CLO monitor, and so you can compare them. Anyway, I just thought I'd bring that up if you hadn't seen it, it's somewhat interesting.
**Hanson Ho** 51:03 It's cool.
**JP Jason Plumb** 51:03 And, yeah.
And then this is interesting, too. Should have released at least one artifact in the last year. Well, okay, we've done that.
Cool.
I'll just… I'll link to it, because it's interesting to me.
We talked about it.
And so they, they, Java Core, they linked their OpenSSF scorecard But they… as a badge, but they don't link to the CLO monitor.
Okay.
And then ours… For… this thing.
Yeah, I think this is not… I think this is not claiming that we have criticals, I think it's claiming that we… Have taken measures to prevent that, or that we don't have that?
But if you scroll down, what do we get? So we're not using fuzzing, so we get dinged on that.
**Hanson Ho** 52:29 What's fuzzing?
**JP Jason Plumb** 52:31 It's like randomizing input, so anything that takes user input, sending a lot of randomized strings in it, the idea being that over time, you would catch edge cases.
Unexpected edge cases.
And then CLI… CII best practices?
I don't know what that is, but… We got dinged on that, and then… No one knows what these are.
**Hanson Ho** 52:59 I thought we have branch protection.
**JP Jason Plumb** 53:01 We do.
Yeah, I don't know why that's… that's question mark.
Maybe they're working on it, I don't know.
Honestly, I have no idea.
Alright, well, we did manage to almost fill an hour. I don't have anything else.
And if no one else does, then we can call it at that.
Right on. That's good. Alright.
Thanks again for your help, it's nice to see everyone.
Let's do it again in a week.
**Hanson Ho** 53:42 Right?
**JP Jason Plumb** 53:42 Right?
