SIG: Swift SIG
Date: 2026-09-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ben Joseph (Raintank, Inc. – Grafana Labs)** 00:54 Hi, Bryce.
**Bryce** 00:59 Hey, Ben, how you doing?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:01 Good, how are you?
**Bryce** 01:03 Oh, not bad, not bad.
**YD Yasura Dodo** 01:07 Hello.
**Bryce** 01:09 Hey!
**YD Yasura Dodo** 02:37 Oop.
Oh, we are going to release 2.6.0?
**Bryce** 02:42 For core.
**YD Yasura Dodo** 02:44 Nice.
Thank you.
**Bryce** 02:48 Yeah.
**YD Yasura Dodo** 02:49 No.
**Bryce** 02:49 it's been dragged out, so I kicked off the, the job just now, so that we can get that going.
**YD Yasura Dodo** 03:00 Nice.
Thank you so much.
**Bryce** 03:02 Yeah, you're welcome. I know you've been waiting for it.
Although the… A runner is not picking up the job to create the PR.
It's been 6 minutes, wow.
All right, let's go ahead and get started. Approver access, topics from last week for Ben and Vishwan. I talked to the other, maintainers, and they don't have a problem with it, so we just need to, create a PR that updates the… I think it updates the, code owners.
And, add you on there as the approver, so that shouldn't be a problem.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:55 Thanks, Bryce.
**Bryce** 03:56 Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:57 Do you want me to create the PRs, or…
**Bryce** 04:00 Yeah, if you don't mind.
Make it easier for us.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:04 Sure thing.
**Bryce** 04:05 Yeah, so just, update this line here, although I'm curious why that is… Oh, maybe this isn't right. Hold on now.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:15 Hmm.
**Bryce** 04:17 Here. Add it down onto this one, not the code owners.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:20 Got it.
**Bryce** 04:23 And, it'll need to be done in both Swift and, the core frameworks.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:29 Understood.
**Bryce** 04:30 Okay, cool. Groovy. And then, once that's done, I can, update the actual, like, permissions and stuff.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:38 Circle.
**Bryce** 04:40 Alright.
Okie dokie. Oh yeah, so, when are we gonna release Hotel Swift? So, I've got a PR job kicked off, for Swift Core.
And hopefully that will actually… Resolve in a minute here.
And then once we get that merged, then we… then it'll generate a… Generate a new build, so… Still not shown up, which is curious, so this might be a little bit more… effort, for some reason. It's really bizarre. I wonder if… I wonder if it has to do with, the runner that it's second. No, it should be fine. Alright, well… I wonder why that's taking so long. So hopefully that'll get out soon.
And, after this meeting, I'll do a review of where we're at with the, main repo, and if, if I think… we are good in terms of what is merged. I'll also generate a release built for that one.
**YD Yasura Dodo** 05:46 Okay, and the metrics exporters also can be… included for the, the main auto-slift REPL release.
So, I linked the metrics exporter fix, for autonom Telemetry saved to Rapo.
Oh, yeah. And… Yeah.
**Bryce** 06:13 Oh yeah, we can… I can wait for this one, if, Yeah, I think there's… there's a couple of, yeah, like, this one needs to get merged. Yeah, there's a couple of open issues that might be good to get merged in before… oh, well… We need to get… get all these merged in.
Yeah, maybe we'll clean up all of these open requests before doing release.
Of the main repo.
**YD Yasura Dodo** 06:45 Okay.
**Bryce** 06:47 I just don't… I, the… the one caveat, I think, is there's a couple of… yeah, session ones that are kind of pending. I'm… I'm… in, I wonder if, if, I think that we might not want to wait for this one.
I don't know if the, because it's kind of a chain PR, or chain change.
If it's gonna… if partially released, if it's gonna cause any problems or not.
So I'll… I'll double-check with, with, Was that Vishwan who opened that one?
But I'll, But Jim and asked Kim if that's okay to do a release without that getting merged.
Yep.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:42 Vishwan is out on vacation, so…
**Bryce** 07:45 Okay.
Well, Ben, do you know if that's gonna cause any problems if we do a release without this,
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:54 No, should be alright.
**Bryce** 08:00 Alright, cool.
And then once that drops, then we can do another release, so it's not a big deal.
**YD Yasura Dodo** 08:07 Okay. I will update the metrics exporter PR because, I need to tag the version of their core.
**Bryce** 08:15 Okay.
**YD Yasura Dodo** 08:18 Yeah, right now, it's detagging my, repo solely. I mean, like, I… I fork the repo and tagging the… the… the brand, so… revision, I don't remember, but, I need to update a package manifest… package.sitfile.
**Bryce** 08:37 Oh, I see, okay. I gotcha.
**YD Yasura Dodo** 08:41 Nope.
**Bryce** 08:43 Yeah. Okay, yeah, no problem.
Do you need, these changes to be merged? Is there PR open for these ones, or is that already…
**YD Yasura Dodo** 08:55 Sorry?
**Bryce** 08:57 So you, you say you're referencing Yes.
**YD Yasura Dodo** 09:00 Yes.
**Bryce** 09:00 Your, your, your, fork of the core, Do those ones need to get resolved in the core for this change to go through, or are they not… is that just a separate thing, like, your working copy or something?
Have you made changes in core that this PR requires, is what I'm trying to.
**YD Yasura Dodo** 09:19 Yes, yes, yes, yes. The core requires that what changes are required.
**Bryce** 09:28 But, okay, but that's this one here.
**YD Yasura Dodo** 09:30 Yes.
**Bryce** 09:31 Okay, I see.
**YD Yasura Dodo** 09:31 It's already Mars.
**Bryce** 09:33 Okay, it's already merged, we just need a release. Okay, and then you can update that, and that'll be good to go. Okay, cool.
I getcha, alright. Sorry, just taking a little while to… Understand what… where we're at. Okay, cool.
Alright, yeah, so we have the session PR still, this is the next one in the list that we'll… we'll review.
And I think that kind of It covers everything from… from last week.
So let's hop into new topics. So we have, yeah, your metric exporter bug, fixed PR.
And we have this merged. Yep, yeah, we were waiting for Nacho. I just decided to merge it because He didn't look at it, so… That's fine.
And then, yeah, and this dependency. So, we'll get that release out, and then you can update your, package.swift, and then we can get that one, merged in, but I can do a… I can review it before that happens as well, too, so… That's no problem.
Okie dokie.
Any other topics for today?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 10:49 So, I just wanted to get some feedback on, like, what is the general stance on, like, adding iOS-specific instrumentation. I was interested in adding some view tracking or navigation-related, instrumentation.
I understand, like.
it's a switch repository, but, like, we do have some IRS-specific instrumentation as well, like, say, Metricit, or… I mean.
something specific, right? Like, is that… do you think that can be part of the Swift, repo?
**Bryce** 11:23 Yeah, absolutely.
the… where I would suggest we put it is in, just the instrumentation folder here. I mean, most of… most of our existing instrumentation is kind of iOS-specific anyway, like… But, yeah, so we don't have any problem with that. It's only fairly recently that we've kind of expanded this project out, at least, conceptually, as being, like, a more broad, like, for back-end uses and stuff like that as well. So, kind of started as just focusing on iOS.
So I have no issues with adding that in there, not at all.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 12:02 Sure. That sounds great.
**Bryce** 12:19 Alright. I kinda just wanna… Get… dive into some, some… poll request reviews, which I don't really necessarily think we need to do on the call, so unless there's any other, any other topics, maybe we can just call it here, and I can, get these, or figure out why the release isn't actually releasing, and and get some of these other PRs approved and merged.
Sound good?
**YD Yasura Dodo** 12:54 Sounds good.
**Bryce** 12:55 Alright, cool. Thanks, everybody.
Have a good rest of your day.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 12:58 Thank you, guys. See you. Bye.
**YD Yasura Dodo** 13:00 I…
