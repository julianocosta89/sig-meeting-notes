SIG: Swift SIG
Date: 2026-02-26
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Vinod Vydier** 00:47 Hey, Bryce.
**Bryce Buchanan** 00:54 Hey, Vinod.
**Vinod Vydier** 00:54 Give it not happened.
So you're, you're back from.
**Bryce Buchanan** 00:58 No, I haven't gone yet.
**Vinod Vydier** 01:00 Okay, okay, okay.
Still…
**Bryce Buchanan** 01:06 It's still… still waiting.
**Vinod Vydier** 01:08 When is the due date?
**Bryce Buchanan** 01:10 It was on Monday…
**Vinod Vydier** 01:12 Oh, okay.
**Bryce Buchanan** 01:13 Yeah, so, we're a little late, but it's okay.
Oops.
Hey, Ari, m There you are.
**Ariel Demarco** 01:44 Alright, you guys?
**Bryce Buchanan** 01:46 Good.
**Ariel Demarco** 01:49 Peace.
their baby?
**Bryce Buchanan** 01:51 No, there's no baby yet. Still waiting.
**Ariel Demarco** 01:55 In the sweet wake.
**nacho** 02:02 Hello?
**Bryce Buchanan** 02:05 Hey, Nacho.
What was that? I missed what you said.
**Ariel Demarco** 02:10 Oh.
In the anxious weight.
**Bryce Buchanan** 02:13 Oh yeah, it's true.
My wife, with the last two babies, was very prompt. All of the labor started exactly on the predicted due date, and so now she's like, I feel like a failure now. So…
I have to keep her in good spirits.
She's not uncomfortable or anything, so it's not bad, but…
**Ariel Demarco** 02:38 It's a lazy baby. That's it.
**Bryce Buchanan** 02:40 Yeah. Yeah, it's true, yep. It's like, you know what, I hear what's going on out there, I'm just gonna chill in here for a little bit longer. Yeah.
**Ariel Demarco** 02:47 Exactly.
**Bryce Buchanan** 02:48 It's probably not looking forward to having two older siblings. It's never, never any good.
**Ariel Demarco** 03:02 Okay, I can talk about the last week, the injury.
**Bryce Buchanan** 03:08 Yeah.
**Ariel Demarco** 03:09 So… I did all the things to do the release.
And suddenly, the releases started failing, but…
It is weird why it's failing,
it started failing on VisionOS. I fixed VisionOS and started failing iOS, and whenever I merged everything, and it's a bit problematic because I cannot push in the release branch, I had to create a fork to the release branch.
To fix the issue.
the last thing I tried, makes that VisionOS still fails, but it's not failing because the code is wrong, because I tested locally, it's because, problems with provisioning of the simulator, TVOS simulator… VisionOS simulator, sorry. So…
there are two things we can do, I think. One of them is, like, just merge,
That's it, because we know it's not an issue on the actual thing.
That is testing.
And the other one would be, like, try to fix this.
issue. I had a way of doing it that… I don't know if it's… We're straightened out.
**Bryce Buchanan** 04:28 Oh, actually, I just had a problem similar to this,
Vision… vision? Yeah, the problem is that…
**Ariel Demarco** 04:38 If it doesn't match the name.
on the OS version, it fails, so I was planning on just making everything generic.
And that's it.
Like, grab the first… simulator you have.
**Bryce Buchanan** 04:56 Yeah.
Yeah, maybe what we should do is, like, parse the list and then grab one. That way we don't have to, yeah, don't have to,
Keep updating it, but yeah, that's…
**Ariel Demarco** 05:10 Yeah, and I found something funny, that is, sometimes we have some failing tests.
because… or some failing CI jobs, because it can find any device,
The problem is that some commands on the runners are cached.
And in particular, the one that gets simulators, so I added an XC Run
a list of simulators, so I'll… so we can… Clean that cache.
Prior to running these things.
**Bryce Buchanan** 05:42 Oh, okay.
**Ariel Demarco** 05:43 as you can see, like, it shows every single device, but it doesn't have the exact device that we are waiting for, so I would do something like you said, like, grabbing one of the
the ones that are Vision OS, or iPhone OS, or something like that, and that's it.
**Bryce Buchanan** 06:01 Yeah. Okay.
**nacho** 06:04 Yeah, that makes sense. Yeah, definitely, it…
Yeah, it's always a mess with the command line.
**Ariel Demarco** 06:12 Yeah.
**Bryce Buchanan** 06:14 Yam.
Alright, so what's this other one here?
From last week, make span context and trace state syndable. Okay.
**Ariel Demarco** 06:25 Yeah.
**nacho** 06:33 Yeah, I should review that again. Yeah, I… he… basically, he added that change to make that unsectionable.
Initially.
So, the truth was that
it was just avoiding the checks, which is not what we want, really. So, yeah, it looks like now it's sendable, really sendable, instead of check.
And checks send double, and it's… Yeah, I wish…
Yeah, I don't know if he needed to change any other uses.
Of that. Yeah, that was the one thing I didn't like at all.
Because it could crash,
But I don't know if now he had to change more things. I have not reviewed that, sorry.
I can do that, and… and…
And merch, if you think it's good.
**Bryce Buchanan** 07:32 Yeah, cool. I'll take a look at it as well, after the meeting.
Okay.
Any other topics anybody wants to add for today?
**Ariel Demarco** 07:44 Mostly to understand… sorry. Shall we…
merge the release PR and fix, in another moment, the simulator stuff, or do you want me to fix it on that specific branch?
**Bryce Buchanan** 07:58 Let's merge the release PR, and if we can, I'm not sure it'll let us, will it? With the errors? Yeah.
**Ariel Demarco** 08:05 So we do have mixed bags.
**nacho** 08:07 Yeah. Oh, because it needs an approval, right? But not because of the device.
**Bryce Buchanan** 08:11 Oh, yeah, yeah.
**nacho** 08:13 So, I mean, there are only… I think only iOS is… or iOS and macOS are…
Must pass in order to… to… to approve.
So, yeah, I think we… yeah, releasing is better, because basically it's an issue in our testing infrastructure that.
**Ariel Demarco** 08:30 Oh, he does.
**nacho** 08:31 review.
**Ariel Demarco** 08:33 It doesn't allow us to merge.
**Bryce Buchanan** 08:35 Yeah, I won't.
**Ariel Demarco** 08:36 No, because of the required status check.
**nacho** 08:39 No worries. That one?
That's… that's…
**Ariel Demarco** 08:45 Unchecks every single… M… If one of the runs on builds and tests.
He's saying?
**nacho** 08:52 Oh, really?
**Ariel Demarco** 08:52 Deep fans, yeah.
**nacho** 08:53 That was not like that in the past, right?
**Ariel Demarco** 08:57 I don't know.
**nacho** 08:58 I can remember, this was…
**Bryce Buchanan** 08:59 This was a change that I made so that we could merge the dependencies more easily without having to run all the… all the checks, but, it does kind of grab all of them and then require, like… so maybe it can be changed.
Because it just checks if any of them are failures.
**nacho** 09:18 Okay.
**Bryce Buchanan** 09:19 But maybe we can, bypass, like, set it so that we can bypass, like, VisionOS.
**nacho** 09:25 But you can… but you can… you can bypass that, right?
Bryce, as a… as a… I'm sorry.
**Bryce Buchanan** 09:32 No, I mean, not in the current state. We'd have to update the issue.
Update the, build, build process.
**Ariel Demarco** 09:44 I'll try to fix it then, and see if… everything works. I'll probably merge…
merge my VR slightly to release.
Do you guys agree with that?
**Bryce Buchanan** 09:58 Sounds good.
**Ariel Demarco** 09:59 Okay.
**nacho** 10:01 I'll do that then.
**Bryce Buchanan** 10:09 We got one other PR…
**Ariel Demarco** 10:14 This… this is a bit old.
**Bryce Buchanan** 10:16 Is Will here? I thought I saw him.
**Ariel Demarco** 10:20 Yup.
He was.
**nacho** 10:23 Good.
**Bryce Buchanan** 10:24 Okay, let's see, so…
**Vinod Vydier** 10:27 Oh yeah, he's here.
**Bryce Buchanan** 10:34 Just a minor thing. Where does it say that there's two, or…
Two, cocoa pods, there's three.
**Billy Zhou** 10:46 Yeah, let me, take care of these today. Just, by the way, like, for the Vision OS thing, was this an issue caused by the, GitHub runner just randomly changing the images that it has, or…
**Ariel Demarco** 11:01 Yeah.
**Billy Zhou** 11:02 Like, it does that every now and then.
**Ariel Demarco** 11:03 Yeah.
**Billy Zhou** 11:03 Yeah.
**Ariel Demarco** 11:05 It does change the images, and if the…
First of all, the first issue was the cache was not working, so I added something to clear that cache.
But now it's… the problem is that the OS version that it uses for Xcode, or… the Xcode version that,
doesn't have that specific device that we are requesting. That's why it's breaking now.
**Billy Zhou** 11:31 Yeah, got it.
**Ariel Demarco** 11:34 It's not difficult to fix, it's just, to be honest, I didn't have that much time after After that.
As I'm… I'm leaving next week on vacation, so, you know, bunch of stuff.
**Bryce Buchanan** 11:47 This week. Will you… will you be able to look at it today or tomorrow, Ari?
**Ariel Demarco** 11:51 Yeah, yeah, yeah, yeah, yeah, I'll do it for today tomorrow. If not, I'll let you guys know that I won't be able to.
**Bryce Buchanan** 11:58 But yeah.
**Ariel Demarco** 11:59 Ideally, I'll do it. Just wanted to know if you guys are okay for me to merge it.
directly to the branch without approval, because I'm not able to push directly to it.
**Bryce Buchanan** 12:11 Oh yeah, that's fine. I have no problem with that.
**Ariel Demarco** 12:15 Awesome.
**Bryce Buchanan** 12:15 Is this a new… this must be a new, like, security-protected thing that… that…
For… for release branches that was added, because this didn't used to be like that.
Maybe we should change our release branch naming scheme to something else, because it's not really…
We don't really treat it like a release branch, it's more of a version bumping kind of thing.
**Ariel Demarco** 12:42 Hmm.
**Bryce Buchanan** 12:46 I'm just curious, actually, let's see, bloom, blah, blah.
**Ariel Demarco** 12:52 Those are the Terraform rules.
**Bryce Buchanan** 12:55 As we have to… Or not.
Hmm… Oh, here, yum.
-Oh.
View rules… Hmm… That's interesting.
I'm not seeing that this is actually protected.
**Billy Zhou** 13:35 Are there, like, worldwide rules that could affect us?
**Bryce Buchanan** 13:43 Well, just the, I guess, the main branch here, but usually there's, like, a little thing that says protected,
for the… on the branch rules, yeah, so it's not the easy CLA, it's…
Restricting only users with bypass permission can delete matching refs, okay.
interesting. All right, well, I'll look into that a little bit more, after the meeting, because I'm a little confused by that. So, but you can't… you're not allowed to push directly to the release branch, is what you were saying? Okay.
**Ariel Demarco** 14:23 Yeah, doesn't matter if I'm internal or not, it basically doesn't allow me.
**Bryce Buchanan** 14:28 Okay.
**nacho** 14:34 It was… yeah, I thought we could merge manually, being admins before also.
**Bryce Buchanan** 14:50 Looks like there's no other new issues on this branch, or on this, repo.
Oh yeah, I think this was something I noticed, the other day, and it was reported by somebody also in the repo, that the tag was still in the repo.
And so I deleted the 2.4 tag on core, so that it,
So that the SBM would stop pulling it, because it would still… if it was cashed, it would still pull it,
Even though it was not actually, like, marked as a release in the repo.
**Ariel Demarco** 15:41 Yeah.
**Bryce Buchanan** 15:42 So, yeah, that was… an interesting thing to discover. Idiosyncrasy, I guess.
And this is… we've already looked at this one.
**Ariel Demarco** 16:07 Yeah, that's the one I had to finish. Wasn't able to. That's… that's on me.
**Bryce Buchanan** 16:12 Okay, okay.
Yeah, let's see…
Okay, I'm gonna close this one.
Because this… we have a follow-up for this one.
Swift package for auto talent.
Oh, okay, yeah, that was…
I haven't had a chance to really look… I… well, maybe I did, but I need to look at it again, I can't remember.
Okay. I don't think there's really anything else actionable at the moment here.
Any new pull requests? These just all need to get done. Has anybody had a chance to look at Swift Neo and see if that is breaking anything?
**Ariel Demarco** 17:09 I tested it locally, and it didn't break.
**Bryce Buchanan** 17:12 It didn't? Okay.
**Ariel Demarco** 17:13 No, no problem.
**Bryce Buchanan** 17:14 This is, like, one of those things where I wish I could tell it to run the build jobs.
But, oh well.
Okay.
**Ariel Demarco** 17:25 We can add an exception.
**Bryce Buchanan** 17:27 Yeah.
**Ariel Demarco** 17:29 Because the branch naming is always similar.
Because it includes the dependency.
**Bryce Buchanan** 17:34 Yeah, yum.
Okay. Well, I can also work through this.
**Vinod Vydier** 17:38 So, so these are automatic PRs?
**Bryce Buchanan** 17:41 Yeah, the Renovate bot, detects that the version changes and, opens PRs for them.
**Ariel Demarco** 17:53 And we have the rule to not run tests on…
all of them, because sadly, from one moment to another, you receive 5 PRs, and you have, like.
**Bryce Buchanan** 18:02 40 workshops running. Yeah, it takes… it takes, like, all day to merge them all, basically.
**Ariel Demarco** 18:07 Yeah.
**Bryce Buchanan** 18:10 Let's see, so what is the status of this PR? Will,
It looks like there's just still a couple of.
**Billy Zhou** 18:23 Yeah, I just have feedback.
**Bryce Buchanan** 18:25 I haven't been… been… addressed.
Okay.
**Billy Zhou** 18:29 Yeah, I can, yeah, I just had too many other things going on, I can…
Try to prioritize it this way.
**Bryce Buchanan** 18:36 Okay, no problem.
Very good.
Okay.
**nacho** 18:48 Regarding the, the send double,
Pierre, Bryce, if you're gonna take a look, I have… it looks good.
What it does now, but it hasn't moved a pair of methods in the…
In the wake. So you cannot modify that.
So I don't know if that will break something.
In the street libraries.
**Bryce Buchanan** 19:12 It hasn't moved a pair of methods? What do you mean?
**nacho** 19:17 He has removed the… yeah, because they are now in multiple, to be…
To the beginning, so it's like an immutable, and you copy everything when you create another one. So the…
Set values… the set are not.
anymore, yeah, so that… I'm not sure that will.
**Bryce Buchanan** 19:35 not break anything. Oh, I see, okay. I gotcha.
**nacho** 19:38 I don't know if we are…
**Bryce Buchanan** 19:40 Picked.
**nacho** 19:40 Yeah. Or, or if… So that could be a breaking change that…
it's not… I mean, it can be nice, but maybe we would need a… Maybe fix something.
To the users.
in March.
**Bryce Buchanan** 19:56 These are not, public, though.
Or are they all public because it's a public struct?
**nacho** 20:05 Nope.
That's true. You just need it. If they are not public, they are not used, yeah, that's true.
**Bryce Buchanan** 20:15 Okay.
**nacho** 20:18 And it has private sets, so yeah, probably it's only… It's not… non-hearting.
**Bryce Buchanan** 20:24 Yeah.
**nacho** 20:25 Yes, for you to take that into account.
**Bryce Buchanan** 20:28 I'm surprised.
**nacho** 20:29 For the rest, it looks good.
**Bryce Buchanan** 20:30 Let's see, this is on core.
So… yeah, okay.
It'd be… yeah, it'd be… we probably need to check, this against the main repo to see if there's any…
changes, or if that affects it there, if this is being used by the upstream dependency, which I don't think it should be able to if it's…
**nacho** 20:52 Yeah, it's true that it's not public, so probably it's not used anymore, and it's just… it was created like that.
Long ago, because, yeah, it made sense then.
**Bryce Buchanan** 21:04 That could change.
Okay.
**nacho** 21:10 Yes, yes, that.
**Bryce Buchanan** 21:13 Did we, did we make a, like, a nightly… Regression test… No. Yeah.
**nacho** 21:22 I… I… I… that… that was a task I had in my… In my…
my place, I tried to…
address that, but I was not able.
**Bryce Buchanan** 21:36 Oh, okay.
**nacho** 21:36 de… Yeah, because I didn't want to change the package of Swift.
But there is no way to do that without changing.
Yeah, I… I think we should…
change the package script, you know, pentelemetry script, in order to set the… the…
To set that as a global variable, so we can modify that.
Before doing. It's not… definitely is not a direct thing to do.
Or…
**Bryce Buchanan** 22:09 God.
**nacho** 22:10 Really easy.
**Bryce Buchanan** 22:11 I mean, we could just… we could just do, like, a find and replace for the version, and just set it, or, you know…
**nacho** 22:18 Yeah, yeah, yeah, something like that, that's the real need. I tried just, playing with Git.
to… to replace the Git version with another, but it… it… It never worked for me.
Okay. I did many iterations, and yeah, I just dropped that. Okay.
**Bryce Buchanan** 22:38 Bum.
**nacho** 22:39 Definitely need to change the… package.shift, I don't know if other projects do that.
**Bryce Buchanan** 22:44 Okay. Where, or how they do?
I'll, I can actually take a look at that today. I'm trying to do… because I don't know when this baby's coming, like, I'm trying to, you know, keep busy, but not take on too big of a project, so it's kind of been hard to find, small little bites of things, so this is a good thing for me to work on, so…
**nacho** 23:06 Yep, go for it, yeah.
I mean, I wouldn't go with a Git changing dependencies way, because for me, it was a…
I'm not sure.
**Bryce Buchanan** 23:18 Ram.
**nacho** 23:19 yeah, a rabbit hole that never get anywhere. And also, you must test that in a different branch in your… it's very time-consuming, and the feedback is really bad. So, yeah,
If you can go for it, it will… definitely it will be great, because it will have cut this issue that we had in the latest release.
With compatibility and breaking changes, yeah.
**Bryce Buchanan** 23:43 Yeah, I think I can come up with something, we'll see. Alright.
Alright, anything else?
**Ariel Demarco** 23:55 Nope. Do you want me to do the change so SwiftNIO runs on…
whenever we have a new PR for Swift NIO.
**Bryce Buchanan** 24:05 Sure, yeah. If you, if you.
**Ariel Demarco** 24:08 Jackson.
**Bryce Buchanan** 24:08 Ben?
**Ariel Demarco** 24:09 Yeah, it's an easy one. It should be, three liners.
**Bryce Buchanan** 24:13 Cool?
**Ariel Demarco** 24:16 Okay.
Alright, up.
**Bryce Buchanan** 24:19 Alright, have a great rest of your day, everybody.
**Ariel Demarco** 24:25 Cheers.
**Billy Zhou** 24:26 Paint price.
